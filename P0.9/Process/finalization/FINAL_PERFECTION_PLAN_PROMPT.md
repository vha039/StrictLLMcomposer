/Plan

Reasoning: use the highest available planning/reasoning effort. This turn is ANALYSIS AND PLANNING ONLY. Do not implement code, do not modify the production Build, do not rewrite pilot artifacts, and do not change frozen architecture in this turn. You may create only the requested planning documents in a planning directory outside the active Build/source tree.

## Objective

Produce the definitive, implementation-ready plan for the final pilot-learned optimization pass over Jobbsok_26.

This is not a general redesign exercise. The system has already completed its first two real vacancies successfully. The purpose of this pass is to use the real pilot evidence to remove the remaining material employer-facing quality defects, improve candidate-specific professional voice, and resolve any other suboptimalities that the pilot actually exposes, while preserving the framework's truth, provenance, stage-ownership, recoverability, and MVP-KISS principles.

Minor increases in complexity are allowed where the expected quality/throughput gain is significant and well evidenced. The target surface must be wide enough to fully mitigate the observed problem or realize the intended gain, but no wider.

## Authority and evidence order

Use this order:

1. This current prompt and explicit user requirements below.
2. The frozen/core-truth architecture currently present in the repository.
3. The actual current repository and exact current runtime behavior as implementation truth.
4. The actual two-vacancy pilot inputs, every stage artifact, render receipts, and final employer-facing outputs.
5. `NON_AUTHORITATIVE_CONSIDERATIONS.md` as deliberation material only.
6. Historical plans, reports, and completion narratives as claims/evidence only.

`NON_AUTHORITATIVE_CONSIDERATIONS.md` is intentionally NON-AUTHORITATIVE. Read it fully, use it to broaden your search and understand prior reasoning, but independently validate every repo-specific statement and freely reject its recommendations.

Do not assume an issue exists because the considerations file names it. Reproduce/verify it from the actual pilot/repository first.

Do not assume an architecture amendment is forbidden. If a change genuinely requires one, specify the smallest explicit normative diff. Conversely, do not amend architecture merely because a new concept has been named.

## Mandatory behavioral outcomes whose implementation YOU must decide

Independently determine the best implementation of each outcome. The mechanism, file placement, stage ownership, degree of enforcement, and test surface are yours to adjudicate.

### A. Readability over fit-to-page

- Main employer-facing body text should default to 12 pt.
- Compress/edit content before shrinking normal prose to meet a page target.
- Smaller text is reserved for deliberately subordinate information.
- Avoid half-point micro-tuning merely to force fit.
- Preserve readability, machine parsing, template integrity, and sensible page balance.

### B. Earned motivation only

- Motivation should primarily arise from the actual work, responsibilities, problem, environment, learning, leverage, autonomy, capability expansion, or useful improvement.
- Employer mission/societal importance should be invoked only when it is genuinely consequential and credibly motivating for this candidate.
- When in doubt, omit mission enthusiasm rather than manufacture it.
- Employer specificity must not be confused with ceremonial employer praise.

### C. Maximum truthful leverage

- Candidate factual authorities are canonical ground truth.
- Nothing may exceed what they support.
- Once a proposition clears the truth bar, however, state/frame it with the maximum defensible persuasive force: strongest accurate verb, attribution, specificity, outcome, emphasis, placement, and employer-relevant framing supported by evidence.
- Do not add uncertainty, passive distancing, or hedges that are absent from the evidence.
- Known truth should sound known.
- Preserve genuine uncertainty/qualification when it exists in the evidence.
- Treat material truth attenuation/understatement as a quality defect just as unsupported inflation is.

### D. Plain human punctuation

- En dash `–` and em dash `—` are strongly prohibited in employer-facing text.
- Ordinary hyphen `-` remains allowed where normal human writing calls for it, including compounds, dates, ranges, etc.
- Do not use a hyphen merely to divide clauses when ordinary sentence punctuation can do the job.
- Prefer `.`, `,`, `:`, parentheses, `?`, `!`, and quotation marks where natural.
- Semicolon is allowed but uncommon.
- `|` may remain a structural divider in headings/titles.
- The behavioral rule is strong; do not automatically assume it needs a new Python validator.

### E. Candidate-specific professional-voice / "write this professionally as me" function

The current personality mechanism is primarily a vacancy-specific positioning/interpretive mechanism. Preserve that concept as a strong prior; do not repurpose it casually.

The new objective is orthogonal:

> Given the strongest truth-safe employer argument, make the final writing plausibly authored by this particular candidate in a professional context, rather than generic over-perfected LLM application prose.

This is NOT a generic humanizer. It should derive candidate-specific rhetorical tendencies from the actual personality profile and, where useful, real candidate writing evidence.

You must decide:

- whether this belongs primarily in Stage 1, Stage 2, Stage 3, or more than one stage;
- whether it should be a distinct frozen context source, a subsection/translation of personality, an addition to writing doctrine/stage instructions, or another minimal mechanism;
- how it interacts with the existing 0-3 personality facet system;
- how much of the full personality profile downstream writers should see;
- how to prevent voice from gaining factual/claim/strategy authority;
- how to keep the effect moderate and professional rather than caricatured;
- how CV and letter should receive different voice intensity/register;
- how employer-specific register changes while author identity remains stable;
- how to prevent generic Stage-2 prose from anchoring Stage 3 if Stage 3 is the primary owner.

A dedicated Stage 3 professional-voice context is a prior proposal, NOT a requirement. Decide independently.

Hard anti-goals unless you can prove they are uniquely justified:

- no new semantic Stage 4 merely for voice;
- no numeric "sounds like Vegard" score;
- no generic deterministic humanizer;
- no personality cosplay;
- no new factual claims created from personality;
- no dynamic per-vacancy personality facts;
- no architecture/state expansion merely to represent style.

## Required work sequence

Follow the sequence below. You may iterate inside a step, but do not skip stages of reasoning.

### STEP 0 - Reconstruct the actual current system and pilot

Before designing anything:

1. Read the repository-root instructions.
2. Read the frozen/core architecture completely enough to identify all affected invariants and stage responsibilities.
3. Read current RUNBOOK, Stage 1/2/3 instructions, writing doctrine, persuasion calibration, settings, templates, schemas, personality context, evidence authorities, status/render/finalization logic, and relevant tests.
4. Reconstruct the actual two-vacancy pilot from disk.

Known pilot identifiers to verify, not trust blindly:

```text
run:     r20260828-213932-7f13b4
cluster: pilot_live_smoke
jobs:
  huseierne_strategi_maalstyring
  avinor_digital_transformasjon
```

For each vacancy inspect the entire artifact lineage:

```text
vacancy source
-> normalized/source-inspection input
-> Stage 1 context/handoff -> strategy.json
-> Stage 2 context/handoff -> draft_package.json
-> Stage 3 context/handoff -> final_package.json + review.json
-> finalization
-> render_report/receipts
-> actual DOCX/PDF employer-facing package
```

Visually inspect the actual rendered pages where possible. Do not evaluate typography/layout from parsed text alone.

### STEP 1 - Decide the optimal implementation of each mandatory outcome individually

For A-E above, independently determine:

- the actual current failure/gap;
- the correct behavioral target;
- the best implementation surface;
- exact owner/stage;
- what should remain unchanged;
- top alternatives;
- why the chosen approach dominates;
- implementation complexity;
- tests/verification needed;
- expected employer-facing gain;
- risks and anti-regression boundaries.

Do not optimize the combined system yet. Establish the individually best solution first.

### STEP 2 - Multivariate combined-design analysis

Now reason across all proposed solutions together.

Analyze direct and indirect interactions, covariance, conflicts, redundancy, and emergent effects, especially:

- typography x page targets x content compression x page balance;
- readability x ATS/machine parsing/template contract;
- maximum truthful leverage x claim ceiling/evidence authority;
- maximum truthful leverage x objection handling;
- earned motivation x personality motivation profile;
- earned motivation x employer-specificity/Arbeidsgiverbyttetesten;
- voice x writing doctrine;
- voice x existing personality positioning;
- voice x Stage-2 anchoring;
- voice x Stage-3 reconstructive authority;
- voice x directness/social temperature/employer register;
- punctuation x template static text and generated text;
- voice x cross-job structural formulaicity;
- any proposed context addition x frozen-run provenance/currentness;
- all changes x stage separation and artifact ownership;
- all changes x cluster throughput/human handling;
- all changes x final package quality, which dominates optimization.

Consolidate overlapping mechanisms. If one accepted change sufficiently mitigates another issue, do not implement a second redundant fix.

### STEP 3 - Produce the first integrated implementation design

After Step 2, define an initial coherent implementation plan for A-E.

It must already be exact enough to implement: files, functions/sections/styles, data flow, stage contracts, tests, ordering, and invariants.

This is not yet final because the pilot forensic audit may reveal additional problems/root causes.

### STEP 4 - Adversarial forensic audit of BOTH real pilot vacancies

Now temporarily put the proposed fixes aside and audit the actual two-vacancy test with maximum scrutiny.

Critically analyze:

- the input vacancy and candidate evidence;
- Stage 1 route, requirements analysis, objections, evidence selection, selected personality facets, claim ceilings, and strategy quality;
- Stage 2 CV and letter composition, tailoring, evidence order, complementarity, native Bokmal, motivation, generic filler, and any loss/attenuation of Stage-1 insight;
- Stage 3 changes relative to Stage 2, including what it reconstructed, what it retained, what it failed to repair, triage calibration, personality/voice expression, truth calibration, employer specificity, and final argument shape;
- final CV and letter content;
- final typography, spacing, page balance, section hierarchy, page count, machine readability, static template content, punctuation, and rendered visual quality;
- render/output/operator friction, including the original output-directory ACL/access issue if still reproducible;
- cross-job leakage or unjustified structural/template reuse;
- any mismatch between design intent and actual output.

Identify **every atomic element** that is materially or detectably short of the intended optimum. Do not restrict yourself to the issues listed in `NON_AUTHORITATIVE_CONSIDERATIONS.md`.

At the same time, do not manufacture defects: distinguish personal preference, acceptable alternative, local one-off, actual quality defect, architecture defect, model stochasticity, template issue, evidence issue, and environment issue.

### STEP 5 - Deep root-cause analysis for every identified issue

For every atomic issue:

1. Locate the first artifact/stage where it appears.
2. Determine whether it originates in input evidence, strategy, drafting, finalization, template/rendering, or environment.
3. Identify any upstream policy/instruction/context that caused or encouraged it.
4. Identify later stages that had the information/authority to repair it but failed to.
5. Determine whether the cause is singular or multivariate.
6. Separate direct cause, contributing cause, enabling condition, and downstream repair failure.
7. Define the exact boundary of the suboptimal behavior.
8. Explicitly identify adjacent behavior that is NOT defective and must not be refactored.
9. Estimate recurrence likelihood/systemicity and employer-facing impact.
10. Define the smallest root-cause-level fix surface capable of resolving it.

Do not jump from symptom directly to rewrite.

### STEP 6 - Re-run Steps 1-3 for all newly identified issues

For each newly discovered issue:

- identify its individually optimal fix;
- analyze interactions with A-E and with fixes for other pilot issues;
- determine whether the existing Step-3 plan already mitigates it sufficiently;
- add a new fix only where residual material suboptimality remains;
- remove/merge earlier fixes if the root-cause analysis shows a better common solution.

### STEP 7 - Define the absolute final integrated change target

Now perform another full Step-3-quality combined analysis over:

- mandatory outcomes A-E;
- every validated pilot issue;
- every root cause;
- every proposed mitigation;
- every interaction discovered.

Land a SINGLE coherent final target state.

MVP-KISS remains the governing implementation discipline, but slightly relaxed versus the prior patch:

- minor complexity increases are acceptable where expected benefit is significant;
- the change surface must be extensive enough to fully mitigate the observed issue or realize the intended high-value trade-off;
- it must be **only that wide and no wider**;
- avoid speculative extensibility, generalized subsystems, duplicate state, redundant rubrics, or architectural ceremony.

No unresolved design forks should remain in the final plan. Pick the best design and explain why.

### STEP 8 - Top-to-bottom framework impact sweep

With the final proposed change set in hand, sweep the entire framework for consequences of any combination of changes.

Review at minimum:

- intake/freeze;
- frozen-input manifest/provenance;
- schemas/artifact ownership;
- Stage 1 context/strategy/personality;
- Stage 2 drafting;
- Stage 3 reconstruction/review;
- writing/persuasion doctrine;
- candidate factual authorities;
- templates/style map;
- finalization/date semantics;
- rendering/page warnings/PDF receipts;
- status/next/continuation;
- recovery/failure handling;
- cross-job reset/isolation;
- pilot instrumentation;
- operator workflow and handling minutes;
- security/containment;
- test/traceability system;
- architecture documents and revision semantics.

This is an **impact-driven sweep**, not permission to reopen settled subsystems gratuitously. Only add mitigations where a proposed change actually creates or exposes a material issue.

For every mitigation discovered, integrate it into the final plan and then update the impact analysis accordingly.

### STEP 9 - Final viability and optimal-state review

Perform one last adversarial review of your own final plan.

Ask:

- Does it actually solve the validated pilot weaknesses?
- Does it maximize employer-facing quality rather than merely satisfy policy language?
- Does any change weaken truth/evidence boundaries?
- Does any change reduce pipeline coherence or stage separation?
- Is any new complexity unnecessary?
- Is any proposed simplification too narrow to realize the intended gain?
- Is the voice system likely to produce authentic professional authorship rather than cosplay?
- Will 12 pt typography remain viable without destructive content loss?
- Can every change be verified on the two existing pilot jobs?
- Is representative-cluster throughput still viable?
- What could a hostile reviewer still object to?
- What remains genuinely empirical and should be deferred to the representative cluster rather than engineered now?

Then freeze the plan. Do not continue ideating after this review unless you uncover a load-bearing contradiction.

## Issue-registry requirements

Every atomic issue in the final registry should include at least:

- ID and title;
- affected job/artifact/page/stage;
- exact observed evidence;
- expected behavior;
- actual behavior;
- employer-facing consequence;
- first stage introduced;
- stages that could have repaired it;
- root cause(s);
- contributing factors;
- root-cause confidence;
- severity;
- recurrence likelihood;
- systemic/local classification;
- exact scope boundary;
- explicit non-target surfaces;
- proposed fix;
- why this is the correct fix surface;
- top alternatives and why they lose;
- interaction with every other relevant fix;
- architecture impact;
- implementation cost/risk;
- verification method;
- final acceptance criterion.

## Architecture-specification requirements

The final architecture document must explicitly diff the proposed target against the established core-truth architecture.

For each material change classify it as:

- implementation-only correction;
- policy/writing-doctrine refinement;
- template/configuration change;
- context/frozen-input addition;
- stage-responsibility clarification;
- actual normative architecture amendment.

For any architecture amendment, provide:

- exact current architectural principle/wording affected;
- why existing architecture cannot truthfully accommodate the desired behavior;
- smallest proposed normative change;
- downstream effects;
- migration/frozen-run implications;
- tests/acceptance consequences.

If no architecture amendment is necessary for a change, say so explicitly and explain why.

## Implementation-plan requirements

The implementation instructions must be sufficiently exact that a separate implementation agent has no meaningful design decisions left.

Include:

- exact files to modify;
- exact functions/classes/sections/styles/schemas touched;
- exact behavior before and after;
- exact order of implementation;
- dependencies among changes;
- TDD red/green sequence where appropriate;
- focused test names and assertions;
- full-suite/adversarial tests;
- public CLI/end-to-end smoke steps;
- template/render verification;
- re-run/re-render procedure for both pilot vacancies;
- comparison against original pilot outputs;
- representative-cluster gate;
- expected outputs;
- rollback/stop conditions;
- final changed-file/scope gate;
- explicit `must not change` surfaces.

Where a proposed change turns out already correctly implemented, remove it rather than manufacturing work.

## Required output files

Write the planning package to a NEW planning directory outside the active `P0.9/Build` source tree, using the repository's existing Process/planning convention if one exists. Do not modify Build during this `/Plan` turn.

Return these files:

### `00_OVERVIEW.md`

Broad-strokes holistic plan:

- executive verdict;
- target state;
- principal weaknesses found;
- major chosen changes and why;
- expected employer-facing gains;
- architecture impact summary;
- implementation scope summary;
- detailed index/information map for every other file;
- final stopping rule.

### `01_CHANGE_ARCHITECTURE_SPECIFICATION.md`

Full architecture specification for the final proposed changes, including an explicit diff against the established core-truth architecture and exact treatment of frozen-run/backward-compatibility semantics.

### `02_IMPLEMENTATION_DESCRIPTIONS_INSTRUCTIONS_AND_DEFINITIONS.md`

The definitive, explicit, granular implementation plan and behavioral definitions. This must contain step-by-step implementation detail, exact files/functions/sections/styles, TDD order, verification, and acceptance.

### `03_ISSUE_REGISTRY_MITIGATION_AND_FIX_LOGIC.md`

One complete atomic registry entry for every validated issue and fix, including all required causal, scope, alternative, interaction, and verification reasoning.

### `04_PILOT_FORENSIC_AUDIT.md`

A full stage-by-stage forensic reconstruction of BOTH real pilot vacancies, from vacancy/evidence through Stage 1, Stage 2, Stage 3 and rendered outputs. Include cross-job comparison and exact lineage of every material final defect.

### `05_DECISION_LOG_AND_ALTERNATIVES.md`

Record the major implementation decisions, top alternatives, rejected approaches, trade-offs, and why the final choice dominates. Include especially the professional-voice architecture and the implementation decision for each mandatory rule A-E.

### `06_CHANGE_IMPACT_AND_TRACEABILITY_MATRIX.md`

Map every proposed change against every affected framework surface, architecture clause/invariant, pilot issue, test, and acceptance proof. Explicitly show unchanged/non-target surfaces.

### `07_VERIFICATION_ACCEPTANCE_AND_STOPPING_PLAN.md`

Define exact mechanical tests, semantic/pilot regression checks, render/visual inspection, A/B comparison where useful, representative-cluster validation, success/failure criteria, and the point at which further framework iteration must stop.

You may add another `.md` file only if it materially improves implementability or auditability and is not redundant with the above. If you add one, explain its unique purpose in `00_OVERVIEW.md`.

## Final response in chat

After writing the files, return only:

1. the final planning verdict in 5-10 bullets;
2. the exact list/paths of created planning files;
3. the most consequential architecture/implementation decision;
4. the top 3 pilot defects by employer-facing impact;
5. any remaining open uncertainty that genuinely cannot be resolved without implementation or another real cluster.

Do not implement. Do not modify the production Build. Do not continue feature ideation after the final viability review.
