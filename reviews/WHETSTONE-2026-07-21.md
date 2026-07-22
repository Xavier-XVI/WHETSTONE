# WHETSTONE review log
- agent: WHETSTONE (self-review)
- target: https://github.com/Xavier-XVI/WHETSTONE
- date: 2026-07-21
- reviewer: WHETSTONE (finding surfaced by the builder, Xavier, from two live runs)
- status: COMPLETE (close_review.py, 2026-07-21)

<!-- Dogfood entry. WHETSTONE reviewed against its own PRD after Xavier observed it skipping the JTBD-first turn on the SentinelRx and THE_WILDCARD runs. close_review.py stamps final status. -->

## 1. JTBD (anchor)
- builder stated (verbatim): "at first it should start asking for the JTBD and the few questions, prior running any python scripts. both tries went directly to running the script without asking what is the JTBD."
- ANCHOR: WHETSTONE elicits the builder's stated JTBD FIRST, then critiques an ICM folder against it — surfacing decisions the builder can't outsource, without rewriting the agent. "JTBD-first" is load-bearing: every finding is anchored to the elicited job.

## 2. verify.py — before
```
structural blockers: 0 | total notes: 19 (all INFO imperative-leads + the review-log schema <...> placeholders)
The mechanical floor was clean — this finding is NOT one verify.py can catch. It is a behavioral-ordering gap,
surfaced by a human running the agent. (Noted: the deterministic layer cannot police its own operator's turn order.)
```

## 3. Defects (resolvable from the folder)
- D1 — **FIXED this session.** JTBD-first was unenforced. Gate 1 said "you may not *critique* until you can state the JTBD," but running `verify.py` and reading files are not "critique," so an eager operator could go mechanical-first — which is exactly what happened on both runs. There was no dedicated first-turn rule. Irony noted: WHETSTONE's own core critique ("a `must` in prose is a request") applied to WHETSTONE itself.
  - FIX APPLIED: added "Session start — Turn 1 (hard stop)" block at the top of `rules.md` (first message must be the intake questions only; no reading-for-critique, no `verify.py`, no findings until the builder answers); closed the Gate 1 loophole ("may not read-for-critique, run `verify.py`, or produce any finding until…"); mirrored the first-turn rule in `identity.md`.
- D2 — **identified, not yet applied.** `verify.py` placeholder scan flags `<...>` but not `[bracket]` placeholders; it missed the live `[Xavier's email]` in the THE_WILDCARD run. Add a `[ ... ]` placeholder pattern.
- D3 — **identified, not yet applied.** `verify.py` README check false-flagged THE_WILDCARD's strong README because its keyword list lacks "how to run"/"how to test"/"for judges". Broaden the list.

## 4. Decisions

### DECISION #1 — Prose hard-stop vs runtime-enforced Turn-1 gate — rules.md Session start
- IMPACT: high
- STATUS: DEFERRED
- collides when: "An operator with tools (or an eager model) is handed a folder and *wants* to run the mechanical checks first. The new hard-stop tells it not to — but it is still prose. In a runtime that lets the model call a script, nothing physically prevents a Turn-1 violation; the rule relies on the operator obeying it."
- branch A: "Accept the prose hard-stop (now applied) — prominence + closed loophole + explicit 'no verify.py before intake' as the mitigation." → costs: still defeatable by an operator who ignores instructions; same class of gap WHETSTONE flags in others.
- branch B: "Runtime-enforced gate — a wrapper/harness that refuses to expose `verify.py` or the folder contents until an intake answer is recorded." → costs: engineering beyond pure ICM; not portable to a plain Claude Project (the very environment WHETSTONE targets).
- what only you know: "whether WHETSTONE will ever run in a harness you control (where B is possible), or always as a portable folder dropped into someone's project (where A is the ceiling)."
- builder answer (verbatim): "apply the edit to whetstone and note this as a review entry." → treated as: apply the prose hard-stop now (Branch A), defer the runtime gate.
- resolution note: DEFERRED — Branch A applied as the practical fix; Branch B (true runtime enforcement) carried, unsolved, and honestly the same limit as SentinelRx Decision #4. Revisit if/when WHETSTONE runs in a controlled harness.

## 5. verify.py — after
```
Re-ran on WHETSTONE after the edit: structural blockers: 0. The Turn-1 block and Gate 1 change are in place.
(D2/D3 verify.py improvements not yet applied — see Defects.)
```

## 6. Close
- close_review.py verdict: COMPLETE — every decision RESOLVED or DEFERRED (run 2026-07-21).
- still open: none blocking — D1 FIXED; Decision #1 DEFERRED with reason. D2/D3 are low-impact tool defects, open by choice (verify.py improvements, pending builder go-ahead).
