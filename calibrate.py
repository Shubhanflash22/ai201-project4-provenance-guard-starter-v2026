"""Print both signals and the combined score for four calibration inputs."""
import detector
import scoring
import stylometry

INPUTS = {
    "clearly AI": (
        "The implementation of the proposed framework requires careful "
        "consideration of several key factors. First, it is important to note "
        "that the system must be able to handle a wide variety of different "
        "inputs. Additionally, the overall performance of the solution depends "
        "on a number of important variables."
    ),
    "clearly human": (
        "Honestly I burned the toast again this morning, set off the smoke "
        "alarm, and my cat bolted under the couch like I had committed a "
        "crime. Third time this week. Not great."
    ),
    # REPLACE this with a plain paragraph YOU wrote: short sentences, simple words.
    "plain human": (
        "I like my school. It is big. I have many friends. We play games at "
        "lunch. My teacher is nice. She helps me a lot. I want to go to college."
    ),
    "lightly-edited AI": (
        "The implementation of the proposed framework requires careful "
        "considration of several key factors. First, it is important to note "
        "that the system must handle a wide variety of inputs. Additionally, "
        "overall performance depends on a number of variables. Which matters."
    ),
}

print(f"{'input':<20}{'model':>8}{'style':>8}{'combined':>10}  guess")
for name, text in INPUTS.items():
    m = detector.model_signal(text)
    s = stylometry.style_signal(text)
    c = scoring.combine_signals(m, s)
    guess, _ = scoring.score_to_label(c)
    print(f"{name:<20}{m:>8.3f}{s:>8.3f}{c:>10.3f}  {guess}")