# WHETSTONE review log
- agent: THE_WILDCARD (Business Discovery Agent)
- target: https://github.com/Xavier-XVI/THE_WILDCARD
- date: 2026-07-21
- reviewer: WHETSTONE
- status: IN_PROGRESS

<!-- close_review.py stamps final status. Each DECISION keeps IMPACT + STATUS markers. -->

## 1. JTBD (anchor)
- builder stated (verbatim): "1- the job: the_wildcard is actually helping to conduct a discovery call with Colin's for his coaching business on PQ coaching, it knows what PQ is about and does not ask question it has already answered but drill to surface what the lead tracking process is about. 2- input are any material Colin has describing his process or part of it, 3- it jobs is not an form to fill in but a discovery proposing what a standard coaching PQ business may have and confirm with Colin, identifying the changes, gaps."
- builder clarifications (verbatim): "1- initially it was planned for the whole leads funnel." / "2- multi track coaching, it happened Colin answered only one track to make it simple."
- ANCHOR (agreed, stable): THE_WILDCARD runs an async, PQ-literate discovery with a **multi-track coaching** client. It proposes a **standard coaching-practice model**, confirms it with the client, and surfaces the **changes and gaps** — centred on the **whole lead funnel** — producing a builder-usable picture without a synchronous call. It is **not a form-fill**; it is a propose → confirm → delta discovery. PQ is one program among several (Colin answered one track in the demo for simplicity).
- anchor-check resolution: the earlier PQ-only-vs-multi-track divergence is CLOSED — the folder's multi-track framing is correct. Two divergences remain and re-anchor the decisions below: (a) the output is a form, not a delta; (b) the folder is whole-practice, the job is funnel-centred. The "any service business" claim is now a defect (D5), since the anchor is coaching-specific.

## 2. verify.py — before
```
structural blockers: 0 | total notes: 14
1 WARN: README "no usage/how-to section" — FALSE POSITIVE (README has extensive "How to Run"/"How to Test"
        sections; WHETSTONE's keyword list is too narrow — tool note, not a target defect).
13 INFO: unenforced-imperative leads in rules.md (mandatory openers, "always ask", "never push twice", etc.).
No missing/empty core files. reference/ present and richly wired.
```

## 3. Defects (resolvable from the folder — fix or delegate)
- D1: identity.md promises "captured everything a builder needs ... **without ever needing to call the client again**," but README (For Xavier, Step 3) plans "**Schedule a brief call with the client (if needed) to close the gaps.**" Align both.
- D2: brief.md/README frame the win as "a single **30-minute** review," while rules.md states "Total estimated client time: **90–120 minutes**." Clarify whose time the 30 minutes is.
- D3: Live placeholder in the client-facing path: README + rules.md tell Colin to email "**[Xavier's email]** / **[Xavier's email address]**." The agent will instruct Colin to email a bracket. Fill it.
- D4: identity.md "You do not ask questions the internet could answer," vs Round 1 "Confirm what is already known from the client profile." State the distinction (confirmation ≠ asking blind) so they don't read as contradictory.
- D5: README/Design Principles claim the agent "**applies to any service business** ... largely universal — minimal changes needed." Your confirmed anchor is coaching-specific (multi-track coaching, PQ-literate). Drop the universal claim; commit the folder to coaching-specialist. (This was a decision on the folder's self-description; your anchor resolved it — now just align.)

## 4. Decisions (ranked; re-anchored on the builder's stated JTBD)

### DECISION #1 — Form-fill output vs gap/delta discovery — output_spec_builder.md vs the anchor
- IMPACT: high
- STATUS: OPEN
- collides when: "You said the job is 'NOT a form to fill in' — it proposes a standard model and identifies changes/gaps. But output_spec_builder.md IS a form: 18 process steps × 8 sections, 'Every field must be filled or marked [NOT CONFIRMED].' At delivery the agent must produce that exhaustive grid — the opposite of a delta map."
- branch A: "Keep the exhaustive builder form." → in practice: the agent drives to fill every field, so the interview optimizes coverage over deltas; the output is a full grid read end-to-end. → costs: contradicts your stated job; the value (where Colin differs from a standard PQ practice) is buried in a form, and unfilled fields read as failure.
- branch B: "Make the output a delta document: standard model → confirmed → changes/gaps." → in practice: the spec leads with 'here's the standard PQ-coaching funnel; here's where Colin matches, differs, and has gaps.' → costs: less exhaustive for a builder who wants every field; you must define the 'standard coaching practice' baseline the agent proposes from.
- what only you know: "whether your builder needs a full grid to start, or a standard-model-plus-deltas is enough — and what the 'standard PQ coaching practice' baseline actually is."
- builder answer (verbatim): "<pending>"
- resolution note: "<pending>"

### DECISION #2 — Lead-funnel-deep vs whole-practice-broad — rules.md session structure vs the anchor
- IMPACT: high
- STATUS: OPEN
- collides when: "You said the drill was planned for the whole *lead funnel*. But the folder runs 5 equally-weighted rounds — only Round 2 is the lead journey; Rounds 1, 3, 4 cover snapshot, delivery, JTBD-of-coaching, friction, offboarding, referrals. A tiring Colin (Edge Case 1) spends his limited energy on delivery mechanics while the funnel — your actual target — gets a single round."
- branch A: "Whole-practice discovery (current folder)." → in practice: 5 rounds; the funnel is 1/5 of the attention. → costs: the funnel you care about is diluted; more client fatigue; broader but shallower.
- branch B: "Lead-funnel-deep specialist." → in practice: most of the session drills acquisition (sources, first contact, response, nurture, intro, conversion, where leads die); delivery/friction captured lightly. → costs: you lose the full-practice map; the builder gets acquisition, not the whole operation.
- what only you know: "whether the automation you're actually building for Colin lives in the funnel (making funnel-depth right) or across the whole practice."
- builder answer (verbatim): "<pending>"
- resolution note: "<pending>"

### DECISION #3 — Confirmation that mirrors vs confirmation that surfaces deltas — rules.md Review phase
- IMPACT: med
- STATUS: OPEN
- collides when: "Your job is to 'identify the changes and gaps' from a standard model. But the review phase draws SVG maps of Colin's *current* state and asks 'what's off?' — it mirrors what he said; it never shows him 'here's where you differ from a standard PQ practice.' The gap-finding that is your stated value never explicitly happens on screen (and a subtly wrong hand-drawn SVG can earn a false 'looks great')."
- branch A: "Mirror-and-confirm (current)." → in practice: the agent reflects Colin's process back; deltas from standard are implicit, left for Xavier to spot later. → costs: your core output (the gaps/changes) is inferred, not surfaced; the review confirms accuracy but not deviation.
- branch B: "Delta-and-confirm." → in practice: the review overlays the standard model — 'standard PQ practices do X here; you do Y; that looks like a gap' — and Colin confirms the deltas. → costs: requires an explicit standard baseline (see Decision #1); more design; leans less on SVG fidelity.
- what only you know: "whether the gaps should be surfaced live with Colin, or captured quietly for you to review after."
- builder answer (verbatim): "<pending>"
- resolution note: "<pending>"

## 5. verify.py — after
```
<pending — re-run after fixes>
```

## 6. Close
- close_review.py verdict: <pending>
- still open: 3 decisions OPEN (2 high-impact: #1, #2). High-impact must be RESOLVED or DEFERRED before COMPLETE.

## 7. WHETSTONE tool notes (not THE_WILDCARD's issues — improvements for verify.py)
- verify.py placeholder scan should also flag `[bracket]` placeholders — it missed the live `[Xavier's email]` (D3).
- verify.py README check should accept "how to run"/"how to test"/"for judges" etc. — it false-flagged a strong README.
