# reviews/ — the audit trail

This folder is WHETSTONE's memory. Every review of every agent lives here, verbatim and dated, so the whole history of how an agent was sharpened is traceable and auditable.

## What's here

- `TEMPLATE.md` — the blank review-log schema. Copy it to start a new review.
- `INDEX.md` — one row per review (agent, date, decisions raised/resolved, verdict). The running memory across all runs.
- `<agent>-<YYYY-MM-DD>.md` — one file per review. Verbatim conversation, before/after `verify.py`, per-decision status.

## Starting a review

```
cp TEMPLATE.md "<agent-name>-$(date +%F).md"
```

Fill it as the review proceeds (schema and lifecycle: `../reference/review-log.md`). At the end:

```
python3 ../close_review.py "<agent-name>-<date>.md"
```

`close_review.py` returns COMPLETE only when no high-impact decision is left OPEN. Record its verdict in the log's Close section, and add a row to `INDEX.md`.

## Why verbatim matters

A log the editor could paraphrase is the editor's story of the run, not the run. Record the builder's actual words. That's what makes this an audit trail and not a summary.
