"""
Signal three: stock formal phrases.

Counts how often the text uses phrases that formulaic (and often AI) writing
leans on. Scores run 0.5 to 1.0 (higher = more AI-like). No phrases found
gives 0.5, "no opinion", because plenty of AI text avoids these phrases, so
this signal can add suspicion but never clears anyone.
"""

import re

PHRASES = [
    "it is important to note", "it is worth noting", "in conclusion",
    "in summary", "furthermore", "moreover", "additionally", "overall,",
    "ultimately", "plays a crucial role", "a wide variety of", "a number of",
    "key factors", "careful consideration", "it is essential",
    "first and foremost", "serves as a", "a testament to", "in today's",
    "delve", "landscape", "on the other hand", "in the realm of", "navigate",
]

PER_100_WORDS_FOR_MAX = 2.0  # this many phrases per 100 words = full score


def phrase_signal(text: str) -> float:
    """The phrase signal as a score from 0.5 to 1.0. Higher = more AI-like."""
    n_words = len(re.findall(r"[a-z0-9']+", text.lower()))
    if n_words < 3:
        return 0.5
    lowered = text.lower()
    hits = sum(lowered.count(p) for p in PHRASES)
    per_100 = hits * 100 / n_words
    return round(0.5 + 0.5 * min(1.0, per_100 / PER_100_WORDS_FOR_MAX), 4)


if __name__ == "__main__":
    import sys

    sample = " ".join(sys.argv[1:])
    print(f"phrase_signal   {phrase_signal(sample)}   (higher = more likely AI)")