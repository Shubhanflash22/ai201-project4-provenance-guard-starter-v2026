# Attack run — after2

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-05 15:39
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `02481be8-e905-4619-81c5-1e7477554025` | unsure | 0.448 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `8c169176-1af4-40d2-83fa-57bfaf3d505f` | unsure | 0.431 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `f18a99a2-588d-429c-bcbe-0c0d79747c1c` | unsure | 0.520 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `72718eaa-f71b-42ee-83d3-5246845db5e6` | unsure | 0.558 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `fc48153e-0253-42d3-ae04-7d3c5f83f06b` | human | 0.322 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `b02e5adc-a91f-455f-b99a-d65c758a3099` | unsure | 0.516 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `3f013c0c-aede-4724-9a8b-195d2ad2601e` | unsure | 0.638 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `42634b13-cd00-4f44-9d0c-fec6b3b65685` | unsure | 0.445 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `bfee819d-7ea7-48be-b31e-4fa9f4f02ace` | unsure | 0.525 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `81648382-8e19-49f8-801a-6ee9e771a435` | ai | 0.832 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `a9b2d778-2d19-47b6-9d6a-1eb15a2184c1` | unsure | 0.597 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `e6e28541-4321-42c8-a479-bd7f30868992` | unsure | 0.702 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `4592dc75-00e9-4da4-ab46-bd1cdc1e6d61` | unsure | 0.719 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c6feb3a0-dc99-4cf1-b960-522ad32f96c4` | unsure | 0.747 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `1d5ccd8d-e79a-4d00-8a8b-70b62b82715b` | unsure | 0.742 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `5bb037c5-a1e0-4991-b1c7-94dc7d3299b0` | unsure | 0.680 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `82ff3b57-86e9-455a-93ee-597ac8fe3023` | unsure | 0.669 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `8cc0b138-359c-4cd1-804a-89c4ec616dcc` | unsure | 0.439 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `83ac8eef-7a01-45dd-887e-b7cb8e2a2a48` | unsure | 0.439 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `84a8de58-1b81-4f33-960e-b762e5967b98` | human | 0.285 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `ccf98b67-d65d-47d6-971f-bab128b47476` | unsure | 0.505 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `cf01dd33-76ad-47e2-b0af-53b15ef5c825` | unsure | 0.438 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `de7a4996-b1ff-4d42-9b1e-33490026ffe0` | unsure | 0.469 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `efed26fb-488e-4bf2-ab26-8ff402073109` | unsure | 0.568 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 200 | `319a39cb-628c-4532-8e4c-bba984242f5a` | unsure | 0.600 |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 200 | `08e8d278-7905-48f1-9788-544f30d2b1b6` | unsure | 0.581 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `741571f4-7a0b-4ded-a437-6407247552f5` | unsure | 0.446 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `42aeee87-487b-4d5a-b93d-fa969c413ba1` | unsure | 0.446 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0c505dfd-8de6-4a00-8701-c32f0a882b3e` | unsure | 0.446 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7868be3c-6c93-42d9-a112-da3fc5b9756c` | unsure | 0.446 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b3780af3-3c47-4807-9cc2-33f5e50fa67e` | unsure | 0.446 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a9821335-d126-4f36-830a-521320509d40` | unsure | 0.446 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3d972933-e02c-46e4-8afc-d0d9d4bb8571` | unsure | 0.446 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `65a95fb5-a76a-4ef2-a9cf-710382adf1b2` | unsure | 0.446 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e552090a-e914-4592-b8fb-0a46c93737a6` | unsure | 0.446 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6e947782-344e-4972-9685-a9ad80d02fcc` | unsure | 0.446 |  |
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
  "content_id": "02481be8-e905-4619-81c5-1e7477554025",
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
  "content_id": "8c169176-1af4-40d2-83fa-57bfaf3d505f",
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
  "content_id": "f18a99a2-588d-429c-bcbe-0c0d79747c1c",
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
  "content_id": "72718eaa-f71b-42ee-83d3-5246845db5e6",
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
  "content_id": "fc48153e-0253-42d3-ae04-7d3c5f83f06b",
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
  "content_id": "b02e5adc-a91f-455f-b99a-d65c758a3099",
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
  "content_id": "3f013c0c-aede-4724-9a8b-195d2ad2601e",
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
  "content_id": "42634b13-cd00-4f44-9d0c-fec6b3b65685",
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
  "content_id": "bfee819d-7ea7-48be-b31e-4fa9f4f02ace",
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
  "content_id": "81648382-8e19-49f8-801a-6ee9e771a435",
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
  "content_id": "a9b2d778-2d19-47b6-9d6a-1eb15a2184c1",
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
  "content_id": "e6e28541-4321-42c8-a479-bd7f30868992",
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
  "content_id": "4592dc75-00e9-4da4-ab46-bd1cdc1e6d61",
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
  "content_id": "c6feb3a0-dc99-4cf1-b960-522ad32f96c4",
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
  "content_id": "1d5ccd8d-e79a-4d00-8a8b-70b62b82715b",
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
  "content_id": "5bb037c5-a1e0-4991-b1c7-94dc7d3299b0",
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
  "content_id": "82ff3b57-86e9-455a-93ee-597ac8fe3023",
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
  "content_id": "8cc0b138-359c-4cd1-804a-89c4ec616dcc",
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
  "content_id": "83ac8eef-7a01-45dd-887e-b7cb8e2a2a48",
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
  "content_id": "84a8de58-1b81-4f33-960e-b762e5967b98",
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
  "content_id": "ccf98b67-d65d-47d6-971f-bab128b47476",
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
  "content_id": "cf01dd33-76ad-47e2-b0af-53b15ef5c825",
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
  "content_id": "de7a4996-b1ff-4d42-9b1e-33490026ffe0",
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
  "content_id": "efed26fb-488e-4bf2-ab26-8ff402073109",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "319a39cb-628c-4532-8e4c-bba984242f5a",
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
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
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
  "content_id": "08e8d278-7905-48f1-9788-544f30d2b1b6",
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
  "content_id": "741571f4-7a0b-4ded-a437-6407247552f5",
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
  "content_id": "42aeee87-487b-4d5a-b93d-fa969c413ba1",
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
  "content_id": "0c505dfd-8de6-4a00-8701-c32f0a882b3e",
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
  "content_id": "7868be3c-6c93-42d9-a112-da3fc5b9756c",
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
  "content_id": "b3780af3-3c47-4807-9cc2-33f5e50fa67e",
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
  "content_id": "a9821335-d126-4f36-830a-521320509d40",
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
  "content_id": "3d972933-e02c-46e4-8afc-d0d9d4bb8571",
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
  "content_id": "65a95fb5-a76a-4ef2-a9cf-710382adf1b2",
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
  "content_id": "e552090a-e914-4592-b8fb-0a46c93737a6",
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
  "content_id": "6e947782-344e-4972-9685-a9ad80d02fcc",
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
