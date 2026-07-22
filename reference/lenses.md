# Reference — the six divergence lenses

How WHETSTONE looks for the gap between the stated JTBD and what the folder actually does. Each lens has: **what it hunts**, **sharp criteria** (what to actually check), **the usual type** (defect or decision), and **the classification test** applied.

The classification test is always the same (Gate 3): *can this be correctly resolved using only the folder + the stated JTBD?* Yes → **defect** (state it, delegate it). No → **decision** (illustrate it, hand it back, never resolve it).

---

## Lens 1 — Job clarity
**Hunts:** ambiguity in the JTBD itself. Can `identity.md` be read two ways? Is "done" defined?
**Check:** Try to state the JTBD in one sentence. If you can produce two defensible sentences, it's ambiguous. Look for undefined success ("gives good feedback" — good how?), and for input words broad enough to smuggle in work the agent shouldn't touch.
**Anchor pressure-test (Gate 1 support):** Is it one job or several bolted together? Would generic advice be useless inside this scope, or could it apply to any agent?
**Usual type:** **Decision** — which of the two readings is the real job is knowledge in the builder's head.

## Lens 2 — Scope integrity
**Hunts:** scope wide enough that the agent must silently choose what to do, or what to refuse, with no rule telling it how.
**Check:** Find the edge cases that sit exactly on the boundary of the stated scope. For each, ask: does the folder tell the agent whether this is in or out? If not, the agent will decide arbitrarily and inconsistently.
**Usual type:** **Decision** — where the boundary *should* sit turns on what the builder wants the agent to own vs. refuse.

## Lens 3 — Enforcement gap
**Hunts:** load-bearing rules stated in prose that nothing enforces.
**Check:** For each `must`/`should`/`always`/`never`/`require` in `rules.md` (verify.py lists these), ask "what makes the agent actually do this?" A rule with a gate, a required step, or a refusal behind it is enforced. A rule that's just a sentence is a wish.
**Usual type:** **Defect** when the fix is obvious (add the gate) — *unless* whether to enforce it at all is a real trade-off (e.g., enforcing a clarifying-question step conflicts with a speed JTBD), in which case it's a **decision**.

## Lens 4 — Behavioral fidelity
**Hunts:** examples that contradict the rules, or demonstrate behavior the JTBD doesn't want; made-up quotes; placeholders.
**Check:** Read `examples.md` against `rules.md`. Does each example actually obey the rules? Does it show the agent doing the stated job the stated way? Are quoted passages real (verify.py string-matches these)?
**Usual type:** **Defect** (a contradictory or unproofed example is just wrong) — occasionally a **decision** if the example reveals the builder actually wants a behavior the rules forbid, exposing an unmade choice about what the agent should do.

## Lens 5 — Reference sufficiency
**Hunts:** rules that depend on knowledge `reference/` doesn't contain (empty dependency), or reference files nothing uses (dead weight).
**Check:** For each rule that invokes a framework/checklist/standard, confirm it exists in `reference/`. For each file in `reference/`, confirm something points to it (verify.py flags the wiring).
**Usual type:** **Defect** — the fix (add the missing reference, or cut the dead file) is determinable from the folder.

## Lens 6 — Handoff usability
**Hunts:** a README that assumes knowledge a stranger doesn't have to do the job.
**Check:** Read `README.md` as someone who has never seen the folder. Can you install it, know what to hand it, and know what you'll get back? Is there a concrete invocation and a 30-second try-it case?
**Usual type:** **Defect** — missing usage sections have obvious fixes.

---

## Worked classification (the honest test in action)

**Finding A.** `rules.md` says "always confirm the user's intent before responding," but `identity.md`'s JTBD is "instant one-line feedback for expert users who value speed."
- Can folder + JTBD resolve it? No — you can't tell from the folder whether the builder values the safety of confirming or the speed they claimed. The two rules encode opposite priorities. → **Decision.** Illustrate: under "always confirm," an expert gets a clarifying question they find patronizing; under "never confirm," a genuinely ambiguous request gets a confident wrong answer. The builder must choose; it turns on how expert their users really are.

**Finding B.** `rules.md` references "the CRAAP checklist" but `reference/` contains no such file.
- Can folder + JTBD resolve it? Yes — the rule depends on a file that must exist; either add it or stop citing it. → **Defect.** State it, tell them to fix it, move on. Do not dress it up as a decision.

The discipline is symmetric: **do not inflate defects into decisions to look profound, and do not flatten decisions into defects to look decisive.** Getting this split right is the whole product.
