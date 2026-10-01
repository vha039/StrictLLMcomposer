# Jobbsøk_26 P0.9 — Post-Critique Authoritative User Decision & Adjudication Directive

**Status:** `AUTHORITATIVE_PRE_FREEZE_DIRECTIVE`  
**Purpose:** Highest-authority decision input for the final P0.9 architecture adjudication and freeze  
**Applies to:** Final generation of the P0.9 normative specification, decision/adoption record, and implementation/verification contract  
**Date:** 2026-08-22  
**Authority:** Represents the user's latest explicit post-critique decisions and the necessary consequences of those decisions.

---

## 0. Authority and precedence

This document is the **highest-authority source for every subject it addresses**.

When generating, adjudicating, or freezing the final P0.9 architecture, use this precedence:

1. **This document**
2. Other explicit user decisions not contradicted by this document
3. The seven-file canonical P0.9 context package
4. Verified implementation evidence from P0.7, at its proper empirical scope
5. The Opus P0.9 draft architecture
6. Independent critique reports
7. Earlier proposals, synthesis, brainstorms, research implications, or model recommendations

If any earlier source, draft, critique, resolution queue, or derived synthesis conflicts with this document, **this document wins**.

Critique findings are evidence and suggestions, not authority. In particular, critiques MUST NOT reopen a user decision that is explicitly frozen here merely because an earlier context file still labels it `OPEN`, `STRONG_DEFAULT`, `VERIFY`, or similar.

### 0.1 Decision labels used here

- **`USER-LOCKED`** — explicit current user decision. Final architecture MUST preserve it.
- **`NORMATIVE-CONSEQUENCE`** — necessary architectural consequence of one or more `USER-LOCKED` decisions. Final architecture may improve wording/implementation expression, but MUST preserve the consequence unless a direct contradiction is found.
- **`IMPLEMENTATION-DEFAULT`** — preferred initial implementation behavior that may later be tuned without reopening architecture, provided invariant behavior remains intact.
- **`VERIFY`** — empirical behavior to prove during implementation or operation; verification MUST NOT silently alter a `USER-LOCKED` policy.
- **`EXPERIMENT`** — optional post-baseline quality/ergonomic question. Baseline correctness MUST NOT depend on it.

---

# 1. Updated framework intention

## 1.1 Purist MVP-KISS product philosophy — `USER-LOCKED`

P0.9 is intentionally **not** a generalized application-channel framework.

It is a narrow, opinionated, production-focused system optimized around the application elements that are known in advance to be:

1. consistently useful;
2. consistently required for the overwhelming useful majority of the target opportunity set;
3. sufficiently invariant to justify deep optimization;
4. high-return targets for model reasoning and implementation effort.

The core framework therefore deliberately optimizes the **invariant happy path**, approximately the useful ~80% case, rather than universalizing itself around difficult or low-return edge cases.

The governing design principle is:

> **Optimize the invariant CV + application-letter production path ruthlessly. Push irregular channel, portal, language, and other edge-case complexity outside the core instead of contaminating every normal package with dynamic branching, uncertain state, uncertain outputs, extra prompts, extra schemas, extra validation, and lower semantic attention.**

This is a deliberate expected-value choice, not an omission.

Difficult edge cases often have:
- disproportionate human and model input requirements;
- lower marginal quality return;
- higher framework complexity;
- larger risk of depressing quality on otherwise straightforward applications because semantic/model attention and implementation effort are spent on rare variation.

The framework SHOULD therefore accept that some nonconforming jobs receive separate/manual handling rather than optimize all jobs uniformly.

## 1.2 Optimization hierarchy — retained

Among truth-safe choices:

1. **final package quality / expected interview value**
2. **low human effort**
3. **fast and simple implementation**
4. **model cost**
5. **reversibility / optionality**

Truth, factual identity, employer usability, and human final authority remain hard constraints.

## 1.3 Selective-quality objective — retained

P0.9 optimizes the useful majority rather than batch uniformity.

The approximate operational objective remains:

- roughly 30 strong packages from a batch of roughly 40 is acceptable;
- weak, awkward, or nonconforming tail cases may be deferred, separately handled, rerun manually, or dropped;
- the system SHOULD NOT weaken strong packages merely to make the weak tail more uniform.

`Q_happy` remains a human/evaluation concept, not a runtime model score.

---

# 2. Core product boundary

## 2.1 Invariant CV + application letter — `USER-LOCKED`

The P0.9 core ALWAYS produces:

- one materially tailored CV; and
- one materially tailored application letter.

This is an architectural invariant.

The final architecture MUST NOT reopen this choice based on:
- vacancy inventory;
- portal prevalence;
- platform mix;
- public/private sector distribution;
- reviewer speculation;
- unusual jobs;
- inferred channel behavior.

The invariant pair is selected precisely because it is the stable product surface worth optimizing deeply.

The architecture MUST NOT reintroduce a `letter_required` branch merely to optimize rare cases.

If a particular employer does not consume one of the generated documents, the unused artifact is tolerated as low-cost surplus rather than allowing conditional-output complexity to contaminate the core.

## 2.2 Bokmål-only core — `USER-LOCKED`

P0.9 core is **Norwegian Bokmål (`nb-NO`) only**.

This is an architectural choice, not an empirical assumption about the exact first-batch language distribution.

Non-Bokmål vacancies are handled outside the core or as explicit exceptions. Their existence does NOT reopen the core language architecture.

The final architecture MUST NOT retain language branching inside normal core schemas/prompts/render paths.

## 2.3 Portal/forms outside core — `USER-LOCKED`

Portal questions, structured form answers, platform-specific text boxes, question IDs, limits, portal state, and portal answer generation remain **completely outside the P0.9 core**.

When needed, portal/form assistance may be performed:
- downstream;
- manually initiated;
- using the already approved/final package and authoritative sources;
- without becoming a prerequisite for normal package completion.

The core MUST NOT contain:
- portal schemas;
- portal answer arrays;
- portal validation;
- portal status;
- channel matrix machinery;
- portal-driven readiness;
- portal-specific model stages.

## 2.4 No channel/platform machinery in core — `USER-LOCKED`

The core SHOULD NOT maintain machine-readable state such as:

- `platform`
- `channel`
- `portal_required`
- `letter_required`
- a generalized `required_components` matrix
- platform-specific submission-mode logic

solely to dynamically adapt the core package.

Operational/human notes may identify unusual jobs, but those facts MUST NOT become a generalized branching architecture.

This explicitly overrides critique recommendations to restore a small channel-fact model merely because one could be implemented cheaply.

## 2.5 Vacancy inventory is operational, not architectural — `USER-LOCKED`

The real vacancy/channel inventory is useful operational information.

It is **not a prerequisite for freezing**:
- CV + letter invariance;
- Bokmål-only core;
- portal detachment;
- no-channel-state core.

Inventory may:
- identify exceptions;
- help prioritize work;
- reveal future redesign opportunities;
- support later manual decisions.

It MUST NOT automatically reopen these core decisions.

## 2.6 No automatic exception threshold — `USER-LOCKED`

Delete the draft's numeric architecture-reopening triggers such as:

- `>20% exceptions`
- `two` or `more than two` jobs sharing a reason
- any similar automatic threshold

The human decides if exception volume or a recurring edge case becomes sufficiently annoying or valuable to justify a later redesign.

No threshold should mechanically reopen architecture.

## 2.7 Exception handling — `NORMATIVE-CONSEQUENCE`

Nonconforming jobs SHOULD be:
- explicitly visible;
- not silently lost;
- separately/manual handled;
- prevented from blocking normal core jobs.

The exception mechanism itself MUST remain small. It exists for visibility and isolation, not as a second generalized workflow.

---

# 3. `Q_happy` and exception reporting

## 3.1 Core denominator — `USER-LOCKED`

Calculate `Q_happy` on **CORE automated jobs**.

Exceptions are outside the core quality distribution.

## 3.2 Anti-gaming/reporting requirement — `NORMATIVE-CONSEQUENCE`

Every evaluation that reports core `Q_happy` MUST also report enough batch counts to prevent denominator ambiguity, at minimum:

- total approved opportunities;
- core jobs;
- exception jobs;
- submitted packages if known.

The system MUST NOT present core `Q_happy` as if it measures all approved opportunities.

---

# 4. Run immutability and reopen semantics

## 4.1 Frozen run is genuinely immutable — `USER-LOCKED`

Once frozen, a run MUST never be mutated in place.

Remove the draft's `freeze --amend` model.

No operation may silently alter inside an existing frozen run:
- expected jobs;
- authoritative source hashes;
- vacancy hashes;
- semantic policy snapshot;
- model/stage configuration that determines the package;
- canonical run-level authority.

## 4.2 Reopen = branch to a new run — `USER-LOCKED`

Immutability MUST NOT create usability friction.

When the user wants to reopen/change any frozen-run element:

1. create a new run;
2. assign a new `run_id`;
3. record the original as `parent_run_id`;
4. copy, link, or otherwise reuse current relevant run state/artifacts where safe;
5. leave the original run permanently untouched and auditable;
6. continue work in the new run.

The backend may implement copying/referencing efficiently. The user SHOULD NOT have to manually reconstruct state.

The user-facing experience should remain simple, e.g.:

> “This inquiry/work is referenced by run ID X.”

## 4.3 No general manifest-version lineage engine — `NORMATIVE-CONSEQUENCE`

Do NOT solve run immutability by creating an event-sourced/versioned mutable manifest system.

Prefer:

> immutable run + cheap branch

over:

> mutable run + manifest versions + artifact lineage graph.

---

# 5. Semantic stage topology

## 5.1 Core three-stage topology — retained

The core semantic architecture remains:

1. **Stage 1 — Sol-class Decision Architecture**
2. **Stage 2 — Terra-class Native Package Writer**
3. **Stage 3 — Sol-class Elastic Final Writer / Review**

No fourth standard semantic stage is required.

Semantic stages remain manually initiated model chats rather than a normal API/model-call orchestrator.

## 5.2 Final writer elasticity — retained

Stage 3 remains `ELASTIC` within immutable truth ceilings.

It may reconstruct identity, headline, evidence emphasis, CV dynamic content, argument structure, full application prose, and personality-conditioned expression.

It is not required to defend or comply semantically with Stage 1 strategy.

---

# 6. `RERUN` meaning and recovery architecture

## 6.1 `RERUN` is triage only — `USER-LOCKED`

Keep `RERUN` as a **triage/status concept only**.

It means approximately:

> The package requires broader model reprocessing/reconstruction rather than a bounded local human edit.

There is NO dedicated RERUN subsystem.

Do NOT create:
- special RERUN schemas;
- a fourth-stage RERUN workflow;
- special RERUN state machines;
- RERUN-specific strategy mutation rules;
- RERUN-specific history/invalidation complexity.

When a human acts on a `RERUN`, they may choose the most sensible restart point or request fresh processing. Existing artifacts may be supplied as context/history, but the framework does not need a separate architectural lifecycle for this.

## 6.2 `READY / CHECK / RERUN` meaning — `USER-LOCKED`

Semantic/operator triage is based on **remaining repair scope**, not number of reasons.

- `READY` — no known material repair needed; bounded final human skim/approval.
- `CHECK` — local confirmation/editing, not strategic reconstruction.
- `RERUN` — broader semantic reconstruction is cheaper/better than local editing.

Up to approximately three displayed reasons may be useful for operator UX, but:

> **“4 reasons ⇒ RERUN” is deleted.**

Reason count MUST NOT mechanically route the status.

---

# 7. Retry and repair policy

## 7.1 Architectural rule — `USER-LOCKED`

Repair/retry behavior MUST remain:

- bounded;
- visible;
- no hidden retries;
- no uncontrolled loop;
- job-local;
- non-blocking for unrelated jobs.

The exact retry depth is NOT a frozen architecture constant.

## 7.2 Settings-driven retry escalation — `USER-LOCKED`, conditional on KISS implementation

If this can be implemented **cleanly, cheaply, and without a large orchestration subsystem**, expose a setting conceptually equivalent to:

```text
retry_start_stages = [3]
```

Array semantics:

- number of entries = maximum configured retry/escalation attempts;
- each entry = earliest semantic stage to restart on that attempt;
- retry proceeds from that stage through Stage 3.

Examples:

```text
[3]
```

= one retry, redoing Stage 3 only.

```text
[3, 2, 1]
```

= three escalating retries:

1. Stage 3 only;
2. Stage 2 → Stage 3;
3. Stage 1 → Stage 2 → Stage 3.

An empty array may mean no configured semantic retry.

## 7.3 Initial default — `IMPLEMENTATION-DEFAULT`

Initial default:

```text
retry_start_stages = [3]
```

i.e. **one retry attempt**, starting at Stage 3.

The setting may later be tuned through `SETTINGS.md` without architecture revision.

## 7.4 Critical anti-complexity constraint — `USER-LOCKED`

This setting MUST NOT justify introducing:

- API orchestration;
- generalized model runners;
- hidden autonomous multi-stage retry loops;
- a retry workflow engine;
- additional persistent retry-state architecture.

If the chosen execution surface cannot support this cleanly within the existing manual-chat operating model, **do not build a large subsystem to force it**.

Use the fallback below instead.

## 7.5 Exhaustion / fallback — `USER-LOCKED`

When the configured retry path:
- is unavailable;
- cannot be implemented simply;
- or is exhausted without resolution,

the package is deferred to the human.

Use a simple operator-facing terminal state such as:

```text
BLOCKED_MANUAL
```

Meaning:

> blocked / deferred — waiting for manual control.

The system SHOULD surface:

- run ID;
- job ID;
- identified issue;
- last successful stage if relevant;
- attempts used;
- deterministic validation/render diagnostic where relevant;
- recommended next step.

Then continue processing independent jobs.

No recovery state machine is required.

## 7.6 Mechanical repair behavior — `NORMATIVE-CONSEQUENCE`

Where a model can correct a deterministic artifact-format/validation defect in the same session, one visible correction attempt is a reasonable initial implementation default.

Validators SHOULD report all mechanically detectable violations in one pass where practical.

Failure after the allowed repair/retry path should become visible and job-local, not silently retried.

---

# 8. State and failure representation

## 8.1 Failure must be derivable without reading audit history — `NORMATIVE-CONSEQUENCE`

The final architecture MUST define one minimal **current failure/blocking representation** readable by status derivation.

It may be:
- a small current `stage_failure` record;
- or an equivalent canonical validation-result pointer.

It MUST NOT require event sourcing.

Audit history remains non-authoritative.

## 8.2 History — `NORMATIVE-CONSEQUENCE`

History exists for audit, superseded artifacts, and diagnostics.

Status and current behavior SHOULD be derivable from current canonical state, not by replaying history.

---

# 9. Strategy artifact

## 9.1 Canonical structured strategy — `USER-LOCKED`

Keep:

- canonical `strategy.json`;
- deterministic generated human-readable view if useful.

There MUST NOT be two independently authored canonical strategy representations.

## 9.2 Strategy epistemic role — retained

Strategy remains hypothesis, non-factual, non-final, revisable downstream, subordinate to factual sources, and non-binding on Stage 3.

## 9.3 Validation boundary — `USER-LOCKED`

Hard deterministic validation of strategy is for mechanical concerns such as:

- schema/structure;
- job identity;
- required epistemic constants where useful;
- valid source/evidence references;
- valid employment IDs;
- unknown fields where intentionally forbidden;
- true external/tool constraints.

Word counts, counts of requirements, counts of evidence bridges, number of paragraphs, number of CV bullets, and similar semantic-density choices SHOULD be defaults, soft targets, warnings, or model guidance rather than hard failures unless a real rendering/schema/external constraint makes a hard limit necessary.

## 9.4 Material requirements must not be truncated — `NORMATIVE-CONSEQUENCE`

No hard cap such as `≤12 requirements` may force omission of an actual material employer requirement.

## 9.5 Historical P0.7 cardinalities are not automatic P0.9 law — `NORMATIVE-CONSEQUENCE`

Bounds inherited from older schemas such as 4–8 competencies, max 4 employment overrides, 1–5 bullets, or 1–5 application paragraphs may be sensible defaults, but MUST NOT become hard P0.9 semantic rules merely because P0.7 used them.

---

# 10. Evidence index and provenance

## 10.1 Lean deterministic evidence index — `USER-LOCKED`

P0.9 baseline includes a **lean deterministic evidence index**.

Purpose:
- stable factual evidence addresses;
- source navigation;
- mechanical detection of invented/nonexistent evidence IDs;
- provenance;
- final evidence-reference auditability.

It is NOT a retrieval/ranking platform.

## 10.2 Required index properties — `USER-LOCKED`

The index MUST be:

- generated automatically;
- deterministic;
- source-linked;
- regenerable;
- non-semantic;
- free of model-written summaries;
- free of relevance scores;
- free of ranking;
- free of inferred fit;
- free of manual maintenance;
- compatible with unconditional direct source access.

It SHOULD give all **usable factual evidence** stable addresses.

## 10.3 Explicitly rejected overengineering — `USER-LOCKED`

Do NOT require every byte of every source to belong to exactly one mathematically exhaustive, non-overlapping leaf entry.

No byte-partition theorem, vector DB, graph, embeddings, relevance index, or manually curated claim graph is required.

The useful guarantee is:

> useful factual evidence is addressable and nothing is deliberately filtered out as irrelevant.

## 10.4 Factual authority namespace — `USER-LOCKED`

Final factual `used_evidence_refs` may point only to the three factual candidate authorities:

- `Work_experience.md`
- `Education.md`
- `Other_high_value_information.md`

`CV_BASELINE.md` remains a derived chronology/rendering structure and may provide employment IDs, section identity, and merge mechanics through a **separate mechanical reference mechanism**.

It MUST NOT gain factual-authority status merely by sharing an index namespace.

## 10.5 Reference validation does not prove truth — `NORMATIVE-CONSEQUENCE`

Deterministic code may prove:

- evidence ID exists;
- allowed authority source;
- index/source hash consistency.

It cannot prove that a prose claim is semantically supported by that evidence, that attribution is correct, or that the selected evidence is strongest.

Semantic support remains model + human responsibility.

---

# 11. Personality

## 11.1 Active feature from day one — `USER-LOCKED`

Personality is **ON by default** in the first P0.9 production baseline.

Do not implement it as a half-finished, low-priority, optional stub that models subsequently treat as unimportant.

If the feature is present, it should be properly integrated as a first-class semantic-quality feature from the beginning.

## 11.2 Runtime pattern — `USER-LOCKED`

Use a bounded **0–3 facet** runtime selection.

Stage 1 may select 0–3 relevant personality facets after grounding itself in:

1. vacancy;
2. factual candidate evidence.

Zero remains valid when no personality facet materially improves the package.

## 11.3 Authority boundary — retained and mandatory

Personality is interpretive context, never factual candidate authority, incapable of raising a factual claim ceiling, and incapable of inventing achievements/skills/results/history.

Employer-facing text MUST use ordinary professional language rather than typology jargon.

## 11.4 Downstream handling — retained

Preferred integration:

- Stage 1 reads the rich personality source;
- Stage 1 selects/distills 0–3 relevant facets;
- Stage 2 receives only the distilled guidance needed for writing;
- Stage 3 may suppress, replace, or ignore personality-conditioned framing.

The full personality profile SHOULD NOT be repeatedly injected into every downstream stage when a distilled handoff is sufficient.

---

# 12. Cross-job semantic carryover

## 12.1 Baseline controls — `USER-LOCKED`

Use:

- hard file/state isolation between jobs;
- exact job identity checks;
- explicit per-job reset/reload protocol;
- one-job persistence before moving on.

## 12.2 No convergence detector yet — `USER-LOCKED`

Do NOT build a baseline similarity detector, n-gram gate, headline similarity gate, or semantic convergence detector.

Observe actual convergence/position effects during the pilot first.

## 12.3 Epistemic classification — `NORMATIVE-CONSEQUENCE`

Do not claim that shared sequential cluster chats can mechanically guarantee zero semantic carryover.

Separate hard mechanical state/file isolation from semantic carryover risk, which is protocol + evaluation.

---

# 13. Rendering and output degradation

## 13.1 Target deliverables

Normal target output per core job remains:

- CV DOCX
- CV PDF
- application letter DOCX
- application letter PDF

## 13.2 PDF conversion failure is graceful degradation — `USER-LOCKED`

If native/automated PDF conversion fails but the DOCX outputs are valid:

- the package MAY still be `READY` or `CHECK`;
- the package remains usable/conforming;
- PDF failure MUST be surfaced clearly as a rendering limitation;
- the semantic package MUST NOT become `FAILED` merely because automated PDF conversion failed;
- the human may manually export/save the DOCX as PDF.

This explicitly overrides the Opus draft's all-four-files-or-fail contract.

## 13.3 Orthogonal semantic and render status — `NORMATIVE-CONSEQUENCE`

Do NOT create semantic statuses such as `READY_DOCX_ONLY`.

Keep semantic triage:

- `READY`
- `CHECK`
- `RERUN`

and represent rendering separately, e.g. conceptually:

```text
render:
  docx: OK
  pdf: OK | DEGRADED | FAILED
  limitation: ...
```

## 13.4 Render fallback must remain KISS

Do not build complex multi-converter infrastructure merely to avoid a PDF degradation flag.

A simple verified fallback/manual export path is acceptable.

---

# 14. Employer-facing document date

## 14.1 Finalization-time date — `USER-LOCKED`

The application/document date becomes fixed when the semantic package is **finalized/approved**, not at initial run freeze.

Afterward, a pure deterministic rerender MUST preserve that approved date.

---

# 15. Identity/contact placement and parseability

## 15.1 Outcome, not layout, is normative — `USER-LOCKED`

The normative requirement is successful ordinary extraction/parseability of critical identity/contact information.

The architecture MUST NOT require body-flow duplication merely because generic ATS advice says headers may be unsafe.

Step 2 should inspect/test the actual masters, verify extraction/read order, and move or duplicate critical identity/contact into body flow only if needed.

Actual template/channel evidence outranks generic document folklore.

---

# 16. Derived views and epistemic labels

## 16.1 Do not falsely label convenience views as lossless — `NORMATIVE-CONSEQUENCE`

`CV_BASELINE.md`, normalized vacancy text, and `job_context` MUST NOT be called `DERIVED_LOSSLESS_VIEW` unless losslessness is mechanically proven for the relevant scope.

Use labels such as `DERIVED_VIEW` or `DERIVED_CONVENIENCE_VIEW`.

Direct source escape remains available.

---

# 17. `requires_source_inspection`

## 17.1 Canonical home required — `NORMATIVE-CONSEQUENCE`

If vacancy normalization/extraction sanity detects that a derived text view may be unreliable, the signal such as:

```text
requires_source_inspection = true
```

must have one explicit canonical home available to stage prompts.

Do not leave this as prose with no schema/storage location.

---

# 18. Continuation behavior

## 18.1 Fresh continuation protocol — `NORMATIVE-CONSEQUENCE`

If a cluster-stage chat is interrupted or context-exhausted:

1. open a fresh continuation chat;
2. load the stage instruction/policy;
3. identify the cluster/run;
4. derive the next unfinished/blocked job from current state;
5. load that job's required inputs;
6. continue.

Do NOT reload completed jobs' full artifacts merely to reconstruct chat history.

The disk/run state is authoritative, not remembered chat position.

---

# 19. Human pilot logging

## 19.1 Never write human measurements into regenerable views — `NORMATIVE-CONSEQUENCE`

Human pilot data such as:

- 1–10 quality score;
- handling minutes;
- corrections;
- submit-ready;
- qualitative notes;

must live in a separate persistent human-owned log/spreadsheet/file.

Derived queue regeneration MUST NOT erase human measurements.

---

# 20. Direct human edits to rendered documents

## 20.1 Canonical semantic source versus post-pipeline edits — `NORMATIVE-CONSEQUENCE`

The canonical semantic package remains the structured final package.

Preferred workflow:
- make semantic text edits in the canonical package;
- rerender.

If the human directly edits a final DOCX:
- treat it as a post-pipeline submission artifact;
- do not silently overwrite it on subsequent deterministic runs.

The implementation SHOULD protect human edits with a simple explicit overwrite/force/no-clobber behavior.

Do not build document version management.

---

# 21. Validator scope and diagnostics

## 21.1 Code owns mechanics only — retained

Deterministic validation may enforce schema, identity, paths, known IDs, source/reference existence, template mechanics, output presence/readability, leakage of known private/control tokens, and true external technical limits.

It MUST NOT claim to prove truth, relevance, natural language quality, persuasion, motivation authenticity, or factual support of free prose.

## 21.2 Report violations densely — `NORMATIVE-CONSEQUENCE`

Where practical, validators SHOULD return all detected mechanical violations in one run rather than fail at the first issue.

## 21.3 Style phrases are not Python failures

Norwegian stock/cliché phrase guidance remains a semantic writing instruction.

Strings such as `brenner for` MUST NOT cause deterministic failure merely because they appear.

Only closed-set tokens with no legitimate employer-facing use may justify narrow lexical boundary checks.

---

# 22. P0.8.1 provenance language

## 22.1 No retroactive authority promotion — `NORMATIVE-CONSEQUENCE`

The final P0.9 specification/decision record MUST NOT label prior P0.8.1 mechanisms simply `[P0.8.1 adopted]` in a way that implies historical normative adoption.

Where P0.9 adopts a useful P0.8.1 hardening, describe it as a P0.9 adoption/decision informed by P0.8.1.

---

# 23. Product pilot and acceptance

## 23.1 Engineering proof ≠ semantic quality — retained

Maintain separate evidence loops:

1. deterministic engineering conformance;
2. real product-quality pilot;
3. later optional-feature/parameter experiments.

## 23.2 No desired-outcome acceptance gaming — `NORMATIVE-CONSEQUENCE`

Do not require the real pilot to demonstrate that Stage 3 performs a major reconstruction at least once.

If weak upstream work naturally occurs, observe whether Stage 3 repairs it. Otherwise `N/A`.

Synthetic tests may prove that the architecture permits elastic reconstruction.

## 23.3 Truth guardrail

Approved/submitted final packages SHOULD have zero **known material** truth/attribution defects.

Caught-and-repaired upstream defects are useful process diagnostics and do not count as final truth failures.

## 23.4 Human-evaluated criteria are human-evaluated

Employer specificity, persuasive quality, native Bokmål, backbone coherence, evidence strength, and human handling burden require human/model evaluation.

---

# 24. Final architecture simplifications explicitly required

## Keep

- invariant Bokmål CV + letter;
- three-stage Sol→Terra→Sol;
- final-Sol elasticity;
- human clustering/order;
- job-centric runtime;
- immutable runs;
- derived status;
- partial success;
- static/simple invalidation;
- structured strategy;
- lean deterministic evidence addresses;
- personality active ON with 0–3 facets;
- mechanical/semantic validation separation;
- READY/CHECK/RERUN;
- job-local failure;
- manual final submission;
- P0.7 template reuse only after inspection;
- DOCX/PDF rendering with graceful PDF degradation;
- three separate evaluation loops.

## Delete / reject

- portal/form machinery in core;
- channel/platform branching in core;
- automatic exception thresholds;
- mutable-run `freeze --amend`;
- dedicated RERUN subsystem;
- RERUN strategy-mutation lifecycle;
- exhaustive byte-partition evidence indexing;
- fixed normative retry count;
- reason-count-based RERUN routing;
- automatic convergence detector in baseline;
- hard semantic-density/cardinality limits without real technical need;
- P0.7 numeric schema bounds treated as automatic P0.9 law;
- body-flow identity placement as a universal normative rule;
- PDF conversion failure as semantic package failure;
- optionality-only future hooks that add baseline framework surface;
- event-sourced/dependency-engine/database solutions to problems handled by immutable runs + simple derived state.

---

# 25. Final intended architecture character

The final P0.9 framework should be understood as:

> **A narrow, opinionated, quality-first, one-candidate production pipeline that applies sophisticated model reasoning where semantic quality matters and aggressively minimizes mechanics, branching, state, recovery machinery, and edge-case generality everywhere else.**

Its design law is:

> **Strict mechanics where mechanics protect truth/state; maximal semantic freedom where frontier models create package quality; push irregular low-return cases outward rather than generalizing the happy path.**

| Concern | P0.9 authoritative posture |
|---|---|
| Core product | invariant CV + application letter |
| Core language | Bokmål only |
| Portal/forms | outside core |
| Channel state | no generalized core machinery |
| Inventory | operational, not architecture-defining |
| Exceptions | visible, isolated, human/peripheral |
| Quality objective | strong-majority / `Q_happy` |
| Run state | immutable run + branch-on-reopen |
| Stage topology | Sol → Terra → Sol |
| Final writer | ELASTIC |
| Strategy | canonical structured JSON, mechanical hard checks only |
| Evidence | lean deterministic addresses, factual-authority-only refs |
| Personality | ON by default, 0–3 facets, properly integrated |
| Retry | bounded/settings-driven only if trivial to implement |
| Exhaustion | `BLOCKED_MANUAL` / defer and continue |
| RERUN | triage label, not subsystem |
| Status | semantic repair-scope status separated from render state |
| Rendering | DOCX required; PDF target with graceful conversion degradation |
| Cross-job control | hard file/state isolation + semantic reset protocol |
| Convergence | observe first; no detector yet |
| Dates | fixed at finalization/approval, stable on rerender |
| Parseability | outcome-based, template tested empirically |
| Human authority | final factual/semantic/submission authority |

---

# 26. Instructions to the final P0.9 adjudicator

When using this directive together with the seven canonical context files, Opus draft, and independent critiques:

1. **Do not majority-vote.**
2. Treat this directive as authoritative over critic objections.
3. Do not reopen invariant CV+letter, Bokmål-only core, portal detachment, or no-channel-core merely because an earlier critique classified inventory as a freeze prerequisite.
4. Use critique findings only to identify contradictions, simplify mechanisms, repair lifecycle gaps, clarify implementation boundaries, and improve testability.
5. Preserve the architecture skeleton where compatible with this directive.
6. Prefer deleting machinery over adding reconciliation/state infrastructure.
7. Distinguish `USER-LOCKED` policy, derived architectural consequence, implementation default, empirical verification, and later experiment.
8. Do not convert easy-to-tune parameters into frozen architecture.
9. Do not let implementation constraints silently broaden the product.
10. Regenerate the final three P0.9 artifacts coherently after adjudication; do not textual-patch the Opus drafts.
11. Cross-audit the regenerated artifacts for authority consistency, status/state coherence, no hidden portal/channel branch, immutable-run compliance, retry/recovery KISS compliance, evidence-authority correctness, semantic/mechanical separation, and implementation-contract derivation fidelity.
12. Final target status after successful adjudication:
    - `Project architecture: P0.9`
    - `Specification revision: 0.9.0`
    - `Status: FROZEN_NORMATIVE`

---

# 27. Superseded post-critique interpretations

The following interpretations are explicitly superseded:

- “CV+letter invariant remains open until vacancy inventory” → **superseded; invariant is locked.**
- “Bokmål-only remains open until inventory” → **superseded; Bokmål-only is locked.**
- “Channel/platform facts must be restored to core” → **superseded; no generalized channel machinery in core.**
- “Vacancy inventory is a Step-1 architecture prerequisite” → **superseded; inventory is operational.**
- “Exception percentage automatically reopens architecture” → **superseded; human decides.**
- “Frozen run should support same-run amendment/versioning” → **superseded; immutable run + new-run branch.**
- “PDF absence necessarily means package failure” → **superseded; validated DOCX can remain READY/CHECK with render degradation.**
- “RERUN requires a dedicated workflow/subsystem” → **superseded; RERUN is triage only.**
- “RERUN may mutate strategy under special lifecycle rules” → **superseded; no special RERUN lifecycle.**
- “Exactly two repair attempts are normative” → **superseded; bounded retry is architectural, initial setting is one Stage-3 retry if cheaply supported.**
- “Four review reasons imply RERUN” → **superseded; repair scope determines status.**
- “Evidence index must partition every source byte” → **superseded; lean stable-address index.**
- “Personality should default OFF / detailed interface may be deferred” → **superseded; personality is ON and properly implemented with 0–3 facets.**
- “Body-flow identity duplication is mandatory architecture” → **superseded; verified parseability is the invariant.**
- “Employer-facing document date freezes with run” → **superseded; date freezes at semantic finalization/approval.**

---

# 28. Closure statement

This directive is intended to eliminate the remaining ambiguity introduced by the post-Opus critique phase.

The final architecture adjudicator should not spend another cycle debating the user choices recorded here.

Remaining discretion belongs principally to:

- exact repository/module implementation;
- exact schema field names that do not affect semantics;
- exact UI/CLI representation;
- efficient copy/link mechanics for branched runs;
- implementation of the minimal current failure record;
- exact deterministic evidence-ID syntax;
- exact render-state field names;
- whether the retry-stage array can be supported cheaply enough to warrant implementation;
- local template/rendering choices proven through target-machine verification.

Those decisions MUST remain subordinate to the product and KISS principles above.

**End state desired:** a final P0.9 normative specification that is more decisive, narrower, simpler, and more production-effective than the Opus draft—not a broader framework produced by accumulating every critique recommendation.
