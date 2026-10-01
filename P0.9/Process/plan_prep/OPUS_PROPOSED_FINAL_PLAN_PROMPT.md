/plan

Produce the decision-complete final perfection plan for the existing Jobbsøk_26 P0.9 implementation. Planning only — change nothing on disk.

## Read

1. `/AGENTS.md` (authority order, boundaries, optimization hierarchy — assume it, do not restate it).
2. `P0.9/Architecture/P0.9_FINAL_NORMATIVE_SPECIFICATION.md` and `P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md`.
3. `P0.9/Finalization_Review/P0.9_Final_Multi_Model_Review_Reconciliation.md` — the reconciled six-model review. Other documents call it `00_FINAL_RECONCILIATION.md`; that name does not exist on disk.
4. `P0.9/Build/` — code, tests, `evidence/`, `BUILDER_REPORT.md` — as deep as adjudication requires.

The reconciliation carries inline `<!-- OPUS_META_ADD OM-### -->` blocks from a later meta-review pass. The base text was deliberately preserved where the addition disagrees with it. Neither wins by position: adjudicate both against the code.

Open `P0.9/Architecture/P0.9_FINAL_DECISION_AND_ADOPTION_RECORD.md` only where intent decides a call, and `Finalization_Review/sources/*` only where a finding is contested, evidence-poor, or you need the original reproduction. Do not bulk-read `Architecture/Process/`, `P0.7/`, or the sources.

## Adjudicate

The reviews are evidence, not instructions, and their severity and remedies are not binding. Reproduced behaviour outranks any reviewer's assertion, including the meta-review's. The frozen architecture is a strong prior; the objective is the best achievable framework under `/AGENTS.md`'s hierarchy, not maximal literal compliance.

Give every material finding one disposition — **FIX / IMPROVE / KEEP / AMEND / DEFER** — and one line of evidence you personally verified.

Before accepting any finding rated Critical or High, try to falsify it against the current build. Report which ones survived, which collapsed, and — explicitly — which you accepted on inherited evidence without independent verification. A finding you did not test is not a finding you confirmed.

Two failure modes to test each remedy against:

- **If this finding is wrong, what does my remedy cost?** A repair that adds machinery, restores P0.7 behaviour, or improves formal compliance while reducing package quality, robustness or KISS is a regression even when the finding is real.
- **If this trust boundary stays broken, what reaches the employer?** Do not excuse a real boundary failure because the current happy path works.

Prefer the smallest change that makes the defect unrepresentable. Where a remedy needs a new module, abstraction or config surface, name the smaller alternative you rejected and why.

## Consolidate

Repair shared root causes, not reviewer IDs. The reconciliation proposes nine (`RC-1`…`RC-9`); confirm, merge or split them on your own reading. Several register rows are one defect seen from two angles, and at least one register remedy is larger than the defect requires. One shared correction beats five local patches — but invent no abstraction that has only one caller.

## Scope

Bounded to what makes the two-real-job semantic smoke trustworthy. New work enters the baseline only if it is a material P0/P1 correctness, integrity, containment or regression defect, is operator-blocking or smoke-contaminating, or is a direct consequence of an accepted change. Everything else is recorded `DEFER`. Semantic-quality questions with no implementation evidence belong to the pilot, not to this pass.

Do not edit the frozen Architecture files or the reconciliation during planning. `AMEND` items are *planned* here and applied during execution.

## Verify

Use scratch copies outside the canonical `Build/` for anything destructive; leave `Build/` byte-identical when planning ends. Green tests are evidence, not proof: the suite passes today while several invariants it claims to cover are unenforced in production. Distinguish helper-level coverage from public-command behaviour before trusting either.

Your verification plan must prove, through public commands, that:

- a frozen run's behaviour and output cannot be changed by editing any maintained root input;
- an artifact is current at acceptance, and no command consumes a stale, invalid or ineligible one;
- render state and delivered bytes correspond to the current semantic final, and its provenance record states what was actually consumed;
- one job's failure — including an unmodelled exception — cannot halt, corrupt or hide another job;
- branching leaves the parent untouched and yields a child that is usable without regeneration when its governing inputs are unchanged;
- the manual stage handoff can complete: `context` gives the operator everything a submission needs, and a wrong submission is refused before it displaces good work;
- every anti-regression guard in the reconciliation's `AR` register is still intact;
- regenerated gate, slice and builder evidence is re-derivable from the repaired build and claims no more than it proves.

## Return

1. Verdict, and the pre-smoke blocker set **ordered by expected value, not by finding ID**.
2. Disposition ledger grouped by root cause — including one line per rejected or downgraded finding.
3. `KEEP` register: the protected behaviour stated precisely enough that a later coding pass cannot "fix" it by accident.
4. Ordered implementation phases. Per accepted item: governing invariant and confirmed root cause, the chosen remedy, the code surface it touches, interactions with other items, regression risk, targeted verification.
5. Architecture amendments, if any, with affected IDs and the exact wording change.
6. `DEFER` list.
7. Final verification and evidence-regeneration sequence.
8. Anything genuinely requiring the user's policy or factual input.

Resolve ordinary implementation choices yourself from evidence and the optimization hierarchy. Escalate only a user-owned policy or factual choice, or a demonstrated conflict between two hard constraints.

Finally, append a `GOAL CONTRACT` of at most 3,500 characters for direct use with `/goal`. State the observable end state as verifiable properties — not a file list and not "implement the plan" — plus non-negotiable constraints, acceptance criteria, the anti-regression requirement, the scope boundary and legitimate stop conditions. Point at repository paths for detail rather than restating the plan.
