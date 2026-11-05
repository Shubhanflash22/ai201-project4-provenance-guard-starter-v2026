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

<!-- **What it measures:**

**Why that might differ between human and AI writing:**

**What it can't see:** -->

**What it measures:** How predictable the text is to a language model (gpt2 running on my own machine). The model’s surprise is called perplexity. Low perplexity (easy to predict) becomes a high score, and the score runs from 0 (human-like) to 1 (AI-like).

**Why that might differ between human and AI writing:** An AI writes by repeatedly choosing a likely next word, so its text tends to be easy for another model to predict. Human writing wanders more, with unusual word choices, abrupt turns and specific details that a model doesn’t expect.

**What it can't see:** The difference between predictable and AI-written. A person writing plainly with common words in short sentences can score as “AI” as strongly as real AI does. That includes a second-language writer sticking to safe vocabulary, a younger writer, and anyone writing simply on purpose. The reverse also happens: dense, ornate human prose full of rare words can score as human even when a model wrote it. It also reads only the first 400 tokens (about 300 words), so anything later in a long submission is invisible to it.

### Signal two — the style signal

<!-- **What it measures:**

**Why that might differ between human and AI writing:**

**What it can't see:** -->

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

<!-- **The rule:**

**The numbers:**

**Where it lives:** `scoring.py::combine_signals` -->

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

<!-- | Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human |  |  |
| unsure |  |  |
| high-confidence AI |  |  |

**Why I worded the "unsure" one this way:** -->
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
<!-- 
**A submission** -->

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

<!-- ```bash
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

```json -->

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

<!-- **Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:* -->

**Moment 1: a wrong prediction**

- *What I asked for:* A text that would make my two signals split.
- *What came back:* A choppy, comma-heavy rewrite of AI-style text, with a prediction that signal one would stay high.
- *What I changed:* I ran it, and signal one dropped to 0.3871 instead of staying high, so the signals moved together and it wasn't a real split. I recorded it as a finding (reshaped AI text fooled both signals), and then tried a different text that did split them.

**Moment 2: choosing and setting up the third signal (stretch)**

- *What I asked for:* Help deciding which stretch features to take on and what a third signal should measure that my first two don't, and how to set it up properly.
- *What came back:* A plan to declare the stretch features in my README before building them, and a proposal for a phrase signal that counts stock formal phrases ("it is important to note", "furthermore", "a wide variety of"). It scores 0.5 when no phrases are found, so it can add suspicion but never clear anyone, with a suggested weight of 0.2 for the new signal and 0.4 for each of the other two.
- *What I changed:* I added the Stretch Features declaration to my README before starting. I built `phrases.py` and ran it alone on my texts before wiring it in. Then I ran all 13 of my own essays through the three-signal version instead of trusting the proposal: 6 of them labeled "ai" with two signals and 4 with three. I didn't take that as proof the new signal is good. In my weighting note I wrote that part of the drop is just the neutral 0.5 baseline pulling every score toward the middle, and I didn't tune the weights on my essays, because they are my test set for the next unit.

**Moment 3: choosing the one improvement**
- *What I asked for:* Which single change my diagnoses pointed at, and what it would do to my results before I made it.
- *What came back:* A recommendation to raise `AI_THRESHOLD` from 0.65 to 0.75, with predictions from my before-run data (the six false positives would drop to "unsure", criterion 1 would go from 3 of 10 to 0, the evasions would not change), plus a warning that 0.75 was chosen just above my highest false positive.
- *What I changed:* I made only that one edit and compared the real runs against the predictions. They matched (45 held, 11 broke). I wrote the cost into the README, that none of my AI paragraphs is labeled AI now and that the threshold is fitted to this data, and I left the other fixes under "What's Still Broken" instead of making them.

## Stretch Features

I added four stretch features:

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

3. **Per-creator rate limits**, with a note on what that changes. My limiter counts requests by `creator_id` and falls back to the caller's address only when there isn't a usable one (`app.py::rate_limit_key`). Evidence is below.

**Evidence for per-creator limits.** My limiter counts requests by `creator_id` (`app.py::rate_limit_key`). Sending 15 submissions under one `creator_id` got blocked after 10 (see Rate Limiting above: `200` ×10, then `429` ×5). Sending the same 15 submissions under 15 different `creator_id`s with `rotate_creators.py`:

```bash
$ python rotate_creators.py
```

```
200 200 200 200 200 200 200 200 200 200 200 200 200 200 200
```

**What counting per creator changes.** It protects people who share a connection: a household or a campus network is not treated as one caller, so one person's heavy use doesn't lock out the others. The cost is that the limit is only as strong as the identity behind it. `creator_id` is a string the caller chooses, so a script that makes up a new one for every request gets a fresh allowance each time and was never limited. If this ran for real, I would keep the per-creator limit and add a second limit per address, so rotating names from one machine still hits a ceiling.

4. **A second improvement, measured the same way:** reject text with fewer than 10 letters before the signals run (fixes MF03 and MF04), compared against the first improvement's results.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 120 per day

**Why those numbers and not others:** I'm the realistic heavy user. I take about 8 to 10 tries on a draft (mostly fixing spelling and wording) and I work on 10 to 12 pieces at a time, so a hard day is roughly 80 to 120 submissions. 120 per day covers that without getting in my way. 10 per minute is far above what a person can reach, because each submission takes a second or two to score and I have to edit between tries, so only a script hits it. A script mapping my thresholds with hundreds of slightly different versions of one text runs into the cap within a minute, and the daily cap stops it from just waiting and starting again.

**What a caller counts as:** The `creator_id` in the request, or the caller's address if there isn't a usable one (`app.py::rate_limit_key`). This means one name can't flood the service, but a script that changes `creator_id` on every request gets a fresh allowance each time, so my limit slows down a casual prober and not a determined one. Counting by address would catch that script but would treat everyone behind a shared connection, like one household, as one caller.

**The run of status codes when I pushed past it:**

```bash
$ python run_attacks.py --flood 15
```

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

5 of 15 were rate limited. The first 10 went through and the next 5 were rejected with a 429.

<!-- **My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

<!-- **What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

<!-- **The run of status codes when I pushed past it:**

python run_attacks.py --flood 15 -->

---

## Attack Run — Before

56 attacks from the staff attack set, sent through `POST /submit` with `run_attacks.py --set attack_set\attack_set --label before` (full output in `results/attack_run_2026-11-04_1728_before.md`). Nothing in the code was changed between reading the attack set and this run.

**How I marked them.** Held means the service did what it should; broke means it did what the attack wanted.

- **evasion:** the text is AI-derived, so HELD only if it was labeled `ai`. A label of `unsure` says "nothing happens to your work", so I count it as getting through. (EV10 is the only one caught.)
- **false_positive:** the text is genuine human writing, so BROKE if labeled `ai`; `unsure` and `human` are HELD.
- **prompt_injection:** HELD if the label text and the audit log came back intact and the score looks like it came from the signals, not from obeying the text.
- **malformed:** HELD for a clean 400, or for a sensible non-crashing answer. BROKE when input that should be refused like the whitespace case (MF01) was scored as if it were writing.
- **flood:** HELD if the limiter engaged. The first 10 requests get through by design (limit 10 per minute).

| ID | Family | What it targets | Status | Guess | Score | Held / Broke |
|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.448 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.431 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.520 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.558 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.322 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.516 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.638 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | unsure | 0.445 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.525 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.832 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.597 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | ai | 0.702 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | ai | 0.719 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | ai | 0.747 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | ai | 0.742 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | ai | 0.680 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | ai | 0.669 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | unsure | 0.439 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.439 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.285 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.505 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.438 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.469 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.568 | HELD |
| MF01 | malformed | text is only whitespace | 400 | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | unsure | 0.440 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | unsure | 0.402 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | unsure | 0.600 | HELD |
| MF06 | malformed | text is emoji only | 200 | unsure | 0.599 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | unsure | 0.581 | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | HELD |
| RQ05 | malformed | text is null | 400 | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD |

**Totals: 39 held, 17 broke out of 56.**

| Family | Held | Broke | Attacks |
|---|---|---|---|
| evasion | 1 | 9 | 10 |
| false_positive | 2 | 6 | 8 |
| prompt_injection | 6 | 0 | 6 |
| malformed (MF, odd text) | 6 | 2 | 8 |
| malformed (RQ, bad request shape) | 12 | 0 | 12 |
| flood_same_creator | 12 | 0 | 12 |

**Ten audit log entries from the run**

Chosen to show the interesting failures: three real writers labeled AI (FP03, FP05, FP07); typos that dropped signal one to 0.16 (EV01); broken-up sentences that dropped signal two (EV02); the one evasion labeled "human" (EV05); a text 0.012 under the AI threshold that only signal three nudged (EV07); two non-text inputs scored as if they were writing (MF03, MF06); and one rejected request (rate limit).

```json
{
  "combined_score": 0.7189,
  "content_id": "2b48c19b-49d8-4e21-9047-b756b55c4d83",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
  "model_score": 0.8051,
  "phrase_score": 0.5,
  "status": "decided",
  "style_score": 0.7421,
  "timestamp": "2026-11-05T01:28:30+00:00"
}
{
  "combined_score": 0.7424,
  "content_id": "88da7922-0636-463d-ab09-4bd084421e3f",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
  "model_score": 0.8005,
  "phrase_score": 0.5,
  "status": "decided",
  "style_score": 0.8055,
  "timestamp": "2026-11-05T01:28:30+00:00"
}
{
  "combined_score": 0.669,
  "content_id": "0a6a9560-f008-4af2-b5ed-fdffeea5e748",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
  "model_score": 0.8816,
  "phrase_score": 0.5,
  "status": "decided",
  "style_score": 0.5408,
  "timestamp": "2026-11-05T01:28:30+00:00"
}
{
  "combined_score": 0.4482,
  "content_id": "e2afcc9c-ff86-4426-a41a-b0e06d30e524",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "model_score": 0.1635,
  "phrase_score": 0.5,
  "status": "decided",
  "style_score": 0.5773,
  "timestamp": "2026-11-05T01:28:28+00:00"
}
{
  "combined_score": 0.4309,
  "content_id": "ad863588-f057-4e85-8c39-6f0c923ff408",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "model_score": 0.5943,
  "phrase_score": 0.5,
  "status": "decided",
  "style_score": 0.233,
  "timestamp": "2026-11-05T01:28:28+00:00"
}
{
  "combined_score": 0.3218,
  "content_id": "8eccdd66-9113-477b-ad36-75f604f8db1f",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "label": "We think this was probably written by a person.",
  "model_score": 0.3212,
  "phrase_score": 0.5,
  "status": "decided",
  "style_score": 0.2334,
  "timestamp": "2026-11-05T01:28:28+00:00"
}
{
  "combined_score": 0.638,
  "content_id": "5cf32684-6a81-475b-8880-1cd48e97b16f",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "model_score": 0.5862,
  "phrase_score": 1.0,
  "status": "decided",
  "style_score": 0.5087,
  "timestamp": "2026-11-05T01:28:29+00:00"
}
{
  "combined_score": 0.44,
  "content_id": "9a0a391a-bdd6-4f0c-b166-e7d45e0fa51b",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "model_score": 0.0,
  "phrase_score": 0.5,
  "status": "decided",
  "style_score": 0.7,
  "timestamp": "2026-11-05T01:28:31+00:00"
}
{
  "combined_score": 0.5994,
  "content_id": "086795a6-d980-47e3-8439-a3ab1385ad3d",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "model_score": 0.9969,
  "phrase_score": 0.5,
  "status": "decided",
  "style_score": 0.5,
  "timestamp": "2026-11-05T01:28:32+00:00"
}
{
  "creator_id": "attacker_flood",
  "event": "rejected",
  "limit": "10 per 1 minute",
  "reason": "rate_limited",
  "status": "rejected",
  "timestamp": "2026-11-05T01:28:33+00:00"
}
```

**The single worst outcome** — the one I'd least want to explain to a writer whose work got caught by it:

FP03, "a non-native English speaker writing carefully". The service returned `guess: ai` with confidence 0.7189 (model 0.8051, style 0.7421). This is a person writing carefully in a second language, sticking to words they're sure of, and both of my signals read that care as machine-like. They are also the writer with the least room to argue back. The label tells them it "may have been written with AI" and gives them one recourse, an appeal that moves the item to `under_review`; nothing about the label tells them why it happened or that it is a known weakness for exactly their kind of writing.

---

<!-- ## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



<!-- **Ten audit log entries from the run** -->

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

<!-- ```json

``` -->

<!--**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

 -->

---

## Run Log and Verdicts

Five criteria, three trials each, run with python run_eval.py --label before (criteria 1, 2, 3 and 5; output in results/run_2026-11-04_1738_before.md) and python run_appeals.py --label before (criterion 4; output in results/appeals_2026-11-04_1738_before.md). Nothing was changed between trials.

Criterion	Target	Run 1	Run 2	Run 3	Verdict
1. My own writing flagged as AI	≤ 1 of 10	3/10	3/10	3/10	MISSED
2. AI and human text score apart	gap ≥ 0.4 in ≥ 4 of 5 pairs	0/5 pairs	0/5 pairs	0/5 pairs	MISSED
3. All three labels reachable	3 of 3	3/3	3/3	3/3	MET
4. Appeal changes status and is logged	5 of 5	5/5	5/5	5/5	MET
5. Bad input returns 400, never 500	5 of 5	5/5	5/5	5/5	MET

All three trials of every criterion came out identical, which is what I expected: neither signal has any randomness.

How I decided each verdict

Criterion 1, MISSED. The 10 pieces are the first 10 essays in my_writing.txt, chosen by position, not by score. Essays 1, 8 and 9 were labeled ai (confidence 0.7136, 0.6909, 0.6847) in every trial. 3 is above my limit of 1, so it misses in all three trials.
Criterion 2, MISSED. I paired five unedited AI paragraphs with my own essays 1 to 5. The gap (AI confidence minus human confidence) was -0.0017, +0.0045, -0.0460, -0.0072, +0.0004 for pairs 1 to 5. None reaches 0.4, and the largest is under 0.005, so on this set the combined score does not separate the two at all (average 0.606 for AI, 0.616 for my essays).
Criterion 3, MET. The five inputs produced ai, human, unsure, ai, unsure in every trial: all three labels within 5 submissions, well inside my limit of 20.
Criterion 4, MET. In all three trials, all 5 appeals returned status under_review and a matching appeal entry appeared in GET /log for that content_id. Because run_eval.py can't send an appeal after a submission, I wrote run_appeals.py to do it.
Criterion 5, MET. All five bad inputs (missing text, empty text, whitespace only, text over 10,000 characters, non-string text) returned status 400 in every trial, and none returned a 500. The error message in the body comes from app.py::submit, where every 400 branch returns a message.

Criterion 2 in numbers (the same in all three trials):

Pair	AI confidence	Human confidence	Gap	≥ 0.4?
1	0.7119	0.7136	-0.0017	no
2	0.6311	0.6266	+0.0045	no
3	0.5416	0.5876	-0.0460	no
4	0.5910	0.5982	-0.0072	no
5	0.5566	0.5562	+0.0004	no

Averages over the five pairs: model signal 0.837 (AI) vs 0.643 (human), style signal 0.427 (AI) vs 0.631 (human), combined 0.606 vs 0.616.

Real output from one trial (trial 1 of each criterion), pasted from the results files. Produced by run_eval.py::main, which sends each text to POST /submit (app.py::submit, scoring in scoring.py::combine_signals). sent is the first 70 characters of what was sent.

Criterion 1, my own writing:

json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7136,
    "model_score": 0.7274,
    "style_score": 0.7788,
    "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
    "sent": "I believe that having sound moral judgment and maintaining the respect"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6266,
    "model_score": 0.6693,
    "style_score": 0.5883,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "Although science and technology have managed to solve a substantial am"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5876,
    "model_score": 0.5511,
    "style_score": 0.6678,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "Human beings are some of the most social creatures on planet earth. As"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5982,
    "model_score": 0.6268,
    "style_score": 0.6186,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "Leadership is a skill that is developed with experience. However, it's"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5562,
    "model_score": 0.6381,
    "style_score": 0.5023,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "Persistence and perseverance are the two hallmarks of the human race. "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5845,
    "model_score": 0.652,
    "style_score": 0.5352,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "As Plato said, \"Necessity is the mother of all inventions\". In today's"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.632,
    "model_score": 0.6893,
    "style_score": 0.6407,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "The passage presents an argument that claims Paleo diets to be a cure "
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6909,
    "model_score": 0.742,
    "style_score": 0.7044,
    "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
    "sent": "The arguments passed by the author in their argument to get the use of"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6847,
    "model_score": 0.7185,
    "style_score": 0.6723,
    "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
    "sent": "The central claim here is that the charities in need will receive what"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6088,
    "model_score": 0.6626,
    "style_score": 0.5854,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "Today's world is rapidly evolving as we made technological leaps that "
  }
]

Criterion 2, score spread (odd positions are AI text, even positions are my essays; pair k is positions 2k-1 and 2k):

json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7119,
    "model_score": 0.7911,
    "style_score": 0.4886,
    "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
    "sent": "Remote work has become increasingly common in recent years, offering b"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7136,
    "model_score": 0.7274,
    "style_score": 0.7788,
    "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
    "sent": "I believe that having sound moral judgment and maintaining the respect"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6311,
    "model_score": 0.9152,
    "style_score": 0.4905,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "Renewable energy plays a crucial role in addressing the growing challe"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6266,
    "model_score": 0.6693,
    "style_score": 0.5883,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "Although science and technology have managed to solve a substantial am"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5416,
    "model_score": 0.7712,
    "style_score": 0.2864,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "Social media has fundamentally transformed the way teenagers communica"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5876,
    "model_score": 0.5511,
    "style_score": 0.6678,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "Human beings are some of the most social creatures on planet earth. As"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.591,
    "model_score": 0.8588,
    "style_score": 0.4381,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "Getting enough sleep is one of the most important factors in maintaini"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5982,
    "model_score": 0.6268,
    "style_score": 0.6186,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "Leadership is a skill that is developed with experience. However, it's"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5566,
    "model_score": 0.8494,
    "style_score": 0.4336,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "Public transportation is an essential component of modern urban life, "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5562,
    "model_score": 0.6381,
    "style_score": 0.5023,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "Persistence and perseverance are the two hallmarks of the human race. "
  }
]

Criterion 3, label coverage:

json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8068,
    "model_score": 0.8864,
    "style_score": 0.6306,
    "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
    "sent": "The implementation of the proposed framework requires careful consider"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3148,
    "model_score": 0.403,
    "style_score": 0.1339,
    "label": "We think this was probably written by a person.",
    "sent": "Honestly I burned the toast again this morning, set off the smoke alar"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5412,
    "model_score": 0.7773,
    "style_score": 0.1787,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "Short answer: yes. The implementation of the proposed framework requir"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7156,
    "model_score": 0.8299,
    "style_score": 0.7092,
    "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
    "sent": "I like my school. It is big. I have many friends. We play games at lun"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5636,
    "model_score": 0.5965,
    "style_score": 0.3125,
    "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
    "sent": "The implementation of the proposed framework requires careful considra"
  }
]

Criterion 4, appeal path (produced by run_appeals.py::one_trial):

PASTE_CRITERION_4_JSON_HERE

Criterion 5, bad input:

json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "   "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": 12345, \"creator_id\": \"eval_bad_notstring\"}"
  }
]

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

<!-- | Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it: -->

<!-- ```json

```

**Diagnoses** -->
**Diagnoses**

The 17 broken attacks and the two missed criteria come from three causes, not 19. Each is below with its stage and mechanism.

**1. Real writing labeled AI: criterion 1 (3 of 10 essays) and FP02 to FP07 (6 of 8 attacks).**
*Stage: signal one, with the combining rule failing to catch it.* Formal, rubric-driven, technical and careful second-language writing uses common words in stock structures, so gpt2 finds it easy to predict and signal one scores it high: 0.74 to 0.88 on FP02 to FP07, and 0.72, 0.74 and 0.72 on my essays 1, 8 and 9. Signal two agreed or was near it (0.54 to 0.81), because evenly paced sentences with few commas look machine-made to it. My disagreement guard only fires when signals one and two differ by more than 0.40, and in these cases they differed by 0.34 at most (FP07: 0.8816 against 0.5408), so nothing pulled the score back toward "unsure" before it crossed 0.65. The weakness is the one I named in Milestone 1, and the rule that was meant to protect writers cannot see it, because it only handles disagreement and here the signals agree.

**2. AI and human text not scoring apart: criterion 2 (gap under 0.005 in all five pairs).**
*Stage: signal two, with the equal weights in the combining rule.* Signal one did separate them (0.837 for the AI paragraphs against 0.643 for my essays), but signal two ran the wrong way (0.427 for AI against 0.631 for my essays), and at weights of 0.4 each they cancelled out. I checked which measure was responsible: the AI paragraphs have punctuation density 0.116 against 0.032 for my essays, and vocabulary variety 0.824 against 0.700, and signal two reads both of those as human. Only sentence-length spread pointed the right way (0.20 against 0.39). Part of this is how I built the test: each AI paragraph is about 85 words in 4 sentences, my essays are 420 to 510 words, and the signal's own documentation warns that vocabulary variety falls as text gets longer, so the pair set is not length-matched. The mechanism is still real, because a comma-heavy AI paragraph beats the style signal by looking human.

**3. AI-derived text getting through: EV01 to EV09 (9 of 10 evasions, 8 of them landing in "unsure").**
*Stage: the combining rule, with each attack fooling the signal it targeted.* Each attack moved the signal it aimed at, and a plain average then carried the result under the 0.65 line, because beating one signal is enough when each counts 0.4. Typos (EV01) dropped signal one to 0.1635, since misspellings are rare tokens and raise perplexity. Broken-up sentences (EV02, 0.233) and one very long plus one very short sentence (EV06, 0.331) dropped signal two. EV08 scored 0.2452 on signal one, consistent with the AI part sitting beyond the 400-token window it reads. Nearly everything ended up between 0.43 and 0.64 because a fooled signal averaged with an unfooled one lands in the middle: EV02 is (0.4 × 0.5943) + (0.4 × 0.233) + (0.2 × 0.5) = 0.4309. The one that reached "human" (EV05, 0.3218) fooled both signals with a heavy edit. EV07 scored 0.638, 0.012 under the AI threshold, and only signal three (1.0) kept it that close.

**4. Non-text accepted as a submission: MF03 and MF04.**
*Stage: the route.* `app.py::submit` only rejects text that is missing, not a string, empty after `.strip()`, or over 10,000 characters. Control characters and punctuation-only text pass all four checks, so they reach signal one, which returns 0.0 and 0.0112 and logs a "decision" with status `decided`, while whitespace-only text (MF01) gets a 400. MF05 to MF07 (a long single word, emoji, right-to-left script) show the same gap from the other side: signal one scored them 0.9976, 0.9969 and 0.9064, and only signal two's neutral 0.5 for very short texts kept them at "unsure".

**The pattern.** Causes 1 to 3 share one idea. My signals measure surface properties (how predictable the words are, and what shape the text has), and those track register and style more than authorship, so formal humans look like AI and shaped AI looks like a human. The combining rule then adds a second problem, because averaging lets one fooled signal decide the outcome, and the guard only helps when the signals disagree. Cause 4 is a separate and smaller bug in the route.

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

**What I changed:** One value in `config.py`: `AI_THRESHOLD` from 0.65 to 0.75. That is the only change in this unit besides the rate limiter and the logging of rejected requests. No score changes anywhere (every signal and the combining rule are untouched), so the only thing that moves is the line where a score starts to be called "high-confidence AI". The "unsure" band is now 0.35 to 0.75.

**Which diagnosis pointed at it:** Diagnosis 1, real writing labeled AI. Criterion 1 (3 of 10 essays) and six of the false-positive attacks (FP02 to FP07) all scored between 0.669 and 0.747 and landed just over the 0.65 line, and none of them could be caught by the disagreement guard because the signals agreed. Moving the line is the smallest change that takes those writers out of the "AI" label. I picked 0.75 because it is the first round number above the highest false positive I saw (FP04, 0.747), so I should be honest about what that means: I fitted the threshold to this attack set, and the result below is therefore optimistic. It does not show how a threshold of 0.75 would do on writing I haven't seen.

### Attack Run — After

Same 56 attacks, same marking rules as Attack Run — Before, run with `python run_attacks.py --set attack_set\attack_set --label after` (full output in `results/attack_run_2026-11-05_0050_after.md`). Scores are identical to the before run; only the labels in the six changed rows differ.

| ID | Family | What it targets | Status | Guess | Score | Before | After |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | unsure | 0.448 | BROKE | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | unsure | 0.431 | BROKE | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | unsure | 0.520 | BROKE | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | unsure | 0.558 | BROKE | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | human | 0.322 | BROKE | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | unsure | 0.516 | BROKE | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | unsure | 0.638 | BROKE | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | unsure | 0.445 | BROKE | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | unsure | 0.525 | BROKE | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | ai | 0.832 | HELD | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | unsure | 0.597 | HELD | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | ai → unsure | 0.702 | BROKE | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | ai → unsure | 0.719 | BROKE | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | ai → unsure | 0.747 | BROKE | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | ai → unsure | 0.742 | BROKE | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | ai → unsure | 0.680 | BROKE | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | ai → unsure | 0.669 | BROKE | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | unsure | 0.439 | HELD | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | unsure | 0.439 | HELD | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | human | 0.285 | HELD | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | unsure | 0.505 | HELD | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | unsure | 0.438 | HELD | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | unsure | 0.469 | HELD | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | unsure | 0.568 | HELD | HELD |
| MF01 | malformed | text is only whitespace | 400 | — | — | HELD | HELD |
| MF02 | malformed | text is a single character | 400 | — | — | HELD | HELD |
| MF03 | malformed | text is control characters | 200 | unsure | 0.440 | BROKE | BROKE |
| MF04 | malformed | text is only punctuation | 200 | unsure | 0.402 | BROKE | BROKE |
| MF05 | malformed | text is a very long single word | 200 | unsure | 0.600 | HELD | HELD |
| MF06 | malformed | text is emoji only | 200 | unsure | 0.599 | HELD | HELD |
| MF07 | malformed | text is right-to-left script | 200 | unsure | 0.581 | HELD | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | — | — | HELD | HELD |
| RQ01 | malformed | no text field at all | 400 | — | — | HELD | HELD |
| RQ02 | malformed | no creator_id | 400 | — | — | HELD | HELD |
| RQ03 | malformed | text is a number | 400 | — | — | HELD | HELD |
| RQ04 | malformed | text is a list | 400 | — | — | HELD | HELD |
| RQ05 | malformed | text is null | 400 | — | — | HELD | HELD |
| RQ06 | malformed | creator_id is an object | 400 | — | — | HELD | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | — | — | HELD | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | — | — | HELD | HELD |
| RQ09 | malformed | body is empty | 400 | — | — | HELD | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | — | — | HELD | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | — | — | HELD | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | — | — | HELD | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | unsure | 0.446 | HELD | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | — | — | HELD | HELD |

**Totals: 45 held, 11 broke out of 56** (before: 39 held, 17 broke).

| Family | Held before | Held after | Broke before | Broke after |
|---|---|---|---|---|
| evasion | 1 | 1 | 9 | 9 |
| false_positive | 2 | 8 | 6 | 0 |
| prompt_injection | 6 | 6 | 0 | 0 |
| malformed (MF, odd text) | 6 | 6 | 2 | 2 |
| malformed (RQ, bad request shape) | 12 | 12 | 0 | 0 |
| flood_same_creator | 12 | 12 | 0 | 0 |

**My five criteria, before and after** (three trials each; every trial within a run was identical). After: `python run_eval.py --label after` and `python run_appeals.py --label after`, output in `results/run_2026-11-05_0050_after.md` and `results/appeals_2026-11-05_0050_after.md`.

| Criterion | Target | Before (runs 1, 2, 3) | After (runs 1, 2, 3) | Verdict before → after |
|---|---|---|---|---|
| 1. My own writing flagged as AI | ≤ 1 of 10 | 3/10, 3/10, 3/10 | 0/10, 0/10, 0/10 | MISSED → **MET** |
| 2. AI and human text score apart | gap ≥ 0.4 in ≥ 4 of 5 pairs | 0/5, 0/5, 0/5 | 0/5, 0/5, 0/5 | MISSED → **MISSED** |
| 3. All three labels reachable | 3 of 3 | 3/3, 3/3, 3/3 | 3/3, 3/3, 3/3 | MET → **MET** |
| 4. Appeal changes status and is logged | 5 of 5 | 5/5, 5/5, 5/5 | 5/5, 5/5, 5/5 | MET → **MET** |
| 5. Bad input returns 400, never 500 | 5 of 5 | 5/5, 5/5, 5/5 | 5/5, 5/5, 5/5 | MET → **MET** |

**Did it help, and how do I know:**

It did what I aimed it at. All six false positives (FP02 to FP07) went from `ai` to `unsure` with the same scores (for example FP04 was 0.747 before and is 0.747 now), so the false-positive family went from 2 held to 8 held. Criterion 1 went from 3 of 10 to 0 of 10 in all three trials, which turns a missed criterion into a met one. Nothing else in the attack set changed.

What it cost, which is the trade I knew I was making:

- **Less AI text gets labeled AI.** Before, 7 submissions in the attack set were labeled `ai` (FP02 to FP07 and EV10). After, only EV10 (0.832) is. In criterion 2, my first AI paragraph (0.7119) was labeled `ai` before and is `unsure` now, so none of the five AI paragraphs is labeled `ai` any more. In criterion 3, the plainly written school paragraph (0.7156) moved from `ai` to `unsure`; all three labels are still reachable, but now only the 0.8068 text produces the `ai` label, so that criterion passes on one input.
- **Nothing was fixed upstream.** The signals still score these writers at 0.67 to 0.75. They are now told "we couldn't tell" instead of "may have been written with AI", which is a better thing to say to a real writer but not a better reading of their writing.
- **No evasion got worse,** because EV10 was the only evasion labeled `ai` before and it still is.
- **It did not touch criterion 2,** which doesn't depend on thresholds: the gaps are identical to the before run (largest +0.0045).

---

### Second improvement (stretch)

**What I changed:** I made the service refuse text with fewer than 10 letters before either signal runs. This is two small edits: `MIN_LETTERS = 10` in `config.py`, and a check in `app.py::submit` after the existing input checks that logs a rejection (reason `too_few_letters`) and returns a 400 with "Please enter some text with words in it." Letters are counted with `str.isalpha()`, which also counts letters in other scripts, so right-to-left and non-Latin writing still passes. It is measured against the "after" run of the first improvement (threshold 0.75), so that is the baseline, and nothing else changed between the two runs.

**Which diagnosis pointed at it:** Diagnosis 4, non-text accepted as a submission. `app.py::submit` only rejected text that was missing, not a string, empty after `.strip()` or too long, so control characters (MF03) and punctuation-only text (MF04) reached signal one, which scored them 0.0 and 0.0112 and logged a "decision".

**Result:** `python run_attacks.py --set attack_set\attack_set --label after2` (output in `results/attack_run_2026-11-05_1539_after2.md`) and `python run_eval.py --label after2` (`results/run_2026-11-05_1540_after2.md`). Comparing the two attack runs row by row, exactly three rows changed and everything else is identical, including every score:

| ID | What it targets | After first improvement | After second improvement | Held / Broke |
|---|---|---|---|---|
| MF03 | text is control characters | 200, unsure (0.440) | 400 | BROKE → **HELD** |
| MF04 | text is only punctuation | 200, unsure (0.402) | 400 | BROKE → **HELD** |
| MF06 | text is emoji only | 200, unsure (0.599) | 400 | HELD → HELD (now refused instead of scored) |

**Totals: 47 held, 9 broke out of 56** (after the first improvement: 45 held, 11 broke).

| Family | Held before | Held after | Broke before | Broke after |
|---|---|---|---|---|
| evasion | 1 | 1 | 9 | 9 |
| false_positive | 8 | 8 | 0 | 0 |
| prompt_injection | 6 | 6 | 0 | 0 |
| malformed (MF, odd text) | 6 | 8 | 2 | 0 |
| malformed (RQ, bad request shape) | 12 | 12 | 0 | 0 |
| flood_same_creator | 12 | 12 | 0 | 0 |

My five criteria are unchanged: criterion 1 still 0 of 10, criterion 2 still 0 of 5 pairs (gaps identical to the earlier runs, largest +0.0045), criterion 3 still 3 of 3 labels, criterion 5 still 5 of 5 returning 400, in all three trials.

**Did it help, and what did it cost:** It fixed what it was aimed at: the two non-text inputs that were wrongly broke, MF03 and MF04, are now refused like whitespace-only text is. What it costs:

- **Short genuine text can now be refused.** Anything with fewer than 10 letters ("Yes, thank you." has 11, but "I am ok." has 5) gets a 400, where before it reached the signals. My shortest genuine attack, FP08, has enough letters and was not affected, but a real very short submission could be. I set 10 by judgment and did not tune it.
- **It does not catch every non-prose input.** MF05, one very long word, still passes (it has plenty of letters) and signal one still scores it 0.9976; it stays "unsure" because signal two returns its neutral 0.5 for very short texts, which opens a 0.50 gap with signal one and triggers the disagreement guard (combined 0.5995). That is held by my marking rule but is still a weakness in signal one.
- **MF06 (emoji only) is now refused** with a message asking for text with words in it, which is a better answer than scoring emoji, but a writer who really meant to submit symbols only would have to be told differently.

## What's Still Broken

<!-- **11 attacks still broke, and one criterion is still missed.**  -->
**9 attacks still broke, and one criterion is still missed.**
For each, what I would do and why I stopped:

- **Criterion 2 (score spread), still missed.** Cause: signal two reads comma-heavy, short AI paragraphs as human (punctuation density 0.116 against 0.032 for my essays), and at equal weights that cancels signal one's separation. I would remove the punctuation measure from signal two or length-normalize it, and rebuild the pairs so both sides are about the same length. I stopped because this unit allows one change and I used it on the false positives, and because the pair set itself is partly a length confound (85-word paragraphs against 450-word essays), so I want to fix the test before I trust a fix to the signal.
- **EV01 to EV09 (9 evasions), still broke.** Cause: a plain average lets one fooled signal decide the result. I would require both signals to agree before the service says "human", and check spelling before signal one reads the text, since typos pushed it to 0.1635. I stopped because that changes how every label is decided, so it needs its own before-and-after, and because any rule that makes "human" harder to reach also makes real writers wait longer for a clear label.
<!-- - **MF03 and MF04 (control characters, punctuation only), still broke.** Cause: the route's validation. I would require a minimum number of letters before the signals run, and return a 400 like MF01 does. This is the cheapest fix on the list and the only one I am sure has no downside. I left it so the before and after runs stay comparable, and because I was told to make one change. -->
- **MF03 and MF04 (control characters, punctuation only): fixed by the second improvement** (reject text with fewer than 10 letters). What remains is MF05, a very long single word, which passes the letter check and still scores 0.9976 on signal one; I would also require a minimum number of distinct words.
- **My own formal writing still never gets a clear label.** None of my essays is labeled `ai` now, but none is labeled `human` either (scores 0.55 to 0.71 against a human line of 0.35). Fixing that means changing what signals one and two measure, which is a bigger job than a threshold.

**The trade I'd make if this ran for real:**

I would keep the higher line and let more AI text through, because a wrong accusation costs one real writer their standing while a missed detection costs the site only a little. Honest writers pay for that choice, along with the site, because they end up competing against AI text that was labeled "unsure" instead of caught, so I would pair the wider "unsure" band with human review of that band.

---

<!-- ## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



<!-- **Did it help, and how do I know:** -->

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->
 -->


<!-- ---

## What's Still Broken -->

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



<!-- **The trade I'd make if this ran for real:** -->

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
