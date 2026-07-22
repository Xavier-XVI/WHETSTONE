#!/usr/bin/env python3
"""
verify.py — WHETSTONE's deterministic floor.

Runs mechanical, non-judgment checks on a TARGET single-specialist ICM folder and
prints a report. It reports FACTS only; it never judges quality. Its output feeds
WHETSTONE's lenses as *leads*, not verdicts.

Usage:
    python3 verify.py /path/to/target-agent-folder
    python3 verify.py /path/to/target-agent-folder --json

Exit code: 0 if no blocking structural problems, 1 otherwise. Stdlib only.
"""

import os
import re
import sys
import json

ICM_FILES = ["identity.md", "rules.md", "examples.md", "README.md"]
# word-like tokens are matched on word boundaries (so "TBD" does not fire inside "JTBD",
# and "PLACEHOLDER" does not fire inside "placeholders"); symbol tokens match as substrings.
PLACEHOLDERS_WORD = ["TODO", "TBD", "XXX", "FIXME", "PLACEHOLDER"]
PLACEHOLDERS_SUB = ["Lorem ipsum", "<...>"]
IMPERATIVES = ["must", "should", "always", "never", "require"]


def read(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except (OSError, UnicodeDecodeError):
        return None


def est_tokens(text):
    # crude but consistent: ~4 chars per token
    return max(1, len(text) // 4)


def check_structure(folder):
    findings = []
    present = {}
    for name in ICM_FILES:
        p = os.path.join(folder, name)
        content = read(p) if os.path.isfile(p) else None
        present[name] = content
        if content is None:
            findings.append(("BLOCK", f"missing file: {name}"))
        elif not content.strip():
            findings.append(("BLOCK", f"empty file: {name}"))
    ref = os.path.join(folder, "reference")
    if not os.path.isdir(ref):
        findings.append(("WARN", "no reference/ directory (single-specialist ICM usually has one)"))
    return findings, present


def check_placeholders(present, folder):
    findings = []
    files = dict(present)
    ref = os.path.join(folder, "reference")
    if os.path.isdir(ref):
        for fn in sorted(os.listdir(ref)):
            fp = os.path.join(ref, fn)
            if os.path.isfile(fp):
                files["reference/" + fn] = read(fp)
    for name, content in files.items():
        if not content:
            continue
        for line_no, line in enumerate(content.splitlines(), 1):
            for token in PLACEHOLDERS_WORD:
                if re.search(r"\b" + re.escape(token) + r"\b", line, re.I):
                    findings.append(("WARN", f"{name}:{line_no} placeholder '{token}': {line.strip()[:80]}"))
            for token in PLACEHOLDERS_SUB:
                if token.lower() in line.lower():
                    findings.append(("WARN", f"{name}:{line_no} placeholder '{token}': {line.strip()[:80]}"))
    return findings


def check_imperatives(present):
    """List every unenforced-imperative CANDIDATE in rules.md. Judgment stays with WHETSTONE."""
    findings = []
    rules = present.get("rules.md")
    if not rules:
        return findings
    for line_no, line in enumerate(rules.splitlines(), 1):
        low = line.lower()
        if any(re.search(r"\b" + w + r"\b", low) for w in IMPERATIVES):
            findings.append(("INFO", f"rules.md:{line_no} imperative — ask 'what enforces this?': {line.strip()[:90]}"))
    return findings


def check_reference_wiring(present, folder):
    findings = []
    ref = os.path.join(folder, "reference")
    if not os.path.isdir(ref):
        return findings
    # gather all text outside reference/ plus reference files themselves
    corpus = " ".join(v for v in present.values() if v)
    ref_files = [fn for fn in os.listdir(ref) if os.path.isfile(os.path.join(ref, fn))]
    corpus_all = corpus + " " + " ".join(
        (read(os.path.join(ref, fn)) or "") for fn in ref_files
    )
    for fn in sorted(ref_files):
        stem = os.path.splitext(fn)[0]
        # mentioned by full name or stem anywhere?
        if fn not in corpus_all and stem not in corpus_all:
            findings.append(("WARN", f"reference/{fn} is referenced by nothing (dead weight?)"))
    return findings


def check_readme(present):
    findings = []
    readme = present.get("README.md")
    if not readme:
        return findings
    low = readme.lower()
    if not any(k in low for k in ["how to use", "usage", "quickstart", "getting started", "try it", "how it works"]):
        findings.append(("WARN", "README.md has no usage/how-to section a stranger can follow"))
    if "```" not in readme and not re.search(r"^\s*(\$|>|\d+\.)", readme, re.M):
        findings.append(("WARN", "README.md has no concrete invocation / example block"))
    return findings


def check_token_weight(present, folder):
    findings = []
    weights = {}
    for name, content in present.items():
        if content:
            weights[name] = est_tokens(content)
    ref = os.path.join(folder, "reference")
    if os.path.isdir(ref):
        for fn in sorted(os.listdir(ref)):
            fp = os.path.join(ref, fn)
            if os.path.isfile(fp):
                c = read(fp)
                if c:
                    weights["reference/" + fn] = est_tokens(c)
    if weights:
        vals = sorted(weights.values())
        median = vals[len(vals) // 2]
        for name, w in weights.items():
            if w > max(4 * median, 1200):
                findings.append(("INFO", f"{name} ~{w} tokens dwarfs the folder (median ~{median}) — bloat tell?"))
    return findings, weights


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_json = "--json" in sys.argv
    if not args:
        print("usage: python3 verify.py /path/to/target-agent-folder [--json]")
        sys.exit(2)
    folder = args[0]
    if not os.path.isdir(folder):
        print(f"error: not a folder: {folder}")
        sys.exit(2)

    all_findings = []
    struct, present = check_structure(folder)
    all_findings += struct
    all_findings += check_placeholders(present, folder)
    all_findings += check_imperatives(present)
    all_findings += check_reference_wiring(present, folder)
    all_findings += check_readme(present)
    weight_findings, weights = check_token_weight(present, folder)
    all_findings += weight_findings

    blocking = [f for f in all_findings if f[0] == "BLOCK"]

    if as_json:
        print(json.dumps({
            "folder": folder,
            "blocking": len(blocking),
            "findings": [{"level": lvl, "message": msg} for lvl, msg in all_findings],
            "token_weights": weights,
        }, indent=2))
    else:
        print(f"WHETSTONE verify.py — target: {folder}\n" + "=" * 60)
        order = {"BLOCK": 0, "WARN": 1, "INFO": 2}
        for lvl, msg in sorted(all_findings, key=lambda x: order.get(x[0], 9)):
            print(f"[{lvl}] {msg}")
        print("=" * 60)
        print(f"structural blockers: {len(blocking)} | total notes: {len(all_findings)}")
        print("NOTE: these are leads, not verdicts. Judgment (defect vs decision) is WHETSTONE's.")

    sys.exit(1 if blocking else 0)


if __name__ == "__main__":
    main()
