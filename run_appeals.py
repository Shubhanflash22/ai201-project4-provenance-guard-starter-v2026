#!/usr/bin/env python3
"""
Criterion 4: for 5 submitted items, an appeal returns status "under_review"
and a matching appeal entry appears in GET /log for that content_id.

    python app.py                              # in one terminal
    python run_appeals.py --label before       # in another

Each trial submits 5 texts, appeals each one, then reads the log back.
Runs 3 trials by default and writes results/appeals_<date>_<label>.md.
"""

import argparse
import datetime as dt
import json
import sys

import requests

import config

TEXTS = [
    "The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must be able to handle a wide variety of different inputs. Additionally, the overall performance of the solution depends on a number of important variables.",
    "Honestly I burned the toast again this morning, set off the smoke alarm, and my cat bolted under the couch like I had committed a crime. Third time this week. Not great.",
    "Short answer: yes. The implementation of the proposed framework requires careful consideration of several key factors, and it is important to note that the system must be able to handle a wide variety of different inputs, because the overall performance of the solution depends on a number of important variables, which is why careful planning matters. Clearly, this is important.",
    "I like my school. It is big. I have many friends. We play games at lunch. My teacher is nice. She helps me a lot. I want to go to college.",
    "The implementation of the proposed framework requires careful considration of several key factors. First, it is important to note that the system must handle a wide variety of inputs. Additionally, overall performance depends on a number of variables. Which matters.",
]


def one_trial(url):
    results = []
    for i, text in enumerate(TEXTS, 1):
        row = {"item": i}
        try:
            submit = requests.post(
                f"{url}/submit",
                json={"text": text, "creator_id": f"eval_appeal_{i}"},
                timeout=90,
            )
            row["submit_status"] = submit.status_code
            content_id = submit.json().get("content_id")
            row["content_id"] = content_id

            appeal = requests.post(
                f"{url}/appeal",
                json={"content_id": content_id, "reasoning": "I wrote this myself."},
                timeout=30,
            )
            row["appeal_status"] = appeal.status_code
            row["appeal_response_status"] = appeal.json().get("status")

            entries = requests.get(f"{url}/log", timeout=30).json()["entries"]
            row["in_log"] = any(
                e.get("content_id") == content_id
                and e.get("event") == "appeal"
                and e.get("status") == "under_review"
                for e in entries
            )
            row["passed"] = bool(
                content_id
                and row["appeal_status"] == 200
                and row["appeal_response_status"] == "under_review"
                and row["in_log"]
            )
        except Exception as exc:  # noqa: BLE001
            row["error"] = f"{type(exc).__name__}: {exc}"
            row["passed"] = False
        results.append(row)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=f"http://{config.HOST}:{config.PORT}")
    args = parser.parse_args()

    try:
        requests.get(f"{args.url}/health", timeout=5)
    except Exception:  # noqa: BLE001
        print(f"Nothing answering at {args.url}. Start it:  python app.py",
              file=sys.stderr)
        sys.exit(1)

    trials = []
    for trial in range(1, args.trials + 1):
        results = one_trial(args.url)
        passed = sum(r["passed"] for r in results)
        trials.append(results)
        print(f"trial {trial}: {passed}/{len(results)} appeals returned under_review "
              f"and appear in the log")

    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"appeals_{stamp}{label}.md"
    lines = [
        f"# Appeal path (criterion 4){f' — {args.label}' if args.label else ''}",
        "",
        "- Produced by: `run_appeals.py::main`",
        f"- {args.trials} trials · {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "| Trial | Appeals that returned under_review and appear in the log |",
        "|---|---|",
    ]
    for n, results in enumerate(trials, 1):
        lines.append(f"| {n} | {sum(r['passed'] for r in results)}/{len(results)} |")
    lines += ["", "---", "", "## What actually came back", ""]
    for n, results in enumerate(trials, 1):
        lines += [f"**Trial {n}**", "", "```json", json.dumps(results, indent=2), "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
