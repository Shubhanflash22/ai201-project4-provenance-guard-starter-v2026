"""
Turning three numbers into one, and one number into something a person can
read.

`combine_signals` is where the false-positive decision actually gets made.
Everything downstream of it (the labels, the appeal path) depends on a number
this function produced.

`score_to_label` is where the output stops being for a machine and starts being
for a person. A score of 0.62 means nothing to a writer.

The combining rule lives in `scoring.py::combine_signals`.
"""

import config


def combine_signals(
    model_score: float, style_score: float, phrase_score: float = 0.5
) -> float:
    """
    Combine three 0-1 signals into one 0-1 score. Higher = more likely AI.

    The rule:
      1. Weighted average (weights in config.py: 0.4 model, 0.4 style, 0.2 phrase).
         The phrase signal gets the smallest weight because it only runs from
         0.5 to 1.0 (it can add suspicion but never clears anyone), is easy to
         evade by deleting stock phrases, and formal human writers use them too.
      2. Disagreement guard: if signals one and two differ by more than
         config.DISAGREEMENT_GAP, the average is pulled back toward 0.5.
         The guard ignores the phrase signal because it can't go below 0.5.

    Returns:
        A float from 0.0 (confidently human) to 1.0 (confidently AI).
    """
    average = (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
        + config.WEIGHT_PHRASE_SIGNAL * phrase_score
    )
    if abs(model_score - style_score) > config.DISAGREEMENT_GAP:
        average = 0.5 + (average - 0.5) * config.DISAGREEMENT_PULL
    return round(min(max(average, 0.0), 1.0), 4)


LABELS = {
    "human": "We think this was probably written by a person.",
    "unsure": (
        "We couldn't tell whether this was written by a person or by AI. "
        "That isn't a finding against you, and nothing happens to your work "
        "because of it. If you'd like a person to look at it, you can request "
        "a review."
    ),
    "ai": (
        "Our automated check thinks this may have been written with AI. It "
        "can be wrong, especially for writers who use short, plain sentences "
        "or a formal style. If you wrote it yourself, you can appeal and it "
        "will be marked for review by a person."
    ),
}
def score_to_label(score: float) -> tuple[str, str]:
    """
    Turn a score into a guess and the text a reader actually sees.

        Returns:
            (guess, label_text), where `guess` is a short machine-readable string
            ("ai" / "human" / "unsure") and `label_text` is the full sentence shown
            to a person.

        The label text is written for someone who has never heard the word
        "threshold": not "human, 0.81 confidence" but "We think this was probably
        written by a person."

        All three labels are reachable: thresholds are in config.py. "Unsure" is the
        hardest to write, because it has to admit uncertainty without sounding like
        an accusation, since the person reading it may well have written every word
        themselves.
    """
    if score >= config.AI_THRESHOLD:
        return "ai", LABELS["ai"]
    if score <= config.HUMAN_THRESHOLD:
        return "human", LABELS["human"]
    return "unsure", LABELS["unsure"]


def label_ranges() -> list[tuple[str, str]]:
    """
    The score range each label covers, taken from config.py so the numbers can't
        drift apart from it.
    """
    return [
        ("high-confidence human", f"0.00 – {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} – {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} – 1.00"),
    ]
