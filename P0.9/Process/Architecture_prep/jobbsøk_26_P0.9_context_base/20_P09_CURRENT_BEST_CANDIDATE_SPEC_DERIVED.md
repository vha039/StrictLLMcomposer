---
document: "Jobbsok_26 - Final, seamlessly integrated, fully consolidated and deeply reasoned P0.9 specification, architecture, design and preferences magnum opus"
framework: "Jobbsok_26"
specification_version: "P0.9.0-derived-final"
artifact_role: "integrated architecture lock + implementation specification + decision/provenance record"
status: "DERIVED_FINAL_CANDIDATE_FOR_ADOPTION"
generated: "2026-08-22"
historical_state_before_this_synthesis: "P0.8.0 was last adopted normative architecture; P0.8.1 was non-normative hardening; P0.9 had not yet been formally architecture-locked"
primary_scope: "P0.8.1 and P0.9 corpus, integrated against the previously established executable P0.7 baseline only where needed to preserve empirical constraints"
primary_user: "Vegard"
language_runtime_v1: "nb-NO"
---

# Jobbsok_26 P0.9 - Final integrated specification, architecture, design and preferences magnum opus

> **Executive status.** This document is the first deliberately *converged* P0.9 architecture produced from the P0.8.1 hardening layer and the full P0.9 option/research/decision corpus. It is not a claim that an earlier chat had already adopted this exact architecture. Before this synthesis, the historical record ended with P0.8.0 as the last formally normative but unimplemented architecture, P0.8.1 as a strong non-normative hardening layer, and P0.9 as a mature but deliberately unselected decision basis. This artifact performs the missing convergence step.
>
> **Core design thesis.** P0.9 should be a fresh, local, file-authoritative, manually initiated three-stage system that keeps P0.8's Selective Quality topology, deletes product branches that P0.9 evidence shows do not belong in the core, adopts only the P0.8.1 hardening whose contract surfaces still exist, moves evidence navigation into a deterministic generated index, makes strategy a structured but explicitly non-authoritative hypothesis, gives final Sol elastic reconstruction authority within immutable truth ceilings, and keeps uncertain quality enhancers such as personality and Luna context prep as bounded, attributable toggles outside the core baseline.

---

# 0. How to read this document

## 0.1 Why a second-order synthesis was necessary

The P0.8.1 and P0.9 corpus cannot be merged correctly by chronological overwrite alone.

P0.8.1 is primarily a **contract-hardening layer**. It assumes most of P0.8's product surface remains in place and therefore spends substantial effort specifying those interfaces safely.

P0.9 is primarily an **option-space, simplification and quality-allocation layer**. It asks whether some of those product surfaces should exist at all, introduces later user constraints, and explores new quality mechanisms whose value is uncertain.

The non-linear consequence is crucial:

> **Delete obsolete contract surfaces first; harden only the contract surfaces that survive.**

Examples:

- If portal answers are detached from the core package, P0.8.1's elaborate core portal state/limit contract should not be implemented and then bypassed; the core branch should be deleted.
- If differentiated Priority A/B treatment is removed, a model-generated `cluster_plan.json` may cease to carry unique state, so hardening it with a schema can become wasted work.
- If one run manifest becomes the frozen authority, P0.8.1's separate snapshot/progress objects should be re-evaluated for duplication rather than copied forward mechanically.

Conversely, several P0.8.1 mechanisms become *more* important under P0.9:

- mechanical vs semantic truth separation;
- exact expected-job reconciliation;
- full replacement semantics for CV employment overrides;
- final evidence-ref synchronization;
- repair-scope based READY/CHECK/RERUN;
- same-chat validator repair;
- partial success;
- one-job transactional persistence;
- bounded human effort measurement;
- actual rendering validation.

This document therefore performs a **surface-by-surface semantic merge**, not a document-level merge.

## 0.2 Provenance labels used throughout

Every load-bearing choice belongs to one of these classes:

| Label | Meaning |
|---|---|
| **USER-LOCKED** | Explicit current user decision or correction. Highest design authority below truth/safety constraints. |
| **P08-INHERITED** | P0.8 normative rule not later superseded. |
| **P081-HARDENED** | P0.8.1 contract repair selected because the underlying surface survives and the repair is directly useful. |
| **P09-EVIDENCE** | Supported by P0.9 analysis/research but not itself a historical user decision. |
| **SYNTHESIS-LOCK** | Architecture choice selected in this document after cross-analysis of competing P0.8.1/P0.9 options. It becomes historical project authority only when the user adopts this specification. |
| **EXPERIMENTAL** | Implemented only as a bounded toggle or test surface; not part of baseline semantics. |
| **ENV-VERIFY** | Architecture is fixed, but an environment-specific implementation parameter must be proven locally. |
| **DEFERRED** | Intentionally excluded from P0.9 core; re-open only on a named activation signal. |

## 0.3 Precedence model

Within this document, conflicts are resolved in the following order:

1. Truth, identity, usability and human-final-authority constraints.
2. Latest explicit user decision/correction.
3. This integrated P0.9 architecture lock.
4. P0.8.1 hardening selected here.
5. P0.8 normative rule not superseded.
6. Research/assistant recommendations.
7. Historical proposals.

The architecture must never silently convert an assistant proposal into a user decision. `SYNTHESIS-LOCK` is therefore explicitly distinguished from `USER-LOCKED` even when the design recommendation is strong.

## 0.4 Historical baseline versus target baseline

Two different baselines must not be confused:

- **Executable historical baseline:** P0.7.
- **Normative historical baseline:** P0.8.0.
- **Hardening baseline:** P0.8.1 review, never formally adopted.
- **Target baseline after this synthesis:** this P0.9.0-derived-final specification.

P0.7 remains valuable empirical evidence for scripts, Word masters, validation and file-based execution, but **P0.9 is a fresh runtime**. Legacy components are reused only after explicit fit review, not because backward compatibility is required.

---

# 1. Executive architecture lock

## 1.1 Product definition

**USER-LOCKED + SYNTHESIS-LOCK**

Jobbsok_26 P0.9 is a private, local, manually operated, reusable application-package system for **one candidate** over multiple future job-search batches.

Its core product is invariant:

> **one tailored CV + one tailored application letter per conforming vacancy, in native Norwegian Bokmal for P0.9 v1.**

Portal/form answers are **detached downstream artifacts**, generated only for vacancies that need them and only after the core package exists. Non-Norwegian, CV-only, portal-only, or structurally exceptional vacancies are **exception-path jobs**, not reasons to complicate the core.

The system does not:

- discover jobs as part of production runtime;
- contact employers;
- submit applications;
- mutate candidate factual authorities during a run;
- support multiple candidates;
- generalize rare channels into core abstractions;
- use API orchestration as the normal semantic workflow;
- silently retry model calls;
- hide model judgments behind a state machine.

## 1.2 Optimization objective

**USER-LOCKED**

Truth-safe tradeoff order:

1. **Final package quality / expected interview effect**
2. **Human effort per submitted package**
3. **Implementation speed and simplicity**
4. **Model cost**
5. **Reversibility / optionality**

Hard constraints:

- factual truth and identity;
- claim strength defensible from candidate authorities;
- employer usability;
- human control of irreversible actions.

The system is distribution-optimized, not uniformity-optimized. The operational target is approximately **30 strong packages from a ~40-job batch**, with weak cases selectively rerun, separately handled or dropped rather than rescued at the expense of the strong majority.

P0.8's quality distribution metric remains useful for pilot analysis:

```text
Q_happy = (median(q) + mean(top_80_percent(q))) / 2
```

but it is an **evaluation metric**, never a writing-time objective that models optimize numerically.

## 1.3 Core topology

**P08-INHERITED + USER-LOCKED**

Normal semantic route:

```text
Human-approved frozen batch
        |
        v
Deterministic ingest + evidence index + run freeze
        |
        v
Stage 1 - Sol Max - Decision Architecture
        |
        v
Stage 2 - Terra Max - Native Package Writer
        |
        v
Stage 3 - Sol Max - Elastic Final Writer + Selective Review
        |
        v
Deterministic finalization + Word/PDF rendering + run reconciliation
        |
        v
READY / CHECK / RERUN / FAILED
        |
        v
Human review + manual submission
```

Normal semantic stages are manually initiated as distinct model chats. Within each cluster-stage chat, jobs are processed sequentially without routine between-job human confirmations, and each job is persisted and validated before the next begins.

## 1.4 Core architecture choices selected in this synthesis

| Design cluster | P0.9 lock | Provenance |
|---|---|---|
| Product boundary | CV + application invariant; portal detached; nb-NO v1; exceptions separate | **SYNTHESIS-LOCK**, strongly supported by DC-1 1a + user permission |
| Authenticity/personality | Build bounded optional module; **default OFF until paired test establishes benefit** | **SYNTHESIS-LOCK + EXPERIMENTAL** |
| Context preparation | Deterministic evidence index is core; Luna prep is optional, default OFF | **SYNTHESIS-LOCK + EXPERIMENTAL** |
| Strategy artifact | Canonical `strategy.json` with prose-capable fields + generated human `strategy.md` view; explicit hypothesis status | **SYNTHESIS-LOCK** |
| Runtime/state | One frozen `run_manifest.json`; job-centric tree; derived job views; regenerable status | **SYNTHESIS-LOCK** |
| Priority/order | Human-fixed clusters/order in intake; no differentiated A/B treatment; no model-generated core `cluster_plan.json` | **SYNTHESIS-LOCK** |
| Validation | Stage validator before completion; max two same-chat repair attempts; third failure => job FAILED and continue | **P081-HARDENED / N-04** |
| Final authority | Stage 3 elasticity = ELASTIC | **USER-LOCKED** |
| RERUN | Sol Max, one job, separate manual chat, targeted source access; not a standard fourth stage | **P081-HARDENED** |
| Rendering | One job transaction; isolated converter environment; each expected PDF independently verified; batching only if target-machine test proves it safe | **SYNTHESIS-LOCK / ENV-VERIFY** |

## 1.5 Prompt/human envelope

**USER-LOCKED**

- Routine model prompt budget: approximately **20-25 prompts for a ~40-job batch**.
- No absolute ceiling if a larger budget has demonstrated quality value; required evidence rises sharply above the normal envelope.
- Human review + submission capacity: about **5-10 hours/week**.
- Desired human handling: about **10-20 minutes per submitted package**.
- First-batch urgency: **1-4 weeks**, with meaningful deadlines potentially under two weeks.

Prompt count is treated as a human-complexity variable, not merely a token-cost variable.

---

# 2. What P0.8.1 and P0.9 contribute when read together

## 2.1 P0.8.1's unique contribution: interface correctness

P0.8.1's strongest insight is that P0.8's topology was already good and the remaining engineering risk was concentrated at **interfaces between individually reasonable components**:

- intake -> identity;
- deliverable requirements -> state;
- batch plan -> freeze;
- cluster plan -> stage progress;
- semantic truth -> deterministic hard failure;
- package JSON -> template fields;
- strategy -> writer;
- final writer -> review action;
- artifacts -> batch completion;
- pilot data -> architecture conclusions.

P0.8.1 is therefore a catalog of **where ambiguity becomes expensive**.

Its most durable insight is not any single filename. It is the general rule:

> If a boundary controls correctness, state, measurement or human action, make its contract explicit enough that the builder cannot improvise a materially different interpretation.

## 2.2 P0.9's unique contribution: surface minimization and quality reallocation

P0.9 asks a different question:

> Before hardening every P0.8 surface, which surfaces are actually worth carrying into the next system?

This produces several large simplifications:

- invariant CV+application core;
- detached portal workflow;
- nb-NO first release;
- fixed dynamic CV surface;
- job-centric runtime;
- human clustering;
- removal of mandatory microvariation;
- possible deletion of A/B treatment;
- deterministic evidence indexing instead of model-generated indexing;
- optional, attributable personality and Luna layers rather than mandatory context machinery.

This is why P0.9 is not just P0.8.1 plus more features. It is a **reallocation of complexity budget**:

```text
less complexity in channel/state/branch machinery
                  ->
more room for evidence navigation, final-writer freedom,
authenticity experiments and observability where quality may actually improve
```

## 2.3 The integrated interpretation

The correct P0.9 relationship is:

```text
P0.8 core quality topology
+ P0.9 product simplification
+ P0.8.1 hardening on surviving interfaces
+ P0.9 current user policy
+ bounded P0.9 experimental quality modules
= P0.9 integrated target
```

Not:

```text
P0.8
+ every CR in P0.8.1
+ every idea in Brainstorm Brief
+ every research recommendation
```

The latter would recreate precisely the over-structured system the project has repeatedly rejected.

---

# 3. Non-linear cross-document insights

This section records the deductions that only become visible when P0.8.1 and P0.9 are considered together.

## 3.1 Contract deletion dominates contract hardening when the product branch disappears

P0.8.1 correctly hardens portal limits, deliverable state and cluster plans *given P0.8's product*. P0.9 demonstrates that some of these branches can be removed from core entirely.

Therefore:

> A contract should be hardened only after the product boundary that requires it has survived architecture selection.

This prevents a common failure mode in framework evolution: converting yesterday's accidental complexity into tomorrow's rigorously specified accidental complexity.

### Consequences

- Core `required_outputs` can be invariant rather than a general channel matrix.
- Portal limit validation moves to a detached portal module.
- Core review codes no longer need portal-specific cases.
- Core templates/finalizer no longer need portal branches.
- `cluster_plan.schema.json` is unnecessary if cluster/order are frozen human input and A/B treatment disappears.

## 3.2 Two orthogonal authority axes resolve strict-contract versus elastic-writer tension

The corpus repeatedly appears to pull in opposite directions:

- P0.8.1 demands explicit schemas, validation and provenance.
- P0.8/P0.9 demand an elastic final Sol that can reconstruct weak upstream strategy.

The tension disappears when authority is split into two axes:

### Axis A - factual authority

Fixed upstream:

```text
candidate factual authorities
+ original vacancy
> all model-authored artifacts
```

No model stage can raise a claim ceiling beyond source evidence.

### Axis B - strategic decision authority

Intentionally migrates downstream:

```text
Stage 1 strategy hypothesis
   -> Stage 2 realized draft
   -> Stage 3 final strategic decision
   -> human approval
```

Stage 3 may replace identity framing, evidence emphasis, argument architecture and prose. It may not replace reality.

### Result

Structured strategy and elastic final writing are compatible **if the strategy object is explicitly typed as a hypothesis, not a command**.

This becomes a central P0.9 contract.

## 3.3 Structured strategy's real risk is authority inflation, not JSON syntax

Earlier debate framed Markdown versus JSON as a parsing question. The cross-analysis shows the deeper risk:

> A schema-valid structured object may *feel* more authoritative to downstream models and reduce the final Sol's willingness to reconstruct it.

P0.9 therefore adopts structured strategy only with compensating freedom:

- `strategy_status = HYPOTHESIS_NOT_AUTHORITY`;
- `elasticity = ELASTIC`;
- a mandatory counterfactual reserve;
- Stage 3 vacancy-first read-order protocol;
- explicit permission to contradict the strategy;
- `material_strategy_change` observability in review;
- no schema constraint on subjective quality targets.

JSON then becomes an **information-shape tool**, not an epistemic elevation.

## 3.4 Deterministic evidence indexing is the bridge between P0.8.1 provenance and P0.9 context design

P0.8.1 requires meaningful `used_evidence_refs`, but stable source addressing is fragile if refs are ad hoc strings.

P0.9 context work notices that many proposed Luna tasks are deterministic over stable candidate files.

The merged solution is a generated **deterministic evidence index**:

- stable addresses;
- no relevance filtering;
- no model interpretation;
- no prompts;
- batch-reusable;
- invalidated only when source truth changes.

This creates a common coordinate system for:

- Stage 1 evidence selection;
- Stage 2 source escape;
- Stage 3 final evidence synchronization;
- pilot provenance;
- optional Luna prep;
- human auditing.

It is therefore more valuable than a retrieval convenience: it is the **shared reference plane** of the semantic pipeline.

## 3.5 Context reduction is safe only when recovery is structurally easier than blind trust

The combined corpus reveals a four-part safety pattern:

1. deterministic index keeps all sources addressable;
2. advisory context artifacts state explicitly that they are non-authoritative;
3. no summary-of-summary is allowed to become factual grounding;
4. every semantic stage can source-escape to original authorities.

This is the minimum architecture for safe context compression.

Without those four, a cheap/preparatory model can silently decide what a stronger later model never sees.

## 3.6 Job-centric runtime converts orchestration into transaction management

P0.8.1 describes multiple stage-centric state objects. P0.9's job-centric view reveals a simpler abstraction:

> One job is the unit of semantic transaction, rerun, context loading, backup, finalization and detached portal derivation.

This makes the runtime a provenance/transaction problem rather than an orchestration problem.

The system therefore does not need:

- a database;
- event sourcing;
- a scheduler;
- a dependency graph engine;
- hidden retries.

A frozen manifest + deterministic artifacts + regenerable status is enough.

## 3.7 Static invalidation classes can be more precise than P0.8.1 N-01 without becoming a state engine

P0.8.1/P0.9 N-01 has four broad classes. Cross-analysis shows that `WRITING_POLICY` is too coarse: a Stage-3-only policy change should not force Stage 1 rerun; a personality strategy change should.

P0.9 therefore uses a slightly finer **static invalidation lattice**:

| Class | Typical members | Stale scope |
|---|---|---|
| `SOURCE_TRUTH` | candidate authorities, vacancy content | strategy + draft + final + review + render for affected jobs |
| `STRATEGY_POLICY` | Stage 1 instruction, personality runtime policy when ON, strategy schema semantics | strategy + downstream |
| `WRITER_POLICY` | Stage 2 instruction, writing standard/calibration used by writer | draft + downstream |
| `FINAL_POLICY` | Stage 3 instruction/review policy | final + review + render |
| `RENDER_ASSET` | Word masters, renderer config, fonts/locale | rendered artifacts only |
| `SCHEMA_VALIDATION` | structural schemas whose semantics did not change | revalidate/adapt structure; no automatic semantic rerun |

This remains a **static table**. It reports staleness; it never automatically runs semantic stages.

## 3.8 Minimal authoritative core, rich disposable views

The project repeatedly risks equating fewer files with lower complexity. The P0.9 synthesis uses a different rule:

> Minimize authoritative objects; allow disposable generated views when they reduce human/model cognitive load.

Authoritative/frozen:

- original candidate authorities;
- original vacancy sources;
- frozen run manifest;
- current semantic outputs;
- approved template/policy versions.

Derived/disposable:

- evidence index;
- normalized vacancy text;
- job context view;
- generated `strategy.md` human view;
- run status/review queue;
- optional context-prep slice.

A derived file can always be regenerated from stronger authority. It therefore adds less conceptual state than an extra manually authored field in an authoritative object.

## 3.9 READY/CHECK/RERUN is a repair-cost prediction, not a quality score

P0.8.1's repair-scope rule is retained and sharpened.

Stage 3 does **not** have enough independence to be a judge of its own output. Its review status predicts the *kind of remaining human/system action*:

- READY: no material issue detected;
- CHECK: local bounded inspection/repair;
- RERUN: strategic backbone likely needs reconstruction;
- FAILED: mechanical/contract completion failed.

The status is useful only if calibrated against human outcomes. It must not be presented as a confidence probability or quality score.

## 3.10 Experimental features should be off-core, fail-open and attributable

Personality and Luna prep are the highest-variance surviving P0.9 ideas. Their architecture should not contaminate the core before they prove value.

Each experimental feature must satisfy:

1. one explicit setting controls it;
2. OFF produces the complete baseline system;
3. failure does not block the job;
4. output is non-authoritative;
5. no factual claim ceiling is expanded;
6. the effect can be measured against a control;
7. removing the feature requires no migration of core artifacts.

This allows high-agency experimentation without turning the experiment into permanent architecture.

## 3.11 Evaluation requires three distinct evidence loops

The corpus sometimes overloaded one 8-job pilot with too many purposes. P0.9 separates:

### Loop A - engineering proof

Can the deterministic pipeline ingest, validate, persist, merge and render correctly?

### Loop B - product baseline observation

Does the unchanged core Sol->Terra->Sol system produce useful packages at acceptable human cost?

### Loop C - causal feature tests

Does a specific uncertain mechanism such as personality or Luna prep improve quality enough to justify itself?

These loops should not be conflated. A system can be mechanically correct and semantically weak; a pilot can look good without identifying which feature caused it.

## 3.12 Security and context governance are the same control-plane problem

Two seemingly separate risks share the same structure:

- vacancy text may contain untrusted instructions;
- Luna/personality/context artifacts may contain useful but non-authoritative interpretations.

P0.9 applies one generalized rule:

> **Data-plane inputs may influence analysis but may not issue operating instructions, create factual authority, expand permissions or modify control policy.**

This yields a simpler security/context doctrine than separate ad hoc warnings.

---

# 4. Normative P0.9 product contract

## 4.1 Intended user and reuse horizon

**USER-LOCKED**

- One candidate: Vegard.
- Multiple future batches are expected; long-term personal reuse is plausible.
- The system is not designed for arbitrary candidate onboarding.
- Candidate factual authorities are maintained outside production and are frozen during a run.

This reuse horizon justifies modest stable abstractions such as a deterministic evidence index and a run manifest, but does **not** justify a generalized multi-user platform.

## 4.2 Core deliverables

**SYNTHESIS-LOCK**

Every conforming core job produces:

1. tailored CV content merged into the approved CV baseline/master;
2. tailored application letter;
3. DOCX for both;
4. PDF for both when required/desired by submission channel;
5. private machine artifacts (`strategy`, `draft_package`, `final_package`, `review`) used for audit and rerun.

Core semantic output requirements are invariant:

```text
CV + APPLICATION
```

No `channel` enum is required in the core semantic schema.

## 4.3 Detached portal product

**SYNTHESIS-LOCK**

Portal answers are not part of core Stage 1/2/3 completeness.

They are generated downstream only when an actual employer form requires them.

Advantages:

- eliminates core channel branching;
- exact form limits can be captured at time of use rather than predicted during batch architecture;
- portal answers can be grounded in an already approved coherent package;
- no portal failure can block core CV/application completion;
- rare portal-only cases can use an exception workflow rather than infecting the standard schema.

Detailed portal contract is defined in §18.

## 4.4 Language scope

**SYNTHESIS-LOCK based on USER permission**

P0.9 v1 is `nb-NO` only.

A non-Norwegian vacancy is flagged `EXCEPTION_LANGUAGE` at ingest and excluded from standard cluster production unless the operator explicitly elects a separate run/path.

This is a deliberate scope cut, not an assertion that future versions cannot support English.

## 4.5 Dynamic CV surface

**SYNTHESIS-LOCK based on USER permission + P08 inheritance**

Only these content zones are dynamically model-authored:

1. headline/title;
2. profile/summary;
3. competency selection/ordering/wording;
4. employment bullet overrides.

Stable chronology, role names, employer names, dates, education chronology and other factual scaffolding remain baseline-owned.

No dynamic education/support section is part of P0.9 v1.

## 4.6 Exception-path principle

**USER-LOCKED**

Rare jobs do not define the common architecture.

At ingest, a job may be marked:

- `CORE`;
- `EXCEPTION_LANGUAGE`;
- `EXCEPTION_CV_ONLY`;
- `EXCEPTION_PORTAL_ONLY`;
- `EXCEPTION_OTHER`.

Exception jobs are preserved in the inventory but do not block core batch execution. The human may handle them manually or invoke a deliberately separate extension.


---

# 5. Source truth, evidence and claim governance

## 5.1 Candidate factual authorities

**USER-LOCKED**

The canonical factual authority set is:

- `Work_experience.md`
- `Education.md`
- `Other_high_value_information.md`

All three were explicitly confirmed CURRENT in the latest P0.9 user answers.

During production they are immutable.

Not factual authorities:

- `Personality.md`;
- framework-adapted personality derivatives;
- strategies;
- drafts;
- previous applications;
- research reports about the candidate;
- assistant memory;
- generated evidence indices;
- final packages from other jobs.

Those may direct attention or provide interpretive context, but every new employer-facing factual implication must remain supportable by the factual authorities.

## 5.2 Vacancy authority

The employer's original vacancy artifact is the primary authority for:

- requirements;
- responsibilities;
- employer framing;
- language;
- application deadline;
- channel/form constraints actually visible in the source;
- role-specific terminology.

A normalized text extraction is a **derived convenience view**, never a replacement for the original artifact where layout, tables or omitted fields matter.

No model or deterministic normalizer may silently rewrite vacancy content into a new "canonical vacancy" that supersedes the original.

## 5.3 Evidence addressing

**P081-HARDENED + SYNTHESIS-LOCK**

Every material candidate evidence item used downstream should be addressable by a stable generated identifier.

The deterministic evidence index contains, at minimum:

```text
evidence_id
source_file
heading_path
section_hash
approx_size
lifecycle_label       # only when source explicitly supports it
claim_ceiling_marker  # only when source explicitly supports it
```

The index must not contain vacancy-conditioned relevance scores.

It may contain objective mechanical labels such as:

- duplicate;
- superseded source section;
- objectively invalid/unavailable.

It must never label evidence `IRRELEVANT` based on model or heuristic judgment.

## 5.4 Claim ceiling

A claim ceiling is the strongest employer-facing implication that the evidence can reasonably support.

Rules:

1. Evidence selection does not increase the claim ceiling.
2. Personality does not increase the claim ceiling.
3. Strategy does not increase the claim ceiling.
4. Repetition across sources does not automatically increase the claim ceiling.
5. Stage 3 may strengthen rhetoric only while remaining within the same evidence-supported ceiling.
6. Human approval may still reject a technically supportable claim as strategically or culturally unwise.

## 5.5 Final evidence synchronization

**P081-HARDENED**

The final package's `used_evidence_refs` must represent the evidence actually relied upon by the final employer-facing text.

It must not simply preserve Stage 1's intended evidence list after Stage 3 has changed the package.

Mechanical existence validation verifies only:

- reference format;
- source existence;
- stable ID resolvability.

It **does not prove** that the prose semantic claim is valid. Semantic truth remains a model/human responsibility.

## 5.6 Requirement coverage versus checklist prose

**P09-EVIDENCE + SYNTHESIS-LOCK**

Norwegian public-sector qualification principles and normal hiring logic make explicit vacancy requirements decision-relevant. The safe architecture is therefore:

- privately map every material stated requirement;
- classify candidate relation as `SUPPORTED`, `ADJACENT`, `GAP`, `NOT_MATERIAL`, or `UNKNOWN`;
- use that map in strategy and evidence selection;
- do **not** require the application letter to itemize requirements mechanically.

The package should persuade through a coherent employer decision argument, not read like a compliance checklist unless the vacancy itself demands that format.

---

# 6. Batch intake, freeze and identity

## 6.1 Human batch inventory

**SYNTHESIS-LOCK**

The highest-value operator artifact before production is a one-row-per-vacancy inventory.

Recommended human-editable file:

`batch_inventory.csv`

Minimum columns:

```text
job_id
employer
title
unit
reference
deadline
vacancy_path
sector
platform
cluster_id
sequence
user_priority
exception_class
notes
```

Notes:

- `sector` and `platform` are descriptive metadata, not routing authority unless a later feature explicitly uses them.
- `user_priority` is the human's application preference/scheduling input, not model A/B treatment.
- `cluster_id` and `sequence` are human-assigned in P0.9 v1.
- exact portal questions are **not** core batch state because portal is detached.
- language is fixed to nb-NO for core; exceptions are flagged through `exception_class`.

The system may accept JSON instead if implementation convenience clearly wins, but there must be **one operator-editable batch authority**, not several overlapping representations.

## 6.2 Ingest compilation

The ingest command:

1. reads the batch inventory;
2. validates unique `job_id`;
3. validates source paths and allowed file types;
4. copies or registers original vacancy artifacts into the controlled run root;
5. computes hashes;
6. derives normalized vacancy text where supported;
7. classifies core vs exception jobs based on explicit inventory and source facts;
8. validates cluster membership and sequence uniqueness;
9. generates the deterministic candidate evidence index if stale;
10. creates the frozen `run_manifest.json`;
11. creates derived `job_context.json` views;
12. refuses to freeze if identity or expected-set reconciliation fails.

## 6.3 Frozen run manifest

**SYNTHESIS-LOCK, replacing separate P0.8.1 snapshot state**

`run_manifest.json` is the single canonical freeze object.

It stores facts and fingerprints, not semantic conclusions.

Recommended high-level structure:

```json
{
  "run_id": "2026-08-22_batch01",
  "framework_version": "P0.9.0",
  "frozen_at": "...",
  "document_date": "...",
  "core_language": "nb-NO",
  "candidate_authorities": [...],
  "policy_assets": {...},
  "render_assets": {...},
  "schema_assets": {...},
  "settings": {...},
  "jobs": [...],
  "clusters": [...]
}
```

The manifest records hashes/versions for:

### Source truth

- three candidate authorities;
- each original vacancy source;
- stable CV baseline data if separate from template;

### Strategy policy

- Stage 1 instruction;
- personality policy/hash if active;
- strategy schema semantic version;

### Writer policy

- Stage 2 instruction;
- writing standard;
- calibration material actually used;

### Final policy

- Stage 3 instruction;
- review policy;

### Render assets

- Word masters;
- template map;
- renderer configuration;
- font/locale preflight record where available;

### Validation assets

- schema bundle version/hashes;
- validator code version/hash if practical;

No authority file is duplicated into every job object.

## 6.4 Freeze semantics

Once frozen:

- normal semantic production assumes the manifest is immutable;
- late changes are exceptional;
- any changed source/policy/template is compared against the frozen hash set;
- the system reports stale scope using the static invalidation table;
- no semantic rerun is automatically launched.

If the human elects to continue after a material change, a new run manifest or explicit amended-run version should be produced rather than silently mutating the frozen original.

## 6.5 Static invalidation lattice

**SYNTHESIS-LOCK, refined from N-01**

| Change class | Examples | Minimum stale scope |
|---|---|---|
| `SOURCE_TRUTH` | candidate authority, vacancy source | strategy, draft, final, review, render for affected job(s) |
| `STRATEGY_POLICY` | Stage 1 prompt, personality strategy contract, strategy semantics | strategy + all downstream semantic artifacts |
| `WRITER_POLICY` | Stage 2 prompt, writing standard | draft + final + review + render |
| `FINAL_POLICY` | Stage 3 prompt/review contract | final + review + render |
| `RENDER_ASSET` | Word master, font, conversion settings | rendered artifacts only |
| `SCHEMA_VALIDATION` | compatible schema/validator change | revalidate/restructure as needed; no automatic semantic rerun |

A semantic schema change that actually changes meaning must be classified under the relevant policy class rather than abusing `SCHEMA_VALIDATION`.

## 6.6 Expected-set reconciliation

**P081-HARDENED**

The finalizer never decides batch completeness by discovering directories.

Expected core jobs come from the frozen manifest.

For each expected job, it must distinguish:

- current valid final artifacts exist;
- semantic production incomplete;
- explicitly failed;
- exception/non-core job;
- stale due to manifest mismatch.

Missing output folders can therefore never make a job silently disappear from the batch.

---

# 7. Runtime filesystem and state model

## 7.1 Design rule

**SYNTHESIS-LOCK**

The filesystem is **job-centric** because the job is the natural transaction and rerun unit.

Illustrative tree:

```text
Jobbsok_26/
  authorities/
    Work_experience.md
    Education.md
    Other_high_value_information.md

  policy/
    WRITING_STANDARD.md
    PERSUASION_CALIBRATION.md
    Personality.md
    SETTINGS.md
    stage1_instruction.md
    stage2_instruction.md
    stage3_instruction.md

  templates/
    CV_MASTER.docx
    APPLICATION_MASTER.docx
    template_map.json

  schemas/
    run_manifest.schema.json
    strategy.schema.json
    draft_package.schema.json
    final_package.schema.json
    review.schema.json
    portal_answers.schema.json

  generated/
    evidence_index.json

  runs/
    <run_id>/
      batch_inventory.csv
      run_manifest.json
      run_status.json             # derived/regenerable
      review_queue.md             # derived/regenerable

      clusters/
        <cluster_id>/
          cluster_context.md      # optional, bounded, non-authoritative

      jobs/
        <job_id>/
          source/
            vacancy_original.<ext>
            vacancy_normalized.md
          job_context.json        # derived view
          context_prep.md         # optional, EXPERIMENTAL
          strategy.json
          strategy.md             # generated human view
          draft_package.json
          final_package.json
          review.json
          history/
            ...                   # only when rerun/replacement occurs
          rendered/
            cv.docx
            cv.pdf
            application.docx
            application.pdf
          portal/
            ...                   # created only when detached workflow used
```

Exact directory names may change during implementation if a simpler layout preserves the same invariants. The **job-centric transaction principle** is normative; spelling is not.

## 7.2 Authoritative versus derived runtime files

### Frozen authority

- `run_manifest.json`;
- original vacancy source;
- candidate authorities referenced by manifest;
- frozen policy/template/schema versions.

### Current semantic artifacts

- `strategy.json`;
- `draft_package.json`;
- `final_package.json`;
- `review.json`.

These are model-authored but current workflow state.

### Derived/regenerable

- evidence index;
- normalized vacancy;
- `job_context.json`;
- `strategy.md`;
- `run_status.json`;
- `review_queue.md`;
- mechanical render diagnostics.

### Experimental/advisory

- `context_prep.md`;
- any personality resonance candidate view beyond strategy's selected fields.

## 7.3 Progress state

**SYNTHESIS-LOCK**

P0.9 does not keep one manually updated progress file per stage.

`run_status.json` is a generated/reconciled operator view containing, per job:

- expected stage artifacts;
- validator state;
- completed semantic stages;
- explicit failure record if any;
- stale flags from manifest comparison;
- current final review status;
- render state;
- next actionable step.

Its state is reconstructible from manifest + artifacts + explicit failure records. It is therefore not an independent truth source.

Continuation starts with reconciliation, not blind trust in a stale `next` pointer.

## 7.4 Rerun history

Before a targeted RERUN replaces `final_package.json` or `review.json`, the current versions are copied into `history/` with an attempt identifier.

The job folder continues to expose exactly one current final/review pair.

This gives auditability without turning every normal run into an event-sourced system.

---

# 8. Model routing, chat topology and execution boundary

## 8.1 Normal model route

**P08-INHERITED**

```text
Stage 1: Sol Max
Stage 2: Terra Max
Stage 3: Sol Max
RERUN:   Sol Max, one job, separate chat
```

Model names/effort modes are implementation-era routing choices and may be updated if product capabilities change. The *role split* is the more durable architecture:

- strongest reasoning for decision architecture;
- strong native writing model for full package realization;
- strongest reasoning/writing model for final reconstruction and review.

## 8.2 Manual distinct chats

**USER-LOCKED**

No normal API orchestrator initiates semantic model stages.

The human starts each cluster-stage chat manually with the prepared stage prompt/context.

Within that chat, the model may:

- read local files through the supported environment;
- write the job artifact;
- invoke supplied deterministic validators;
- repair validation errors;
- move to the next job when the current job is safely persisted.

It may not:

- submit applications;
- spawn hidden model calls;
- run automatic semantic retries;
- silently change the frozen run.

## 8.3 Cluster sizing

**P08-INHERITED, empirical parameter**

Initial target:

- roughly five clusters for ~40 jobs;
- around eight jobs per cluster;
- normal practical band six to ten.

Cluster size is not an architectural doctrine. Change it only after evidence from context quality, early/late effects, human handling or failure rate.

## 8.4 Clustering and sequence

**SYNTHESIS-LOCK**

P0.9 v1 uses **human clustering and human-fixed sequence** in the batch inventory.

Guidelines:

- cluster by strategic similarity where shared context is genuinely useful;
- place strategically distinct jobs early enough to prevent the chat's first identity framing from dominating all later jobs;
- separate extremely similar jobs where phrase convergence is a risk;
- do not require a model-generated cluster-preflight pass;
- do not create a separate core `cluster_plan.json` merely to restate frozen input.

## 8.5 Priority A/B

**SYNTHESIS-LOCK**

P0.9 removes differentiated Priority A/B treatment from production semantics.

There is no:

- extra compute for A;
- mandatory microvariation for A;
- different stage instruction for A/B;
- cluster-plan state whose only purpose is A/B.

The system may optionally log a non-treatment `opportunity_prediction` for research, but it must not affect treatment. If such predictions show no useful relationship to later human top-quality judgments, remove them.

Human `user_priority` remains valid because it represents the operator's actual application preference/scheduling, not an attempt to infer package quality.

---

# 9. Stage 1 - Decision Architecture

## 9.1 Purpose

**P08-INHERITED, refined by P09**

Stage 1 answers:

> What truthful candidate identity, evidence set, employer-decision argument and writing architecture gives this specific vacancy the highest expected interview value?

It is not primarily a prose-writing stage.

## 9.2 Read-order protocol

**P081-HARDENED / N-06 PROTOCOL**

For each job:

1. open original/normalized vacancy first;
2. form a provisional employer decision model and requirement structure;
3. inspect `job_context.json` and evidence index;
4. open candidate primary sources as needed;
5. only after evidence understanding, read personality context if enabled;
6. produce strategy;
7. run validator;
8. repair/revalidate if needed;
9. persist before moving to next job.

This is a **debiasing protocol**, not cryptographic or filesystem isolation. Tests must not pretend otherwise.

## 9.3 Stage 1 responsibilities

Stage 1 must:

- identify the employer's likely decision problem;
- map explicit material requirements;
- identify strongest candidate identity for the vacancy;
- select primary and supporting evidence;
- record evidence ceilings and gaps;
- identify likely objection(s) and truthful reframing;
- decide headline hypothesis;
- decide CV emphasis and application backbone;
- define channel roles between CV and letter;
- formulate motivation that is specific and grounded;
- if personality ON, select 0-3 relevant interpretive facets only after evidence is known;
- choose at most one primary interest spark and, if genuinely useful, one support spark;
- preserve one meaningful counterfactual strategy route;
- explicitly mark areas where the final writer should remain free;
- set `elasticity = ELASTIC`.

## 9.4 Requirement map

Recommended private structure:

```json
{
  "requirement": "...",
  "materiality": "HIGH|MEDIUM|LOW",
  "candidate_relation": "SUPPORTED|ADJACENT|GAP|NOT_MATERIAL|UNKNOWN",
  "evidence_refs": ["..."],
  "claim_ceiling": "...",
  "package_role": "CV|APPLICATION|BOTH|DO_NOT_FORCE"
}
```

This map is not rendered to the employer.

## 9.5 Stage 1 must not

- invent facts;
- draft a full application letter as a substitute for strategy;
- force every requirement into final prose;
- assume the current job resembles the previous job in the cluster;
- treat personality as evidence;
- let a context-prep artifact define what sources may be opened;
- optimize for a numeric fit probability;
- write a strategy so rigid that Stage 3 becomes a proofreader.


---

# 10. Canonical strategy contract

## 10.1 Format selection

**SYNTHESIS-LOCK: canonical JSON + generated Markdown view**

P0.8.1's Markdown strategy was robustly human-readable, but the P0.9 corpus exposes four distinct consumers:

1. Terra writer;
2. final Sol;
3. deterministic evidence/provenance validation;
4. human audit.

P0.9 therefore uses one canonical `strategy.json` and one deterministic human-readable `strategy.md` generated from it.

There is **no model-written second Markdown strategy**. This avoids dual truth.

## 10.2 Why structured strategy is selected despite X-5

The strongest case for structure is not JSON parsing. It is that several decision-critical ideas should be mechanically present:

- evidence refs;
- evidence claim ceilings;
- requirement coverage;
- elasticity;
- counterfactual reserve;
- personality handoff when enabled;
- risk/gap fields;
- CV/application channel roles.

The main counter-risk is **formalization-authority leakage**: a schema-valid object may look too final.

P0.9 directly compensates for this by making these fields mandatory:

```json
{
  "artifact_role": "STRATEGY_HYPOTHESIS",
  "authority": "NON_FACTUAL_NON_FINAL",
  "elasticity": "ELASTIC",
  "final_writer_may_reconstruct": true
}
```

Stage 3's read-order contract and change logging are equally important. Structured strategy without those compensators is not compliant P0.9.

## 10.3 Strategy schema - conceptual form

The exact JSON Schema may evolve during implementation, but the semantic contract is:

```json
{
  "schema_version": "p0.9.strategy.v1",
  "job_id": "...",

  "artifact_role": "STRATEGY_HYPOTHESIS",
  "authority": "NON_FACTUAL_NON_FINAL",
  "elasticity": "ELASTIC",
  "final_writer_may_reconstruct": true,

  "employer_decision_model": "short prose",
  "candidate_identity": {
    "one_line": "...",
    "why_this_identity": "...",
    "avoid_identity": ["..."]
  },

  "headline_hypothesis": "...",

  "requirements": [
    {
      "requirement": "...",
      "materiality": "HIGH",
      "candidate_relation": "SUPPORTED",
      "evidence_refs": ["E-..."],
      "claim_ceiling": "...",
      "package_role": "BOTH"
    }
  ],

  "evidence_plan": {
    "primary": [
      {
        "evidence_ref": "E-...",
        "role": "...",
        "claim_ceiling": "...",
        "channel_role": "CV|APPLICATION|BOTH"
      }
    ],
    "supporting": [],
    "alternatives": []
  },

  "objections_and_reframes": [
    {
      "objection": "...",
      "truth_safe_reframe": "...",
      "evidence_refs": ["..."]
    }
  ],

  "motivation_bridge": "...",

  "interest_spark": {
    "status": "USED|NOT_USEFUL",
    "primary": null,
    "supporting": null
  },

  "personality_resonance": {
    "status": "DISABLED|NOT_USEFUL|USED",
    "selected_facets": []
  },

  "cv_direction": {
    "headline": "...",
    "profile_direction": "...",
    "competency_priorities": ["..."],
    "employment_emphasis": ["..."]
  },

  "application_direction": {
    "backbone": "...",
    "opening_job": "...",
    "proof_sequence": ["..."],
    "closing_job": "...",
    "avoid": ["..."]
  },

  "counterfactual_reserve": {
    "alternate_identity": "...",
    "alternate_evidence_refs": ["..."],
    "trigger_to_switch": "...",
    "why_secondary": "..."
  },

  "gaps_and_risks": ["..."],
  "source_escape_notes": ["..."],
  "strategy_notes_for_writer": ["..."]
}
```

## 10.4 Strategy length and compression

**P09-EVIDENCE + SYNTHESIS-LOCK**

Target total substantive prose:

- simple job: ~400-700 words equivalent;
- complex job: ~700-1000 words equivalent;
- soft ceiling ~1200 words;
- no minimum.

The goal is **decision density**, not shortness.

Compression is safe because:

- evidence refs preserve source access;
- counterfactual reserve preserves an alternate route;
- Stage 2/3 can source-escape;
- final writer is elastic.

## 10.5 Schema hard versus quality soft

The JSON schema may hard-enforce:

- IDs;
- enums;
- array/object structure;
- maximum list sizes generous enough to prevent runaway output;
- required evidence-ref field presence;
- no unknown critical fields if that aids validation.

It must **not** hard-enforce subjective writing targets such as:

- exact strategy word count;
- exact number of arguments;
- exact application length unless employer-imposed;
- exact number of evidence items;
- arbitrary confidence scores.

Quality rules belong in stage instructions and review policy, not schema.

## 10.6 Cheap falsification safeguard

Because strategy format was historically unresolved, the implementation may run one small pre-release E-01 comparison before locking fixtures permanently.

Reversal criterion is not merely "JSON validates less often". The important failure signal is:

- structured strategy systematically makes final Sol less willing to change a weak strategy;
- final human quality declines;
- Terra becomes generic field-filling rather than writing coherently.

If that occurs, revert to canonical stable-label Markdown **without changing the rest of P0.9 architecture**.

This is a rollback gate, not an open architecture dependency.

---

# 11. Stage 2 - Native Package Writer

## 11.1 Purpose

Stage 2 turns the decision architecture into a complete, natural Norwegian application package.

It is not a template filler in the rhetorical sense. It owns **native prose realization**, coherence, voice, and first-pass editing.

## 11.2 Inputs

For each job, Terra receives only the material needed to write well:

- original/normalized vacancy;
- `job_context.json`;
- canonical `strategy.json`;
- writing standard;
- targeted candidate sources/evidence refs as needed;
- CV baseline dynamic-zone contract;
- distilled personality guidance only when personality is ON and Stage 1 selected facets;
- no raw Luna context by default.

It can reopen original candidate authorities when the strategy is insufficient or ambiguous.

## 11.3 Writer freedom

Stage 2 should follow strategy strongly, but not mechanically.

If the strategy contains an unwriteable, contradictory or obviously weak instruction, Terra may make a bounded correction and record a short `writer_delta`.

`writer_delta` is not a second strategy. It exists only when the writer materially departs from the hypothesis.

## 11.4 Draft package contract

Conceptually:

```json
{
  "schema_version": "p0.9.package.v1",
  "job_id": "...",
  "cv_overrides": {
    "headline": "...",
    "profile": "...",
    "competencies": ["..."],
    "employment": {
      "<employment_id>": {
        "default_bullets": ["... full replacement array ..."]
      }
    }
  },
  "application": {
    "text": "..."
  },
  "used_evidence_refs": ["..."],
  "writer_delta": null
}
```

The exact key names may be adapted to the baseline/template map, but semantics must remain fixed.

## 11.5 Employment override semantics

**P081-HARDENED**

If an employment override exists for one employment entry, its bullet array is a **full replacement** of that employment's dynamic/default bullet set.

Forbidden ambiguous behaviors:

- append model bullets to baseline bullets;
- merge by list position;
- silently fall back to unspecified baseline bullets in the same overridden employment;
- treat empty array as "use defaults" unless explicitly specified.

This is one of the most important deterministic CV contracts.

## 11.6 Application-writing doctrine

The application should normally:

- open on the employer's problem/opportunity, not generic enthusiasm;
- establish a single candidate identity/backbone;
- use a small number of evidence-rich proof arcs;
- connect evidence to future usefulness;
- express motivation through actual work/problem fit rather than flattery;
- surface gaps honestly when necessary rather than disguising them;
- avoid keyword stuffing and requirement checklist prose;
- avoid generic "I am structured, analytical and solution-oriented" claims without evidence;
- avoid synthetic LinkedIn/AI tone;
- use native, restrained, confident Bokmal;
- remain plausibly written by the candidate.

Length is a soft editorial target unless the employer imposes a hard limit.

## 11.7 CV-writing doctrine

Dynamic CV text should:

- increase decision relevance, not merely keyword density;
- preserve factual chronology;
- use compact evidence-bearing bullets;
- foreground the experience most diagnostic for this employer;
- avoid inflating role scope or formal authority;
- preserve readable page density;
- never dynamically rewrite factual scaffolding that baseline owns.

## 11.8 Stage 2 completion

Before moving to the next job:

1. write `draft_package.json`;
2. run the Stage 2 validator;
3. repair up to two times if validation fails;
4. on third failed validation, record job failure for Stage 2 and continue;
5. never mark Stage 2 completed while its current artifact fails validator.

---

# 12. Stage 3 - Elastic Final Writer and Selective Review

## 12.1 Purpose

Stage 3 is the system's final semantic quality stage.

It performs two linked but distinct jobs:

1. reconstruct/repair the package to the strongest truth-safe final form;
2. classify any remaining repair scope for human action.

It is **not** an independent external judge.

## 12.2 Read-order protocol

For each job:

1. read vacancy first and form a fresh provisional view;
2. inspect relevant candidate evidence / evidence index;
3. then read strategy and draft;
4. use raw source escape when needed;
5. read personality context only if relevant/active;
6. produce final package;
7. synchronize final evidence refs;
8. produce review object;
9. validate both;
10. repair/revalidate before completion.

Again, this is a `PROTOCOL`, not enforceable isolation.

## 12.3 Elastic reconstruction authority

**USER-LOCKED**

Stage 3 may:

- change headline;
- change candidate identity framing;
- replace primary evidence;
- switch to counterfactual reserve;
- change CV emphasis;
- rewrite the entire application;
- change opening/closing;
- remove personality-conditioned material;
- reopen evidence not surfaced upstream;
- reject Stage 1's argument architecture.

It may not:

- invent factual support;
- exceed claim ceilings;
- mutate source truth;
- ignore employer hard constraints;
- reinterpret a validator pass as proof of semantic truth.

## 12.4 Final package

`final_package.json` uses the same semantic package schema as the draft so deterministic finalization needs one source map.

It becomes the **current semantic package authority for that job**, subordinate only to factual authorities/vacancy and human approval.

## 12.5 Mandatory evidence reconciliation

Stage 3 must rebuild `used_evidence_refs` from the final content.

If final text uses evidence that neither optional context prep nor strategy surfaced, record:

```json
"evidence_outside_prep_refs": ["..."]
```

and derive the count.

When context prep is OFF, the field may be empty or marked N/A depending schema implementation; it must not imply a prep failure that did not exist.

## 12.6 Upstream claim repair trace

**P081-HARDENED / N-05**

Review includes:

```json
{
  "upstream_claim_repaired": true,
  "upstream_claim_repair_note": "short non-sensitive description"
}
```

This is not for blaming Stage 2. It measures how often final truth repair was necessary and becomes a direct signal for improving upstream instructions.

## 12.7 Strategy change trace

Review also records whether final Sol materially reconstructed strategy:

```json
{
  "material_strategy_change": true,
  "strategy_change_summary": "..."
}
```

This is central to detecting structured-strategy authority inflation.

## 12.8 Anti-convergence check

Before saving final text, Stage 3 asks qualitatively:

> What does this package say, show or imply that a polished generic package for this candidate would not?

This is not an employer-facing phrase and not a numeric score.

The purpose is to detect identity collapse across similar jobs.

## 12.9 Review object

Recommended conceptual form:

```json
{
  "schema_version": "p0.9.review.v1",
  "job_id": "...",
  "status": "READY|CHECK|RERUN",
  "reasons": ["..."],
  "upstream_claim_repaired": false,
  "upstream_claim_repair_note": null,
  "material_strategy_change": false,
  "strategy_change_summary": null,
  "evidence_outside_prep_refs": [],
  "human_attention": ["..."],
  "known_limitations": ["..."]
}
```

No numeric quality/confidence score is required.

## 12.10 Status semantics

**P081-HARDENED**

### READY

Use when no material issue requiring human repair is known.

Human still reviews before submission.

### CHECK

Use when remaining issues are localized and bounded, for example:

- wording that deserves human preference judgment;
- a narrow claim-strength nuance;
- visual/render issue that can be inspected locally;
- employer-specific detail needing confirmation;
- small fit/motivation nuance.

### RERUN

Use when the remaining defect is structural/strategic, such as:

- wrong candidate identity;
- weak or mismatched primary evidence;
- broken application backbone;
- multi-section rewrite required;
- serious convergence/genericity;
- uncertainty too broad for a local human edit to be efficient.

Known unsupported claims must be repaired before saving; an unsupported claim is not left in the package and merely labeled CHECK.

### FAILED

`FAILED` is deterministic runtime state, not a Stage 3 self-assessment. It means the semantic stage could not produce validator-clean required artifacts within the bounded repair protocol.

---

# 13. RERUN contract and partial success

## 13.1 RERUN route

**P081-HARDENED**

A RERUN is:

- manually initiated;
- one job;
- separate chat;
- Sol Max;
- full relevant vacancy/source access;
- access to current strategy/draft/final/review/history;
- free to reconstruct the package;
- required to write a replacement final package and review;
- validated before becoming current.

It is **not**:

- automatic retry;
- a standard fourth stage for all jobs;
- a code-triggered model call;
- a hidden retry loop.

## 13.2 Partial-success invariant

One failed or weak job does not invalidate successful jobs.

Batch completion states are per job.

A run may finish with a mixture of:

- `DELIVERED_READY`;
- `DELIVERED_CHECK`;
- `DELIVERED_RERUN`;
- `FAILED`;
- exception/non-core jobs.

The finalizer may return nonzero overall status while preserving all valid delivered outputs.

## 13.3 Tail economics

The system is explicitly allowed to stop investing in a weak tail when:

- repair cost is disproportionate;
- vacancy fit is weak;
- deadline/opportunity value is low;
- the human chooses not to submit;
- rare channel structure makes standard processing inefficient.

This is not failure of the quality objective. It is the intended Selective Quality policy.

---

# 14. Deterministic validation architecture

## 14.1 Three validation classes

**P081-HARDENED**

### Class A - mechanical hard failures

Deterministic code can and should enforce:

- JSON/schema validity;
- job/run identity equality;
- expected job set;
- valid evidence-ref syntax/resolution;
- required object/field presence;
- forbidden placeholders;
- path safety;
- output file existence;
- hard portal limits in detached portal module;
- template mapping keys;
- document generation prerequisites;
- no leftover unresolved transient template controls where the renderer contract forbids them.

### Class B - semantic hard truth policy

Models/human enforce:

- no unsupported factual claims;
- no inflated role/authority;
- no invented motivation facts;
- evidence supports actual wording;
- requirement/gap representation is honest.

Python should not pretend to prove these through keyword matching.

### Class C - soft quality/review

Examples:

- naturalness;
- distinctiveness;
- persuasion;
- compression;
- redundancy;
- page density;
- motivation strength;
- cross-job convergence.

These guide models/human review and pilot analysis.

## 14.2 Standard validator rule

There must be one documented stage-validator interface, not ad hoc one-liners embedded in prompts.

Internal modules may be as small as necessary. The operator surface should remain simple.

## 14.3 Same-chat repair protocol

**USER permission + N-04**

For any semantic stage:

```text
validator exit != 0
  -> model reads exact validator error
  -> repairs artifact in same chat
  -> validates again
  -> maximum two repair attempts
  -> third failure => record FAILED for that stage/job
  -> do not mark completed
  -> continue to next independent job when safe
```

No model call is launched by validator code.

## 14.4 Validator output design

Errors must be:

- deterministic;
- localized where possible;
- stable enough for tests;
- useful to a model/human;
- explicit about file, field and violated invariant.

Example:

```text
E_STRATEGY_EVIDENCE_REF_UNKNOWN:
job=FIN-014
field=evidence_plan.primary[1].evidence_ref
value=E-WORK-0091
reason=not present in frozen evidence index
```

Avoid vague `validation failed` output.

## 14.5 No keyword-theatre testing

A stage contract is not proven because an instruction contains required phrases.

Tests should target observable behavior/structure where deterministic, and pilot behavior where semantic.

Examples of non-proofs:

- prompt contains "read vacancy first";
- output contains "truthful";
- `_DONE.md` contains stage name.

These are protocols, not boundaries.

---

# 15. Evidence navigation and context architecture

## 15.1 Core control: deterministic index

**SYNTHESIS-LOCK**

The deterministic candidate evidence index is part of baseline P0.9.

It is deliberately minimal:

- indexes structure and stable addresses;
- does not predict relevance;
- does not summarize candidate facts;
- does not create a claim graph;
- does not rank evidence for vacancies.

Models remain responsible for interpretation.

## 15.2 Source Escape Protocol

Every semantic stage may open original candidate sources when:

- the index is insufficient;
- a strategy/draft claim needs verification;
- context prep appears lossy;
- evidence refs point to a section requiring fuller context;
- the model suspects important omitted information.

No upstream handoff can prohibit source escape.

## 15.3 No summary-of-summary as factual carrier

An optional context-prep artifact may point to evidence, but Stage 1 should not ground a material employer claim in:

```text
Luna summary -> Sol strategy -> Terra prose
```

without the relevant primary source being addressable/reopenable.

The same principle applies to personality summaries and previous packages.

## 15.4 Context ordering

Question-aware ordering is preferred:

- employer/vacancy first;
- then candidate navigation/evidence;
- then optional interpretive layers;
- then prior model artifacts.

This reduces anchoring without pretending long-context order creates independence.

---

# 16. Optional Luna context-prep module

## 16.1 Status

**EXPERIMENTAL, default OFF**

Luna's low cost is not sufficient reason to add a stage. Its only legitimate question is:

> Does a bounded cheap prep pass improve final package quality or reduce stronger-model retrieval burden enough to justify the extra prompts/context/anchoring risk beyond the deterministic evidence-index control?

## 16.2 Preconditions

Luna prep may be tested only after:

- deterministic evidence index exists;
- source escape exists;
- context artifacts are labeled non-authoritative;
- Stage 1 reads vacancy first;
- Luna output cannot exclude source access;
- personality is not passed to Luna;
- `elasticity` remains ELASTIC;
- a control run without Luna is available.

## 16.3 Allowed Luna tasks

Only bounded, source-linked advisory work such as:

- literal requirement extraction;
- source navigation hints;
- candidate evidence candidates with refs;
- lifecycle/claim-ceiling extraction where explicit;
- contradiction/gap surfacing;
- actor/problem map;
- cross-source bridge candidates;
- cluster convergence/collision notes;
- job-local context slices.

## 16.4 Forbidden Luna tasks in P0.9 core

Luna does not:

- choose final candidate identity;
- write employer-facing CV/application prose;
- establish factual authority;
- see/use personality for positioning;
- remove evidence from stronger-model access based on relevance;
- decide final fit;
- review final package;
- become mandatory production dependency.

## 16.5 Output

If enabled, output is job-local `context_prep.md` or equivalent.

Header must explicitly state:

```text
ADVISORY CONTEXT ONLY
NOT FACTUAL AUTHORITY
NOT A SOURCE FILTER
PRIMARY SOURCES REMAIN AVAILABLE
```

## 16.6 Fail-open behavior

If Luna prep is missing, invalid or judged unhelpful, Stage 1 proceeds normally from deterministic index + sources.

The job must never fail because an experimental prep artifact is absent.

## 16.7 Evaluation

Compare against deterministic-index-only control, not against "no navigation".

Measure at minimum:

- final human quality;
- stronger-model source openings if observable;
- evidence recall;
- `evidence_outside_prep_refs`;
- added prompt/human overhead;
- signs of anchoring or bloat.

If no material benefit appears, remove or leave OFF indefinitely.


---

# 17. Personality / authenticity architecture

## 17.1 Role

**USER-LOCKED boundary + SYNTHESIS-LOCK implementation posture**

`Personality.md` is an **interpretive positioning lens**, not a candidate factual authority.

Its legitimate purpose is to help answer:

- which truth-supported aspects of the candidate are especially characteristic;
- how a real behavior may be useful for this employer;
- how the same behavior might be misread;
- how to frame it accurately without caricature;
- where an authentic "interest spark" may make the package feel more candidate-specific.

It must never:

- create experience;
- establish a skill unsupported by factual authorities;
- turn typology into employer-facing evidence;
- justify claims because "the candidate's personality says so";
- produce cosplay or conspicuous self-branding.

## 17.2 Runtime status

**SYNTHESIS-LOCK**

P0.9 implements the personality capability but ships the first baseline with:

```text
personality = OFF
```

until a small paired test shows a meaningful quality benefit without unacceptable cringe, overexpression, factual stretch or human-edit cost.

This resolves the historical default uncertainty without discarding the feature.

## 17.3 Canonical source versus runtime view

The rich canonical personality source may preserve broad nuance and internal conceptual mappings.

The runtime must use a **thin application-facing interface**.

Important design choice:

> The canonical source may contain more facets than runtime normally selects. The exact number of stored facet IDs is not a P0.9 contract.

This avoids incorrectly ratifying the assistant-generated 20-facet derivative as architecture.

## 17.4 Selection protocol when ON

Stage 1:

1. reads vacancy and candidate evidence first;
2. asks whether personality adds decision value;
3. may select **0-3** facets;
4. zero facets is fully valid;
5. every selected facet must be linked to candidate factual evidence;
6. records desired recruiter read, likely misread, prevention rule and expression ceiling;
7. chooses a channel only if explicit expression is beneficial.

Conceptual handoff:

```json
{
  "status": "USED|NOT_USEFUL",
  "selected_facets": [
    {
      "facet_id": "PF-...",
      "relevance": "...",
      "evidence_refs": ["..."],
      "desired_recruiter_read": "...",
      "misread_risk": "...",
      "prevention_rule": "...",
      "expression_ceiling": "...",
      "channel_guidance": "INTERNAL_ONLY|CV|APPLICATION|BOTH"
    }
  ],
  "avoid": ["..."]
}
```

## 17.5 Terra exposure

Terra receives only the selected distilled guidance needed to write.

It does not receive, by default:

- the full personality profile;
- MBTI/DISC/Enneagram/RIASEC labels;
- failure-mode taxonomy;
- raw typology reasoning;
- unrelated facets.

This prevents three independent personality strategies across the three stages.

## 17.6 Final Sol authority

Final Sol may:

- suppress all personality-conditioned language;
- replace the selected facet framing;
- decide the feature did not help after seeing the draft;
- keep the personality effect purely implicit.

The feature's purpose is *candidate specificity*, not visible personality jargon.

## 17.7 Interest spark

A valid spark has three elements:

1. a real employer problem/opportunity;
2. a characteristic candidate approach or interest;
3. factual evidence showing the connection is credible.

P0.9 allows:

- at most one primary spark;
- optionally one supporting spark;
- zero sparks.

The strategy owns the **angle**. The writer owns **expression**. Mandatory multi-opening microvariation is removed.

## 17.8 Paired evaluation

Personality adoption test uses identical jobs/inputs with OFF versus ON variants.

Score:

- overall package quality;
- authenticity/candidate specificity;
- employer relevance;
- evidence defensibility;
- overexpression/cringe risk;
- human edits/minutes.

Blinding should be used if practical, but lack of perfect blinding does not make all learning impossible. The user has not yet locked a blinding method.

If the effect is weak/noisy, keep OFF rather than inventing a more elaborate personality engine.

---

# 18. Detached portal-answer workflow

## 18.1 Architectural boundary

**SYNTHESIS-LOCK**

Portal handling is a separate downstream workflow from the approved core package.

Core run status does not depend on portal output.

## 18.2 Inputs

Portal derivation receives:

- exact employer questions;
- exact character/word limits;
- input type where relevant (free text, yes/no, checkbox, date, salary etc.);
- vacancy source;
- current final CV/application package;
- candidate authorities/evidence index for source escape;
- optional human notes.

The form structure is captured **when actually needed**, not guessed from platform name.

## 18.3 Portal input artifact

Recommended:

`portal_input.json`

```json
{
  "job_id": "...",
  "captured_at": "...",
  "questions": [
    {
      "question_id": "q1",
      "prompt": "...",
      "type": "FREE_TEXT",
      "max_chars": 1000,
      "max_words": null,
      "required": true
    }
  ]
}
```

Portal platform metadata may be included for operator reference but must not override the captured form.

## 18.4 Portal answer semantics

Answers should:

- remain consistent with the approved package;
- answer the exact question rather than paste letter fragments mechanically;
- respect hard limits exactly;
- source-escape where factual precision requires it;
- avoid introducing stronger claims than the core package/source truth supports.

## 18.5 Model route

This is not a standard fourth semantic stage.

Default recommendation:

- use Terra-class strong native writer for ordinary short/structured answers;
- use Sol-class reasoning when the portal question itself requires substantial strategic reframing;
- batch several portal jobs in one manual chat when it clearly reduces human overhead and the jobs remain independent.

The exact route is implementation policy, not a core architecture dependency.

## 18.6 Validation

Hard-validate:

- answer/question IDs;
- required answers present;
- exact char/word limits;
- no placeholder text;
- safe encoding.

Human copy/pastes/submits. No browser automation is required.

---

# 19. Settings and configuration philosophy

## 19.1 Rule: configuration only for real modes

P0.9 does not build settings for hypothetical future flexibility.

A setting exists only when:

- two legitimate modes exist now;
- the mode materially changes behavior;
- user may rationally switch it between runs;
- static mapping is sufficient.

No settings compiler or instruction cache is needed.

## 19.2 `SETTINGS.md`

Human-readable, deliberately small.

Recommended P0.9 v1:

```text
personality = OFF | ON
context_prep = OFF | LUNA_JOB_LOCAL
```

Defaults:

```text
personality = OFF
context_prep = OFF
```

`strategy_elasticity` is **not** a configurable first-release knob because the user has explicitly locked it to ELASTIC.

Core language and product boundary are version-level architecture choices, not runtime toggles.

## 19.3 Static mapping

The stage prompt maps settings to short fixed instruction fragments.

No model-generated prompt compilation.

No cached compiled instructions.

No dynamic dependency inference.

---

# 20. Document generation and rendering architecture

## 20.1 Design objective

The document layer should preserve professional established masters and deterministic layout while keeping semantic generation upstream in machine-readable package artifacts.

The model does not directly edit arbitrary Word XML as part of semantic reasoning.

## 20.2 Baseline empirical note from prior P0.7 inspection

This P0.9-focused synthesis retains one earlier empirical finding because it materially changes how P0.8.1/P0.9 template research should be interpreted:

- the inspected P0.7 CV master contained plain, non-data-bound Word content controls;
- it contained no tables, text boxes or drawings in the inspected structure;
- the finalizer filled and **unwrapped** the content controls before LibreOffice;
- it validated that no content controls remained in the final document.

Therefore generic external warnings about "content controls" do **not** by themselves justify discarding that master/template technique.

This is empirical baseline evidence, not a new P0.8.1/P0.9 source claim.

## 20.3 Template reuse rule

**USER-LOCKED reuse policy**

Legacy templates/code may be reused only after explicit:

1. inspection;
2. adaptation;
3. optimization;
4. target-environment verification.

Fresh P0.9 runtime does not imply gratuitously redesigning a template that already performs well.

## 20.4 Package-to-template source map

**P081-HARDENED**

There must be one canonical mapping from package fields to template slots.

Example conceptual map:

```json
{
  "cv.headline": "CV_HEADLINE",
  "cv.profile": "CV_PROFILE",
  "cv.competencies": "CV_COMPETENCIES",
  "cv.employment.<id>.default_bullets": "EMP_<id>_BULLETS",
  "application.text": "APPLICATION_BODY"
}
```

No separate competing mapping in code and documentation.

## 20.5 Finalizer transaction

For each expected job:

1. verify current `final_package.json` + `review.json`;
2. merge dynamic CV zones into stable baseline;
3. fill application master;
4. remove transient template controls/placeholders as required;
5. save DOCX outputs to temporary job transaction path;
6. convert required PDFs;
7. validate each expected output independently;
8. atomically promote outputs only when the job transaction passes;
9. otherwise preserve last known valid delivered outputs and report failure.

## 20.6 LibreOffice process policy

P0.8.1 recommended one isolated LibreOffice invocation per job to reduce process startup. External research warns against assuming multi-file conversion has ideal all-or-nothing semantics.

Integrated P0.9 rule:

> Treat the **job** as the transaction, but treat **each document result** as independently verifiable.

Implementation may convert both DOCX files in one isolated invocation **only after target-Windows smoke testing proves the behavior reliable**.

Otherwise use one isolated invocation per document.

Do not build a persistent LibreOffice service/daemon in P0.9.

## 20.7 Target-environment preflight

**ENV-VERIFY**

Before real production:

- install/locate LibreOffice or chosen converter;
- verify `soffice --headless` on target Windows environment if LO is used;
- verify writable isolated user profile path;
- verify fonts;
- verify locale/Unicode;
- verify output directory/path handling;
- verify two real masters;
- verify sparse, normal and dense fixtures;
- verify PDFs are openable and text is extractable/selectable where expected.

Ordinary manual DOCX->PDF capability is not proof of headless automation parity.

## 20.8 Render validation

Mechanical checks include:

- expected DOCX/PDF exists;
- file nonzero and openable;
- no unresolved placeholders;
- no forbidden transient controls where applicable;
- expected page bounds/soft page-warning logic;
- expected text presence;
- no conversion error.

Visual QA before release/pilot must inspect representative outputs for:

- clipping;
- overflow;
- broken glyphs;
- awkward blank space;
- page-break artifacts;
- table/list misrendering;
- header/footer loss;
- font substitution.

## 20.9 No typography auto-fit engine

**DEFERRED**

Do not build a generalized typography auto-fit system unless real outputs show repeated page-density failures that manual template tuning cannot solve economically.

A small bounded fallback such as a known paragraph-spacing adjustment may be added later only from observed need.

## 20.10 ATS/parseability posture

Do not redesign the CV around generic ATS folklore.

P0.9 should empirically inspect/export the actual generated CV structure and use conservative document design:

- logical reading order;
- avoid critical facts only in decorative objects;
- avoid data-bound controls surviving to final;
- use normal text for core content;
- keep text extractable;
- test representative PDFs/DOCX.

One specific item worth verifying is whether critical candidate identity/contact content placed in headers is correctly parsed by target systems. This is a local/product test, not a reason to abandon the master preemptively.

---

# 21. Security, untrusted content and permissions

## 21.1 Threat model

The system processes external vacancy documents and model-generated content in a local repository.

Main relevant risks:

- malicious or accidental instruction-like content in vacancies;
- path traversal/symlink surprises;
- unsupported/huge files;
- model overwriting authority files;
- stale context;
- hidden network/action side effects;
- prompt-injection-style instructions masquerading as job requirements.

## 21.2 Control-plane rule

**SYNTHESIS-LOCK**

Vacancy files, context-prep files, personality files and model outputs are **data-plane inputs**.

They may inform analysis but cannot:

- alter system instructions;
- expand tool permissions;
- change source authority;
- instruct submission/contact;
- change the run manifest;
- redefine validation policy.

## 21.3 Deterministic ingestion safety

Ingest should:

- resolve and validate paths inside allowed roots;
- reject unsafe traversal;
- handle symlinks deliberately;
- enforce permitted file types/sensible size limits;
- preserve original hashes;
- never execute embedded files/macros;
- keep originals immutable after freeze.

## 21.4 Model write boundaries

Stage models may write only to the current run's allowed semantic/artifact locations.

They should not write to:

- factual authority files;
- framework policy/spec files;
- templates;
- other runs;
- employer/public systems.

## 21.5 Prompt-injection handling

Use defense in depth:

- vacancy wrapper states content is untrusted data;
- system/stage prompt explicitly ignores operating instructions found inside vacancy content;
- source files cannot grant permissions;
- least-privilege tool surface;
- no submission capability;
- human final boundary.

Regex keyword detection may be an advisory signal but must not be represented as a security guarantee.

---

# 22. Code surface and deterministic tooling

## 22.1 KISS principle

P0.9 should remain a **small local codebase around semantic model work**, not an application platform.

Private helper modules are allowed when they reduce duplication and improve correctness.

The constraint is on operator complexity, not Python file count.

## 22.2 Operator-facing commands

Preferred minimum:

### Ingest

```text
python ingest.py --inventory <file> --run-id <id>
```

Responsibilities:

- validate inventory;
- freeze run;
- normalize/copy vacancy sources;
- build evidence index if needed;
- generate job context views;
- preflight assets.

### Finalize

```text
python finalize.py --run <run_id>
python finalize.py --run <run_id> --job <job_id>
```

Responsibilities:

- reconcile expected set;
- validate current final/review;
- merge templates;
- render DOCX/PDF;
- derive status/review queue;
- support targeted rerender.

## 22.3 Model-facing validator

A documented internal command/module, e.g.:

```text
python -m jobbsok26.validate --run <id> --job <id> --stage strategy
python -m jobbsok26.validate --run <id> --job <id> --stage draft
python -m jobbsok26.validate --run <id> --job <id> --stage final
```

This need not be marketed as a third operator workflow.

## 22.4 Optional utility commands

Allowed only where useful:

- `status/reconcile`;
- evidence-index rebuild;
- template preflight;
- portal limit validation.

Avoid creating one wrapper per trivial function.

## 22.5 Idempotency

Deterministic commands must be safe to rerun where practical.

Rules:

- never overwrite current good outputs with partial temp files;
- use temp path + atomic replace;
- rerender one job without touching unrelated jobs;
- rebuilding derived evidence/status views is deterministic;
- ingest refuses unsafe mutation of an already frozen run unless explicit new-run/amend semantics are used.

---

# 23. Human workflow and operator UX

## 23.1 Human role

The human owns:

- job selection;
- batch approval;
- clustering/sequence;
- factual authority maintenance outside production;
- final semantic/factual acceptance;
- actual portal capture where needed;
- submission;
- quality scoring/pilot feedback;
- decision to rerun/drop/exception-handle a job.

The human should **not** be required to:

- confirm every job between model generations;
- manually synchronize status files;
- reconcile artifact directories;
- repeatedly re-enter candidate facts;
- inspect every model's intermediate reasoning;
- rescue all weak jobs.

## 23.2 Human review queue

`review_queue.md` is generated from current run state.

Suggested grouping:

1. READY - normal skim/approval/submission;
2. CHECK - bounded issue with explicit attention note;
3. RERUN - strategic failure candidate;
4. FAILED - mechanical/runtime incomplete;
5. EXCEPTION - handled outside core.

Within groups, sort by user priority/deadline rather than an opaque model score.

## 23.3 Human-time metric

Measure **total human minutes per submitted package**, not edit minutes alone.

Where practical separate:

- review minutes;
- edit minutes;
- portal minutes;
- submission/admin minutes.

But if detailed timing creates too much burden, capture one total plus exceptional notes. An unrecorded metric has no value.

## 23.4 No routine between-job confirmation

Within a validated cluster-stage chat, the model proceeds job by job.

Human interruption is reserved for:

- unresolved factual ambiguity requiring the user;
- run-level source mismatch;
- safety/permission issue;
- repeated validator failure that cannot be resolved locally;
- explicit request from the user.

---

# 24. Pilot, measurement and learning architecture

## 24.1 Three evidence loops

### Loop A - deterministic engineering proof

Goal: prove the runtime works.

No model-quality inference.

### Loop B - clean product baseline

Goal: observe real Sol->Terra->Sol package quality/human cost with experimental modules OFF.

### Loop C - paired mechanism tests

Goal: identify whether one optional mechanism improves the product enough to justify itself.

## 24.2 Before broad model use: engineering gates

### Gate A0 - precedence/authority

- candidate sources current;
- spec version fixed;
- no stale conflicting instructions in runtime;
- batch inventory canonical.

### Gate A1 - template/environment spike

- masters parseable;
- renderer works target-side;
- required fonts/locale available;
- finalizer approach viable.

### Gate A2 - one-job deterministic vertical slice

Using synthetic/fixture package artifacts:

```text
inventory -> freeze -> job view -> strategy/draft/final schema fixtures
-> finalizer -> DOCX/PDF -> status
```

Must work before relying on models.

## 24.3 Live developer smoke

Use two real jobs with the baseline architecture.

Purpose:

- model instructions actually executable;
- validators usable by the model;
- artifacts persist correctly;
- render outputs usable;
- no hidden integration defect.

Do not use two-job smoke to declare model routing statistically superior.

## 24.4 Pre-release strategy-format falsification

Because strategy structure affects core stage contracts, E-01 is the highest-value small format test.

Two representative jobs, same routing, compare:

- canonical stable-label Markdown;
- canonical structured JSON + generated Markdown view.

Measure:

- validator/format repair burden;
- Terra writing coherence;
- generic field-filling tendency;
- final Sol material strategy-change rate;
- final human quality;
- human inspectability.

P0.9 default remains JSON unless this test exposes a material quality/regression signal.

## 24.5 Personality test

Can occur before or after the first baseline pilot depending deadlines because personality is OFF by default and fully reversible.

Use 2-3 jobs paired OFF/ON.

Do not simultaneously change strategy format or context prep.

## 24.6 Luna prep test

Run only after deterministic index exists.

Compare:

```text
baseline = deterministic index only
variant  = same + Luna job-local prep
```

Do not combine with personality ON during first Luna test.

## 24.7 Eight-job product pilot

Initial clean baseline preference:

```text
personality = OFF
context_prep = OFF
strategy = selected core format
```

Unless a pre-pilot test has already produced an unusually clear win and user consciously chooses to include it.

The pilot is an observational product baseline, not a routing RCT.

## 24.8 Small-n Top80

**P081-HARDENED**

For `n=8`:

```text
bottom_k = max(1, floor(0.20*n + 0.5)) = 2
top_k = 6
```

Report:

- median;
- mean all 8;
- mean top 6;
- sensitivity mean top 7;
- `Q_happy` using top 6;
- individual job scores.

Do not hide the discrete sensitivity behind one decimal metric.

## 24.9 Human quality scoring

Recommended 1-10 overall score plus a few optional dimensions when decision-relevant:

- employer relevance;
- persuasion;
- naturalness/authenticity;
- evidence credibility;
- need for human rewrite.

Avoid making the user fill a giant rubric for every job.

Self-rating repeatability is expected around 7/10, so small score differences should not drive architecture changes.

## 24.10 First-batch calibration replaces stale historical anchors

Historical applications and interview conversion were explicitly judged incomparable/outdated.

Therefore:

- do not calibrate P0.9 against old package scores as if they were controlled baselines;
- use first-batch feedback to identify examples of strong/medium/weak current packages;
- update `PERSUASION_CALIBRATION.md` from recent comparable evidence only.

## 24.11 Review calibration

Compare Stage 3 status to human experience:

- READY but low human score => potential overconfidence;
- CHECK requiring major rewrite => CHECK boundary too permissive;
- RERUN that human fixes in 2 minutes => RERUN too aggressive.

A separate reviewer stage remains **DEFERRED**. Activation trigger:

> systematic Stage-3 overconfidence: materially many READY packages receive poor human quality or require major hidden repair.

## 24.12 Cross-cluster convergence check

**P081-HARDENED**

Human spot-check after pilot/batch:

- repeated openings;
- repeated identity phrasing;
- evidence reuse without role-specific reason;
- generic motivation templates;
- semantically identical packages for materially different jobs.

Do not build a 5-gram/similarity engine unless actual observed convergence makes the human spot-check insufficient.

## 24.13 Run-level cost logging

Log model usage at the unit where it actually occurs: chat/stage/run, not fabricated per-job allocations unless clearly estimated.

Suggested `PILOT_RUN_LOG.csv`:

```text
run_id
cluster_id
stage
model
effort
jobs_attempted
jobs_completed
prompts
credits_or_cost_if_available
wall_time_if_available
notes
```

Model cost is fourth in the current priority hierarchy, so logging should not itself become operational burden.

---

# 25. Implementation plan - risk-ordered, not document-ordered

## 25.1 Principle

Do not build every specification object before seeing one real document.

Implementation order follows the earliest point at which a wrong assumption can invalidate expensive downstream work.

## Wave 0 - freeze this architecture and clean runtime authority

Deliver:

- adopted P0.9 spec;
- precedence statement;
- current source list;
- explicit exclusions of historical P0.8/P0.8.1 proposals not selected;
- minimal settings defaults.

Exit:

- builder can identify exactly which document wins every architecture conflict.

## Wave 1 - template and environment spike

Before finalizer architecture becomes expensive:

- inspect CV/application masters;
- verify field map feasibility;
- verify target Windows rendering/conversion;
- verify fonts/locale;
- verify header/contact parseability concern;
- verify sparse/normal/dense sample outputs.

Exit:

- rendering approach selected with empirical evidence.

## Wave 2 - deterministic contracts and frozen run

Implement:

- batch inventory parser;
- run manifest/schema;
- safe file ingestion;
- vacancy normalization;
- deterministic evidence index;
- derived job context;
- static invalidation reporting;
- expected-set reconciliation.

Exit:

- a frozen run can be created/reconciled without models.

## Wave 3 - one-job deterministic vertical slice

Implement:

- package schemas;
- template merge;
- finalizer;
- output transaction;
- derived status/review queue;
- target render validation.

Use synthetic valid/invalid artifacts.

Exit:

- one job goes deterministically from frozen identity to delivered DOCX/PDF.

## Wave 4 - strategy and stage validators

Implement:

- `strategy.json` schema;
- generated `strategy.md`;
- draft/final/review schemas;
- validator error model;
- same-chat repair instructions;
- evidence-ref synchronization checks.

Run cheap E-01 if desired before prompt fixtures harden around strategy format.

Exit:

- stage artifacts have stable contracts.

## Wave 5 - semantic stage instructions

Write/test:

- Stage 1 vacancy-first decision architecture;
- Stage 2 native writer;
- Stage 3 vacancy-first elastic reconstruction/review;
- RERUN prompt;
- protocol-vs-boundary labels.

No experimental personality/Luna dependency required.

## Wave 6 - multi-job/cluster mechanics

Implement:

- human cluster/sequence handling;
- one-job transaction sequencing;
- artifact reconciliation on continuation;
- failure/partial-success behavior;
- cross-job write-boundary checks.

No model-generated cluster plan.

## Wave 7 - two-job live smoke

Run real Sol/Terra/Sol.

Patch only observed integration defects.

Do not redesign from speculation after smoke unless a load-bearing assumption fails.

## Wave 8 - baseline eight-job pilot

Run clean core baseline.

Collect quality, handling and calibration metrics.

## Wave 9 - optional quality experiments

Run personality and Luna tests when their expected decision value exceeds deadline/opportunity cost.

Do not block first submissions merely because an optional module has not been tested.

## Wave 10 - production batch

Process remaining conforming jobs.

Use targeted RERUN/exception handling for tail cases.

## Wave 11 - post-batch learning

Update only from observed bottlenecks:

- writing calibration;
- cluster size;
- personality default if evidence exists;
- context prep default if evidence exists;
- review boundary;
- template tuning;
- source-maintenance needs.

One material variable at a time where causal attribution matters.

---

# 26. Acceptance criteria

## 26.1 Architecture acceptance

- one unambiguous product boundary;
- one factual authority layer;
- one frozen run manifest;
- one current strategy/draft/final/review artifact per job;
- explicit derived/non-authoritative status for convenience views;
- no unresolved core channel branch;
- no model-generated cluster state required;
- no hidden semantic orchestration.

## 26.2 Ingest acceptance

- duplicate job IDs rejected;
- missing vacancy rejected;
- unsafe path rejected;
- original vacancy hash recorded;
- every core job appears exactly once in frozen manifest;
- every core job assigned cluster/sequence;
- evidence index regenerated deterministically when source truth changes;
- frozen manifest validates.

## 26.3 Strategy acceptance

- schema valid;
- correct job/run identity;
- hypothesis/non-authority fields present;
- elasticity ELASTIC;
- requirement map present for material requirements;
- evidence refs resolvable;
- counterfactual reserve present unless explicitly `NOT_USEFUL` with reason;
- no factual claim depends solely on personality/context prep;
- human view generated deterministically.

## 26.4 Draft acceptance

- schema valid;
- complete dynamic CV zones according to contract;
- employment override semantics deterministic;
- application text present;
- evidence refs resolvable;
- no placeholders;
- no wrong job identity.

## 26.5 Final acceptance

- final package schema valid;
- review schema valid;
- evidence refs synchronized to final content;
- unsupported known claims repaired before save;
- material strategy changes logged;
- status uses repair-scope semantics;
- validator exit 0.

## 26.6 Rendering acceptance

- correct source map;
- all expected DOCX created;
- all required PDFs created/openable;
- no unresolved template markers;
- no broken glyphs/clipping in fixture/representative visual QA;
- job transaction does not corrupt prior valid outputs;
- targeted rerender works.

## 26.7 Runtime acceptance

- continuation reconciles artifacts rather than trusting stale progress;
- one failed job does not delete successful outputs;
- finalizer enumerates frozen expected jobs;
- changed frozen inputs produce stale report;
- no automatic model call is made by deterministic code;
- human can determine next action from generated review queue.

## 26.8 Product pilot acceptance

Before full batch, evidence should show:

- packages are genuinely job-specific;
- human time roughly compatible with 10-20 min submitted-package target;
- no systemic truth inflation;
- Stage 3 materially repairs weak drafts when needed;
- READY/CHECK/RERUN roughly correlates with human repair scope;
- rendering is stable;
- no severe early-to-late cluster degradation;
- no unacceptable cross-job convergence.

There is no single numeric pass threshold that substitutes for judgment.

---

# 27. Explicit do-not-build firewall

Unless activated by observed evidence, P0.9 does **not** include:

- vector database;
- embeddings/RAG platform;
- semantic cache;
- persistent candidate role/archetype memory;
- cross-job personality memory;
- multi-agent debate;
- LLM-as-judge standard stage;
- model router infrastructure;
- automatic best-of-N package generation;
- semantic auto-repair orchestrator;
- hidden retries;
- database/state machine/event sourcing;
- broad claim/provenance graph;
- automatic dependency-execution engine;
- large similarity/n-gram gate;
- typography auto-fit engine;
- persistent LibreOffice daemon;
- automatic employer research in production;
- automatic job search;
- automatic application submission;
- automatic employer contact;
- numeric fit probability used for treatment;
- generalized release-governance platform;
- per-job copies of all factual authorities;
- separate blind reviewer stage by default;
- standard RERUN folder/stage for every job;
- `_DONE.md` completion markers;
- rigid exact Python-file count;
- model-compiled settings/instruction cache;
- global Luna filtering funnel;
- relevance-based source exclusion;
- personality-driven factual claims;
- full personality profile to every model stage;
- mandatory microvariation for Priority A jobs;
- model-generated clustering preflight as a release requirement.

---

# 28. Failure-mode register and response policy

| Failure mode | Detection | Response | Do not do |
|---|---|---|---|
| Wrong job identity | deterministic validator | fail artifact, repair same chat | silently continue |
| Unknown evidence ref | deterministic validator | repair/refetch source | accept because prose looks good |
| Unsupported semantic claim | Stage 3/human | repair before final save; log upstream repair | leave claim + CHECK |
| Strategy too rigid/weak | Stage 3 | reconstruct; log material change | protect strategy because schema-valid |
| Context prep omits key evidence | source escape / outside-prep signal | open original source; continue | treat prep as permission boundary |
| Personality feels performative | Stage 3/human | suppress; possibly keep feature OFF | force selected facet into prose |
| Validator fails once/twice | stage protocol | repair/revalidate | code-trigger model retry |
| Validator fails third time | deterministic state | FAILED for job/stage, continue others | mark completed |
| Render fails | finalizer | preserve prior valid outputs; retry deterministic render when fixed | invalidate unrelated jobs |
| Cluster late-job quality decline | pilot | reduce cluster size/order or context | build complex memory first |
| Cross-job phrase convergence | human spot-check | adjust stage prompts/order; only later automate if recurrent | immediately build similarity engine |
| READY overconfidence | human calibration | tighten Stage 3 review; consider reviewer-stage activation if systematic | add judge from one anecdote |
| Run source changed after freeze | hash comparison | stale report; human chooses new/amended run | silently mix versions |
| Rare non-core vacancy | ingest exception class | separate/manual extension | add branch to core by default |
| Portal hard limit exceeded | portal validator | repair exact answer | allow tolerance |
| Model follows vacancy instruction-as-command | prompt/security protocol + human | ignore data-plane command; continue content analysis | treat vacancy as control plane |

---

# 29. Why this P0.9 is simpler than P0.8.1 while being more capable

The integrated architecture removes entire surfaces:

- no core portal branch;
- no core channel enum;
- no model-generated cluster plan;
- no differentiated A/B treatment;
- no separate per-stage progress truth;
- no personality requirement in baseline;
- no Luna requirement in baseline;
- no backward-compatible old tree;
- no mandatory clustering preflight;
- no historical application calibration dependency.

At the same time it adds high-leverage capability:

- stable deterministic evidence addressing;
- finer static invalidation reporting;
- job-centric transaction model;
- structured strategy with explicit epistemic status;
- counterfactual reserve;
- observable strategy reconstruction;
- observable upstream truth repair;
- optional personality resonance;
- optional bounded Luna prep;
- stronger source-escape/context governance;
- better experimental attribution;
- fresh runtime aligned to actual current user constraints.

This is the defining P0.9 improvement pattern:

> **remove generalized machinery, then spend the recovered complexity budget on quality-critical information interfaces and falsifiable optional improvements.**


---

# 30. P0.8.1 -> P0.9 document graph and unique contribution analysis

This section is intentionally source-centric. It explains what each P0.8.1/P0.9 artifact contributes that cannot safely be replaced by another artifact.

## 30.1 `jobbsok_26_overordnet_systemanalyse.html`

### Role

Early system-level post-P0.8 critique.

### Unique contribution

It is important primarily as a **conservative control voice**. Its strongest recommendation was broadly:

- P0.8 is fundamentally sound;
- freeze rather than endlessly redesign;
- migrate surgically;
- validate with real implementation/pilot evidence.

### How P0.9 uses it

P0.9 does not adopt its conservatism as a prohibition on fresh architecture, because the user later explicitly permitted/preferred a fresh P0.9 runtime. It retains the deeper stopping principle:

> once load-bearing contracts are coherent, implementation evidence outranks another speculative design loop.

### Information not carried forward

Any implicit preference for preserving old runtime shape is superseded by later user permission for a fresh job-centric design.

---

## 30.2 `Jobbsok_26_P0.8_kritisk_review_og_forbedringsbrainstorm_claude.md`

### Role

Independent critical review of final P0.8.

### Unique contribution

Strongest at identifying **contract/governance ambiguities**, including:

- dynamic CV override ambiguity;
- evidence reference semantics;
- RERUN route;
- review/action boundary;
- state/provenance gaps;
- implementation sequencing risks.

### How P0.9 uses it

Its direct contract findings survive through the addendum/consolidated review when they still apply.

P0.9 does **not** use it as independent normative authority; later reconciliation is stronger.

---

## 30.3 `Jobbsok_26_P0.8_kritisk_review_og_forbedringsbrainstorm_Gemini.md`

### Role

Second independent review with more implementation hypotheses.

### Unique contribution

Valuable as a divergent stress test. It raised issues such as:

- Markdown/JSON handoff risk;
- content/structure ambiguity;
- render pipeline questions;
- READY/CHECK/RERUN concerns;
- convergence/phrase drift concerns.

### How P0.9 uses it

Only conflict-resolved signal survives. Several recommendations were later rejected as stale, excessive or solving the wrong problem.

This is a good example of why P0.9 uses **problem preservation, proposal re-evaluation**:

> retain the failure mode even when the first proposed fix is discarded.

---

## 30.4 `Jobbsok_26_P0.8_addendum_cross_model_consolidation.md`

### Role

Adjudication layer across the independent reviews.

### Unique contribution

It converts divergent review output into a conflict-resolved set of concrete improvements, particularly:

- full replacement semantics for employment bullets;
- one current modality for evidence refs;
- explicit RERUN route;
- repair-scope review semantics;
- rejection of several overengineered fixes.

### How P0.9 uses it

This is the main reason some P0.8.1 mechanisms are trustworthy as hardening rather than mere reviewer opinion.

P0.9 retains the conflict-resolution method and most low-cost invariant repairs.

---

## 30.5 `deep-research-report (14).md` - P0.8 external evidence review

### Role

External evidence check on architecture assumptions.

### Unique contribution

It tests project reasoning against outside facts and highlights which assumptions should be local-test dependent rather than architecture dogma.

Notable effects:

- reinforces staged/manual architecture as reasonable;
- increases caution about Word/LibreOffice/ATS assumptions;
- argues for local template/render tests;
- reduces confidence in categorical claims based on generic document advice.

### How P0.9 uses it

As **evidence, not project authority**.

Where direct P0.7 empirical inspection conflicts with generic template caution, the direct artifact evidence wins for that specific master.

---

## 30.6 `Jobbsok_26_P0.8_consolidated_preimplementation_review.md`

### Role

Strongest P0.8.1 synthesis and hardening source.

### Unique contribution

It is the most mature answer to:

> If we implemented P0.8 tomorrow, where would the builder otherwise have to guess?

Its durable contribution is the interface-hardening corpus:

- canonical intake;
- freeze;
- expected set;
- cluster/state coherence;
- deterministic/semantic/quality separation;
- CV merge semantics;
- final evidence refs;
- validator-before-completion;
- bounded same-stage repair concept precursor;
- review/RERUN semantics;
- partial success;
- rendering transaction thinking;
- pilot metric discipline;
- human total-time measurement;
- do-not-build firewall.

### Critical status caveat

It explicitly says `NON_NORMATIVE_UNTIL_ADOPTED`.

P0.9 therefore does not pretend P0.8.1 was a deployed release. Instead it selects its strongest surviving mechanisms by design logic.

---

## 30.7 `Brainstorm_Brief.md`

### Role

Broad P0.9 divergence artifact.

### Unique contribution

It deliberately expands design space rather than picking an architecture.

Its highest-value contributions are **new problem framings**, especially:

- authenticity/personality as a controlled quality lever;
- portal detachment and invariant product surface;
- job-centric runtime;
- context-preparation ideas;
- source escape;
- counterfactual reserve;
- strategy compression;
- model-cost versus context-attention distinction;
- richer thinking about artifacts, state, and optional Luna support;
- interactions among quality mechanisms.

### What not to do with it

Do not implement its entire idea inventory.

Its own epistemic contract is exploratory. P0.9 uses the Brainstorm Brief as a **search space**, not a requirements document.

---

## 30.8 `brainstorm_review.md`

### Role

The key bounded optimization/reconciliation layer between P0.8.1 and the Brainstorm Brief.

### Unique contribution

This is arguably the single most analytically valuable P0.9 architecture document before the later user questionnaire because it:

- examines P0.8.1 independently before adopting brainstorm framing;
- normalizes colliding IDs;
- prunes 100+ mechanisms;
- identifies conditional dependencies;
- introduces DC-1..DC-7;
- introduces N-01..N-06;
- identifies cross-variable interactions X-1..X-6;
- constructs bundles K-0..K-6;
- distinguishes optimized control from historical control;
- identifies cheap experiments E-01/E-02/E-05/E-12;
- proves that "Luna versus nothing" is the wrong experiment once deterministic indexing exists.

### Unique non-linear insights retained in P0.9

- CR-04 cluster-plan hardening is conditional on retaining the cluster-plan function.
- portal contract cost is concentrated/severable.
- strategy artifact problem is multi-consumer authority, not merely syntax.
- freeze granularity should be designed around invalidation blast radius.
- clean baseline and causal experiment are different instruments.
- structured strategy can create authority inflation.
- context prep + tight elasticity is a hazardous interaction.

### How P0.9 differs from it

`brainstorm_review.md` intentionally selected **no bundle**. This magnum opus performs that missing bundle-selection/convergence step.

---

## 30.9 `P0.9_prep_package.md`

### Role

Pre-architecture uncertainty-reduction plan v1.

### Unique contribution

It turns a large abstract option space into a small set of **architecture-blocking unknowns**:

- actual batch/product boundary;
- human load;
- experiment feasibility;
- template/render constraints;
- reuse/generality budget.

It also identifies the one-row-per-vacancy inventory as unusually high-value.

### How P0.9 uses it

This motivates the human batch inventory as a first-class pre-run artifact and prevents architecture decisions based on guessed portal/public-sector prevalence.

---

## 30.10 `P0.9_prep_package(1).md`

### Role

Substantive v2 of the prep package, not a duplicate.

### Unique contribution

The research section was materially upgraded into a more coherent deep-research contract.

This matters historically because it demonstrates an important project method:

> make external research answer decisions that can actually change architecture, rather than collect general background.

### What is superseded

The questionnaire's pre-filled defaults are not current truth. Later actual user responses in the integration summary override them.

---

## 30.11 `claude_P0.9_architecture_prep_chat_integration_summary.md`

### Role

Retrospective reconstruction of the prep/chat workstream.

### Unique contribution

It is useful for **chronology and provenance**, especially distinguishing:

- P0.8 adopted state;
- P0.9 decision basis;
- research not-yet-executed versus later completed work.

### How P0.9 uses it

As historical alignment evidence, not as a primary architecture authority when stronger source artifacts exist.

---

## 30.12 `Optimizing P0.9 Architecture_integration_summary.md`

### Role

Retrospective reconstruction of the parallel architecture-optimization chat.

### Unique contribution

Shows that P0.9 was explicitly designed as an **information-acquisition-before-architecture** process:

- identify architecture-sensitive uncertainty;
- research cheap external unknowns;
- build missing local context such as Personality;
- then run final architecture selection.

### How P0.9 uses it

It explains why the later P0.9 corpus should not be misread as a final spec. The documents were intentionally preparatory.

---

## 30.13 `Norwegian application-package research_integration_summary.md`

### Role

Research-launch/chat reconstruction.

### Unique contribution

Defines the exact architecture-sensitive external questions around:

- Norwegian application channels;
- portal behavior;
- machine readability;
- public-sector requirements;
- Word/LibreOffice rendering.

### Critical boundary

The integration summary itself does **not** contain the substantive final research findings. The questions must not be promoted to conclusions.

This prevents a subtle provenance error.

---

## 30.14 P0.9 External Evidence Report (`compass_artifact...md`)

### Role

Completed external research.

### Unique contribution

It adds independent evidence on:

- OpenAI/long-context behavior;
- limitations of assuming all uploaded context is equally active;
- long-context/lost-in-middle risks;
- JSON structured-output limitations outside API mode;
- Codex/local validator feasibility;
- Norwegian public-sector qualification framing;
- application-platform variability;
- Word/LibreOffice constraints;
- prompt-injection/security;
- need for local rendering/portal/template tests.

### Important limitation

The research model did not have the complete project corpus needed to resolve most DC/N choices.

Therefore it can constrain facts and local-test requirements, but **cannot select P0.9 architecture by itself**.

### Integrated effect

The report strengthens:

- deterministic index as low-risk control;
- source escape;
- original-vacancy-first reading;
- local validator repair;
- local rendering tests;
- reluctance to use weak-model preprocessing as an authority/filter.

It does not establish that Luna prep improves final quality.

---

## 30.15 `Personality.md`

### Role

Canonical high-density interpretive source.

### Unique contribution

It transforms the personality idea from vague "authenticity" into a rich, inspectable model of:

- cognitive/decision style;
- communication preferences;
- motivation;
- execution pattern;
- failure modes;
- collaboration behavior;
- calibration boundaries.

### Architectural implication

Personality becomes a **testable real input**, not a speculative feature description.

But because it is interpretive and partly synthesized, it remains separate from factual candidate authority.

---

## 30.16 `Personality_P0.9_Framework_Context.md`

### Role

Assistant-generated runtime adaptation of the personality source.

### Unique contribution

It demonstrates a plausible bounded interface:

- toggle activation;
- 0-3 facet selection;
- evidence-bound desired recruiter read;
- misread/prevention/ceiling;
- distilled Terra handoff;
- final Sol suppression authority.

### What P0.9 adopts

The **interface pattern**, not necessarily all 20 facet IDs or every internal taxonomy choice.

This distinction avoids turning one assistant-generated derivative into a hidden user-ratified ontology.

---

## 30.17 `Jobbsok_26_integration_summary.md`

### Role

Latest and highest-authority P0.9 historical state reconstruction in the supplied corpus.

### Unique contribution

It contains the **latest actual user answers/corrections**, which materially change earlier prep assumptions:

- quality > human effort > implementation speed > model cost > reversibility;
- first-batch urgency 1-4 weeks;
- ~30 strong of ~40 preferred;
- 10-20 human minutes/package;
- 20-25 prompts normal, no absolute ceiling;
- fresh P0.9 runtime preferred/allowed;
- no old tree compatibility;
- authorities CURRENT;
- final Sol ELASTIC;
- personality optional but default unresolved;
- local validators allowed;
- rare nonconforming jobs may be handled separately;
- historical application/interview baselines are incomparable;
- final P0.9 architecture still had not been selected.

### Authority role

When this document conflicts with pre-filled questionnaire assumptions, the later actual user answers win.

---

# 31. Mechanism-level integration: what survives, transforms or disappears

## 31.1 P0.8.1 hardening disposition in final P0.9

| P0.8.1 mechanism | P0.9 disposition | Reason |
|---|---|---|
| CR-01 canonical machine job intake | **PRESERVE/TRANSFORM** | survives as human inventory -> frozen run manifest |
| CR-02 normalized deliverable state | **CONTRACT DELETED from core** | core outputs invariant CV+application; portal detached |
| CR-03 freeze/context snapshot | **PRESERVE/CONSOLIDATE** | one run manifest becomes freeze object |
| CR-04 cluster-plan schema | **DELETE** | no model-generated core cluster plan; cluster/order frozen in intake |
| CR-05 progress follows plan | **TRANSFORM** | status derived/reconciled from manifest + artifacts |
| CR-06 expected-job reconciliation | **PRESERVE** | essential partial-success invariant |
| CR-07 mechanical/semantic/soft split | **PRESERVE** | foundational validation model |
| CR-08 portal exact hard limits | **MOVE DOWNSTREAM** | detached portal module retains exact limits |
| CR-09 package-template source map | **PRESERVE** | still essential rendering contract |
| CR-10 blind/independent = read-order protocol | **PRESERVE/GENERALIZE** | expanded into protocol-vs-boundary doctrine |
| CR-11 employment override full replacement | **PRESERVE** | critical deterministic CV semantics |
| CR-12 final evidence refs sync | **PRESERVE/EXPAND** | now uses deterministic evidence index |
| CR-13 review by repair scope | **PRESERVE** | READY/CHECK/RERUN semantic core |
| CR-14 RERUN one-job Sol route | **PRESERVE** | unchanged, separate manual path |
| CR-15 run-level credit ledger | **PRESERVE LIGHTLY** | useful but model cost lower priority |
| CR-16 small-n Top80 | **PRESERVE** | correct pilot interpretation |
| CR-17 human total minutes | **PRESERVE/PRIORITIZE** | now tied to explicit 10-20 min target |
| CR-18 A/B prediction-treatment confound | **RESOLVE BY DELETION** | no differentiated treatment; optional research prediction only |
| CR-19 one LO invocation/job | **REFINE** | job transaction preserved; per-document results independently verified; invocation batching environment-tested |
| CR-20 vertical slice first | **PRESERVE** | implementation-risk control |
| CR-21 two operator CLIs, internal modules free | **PRESERVE SPIRIT** | simple operator surface, internal correctness allowed |
| CR-22 human cross-cluster phrase spot-check | **PRESERVE** | low-cost convergence control |
| CR-23 validator before complete | **PRESERVE + N-04** | exact repair behavior defined |
| CR-24 remove mandatory Terra clustering preflight | **PRESERVE** | human clustering selected |
| typography auto-fit | **DEFER** | no observed need yet |
| n-gram similarity engine | **DEFER/REJECT** | human spot-check first |
| LLM-as-judge stage | **DEFER/REJECT** | activation only if Stage 3 systematic overconfidence |

## 31.2 P0.9 DC cluster resolution

| Cluster | Selected final option | Why |
|---|---|---|
| DC-1 Product | 1a | largest contract deletion; quality-neutral/positive theory; exceptions allowed |
| DC-2 Authenticity | bounded 2c-like implementation, OFF baseline | direct quality theory but high variance; reversible and testable |
| DC-3 Context | 3b baseline; 3c optional test | deterministic index dominates no-navigation; Luna incremental value unknown |
| DC-4 Strategy | 4c | structured decision core + generated human view; compensating anti-authority controls added |
| DC-5 State | 5b refined | job-centric transaction + one manifest + derived views fits fresh runtime |
| DC-6 Priority/order | refined 6c | human-fixed order; no A/B treatment; optional prediction research outside control flow |
| DC-7 Implementation | vertical slice + template spike + staged pilots | strongest convergence across sources |

## 31.3 N-series integration

| Mechanism | P0.9 status | Modification |
|---|---|---|
| N-01 invalidation classes | **CORE, REFINED** | 4 classes expanded to 6 static classes to reduce unnecessary stale scope |
| N-02 evidence outside prep | **DIAGNOSTIC** | active only where prep exists; not employer artifact |
| N-03 deterministic evidence index | **CORE** | promoted from option to baseline shared reference plane |
| N-04 validator failure protocol | **CORE** | unchanged: max 2 repairs, third failure => failed |
| N-05 fact-correction trace | **CORE review telemetry** | retained as upstream claim repair signal |
| N-06 protocol-not-isolation | **CORE doctrine** | generalized to context and security controls |

## 31.4 X-series interaction resolution

| Interaction | P0.9 resolution |
|---|---|
| X-1 spark x mandatory microvariation | microvariation removed; strategy chooses angle, writer expression |
| X-2 Luna prep x tight elasticity | elasticity user-locked ELASTIC; hazard structurally removed |
| X-3 personality x Luna candidates | Luna never generates personality candidates in first release |
| X-4 manifest x dependency invalidation | static invalidation lattice; report-only, no state engine |
| X-5 JSON strategy x Stage-3 reconstruction | hypothesis status + vacancy-first protocol + ELASTIC + change telemetry + E-01 rollback gate |
| X-6 compression x elasticity | counterfactual reserve required to preserve alternate decision basis |

---

# 32. Consolidated user preference and architecture policy register

This section distinguishes current user constraints from synthesis choices so future models do not blur them.

## 32.1 User-locked product/quality policy

- Truth, identity and employer usability are hard boundaries.
- Final package quality is the first truth-safe objective.
- Human effort is second.
- Implementation speed/simplicity is third.
- Model cost is fourth.
- Reversibility is fifth.
- Strong-majority quality is preferred over rescuing every tail case.
- Approximately 30 strong packages from ~40 is a valid target shape.
- Rare/nonconforming jobs may be handled separately.
- The framework is personal/reusable for the same candidate, not a general multi-candidate product.

## 32.2 User-locked operation policy

- Jobs normally frozen before production.
- Human time envelope ~5-10 h/week.
- ~10-20 minutes human handling per submitted package is acceptable target.
- Routine between-job confirmation is undesirable.
- Semantic stages are manually initiated distinct model chats.
- One cluster chat may process jobs sequentially.
- Local repository/files are runtime authority.
- Deterministic validators may run in-model-session with repair/revalidation.
- No automatic submission.
- Candidate factual authorities immutable during production.
- All three factual authorities current.
- Fresh P0.9 runtime preferred/allowed.
- No old directory compatibility requirement.
- Legacy assets must earn reuse through review.
- Final Sol elasticity = ELASTIC.
- Routine prompt budget ~20-25, no absolute ceiling with demonstrated quality value.

## 32.3 User-locked/permission product simplifications

- invariant CV+application core is allowed;
- detached portal is allowed;
- nb-NO-only first release is allowed;
- four-zone dynamic CV surface is allowed;
- job-centric runtime is allowed.

This magnum opus converts those permissions into `SYNTHESIS-LOCK` choices because they jointly dominate the remaining alternatives under the current objective function.

## 32.4 Personality policy

User-locked:

- feature optional;
- controlled via `SETTINGS.md`;
- source is composite/self-synthesized, not factual candidate authority.

Not historically user-locked before this synthesis:

- default OFF;
- exact facet count;
- exact 0-3 runtime selection;
- exact handoff schema.

This spec chooses default OFF + bounded selection because it best preserves baseline quality attribution and is cheap to reverse.

## 32.5 Evaluation policy

User-locked/current:

- old application anchors are not comparable;
- old interview conversion is not comparable;
- first-batch feedback is the relevant calibration source;
- self-rating consistency expected around 7/10;
- up to about 3-4 small, high-value tests acceptable;
- exact blinding method unresolved.

---

# 33. End-to-end production runbook

## 33.1 Pre-run

Human:

1. collects vacancies;
2. decides conforming core vs exceptions;
3. assigns `job_id`;
4. assigns cluster and sequence;
5. records deadline/user priority;
6. confirms candidate authorities current;
7. sets `personality` and `context_prep` toggles;
8. starts ingest.

## 33.2 Ingest

System:

1. validates inventory;
2. validates/copies original vacancies;
3. hashes all frozen assets;
4. builds/reuses deterministic evidence index;
5. freezes `run_manifest.json`;
6. generates job views;
7. reports exceptions/warnings;
8. refuses production on identity/set-critical error.

## 33.3 Stage 1 cluster chat

For each job in frozen cluster order:

1. vacancy first;
2. provisional employer-decision model;
3. source/evidence exploration;
4. optional personality after evidence;
5. write strategy;
6. validate;
7. repair <=2;
8. persist;
9. continue.

At cluster end, reconcile completed/failed artifacts.

## 33.4 Stage 2 cluster chat

For each valid strategy:

1. open vacancy + strategy + required writing context;
2. reopen evidence as needed;
3. write full dynamic CV/application draft package;
4. record bounded writer delta only if material;
5. validate;
6. repair <=2;
7. persist;
8. continue.

## 33.5 Stage 3 cluster chat

For each valid draft:

1. vacancy-first fresh provisional view;
2. inspect relevant sources;
3. inspect strategy/draft;
4. reconstruct freely within truth;
5. synchronize final evidence refs;
6. record strategy change / upstream claim repair;
7. set READY/CHECK/RERUN by remaining repair scope;
8. validate final+review;
9. repair <=2;
10. persist;
11. continue.

## 33.6 Finalization

System:

1. enumerates expected jobs from run manifest;
2. validates current semantic artifacts;
3. merges baseline/templates;
4. converts documents;
5. verifies outputs;
6. creates derived run status/review queue;
7. preserves partial success.

## 33.7 Human review

Human:

- reviews READY first by deadline/priority;
- handles CHECK locally;
- chooses whether RERUN is worth the cost;
- may drop weak/low-value tail;
- manually submits approved package;
- captures portal questions only where needed and uses detached workflow.

## 33.8 RERUN

Human manually opens one-job Sol RERUN chat.

Current final/review are archived to history before new validated result becomes current.

## 33.9 Post-run

System/human:

- record package scores/time where useful;
- inspect convergence;
- calibrate READY/CHECK/RERUN;
- update writing calibration from comparable first-batch evidence;
- maintain candidate sources only outside frozen run;
- choose one observed bottleneck for next iteration.

---

# 34. Detailed P0.9 semantic invariants

The following should be testable as architecture invariants even when exact filenames change.

## 34.1 Truth invariants

- No model-authored artifact can become candidate factual authority.
- Personality is never fact authority.
- Context prep is never fact authority.
- Final package evidence refs must point to frozen sources.
- Unsupported known claim is repaired before current final save.
- Final Sol may change strategy but not source reality.

## 34.2 State invariants

- Run expected set originates from frozen manifest.
- Job appears exactly once as core/exception in run identity.
- Derived status cannot make a missing expected job disappear.
- Current final/review pair is unique.
- Rerun preserves replaced current artifacts in history.
- Frozen input changes produce explicit staleness.

## 34.3 Execution invariants

- No deterministic script invokes semantic model calls automatically.
- Model stage validates before completion.
- Same-chat repair bounded at two attempts.
- One job failure does not abort independent successful jobs.
- RERUN is manual and one-job.

## 34.4 Quality invariants

- Stage 3 is allowed to reconstruct materially.
- No strategy format may become a de facto constraint on final quality.
- Quality targets remain soft unless employer imposed.
- Human remains final quality/fact authority before submission.
- Weak tail may be selectively abandoned.

## 34.5 Context invariants

- Original vacancy is always reopenable.
- Candidate primary sources remain reopenable.
- Evidence index does not relevance-filter.
- Optional prep does not permission-filter.
- No summary-of-summary becomes sole grounding for material claim.

## 34.6 Product invariants

- Core normal job = CV + application.
- Core normal language = nb-NO.
- Portal is downstream.
- Dynamic CV surface fixed to four zones in P0.9 v1.
- Exception jobs do not force core branching.

---

# 35. Current empirical parameters versus architecture choices

Not every undecided numeric value is an architecture gap.

## 35.1 Architecture-locked

- three semantic roles;
- core product boundary;
- detached portal;
- job-centric runtime;
- run manifest authority;
- human clustering/order;
- deterministic evidence index;
- strategy hypothesis semantics;
- ELASTIC final writer;
- partial success;
- validator repair protocol;
- personality/Luna optionality;
- no auto submission.

## 35.2 Empirical/configurable parameters

- exact cluster size within practical range;
- exact strategy soft word budget;
- exact personality facet count in canonical source;
- personality ON adoption after test;
- Luna prep ON adoption after test;
- one vs two LibreOffice invocations/job;
- exact page-density warning thresholds;
- exact number of pilot jobs after first 8-job baseline;
- whether pure opportunity prediction is worth logging;
- exact model effort/routing if product capabilities/pricing change.

These should be changed from evidence without calling the framework "P0.10" unless the architecture contract changes.

---

# 36. What this improves versus the previous derived target specification

The earlier derived target correctly preserved open forks because the historical corpus had not architecture-locked P0.9. This magnum opus goes further because the user explicitly requested a final integrated design.

Material improvements:

1. **Resolves product boundary:** portal detached, nb-NO core, exceptions separate.
2. **Resolves runtime tree:** job-centric + one frozen manifest.
3. **Deletes cluster-plan contract:** human cluster/order makes it redundant.
4. **Resolves A/B:** no differentiated treatment; no production dependency.
5. **Promotes deterministic evidence index to core**, rather than merely recommending it.
6. **Resolves strategy format to structured JSON + generated MD**, with explicit anti-authority controls.
7. **Introduces orthogonal factual vs strategic authority axes**, clarifying how deterministic contracts coexist with elastic writing.
8. **Refines invalidation from four broad classes to six static scopes** without adding a dependency engine.
9. **Sets personality default OFF while still building the bounded interface**, converting historical ambiguity into a falsifiable optional feature.
10. **Sets Luna context prep OFF and defines the correct deterministic-index control condition.**
11. **Moves portal hard limits to the detached module**, deleting core portal contract machinery.
12. **Makes progress regenerable rather than authoritative.**
13. **Refines rendering:** job transaction is normative; one-invocation batching is environment-dependent rather than dogma.
14. **Separates engineering proof, product baseline and causal feature experiments** into three evidence loops.
15. **Defines current runbook, invariants and acceptance criteria** at implementation-ready granularity.
16. **Preserves P0.8.1 hardening selectively** instead of treating the entire non-normative diff as one block.
17. **Records provenance classes** so later models can tell user decisions from this synthesis's architecture selections.

---

# 37. Residual risks after architecture lock

No meaningful architecture eliminates uncertainty. The remaining risks are deliberately converted into local tests or monitoring rather than additional speculative layers.

## 37.1 Strategy formalization risk

Risk: structured strategy increases downstream anchoring.

Mitigation:

- hypothesis fields;
- ELASTIC;
- vacancy-first Stage 3;
- material-strategy-change logging;
- E-01 rollback gate.

## 37.2 Personality quality risk

Risk: subtle artificiality/cringe or retrospective evidence fitting.

Mitigation:

- OFF baseline;
- 0 facets valid;
- evidence anchoring;
- expression ceilings;
- final Sol suppression;
- paired evaluation.

## 37.3 Context-prep anchoring risk

Risk: cheap prep biases stronger models or bloats context.

Mitigation:

- deterministic index baseline;
- OFF default;
- source escape;
- advisory header;
- no relevance exclusion;
- no personality;
- direct paired test.

## 37.4 Cluster context accumulation

Risk: later jobs inherit earlier job framing/phrases.

Mitigation:

- vacancy-first protocol per job;
- one-job transaction;
- human sequence;
- cross-cluster spot-check;
- early/late pilot observation;
- reduce cluster size only if evidence shows degradation.

## 37.5 Rendering/environment risk

Risk: headless LO, fonts, Windows paths or master structure behave differently on target machine.

Mitigation: mandatory template/environment spike before broad build.

## 37.6 Human review calibration risk

Risk: READY self-assessment is overconfident.

Mitigation: calibrate against human; activate separate reviewer-stage research only on systematic signal.

## 37.7 Vacancy mix mismatch

Risk: real batch contains more non-core channel/language forms than expected.

Mitigation: inventory before run; exception classification; only revise core if exception frequency makes separate handling genuinely more costly than architecture expansion.

---

# 38. Formal adoption checklist

If this document is adopted as P0.9 architecture authority, the following historical ambiguities are considered closed for P0.9 v1:

- [ ] Core = tailored CV + application.
- [ ] Portal detached downstream.
- [ ] nb-NO only core v1.
- [ ] Rare nonconforming jobs use exception path.
- [ ] Dynamic CV surface = headline/profile/competencies/employment bullets.
- [ ] Fresh job-centric runtime.
- [ ] Frozen `run_manifest.json` is canonical run snapshot.
- [ ] No separate core model-generated `cluster_plan.json`.
- [ ] Human assigns cluster/order.
- [ ] No differentiated A/B treatment.
- [ ] Deterministic evidence index is baseline.
- [ ] Canonical strategy is JSON; Markdown is generated view.
- [ ] Strategy explicitly non-authoritative/hypothesis; final Sol ELASTIC.
- [ ] Personality module exists but default OFF until validated.
- [ ] Luna context prep optional default OFF.
- [ ] Stage validators support max two same-chat repairs.
- [ ] RERUN = manual one-job Sol route.
- [ ] Rendering is per-job transaction with independent output verification.
- [ ] Human owns final approval/submission.
- [ ] Pilot separates engineering proof, baseline observation and causal feature tests.

If the user later changes any checked item, that later explicit decision supersedes this artifact only for the affected granular contract and its dependencies.

---

# 39. Condensed normative P0.9 contract

For a future builder or model that cannot ingest the entire analysis, this section is the minimal authoritative reading of the selected design.

## 39.1 Product

Build a fresh local one-candidate Jobbsok_26 P0.9 system for repeat use.

Normal core job produces a tailored Norwegian Bokmal CV and application letter. Portal/form answers are detached downstream. Non-Norwegian/CV-only/portal-only/other rare jobs are exception paths.

Optimize truth-safe final package quality first, human work second, implementation speed third, model cost fourth, reversibility fifth. Prefer ~30 strong packages from ~40 over uniform rescue of the weakest tail.

## 39.2 Truth

Only `Work_experience.md`, `Education.md` and `Other_high_value_information.md` are candidate factual authorities. Original vacancy is employer authority. Freeze their hashes per run. Personality, index, strategy, drafts and prior packages are non-authoritative.

Generate a deterministic evidence index with stable source/heading IDs and no relevance filtering. Final package evidence refs must match actual final content.

## 39.3 Run/state

Human creates one vacancy inventory with `job_id`, vacancy path, cluster, sequence, deadline/priority and exception class.

Ingest creates one frozen `run_manifest.json`, safe source copies/refs, evidence index and derived job views.

Use a job-centric runtime. `run_status.json`, review queue and human `strategy.md` are derived views, not authority. Expected job set comes from manifest, never directory discovery.

Static stale scopes: SOURCE_TRUTH, STRATEGY_POLICY, WRITER_POLICY, FINAL_POLICY, RENDER_ASSET, SCHEMA_VALIDATION. Report staleness; never auto-run semantic stages.

## 39.4 Semantic route

Manual cluster chats:

1. Sol Max Stage 1 decision architecture.
2. Terra Max Stage 2 native package writer.
3. Sol Max Stage 3 elastic final writer + review.

One job is fully written/validated/persisted before the next job in the chat.

Human clustering/order. No model-generated core cluster plan. No A/B differentiated treatment.

## 39.5 Strategy

Canonical `strategy.json`; deterministic `strategy.md` view.

Strategy is explicitly `STRATEGY_HYPOTHESIS`, non-factual, non-final, `ELASTIC`, final writer may reconstruct.

Include employer decision model, identity, material requirement map, evidence refs/ceilings/roles, objection/reframe, motivation bridge, CV/application direction, optional personality resonance, gaps/risks, and one counterfactual reserve.

Target ~400-1000 substantive words equivalent, soft max ~1200.

## 39.6 Stage 2

Produce one complete `draft_package.json` with four dynamic CV zones and application text.

Employment bullet override = full replacement for that employment.

Write natural, evidence-backed, employer-specific Bokmal. Source-escape allowed.

## 39.7 Stage 3

Read vacancy first, then relevant sources, then strategy/draft. Reconstruct freely within truth.

Synchronize final evidence refs. Log material strategy change and upstream claim repair. Output `final_package.json` + `review.json`.

READY/CHECK/RERUN reflects remaining repair scope, not numeric quality/confidence.

## 39.8 Validation

Separate deterministic hard, semantic truth hard and soft quality.

Every stage validates before completion.

On validator failure: repair in same chat, revalidate, maximum two repairs; third failure => FAILED for that job/stage and continue independent jobs.

No hidden retry/orchestrator.

## 39.9 Personality/context experiments

`SETTINGS.md`:

```text
personality = OFF
context_prep = OFF
```

Personality may be turned ON after paired evidence; if ON Stage 1 selects 0-3 evidence-bound facets and Terra gets distilled guidance only.

Optional Luna prep, if tested, runs against deterministic-index-only control, is advisory/fail-open, cannot filter sources, sees no personality, writes no employer prose and never becomes factual authority.

## 39.10 Rendering

Reuse/adapt legacy masters only after explicit inspection/test. One canonical package-to-template map. Treat job as render transaction; verify each output independently. Use isolated LibreOffice/profile or chosen converter based on target-Windows spike. No persistent converter service. No auto-fit engine without observed need.

## 39.11 Human boundary

Human approves facts/claims/package and submits manually.

Review queue groups READY/CHECK/RERUN/FAILED/EXCEPTION. Human may rerun or drop weak tail. No auto submission or employer contact.

## 39.12 Learning

First prove deterministic vertical slice, then two-job live smoke, then clean ~8-job core pilot. Separate optional personality/Luna causal tests from baseline. Measure final human quality, total human minutes, review calibration, tail distribution, convergence and actual runtime defects. Change architecture only from material evidence.

---

# Appendix A - P0.8.1/P0.9 source precedence for future reconciliation

When future work needs to understand *why* a rule exists, use this precedence:

1. Latest user decisions captured in `Jobbs#U00f8k_26_integration_summary.md`.
2. This integrated P0.9 specification once adopted.
3. `brainstorm_review.md` for design-option provenance/interactions not reproduced here.
4. `Jobbsok_26_P0.8_consolidated_preimplementation_review.md` for surviving contract rationale.
5. `Brainstorm_Brief.md` for exploratory alternatives/novel mechanisms.
6. `P0.9_prep_package(1).md` for unresolved-information rationale.
7. P0.9 External Evidence Report for external fact constraints, subject to its project-context limitations.
8. `Personality.md` as interpretive source; framework derivative as a proposal/reference, not factual authority.
9. Individual Claude/Gemini reviews/addendum for historical rationale where the consolidated review does not preserve enough detail.

Do not use download date as semantic version precedence.

---

# Appendix B - Research claims that must remain conditional

- Long-context headline token capacity does not imply equal attention/retrieval quality across all content.
- Manual chat JSON is not guaranteed by API Structured Outputs; local validation remains necessary.
- Cheap Luna does not imply positive context-prep value.
- Norwegian platform behavior varies by employer/vacancy; actual form is authority.
- Qualification principles make requirements decision-relevant but do not mandate checklist-style letter prose.
- Generic ATS advice does not automatically invalidate the actual tested Word master.
- LibreOffice behavior must be proven on target machine.
- Public-sector share and portal prevalence must come from actual batch inventory, not stale questionnaire guesses.

---

# Appendix C - Activation triggers for deferred complexity

| Deferred mechanism | Re-open only if |
|---|---|
| Separate reviewer/LLM judge | Stage 3 systematically marks READY on packages humans judge poor/major-repair |
| Similarity/n-gram engine | repeated convergence survives prompt/order/template fixes and human spot-check becomes costly |
| Typography auto-fit | recurring render overflow cannot be fixed economically in template/prompt layer |
| Persistent LO service | converter startup is measured as material bottleneck and service reliability is proven |
| Database/state machine | filesystem/manifest state creates repeated material correctness failures that static reconciliation cannot solve |
| Vector/RAG | candidate corpus/retrieval scale outgrows deterministic index + source escape with measured quality/human cost |
| Automatic clustering | human clustering becomes meaningful recurring bottleneck and model proposal can be validated cheaply |
| Multi-language core | enough target jobs require it that exception handling costs exceed branch complexity |
| Portal reintegration | detached workflow creates larger measured human/quality cost than core branching |
| Full candidate role memory | repeated cross-job learning has durable value not captured by maintained source/policy/calibration artifacts |

---

# Appendix D - Architecture stopping rule

The framework should now stop redesigning by default.

After adoption of this P0.9 specification:

```text
implement
-> render
-> inspect
-> run real models
-> measure final package quality and human handling
-> identify the largest observed bottleneck
-> change the smallest architecture/policy surface that addresses it
-> remeasure
```

Do not reopen broad architecture because another plausible mechanism can be imagined.

A new architecture round is justified only when evidence shows one of:

1. product boundary wrong for real vacancy mix;
2. three-stage topology creates persistent quality/cost failure;
3. state model cannot preserve correctness under real operation;
4. source/evidence architecture materially loses important truth;
5. rendering architecture is incompatible with target channels;
6. human burden materially exceeds target and cannot be fixed locally;
7. a deferred mechanism demonstrates large repeatable quality leverage.

This is the intended convergence point from P0.8.1 hardening and P0.9 exploration into an implementable framework.


---

# Appendix E - Higher-order design laws derived from the combined P0.8.1/P0.9 corpus

These are not new product features. They are compact principles explaining why the selected architecture is internally coherent and giving future maintainers tests for whether a proposed change moves the system in the right direction.

## E.1 Entropy placement principle

The framework should not minimize variability everywhere. It should place variability where it can improve employer-facing quality and eliminate it where it creates state/correctness risk.

### Intentionally low-entropy surfaces

- job/run identity;
- frozen source membership;
- evidence addresses;
- schema structure;
- package-to-template map;
- hard employer limits;
- validator behavior;
- expected-job reconciliation;
- render output checks.

These should have one interpretation.

### Intentionally high-entropy surfaces

- candidate positioning search;
- evidence prioritization;
- argument architecture;
- prose realization;
- final strategic reconstruction;
- whether personality is useful for a particular vacancy.

These benefit from model judgment.

### Pipeline interpretation

```text
low-entropy factual substrate
        -> high-entropy strategic search
        -> constrained coherent realization
        -> high-authority corrective reconstruction
        -> low-entropy persistence/rendering
        -> human irreversible decision
```

A proposed feature is suspicious if it moves entropy in the wrong direction, for example:

- model-generated job identity => unnecessary entropy in state;
- deterministic relevance filtering => false certainty in semantic selection;
- rigid strategy schema semantics => too little entropy in final correction;
- model-generated template mapping => entropy in rendering correctness.

## E.2 Compensating-freedom principle

Any mechanism that compresses or structures upstream model choice should be paired with a downstream recovery mechanism.

| Constraint/reduction | Required compensating freedom |
|---|---|
| deterministic evidence index | source escape |
| optional context-prep slice | primary sources remain available |
| compressed strategy | counterfactual reserve + ELASTIC final writer |
| structured strategy JSON | explicit hypothesis status + Stage 3 may reconstruct |
| fixed dynamic CV surface | high semantic freedom inside the four zones/application |
| human-fixed cluster/order | Stage 1 still performs job-local strategic search |
| nb-NO core | exception path rather than silently mishandling other languages |

This is a general defense against "optimization by irreversible narrowing."

## E.3 False-exclusion asymmetry

For this problem, **omitting decisive evidence is usually more damaging than exposing a strong model to some extra irrelevant evidence**.

Why:

- candidate authority corpus is finite and stable;
- final package requires only a few decisive proof points;
- a missing high-value example can change positioning entirely;
- extra retrieval cost is mostly model/human complexity, not factual harm;
- stronger stages can ignore unhelpful material, but cannot use evidence they never see.

Therefore context systems should prefer:

```text
navigation + prioritization + source escape
```

over:

```text
hard relevance filtering + inaccessible reserve
```

This is why N-03 indexes without relevance judgment and why Luna cannot create permission boundaries.

## E.4 Complexity-reinvestment principle

P0.9's simplification is not an end in itself. Removed complexity should be reinvested only where expected final package value is higher.

### Complexity removed

- channel abstraction;
- portal core branch;
- model cluster planning;
- A/B differentiated treatment;
- redundant progress authority;
- backward-compatible tree;
- mandatory cheap-model prep;
- universal personality layer.

### Complexity selectively added

- evidence index;
- stronger strategy semantics/provenance;
- static invalidation scopes;
- repair telemetry;
- optional authenticity/context experiments;
- real pilot instrumentation.

The net design can therefore be both **simpler operationally** and **more sophisticated informationally**.

## E.5 Authority monotonicity principle

Factual authority never increases downstream.

A later artifact may be a better *decision artifact* but cannot become a better source of reality merely because it is newer.

```text
source truth > evidence index/context/strategy/draft/final for facts
```

Strategic authority, by contrast, is deliberately downstream-increasing:

```text
Stage 1 hypothesis < Stage 2 realized draft < Stage 3 final semantic decision < human approval
```

Keeping these two monotonicities separate prevents both hallucination and over-constrained final writing.

## E.6 Observability-before-automation principle

When a failure mode is plausible but unmeasured, first add the smallest signal that would prove it matters.

Examples:

- feared context loss -> `evidence_outside_prep_refs`, not an evidence graph;
- feared Stage-2 truth issues -> `upstream_claim_repaired`, not a judge stage;
- feared strategy rigidity -> `material_strategy_change`, not a more elaborate strategy system;
- feared convergence -> human spot-check, not similarity infrastructure;
- feared READY overconfidence -> compare status with human review, not immediate reviewer model.

Automation follows repeated observed cost, not imagined elegance.

## E.7 Transaction-local failure containment

Because each job is independently valuable, failure boundaries should align with jobs wherever possible.

The job-centric tree, per-job semantic artifacts, targeted rerun and partial-success finalizer all instantiate one principle:

> A defect in job J should not change the semantic state of jobs K..N unless a frozen shared dependency actually changed.

This improves recovery, auditability and human trust without requiring transactional database machinery.

## E.8 Policy versus mechanism separation

The architecture should distinguish:

- **policy:** what behavior/output is desired;
- **mechanism:** how the current implementation achieves it.

Examples:

| Policy | Current mechanism | Replaceable? |
|---|---|---|
| freeze run identity | `run_manifest.json` hashes | yes, if equivalent deterministic authority exists |
| final source traceability | deterministic evidence IDs | yes, if replacement preserves stable addresses |
| document rendering | Word master + converter | yes, if quality/channel compatibility improves |
| distinct semantic roles | Sol/Terra/Sol current routing | model names yes; roles no without evidence |
| manual irreversible gate | human submission | not in P0.9 |

This prevents model/provider/runtime changes from being mistaken for architecture changes.

## E.9 Context artifacts should have an epistemic type

Every generated context object should state what it is allowed to do.

Recommended conceptual types:

- `AUTHORITY_SOURCE`
- `DETERMINISTIC_INDEX`
- `ADVISORY_CONTEXT`
- `STRATEGY_HYPOTHESIS`
- `DRAFT`
- `FINAL_SEMANTIC_OUTPUT`
- `REVIEW_TELEMETRY`
- `DERIVED_OPERATOR_VIEW`

This is more useful than vague labels like "context file" because it tells models and humans whether the content may establish facts, constrain decisions or be regenerated.

## E.10 Latest-wins must be granular, not document-global

The project evolved through overlapping chats. Therefore future reconciliation must apply:

> Newer information supersedes older information only where it directly changes, specifies, narrows or invalidates the same granular contract.

Examples:

- later user prompt-budget answer supersedes earlier 15/20-prompt assumptions;
- portal detachment selection deletes core portal contract but does not supersede the general exact-limit rule in the detached module;
- job-centric manifest design supersedes stage-centric state layout but does not supersede P0.8.1 expected-set reconciliation;
- personality default OFF is a new synthesis decision but does not supersede the canonical personality source content;
- final Sol ELASTIC reinforces rather than replaces P0.8 free-writer philosophy.

This rule should be used for all future P0.9.x integration work.

