# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-05 00:50
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `c9eabf68-c038-418c-93aa-3e469561d7d7` | unsure | 0.448 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `53baf9b1-6ca0-4c67-9520-7f3f773f2235` | unsure | 0.431 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `95591ebd-a0e4-470c-bf40-7271c0349f55` | unsure | 0.520 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `606a2d7d-cec6-4fd5-b3bc-42e8c48855ef` | unsure | 0.558 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `27483d60-185b-4e50-a698-063c5f6bc50b` | human | 0.322 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `0ac39fd0-a676-45b4-9c73-15b92f5de9cb` | unsure | 0.516 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `04ccbcc3-b018-4c96-8f12-5cef4c8a6eaa` | unsure | 0.638 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `92d59d83-0715-4327-95d2-8a2941899eb3` | unsure | 0.445 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `d43492e9-1038-46ec-bbbb-5817175ccf21` | unsure | 0.525 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `7686e8a0-9064-4be9-8c3c-8057ff67e720` | ai | 0.832 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `88806c5e-d491-4ba4-a34c-a6645ffe616f` | unsure | 0.597 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `e13948cb-284d-4b7a-bd84-8cfe0a5e4ab8` | unsure | 0.702 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `50da18bd-929e-4a79-8f3e-ffd0c72f64df` | unsure | 0.719 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `00f079da-bf74-497f-9fc9-6c377ff31113` | unsure | 0.747 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `05b4083f-998f-40a1-a6cd-c3490b33a389` | unsure | 0.742 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `8c7a9011-1e5b-4416-9022-05d6e553e447` | unsure | 0.680 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `ec2d5b03-70df-443e-8e04-d19665cc88bf` | unsure | 0.669 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `50a7f946-2ce6-47d7-b985-167eae154a9d` | unsure | 0.439 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `70443786-a8eb-43d0-8e64-13d2f457e8e6` | unsure | 0.439 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `b94ab394-d94b-4727-bbf8-94e998a8feb3` | human | 0.285 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `9b219123-ffbf-41d3-9f85-10c82ee7920e` | unsure | 0.505 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `4e229ac2-0c29-4f2b-902f-2bd34fe78f7d` | unsure | 0.438 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `90318476-6abb-4f00-9e68-5e771a4a0a4d` | unsure | 0.469 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `95da62fb-e80a-46b9-82f2-910f683a9328` | unsure | 0.568 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `0b2c520f-f40c-47f9-b04b-ba0e8c2c2bb9` | unsure | 0.440 |  |
| MF04 | malformed | text is only punctuation | 200 | `994a3945-f36a-45e4-b086-5c7b09186fd6` | unsure | 0.402 |  |
| MF05 | malformed | text is a very long single word | 200 | `71c2de01-9a26-4f4e-99db-a983ced00783` | unsure | 0.600 |  |
| MF06 | malformed | text is emoji only | 200 | `bd435e15-ec26-41be-b4f3-15b6f86fb4fb` | unsure | 0.599 |  |
| MF07 | malformed | text is right-to-left script | 200 | `9790a50e-a1f8-4ca4-aa98-7bd2b3d88daf` | unsure | 0.581 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c216f6e6-7b33-4a8d-ba56-0cb44ddbbd4b` | unsure | 0.446 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2e9645a3-e4aa-4039-8217-967ed269f32f` | unsure | 0.446 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `18af368b-9be7-414d-8992-bf8b6a8a0a50` | unsure | 0.446 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b99ba3c6-c470-4918-988c-2ecd925ec647` | unsure | 0.446 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `439070a2-81a4-4070-823b-cceee00c803b` | unsure | 0.446 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b93bd17f-d0b0-4fca-9ff2-d57f70d4a4b0` | unsure | 0.446 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `51b52190-da16-4115-b83f-f6c849e9af3f` | unsure | 0.446 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `5c1dbae7-1f16-4a9b-9450-c8a9159dc1dd` | unsure | 0.446 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `05fe7f9a-4df7-4c00-80fe-6c58b0998ba1` | unsure | 0.446 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6dd59996-c42f-432e-b894-dc5a375c5515` | unsure | 0.446 |  |
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
  "content_id": "c9eabf68-c038-418c-93aa-3e469561d7d7",
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
  "content_id": "53baf9b1-6ca0-4c67-9520-7f3f773f2235",
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
  "content_id": "95591ebd-a0e4-470c-bf40-7271c0349f55",
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
  "content_id": "606a2d7d-cec6-4fd5-b3bc-42e8c48855ef",
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
  "content_id": "27483d60-185b-4e50-a698-063c5f6bc50b",
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
  "content_id": "0ac39fd0-a676-45b4-9c73-15b92f5de9cb",
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
  "content_id": "04ccbcc3-b018-4c96-8f12-5cef4c8a6eaa",
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
  "content_id": "92d59d83-0715-4327-95d2-8a2941899eb3",
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
  "content_id": "d43492e9-1038-46ec-bbbb-5817175ccf21",
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
  "content_id": "7686e8a0-9064-4be9-8c3c-8057ff67e720",
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
  "content_id": "88806c5e-d491-4ba4-a34c-a6645ffe616f",
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
  "content_id": "e13948cb-284d-4b7a-bd84-8cfe0a5e4ab8",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7024,
  "model_score": 0.7387,
  "style_score": 0.7673,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
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
  "content_id": "50da18bd-929e-4a79-8f3e-ffd0c72f64df",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7189,
  "model_score": 0.8051,
  "style_score": 0.7421,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
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
  "content_id": "00f079da-bf74-497f-9fc9-6c377ff31113",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.747,
  "model_score": 0.8329,
  "style_score": 0.6007,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
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
  "content_id": "05b4083f-998f-40a1-a6cd-c3490b33a389",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7424,
  "model_score": 0.8005,
  "style_score": 0.8055,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
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
  "content_id": "8c7a9011-1e5b-4416-9022-05d6e553e447",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6797,
  "model_score": 0.8814,
  "style_score": 0.5679,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
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
  "content_id": "ec2d5b03-70df-443e-8e04-d19665cc88bf",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.669,
  "model_score": 0.8816,
  "style_score": 0.5408,
  "label": "We couldn't tell whether this was written by a person or by AI. That isn't a finding against you, and nothing happens to your work because of it. If you'd like a person to look at it, you can request a review.",
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
  "content_id": "50a7f946-2ce6-47d7-b985-167eae154a9d",
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
  "content_id": "70443786-a8eb-43d0-8e64-13d2f457e8e6",
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
  "content_id": "b94ab394-d94b-4727-bbf8-94e998a8feb3",
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
  "content_id": "9b219123-ffbf-41d3-9f85-10c82ee7920e",
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
  "content_id": "4e229ac2-0c29-4f2b-902f-2bd34fe78f7d",
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
  "content_id": "90318476-6abb-4f00-9e68-5e771a4a0a4d",
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
  "content_id": "95da62fb-e80a-46b9-82f2-910f683a9328",
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
  "content_id": "0b2c520f-f40c-47f9-b04b-ba0e8c2c2bb9",
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
  "content_id": "994a3945-f36a-45e4-b086-5c7b09186fd6",
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
  "content_id": "71c2de01-9a26-4f4e-99db-a983ced00783",
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
  "content_id": "bd435e15-ec26-41be-b4f3-15b6f86fb4fb",
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
  "content_id": "9790a50e-a1f8-4ca4-aa98-7bd2b3d88daf",
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
  "content_id": "c216f6e6-7b33-4a8d-ba56-0cb44ddbbd4b",
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
  "content_id": "2e9645a3-e4aa-4039-8217-967ed269f32f",
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
  "content_id": "18af368b-9be7-414d-8992-bf8b6a8a0a50",
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
  "content_id": "b99ba3c6-c470-4918-988c-2ecd925ec647",
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
  "content_id": "439070a2-81a4-4070-823b-cceee00c803b",
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
  "content_id": "b93bd17f-d0b0-4fca-9ff2-d57f70d4a4b0",
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
  "content_id": "51b52190-da16-4115-b83f-f6c849e9af3f",
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
  "content_id": "5c1dbae7-1f16-4a9b-9450-c8a9159dc1dd",
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
  "content_id": "05fe7f9a-4df7-4c00-80fe-6c58b0998ba1",
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
  "content_id": "6dd59996-c42f-432e-b894-dc5a375c5515",
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
