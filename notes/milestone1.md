## Part 3: The false-positive trace

A writer, Maya, writes an essay herself in short sentences with simple, common words, and submits it through `POST /submit` with her `creator_id`.

- **Signal one** finds her text very predictable to gpt2 and scores it high, about 0.85.
- **Signal two** sees even sentence lengths and a narrow vocabulary and scores it about 0.70.
- **Combined score:** about 0.78, above the 0.65 threshold, so the service returns guess `ai`.
- **What the label says to her:** the high-confidence AI sentence, telling her we think this was probably written by an AI.
- **What she can do:** send her `content_id` and her reasoning to `POST /appeal`. The item moves to `under_review` and the appeal is logged next to the original decision. Nothing re-checks it automatically, so it depends on a person looking at it.

(The scores are illustrative. I'll replace them with real numbers from my calibration inputs in Milestone 4.)

This is the case that decides my thresholds. A wrong accusation costs the writer far more than a missed AI text costs the site, so I want the AI label to need a high score, and I'd rather widen the "unsure" band than accuse someone.

## Part 4: Endpoint shapes

### POST /submit
**In:** `{"text": "...", "creator_id": "..."}`
- `text`: string, required, not empty or whitespace-only, at most 10,000 characters
- `creator_id`: string, required, not empty

**Out, 200:**
`{"content_id": "...", "guess": "ai | human | unsure", "confidence": 0.0-1.0, "label": "full sentence", "model_score": 0.0-1.0, "style_score": 0.0-1.0}`
- `confidence` is the combined score (higher means more likely AI)

**Out, 400:** `{"error": "invalid_input", "message": "..."}` when `text` or `creator_id` is missing, empty, wrong type, or `text` is too long.
**Out, 503:** `{"error": "detector_unavailable", "message": "..."}` when the model can't load.

### POST /appeal
**In:** `{"content_id": "...", "reasoning": "..."}`, both required, non-empty strings

**Out, 200:** `{"content_id": "...", "status": "under_review", "message": "Your appeal has been recorded."}`
**Out, 400:** `content_id` or `reasoning` is missing or empty.
**Out, 404:** the `content_id` doesn't exist in the log.