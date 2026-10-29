# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->
Route (/submit in app.py) receives a POST request with JSON (text and creator_id) and adds a unique content_id for this submission.
Input check receives the raw JSON and adds a yes/no on whether text is usable (present, not empty, not enormous). If it says no, nothing else runs, and the service jumps to the final response with a 400 and “please enter some text”.
Signal one (detector.py, the model signal) receives the text and adds a score from 0 to 1 for how predictable it is to a language model. Higher means more AI-like.
Signal two (stylometry.py, the style signal) receives the same text and adds a score from 0 to 1 for its shape, which is sentence-length variety, word variety and punctuation. Higher means more AI-like.
Combine (scoring.py::combine_signals) receives the two scores and adds one combined score from 0 (confidently human) to 1 (confidently AI).
Label (scoring.py::score_to_label) receives the combined score and adds two things: a short guess (ai, human or unsure) and a plain-English sentence a reader sees.
Log (audit.py) receives content_id, creator_id, the guess, both signal scores, the combined score, the label and the status. It adds one permanent line in logs/audit.jsonl, so the decision can be reconstructed later and an appeal can find it.
Response receives all of the above and adds the JSON the caller sees: content_id, guess, confidence, label, model_score and style_score.



---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**

**Why that might differ between human and AI writing:**

**What it can't see:**

**What it measures:** How predictable the text is to a language model (gpt2 running on my own machine). The model’s surprise is called perplexity. Low perplexity (easy to predict) becomes a high score, and the score runs from 0 (human-like) to 1 (AI-like).

**Why that might differ between human and AI writing:** An AI writes by repeatedly choosing a likely next word, so its text tends to be easy for another model to predict. Human writing wanders more, with unusual word choices, abrupt turns and specific details that a model doesn’t expect.

**What it can't see:** The difference between predictable and AI-written. A person writing plainly with common words in short sentences can score as “AI” as strongly as real AI does. That includes a second-language writer sticking to safe vocabulary, a younger writer, and anyone writing simply on purpose. The reverse also happens: dense, ornate human prose full of rare words can score as human even when a model wrote it. It also reads only the first 400 tokens (about 300 words), so anything later in a long submission is invisible to it.

### Signal two — the style signal

**What it measures:**

**Why that might differ between human and AI writing:**

**What it can't see:**

**What it measures:**The shape of the text, without understanding any of it. It combines three things into one 0–1 score: how much sentence length varies, how much of the vocabulary repeats (unique words divided by total words), and how much punctuation there is and how varied it is. Higher means more AI-like.

**Why that might differ between human and AI writing:** AI text tends toward even, mid-length sentences and a narrower, more repetitive vocabulary. Human writing is lumpier, with a three-word sentence next to a forty-word one, and more variety in punctuation such as dashes and semicolons.

**What it can't see:** Meaning. It has no idea what the text says, so anything that changes the shape without changing the substance fools it. Someone can add typos (which look like extra vocabulary variety), chop long sentences into uneven pieces, or paste in a quotation, and AI text starts to look human. In the other direction, a real writer who naturally writes in even, regular sentences can be wrongly pushed toward AI. Very short texts also give it too little to measure, and vocabulary variety falls as text gets longer, so text length alone can distort the score.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**

**The numbers:**

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

### The combining rule

**The rule:** Start with a plain average of the two signals, so each one counts equally. Then check whether the two signals strongly disagree. If they differ by more than 0.40, don't trust the average. Pull it halfway back toward 0.5, which means "unsure". Two methods disagreeing is itself a sign we don't know, and a wrong accusation costs a real writer far more than a missed AI text costs the site.

**The numbers:**
- combined = 0.5 × model_score + 0.5 × style_score (weights in `config.py`)
- Disagreement guard: if |model_score − style_score| > 0.40, then
  combined = 0.5 + (combined − 0.5) × 0.5
- Labels use the thresholds in `config.py`: below 0.35 is high-confidence human, 0.35 to 0.65 is unsure, above 0.65 is high-confidence AI.
- These values are a first draft and will be checked against my four calibration inputs in Milestone 4.

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:**
**A case where my two signals split, and what my rule does with it:**
I wrote a text that keeps AI-style wording but changes its shape: one very short sentence, then one very long, comma-heavy sentence, then another short one ("Short answer: yes. The implementation of the proposed framework requires careful consideration..."). Signal one scored it 0.7773 because the words are very predictable. Signal two scored it 0.1787 because the sentence lengths and punctuation look human. The gap is 0.60, over my 0.40 limit, so the guard fired: the plain average of 0.478 became 0.489, which is "unsure". The label would have been "unsure" even without the guard, so here it only nudged the score by 0.011. The guard matters most when the signals split and the average lands far from the middle.

**Where the rule does not help:** when both signals agree and are both wrong. A plainly written paragraph I wrote in short sentences scored 0.83 and 0.71 (combined 0.77, "ai"), and 6 of my 13 GRE practice essays came back "ai" (combined 0.57 to 0.75, none "human") because both signals read formal, evenly paced writing as machine-like. The gap in those cases was under 0.20, so the guard never fired. I haven't changed the weights for this, because these essays are the test set for my false-positive criterion in the next unit.

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human |  |  |
| unsure |  |  |
| high-confidence AI |  |  |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```

```json

```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
