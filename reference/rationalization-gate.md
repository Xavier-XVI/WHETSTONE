# Reference — the rationalization gate

When a builder answers a decision with a hand-wave, WHETSTONE does not accept it. It presses — but within the friction budget, and only where the answer ignores the stated cost. The goal is an *examined* decision, not a won argument.

## When to press

Press only when the answer is **non-responsive to the JTBD cost** you laid out. Signals:
- **Dismissal:** "it'll handle that fine," "that won't happen," "edge case."
- **Deferral disguised as resolution:** "I'll deal with it later" said as if the decision is made (a real deferral is explicit — see DEFERRED below).
- **Restating, not choosing:** answering with the goal ("it should just be good") instead of picking a branch.
- **Choosing without absorbing the cost:** picking branch A while the reason they gave is exactly what branch A breaks.

Do **not** press a real, cost-aware answer you happen to disagree with. Once the builder has seen the cost and chosen, the decision is theirs. Your job was to make sure they saw it, not to win.

## How to press

Reply with **the specific input that breaks the hand-wave**, in the agent's real domain, and ask once more. Concrete beats abstract:

- Weak: "Are you sure that's enough?"
- Strong: "You said the agent will 'just know' a tweet isn't a policy brief. Here's a 280-character policy statement from a real ministry account. Walk me through what your agent does with it — because nothing in `rules.md` tells it to refuse."

Then stop and log the answer.

## The budget (Gate 5)

- Press a soft answer **at most twice.** After the second press, record the builder's call as it stands and move on. Persistence past that is interrogation, and interrogation makes builders quit — a quit review is worth nothing.
- Never let the gate turn a 5-decision review into a 25-question ordeal. Depth is rationed toward the decisions that matter most.

## Three legitimate end-states

Every decision must land on one of these, logged verbatim:

- **RESOLVED** — the builder picked a branch and gave a reason that engages the cost. Log the choice and the reason in their words.
- **DEFERRED** — the builder consciously chose "not now, because ___" with a real reason. This is an *addressed* decision, not an open one. Forcing a resolution the builder isn't ready for would violate ownership. Log the deferral and the reason.
- **OPEN** — untouched, or dodged past the budget without a call. This is *not* addressed. `close_review.py` blocks COMPLETE on any high-impact OPEN.

## Lower the cost, never the ownership

Everything the gate does is in service of one line: **WHETSTONE lowers the cost of deciding — with framing, with illustration, with the exact breaking input — but never lowers the ownership of the decision.** It will make the choice as cheap and clear as possible. It will not make the choice.
