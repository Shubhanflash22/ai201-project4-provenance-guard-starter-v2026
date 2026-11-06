"""
The audit log.

Every decision the service makes gets written here as one JSON object per line.
It is a file that can be read back, not `print()`.

An attack that can't be seen in a log can't be diagnosed: an input that slipped
past the detector leaves no other trace.

All nine required fields are in the entry shape from the start, even where only
some are filled. Adding fields later means early and late entries have different
shapes, and the one most worth comparing is the one from before a change.

    from audit import log_decision, read_entries

    log_decision(content_id=..., creator_id=..., guess="ai", ...)
    entries = read_entries(limit=50)
"""

import json
import threading
from datetime import datetime, timezone

import config

_lock = threading.Lock()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def log_decision(
    content_id: str,
    creator_id: str,
    guess: str | None = None,
    model_score: float | None = None,
    style_score: float | None = None,
    combined_score: float | None = None,
    label: str | None = None,
    status: str = "decided",
    **extra,
) -> dict:
    """
    Write one decision to the audit log.

        The nine required fields:

            timestamp, content_id, creator_id, guess,
            model_score, style_score, combined_score, label, status

        `status` moves over an item's life: `decided` when first judged,
        `under_review` once the writer appeals.

        Anything extra passed in gets written too, which is useful for `rejected`
        entries, where there is no decision but the trace is still wanted.
    """
    entry = {
        "timestamp": _now(),
        "content_id": content_id,
        "creator_id": creator_id,
        "guess": guess,
        "model_score": model_score,
        "style_score": style_score,
        "combined_score": combined_score,
        "label": label,
        "status": status,
    }
    entry.update(extra)
    return _append(entry)


def log_appeal(content_id: str, creator_id: str, reasoning: str) -> dict:
    """
    Record an appeal beside the original decision.

        This doesn't overwrite anything. The log is append-only, so the original
        decision stays where it was and the appeal sits after it. Someone reading
        it later can see what was decided, that it was challenged, and in what
        order.
    """
    return _append({
        "timestamp": _now(),
        "content_id": content_id,
        "creator_id": creator_id,
        "event": "appeal",
        "status": "under_review",
        "reasoning": reasoning,
    })


def log_rejection(creator_id: str, reason: str, **extra) -> dict:
    """
    Record a request that never became a decision: a rate-limit rejection or an
        input the route refused.

        An attack that shows up only as an absence is one that never gets found. A
        thousand requests that got a 429 and left no trace look exactly like a quiet
        afternoon.
    """
    return _append({
        "timestamp": _now(),
        "creator_id": creator_id,
        "event": "rejected",
        "status": "rejected",
        "reason": reason,
        **extra,
    })


def _append(entry: dict) -> dict:
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    line = json.dumps(entry, ensure_ascii=False)
    with _lock:
        with config.AUDIT_LOG.open("a", encoding="utf-8") as f:
            f.write(line + "\n")
    return entry


def read_entries(limit: int | None = None) -> list[dict]:
    """
    Read the log back, oldest first. `limit` keeps the most recent N.

    A malformed line is skipped rather than raising — a log that can't be read
    because of one bad row is worse than a log with a gap.
    """
    if not config.AUDIT_LOG.exists():
        return []

    entries = []
    for line in config.AUDIT_LOG.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entries.append(json.loads(line))
        except json.JSONDecodeError:
            continue

    return entries[-limit:] if limit else entries


def clear() -> int:
    """Wipe the log. Handy between attack runs; returns how many went."""
    count = len(read_entries())
    if config.AUDIT_LOG.exists():
        config.AUDIT_LOG.unlink()
    return count


def entries_for(content_id: str) -> list[dict]:
    """Every entry touching one content id, in order."""
    return [e for e in read_entries() if e.get("content_id") == content_id]
