#!/usr/bin/env python3
"""
Provenance Guard: the web service.

    python app.py

Routes:

    POST /ping            example route, used as a control to check the service is up
    POST /submit          score a piece of text, log the decision, return the result
    POST /appeal          record a writer's appeal and mark the item under_review
    GET  /content/<id>    one item's current status
    GET  /log             the audit log
    GET  /health          is the service up, and is the model loaded
"""

import uuid

from flask import Flask, jsonify, request

import audit
import config
import detector
import phrases
import scoring
import stylometry

app = Flask(__name__)


# ── Rate limiting ─────────────────────────────────────────────────────────────
# Controlled by RATE_LIMITING_ENABLED in config.py. While it is off, the
# @limiter.limit(...) decorator on /submit is a no-op.

class _LimiterOff:
    """Stands in for the real limiter while rate limiting is off."""

    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()
if config.RATE_LIMITING_ENABLED:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        """
        Who a request counts against: the creator_id if one was sent,
        otherwise the caller's address.
        """
        payload = request.get_json(silent=True)
        # A body that is valid JSON but not an object (a bare list or string)
        # has no .get, so fall back to the address instead of raising.
        if not isinstance(payload, dict):
            return get_remote_address()
        creator = payload.get("creator_id")
        return creator if isinstance(creator, str) and creator.strip() else get_remote_address()

    limiter = Limiter(
        key_func=rate_limit_key,
        app=app,
        storage_uri=config.RATE_LIMIT_STORAGE,
        default_limits=[],
    )

    @app.errorhandler(429)
    def rate_limited(exc):
        """A rejected request still leaves an audit entry."""
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            payload = {}
        audit.log_rejection(
            creator_id=payload.get("creator_id", "unknown"),
            reason="rate_limited",
            limit=str(exc.description),
        )
        return jsonify({
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly.",
            "limit": str(exc.description),
        }), 429


# ── Control route ─────────────────────────────────────────────────────────────

@app.post("/ping")
def ping():
    """Echo route. If this answers, the service itself is up."""
    payload = request.get_json(silent=True) or {}
    return jsonify({
        "ok": True,
        "you_sent": payload.get("message"),
        "service": "provenance-guard",
    })


@app.get("/health")
def health():
    """Is the service up, and has the model been downloaded yet?"""
    import detector

    loaded = detector._model is not None
    return jsonify({
        "ok": True,
        "detector_model": config.DETECTOR_MODEL,
        "detector_loaded": loaded,
        "rate_limiting": config.RATE_LIMITING_ENABLED,
        "log_entries": len(audit.read_entries()),
    })


# ── Submit ────────────────────────────────────────────────────────────────────

@app.post("/submit")
@limiter.limit(f"{config.RATE_LIMIT_PER_MINUTE}/minute;{config.RATE_LIMIT_PER_DAY}/day")
def submit():
    """
    Take a piece of text, decide about it, log the decision, answer.

    Expects JSON: {"text": "...", "creator_id": "..."}

    Returns content_id, guess, confidence, label, and all three signal scores
    (model_score, style_score, phrase_score). Bad input gets a 400, an
    unavailable detector a 503.
    """
    content_id = str(uuid.uuid4())

    # Read the request and check it.
    MAX_TEXT_CHARS = 10_000  # matches criterion 5 in criteria.md

    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        audit.log_rejection(creator_id="unknown", reason="body_not_json_object")
        return jsonify({
            "error": "invalid_input",
            "message": "Send a JSON object with 'text' and 'creator_id'.",
        }), 400
    text = payload.get("text")
    creator_id = payload.get("creator_id")
    who = creator_id if isinstance(creator_id, str) and creator_id.strip() else "unknown"

    if not isinstance(text, str) or not text.strip():
        audit.log_rejection(creator_id=who, reason="text_missing_or_empty")
        return jsonify({
            "error": "invalid_input",
            "message": "Please enter some text.",
        }), 400
    if len(text) > MAX_TEXT_CHARS:
        audit.log_rejection(creator_id=who, reason="text_too_long", length=len(text))
        return jsonify({
            "error": "invalid_input",
            "message": f"Text is too long (limit {MAX_TEXT_CHARS} characters).",
        }), 400
    if not isinstance(creator_id, str) or not creator_id.strip():
        audit.log_rejection(creator_id="unknown", reason="creator_id_missing")
        return jsonify({
            "error": "invalid_input",
            "message": "creator_id is required.",
        }), 400

    letters = sum(ch.isalpha() for ch in text)
    if letters < config.MIN_LETTERS:
        audit.log_rejection(creator_id=who, reason="too_few_letters", letters=letters)
        return jsonify({
            "error": "invalid_input",
            "message": "Please enter some text with words in it.",
        }), 400
    # Signal one: the model signal.
    try:
        model_score = detector.model_signal(text)
    except ValueError as exc:
        # text too short for the model to score
        audit.log_rejection(creator_id=creator_id, reason="text_too_short")
        return jsonify({"error": "invalid_input", "message": str(exc)}), 400
    except detector.DetectorUnavailable:
        audit.log_rejection(creator_id=creator_id, reason="detector_unavailable")
        return jsonify({
            "error": "detector_unavailable",
            "message": "The detector model could not be loaded.",
        }), 503

    # Signals two and three, then combine.
    style_score = stylometry.style_signal(text)
    phrase_score = phrases.phrase_signal(text)
    combined = scoring.combine_signals(model_score, style_score, phrase_score)

    guess, label = scoring.score_to_label(combined)

    audit.log_decision(
        content_id=content_id,
        creator_id=creator_id,
        guess=guess,
        model_score=model_score,
        style_score=style_score,
        phrase_score=phrase_score,
        combined_score=combined,
        label=label,
        status="decided",
    )

    return jsonify({
        "content_id": content_id,
        "guess": guess,
        "confidence": combined,
        "label": label,
        "model_score": model_score,
        "style_score": style_score,
        "phrase_score": phrase_score,
    })


@app.post("/appeal")
def appeal():
    """
    A writer says the guess was wrong.

    Expects JSON: {"content_id": "...", "reasoning": "..."}
    Checks the content_id exists, records the appeal (status becomes
    under_review) and confirms to the writer.
    """
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({
            "error": "invalid_input",
            "message": "Send a JSON object with 'content_id' and 'reasoning'.",
        }), 400

    content_id = payload.get("content_id")
    reasoning = payload.get("reasoning")

    if not isinstance(content_id, str) or not content_id.strip():
        return jsonify({
            "error": "invalid_input",
            "message": "content_id is required.",
        }), 400
    if not isinstance(reasoning, str) or not reasoning.strip():
        return jsonify({
            "error": "invalid_input",
            "message": "Please tell us why you think this was wrong.",
        }), 400

    # The id must exist.
    entries = audit.entries_for(content_id)
    if not entries:
        return jsonify({
            "error": "not_found",
            "message": "We couldn't find a submission with that content_id.",
        }), 404

    audit.log_appeal(
        content_id=content_id,
        creator_id=entries[0].get("creator_id"),
        reasoning=reasoning.strip(),
    )

    return jsonify({
        "content_id": content_id,
        "status": "under_review",
        "message": "Your appeal has been recorded and this item is marked for review by a person.",
    })


@app.get("/content/<content_id>")
def get_content(content_id):
    """One item's current status: the decision, and whether it was appealed."""
    entries = audit.entries_for(content_id)
    if not entries:
        return jsonify({
            "error": "not_found",
            "message": "We couldn't find a submission with that content_id.",
        }), 404

    decision = entries[0]
    latest = entries[-1]
    return jsonify({
        "content_id": content_id,
        "status": latest.get("status"),
        "guess": decision.get("guess"),
        "confidence": decision.get("combined_score"),
        "label": decision.get("label"),
        "appealed": any(e.get("event") == "appeal" for e in entries),
    })


# ── Audit log ───────────────────────────────────────────────────────────────

@app.get("/log")
def get_log():
    """The audit log, most recent last. Optional ?limit=N."""
    limit = request.args.get("limit", type=int)
    entries = audit.read_entries(limit=limit)
    return jsonify({"count": len(entries), "entries": entries})


def main():
    print(f"Provenance Guard on http://{config.HOST}:{config.PORT}")
    print(f"  detector model:  {config.DETECTOR_MODEL}")
    print(f"  rate limiting:   {'ON' if config.RATE_LIMITING_ENABLED else 'off (unit 8)'}")
    print(f"  audit log:       {config.AUDIT_LOG}")
    print()
    print("Check it's alive:")
    print(f'  curl -X POST http://{config.HOST}:{config.PORT}/ping \\')
    print('    -H "Content-Type: application/json" \\')
    print("    -d '{\"message\": \"hello\"}'")
    print()
    # debug is local-only, see config.py
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)


if __name__ == "__main__":
    main()
