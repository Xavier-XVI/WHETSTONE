# Reference — the decision ledger format

WHETSTONE does not return prose feedback. It returns a **ranked ledger** with two parts: defects (fix or delegate) and decisions (illustrated, unfilled, for the builder to resolve).

---

## Part 1 — Defects (fix or delegate)

A plain, numbered list. Each item: `file:line` + the miss + the obvious fix. No ceremony — these are cheap, and pretending otherwise wastes the builder's attention.

```
DEFECTS (resolve or hand to a model — no judgment needed)
D1. rules.md L22 — cites "the CRAAP checklist"; no such file in reference/. Add it or stop citing it.
D2. examples.md L8 — quotes identity.md as "reviews policy memos" but identity.md L3 says "policy briefs". Fix the quote.
D3. README.md — no "how to use" section and no example invocation. Add both.
```

## Part 2 — Decisions (ranked; the vital few)

Ranked by JTBD impact, capped at ~5 in the first pass. Note if more exist. Each entry uses this exact shape:

```
DECISION #n — [lens] — [file:line] — [JTBD impact: high | med]
You said the job is:   "<the builder's own stated JTBD, verbatim>"
Your folder says:       "<quote from the folder>"
These collide when:     <one concrete input, from the agent's real domain, that exposes the gap>
  Branch A: <the choice in a phrase>
     → in practice: <2-line sketch of the agent's behavior under A, on that input>
     → costs the JTBD: <the specific consequence>
  Branch B: <the choice in a phrase>
     → in practice: <2-line sketch of the agent's behavior under B, on that input>
     → costs the JTBD: <the specific consequence>
What only you know:     <the outside knowledge this choice turns on>
YOUR CALL: I choose ____ because ____
```

## Rules for a good ledger entry

- **The `YOUR CALL` line stays blank.** WHETSTONE never fills it (Gate 4).
- **Illustration is mandatory and domain-real.** Both branches get a behavior sketch on the *same* concrete input, drawn from the agent's actual domain — not "the agent might behave differently." The illustration is what makes the decision fast to resolve; without it the builder is back to abstract reasoning.
- **"What only you know" must be real outside knowledge.** If you can't name knowledge outside the folder that the choice requires, it isn't a decision — reclassify it as a defect (Gate 3).
- **Two branches minimum, both defensible.** If one branch is obviously wrong, it's a defect, not a fork.
- **Impact is honest.** Reserve `high` for decisions that, chosen wrong, break the job. Everything else is `med`. Low-impact forks are noted, not surfaced.

## Triage (Gate 5)

1. Type every finding (defect vs decision).
2. For decisions, score JTBD impact: **high** = wrong branch breaks the job; **med** = wrong branch degrades it; **low** = cosmetic.
3. Surface all defects (they're cheap) + the top 3–5 decisions by impact. If more decisions exist, end with: `(N more lower-impact decisions available — say "more" to see them.)`
4. Never dump the full set unprompted. A twenty-item ledger gets abandoned; an abandoned ledger has zero value.

## Why this survives outsourcing

Hand this ledger to a model and say "improve the agent," and it will fill every `YOUR CALL` using information it does not have — picking a branch silently, plausibly, and often wrongly. That reproduces the exact failure the agent already had: an unexamined assumption coded in as if it were settled. The only way to extract value is for the human to fill the blanks. That is the design, not a side effect.
