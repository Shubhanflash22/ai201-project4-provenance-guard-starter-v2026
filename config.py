"""
Settings for Provenance Guard.
"""

import os
from pathlib import Path

ROOT = Path(__file__).parent


# ─── The service ─────────────────────────────────────────────────────────────

# 127.0.0.1 is loopback: only this machine can reach it. A host elsewhere needs
# 0.0.0.0, which is set through the HOST env var.
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "5000"))

# Flask's debug mode exposes an interactive Python prompt, so it turns itself
# off whenever HOST is not loopback.
DEBUG = os.getenv("AI201_DEBUG", "1") == "1" and HOST in ("127.0.0.1", "localhost")


# ─── The local model ─────────────────────────────────────────────────────────
# The first signal runs a language model locally (no account or key). It
# downloads about 550 MB the first time. It measures how predictable the text
# is to a language model, since text a model finds easy to predict tends to be
# text a model wrote. The first call takes ten to twenty seconds while the model
# loads; after that it stays in memory.

DETECTOR_MODEL = os.getenv("AI201_DETECTOR_MODEL", "gpt2")

# Longer text gives a steadier reading but takes longer. 400 tokens is roughly
# 300 words.
DETECTOR_MAX_TOKENS = 400


# ─── Scoring ─────────────────────────────────────────────────────────────────
# How much each signal counts toward the combined score.

WEIGHT_MODEL_SIGNAL = 0.4
WEIGHT_STYLE_SIGNAL = 0.4
WEIGHT_PHRASE_SIGNAL = 0.2

# Disagreement guard: if the two signals differ by more than this gap, the
# combined score is pulled toward 0.5 ("unsure"). PULL is the fraction of its
# distance from 0.5 that the score keeps (0.5 = pull it halfway back).
DISAGREEMENT_GAP = 0.40
DISAGREEMENT_PULL = 0.5


# ─── Thresholds ──────────────────────────────────────────────────────────────
# Where one label becomes another. Scores run 0.0 (confidently human) to 1.0
# (confidently AI).
#
#   score < HUMAN_THRESHOLD          -> high-confidence human
#   between the two                  -> unsure
#   score > AI_THRESHOLD             -> high-confidence AI
#
# Widening the unsure band means fewer wrong accusations and more AI text
# getting through.

HUMAN_THRESHOLD = 0.35
AI_THRESHOLD = 0.75

# Text with fewer letters than this never reaches the signals.
MIN_LETTERS = 10


# ─── Rate limiting ───────────────────────────────────────────────────────────
# Limits are keyed by creator_id (see app.py), falling back to the caller's address.
RATE_LIMITING_ENABLED = True

RATE_LIMIT_PER_MINUTE = 10
RATE_LIMIT_PER_DAY = 120

# In-memory storage suits one laptop. A restart forgets every count, and two
# copies of the service would not share limits.
RATE_LIMIT_STORAGE = "memory://"


# ─── Paths ───────────────────────────────────────────────────────────────────

LOG_DIR = ROOT / "logs"
AUDIT_LOG = LOG_DIR / "audit.jsonl"
RESULTS_DIR = ROOT / "results"
