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
Signal three (phrases.py, the phrase signal) receives the same text and adds a score from 0.5 to 1.0 for how many stock formal phrases it uses
<!-- Combine (scoring.py::combine_signals) receives the two scores and adds one combined score from 0 (confidently human) to 1 (confidently AI). -->
Combine (scoring.py::combine_signals) receives the three scores and adds one combined score from 0 (confidently human) to 1 (confidently AI).
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

### Signal three — the phrase signal (stretch)

**What it measures:** How often the text uses stock formal phrases such as "it is important to note", "furthermore", "a wide variety of" and "plays a crucial role" (24 phrases, listed in `phrases.py`). Phrases per 100 words are turned into a score from 0.5 to 1.0. Finding no stock phrases gives 0.5, meaning "no opinion".

**Why that might differ between human and AI writing:** AI-style text leans on the same transition and filler phrases again and again. It measures which phrases are used, not how predictable the text is (signal one) or how it is shaped (signal two).

**What it can't see:** It can only add suspicion, never clear anyone, because plenty of AI text avoids these phrases. Anyone can defeat it by deleting them, and formal human writers use "furthermore" and "moreover" naturally. It also finds nothing in plain AI text that avoids stock phrases.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**

**The numbers:**

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

<!-- **A case where my two signals split, and what my rule does with it:**

**The rule:** Start with a plain average of the two signals, so each one counts equally. Then check whether the two signals strongly disagree. If they differ by more than 0.40, don't trust the average. Pull it halfway back toward 0.5, which means "unsure". Two methods disagreeing is itself a sign we don't know, and a wrong accusation costs a real writer far more than a missed AI text costs the site.

**The numbers:**
- combined = 0.5 × model_score + 0.5 × style_score (weights in `config.py`)
- Disagreement guard: if |model_score − style_score| > 0.40, then
  combined = 0.5 + (combined − 0.5) × 0.5
- Labels use the thresholds in `config.py`: below 0.35 is high-confidence human, 0.35 to 0.65 is unsure, above 0.65 is high-confidence AI.
- These values are a first draft and will be checked against my four calibration inputs in Milestone 4. -->

**The rule:** Take a weighted average of the three signals. Then check whether signals one and two strongly disagree. If they differ by more than 0.40, don't trust the average and pull it halfway back toward 0.5, which means "unsure". The guard ignores signal three because it can never go below 0.5. A wrong accusation costs a real writer far more than a missed AI text costs the site.

**The numbers:**
- combined = 0.4 × model_score + 0.4 × style_score + 0.2 × phrase_score (weights in `config.py`)
- Disagreement guard: if |model_score − style_score| > 0.40, then combined = 0.5 + (combined − 0.5) × 0.5
- Labels use the thresholds in `config.py`: 0.35 and below is high-confidence human, 0.35 to 0.65 is unsure, 0.65 and above is high-confidence AI.

**How I weighted the three signals (stretch):** Signals one and two get equal weight (0.4 each) because I had no evidence either one is more reliable: on my 13 essays they leaned the same way. Signal three gets the smallest weight (0.2) for three reasons: it only runs from 0.5 to 1.0 so it can't clear anyone, it is easy to evade by deleting stock phrases, and formal human writers like me use them too. Adding it changed my 13 essays from 6 labeled "ai" to 4, but I don't read that as the phrase signal being smart. Part of it is dilution, because a neutral 0.5 baseline pulls every score a little toward the middle. It also nudged my toast paragraph from 0.2685 to 0.3148, closer to the AI side. It did not fix the main problem: none of my 13 real essays was labeled "human".

**Where it lives:** `scoring.py::combine_signals`

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

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.35 | We think this was probably written by a person. |
| unsure | 0.35 – 0.65 | We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review. |
| high-confidence AI | 0.65 – 1.00 | Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person. |

**Why I worded the "unsure" one this way:** It says plainly that the system doesn't know, and it says outright that this isn't an accusation, because the person reading it may have written every word. It gives one concrete next step, a review, so the writer isn't left stuck. I avoided words like "confidence" and "score", since a reader doesn't know what they mean. This label matters most in practice: 7 of my 13 real essays received it.

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
**A submission**

```bash
$ curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d '{\"text\": \"The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must be able to handle a wide variety of different inputs. Additionally, the overall performance of the solution depends on a number of important variables.\", \"creator_id\": \"shubhan\"}'
```

```json
{
  "confidence": 0.8068,
  "content_id": "2d300911-db98-41cd-a676-b579ad60ffe2",
  "guess": "ai",
  "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
  "model_score": 0.8864,
  "phrase_score": 1.0,
  "style_score": 0.6306
}
```

**An appeal**

```bash
$ curl.exe -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d "@appeal.json"
```

(`appeal.json` contained: `{"content_id": "2d300911-db98-41cd-a676-b579ad60ffe2", "reasoning": "I wrote this myself as part of a practice essay."}`)

```json
{
  "content_id": "2d300911-db98-41cd-a676-b579ad60ffe2",
  "message": "Your appeal has been recorded and this item is marked for review by a person.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl.exe "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.8068,
      "content_id": "2d300911-db98-41cd-a676-b579ad60ffe2",
      "creator_id": "shubhan",
      "guess": "ai",
      "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
      "model_score": 0.8864,
      "phrase_score": 1.0,
      "status": "decided",
      "style_score": 0.6306,
      "timestamp": "2026-10-31T19:14:53+00:00"
    },
    {
      "content_id": "2d300911-db98-41cd-a676-b579ad60ffe2",
      "creator_id": "shubhan",
      "event": "appeal",
      "reasoning": "I wrote this myself as part of a practice essay.",
      "status": "under_review",
      "timestamp": "2026-10-31T19:16:53+00:00"
    }
  ]
}
```
<!-- **A submission**

```bash
$ curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d '{\"text\": \"The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must be able to handle a wide variety of different inputs. Additionally, the overall performance of the solution depends on a number of important variables.\", \"creator_id\": \"shubhan\"}'
```

```json
{
  "confidence": 0.7585,
  "content_id": "8db1f5a9-b657-41a7-a602-26ad7d011378",
  "guess": "ai",
  "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
  "model_score": 0.8864,
  "style_score": 0.6306
}
```

**An appeal**

```bash
$ curl.exe -X POST http://127.0.0.1:5000/appeal -H "Content-Type: application/json" -d "@appeal.json"
```

(`appeal.json` contained: `{"content_id": "8db1f5a9-b657-41a7-a602-26ad7d011378", "reasoning": "I wrote this myself as part of a practice essay."}`)

```json
{
  "content_id": "8db1f5a9-b657-41a7-a602-26ad7d011378",
  "message": "Your appeal has been recorded and this item is marked for review by a person.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl.exe "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.7585,
      "content_id": "8db1f5a9-b657-41a7-a602-26ad7d011378",
      "creator_id": "shubhan",
      "guess": "ai",
      "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
      "model_score": 0.8864,
      "status": "decided",
      "style_score": 0.6306,
      "timestamp": "2026-10-31T19:00:31+00:00"
    },
    {
      "content_id": "8db1f5a9-b657-41a7-a602-26ad7d011378",
      "creator_id": "shubhan",
      "event": "appeal",
      "reasoning": "I wrote this myself as part of a practice essay.",
      "status": "under_review",
      "timestamp": "2026-10-31T19:01:09+00:00"
    }
  ]
}
```
--- -->

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 1: a wrong prediction**

- *What I asked for:* A text that would make my two signals split.
- *What came back:* A choppy, comma-heavy rewrite of AI-style text, with a prediction that signal one would stay high.
- *What I changed:* I ran it, and signal one dropped to 0.3871 instead of staying high, so the signals moved together and it wasn't a real split. I recorded it as a finding (reshaped AI text fooled both signals), and then tried a different text that did split them.

**Moment 2: choosing and setting up the third signal (stretch)**

- *What I asked for:* Help deciding which stretch features to take on and what a third signal should measure that my first two don't, and how to set it up properly.
- *What came back:* A plan to declare the stretch features in my README before building them, and a proposal for a phrase signal that counts stock formal phrases ("it is important to note", "furthermore", "a wide variety of"). It scores 0.5 when no phrases are found, so it can add suspicion but never clear anyone, with a suggested weight of 0.2 for the new signal and 0.4 for each of the other two.
- *What I changed:* I added the Stretch Features declaration to my README before starting. I built `phrases.py` and ran it alone on my texts before wiring it in. Then I ran all 13 of my own essays through the three-signal version instead of trusting the proposal: 6 of them labeled "ai" with two signals and 4 with three. I didn't take that as proof the new signal is good. In my weighting note I wrote that part of the drop is just the neutral 0.5 baseline pulling every score toward the middle, and I didn't tune the weights on my essays, because they are my test set for the next unit.

## Stretch Features

I added two stretch features:

1. **`GET /content/<id>`**: returns one item's current status (`decided` or `under_review`), whether it was appealed, and the original guess and label. A fake id returns a 404.
2. **A third signal** (`phrases.py::phrase_signal`), with the weighting note in "The combining rule" above.

**Evidence for `GET /content/<id>`:** I requested the item I had appealed:
**Evidence for `GET /content/<id>`:** I requested the item I had appealed, then a fake id.

```bash
$ curl.exe http://127.0.0.1:5000/content/8db1f5a9-b657-41a7-a602-26ad7d011378
```

```json
{
  "appealed": true,
  "confidence": 0.7585,
  "content_id": "8db1f5a9-b657-41a7-a602-26ad7d011378",
  "guess": "ai",
  "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
  "status": "under_review"
}
```

```bash
$ curl.exe http://127.0.0.1:5000/content/not-a-real-id
```

```json
{
  "error": "not_found",
  "message": "We couldn't find a submission with that content_id."
}
```

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
