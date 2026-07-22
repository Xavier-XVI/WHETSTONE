# WHETSTONE review log
- agent: SentinelRx
- target: https://github.com/Xavier-XVI/SentinelRx
- date: 2026-07-21
- reviewer: WHETSTONE
- status: COMPLETE (close_review.py, 2026-07-21)

<!-- close_review.py stamps final status. Each DECISION keeps IMPACT + STATUS markers. -->

## 1. JTBD (anchor)
- builder stated (verbatim): confirmed via Decision #1 — "SentinelRx is decision-support ... because the agent cannot bare responsibility, a human must be in the loop and get accountable/responsible."
- JTBD (agreed): surface OTC-safety risk for a specific elderly patient and route the final call to an accountable human — decision-*support*, not an autonomous operator.
- extracted from identity.md L4: "answer one question: is this product safe for this specific patient to take right now?" — an *operator* that "applies encoded rules to a specific patient profile and returns a trustworthy, traceable decision."
- anchor-check note: the folder gives two different answers to "what authority does SentinelRx have?" — identity/README frame it as a decision-maker ("returns a decision"; "No medical knowledge needed. No guessing."), while the disclaimer frames it as illustrative only ("Do not use this to make real medication decisions"). That unresolved tension is Decision #1. Anchor to be confirmed by the builder before close.

## 2. verify.py — before
```
structural blockers: 0 | total notes: 8
All 8 notes are INFO: unenforced-imperative candidates in rules.md
(§1 "One decision per interaction. Always."; §3 acetaminophen "Always sum...";
 §8 combination overload "Always escalate"; §10 "the agent MUST automatically append..." x2; etc.)
No missing/empty core files. reference/ present and wired.
```

## 3. Defects (resolvable from the folder — fix or delegate)
- D1: rules.md §2 step 2 cross-references ingredients only against "the patient's current **prescription** list," but the profile carries a separate "OTC Products Currently in Regular Use" section AND §3's acetaminophen rule requires summing "across all products the patient takes." Current OTC use is never entered into the decision process. Add current-OTC-in-use to the cross-reference step.
- D2: (clinical — verify; reviewer is not a clinician, confidence <80%) Example 1 tells a warfarin patient "the pain component (acetaminophen 500mg) is safe on its own. Use regular Tylenol." Acetaminophen–warfarin is a recognized interaction (chronic/high-dose acetaminophen can raise INR). risk-reference.md lists acetaminophen only vs "any hepatotoxic Rx," not vs warfarin. Either the interaction is out of scope by design (state it) or the reference is incomplete (add it). Confirm against your source.
- D3: identity.md says "one active patient profile at a time — loaded from patients/," but nothing specifies how the *active* profile is selected if more than one exists in patients/. Minor, but a wrong-patient load is a silent high-severity failure. Name the selection mechanism.

## 4. Decisions (ranked; builder to resolve)

### DECISION #1 — Job clarity / authority — identity.md L4 + README + Disclaimer
- IMPACT: high
- STATUS: RESOLVED
- collides when: "a caregiver the README says needs 'No medical knowledge' photographs Claritin, receives '✅ SAFE TO TAKE', and gives it — acting on the decision exactly as the README invites and exactly as the Disclaimer forbids ('Do not use this to make real medication decisions')."
- branch A: "SentinelRx is an operator that *decides* (its stated identity)." → in practice: it returns a bare ✅/🚫 and the caregiver acts on it with no human in the loop. → costs: it substitutes for caregiver/pharmacist judgment; a wrong ✅ has no catch; it makes the medical call it disclaims.
- branch B: "SentinelRx is decision-*support* that surfaces the risk and always routes the final call to a human." → in practice: it shows the interaction and says 'confirm with your pharmacist before giving,' never a bare green light. → costs: slower; loses the 'no guessing, just tell me' simplicity the README sells; some caregivers want the answer handed over.
- what only you know: "whether you intend an operator that decides or a safety net that informs — and how much authority your real caregivers should be handed in a safety-critical domain."
- builder answer (verbatim): "SentinelRx is decision-support ... because the agent cannot bare responsibility, a human must be in the loop and get accountable/responsible."
- resolution note: Decision-support confirmed. Follow-on edits (builder's to make): identity.md must stop calling itself an operator that "returns a decision"; README must drop "No medical knowledge needed. No guessing."; §9 output must never present a bare ✅/🚫 as an instruction to act — every result routes the final call to a human/pharmacist.

### DECISION #2 — Stale-profile fail-safe — rules.md §7 + examples.md Example 5
- IMPACT: high
- STATUS: RESOLVED
- collides when: "profile is 22 days stale after a discharge that added a new anticoagulant but wasn't recorded; caregiver photographs a supplement that interacts with the NEW drug. Example 5 states plainly: 'the operator would miss it entirely. The staleness warning is the only defense' — for a user the README says 'wants to be told what to do.'"
- branch A: "Decide + warn (current behavior): return the full ✅/🚫 plus an appended staleness line." → in practice: '✅ SAFE TO TAKE … ⚠️ profile 22 days old' — the confident decision leads, the caveat is a line the caregiver may skim past. → costs: a missed new-drug interaction ships as a green light behind a warning few will act on.
- branch B: "Fail-safe: profile beyond STALENESS_THRESHOLD forces 📞 CALL PHARMACIST — no ✅/🚫 issued." → in practice: 'This profile is 22 days old; I can't safely decide — verify current meds or call your pharmacist.' → costs: more escalations and friction, including false alarms when nothing actually changed.
- what only you know: "how reliably your caregivers update after a hospitalization, and whether a skimmed warning is real protection or theater in your setting."
- builder answer (verbatim): "Branch B ... because one mistake can be fatal."
- resolution note: Fail-safe adopted. A profile beyond STALENESS_THRESHOLD_DAYS forces 📞 CALL PHARMACIST — no ✅/🚫 issued on a stale profile. Follow-on edits: §7 and §9 to encode the hard escalation; Example 5 to be rewritten to show escalation, not decide-and-warn.

### DECISION #3 — Stateless scan vs. accumulated load — rules.md §2 + §3 (acetaminophen) + §10
- IMPACT: high
- STATUS: RESOLVED
- collides when: "Monday the caregiver gets ✅ on melatonin; Wednesday ✅ on a 'PM' product. Each is defensible alone, but §2 only reads the profile + current product — it never reads current OTC use or the prior scan log — so the agent cannot see it already cleared a sedative and can't flag additive sedation / anticholinergic load across scans."
- branch A: "Each scan is independent (current behavior)." → in practice: the acetaminophen 'sum across all products' rule and the written-but-never-read audit log are decorative — the agent has no memory of what it already approved. → costs: misses cumulative dose/burden, the exact failure mode §8 warns about; undercuts the 'traceable' identity.
- branch B: "The agent reads current-OTC-use + prior scan log before deciding." → in practice: on Wednesday it says 'you were cleared melatonin Monday — adding diphenhydramine now stacks sedation.' → costs: statefulness, more complexity, and a new failure surface (a stale or wrong log now corrupts a decision).
- what only you know: "whether your real caregivers add OTCs incrementally over days (making accumulation the true risk) or use it one-off, and how much you trust the log as an input rather than just a record."
- builder answer (verbatim): "branch B because a system without memory/context cannot work properly."
- resolution note: Stateful adopted. The agent must read current-OTC-in-use + the prior scan log before deciding; §2 step 2 to include OTC-in-use and accumulated load. CONSEQUENCE: this makes the scan log a decision INPUT, which raises Decision #4 from med to high — a memory you read from must be a memory you can trust.

### DECISION #4 — The "traceable" promise vs. unenforced logging — rules.md §10 + identity.md
- IMPACT: high
- STATUS: DEFERRED
- ESCALATION: raised med→high after Decision #3. The scan log is now a decision INPUT, not just a record. Best-effort/unenforced logging (§10) can therefore silently corrupt a future decision — the accumulated-load safety you just chose is only as good as the logging you haven't secured. Must be RESOLVED or DEFERRED before close.
- collides when: "in a plain Claude project the model finishes a scan and simply doesn't perform the §10 'the agent MUST automatically append...' file write — a prose instruction with nothing enforcing it. No error surfaces; the audit trail just silently has holes, while identity.md still promises a 'traceable decision.'"
- branch A: "Accept best-effort logging and soften the claim." → in practice: identity says 'logs when it can,' not 'traceable'; you stop depending on a guarantee the runtime can't give. → costs: weakens a headline feature and a real differentiator.
- branch B: "Make traceability real: a post-scan check / gate that fails loudly if the log wasn't written (or a deterministic wrapper that writes it)." → in practice: no decision is considered delivered until its log entry exists. → costs: engineering beyond pure ICM prose; may exceed the 'folder-only' constraint.
- what only you know: "how load-bearing traceability actually is to SentinelRx's purpose — a nice-to-have record, or a core promise a caregiver/clinician will rely on."
- builder answer (verbatim): "I defer on decision #4 as i dont have the architecture in mind that would solve such issue for the time being."
- resolution note: DEFERRED — consciously carried, not closed. Open risk of record: with Decision #3 making the scan log a decision input, best-effort logging can silently corrupt an accumulated-load decision. Revisit when an enforcement mechanism is in hand. Until then, the "traceable" claim in identity.md should be softened to reflect best-effort logging.

## 5. verify.py — after
```
<pending — re-run after fixes>
```

## 6. Close
- close_review.py verdict: COMPLETE — every decision is RESOLVED or DEFERRED (run 2026-07-21).
- decisions: #1 RESOLVED, #2 RESOLVED, #3 RESOLVED, #4 DEFERRED (carried, high-impact risk of record).
- follow-on edits for the builder to implement (not applied by WHETSTONE): identity.md (drop "operator/returns a decision"; soften "traceable" to best-effort); README (drop "No medical knowledge needed. No guessing."); §9 (never emit a bare ✅/🚫 as an instruction; route to a human); §7+§9 (hard stale-escalation to CALL PHARMACIST); §2 (add current-OTC-in-use + accumulated load); Example 5 (show escalation, not decide-and-warn); D1–D3 defects.
- after-snapshot (§5): pending the builder's edits; re-run verify.py once applied.
