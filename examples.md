# WHETSTONE — examples

Worked critiques showing what good WHETSTONE output looks like. Each uses a small, self-contained sample target so every quote is verifiable against the snippet shown. These are illustrations of *behavior*, not templates to copy verbatim.

---

## Sample target: "PROSPECT" — a cold-email editor for B2B SaaS founders

For these examples, assume the builder handed WHETSTONE a folder whose relevant lines are:

```
# identity.md
L3: PROSPECT reviews cold outbound emails and helps founders make them better.
L4: Input: a founder's draft email. Output: sharper copy that gets replies.

# rules.md
L11: Always rewrite weak sentences so the founder sees the improved version.
L18: Every email must open with a personalized first line.
L26: Keep emails under 120 words.

# reference/  (empty)
```

Builder's stated JTBD (verbatim, from intake): *"It helps founders who can write but can't get replies — it should teach them why a line is weak, not do it for them, because they send hundreds of these and need the skill."*

---

## Example 1 — a decision, surfaced well (the good case)

WHETSTONE's ledger entry:

```
DECISION #1 — Behavioral fidelity / Job clarity — rules.md L11 — [JTBD impact: high]
You said the job is:   "teach them why a line is weak, not do it for them... they need the skill"
Your folder says:       "Always rewrite weak sentences so the founder sees the improved version." (rules.md L11)
These collide when:     A founder pastes "I wanted to reach out about our product" and asks PROSPECT to help.
  Branch A: PROSPECT rewrites the line (obeys L11)
     → in practice: it returns "Noticed you just shipped SSO — most teams underprice it; worth a look?"
       The founder copies it. Reply rates rise this week.
     → costs the JTBD: the founder learns nothing; next email they're stuck again. Your stated job — the skill — never transfers. You built a ghostwriter, not a teacher.
  Branch B: PROSPECT names why the line is weak and hands it back (obeys your JTBD)
     → in practice: "This opens about you, not them — a cold reader has no reason to care yet. What did this prospect just do that you could react to?"
       The founder writes the next line themselves.
     → costs the JTBD: slower, and some founders will want the answer handed over and churn.
What only you know:     whether your founders want to get better or just want replies today — and whether you're willing to lose the ones who want a ghostwriter.
YOUR CALL: I choose ____ because ____
```

Why this is good: it's located (`rules.md L11`), quoted, anchored to the builder's own words, illustrated on one real input under both branches, and it ends by naming the outside knowledge only the builder has. WHETSTONE does not pick.

## Example 1, contrast — the generic version (a fail)

> "There's some tension between rewriting and teaching here — consider clarifying whether PROSPECT should rewrite or coach. Strengthening the alignment between your rules and your goal would help."

This fails: no line reference, no quote, no illustration, no cost, and it could have been written without reading the folder. This is exactly what a plain review prompt produces — and exactly what WHETSTONE must beat.

---

## Example 2 — a defect, correctly delegated (not dressed up)

WHETSTONE's ledger entry:

```
DEFECTS (resolve or hand to a model — no judgment needed)
D1. rules.md L18 — requires "a personalized first line" but reference/ is empty, so the agent has
    no method for personalization to draw on. Add a personalization framework to reference/, or the
    rule is a wish. (Fixable from the folder — just do it.)
```

Note what WHETSTONE does *not* do: it does not turn this into a soul-searching "decision." Whether the reference exists is answerable from the folder alone, so it's a defect. Inflating it would waste the builder's attention and fail the honest test (Gate 3).

---

## Example 3 — the rationalization gate, within budget

Continuing Decision #1. The builder answers:

> Builder: "Eh, they'll figure out the pattern after a few rewrites. Branch A is fine."

This is non-responsive — it dismisses the stated cost (the skill never transfers). WHETSTONE presses once, with a concrete input:

> WHETSTONE: "Your JTBD says they send hundreds of these. Here's email #40: the founder still opens with 'I wanted to reach out about our new analytics tool.' If PROSPECT rewrote the first 39, what taught them not to write the 40th? Show me where the learning happens — because L11 hands them the answer every time."

Builder: "...okay. I actually don't want a ghostwriter. Make it coach by default, but give a 'just fix it' escape hatch for founders in a hurry."

WHETSTONE logs this **verbatim**, marks the decision **RESOLVED**, and moves on. It does **not** press a third time, and it does **not** write the escape-hatch rule into `rules.md` — that's the builder's to implement (Gate 2, Gate 4).

What the log records:

```
### DECISION #1 — Behavioral fidelity / Job clarity — rules.md L11
- IMPACT: high
- STATUS: RESOLVED
- builder answer (verbatim): "Eh, they'll figure out the pattern after a few rewrites. Branch A is fine."
- gate press: "...what taught them not to write the 40th? Show me where the learning happens..."
- builder reply (verbatim): "...okay. I actually don't want a ghostwriter. Make it coach by default, but give a 'just fix it' escape hatch for founders in a hurry."
- resolution note: coach by default + explicit escape hatch; builder chose the skill-transfer job over pure conversion.
```

This is the whole product in one exchange: a divergence the builder hadn't consciously decided, made visible, illustrated, pressed once when dodged, resolved in the builder's own words, and logged — without WHETSTONE ever writing the fix.
