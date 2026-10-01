# Implementation Baseline and Build Obligations

## 0. Purpose and evidence boundary

This document answers:

> **What is actually implemented and evidenced, what implementation capital can plausibly be reused, and what must a future Codex builder construct, adapt, replace or verify?**

It does not treat a design document as a repository. Four evidence states are used:

| State | Meaning |
|---|---|
| `DESIGNED` | Specified or proposed, but no inspected implementation proves it exists |
| `IMPLEMENTED` | Present in the inspected P0.7 release or otherwise directly evidenced |
| `MECHANICALLY_TESTED` | Exercised by deterministic tests/fixtures in the represented release or direct audit |
| `PRODUCTION-MODEL_TESTED` | Exercised end to end with real vacancies and the intended semantic models, followed by human product review |

The corpus supports substantial `IMPLEMENTED` and `MECHANICALLY_TESTED` evidence for P0.7. It does **not** support a real semantic production pilot for P0.7, P0.8 or P0.9. P0.8.0 is a normative design, P0.8.1 a non-normative hardening layer, and P0.9 remains the architecture target. See `01_CURRENT_STATE_AUTHORITY_AND_DECISIONS.md` for status authority and `02_P0.9_CANDIDATE_ARCHITECTURE.md` for the current candidate.

---

## 1. Verified P0.7 executable baseline

### 1.1 Release identity and evidence level

The represented P0.7 release is the latest actually implemented framework in this corpus. It was produced on 2026-08-04 and later independently inspected. The historical summaries report:

- 52 files in the release package;
- four manually initiated semantic stages;
- three deterministic scripts;
- 12 standard stage chats for a nominal batch;
- 2 macroclusters of roughly 20 jobs and 4 miniclusters of roughly 10;
- 34 automated tests, with 32 passing and 2 skipped because PowerShell was unavailable in the audit environment;
- zero test failures in that rerun;
- a controlled synthetic-vacancy E2E through representative Stage 1/2/3/4 artifacts, check-only validation and DOCX/PDF rendering: PASS;
- no real intended-model run over a genuine vacancy batch.

The direct audit in SRC-19 adds artifact-level evidence about schemas, scripts, Word masters and test behavior. These findings are empirical implementation evidence even though SRC-19 as a whole is a derived synthesis.

### 1.2 P0.7 topology

```text
Human-approved vacancies
        │
        ▼
     ingest.py
        │
        ▼
Stage 1 — Terra Max
broad evidence/first-pass analysis in macroclusters
        │
        ▼
Stage 2 — Sol Max
strategy/blueprint refinement in macroclusters
        │
        ▼
Stage 3 — Terra XHigh
complete package drafting in miniclusters
        │
        ▼
Stage 4 — Sol XHigh
final package/review in miniclusters
        │
        ▼
    finalize.py
        │
        ├── validation/reconciliation
        ├── CV baseline merge
        ├── DOCX generation
        ├── PDF conversion
        └── batch reports/delivery
```

`advance.ps1` mediated physical stage progression. The system used separate stage directories and completion/review sentinels to control movement.

This topology is historical implementation, not the P0.9 target. Its value lies in the mechanical substrate and the defects it exposed.

### 1.3 Implemented source-authority model

P0.7 established the factual authority boundary that survives into the current project:

| Source | Implemented role | Historical P0.7 version / SHA-256 |
|---|---|---|
| `Work_experience.md` | Work, project, responsibility, method, contribution and outcome facts | content `2.4.0`, verified/updated 2026-07-29; `0b39a5105f0d809d1bc9a917665bc69c619eb059253a779079b37304b49a2f9d` |
| `Education.md` | Degree, course, institution and education facts | content `2.3.0`, verified 2026-07-23, updated 2026-07-26; `75e238890215cbc02c3bc59cdaaeb43f467ae7d512e9b5a9c4723ccc0c4580f8` |
| `Other_high_value_information.md` | Identity, contact and other approved supporting facts | content `2.3.0`, verified 2026-07-23, updated 2026-07-26; `58a8f88f9eb627847152d684b19d7938c42da7d173a57a7fff58728a25ae5bf8` |
| `CV_BASELINE.md` | Derived stable CV chronology/rendering baseline; never permitted to supersede the three authorities | baseline `0.7.0`, verified 2026-07-31 |
| Vacancy material | Employer, role, requirement and channel facts; never candidate-fact authority | Per-run input |
| Language/persuasion/reference context | Advisory only; cannot create candidate facts | Versioned runtime context |

Historical master hashes were `CV_MASTER.docx` = `c3809748fe26dd5a7ae0a146d940a15e1b3326036ae5f7fac9fd2be02292e8c5` and `APPLICATION_MASTER.docx` = `dfd24125f921863da23932b8be3255df51cc8a4ee9a97c6a602a33dedb241409`.

These versions/hashes identify the audited P0.7 assets. The Step-2 builder must recompute hashes on the actual supplied files and treat any difference as a review event, not silently assume equivalence. The underlying hash/version pattern should be adapted into the fresh P0.9 freeze rather than discarded.

### 1.4 Implemented artifact and schema concepts

The exact P0.7 repository should be inspected during Step 2, but the corpus supports the following active artifact families:

- normalized job identity and vacancy objects;
- cluster-level evidence/strategy material;
- draft package output;
- final package output;
- private review/status output;
- expected/completed job sets;
- candidate baseline and employment IDs;
- Word masters and rendered job deliverables;
- batch-level reports.

The final package schema represented:

```text
job/batch/cluster identity
candidate-facing CV content
  profile
  competencies
  employment overrides
  education/other sections through baseline merge
application
  null OR opening + body paragraphs + closing
portal_answers[]
  question_id
  question
  answer
  optional max_words/max_chars
private review/status metadata
```

Historical P0.7 contract details worth preserving for migration/test comparison—not as automatic P0.9 requirements—include:

| Contract element | P0.7 rule |
|---|---|
| `contract_version` | constant `0.7` |
| `source_stage` | `STAGE3_DRAFT` or `STAGE4_FINAL` |
| Job identity | `job_id`, `batch_id`, macro/mini cluster IDs, employer, title, language, `letter_required`; optional unit/reference |
| Language | `nb-NO` |
| Profile | schema length 80–1400 |
| Competencies | 4–8 unique items |
| Employment overrides | 1–4, known uppercase baseline employment IDs only |
| Bullets per override | 1–5 |
| Application | opening + 1–5 body paragraphs + closing, or `null` when no letter required |
| Portal answers | maximum 20; exact question ID/text/answer plus word/character limits |
| Additional fields | unknown top-level or nested fields rejected |
| Historical ID shapes | `B[0-9]{2}`, macro/minicluster/job-derived patterns |

A concrete quality omission was the absence of an explicit vacancy-specific `headline` or candidate-identity field. The renderer inferred identity from competencies, contributing to generic positioning. P0.8 corrected this and P0.9 should retain the explicit field.

### 1.5 Implemented scripts

#### `ingest.py`

The ingest layer created deterministic job identity/path objects from approved vacancy inputs and prepared the initial runtime. Its reusable responsibilities include:

- reject malformed or unsupported input;
- create stable job IDs and safe paths;
- preserve vacancy content;
- establish expected jobs;
- prevent cross-job identity drift;
- create the file/runtime structure used by semantic stages.

P0.9 should reuse the proven ideas, not necessarily the exact script. The new ingest must support the final run manifest, canonical vacancy preservation, frozen sources and any simplified product/channel contract selected by Step 1.

#### `advance.ps1`

The PowerShell script moved jobs/artifacts between physical stages and enforced some sentinel checks. It is not a strong P0.9 reuse candidate because:

- two PowerShell-dependent tests remained skipped in the represented audit;
- physical movement is coupled to P0.7’s stage-centric topology;
- `_DONE`/review-state parsing proved weaker than intended;
- fresh P0.9 may be job-centric and Python-only.

Useful transition conditions should be rebuilt as explicit validator/state rules. The script itself should normally be retired.

#### `finalize.py`

The finalizer is the strongest reusable implementation substrate. Implemented responsibilities include:

- reconcile expected and completed jobs;
- cross-check job, batch, cluster, path, employer and title identity;
- verify baseline version;
- validate employment IDs;
- validate portal limits and application/no-letter contracts;
- scan for private leakage and unresolved placeholders;
- enforce historical page rules;
- merge dynamic CV material into the baseline;
- fill the original Word masters;
- convert to PDF;
- avoid overwriting existing outputs without `--force`;
- emit delivery/report artifacts.

P0.9 should not copy this file wholesale. It should extract and test the still-valid primitives—identity validation, full replacement merge, placeholder/leakage checks, rendering transaction, output isolation and targeted rerender—while deleting obsolete portal, page, state and topology assumptions.

### 1.6 Deterministic validation implemented in P0.7

The finalizer and tests prove that code can enforce important mechanical boundaries:

- exact identity agreement across artifacts;
- expected/completed set reconciliation;
- valid employment references;
- configured structural limits;
- required/forbidden fields;
- absence of internal/private markers in employer-facing text;
- absence of unresolved placeholders;
- no silent overwrite;
- render output existence and basic integrity.

They do **not** prove:

- factual truth of free prose;
- correct attribution of team versus personal contribution;
- optimal evidence selection;
- natural Norwegian tone;
- employer relevance;
- interview probability;
- whether a weak package deserves `CHECK` or `RERUN` without semantic judgment.

P0.9 should preserve this enforceability boundary explicitly.

---

## 2. P0.7 test and release evidence

### 2.1 Test state

| Evidence area | State | What is supported | What is not supported |
|---|---|---|---|
| Release inventory | `MECHANICALLY_TESTED` | Expected 52-file package and repository shape were inspected | No claim that every historical file remains useful |
| Python unit/integration tests | `MECHANICALLY_TESTED` | 32/34 tests passed in the represented rerun | Skipped PowerShell paths were not proven |
| Ingest/identity | `MECHANICALLY_TESTED` | Stable IDs, paths and malformed-input controls were exercised | Real heterogeneous vacancy inventory not demonstrated |
| Stage isolation | `MECHANICALLY_TESTED` in fixtures | Directory/artifact separation and expected contracts existed | No proof against all model-generated malformed variants |
| Schema/contract validation | `MECHANICALLY_TESTED` | Representative valid/invalid fixtures were checked | Manual chat outputs are not guaranteed schema-valid before local validation |
| CV merge | `MECHANICALLY_TESTED` | Dynamic content merged into stable baseline with employment-ID checks | P0.8.1 full-array replacement semantics must be explicitly reimplemented/verified |
| DOCX generation | `MECHANICALLY_TESTED` | Controlled fixture documents were created from actual masters | Target Windows fonts/Word/portal parsing remain open |
| PDF conversion | `MECHANICALLY_TESTED` in represented environment | Controlled conversion produced openable outputs | Headless LibreOffice is not installed/proven on the current target machine |
| Page/layout | `MECHANICALLY_TESTED` and visually sampled | Five DOCX-rendered pages and five finalizer-PDF pages were inspected; A4/no clipping, blank error pages, tags or private flags were reported; sparse CV page imbalance was observed | No broad dense/sparse real-package visual QA |
| Real semantic pipeline | `NOT PRODUCTION-MODEL_TESTED` | None | No real intended-model batch, quality distribution, human edit time or interview outcomes |

### 2.2 Known P0.7 defects with implementation consequences

#### Mutable draft-reference integrity bypass

Stage 4 could mutate the draft/reference against which its own final output was compared. This weakens any claim that equality or integrity checks protected upstream state. P0.9 must identify immutable factual inputs separately from mutable strategy/draft artifacts; final refs must be synchronized to the final package rather than proven by comparison to a mutable copy.

#### Completion theatre

`_DONE.md` and review-heading parsing could accept substrings without proving the intended contract. P0.9 completion must be derived from canonical artifact validation, not human-readable markers.

#### Duplicate portal identifiers

The finalizer could accept duplicate portal question IDs. If portal remains anywhere in the architecture, question identity must be unique and exact. If portal is detached, this defect should not justify retaining the full core portal state surface.

#### No target-scale stress proof

The represented tests did not prove the nominal 20-job/10-job cluster volumes with real model outputs. P0.9 cluster size and long-chat behavior remain pilot variables.

#### PowerShell gaps

Two tests were skipped because PowerShell was unavailable. Since P0.9 can be Python-first and fresh, the default response is to remove the dependency rather than recreate an unverified transition layer.

#### Sparse CV page balance

The rendered sparse CV showed weak page balance. This is product evidence, not only test polish. The template adaptation must include sparse, normal and dense fixtures and human visual review.

#### Missing explicit headline

P0.7 lacked an explicit candidate identity/headline. This should be a first-class field from Stage 1 through final rendering.

---

## 3. Concrete Word/document implementation evidence

### 3.1 CV master

Direct inspection represented in SRC-19 found:

- 17 Word content controls (`w:sdt`);
- zero data-bound content controls;
- zero tables;
- zero text boxes;
- zero drawings;
- one document section;
- candidate name and “CV” in the header;
- otherwise a linear main-text flow.

### 3.2 Application master

The represented inspection found:

- 7 SDT instances across 6 unique tags;
- zero data-bound controls;
- two tables;
- zero text boxes;
- zero drawings;
- contact information in the header.

### 3.3 Fill/unwrap/render method

P0.7 did not depend on LibreOffice interpreting data-bound Word controls. Its finalizer:

1. located and filled the expected OOXML SDTs;
2. unwrapped content controls;
3. validated that no `w:sdt` remained;
4. generated the final DOCX;
5. converted the result to PDF;
6. checked expected output existence/integrity.

This materially qualifies generic warnings that “content controls are unsafe.” The actual controls were non-data-bound and removed before conversion. The correct P0.9 response is neither blind reuse nor blanket rejection:

- inspect the exact masters and tag map;
- preserve or simplify the working fill/unwrap method;
- fail if unknown/duplicate/missing controls violate the template contract;
- ensure no transient controls/placeholders remain;
- verify target-machine rendering and extractability;
- specifically test whether critical identity/contact content in headers is available to intended application channels.

### 3.4 DOCX/PDF output contract

The intended implementation should preserve both:

- DOCX as editable/auditable output and master-derived artifact;
- PDF as stable submission/rendering output where the vacancy/channel accepts or prefers it.

Neither format should be assumed universally accepted. Per-vacancy channel facts remain authoritative. A downstream portal may consume plain text rather than either document.

### 3.5 LibreOffice transaction policy

The corpus supports a cautious policy:

- isolate the LibreOffice user profile per invocation;
- use absolute, correctly quoted paths;
- treat one job as the operational transaction;
- verify each document result independently;
- accept one invocation for both job documents only after target-Windows smoke evidence proves partial-success/failure behavior is observable;
- otherwise use one isolated invocation per document;
- never infer success solely from process exit—also verify expected file, nonzero size and openability;
- do not build a persistent daemon in P0.9.

The current target environment does not yet have headless LibreOffice proven. Ordinary DOCX→PDF capability is not equivalent evidence.

---

## 4. Reuse / adapt / rebuild / retire matrix

`Reuse` means the asset can plausibly survive after inspection. `Adapt` means preserve design/implementation capital but change contracts. `Rebuild` means recreate the capability against P0.9. `Retire` means do not carry it into the fresh runtime.

| Asset/mechanism | Reuse | Adapt | Rebuild | Retire | Reason / obligation |
|---|:---:|:---:|:---:|:---:|---|
| Three candidate authority files | ✓ |  |  |  | User-confirmed current factual authorities; preserve bytes unless separately maintained |
| `CV_BASELINE.md` content model |  | ✓ |  |  | Keep derived chronology role; review current facts and rendering split |
| P0.7 CV master |  | ✓ |  |  | Strong direct evidence; adapt headline/page balance/header parseability and final tag map |
| P0.7 application master |  | ✓ |  |  | Adapt to final product/channel contract; verify one-page behavior and header/contact handling |
| OOXML SDT fill/unwrap primitives | ✓ | ✓ |  |  | Working method; isolate into tested template functions and tighten map validation |
| `ingest.py` exact file |  | ✓ | ✓ |  | Reuse parsing/safe-ID ideas, rebuild around final manifest/product scope |
| `advance.ps1` |  |  |  | ✓ | Stage conveyor/sentinel topology is obsolete and partly untested |
| `finalize.py` exact file |  | ✓ | ✓ |  | Mine validated primitives; rewrite around P0.9 artifacts, statuses and targeted jobs |
| Identity/path sanitization | ✓ | ✓ |  |  | Preserve tested behavior; add traversal/symlink and Windows path cases |
| Expected/completed reconciliation | ✓ | ✓ |  |  | Core partial-success mechanism; source expected set from canonical run state |
| Candidate-source hashing | ✓ | ✓ |  |  | Preserve as run freeze; avoid redundant per-job copies unless blast radius requires them |
| P0.7 cluster model |  |  |  | ✓ | Macro/mini topology superseded |
| P0.8 ~5×8 clustering default |  | ✓ |  |  | Strong control; exact grouping/order represented in final run state and pilot metrics |
| Stage 1/2/3 prompts from P0.8 |  | ✓ |  |  | Last normative role contracts; rewrite to final P0.9 product/state/context decisions |
| `strategy.md` P0.8 contract |  | ✓ |  |  | Preserve semantic content, decide serialization and authority wording |
| P0.7/P0.8 package schemas |  | ✓ | ✓ |  | Mine field definitions; rebuild minimal final schema and avoid obsolete portal/state fields |
| Employment override ID checks | ✓ | ✓ |  |  | Add P0.8.1 full-array replacement semantics and deletion rules |
| Page hard gates |  | ✓ |  | ✓ as generic gate | Keep explicit external limits and usability failure; make normal page budgets warning/editorial controls |
| Leakage/placeholder scans | ✓ | ✓ |  |  | Strong mechanical defense; update prohibited tokens/paths and test false positives |
| `_DONE` and heading sentinels |  |  |  | ✓ | Replace with validated artifact state |
| `READY/CHECK/RERUN` |  | ✓ | ✓ |  | P0.8 design; implement action/repair-scope semantics and human queue |
| P0.8.1 snapshot/progress objects |  | ✓ |  |  | Consolidate only unique authority into final manifest/job state |
| Portal-in-core schemas |  |  | conditional | conditional | Build only if Step 1 keeps portal in core; otherwise retire and define downstream handoff |
| Deterministic evidence index |  |  | ✓ |  | Strong P0.9 candidate, not implemented; build minimal structural index only if frozen |
| Personality PF interface |  | ✓ | conditional |  | Optional experiment; source exists, exact runtime/default not adopted |
| Luna context preparation |  |  | conditional |  | No baseline dependency; bounded experiment only |
| P0.7 tests/fixtures | ✓ | ✓ |  |  | Preserve regression intent; update paths/contracts and remove obsolete expectations |
| P0.8 planned tests |  | ✓ | ✓ |  | Convert architecture requirements into executable tests only after Step-1 freeze |
| Historical repository tree |  |  |  | ✓ | Fresh runtime allowed/preferred; no compatibility requirement |

---

## 5. Target-environment questions for Step 2

These are empirical implementation questions, not architecture philosophy. They belong to `STEP2_VERIFY` unless Step 1 must pick a safe fallback.

### 5.1 Runtime and surface

- Which exact Work/Desktop/Codex surface will each stage use?
- Can that surface access the intended repository, run Python validators and repair artifacts in the same session?
- What permissions/approval mode are available?
- Does one selected session preserve enough state to process a cluster sequentially without hidden context truncation?
- What are the current model/effort labels and constraints? Treat these as volatile configuration.

### 5.2 Python and dependencies

- Supported Python version on the target machine.
- Availability/acceptable installation of `python-docx`, `lxml`, JSON Schema validator and PDF inspection libraries actually selected by the build.
- Whether dependency installation is permitted and reproducible.
- Unicode/path behavior for Norwegian characters and long Windows paths.
- Whether all scripts return nonzero on failure and emit actionable diagnostics.

### 5.3 Word/LibreOffice/fonts

- LibreOffice install path/version and `soffice --headless` behavior.
- Per-invocation profile isolation on Windows.
- One-document versus two-document conversion reliability and partial outputs.
- Installed fonts, substitutions and Norwegian glyphs.
- Word and LibreOffice visual parity for representative fixtures.
- PDF text extractability/selectability.
- Header/footer survival and ATS/channel parseability for critical identity/contact fields.

### 5.4 File-system controls

- Safe path-length budget.
- Symlink/reparse-point behavior.
- Atomic write/rename behavior on the selected local/OneDrive path if applicable.
- Backup/overwrite semantics.
- Whether generated and authority files can be permission-separated in practice.

### 5.5 Vacancy/channel reality

- Actual first-batch inventory and file formats.
- Portal/question shapes and limits.
- Whether any job is English, CV-only, portal-only or attachment-constrained.
- Whether employers accept PDF, require DOCX or require portal-entered structured CV.

Architecture should define how these facts are represented and enforced; Step 2 proves the concrete values.

---

## 6. Build obligations for the eventual Codex repository

### 6.1 Repository bootstrap

The builder must:

1. start from the final Step-1 normative P0.9 specification, not directly from this candidate package;
2. inspect the actual P0.7 release before copying code or templates;
3. create a fresh repository/tree unless Step 1 explicitly changes that rule;
4. copy candidate authorities as protected inputs without semantic rewriting;
5. establish a versioned baseline/template/context set;
6. document each reused legacy component and why it fits the final contract;
7. exclude historical material from active runtime unless explicitly referenced.

### 6.2 Canonical state and idempotency

For every command, the repository must define:

- authoritative inputs;
- generated outputs;
- stale/invalidation behavior;
- overwrite policy;
- idempotent rerun behavior;
- atomic write/rename where partial files would be harmful;
- error exit status and operator message;
- audit record sufficient to explain which sources/artifacts produced a deliverable.

A second run with unchanged inputs must either reproduce the same deterministic outputs or state clearly why semantic/model output is intentionally new. No command may silently fall back to stale output.

**Public command surface.** Keep the operator-facing CLI small and task-oriented. P0.8.1's useful principle was “two operator commands, narrow internal modules”: avoid both script sprawl and an artificial monolith. The exact final count follows the Step-1 state/product contract, but ordinary operation should expose only obvious commands or subcommands for intake/freeze, validation/finalization/rendering and narrowly targeted job repair. Internal Python modules are appropriate when they have real reuse or isolate a tested boundary; wrappers with one trivial caller are not.

### 6.3 Ingest and freeze

The implementation must prove:

- every approved vacancy receives one stable unique job ID;
- filenames/paths are sanitized without collisions;
- original vacancy content is retained;
- derived/normalized views are visibly derived;
- expected jobs and human cluster/order are frozen in canonical state;
- candidate/source/template versions or hashes are recorded at appropriate granularity;
- unapproved files cannot silently enter the run;
- duplicate vacancy/job identities fail loudly.

### 6.4 Stage artifact contracts

For each stage:

- one documented input contract;
- one canonical output contract;
- explicit factual and strategic authority statement;
- local validator command;
- success only after validation;
- bounded same-session repair if adopted;
- no implicit cross-job carryover;
- no employer-facing output containing private notes, source IDs or control data.

Manual chat output must never be assumed schema-valid merely because the prompt requested JSON or headings.

### 6.5 Dynamic CV merge

The builder must implement and test:

- explicit headline/profile/competency dynamic zones;
- stable baseline chronology;
- employment ID uniqueness;
- full bullet-array replacement for an overridden employment;
- no positional/partial merge ambiguity;
- no deletion/addition of employment identities through model output;
- no unsupported formal title/date/degree/result mutation;
- deterministic final order and formatting;
- sparse/normal/dense page behavior.

### 6.6 Package and final evidence synchronization

The final package must be the source for final evidence references. When Final Sol changes an argument or evidence item:

- final refs must change with it;
- stale Stage-1 refs must not survive as audit truth;
- every employer-facing factual proposition should be traceable to candidate/vacancy authority at the appropriate granularity;
- absence of a reference must fail where the final contract requires one;
- references remain private/internal.

### 6.7 Partial success and targeted operation

The repository must support:

- one job completing independently;
- failed jobs remaining visibly failed/stale;
- already valid jobs remaining deliverable;
- targeted validation/finalization/rendering by `job_id` or equivalent selector;
- a pure rerender that preserves the frozen document date and semantic package content;
- RERUN without rebuilding unrelated jobs;
- no accidental overwrite of human-edited final deliverables;
- a human queue showing actionable state and reason.

### 6.8 Rendering and document validation

Before a job is marked render-complete, verify at minimum:

- expected DOCX/PDF exists;
- file is non-empty and openable;
- no unresolved placeholders or transient content controls remain;
- expected identity/title text appears;
- no private markers/paths/source IDs appear;
- conversion errors are absent;
- page warning/hard external limit is correctly classified;
- selected text is extractable where required.

Release/pilot evidence must include visual inspection of sparse, normal and dense CV/application fixtures and representative real outputs.

### 6.9 Security and permissions

The build must keep:

- vacancies/model output/personality/context prep in the data plane;
- instructions, permissions, authority, manifests and validation policy in the control plane;
- authority files protected from model-stage mutation;
- external network/actions absent unless explicitly approved;
- no submission/contact/profile update capability;
- path traversal, symlink/reparse and unsupported/oversized file checks;
- logs free of unnecessary personal data and secrets.

### 6.10 Test obligations

Tests should be tiered:

**Tier 1 — before semantic pilot**

- source authority/freeze;
- identity/path collisions;
- schema validation;
- expected-set reconciliation;
- cross-job leakage;
- employment replacement semantics;
- final evidence synchronization;
- placeholder/private-token scanning;
- targeted rerun/render;
- partial success;
- actual master fill/unwrap;
- target-machine render smoke.

**Tier 2 — before first full batch**

- malformed model outputs and bounded repair;
- sparse/normal/dense rendering;
- long paths/Norwegian characters;
- interrupted/partial writes;
- repeated/idempotent commands;
- source/template invalidation;
- cluster start/middle/end position logging;
- review queue and delivery classification.

**Tier 3 — release/polish**

- detailed reporting;
- optional feature toggles;
- noncritical format variants;
- performance tuning based on measured bottlenecks;
- historical compatibility only if explicitly required.

Tests must demonstrate actual output, not only that code imports. Silent or expensive failure modes require adversarial fixtures.

---

## 7. Evidence the builder must produce

The Step-2 implementation is not complete until it can supply:

| Evidence | Minimum proof |
|---|---|
| Repository inventory | Expected active files, no unexplained historical runtime paths |
| Source protection | Hash/version snapshot and failed mutation fixture |
| Ingest | Realistic multi-job sample with stable IDs and collision/error cases |
| Validators | Valid and adversarial invalid stage artifacts with explicit diagnostics |
| CV merge | Exact before/after employment arrays and final rendered order |
| Final refs | Deliberate Stage-3 evidence change followed by synchronized final refs |
| Partial success | One failing job while other jobs finalize and remain untouched |
| Targeted rerender | One job rebuilt without changing unrelated output hashes |
| Word generation | Actual master filled with no residual controls/placeholders |
| PDF conversion | Target-machine command, outputs, exit/error capture and file checks |
| Visual QA | Rendered sparse/normal/dense pages inspected for clipping, balance and glyphs |
| Security | Traversal/symlink/private leakage/control-plane injection cases rejected |
| Operator flow | A clean run from approved vacancy to reviewable package using documented commands |
| Pilot readiness | Stage prompts, human score rubric, time logging and rollback path |

A builder report should separately label `DESIGNED`, `IMPLEMENTED`, `MECHANICALLY_TESTED` and `PRODUCTION-MODEL_TESTED`. “Implemented” without evidence should not be accepted.

---

## 8. What Step 2 must not decide silently

The builder may choose ordinary code-level implementations within the final spec. It may not silently decide:

- whether portal belongs in the core product;
- whether v1 is Bokmål-only;
- whether strategy is Markdown, JSON or another canonical form;
- which runtime/state object is authoritative;
- whether deterministic indexing is mandatory;
- whether personality is enabled or what its default is;
- whether Luna is used;
- whether Priority A/B changes model treatment;
- the exact semantic power of Final Sol;
- the product meaning of `READY/CHECK/RERUN`;
- any candidate claim or source authority change.

Those are Step-1 decisions or explicitly bounded Step-3 experiments. If the final architecture leaves a parameter configurable, the builder should implement the smallest observable configuration surface rather than substitute personal preference.

---

## 9. Build stopping rule

The repository is ready for the first semantic pilot when:

1. all hard source, identity, isolation, merge, leakage and render contracts have executable evidence;
2. every core command fails loudly, is rerunnable and has a documented authoritative input/output set;
3. one complete mechanical vertical slice succeeds on the target machine with real masters;
4. partial success and targeted repair are demonstrated;
5. all unresolved semantic enhancers remain optional or absent;
6. the operator can run the baseline without understanding historical P0.7/P0.8 internals;
7. no design choice in the resolution queue has been invented by the builder.

Do not delay the pilot to build deferred infrastructure. Conversely, do not call the system production-ready on the strength of fixtures alone: real vacancy/model outputs and human review are the next evidence layer.
