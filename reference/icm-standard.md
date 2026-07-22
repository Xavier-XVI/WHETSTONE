# Reference — the single-specialist ICM standard

The yardstick WHETSTONE measures a target against. ICM ("interpretable context methodology") treats the folder as architecture: drop it into a Claude project and Claude *becomes* the specialist. A single-specialist ICM agent is a folder where **each file does one job**. This file describes what "healthy" looks like so you can name where a target diverges from it.

## The five files and the one job each does

**`identity.md` — who the specialist is and what work it handles.**
Healthy: a reader can state, from this file alone, the agent's job to be done, what it takes in, and what it refuses. Rotten: a mission statement with no operational edges ("a helpful writing assistant"), or an identity that quietly contradicts the rules.

**`rules.md` — how the specialist behaves. The real logic lives here.**
Healthy: behaviors are specific, ordered, and — where they matter — enforced (a gate, a refusal, a required step), not just asserted. Rotten: a wall of `must`/`always` that nothing checks; advice a competent reader would already follow; rules that contradict each other or the identity.

**`examples.md` — what good output looks like.**
Healthy: 1–3 worked cases that demonstrate the rules in action, in the agent's real domain, proofed, with any quoted material appearing verbatim in its source. Rotten: aspirational examples that the rules don't actually produce; made-up quotes; placeholders; a single toy case.

**`reference/` — the frameworks, checklists, and data the rules draw on.**
Healthy: contains exactly what the rules depend on, and everything in it is referenced by something. Rotten: rules that lean on knowledge the reference layer doesn't hold (an empty dependency), or reference files nothing else mentions (dead weight).

**`README.md` — how a stranger uses it.**
Healthy: a stranger can install and run the agent, and knows within 30 seconds what to hand it and what they'll get back. Rotten: assumes the builder's context; no concrete invocation; no "try it" case.

## Signs of a healthy folder

- The five files agree with each other. Identity, rules, and examples tell one consistent story.
- The scope is narrow enough that generic advice would be useless inside it.
- The load-bearing rules are enforced, not merely stated.
- Nothing is promised that isn't delivered (no empty "memory," no aspirational example).
- A stranger can run it from the README alone.

## Signs of rot (divergence leads)

- You cannot state the JTBD after reading `identity.md`.
- Scope is so broad the agent must silently choose what to do or refuse.
- `must`/`should`/`never` appears in prose with nothing enforcing it.
- Examples show behavior the rules don't produce, or contradict them.
- Rules depend on a framework that isn't in `reference/`.
- The README only makes sense if you already built the thing.

These map one-to-one onto the six lenses in `lenses.md`.

## Note on the ICM method itself

The power — and the failure mode — of treating the folder as architecture is that the folder is the whole mind. Anything the builder "knows" but didn't write down is not in the agent. WHETSTONE's entire leverage is finding the gap between what the builder knows and what the folder actually says.
