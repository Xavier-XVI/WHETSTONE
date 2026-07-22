# WHETSTONE

**A critique editor for single-specialist ICM agents. It sharpens the builder; it never writes the fix.**

You hand WHETSTONE one AI-specialist folder. It makes you state the job that agent is supposed to do, then reads your folder as a prosecutor of that job — showing you the places it will quietly fail, and the decisions you never actually made. It sorts what it finds into cheap **defects** (just fix them) and real **decisions** (forks only your knowledge can settle), illustrates each decision so you can resolve it in under a minute, and hands it back. It keeps a verbatim, dated log of the whole run so the work is auditable.

It will not rewrite your agent. It will not make your decisions. That's the point — an editor that hands you a "fixed" version taught you nothing.

---

## Intellectual lineage — augmentation, not acceleration

WHETSTONE asks Yves Morieux's question — *how well do you actually do your work?* — of an AI agent. Morieux (Boston Consulting Group; author of *Six Simple Rules* and the *Smart Simplicity* framework) holds that when work is done well AI augments the people doing it, and when it's done poorly AI replaces them — and that no one knows what "well" means better than the people doing the work. His book's subtitle, *How to Manage Complexity without Getting Complicated*, is WHETSTONE's own discipline: keep the real complexity of judgment, cut the complicatedness. It's why WHETSTONE surfaces hard forks but caps them at five — and why it never makes your decisions for you.

It is deliberately not a *10x* tool. Making work ten times faster is substitution — the tool absorbs the work while your judgment stays flat. WHETSTONE optimizes the opposite: it adds friction where friction builds judgment, refuses to hand you a fixed file, and measures success by whether you caught a decision you'd have shipped blind. A whetstone doesn't cut anything. It sharpens your edge, and the edge stays yours.

## What it reviews

One **single-specialist ICM folder** — ICM ("interpretable context methodology," see [`reference/icm-standard.md`](reference/icm-standard.md)) treats the folder as the agent's whole mind: drop it into a Claude project and Claude *becomes* the specialist. The five-file kind: `identity.md`, `rules.md`, `examples.md`, `reference/`, `README.md`. Not multi-folder agencies, not non-ICM agents.

## Quickstart (2 minutes)

**In Claude Code (this repo has `CLAUDE.md`):** open a session with this folder as the working directory. `CLAUDE.md` is the boot directive — it's read automatically and turns Claude into WHETSTONE before it does anything else. Skip straight to step 4.

**In a plain Claude Project (or any Claude chat with file access):**

1. Open a Claude Project.
2. Add **WHETSTONE's** files (`identity.md`, `rules.md`, `examples.md`, `reference/`) to the project so Claude *becomes* WHETSTONE.
3. Paste the kickoff:

   > You are WHETSTONE.

4. WHETSTONE opens the review itself — a short introduction, then it asks for the target (folder path or repo URL) and the job to be done, pressing you to be specific. The target answer always gets logged as `target:` — but `verify.py` and file-reading only ever work against a **local folder**. If you gave a URL, WHETSTONE needs a local copy before it can run `verify.py`: in Claude Code it clones the repo itself; in a plain Claude Project (no shell) you add the target's files to the project directly. Either way this happens before step 5, not after.
5. WHETSTONE pressure-tests your JTBD answer, runs `verify.py` against that local copy, then returns a ranked ledger: defects to fix, and decisions for you to resolve.
6. Work through the decisions. WHETSTONE logs your answers verbatim and marks each RESOLVED, DEFERRED, or OPEN.

## The 30-second try-it

Don't have an agent handy? Point it at itself — WHETSTONE is a single-specialist ICM folder too:

```
python3 verify.py .
```

You'll get the deterministic report (structure, placeholders, unenforced imperatives, reference wiring, README usability, token weight). That's the mechanical floor; the judgment happens in the conversation.

## What you get back

- **A defects list** — located, obvious fixes. Do them or hand them to a model; no judgment needed.
- **A decision ledger** — the 3–5 forks that most threaten the job, each with: the input that exposes it, both branches sketched in your agent's real domain, what each costs the job, and the outside knowledge the choice turns on. Each ends in a blank — `I choose ___ because ___` — that only you can fill.
- **A review log** in `reviews/` — verbatim conversation, before/after `verify.py`, and a per-decision status. This is your audit trail and your proof of work.

## The two scripts (the deterministic floor)

- `verify.py <target-folder>` — mechanical checks on the agent under review. Facts only, never quality. `--json` for machine-readable output.
- `close_review.py <review-log.md>` — the closure gate. A review is **COMPLETE** only when no high-impact decision is left OPEN. WHETSTONE cannot declare a review done on its own — only this script can.

## How the audit trail works

Every review writes to `reviews/<agent>-<date>.md` (schema in `reference/review-log.md`), and adds a row to `reviews/INDEX.md`. Over time the index becomes the memory of how each agent was sharpened — every run readable verbatim, every decision traceable from raised to resolved. If your runtime has no file-write, WHETSTONE keeps the same structure in-chat and you save it at the end.

## Current state of the memory (`reviews/`)

Three agents have gone through WHETSTONE so far — full detail in [`reviews/INDEX.md`](reviews/INDEX.md), one row per run:

| Agent | Where it lives | Stage |
|-------|----------------|-------|
| **WHETSTONE** (self) | [github.com/Xavier-XVI/WHETSTONE](https://github.com/Xavier-XVI/WHETSTONE) | **COMPLETE, and rebuilt.** 1 decision, DEFERRED. The one defect the review found (JTBD-first was unenforced) was fixed in this same folder — see [`reviews/WHETSTONE-2026-07-21.md`](reviews/WHETSTONE-2026-07-21.md). |
| **SentinelRx** | [github.com/Xavier-XVI/SentinelRx](https://github.com/Xavier-XVI/SentinelRx) | **Ledger COMPLETE, folder not yet rebuilt.** 4 decisions raised — 3 RESOLVED, 1 DEFERRED (unenforced audit logging, carried as an open risk). See [`reviews/SentinelRx-2026-07-21.md`](reviews/SentinelRx-2026-07-21.md). |
| **THE_WILDCARD** | [github.com/Xavier-XVI/THE_WILDCARD](https://github.com/Xavier-XVI/THE_WILDCARD) | **IN_PROGRESS.** 3 decisions raised, all still OPEN — 2 high-impact (form-fill output vs. delta discovery; lead-funnel-deep vs. whole-practice-broad) block closure. See [`reviews/THE_WILDCARD-2026-07-21.md`](reviews/THE_WILDCARD-2026-07-21.md). |

**Note:** a WHETSTONE review closes a *ledger*, not a folder — resolving a decision records the builder's call, it doesn't edit the target's files (Gate 2). Besides WHETSTONE itself, none of these agents have actually been rebuilt against their resolved ledgers yet: SentinelRx's decisions are answered but the follow-on edits (softening "traceable," the stale-profile fail-safe, the accumulated-load read, etc.) haven't been applied back to its repo, and THE_WILDCARD hasn't even finished the decision pass. That last mile — carrying a CLOSED or RESOLVED ledger back into an actual rebuild — was skipped for both, given the complexity and time each would take.

## The rules WHETSTONE holds itself to

- **Located or it doesn't count** — every finding has a `file:line` and a quote.
- **Anchored or it doesn't count** — every finding names how it hurts the job.
- **Critique, never rewrite** — it dramatizes what a choice *does*; it never authors your fix.
- **Never resolves your decisions** — it makes them cheap to decide, never decides them.
- **Presses a dodge at most twice** — challenge, not interrogation.
- **Verbatim logs, code-checked closure** — the trail is your words, and a script stamps "done," not the model.

## Folder map

```
WHETSTONE/
├── CLAUDE.md        # boot directive — auto-loads WHETSTONE in Claude Code, routes to identity.md/rules.md
├── identity.md      # who WHETSTONE is, its job, the six lenses
├── rules.md         # the operating protocol and the six gates
├── examples.md      # what good critique looks like (worked cases)
├── reference/
│   ├── icm-standard.md        # what a healthy ICM folder looks like
│   ├── lenses.md              # the six divergence lenses + the defect/decision test
│   ├── ledger-format.md       # the decision ledger + illustration format + triage
│   ├── rationalization-gate.md# how to press a hand-wave, within budget
│   └── review-log.md          # the audit-log schema
├── verify.py         # deterministic checks on a target folder
├── close_review.py   # the closure gate (no high-impact decision left open)
├── reviews/          # per-agent audit logs + INDEX.md (the memory)
└── README.md         # this file
```

## What WHETSTONE is not

Not a rewriter. Not a grader that hands you a score. Not a prompt you could replace with "review my folder and cite lines" — its value is the JTBD wedge, the defect/decision split, the illustrated forks, and the pressure it puts on your hand-waves. If you could get the same result by pasting its output into Claude and saying "now fix it," it would have failed. It's built so you can't.
