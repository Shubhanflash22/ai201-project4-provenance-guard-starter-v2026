"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics
TTR_WINDOW = 100  # only look at the first 100 words so long texts aren't penalized


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

# def sentence_length_spread(text: str) -> float:
#     """
#     How much sentence length varies. ← TODO

#     Returns:
#         A float. Decide yourself what scale it's on and which direction means
#         "more human" — then write that down, because your combining rule
#         depends on knowing it.

#     A hint on what you're reaching for: the standard deviation of sentence
#     lengths, probably divided by the mean so a long text and a short one are
#     comparable. `statistics.stdev` is imported for you.

#     Watch the edge case: a one-sentence submission has no spread at all, and
#     `stdev` raises on fewer than two values. Decide what that should return
#     before the attack set decides for you.
#     """
#     # TODO: replace this
#     return 0.0


# def type_token_ratio(text: str) -> float:
#     """
#     Unique words over total words. ← TODO

#     Returns:
#         A float between 0 and 1. Higher means more varied vocabulary.

#     Worth knowing before you rely on it: this measure falls as text gets
#     longer, because common words repeat. Two texts of different lengths aren't
#     directly comparable on it, and if your test inputs vary a lot in length,
#     that alone can look like a signal.
#     """
#     # TODO: replace this
#     return 0.0


# def punctuation_density(text: str) -> float:
#     """
#     How much punctuation, relative to length. ← TODO

#     Returns:
#         A float. Whether you count all punctuation or only some kinds — commas,
#         semicolons, dashes — is a real choice. Semicolons and em dashes are
#         more interesting than full stops, because they vary more between
#         writers.
#     """
#     # TODO: replace this
#     return 0.0

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies: standard deviation divided by the mean.
    Higher = more varied = more human. 0.0 if there are fewer than 2 sentences.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    return round(statistics.stdev(lengths) / mean, 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words / total words, on the first TTR_WINDOW words only.
    Higher = more varied vocabulary = more human.
    """
    w = words(text)[:TTR_WINDOW]
    if not w:
        return 0.0
    return round(len(set(w)) / len(w), 4)


def punctuation_density(text: str) -> float:
    """
    Commas, semicolons, colons, dashes, brackets, ! and ? per word.
    Full stops are left out because every text has them.
    Higher = more punctuation variety = more human.
    """
    w = words(text)
    if not w:
        return 0.0
    marks = re.findall(r"[,;:!?()\u2014\u2013-]", text)
    return round(len(marks) / len(w), 4)

# ── Combining them ───────────────────────────────────────────────────────────

def _scale(value: float, lo: float, hi: float) -> float:
    """Stretch value onto 0-1, where lo -> 0 and hi -> 1, clamped at both ends."""
    if hi == lo:
        return 0.0
    return min(max((value - lo) / (hi - lo), 0.0), 1.0)


def style_signal(text: str) -> float:
    """
    The style signal as a 0-1 score. Higher = more likely AI.

    Each measure is scaled to a 0-1 "how human does this look" score, then
    weighted: spread 0.4, vocabulary variety 0.3, punctuation 0.3.
    The result is flipped so that high means AI-like.
    """
    if len(words(text)) < 3:
        return 0.5  # too little text to measure: no opinion

    spread = _scale(sentence_length_spread(text), 0.15, 0.80)
    variety = _scale(type_token_ratio(text), 0.55, 0.90)
    punct = _scale(punctuation_density(text), 0.0, 0.10)

    humanness = 0.4 * spread + 0.3 * variety + 0.3 * punct
    return round(1.0 - humanness, 4)

# def style_signal(text: str) -> float:
#     """
#     The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

#     Combine your three measures into one number. Same direction as
#     `detector.model_signal`, so that `scoring.combine_signals` can treat them
#     the same way — if one of your signals runs backwards, everything above it
#     is wrong in a way that's hard to see.

#     Two things to decide and write down:

#       1. Which direction each measure points. Low spread means more AI-ish, so
#          it needs flipping. Work out which of your three need that.
#       2. How to get each onto a comparable scale. A raw type-token ratio sits
#          between 0 and 1; a raw punctuation count doesn't. Adding them
#          unscaled means whichever has the bigger numbers wins by default.

#     Test it on the four calibration inputs from Milestone 4 — clearly AI,
#     clearly human, plain conventional human writing, lightly-edited AI — before
#     you trust it. Plain and ordinary, not formal: formal prose reads as *human*
#     to signal one, and it is plain writing that gets accused.
#     """
#     # TODO: replace this
#     return 0.5


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
