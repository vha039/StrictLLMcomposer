# Jobbsøk_26 P0.9 — Opus Final Roadmap-Package Finalization Prompt
## Repository map updated after project reorganization

You are the **final package architect and adversarial remedy adjudicator** for Jobbsøk_26 P0.9 immediately before a GPT-5.6 Sol implementation Goal.

You have full access to the current project folder and the draft roadmap/handoff materials already placed inside it.

Everything in the roadmap package is a **draft**, including:
- wording;
- strictness levels;
- document boundaries;
- file names;
- number of files;
- package hierarchy;
- proposed execution mechanisms;
- proposed Definition of Done structure;
- proposed execution-ledger design;
- proposed Goal shape.

You are explicitly authorized to rewrite, move, merge, split, add, remove or rename roadmap files when you are reasonably confident the change is a net positive for implementation quality, coherence, adaptability, context efficiency, recoverability or cost.

Do **not** preserve our structure merely because substantial effort has already been invested in it.

The objective is to give the implementing GPT-5.6 Sol agent enough durable structure to finish the P0.9 mechanical baseline correctly, while leaving enough implementation breathing room to exploit direct code evidence and its own engineering judgment.

Do not implement the P0.9 repairs in this pass.

---

# 0. IMPORTANT: current repository layout — do not spend reasoning effort rediscovering it

The P0.9 directory was deliberately reorganized after some of the draft roadmap material was written.

Treat the following layout as the current intended organization.

```text
P0.9/
├── Architecture/
├── Build/
└── Process/
    ├── Architecture_stage/
    │   ├── Draft_critiques/
    │   ├── Final_Arcitechture_draft/
    │   ├── jobbsøk_26_P0.9_context_base/
    │   └── jobbsøk_26_P0.9_context_refined/
    ├── plan_prep/
    │   └── sources/
    └── goal_prep/
        ├── Implementation_Roadmap/
        └── Opus_Handoff/
            └── [includes the original Codex final-perfection plan]
```

## 0.1 `P0.9/Architecture/` is now deliberately clean

`P0.9/Architecture/` contains **only the four frozen final architecture authorities**:

1. `P0.9_FINAL_NORMATIVE_SPECIFICATION.md`
2. `P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md`
3. `P0.9_FINAL_DECISION_AND_ADOPTION_RECORD.md`
4. `P0.9_FINAL_CRITIQUE_ADJUDICATION_AND_CLOSURE_MATRIX.md`

These four files are the P0.9 architecture authority plane.

There is **no longer an Architecture/Process subtree**.

Do not search for historical refinement material under `P0.9/Architecture/`. It was intentionally moved.

## 0.2 `P0.9/Process/` contains process/refinement/provenance material

The directory names are intentionally **preparation-stage labels**, not claims that the contained material is itself authoritative:

- `plan_prep/` = evidence and source material used to prepare/adjudicate the implementation plan;
- `goal_prep/` = the active preparation area for the final Goal-control package and its Opus handoff.

Do not infer authority merely from either directory name.

`P0.9/Process/Architecture_stage/`
contains architecture-development history, drafts, critique material and context packages.

It is **not normative**.

Open it only when a concrete unresolved architecture-rationale/provenance question cannot be resolved from the four final Architecture files plus current finalization evidence.

`P0.9/Process/plan_prep/`
contains planning-preparation evidence and source material retained for provenance, including the integrated/consolidated critique, the Sol adversarial review of the Codex plan, and other planning/review evidence as applicable.

`P0.9/Process/goal_prep/Implementation_Roadmap/`
contains the **draft roadmap/control package that you are being asked to perfect**.

`P0.9/Process/goal_prep/Opus_Handoff/`
contains your commissioning context and prompt **and the original Codex final-perfection plan**.

The original Codex plan is intentionally colocated with the Opus handoff because it is the immediate implementation-plan proposal you are being asked to adjudicate and refine. Treat it as important plan provenance and remedy evidence, not as controlling authority.

## 0.3 `P0.9/Build/` is the active implementation

This is the implementation you must inspect when remedy choices depend on current behavior.

Do not waste context recursively inventorying `.venv/`, `.pytest_cache/`, `__pycache__/` or installed third-party package trees.

Default implementation-inspection focus should be the actual project surfaces, for example:
- runtime source;
- runtime tests;
- runtime tools;
- schemas;
- policy;
- templates;
- run/frozen/output structures;
- evidence/gates/vertical-slice material;
- README/builder report or equivalent project-owned documentation;
- current retained synthetic runs when needed for reproduction.

Inspect environment/cache internals only if a concrete issue requires them.

## 0.4 Known stale references inside the drafts

Some roadmap drafts were generated **before this reorganization** and may still refer to old locations such as:

`P0.9/Finalization_Review/...`

Those path references are known stale draft artifacts.

Do not spend time reconstructing why they differ.

Correct them to the current project layout when finalizing the package.

In particular, after the user's planned directory rename the active roadmap location is:

`P0.9/Process/goal_prep/Implementation_Roadmap/`

and the Opus commissioning material **plus the original Codex plan** live under:

`P0.9/Process/goal_prep/Opus_Handoff/`

## 0.5 Root `AGENTS.md`

Read the repository-root `AGENTS.md` first if present; it remains the ambient repository instruction layer.

Any `AGENTS.md` or AGENTS candidate found inside the roadmap draft package is a **draft candidate**, not automatically ambient authority merely because it is named `AGENTS.md`.

Do not overwrite the repository-root `AGENTS.md` silently during this package-finalization pass.

If you conclude that the root file should change for the implementation Goal, produce the final replacement/candidate clearly and report that decision.

---

# 1. Core assignment

Design and produce the **best possible repository-local implementation-control package** for the final P0.9 mechanical-perfection run.

Your task is not to maximize documentation completeness.

Your task is to create the smallest coherent control system that:
- preserves the true product/architecture constraints;
- gives Sol clear direction;
- prevents silent scope invention;
- permits beneficial local engineering adaptation;
- survives compaction/interruption;
- makes completion objectively provable;
- does not suffocate the implementing agent with repeated or equally weighted instructions.

The final package itself is the main product of this pass.

---

# 2. Recommended reading order

Use this order unless current evidence gives a concrete reason to deviate:

1. repository-root `AGENTS.md`;
2. this commissioning prompt and the companion context in `P0.9/Process/goal_prep/Opus_Handoff/`;
3. all four files in `P0.9/Architecture/`;
4. all draft roadmap files in `P0.9/Process/goal_prep/Implementation_Roadmap/`;
5. the original Codex final-perfection plan under `P0.9/Process/goal_prep/Opus_Handoff/`;
6. the integrated/consolidated critique under `P0.9/Process/plan_prep/sources/`;
7. the Sol adversarial review of the Codex plan under `P0.9/Process/plan_prep/sources/`;
8. actual `P0.9/Build/` code/tests/evidence where needed to adjudicate remedies;
9. other `plan_prep/sources/` only when they materially inform a disputed decision;
10. `P0.9/Process/Architecture_stage/` only on demand for unresolved historical rationale/provenance.

Do not bulk-read all historical process material merely because it exists.

Treat:
- the four `Architecture/` files as the frozen normative architecture baseline;
- current explicit user commissioning instructions as authority over this finalization task;
- current direct Build evidence as authority about actual implementation behavior;
- reconciliation/reviews/plans as evidence and proposals, not commands;
- roadmap files as drafts.

Challenge your own prior recommendations as aggressively as recommendations from other models.

---

# 3. Perform independent current research

Before freezing the final package, conduct your own current-web research into the best practices and failure modes relevant to a long-running GPT-5.6 Sol/Codex implementation task.

Use both:
- official OpenAI/current product/documentation sources;
- experienced community/power-user reports, workflows, failures and practical patterns.

Do not merely repeat our prior queries.

Research whatever current information you judge highest-value, but ensure you resolve at least these classes of uncertainty:

1. Goal-mode persistence, completion auditing, file-referenced goals and legitimate stop/block conditions;
2. current `AGENTS.md` scoping, precedence and practical instruction-budget behavior;
3. long-context/compaction failure modes and reliable task-state recovery;
4. progressive disclosure versus giant always-loaded instruction sets;
5. durable repository-local execution state / ledger / plan patterns;
6. how instruction specificity affects GPT-5.6 Sol quality, autonomy and overengineering;
7. community evidence on Sol scope expansion, speculative abstractions, repeated test loops or refactor churn and how experienced users constrain it;
8. whether multi-file roadmap/control packages improve recovery or instead create synchronization/conflict risk;
9. current `/review`, plan/goal interaction and continuation behavior;
10. context/token-cost consequences of repeatedly rereading large files, logs, diffs or review corpora;
11. reasoning-effort tradeoffs for a highly prepared but tightly coupled coding task, especially Extra High versus Max;
12. any current evidence about how best to encode hard constraints versus soft guidance for frontier coding agents.

A prior research pass suggested the following hypotheses. **Verify or falsify them rather than assuming them:**

- leaner prompting can outperform more prescriptive prompting on GPT-5.6;
- decision-complete planning need not be implementation-prescriptive;
- progressive disclosure is preferable to giant always-loaded instruction files;
- root `AGENTS.md` should behave like a compact map/control layer rather than a task manual;
- repeated accumulated context/tool output can dominate long-run usage and degrade focus;
- compaction recovery is safer when reconstructed from repository state plus compact durable task state rather than conversational memory;
- very high reasoning can increase exploration/overengineering/cost, so Extra High may be a better long implementation default than Max;
- Goal stop conditions should live inside the Goal/control contract;
- property-based DoD is safer than class/helper-existence acceptance;
- targeted verification during edits plus full-suite/checkpoint verification is preferable to rerunning everything after every change.

If current evidence contradicts these, change the package accordingly.

---

# 4. Strictness/authority architecture is a mandatory deliverable

The implementing Sol agent must not experience every sentence in the package as equally binding.

You MUST independently determine and clearly encode the optimal strictness model.

The draft package currently aims for something like:

## Hard limits / non-negotiable outcomes
Very few.

Examples:
- truth, identity and human irreversible authority;
- no automated external submission/model orchestration;
- approved architecture constraints;
- Desired Final State properties;
- Definition-of-Done proof threshold;
- explicitly approved architecture amendments.

## Strong control rules
Rules that normally govern execution and should be broken only through explicit, justified escalation.

Examples:
- scope-admission rules;
- no silent architecture deviation;
- repository evidence outranks stale ledger state;
- public-path evidence is required for public-path claims.

## Strong priors / preferred implementation route
Examples:
- root-cause grouping;
- phase order;
- proposed resolver/handoff/receipt structure;
- candidate branch-hash approach.

These should strongly steer Sol without becoming brittle scripture.

## Soft guidance / heuristics
Examples:
- prefer existing machinery;
- prefer mechanically boring solutions;
- minimize speculative abstraction;
- use targeted tests during development.

## Alterable options / inspiration
Mechanism candidates Sol may replace when direct implementation evidence shows a better route.

## Evidence / provenance
Review findings, reproductions and rationale. Evidence informs decisions; it does not become authority simply by existing.

You may replace this taxonomy.

Your final package must make the intended adherence level unmistakable.

The objective is:

> **few hard walls + strong directional control + generous local implementation freedom + zero silent product-scope invention**

Too rigid is a failure.
Too vague is a failure.

Explicitly reason over where the optimum lies for GPT-5.6 Sol.

---

# 5. Resolve package-level information architecture

The supplied draft currently separates:

- root `AGENTS.md` — durable repository/global boundaries;
- roadmap router/read-first file — package map, precedence and resume protocol;
- Desired Final State — WHAT must be true;
- Guidance — HOW TO DECIDE;
- Execution Plan — preferred HOW;
- Definition of Done — HOW TO PROVE;
- Execution Ledger — WHERE execution actually is.

This is a proposal, not a constraint.

Alter the file count, names, ownership boundaries or package topology if you are reasonably confident the result is better.

For every substantive rule, decide its **single normative owner**.

Run a cross-document audit for:
- duplicated normative statements;
- conflicting authority levels;
- lower-level files redefining higher-level requirements;
- DoD testing plan compliance instead of observable properties;
- plan mechanisms accidentally elevated to Desired Final State;
- mutable ledger changing requirements;
- evidence/reviews accidentally becoming instructions;
- temporary finalization rules leaking into future semantic-pilot work;
- stale paths caused by the repository reorganization;
- repeated instructions that waste context without adding control.

Prefer references over duplicated prose.

---

# 6. Adjudicate the remaining remedy disputes

Do not inherit the Codex plan, Sol plan review or your own prior meta-review mechanically.

At minimum independently resolve the following.

## 6.1 Architecture revision strategy

The Codex plan proposed an active `0.9.1`.

Determine:
- whether a normative revision is actually required;
- how exact frozen `0.9.0` authority is preserved if semantics change;
- whether older synthetic frozen runs are supported, refused or migrated;
- which version/revision fields genuinely change;
- how to prevent accidental interpretation of old runs under new semantics.

Do not globally replace unrelated version fields.

## 6.2 Deterministic binding invariant vs handoff-token mechanism

The underlying requirement is deterministic binding ownership/current-at-birth.

Determine whether:
- a token/digest is the smallest safe mechanism;
- another deterministic envelope/current-context check is simpler;
- architecture should specify only the semantic invariant.

Do not freeze a mechanism into architecture merely because it is useful in the plan.

## 6.3 Review/render orthogonality

Determine precisely whether review/triage is:
- an authorization precondition to render;
- part of render receipt identity;
- neither;
- or both.

Avoid accidental render invalidation from a pure triage/review replacement unless the architecture deliberately intends that behavior.

## 6.4 Failure scope

Do not assume broad `except Exception` + continue is correct.

Distinguish:
- artifact-local;
- job-local;
- run-global;
- environment-global.

Ensure the final package tells Sol to preserve trustworthy state rather than maximize continuation at all costs.

## 6.5 Retry semantics

Verify/falsify whether current architecture distinguishes:
- one bounded same-session mechanical correction for malformed/structurally invalid model output;
- semantic/manual retry/restart after genuine production failure.

Do not collapse them if the distinction is real.

## 6.6 Safe writes versus source maintenance

Run-production/export write boundaries must be safe.

But deliberate maintained-source tooling, including template preparation, may legitimately modify maintained source assets between runs.

Do not write a “safe write” rule that makes legitimate maintenance impossible.

## 6.7 Word process cleanup

Truthful diagnostics are mandatory.

Only auto-kill when exact automation-process ownership is actually established.

Do not promote simple before/after PID differencing into proof merely because it is convenient.

## 6.8 OOXML anti-regression

Protect demonstrated properties:
- target-Word compatibility;
- byte-safe untouched package parts where required;
- no accidental normalization/serialization regression.

Do not permanently ban a library by name unless the property cannot safely be preserved otherwise.

## 6.9 Branch semantic hash

Re-review the proposal to exclude mechanically run-specific identity fields from semantic artifact hashing.

Inspect every consumer.

Adopt only if:
- semantic reuse becomes cleaner;
- wrong run/job identity is still independently rejected;
- no legitimate consumer relies on run identity being part of semantic content identity.

Otherwise choose the smallest safe alternative.

## 6.10 Goal boundary

Determine whether the implementation Goal should stop at:

`GO_FOR_TWO_JOB_SMOKE`

rather than executing two real semantic jobs.

Preserve the engineering-evidence versus product/pilot-evidence separation unless current evidence strongly supports merging them.

---

# 7. Optimize specifically for the implementing GPT-5.6 Sol agent

Expected implementation configuration is currently:

- GPT-5.6 Sol;
- likely Extra High reasoning;
- Goal mode;
- full repository access;
- one principal agent owns convergence.

Reassess this from current research.

Do not over-explain local engineering decisions that Sol can safely infer from code.

Be highly explicit about:
- destination;
- hard boundaries;
- scope admission;
- accepted architecture amendments;
- dangerous regressions;
- proof threshold;
- recovery/resume semantics;
- legal stop conditions.

Leave breathing room around:
- local decomposition;
- helper/function/class names;
- equivalent algorithms;
- test-fixture implementation;
- localized refactors;
- alternative mechanisms that satisfy the same hard property with less machinery.

Prevent feature invention through a strong **scope-admission rule**, not by prescribing every implementation step.

---

# 8. Final package quality gates

Before returning, adversarially test the package against all of the following.

## Single-owner
Does each kind of normative truth have one owner?

## Strictness clarity
Can Sol tell which statements are:
- hard;
- strong control rules;
- preferred route;
- soft guidance;
- options;
- evidence only?

## Decision completeness
Are implementation-critical policy choices resolved, while local engineering choices remain intentionally free?

## Freedom
Can Sol replace a suboptimal mechanism without appearing to violate the entire package?

## Scope
Can Sol invent an unrequested feature and plausibly claim the package authorized it?
If yes, tighten scope admission.

## DoD integrity
Does DoD prove observable properties rather than existence of proposed implementation constructs?

## Recovery
Could a fresh Sol after compaction recover correctly from repository state without chat memory?

## Context efficiency
Does the package avoid unnecessary rereads of large reviews, logs, source trees or historical process material?

## Lifecycle
Will temporary finalization instructions stop governing once the next phase begins?

## Finite completion
Is there a real defensible stopping point?

## Anti-regression
Are beneficial current behaviors protected as properties rather than brittle historical mechanisms?

## Path correctness
Do all final package references reflect the **current** `P0.9/Architecture`, `P0.9/Build`, and `P0.9/Process/{Architecture_stage,plan_prep,goal_prep}` layout?

---

# 9. Final outputs

You may change this set if your analysis shows a better package.

The final repository-local control package should provide the functional equivalents of:

- durable repository routing/global boundaries;
- package router/resume protocol;
- Desired Final State;
- reasoning/scope/strictness guidance;
- final preferred execution roadmap;
- property-based Definition of Done;
- compact durable execution state.

The finalized roadmap/control package should normally live under:

`P0.9/Process/goal_prep/Implementation_Roadmap/`

unless you identify and justify a materially better location.

Also produce:

## `FINAL_GOAL_COMMAND.md`

A very short copy-paste-ready `/goal` command for the implementing Sol session.

It should:
- point to the repository-local roadmap package rather than restating it;
- encode legitimate stop/block conditions;
- not turn the execution plan into immutable scripture;
- be optimized for a long-running Goal.

## `PACKAGE_FINALIZATION_NOTES.md`

Keep this compact.

Record only:
- material package-structure changes;
- material strictness/authority changes;
- material remedy changes from Codex plan / Sol plan review / your own prior recommendations;
- research findings that actually changed the design;
- stale-path corrections resulting from the repository reorganization;
- genuine user-owned unresolved choices, if any.

Do not produce another giant review essay.

## Root `AGENTS.md`

If you conclude the root `AGENTS.md` should change for the implementation Goal:
- produce a clearly identified final root replacement/candidate;
- do not silently overwrite the active root file during this finalization pass unless current explicit user instruction already authorizes it.

---

# 10. Preserve canonical implementation and architecture state during this pass

Before finishing, verify:

- `P0.9/Build/` canonical implementation/data was not modified by this package-finalization pass;
- the four frozen files in `P0.9/Architecture/` were not modified;
- `P0.9/Process/Architecture_stage/` historical material was not rewritten;
- only roadmap/control/finalization artifacts under the goal-stage process area, plus any explicitly produced root-AGENTS candidate, changed.

If you believe an Architecture amendment is already user-approved and must be physically applied before Codex begins, **do not silently apply it here**.

Specify the exact proposed amendment and implementation-phase action in the final roadmap/notes so the subsequent implementation Goal can apply it deliberately.

---

# 11. Final response to the user

Return:

1. overall package-finalization verdict;
2. final strictness/authority model;
3. most important package changes and why;
4. web-research findings that materially changed the design;
5. recommendation for Sol reasoning effort;
6. exact final file list and locations;
7. final `/goal` command verbatim;
8. any single genuine decision the user still needs to make before launching Codex.

Then stop.

Do not implement P0.9 repairs in this pass.
