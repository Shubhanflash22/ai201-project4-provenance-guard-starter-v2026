# Running Provenance Guard

This is a **web service**. It runs on your machine and you talk to it with
`curl` from another terminal.

---

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python test.py
```

Setup is done when `python test.py` passes.

If it reports `[WARN] Detector model — not downloaded yet`:

```bash
python detector.py
```

That downloads about 550 MB and scores a sample.

> **No API key.** Nothing here calls a hosted service. The model that reads the
> text runs on your own machine.

---

## First five minutes

Two terminals. In the first:

```bash
python app.py
```

In the second:

```bash
curl -X POST http://127.0.0.1:5000/ping \
  -H "Content-Type: application/json" \
  -d '{"message": "hello"}'
```

You should get JSON back.

> **On Windows, use `curl.exe` and keep it on one line.**
>
> In PowerShell, `curl` is an alias for a different tool and the command above
> fails with `Cannot bind parameter 'Headers'`. The `\` line breaks don't work
> there either. This does:
>
> ```powershell
> curl.exe -X POST http://127.0.0.1:5000/ping -H "Content-Type: application/json" -d '{\"message\": \"hello\"}'
> ```
>
> Every `curl` command in this file works the same way: swap `curl` for
> `curl.exe` and put it on one line. Git Bash needs no change.

`/ping` is the control. When something breaks, check that `/ping` still
answers: if it does, the problem is in the handler; if it doesn't, it's the
service itself.

Then submit some writing:

```bash
curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "some writing", "creator_id": "me"}'
```

---

## The routes

| Route | What it does |
|---|---|
| `POST /ping` | Example route and control |
| `GET /health` | Is the service up, is the model loaded, is rate limiting on |
| `GET /log` | The audit log, as JSON |
| `POST /submit` | Score a piece of text, log the decision, return the result |
| `POST /appeal` | Contest a decision by `content_id` |

---

## Commands

| Command | What it does |
|---|---|
| `python test.py` | Checks the environment |
| `python app.py` | Runs the service |
| `python detector.py` | Downloads the model and scores a sample |
| `python detector.py "some text"` | Score one piece of text from the terminal |
| `python stylometry.py "some text"` | The style measures for one piece of text |
| `python run_attacks.py --set <folder>` | Runs the attack set |
| `python run_attacks.py --flood 15` | Pushes past the rate limit and prints the status codes |
| `python run_eval.py --label before` | Runs the five criteria, three trials each |
| `python run_appeals.py --label before` | Runs the appeal path check (criterion 4) |

---

## Turning on rate limiting

1. In `config.py`, set `RATE_LIMITING_ENABLED = True`, or run with
   `AI201_RATE_LIMITS=1`.
2. Choose the numbers there.

Then push past the limit and watch for `429`:

```bash
python run_attacks.py --flood 15
```

That sends 15 submissions from one `creator_id` and prints the run of status
codes (`200 200 200 ... 429 429`). It also writes `results/flood_<date>.md`.

The attack set can't do this. Every attack row submits under its own
`creator_id`, so a full attack run looks like dozens of different callers and
never trips a limit.

No `429` at all? Either the limit is above 15 a minute, or rate limiting is
still off. `GET /health` reports which.

Rejections are logged. An attack that shows up only as an absence is one that
never gets found.

---

## Running it somewhere else

Flask's built-in server says "development server" on startup because that is
what it is. A real one comes from `gunicorn`:

```bash
gunicorn app:app --bind 0.0.0.0:$PORT
```

Three settings, all read from the environment:

| Variable | Default | What it does |
|---|---|---|
| `HOST` | `127.0.0.1` | Loopback, this machine only. A host needs `0.0.0.0`, or nothing outside the box can reach the service |
| `PORT` | `5000` | Most hosts hand over a port in `PORT` and expect the app to bind exactly that one |
| `AI201_DEBUG` | `1` | Debug mode. Off automatically whenever `HOST` isn't loopback |

With no variables set you get `http://127.0.0.1:5000` and every `curl` above
still works.

### This project will not fit a free host

| What has to be in memory | Roughly |
|---|---|
| `torch` | ~200-800 MB depending on the build |
| the `gpt2` weights | ~550 MB on disk, loaded into RAM to score |
| Flask, gunicorn, the code | the rest |
| **A free tier gives you** | **512 MB** |

That is over budget before a single request arrives, and a free host has no
persistent disk, so the 550 MB download starts again after every idle
spin-down. No configuration fixes this. The right deployment for this project
is local, with logs.

---

## Where everything lives

| File | What it does |
|---|---|
| `config.py` | Every setting: thresholds, weights, rate limits, the model |
| `app.py` | The service and its routes |
| `detector.py` | Signal one: the local language model |
| `stylometry.py` | Signal two: style measures |
| `phrases.py` | Signal three: stock phrases |
| `scoring.py` | Combining the signals and labelling the score |
| `audit.py` | The audit log writer |
| `calibrate.py`, `score_my_writing.py` | Calibration helpers |
| `run_attacks.py` | Runs the attack set |
| `run_eval.py`, `scenarios.py` | Runs the five criteria three times |
| `run_appeals.py` | Checks the appeal path |
| `rotate_creators.py` | Rotates creator ids for load runs |
| `criteria.md` | The five acceptance criteria |
| `logs/audit.jsonl` | The audit log |
| `results/` | Attack runs and run logs |

`logs/` and `results/` are deliberately not in `.gitignore`. The audit log is
evidence.

---

## The two blind spots

**Signal one** measures how *predictable* the text is. Predictability isn't
authorship. What it rewards is common words in short, ordinary sentences:
someone writing in a second language and staying with vocabulary they're sure
of, a younger writer, anyone writing plainly on purpose. That writing scores
about as machine-like as machine writing does. (Dense, ornate prose often goes
the other way and reads as human, because rare words are what a language model
fails to predict.) So the writers this signal is most likely to accuse are the
ones with the least room to argue back. That is the false positive the whole
project is about, and it is structural rather than a bug.

**Signal two** cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it: typos, broken-up
sentences, a pasted quotation. That is cheap to do on purpose.

---

## When something goes wrong

| What you see | What it means |
|---|---|
| `404` from curl | Is the server running? Is the path exactly what you typed? |
| `Cannot bind parameter 'Headers'` | PowerShell, where `curl` is a different tool. Use `curl.exe`, on one line |
| Request body arrives empty | curl needs `-H "Content-Type: application/json"` |
| `Address already in use` | A server left running from an earlier attempt. Kill it |
| The first submission takes 10+ seconds | Signal one is loading the model into memory. Later ones take a second or two |
| *Every* submission takes 10+ seconds | Something is reloading the model each call. `GET /health` shows `detector_loaded`; if it goes back to `false`, look for a reload in the handler |
| `DetectorUnavailable` | Run `python detector.py` once to download the model |
| `/appeal` seems to do nothing | Does the `content_id` sent actually exist in the log? |
| Every request gets through, no `429` ever | Limiting is still off. Set `RATE_LIMITING_ENABLED` in `config.py` |
| Flask-Limiter warns about storage | `storage_uri` is preconfigured. If it was changed, put it back |
| One of the three labels never appears | The ranges have a gap. `scoring.label_ranges()` prints them |
