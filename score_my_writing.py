"""
Score every essay in my_writing.txt with both signals and count how many get
the high-confidence AI label. Needs no server: run it from the repo folder.

    python score_my_writing.py
"""
from pathlib import Path

import detector
import scoring
import stylometry

raw = Path("my_writing.txt").read_text(encoding="utf-8")
essays = [e.strip() for e in raw.split("\n=====\n") if e.strip()]

print(f"{'#':>3}{'words':>7}{'model':>8}{'style':>8}{'combined':>10}  guess")
flagged = 0
for i, text in enumerate(essays, 1):
    m = detector.model_signal(text)
    s = stylometry.style_signal(text)
    c = scoring.combine_signals(m, s)
    guess, _ = scoring.score_to_label(c)
    flagged += guess == "ai"
    print(f"{i:>3}{len(text.split()):>7}{m:>8.3f}{s:>8.3f}{c:>10.3f}  {guess}")

print(f"\n{flagged} of {len(essays)} labeled high-confidence AI")
