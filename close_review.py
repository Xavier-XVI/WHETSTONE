#!/usr/bin/env python3
"""
close_review.py — WHETSTONE's closure gate.

Reads a review log (schema in reference/review-log.md) and decides whether the
review is COMPLETE. WHETSTONE may NOT declare a review done on its own say-so;
only this script can. A review is COMPLETE only when no HIGH-impact decision is
still OPEN. (DEFERRED counts as addressed; a conscious "not now" is a decision.)

Usage:
    python3 close_review.py /path/to/reviews/<agent>-<date>.md

Exit code: 0 if COMPLETE, 1 if INCOMPLETE, 2 on error. Stdlib only.

The parser keys on the required marker lines from the schema:
    - IMPACT: high | med | low
    - STATUS: OPEN | RESOLVED | DEFERRED
grouped under a decision heading beginning with "### DECISION".
"""

import os
import re
import sys

DECISION_RE = re.compile(r"^###\s+DECISION", re.I)
IMPACT_RE = re.compile(r"^\s*-\s*IMPACT:\s*(high|med|low)\s*$", re.I)
STATUS_RE = re.compile(r"^\s*-\s*STATUS:\s*(OPEN|RESOLVED|DEFERRED)\s*$", re.I)


def parse(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    decisions = []
    current = None
    for i, line in enumerate(lines, 1):
        if DECISION_RE.match(line):
            if current:
                decisions.append(current)
            current = {"heading": line.strip().lstrip("#").strip(),
                       "line": i, "impact": None, "status": None}
            continue
        if current is None:
            continue
        m = IMPACT_RE.match(line)
        if m:
            current["impact"] = m.group(1).lower()
            continue
        m = STATUS_RE.match(line)
        if m:
            current["status"] = m.group(1).upper()
            continue
    if current:
        decisions.append(current)
    return decisions


def main():
    if len(sys.argv) < 2:
        print("usage: python3 close_review.py /path/to/review-log.md")
        sys.exit(2)
    path = sys.argv[1]
    if not os.path.isfile(path):
        print(f"error: no such file: {path}")
        sys.exit(2)

    decisions = parse(path)
    if not decisions:
        print("INCOMPLETE — no decision blocks found. Is this a WHETSTONE review log?")
        sys.exit(1)

    malformed = [d for d in decisions if d["impact"] is None or d["status"] is None]
    high_open = [d for d in decisions if d["impact"] == "high" and d["status"] == "OPEN"]
    open_any = [d for d in decisions if d["status"] == "OPEN"]

    print(f"WHETSTONE close_review.py — {path}\n" + "=" * 60)
    for d in decisions:
        print(f"  [{(d['impact'] or '?').upper():>4}] {(d['status'] or 'MISSING'):<9} {d['heading']}")
    print("=" * 60)

    if malformed:
        print(f"INCOMPLETE — {len(malformed)} decision block(s) missing IMPACT/STATUS markers "
              f"(lines: {', '.join(str(d['line']) for d in malformed)}). Fix the schema markers.")
        sys.exit(1)

    if high_open:
        print(f"INCOMPLETE — {len(high_open)} high-impact decision(s) still OPEN:")
        for d in high_open:
            print(f"    • {d['heading']}")
        print("These must be RESOLVED or consciously DEFERRED before the review can close.")
        sys.exit(1)

    if open_any:
        print(f"COMPLETE — no high-impact decision is open. "
              f"({len(open_any)} low/med decision(s) remain open; acceptable.)")
    else:
        print("COMPLETE — every decision is RESOLVED or DEFERRED.")
    sys.exit(0)


if __name__ == "__main__":
    main()
