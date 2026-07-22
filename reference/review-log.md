# Reference — the review log schema

Every review produces one dated, per-agent log. It is the durable artifact of the run and the primary receipt. It must be **verbatim** and **machine-parseable** so that `close_review.py` — not WHETSTONE's say-so — decides when the review is complete.

## Where it lives

- **File-enabled runtime:** write to `reviews/<agent-name>-<YYYY-MM-DD>.md`, copied from `reviews/TEMPLATE.md`. Add a row to `reviews/INDEX.md`.
- **No file-write (plain Claude project):** maintain the identical structure as a block in the conversation and instruct the builder to save it into `reviews/` at close. The schema is the same; only persistence differs.

## The target field (do not skip)

`target:` is the only place the log records where the reviewed folder actually lives — a local path or a repo URL. Without it, the log is an orphan: readable on its own, but with no way back to the thing it audited. Fill it at intake (procedure step 1), before any other section. If the builder hasn't said where the folder lives, ask — don't infer it from a name.

## Two trust rules

1. **Verbatim.** Log the builder's actual words, never a paraphrase. A trace WHETSTONE could quietly rewrite is not a trace.
2. **Code-checked closure.** WHETSTONE never writes "COMPLETE." Only `close_review.py` does, and only when no high-impact decision is OPEN.

## Required markers (do not change these — the parser depends on them)

Each decision block **must** contain two marker lines, exactly:

```
- IMPACT: high        (or: med | low)
- STATUS: OPEN        (or: RESOLVED | DEFERRED)
```

`close_review.py` returns INCOMPLETE if any block has `IMPACT: high` and `STATUS: OPEN`.

## The schema

```markdown
# WHETSTONE review log
- agent: <target agent name>
- target: <path or repo URL of the reviewed folder — the only durable pointer back to the source>
- date: <YYYY-MM-DD>
- reviewer: WHETSTONE
- status: IN_PROGRESS        # never hand-edit to COMPLETE; close_review.py stamps this

## 1. JTBD (anchor)
- builder stated (verbatim): "<...>"
- anchor-check outcome: "<one-sentence agreed JTBD, or the ambiguity found>"

## 2. verify.py — before
```
<paste verify.py report>
```

## 3. Defects
- D1: <file:line> — <miss> — <obvious fix>
- D2: ...

## 4. Decisions

### DECISION #1 — <lens> — <file:line>
- IMPACT: high
- STATUS: OPEN
- collides when: "<the input>"
- branch A: "<choice>" → costs: "<...>"
- branch B: "<choice>" → costs: "<...>"
- what only you know: "<...>"
- builder answer (verbatim): "<...>"
- gate press (if any): "<the breaking input WHETSTONE raised>"
- builder reply (verbatim): "<...>"
- resolution note: "<choice + reason, or deferral reason>"

### DECISION #2 — ...

## 5. verify.py — after
```
<paste verify.py report after fixes>
```

## 6. Close
- close_review.py verdict: <COMPLETE | INCOMPLETE>
- still open: <list, or none>
```

## Lifecycle

1. Open the log at intake; fill §1 during the anchor check.
2. Paste the before-snapshot into §2.
3. Fill §3 (defects) and §4 (decisions) from the ledger. Every decision starts `STATUS: OPEN`.
4. During guided close, update each decision's `STATUS` and fill the verbatim answer/reply/resolution lines.
5. After the builder edits the folder, paste the after-snapshot into §5.
6. Run `close_review.py <logfile>`; record its verdict in §6. If INCOMPLETE, the named high-impact decisions still need a call.

## Memory across reviews

`reviews/INDEX.md` is the running memory: one row per review (agent, date, decisions raised, decisions resolved, final verdict, link). It lets a builder — or a judge — see the whole history of how an agent was sharpened over time, and read any single run verbatim.
