# WHETSTONE review log
- agent: <target agent name>
- target: <path or repo URL of the reviewed folder>
- date: <YYYY-MM-DD>
- reviewer: WHETSTONE
- status: IN_PROGRESS

<!-- Do NOT hand-edit status to COMPLETE. close_review.py stamps this.
     Each DECISION block MUST keep its two marker lines exactly:
       - IMPACT: high | med | low
       - STATUS: OPEN | RESOLVED | DEFERRED
     close_review.py returns INCOMPLETE if any IMPACT: high block is STATUS: OPEN. -->

## 1. JTBD (anchor)
- builder stated (verbatim): "<...>"
- anchor-check outcome: "<one-sentence agreed JTBD, or the ambiguity found>"

## 2. verify.py — before
```
<paste verify.py report here>
```

## 3. Defects
- D1: <file:line> — <miss> — <obvious fix>

## 4. Decisions

### DECISION #1 — <lens> — <file:line>
- IMPACT: high
- STATUS: OPEN
- collides when: "<the concrete input that exposes the gap>"
- branch A: "<choice>" → costs: "<consequence>"
- branch B: "<choice>" → costs: "<consequence>"
- what only you know: "<the outside knowledge this turns on>"
- builder answer (verbatim): "<...>"
- gate press (if any): "<the breaking input WHETSTONE raised>"
- builder reply (verbatim): "<...>"
- resolution note: "<choice + reason, or deferral reason>"

## 5. verify.py — after
```
<paste verify.py report after fixes here>
```

## 6. Close
- close_review.py verdict: <COMPLETE | INCOMPLETE>
- still open: <list, or none>
