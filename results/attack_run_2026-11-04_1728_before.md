# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 17:28
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `e2afcc9c-ff86-4426-a41a-b0e06d30e524` | unsure | 0.448 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `ad863588-f057-4e85-8c39-6f0c923ff408` | unsure | 0.431 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `bff796e0-1b01-4832-aa81-71d5e84097b3` | unsure | 0.520 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `ab434700-7544-46b6-8ce5-a7d42e4f7897` | unsure | 0.558 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `8eccdd66-9113-477b-ad36-75f604f8db1f` | human | 0.322 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `f9b62032-c3db-4fcb-bace-95641d9a5438` | unsure | 0.516 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `5cf32684-6a81-475b-8880-1cd48e97b16f` | unsure | 0.638 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `43eb4057-6f30-4d90-be86-a967ce025e49` | unsure | 0.445 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `308d4375-bd49-4ebb-878a-9d9a014a62c8` | unsure | 0.525 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `4c75f68f-1636-41bc-9808-a7959073caca` | ai | 0.832 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `41957333-31ab-401e-b48f-b3950755f638` | unsure | 0.597 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `b108b7d7-35ff-4e8e-8f25-27ec7efc61fc` | ai | 0.702 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `2b48c19b-49d8-4e21-9047-b756b55c4d83` | ai | 0.719 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `a4fc93b0-2fc6-4a9a-ba5b-83fca5407702` | ai | 0.747 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `88da7922-0636-463d-ab09-4bd084421e3f` | ai | 0.742 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `3ffb2033-490d-4087-8faa-8df499e9e3a4` | ai | 0.680 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `0a6a9560-f008-4af2-b5ed-fdffeea5e748` | ai | 0.669 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `2cbb981a-152e-4af6-8d1f-f3ed09b9285e` | unsure | 0.439 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `77a92cc8-2b90-4f3a-9a43-a0cddd59c394` | unsure | 0.439 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `e50a2ad3-1790-4cdd-ab85-de850ed11421` | human | 0.285 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `2c108943-026d-47c7-b6a7-5b7f010e77bf` | unsure | 0.505 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `161699ba-1580-4453-98f3-5bd03c4bc678` | unsure | 0.438 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `03d26ce6-2726-4bf4-bdb4-f3f5314b9d3b` | unsure | 0.469 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `72ec38c5-faf7-49e1-908f-63d820273cf4` | unsure | 0.568 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `9a0a391a-bdd6-4f0c-b166-e7d45e0fa51b` | unsure | 0.440 |  |
| MF04 | malformed | text is only punctuation | 200 | `b7f29ef1-cc80-4ccb-8aa2-fcacff950fd2` | unsure | 0.402 |  |
| MF05 | malformed | text is a very long single word | 200 | `f3c6f361-01e7-41b0-8f5f-38bb5360dac2` | unsure | 0.600 |  |
| MF06 | malformed | text is emoji only | 200 | `086795a6-d980-47e3-8439-a3ab1385ad3d` | unsure | 0.599 |  |
| MF07 | malformed | text is right-to-left script | 200 | `05593826-dbab-456c-8670-86bc2767573f` | unsure | 0.581 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b866fd54-f9bb-4aed-ae5e-4fd548cef6cc` | unsure | 0.446 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8c5422b4-07fb-4d6d-925f-971f1b18ef28` | unsure | 0.446 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7d875691-1914-46c0-a02c-8acad2b33c9b` | unsure | 0.446 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b32d3ac4-c600-4290-bb63-8cb59672a52d` | unsure | 0.446 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e4ae726c-e209-46e9-bb7d-2721c76955da` | unsure | 0.446 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `22f5e3ca-ecee-4dc0-9093-0085012d1f88` | unsure | 0.446 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c3a5faf5-6d14-4300-88fd-ab76675facfd` | unsure | 0.446 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `52ce6931-d386-46ce-b25b-85a788d72c3a` | unsure | 0.446 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `73d43569-253a-4ceb-8946-2d05f148f87c` | unsure | 0.446 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cad8b178-f5b7-4a4b-a3bf-5438da5f3878` | unsure | 0.446 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "e2afcc9c-ff86-4426-a41a-b0e06d30e524",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.4482,
  "model_score": 0.1635,
  "style_score": 0.5773,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "ad863588-f057-4e85-8c39-6f0c923ff408",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4309,
  "model_score": 0.5943,
  "style_score": 0.233,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "bff796e0-1b01-4832-aa81-71d5e84097b3",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.52,
  "model_score": 0.6662,
  "style_score": 0.3839,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "ab434700-7544-46b6-8ce5-a7d42e4f7897",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5585,
  "model_score": 0.6114,
  "style_score": 0.5348,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "8eccdd66-9113-477b-ad36-75f604f8db1f",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3218,
  "model_score": 0.3212,
  "style_score": 0.2334,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "f9b62032-c3db-4fcb-bace-95641d9a5438",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.5157,
  "model_score": 0.5727,
  "style_score": 0.3308,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "5cf32684-6a81-475b-8880-1cd48e97b16f",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.638,
  "model_score": 0.5862,
  "style_score": 0.5087,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "43eb4057-6f30-4d90-be86-a967ce025e49",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4454,
  "model_score": 0.2452,
  "style_score": 0.6183,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "308d4375-bd49-4ebb-878a-9d9a014a62c8",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5255,
  "model_score": 0.7042,
  "style_score": 0.3595,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "4c75f68f-1636-41bc-9808-a7959073caca",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8316,
  "model_score": 0.9792,
  "style_score": 0.8499,
  "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "41957333-31ab-401e-b48f-b3950755f638",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5966,
  "model_score": 0.6175,
  "style_score": 0.624,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "b108b7d7-35ff-4e8e-8f25-27ec7efc61fc",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7024,
  "model_score": 0.7387,
  "style_score": 0.7673,
  "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "2b48c19b-49d8-4e21-9047-b756b55c4d83",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7189,
  "model_score": 0.8051,
  "style_score": 0.7421,
  "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "a4fc93b0-2fc6-4a9a-ba5b-83fca5407702",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.747,
  "model_score": 0.8329,
  "style_score": 0.6007,
  "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "88da7922-0636-463d-ab09-4bd084421e3f",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7424,
  "model_score": 0.8005,
  "style_score": 0.8055,
  "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "3ffb2033-490d-4087-8faa-8df499e9e3a4",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.6797,
  "model_score": 0.8814,
  "style_score": 0.5679,
  "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "0a6a9560-f008-4af2-b5ed-fdffeea5e748",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.669,
  "model_score": 0.8816,
  "style_score": 0.5408,
  "label": "Our automated check thinks this may have been written with AI. It can be wrong, especially for writers who use short, plain sentences or a formal style. If you wrote it yourself, you can appeal and it will be marked for review by a person.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "2cbb981a-152e-4af6-8d1f-f3ed09b9285e",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4392,
  "model_score": 0.3223,
  "style_score": 0.5258,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "77a92cc8-2b90-4f3a-9a43-a0cddd59c394",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4388,
  "model_score": 0.4625,
  "style_score": 0.3845,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "e50a2ad3-1790-4cdd-ab85-de850ed11421",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.285,
  "model_score": 0.2044,
  "style_score": 0.258,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "2c108943-026d-47c7-b6a7-5b7f010e77bf",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5048,
  "model_score": 0.5943,
  "style_score": 0.4177,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "161699ba-1580-4453-98f3-5bd03c4bc678",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4379,
  "model_score": 0.4998,
  "style_score": 0.345,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "03d26ce6-2726-4bf4-bdb4-f3f5314b9d3b",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4685,
  "model_score": 0.6401,
  "style_score": 0.2022,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "72ec38c5-faf7-49e1-908f-63d820273cf4",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5676,
  "model_score": 0.5583,
  "style_score": 0.6108,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "9a0a391a-bdd6-4f0c-b166-e7d45e0fa51b",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.44,
  "model_score": 0.0,
  "style_score": 0.7,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "b7f29ef1-cc80-4ccb-8aa2-fcacff950fd2",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.4022,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "f3c6f361-01e7-41b0-8f5f-38bb5360dac2",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.5995,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "086795a6-d980-47e3-8439-a3ab1385ad3d",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.5994,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "05593826-dbab-456c-8670-86bc2767573f",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.5813,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "b866fd54-f9bb-4aed-ae5e-4fd548cef6cc",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4457,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "8c5422b4-07fb-4d6d-925f-971f1b18ef28",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4457,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "7d875691-1914-46c0-a02c-8acad2b33c9b",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4457,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "b32d3ac4-c600-4290-bb63-8cb59672a52d",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4457,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "e4ae726c-e209-46e9-bb7d-2721c76955da",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4457,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "22f5e3ca-ecee-4dc0-9093-0085012d1f88",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4457,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "c3a5faf5-6d14-4300-88fd-ab76675facfd",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4457,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "52ce6931-d386-46ce-b25b-85a788d72c3a",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4457,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "73d43569-253a-4ceb-8946-2d05f148f87c",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4457,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "cad8b178-f5b7-4a4b-a3bf-5438da5f3878",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.4457,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
