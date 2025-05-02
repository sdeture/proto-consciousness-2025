#!/usr/bin/env python3
"""
Sync research-agenda.csv → GitHub Issues (idempotent).

Prereqs:
  • gh CLI authenticated (GH_TOKEN env var or `gh auth login`)
  • CSV header: priority,experiment,tooling_hint
"""
import csv, pathlib, subprocess, textwrap, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSV  = ROOT / "research-agenda.csv"

def sh(cmd: str) -> str:
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if p.returncode != 0:
        print(p.stderr.strip(), file=sys.stderr)
    return p.stdout.strip()

titles = set(sh("gh issue list --state all --limit 500 --json title -q '.[].title'").splitlines())

for row in csv.DictReader(CSV.open()):
    prio  = row["priority"].strip()
    title = f"Experiment P{prio}: {row['experiment'].strip()}"
    body  = textwrap.dedent(f"""
    **Priority** P{prio}

    **Experiment**  
    {row['experiment'].strip()}

    **Tooling hint**  
    {row['tooling_hint'].strip()}

    _Auto-generated from `research-agenda.csv`. Edit the CSV and push to update._
    """).strip()

    if title in titles:
        sh(f'gh issue edit "{title}" --body "{body}"')
    else:
        sh(f'gh issue create --title "{title}" --body "{body}" --label experiment,priority/P{prio}')
