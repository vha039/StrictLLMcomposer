# Canonical Conversation KB

## 0 Context Capsule

### 0.1 Primary purpose

The conversation develops, implements, audits, and repeatedly simplifies **Jobbsøk_26**, a Norwegian job-application production framework for Vegard Håland. The system is intended to convert human-approved Norwegian vacancy material plus authoritative candidate facts into complete, vacancy-specific, persuasive and manually submittable application packages: targeted CV, application letter when appropriate, portal answers, private review notes, and rendered DOCX/PDF.

### 0.2 Latest authoritative state

| Item | Current state | Status | Provenance |
|---|---|---|---|
| Implemented repository | `Jobbsok_26_P0.7_Release.zip` exists and was independently audited. | CURRENT | Chat-contained release artifact + assistant audit |
| Implemented architecture | Four manual stages; Terra→Sol→Terra→Sol; 2×~20 macroclusters; 4×~10 miniclusters; three deterministic scripts. | CURRENT implementation | P0.7 release files |
| Primary optimization objective | Maximize the **median package quality** and the **mean quality of the strongest 80%**; do not spend disproportionate complexity making the weakest 20% uniform. | DECIDED | Latest explicit user correction |
| Quality philosophy | Strong bias toward best possible HappyPath output; weak packages may be rerun outside the main framework. Manual review is accepted; extensive rewriting is a system failure. | DECIDED | User |
| Proposed successor design | A simpler three-stage “Selective Quality MVP”: Sol Max strategy, Terra Max writing, Sol Max final writing/triage; ~4 clusters of 8–10; two scripts; no macro→mini split. | PROPOSED, not adopted or implemented | Assistant response to latest redesign request |
| P0.7.1 reliability hardening | A detailed audit identified real mechanical issues, but the user subsequently changed the optimization objective. Some reliability patches remain valuable; several strict gates are now lower priority or contrary to quality-first operation. | PARTIALLY SUPERSEDED / OPEN | Assistant audit + user correction |
| Submission | Always manual; system must never submit, publish, contact employers, or alter external profiles. | CURRENT / DECIDED | User and all adopted specifications |

### 0.3 Central design trajectory

```text
P0.5.3 API-driven compiler
→ P0.5.3 four-call application compiler
→ Codex-native/manual four-stage architecture
→ P0.6 physical stage isolation and 4×10 / 8×5 clustering
→ P0.7 hybrid Terra/Sol routing and 2×20 / 4×10 clustering
→ P0.7 release audit
→ user-defined selective-quality objective
→ proposed P0.8 three-stage Selective Quality MVP
```

### 0.4 Hard constraints

- Candidate facts are source-governed; formal titles, dates, degrees, institutions, numbers, mandates, personnel responsibility, outcomes, implementation status, and lifecycle must not be invented.
- Strong synthesis, functional equivalence, employer-value framing, and persuasive wording are allowed when interview-defensible.
- Norwegian application quality is not an afterthought: natural Bokmål, restrained confidence, employer relevance, evidence-first persuasion, Jante calibration without underselling, and calm professional weight are core requirements.
- The framework is MVP-KISS: no API/SDK model orchestrator, database, vector store, semantic cache, custom agents, subagents, automated retries, automated employer research, or automated submission unless a future observed problem justifies them.
- Model work is manually initiated in ChatGPT Work/Codex-style stage chats; local scripts perform deterministic ingest, movement/validation, merging, rendering, and batch reporting only.
- The current user preference explicitly favors high top-80% package quality over uniform tail reliability.

### 0.5 Immediate open loops

1. Decide whether to adopt the proposed three-stage Selective Quality architecture as the next target release.
2. If adopted, define its final specification and migration plan from P0.7.
3. Preserve useful P0.7 assets: candidate authorities, baseline, templates, schema foundation, job identity, dynamic CV merge, Norwegian persuasion core, per-job rendering, no-submit boundary.
4. Run a real pilot; no real Terra/Sol vacancy batch has yet been verified in the available release evidence.
5. Determine practical cluster size and effort routing from measured package quality, human edit time, and credits—not architecture intuition alone.
6. Improve explicit CV headline and page balance; both are direct output-quality issues.
7. Replace “uniform batch completion” logic with selective delivery/triage if the quality-first design is adopted.

---

## 1 Scope/Reliability

### 1.1 Accessible corpus

The accessible corpus contains:

- the visible Jobbsøk_26 conversation trajectory, including user corrections, architecture requests, implementation prompts, audits, and redesign requests;
- 36 imported conversation files, including deep-research reports, Norwegian writing/recruitment guides, P0.5.3/P0.6/P0.7 release ZIPs, manifests, test reports, implementation reports, decision logs, and implementation prompts;
- extracted contents of the P0.5.3, P0.6, and P0.7 ZIPs;
- chat-contained summaries of generated artifacts that are not separately mounted;
- tool-reported test, ZIP-integrity, rendering, and audit results.

### 1.2 Reliability levels

| Corpus area | Coverage | Confidence | Basis |
|---|---|---:|---|
| Current user objective and priorities | Complete | High | Explicit latest user statements |
| P0.7 repository structure and implementation | Complete for active files | High | Release ZIP extracted and inspected |
| P0.7 automated test evidence | Complete for available report + independent rerun described in chat | High | Test report and audit outputs |
| P0.7 visual-quality observations | Substantial | Medium-high | Audit rendered and inspected fixtures; exact images are not embedded in this KB |
| P0.6 repository and reports | Substantial | High | Release ZIP and reports available |
| P0.5.3 release history | Substantial | High | Release ZIP, reports, manifests and research files available |
| Full original wording of every skipped chat turn | Inaccessible | Low | Transcript contains many `Skipped N messages` placeholders |
| Full source register for earlier web research | Partial | Medium | Conclusions and citations appeared in prior assistant outputs; complete search result bodies are not preserved here |
| Generated `jobbsøk_26_P0.7.md`, implementation prompt, and audit Markdown | Partial | Medium-high | Their major contents are represented in assistant messages; some generated file bodies are not mounted in the current file list |

### 1.3 Interpretation rule

Current authoritative state leads. Historical architecture is retained only when it explains a decision, exposes a failure, preserves reusable implementation, or identifies a superseded constraint.

---

## 2 Domain Map

1. **Jobbsøk_26 product objective and optimization doctrine**
2. **Candidate authority and truth architecture**
3. **Norwegian recruitment, persuasion, language and document doctrine**
4. **P0.5.3 API/compiler lineage**
5. **Codex-native/manual stage transition**
6. **P0.6 physical stage architecture**
7. **P0.7 hybrid-model implementation**
8. **P0.7 release verification and critical audit**
9. **Selective-quality objective and revised QA philosophy**
10. **Proposed P0.8 Selective Quality MVP**
11. **Model selection, reasoning effort and credit allocation**
12. **Cluster, batch and context design**
13. **Stage contracts and artifacts**
14. **Deterministic scripts, rendering and operator workflow**
15. **Testing, pilot design and evaluation metrics**
16. **Deferred architecture and revisit triggers**
17. **User operating profile**
18. **Decision, artifact, open-risk and coverage registers**

---

## 3 Jobbsøk_26 Product Objective and Optimization Doctrine

### 3.1 Current objective

**Status: DECIDED. Provenance: user.**

The primary system objective is not perfect uniform quality across all jobs. It is to maximize quality where the workflow remains on its HappyPath:

```text
MAX{
  AVG(
    Median_package_quality,
    Mean_package_quality_top_80_percent
  )
}
```

Interpretation:

- the weakest 20% do not count toward the top-80 mean;
- the median prevents optimization for only a few standout packages;
- the architecture should aggressively improve the majority of packages;
- weak outliers may be taken through a separate manual or model-assisted round outside the main workflow;
- a framework that produces approximately 75% top-quality packages can still create enormous value even if the remainder requires extra handling.

### 3.2 Consequence for system design

**Status: DECIDED at principle level; implementation choices remain OPEN/PROPOSED.**

The system should prioritize:

1. employer-specific shortlist probability;
2. decisive evidence selection and strategic framing;
3. natural Norwegian persuasion;
4. coherent candidate identity;
5. complete and visually credible package;
6. low human rewrite burden for the majority;
7. cheap identification of weak-tail packages;
8. credit efficiency only after quality and human effort.

The system should not prioritize:

- equal quality across every job;
- extensive QA infrastructure aimed at rare tail failures;
- strict stage immutability when a later stronger model can materially improve the package using valid facts;
- global batch PASS as a proxy for useful output;
- defensive writing merely to make every package safe;
- heavy recovery/state machinery before a recurring real failure exists.

### 3.3 Cost hierarchy

**Status: CURRENT / DECIDED. Provenance: user.**

```text
Human effort
> Human complexity
> LLM complexity
> LLM effort / credit cost
```

Refined interpretation after the latest objective shift:

```text
Human rewriting burden
> Human operating complexity
> lost persuasion / strategy quality
> critical factual unusability
> implementation complexity
> model credit cost
```

### 3.4 HappyPath quality doctrine

**Status: DECIDED.**

- The framework must write strong packages; text quality is not delegated to the user.
- Vegard performs final semantic control and may tune claim strength downward.
- Starting slightly over-persuasive and calibrating downward was preferred over starting underpowered and never discovering the strongest stable level.
- Norwegian cultural calibration requires strong claims about actual work, not self-ranking, superlatives, inflated enthusiasm, or American confidence theatre.
- Missing or imperfect nonfatal fit should lead to strategic reframing, not automated semantic veto.

### 3.5 Recommended quality distribution logic

**Status: PROPOSED by assistant; not yet adopted.**

- `READY`: likely submit-ready after quick review.
- `CHECK`: one or a few bounded points require targeted verification.
- `RERUN`: complete package exists, but strategy or prose should receive a separate improvement round.
- All approved jobs receive a complete package.
- `RERUN` is not an automatic loop and does not consume the main workflow’s compute indefinitely.

---

## 4 Candidate Authority and Truth Architecture

### 4.1 Current source ownership

**Status: CURRENT / ADOPTED.**

The P0.7 release uses three complementary, byte-frozen candidate authorities:

| File | Authority domain | P0.7 SHA-256 |
|---|---|---|
| `context/Work_experience.md` | Employment, projects, work-derived competence, personal contribution, lifecycle, results and claim ceilings | `0b39a5105f0d809d1bc9a917665bc69c619eb059253a779079b37304b49a2f9d` |
| `context/Education.md` | Degrees, study status, academic subjects, education-derived competence and claim boundaries | `75e238890215cbc02c3bc59cdaaeb43f467ae7d512e9b5a9c4723ccc0c4580f8` |
| `context/Other_high_value_information.md` | Identity, contact, cross-file positioning, role routes, AI-enabled work framing, languages, trust roles, work style and unresolved register | `58a8f88f9eb627847152d684b19d7938c42da7d173a57a7fff58728a25ae5bf8` |

`CV_BASELINE.md` is a derived rendering baseline and never outranks the three authorities.

### 4.2 Core candidate identity

**Status: CURRENT factual/positioning state. Provenance: authority files.**

Vegard Håland is positioned as a cross-disciplinary analyst and adviser whose strongest repeatable pattern is:

```text
Understand
→ delimit
→ structure
→ build
→ control
→ improve
```

The strongest market identity is a **domain-heavy data-to-decision profile**, combining:

- hospital operations and public-sector context;
- economics, budgeting and management information;
- BI, data modeling, reporting and decision support;
- technical implementation and automation;
- process improvement, governance and stakeholder translation;
- AI-enabled work as a controlled delivery method, not a replacement identity.

### 4.3 Current employment and chronology

**Status: CURRENT factual state.**

- Employer: Oslo universitetssykehus HF.
- Formal title: `Rådgiver Økonomi og IKT`.
- OUS employment: March 2023–present.
- BAR operational placement: March–November 2023.
- Formal transfer to Analyseavdelingen: 1 June 2023.
- First operational day in Analyseavdelingen: 1 December 2023.
- Current unit: Direktørens stab – Analyseavdelingen.
- Core work domains: finance, staffing, activity/DRG, patient flow/capacity, management information, Power BI, Excel/VBA, SQL, R/Python as project-dependent tools.
- Participated in the four-person establishment group for Analyseavdelingen with the department head and two colleagues.

### 4.4 Current education

**Status: CURRENT factual state.**

- Universitetet i Agder: ongoing master programme in artificial intelligence, 2024–present.
- NTNU: completed master’s degree in economics, 2020–2022.
- Universitetet i Bergen: completed bachelor’s degree in economics, 2017–2020.
- Ernest Manning High School, Calgary: upper-secondary education, science and advanced mathematics, 2011–2013; not included by default in CV.

### 4.5 Stable CV chronology

**Status: CURRENT / IMPLEMENTED in `CV_BASELINE.md@0.7.0`.**

Employment IDs:

- `EMP_OUS_ANALYSE`
- `EMP_OUS_BAR`
- `EMP_TKS_HEIS`
- `EMP_AHLSELL`
- `EMP_LUFTFORSVARET`
- `EMP_SECTOR_ALARM`

Education IDs:

- `EDU_UIA_AI`
- `EDU_NTNU_ECON`
- `EDU_UIB_ECON`
- `EDU_CALGARY`

The baseline also preserves:

- Norwegian as mother tongue;
- fluent written and spoken English;
- student-housing board roles from 2017–2020;
- Sanitet nivå 2 course, April 2014;
- references available on request.

### 4.6 Highest-value evidence routes

**Status: CURRENT factual/strategic source material.**

| Project/evidence | Core value |
|---|---|
| `PRJ-01` | Greenfield management BI in hospital; semantic model, ETL/Power Query, DAX, backend architecture, decision support |
| `PRJ-02` | Cross-organizational Power BI and semantic-model competence transfer |
| `PRJ-03` | Modernization of an approximately 20-year-old hospital budgeting tool; major code contribution; used in 2026 budget process |
| `PRJ-04` | Hospital-wide benefits-realization framework; four-person revision; lasting common method |
| `PRJ-05` | Forecasting repository for patient volume, beds and capacity; architecture, orchestration, automation and integration |
| `PRJ-06` | Investment support with transparent weighted proxy when direct allocation data was unavailable |
| `PRJ-07` | Platform pilots and modernization mapping, including adjacent Microsoft Fabric exploration |
| `PRJ-08` | Delivery model, team design, agile structuring and functional/technical coordination |
| `PRJ-09` | Intake, requirements and collaboration tooling |
| `PRJ-10` | BAR section-level DRG forecasts using Stata/R/Power Query; actual planning deliverables |
| BAR operational work | Month-end close flow, periodization, reversals, reconciliation, quality control, management reporting, ERP transition and Excel/VBA conversion tooling |

### 4.7 Claim boundaries

**Status: CURRENT / HARD.**

Do not upgrade evidence into unsupported claims of:

- formal personnel responsibility;
- enterprise architect ownership;
- formal project-manager title unless explicitly documented;
- full solo authorship of team or AI-assisted artifacts;
- production deployment when only pilot/development exists;
- quantified gains without verified measurement;
- deep production ownership of enterprise data platforms, cloud engineering or deployed ML/LLM systems;
- enterprise AI governance authority;
- organization-wide AI transformation leadership.

### 4.8 AI-positioning hierarchy

**Status: CURRENT / ADOPTED.**

1. Business/domain value.
2. Analytical and technical delivery.
3. AI-enabled operating method.
4. Tools/products.

Preferred identity: adviser/analyst who uses generative AI and code agents as bounded tools for analysis, development, documentation and quality assurance, with explicit sources, requirements, tests, privacy awareness and human accountability.

Avoid leading with `prompt engineer`, generic `AI expert`, `LLM engineer`, or `AI architect` unless new evidence supports the title.

---

## 5 Norwegian Recruitment, Persuasion, Language and Document Doctrine

### 5.1 Current writing objective

**Status: CURRENT / ADOPTED.**

Write direct, sober, precise, evidence-led and professionally Norwegian Bokmål. The text should sound like a credible Norwegian applicant, not translated management English or American self-branding.

### 5.2 Target voice

- calm and confident without bravado;
- dense but readable;
- specific about problem, contribution, method and boundaries;
- active when personal contribution is supported;
- collective where work was shared;
- candid about gaps without defensive framing;
- pragmatic and decision-oriented.

### 5.3 Core persuasion model

**Status: ADOPTED conceptually; exact enforcement evolved across versions.**

The strongest application package uses one shared backbone:

```text
Chosen candidate identity
+ employer decision problem
+ two strongest evidence bridges
+ at most one controlled differentiator
```

Important principles:

- specialist perception wins first-pass screening;
- supported breadth builds second-pass confidence;
- do not present a 33/33/33 hybrid of BI, process, finance, AI or project identities;
- broad competence should reinforce one primary professional pattern;
- the application is a decision-shaping instrument, not a symmetric checklist;
- approximately 70–85% of application argument weight may be allocated to the two strongest direct-fit evidence bridges when appropriate;
- CV handles breadth, chronology, screening facts and scan-level proof;
- application explains role interpretation, employer relevance, motivation and connected evidence;
- portal answers answer the exact question and limit directly.

### 5.4 Vinklings-Matrisen

**Status: ADOPTED as high-value persuasion mechanism.**

Every selected raw fact should be transformed through:

```text
Raw fact
→ employer’s latent need/fear
→ strategic angle
→ natural Bokmål sentence
```

Typical employer concerns:

- Does the candidate understand the real problem rather than only the requested artifact?
- Can the candidate deliver under operational, compatibility or governance constraints?
- Will the solution be used, understood and maintained?
- Can the candidate connect technical work to decisions or outcomes?
- Can the candidate reduce ambiguity, adoption risk, trust risk or continuity risk?

### 5.5 Jante calibration

**Status: DECIDED.**

- Make strong claims about documented work, responsibility and judgment.
- Avoid unsupported self-ranking, superlatives and performance theatre.
- Do not undersell real ownership merely to sound modest.
- Use scope, method, complexity and employer value to signal seniority.
- Functional leadership is allowed when supported by actions; formal line management is not implied.

### 5.6 Bokmål mechanics

- Use ordinary Norwegian word order.
- Put action in finite verbs.
- Keep actor, action and object visible.
- Prefer `analyserte`, `utformet`, `videreutviklet`, `automatiserte`, `kvalitetssikret`, `koordinerte`, `integrerte`, `forvaltet`, `formidlet` over noun-heavy constructions.
- Replace traits with evidence.
- Use direct openings.
- Motivation must be reasoned, not performed.
- CV and letter must complement rather than duplicate each other.
- Avoid generic AI-signature language and translated English-management rhythm.

### 5.7 Common avoid/review terms

Examples from the approved language core:

- `brenner for`
- `lidenskapelig opptatt av`
- `unik mulighet`
- `spennende reise`
- `fremoverlent`
- `resultatorientert`
- `dynamisk`
- `synergieffekter`
- `game changer`
- `revolusjonerende`
- generic `i skjæringspunktet mellom`
- unsupported `betydelige gevinster`
- unsupported `ledet`
- `jeg er overbevist om at`
- adjective triplets without evidence

These are review triggers, not blind bans when an employer term is exact and natural.

### 5.8 Document norms

**Status: CURRENT.**

- Conventional Norwegian CV structure and reverse chronology.
- Prefer one or two CV pages; P0.7 hard-coded maximum two pages.
- Prefer application no longer than one A4 page when a letter adds value.
- Produce only channels required or beneficial.
- Selectable text and simple reading order.
- Calm Scandinavian/editorial hierarchy.
- No default photo, age, birth date or street address.
- Avoid cyberpunk, neon, robot/brain imagery, radar charts, decorative skill bars and generic AI imagery.
- Preserve professional Word masters rather than silently replacing them with generic layouts.

---

## 6 P0.5.3 API/Compiler Lineage

### 6.1 Initial lean compiler concept

**Status: SUPERSEDED implementation lineage; some concepts retained.**

Early Phase 1 architecture used:

```text
vacancy ingest
→ Pydantic JobConfig
→ LLM compiler / CompiledJob
→ bounded LLM synthesis / GenerationPayload
→ deterministic checks
→ independent LLM QA / QAReport
→ docxtpl rendering
→ human release
```

The phase emphasized:

- one source-governed application compiler;
- explicit human `PRODUCE` gate;
- Structured Outputs/Pydantic;
- no custom XML/SDT parser;
- no local semantic rule engine;
- no Hydra, SAT solver, vector DB or event sourcing;
- LLM-owned semantic interpretation and writing;
- Python-owned exact mechanics.

### 6.2 P0.5.3 four-call release

**Status: SUPERSEDED by Codex-native direction; historically implemented and verified.**

Physical calls:

1. vacancy/hiring analysis;
2. evidence selection and package strategy;
3. complete native-Norwegian writer;
4. constructive Recruiter Mirror.

Key artifacts:

- `vacancy_hiring_model.json`
- `package_strategy.json`
- `draft_package.json`
- `final_package.json`
- `private_review_flags.json`

Notable decisions:

- semantic non-veto after human `PRODUCE`;
- complete CV rather than profile-only output;
- three complementary candidate authorities;
- original professional A4 masters;
- separate private review flags;
- exact source-ID membership;
- explicit `--resume` with fingerprint matching;
- no hidden semantic repair loop.

### 6.3 Verified P0.5.3 release evidence

- Release ZIP: `Jobbsok_26_P0.5.3_Codex_MVP_Release.zip`.
- SHA-256: `bd98fc1fac1124d5bca4b91f92417da54ddd810dd10de723f44bcd8c727a3ee6`.
- 55 members and 55 manifest entries; order matched; CRC valid; deterministic second build byte-identical; no hidden/cache members.
- 21/21 deterministic tests PASS.
- Offline four-call E2E PASS.
- Phase 0 smoke PASS.
- Strict schema conversion 5/5 PASS.
- Rendered DOCX/PDF visually inspected.
- No real approved vacancy/live model run was completed.

### 6.4 Why it was superseded

**Status: DECIDED historical shift.**

The user clarified that the target was not a Python/OpenAI API pipeline. The desired system was a **Codex-native/manual agent workflow** where a model with repository access reads project files and performs stage work inside the repository, while local code remains deterministic support.

---

## 7 Codex-Native / Manual Stage Transition

### 7.1 User’s architectural intent

**Status: DECIDED.**

A Codex/Work agent should:

- have full access to project files;
- receive a standardized user prompt;
- process batches of approved vacancy files from referenced folders;
- use repository-contained instructions, context, schemas and templates;
- write stage artifacts to filesystem;
- avoid project code that calls the OpenAI API for four responses.

### 7.2 Stage-isolation pitch

The user proposed a structure similar to:

```text
Root/
  Agents/
  context/
  stg1/
  stg2/
  stg3/
  stg4/
  output/
```

Intended benefits:

- physical separation of stage work;
- stage-local `AGENTS.md` overrides;
- only direct predecessor output enters the next stage;
- easier recovery after usage limits or errors;
- temporary artifacts remain in their stage/run location;
- reduced instruction leakage.

### 7.3 Deep-research architecture conclusions

**Status: historical research; partially superseded by later KISS decisions.**

Research reports supported:

- fresh stage/session or process boundaries;
- short root `AGENTS.md` and narrow local overrides;
- file-based handoffs;
- PyMuPDF-first PDF ingest;
- explicit schemas;
- static stage definitions separated from mutable run data;
- Windows/PowerShell local testing;
- careful handling of resume, CWD, sandbox and instruction loading.

The research also proposed more elaborate elements—session IDs, fingerprints, atomic writes, locks, hooks, Skills, subagents, workflow engines, state models—which the user later repeatedly cut from MVP scope.

---

## 8 P0.6 Physical Stage Architecture

### 8.1 P0.6 target

**Status: SUPERSEDED by P0.7 but directly relevant implementation base.**

P0.6 implemented:

- four manually started, physically isolated stages;
- four macroclusters of approximately 10 jobs in Stages 1–2;
- eight miniclusters of approximately 5 jobs in Stages 3–4;
- 24-prompt HappyPath;
- cluster-level retrieval and `CLUSTER_EVIDENCE_BASE.md`;
- individual `package_blueprint.md`;
- `MINICLUSTER_SPLIT.json`;
- dynamic CV overrides against `CV_BASELINE.md`;
- `ingest.py`, `advance.ps1`, `finalize.py`;
- `BATCH_STATUS.md`, `_DONE.md`, `BLOCKED.md`;
- Recruiter Mirror without semantic PASS/REVISE/BLOCK.

### 8.2 P0.6 release artifact

- Release ZIP: `Jobbsok_26_P0.6_Release.zip`.
- SHA-256 of accessible artifact: `6b40516a7fa40a07de09c8df20fa7087a1b48d02845f6a3448ea16733fc32a83`.
- Active scripts exactly:
  - `scripts/ingest.py`
  - `scripts/advance.ps1`
  - `scripts/finalize.py`

### 8.3 P0.6 retained strengths

- candidate authorities byte-preserved;
- professional Word masters retained;
- dynamic-only CV zones merged with full baseline;
- deterministic tools never start a model;
- no API runner or automated submission;
- four-stage cognitive separation;
- private review output;
- controlled stage fixtures and rendering tests.

### 8.4 P0.6 limitations that drove P0.7

- prompt count and human load were high;
- 5-job miniclusters were conservative;
- stage model routing was not optimized by model strengths/cost;
- P0.6 hardening issues included employment-override rendering, false global PASS risk, identity consistency, PowerShell gate robustness, ingest strictness, page budgets and runtime test coverage.

---

## 9 P0.7 Hybrid-Model Implementation

### 9.1 Current implemented architecture

**Status: CURRENT implementation.**

```text
Stage 1 — Vacancy Analysis
  GPT-5.6 Terra Max
  2 macroclusters × approximately 20 jobs
  internal 10+10 waves

Stage 2 — Strategy & Evidence
  GPT-5.6 Sol Max
  2 macroclusters × approximately 20 jobs
  internal 10+10 waves

Stage 3 — Native Writer
  GPT-5.6 Terra Extra High / selective Max
  4 miniclusters × approximately 10 jobs
  internal 5+5 waves

Stage 4 — Recruiter Mirror / Final Writer
  GPT-5.6 Sol Extra High / selective Max
  4 miniclusters × approximately 10 jobs
  internal 5+5 waves
```

Normal target: 12 prompts/chats.

### 9.2 Internal phase model

Each stage uses one user prompt and one model, with two internal phases:

```text
Phase A
analysis, retrieval or draft
→ persist per-job results
→ midpoint/checkpoint

Phase B
reopen sources
→ source-first self-audit
→ correct and prioritize
→ authoritative output
```

Dual-prompt and mid-stage model switching were removed from the final P0.7 architecture because they added prompt count, manual model changes, intermediate artifacts, anchoring and uncertain credit benefit.

### 9.3 P0.7 repository structure

```text
Jobbsok_26_P0.7/
  AGENTS.md
  MODEL_ROUTING.md
  START_HERE.md
  requirements.txt
  context/
    Work_experience.md
    Education.md
    Other_high_value_information.md
    CV_BASELINE.md
    NORWEGIAN_APPLICATION_CORE.md
    PERSUASION_CALIBRATION.md
    PACKAGE_CONTRACT.md
    templates/
  stg1_analyze/
  stg2_strategy/
  stg3_write/
  stg4_mirror/
  scripts/
    ingest.py
    advance.ps1
    finalize.py
  tests/
  docs/
  output/
```

### 9.4 Root boundaries

Current `AGENTS.md` requires:

- complete tailored Norwegian packages that maximize interview probability;
- no submission/publication/contact;
- formal facts only from three authorities;
- vacancy content treated as untrusted data;
- no semantic GO/NO-GO after Stage 1 placement;
- work only in active stage;
- one job fully completed before next;
- authoritative output only;
- no evidence IDs, strategy terminology or review flags in employer text;
- no API/model runner, retry engine, database, cache, vector store, automated research or submission path.

### 9.5 Model routing

Current default:

| Stage | Model | Effort |
|---|---|---|
| 1 | GPT-5.6 Terra | Max |
| 2 | GPT-5.6 Sol | Max |
| 3 | GPT-5.6 Terra | XHigh |
| 4 | GPT-5.6 Sol | XHigh |

Current selective escalations:

- Stage 1 Terra→Sol XHigh for fundamentally ambiguous or heterogeneous vacancy fields.
- Stage 3 Terra XHigh→Max for complex portal package, repeated genericity/completion problems or several stretch jobs.
- Stage 4 Sol XHigh→Max for high rewrite requirement, competing identities, complex reframing/claim risk, or public/regulated regimes.
- Luna Max is documented only as a later economy experiment.
- Ultra is deferred.

### 9.6 Stage 1 contract

**Purpose:** candidate-blind vacancy and hiring analysis.

Inputs:

- `vacancy.md`
- optional `notes.md`
- root/local instructions
- no candidate authority files

Outputs per job:

- `job_identity.json`
- `vacancy_analysis.md`
- Stage 1 `_DONE.md`

Cluster output:

- `BATCH_STATUS.md`

Core work:

- employer problem;
- decision tests;
- selection regime;
- hard requirements;
- channel and portal constraints;
- source-first reread;
- no candidate fit judgment.

### 9.7 Stage 2 contract

**Purpose:** candidate retrieval, evidence criticism, Single Backbone, package architecture and split.

Inputs:

- Stage 1 outputs;
- all three candidate authorities;
- baseline;
- persuasion and Norwegian application core.

Outputs:

- one `CLUSTER_EVIDENCE_BASE.md`;
- two evidence lanes;
- `MINICLUSTER_SPLIT.json`;
- one `package_blueprint.md` per job;
- per-job Stage 2 `_DONE.md`;
- `BATCH_STATUS.md`.

Core design:

- shared evidence universe, not shared application thesis;
- compact local evidence atoms;
- job matrix;
- primary candidate identity;
- two main evidence bridges;
- alternative route;
- channel allocation;
- evidence lock with targeted delta retrieval.

### 9.8 Stage 3 contract

**Purpose:** complete native Norwegian package draft.

Outputs:

- `draft_package.json`
- Stage 3 `_DONE.md`
- `BATCH_STATUS.md`

Dynamic package zones:

- profile;
- key competencies;
- selected employment bullet overrides;
- application;
- portal answers.

Stable formal CV history remains in `CV_BASELINE.md`.

### 9.9 Stage 4 contract

**Purpose:** independent final writer and constructive Recruiter Mirror.

Outputs:

- `final_package.json`
- `review_flags.md`
- Stage 4 `_DONE.md`
- `BATCH_STATUS.md`

Current P0.7 rules emphasize:

- first-20-seconds test;
- employer-swap test;
- candidate identity;
- evidence strength;
- natural Bokmål;
- calm professional weight;
- channel complementarity;
- `jeg`/`vi` calibration;
- no new facts;
- cross-job variation;
- no semantic PASS/REVISE/BLOCK verdict.

### 9.10 Dynamic CV merge

**Status: CURRENT / IMPLEMENTED.**

Finalizer combines:

```text
candidate header          ← CV_BASELINE
profile                   ← final package
key competencies          ← final package
employment identity       ← CV_BASELINE
employment period/order   ← CV_BASELINE
employment bullets        ← override if present, otherwise baseline
education                 ← CV_BASELINE
languages                 ← CV_BASELINE
other stable sections     ← CV_BASELINE
references                ← CV_BASELINE
```

This reduced model output volume and protects chronology/contact/education from truncation or hallucination.

### 9.11 P0.7 scripts

#### `ingest.py`

- validates batch/cluster/job IDs and prefixes;
- accepts meaningful `vacancy.md` or one `vacancy.pdf`;
- extracts PDF page by page via PyMuPDF;
- records SHA-256 and page markers;
- warns on legitimate short pages;
- blocks globally weak/scanned-like extraction;
- no OCR in MVP;
- no model calls.

#### `advance.ps1`

- validates Stage 2 completeness;
- reads split JSON;
- creates two Stage 3 miniclusters;
- copies clusterbase and job artifacts;
- excludes prior state markers;
- no model/state logic.

#### `finalize.py`

- reconciles expected Stage 4 input with completed output;
- validates package schema, identity, baseline and employment IDs;
- merges dynamic CV data with baseline;
- fills original Word masters;
- converts to PDF via LibreOffice;
- enforces page limits;
- keeps review flags private;
- writes terminal summary;
- does not create `FINALIZE_REPORT.md` or `output/INDEX.md`.

### 9.12 P0.7 release evidence

- Release ZIP: `Jobbsok_26_P0.7_Release.zip`.
- SHA-256: `c74565ceb32900beba4b912e1cec93abe68039f83a29da6952f7ad9f57feb1a8`.
- 52 files / 52 ZIP members; no duplicate members; valid CRC; common deterministic timestamp.
- Candidate and template assets byte-identical to frozen hashes.
- Automated suite: 34 tests; 32 PASS; 2 skipped/blocked because PowerShell unavailable; 0 FAIL.
- Controlled E2E fixture PASS.
- DOCX/PDF rendering PASS.
- Dense and sparse CV fixtures rendered to two pages; letter to one page.
- No real Terra/Sol production stages or real vacancy pilot run.

---

## 10 P0.7 Critical Audit

### 10.1 Audit verdict

**Status: CURRENT factual audit. Provenance: assistant independent release audit.**

P0.7 was judged a substantial, coherent and genuinely runnable implementation—not a façade or renamed P0.6 release. Architecture and MVP-KISS scope were strong. Production readiness was conditional.

### 10.2 Confirmed strengths

- four physical stages implemented;
- exactly three active scripts;
- source authorities and Word masters hash-frozen;
- strict package schema;
- `job_identity.json` integrated;
- older employment override rendering defect fixed;
- expected/completed reconciliation materially stronger;
- hard page budgets implemented;
- original-master DOCX/PDF rendering works;
- release is clean and deterministic;
- reports distinguish PASS/BLOCKED/NOT RUN honestly;
- no deferred orchestration infrastructure leaked into MVP.

### 10.3 Confirmed audit defects

#### A. Stage 4 mutable-draft integrity bypass

Current finalizer compares Stage 4 final output against a draft copy controlled by Stage 4 output, not necessarily the canonical Stage 3 input draft. The audit reproduced acceptance when both output draft and final package introduced a new employment ID.

Original audit recommendation: make Stage 3 input draft canonical or require exact equality.

Latest quality-first reinterpretation: strict “no new ID after Stage 3” may itself suppress quality. A future design should instead allow Stage 4 to use any baseline-known and source-supported employment ID, while recording a private strategy delta.

**Status:** defect factual finding CURRENT; remedy SUPERSEDED/OPEN.

#### B. `_DONE.md` token-search rather than structural parse

Required tokens could appear in prose and pass.

**Status:** factual finding CURRENT; hardening priority lowered after objective shift.

#### C. Review headings can be faked in prose

Heading strings were searched as substrings rather than exact Markdown headings.

**Status:** factual finding CURRENT; low direct package-quality value; DEFER candidate.

#### D. Duplicate portal question IDs accepted

Two identical `question_id` values could pass and render duplicate portal sections.

**Status:** CURRENT; cheap visible quality defect; still high-value fix.

#### E. Target-scale 20/10 topology not mechanically proven

Fixtures exercised 2 or 10 jobs, not a complete 20-job macrocluster and 10-job final batch.

**Status:** CURRENT evidence gap. Latest priority favors a real pilot over a large synthetic suite.

#### F. PowerShell runtime unverified

`advance.ps1` runtime tests were blocked in Linux because PowerShell was unavailable.

**Status:** CURRENT evidence gap for P0.7.

#### G. CV page balance weak

Technical rendering was clean, but both dense and sparse CVs used space conservatively; sparse CV was forced to two pages and page 2 had large unused space.

**Status:** CURRENT direct quality issue; high priority.

#### H. Candidate identity not explicit in final schema

CV functional headline was derived by joining the first three key competencies instead of using a dedicated candidate-identity/headline field.

**Status:** CURRENT direct quality issue; high priority.

#### I. Other medium findings

- runtime-dependent application date;
- generated DOCX metadata retained old 2013 timestamps;
- production input directories not fully git-ignored;
- normative P0.7 architecture not included in release ZIP;
- JSON-schema fallback could drift if new unsupported keywords appear;
- some baseline phrases duplicated in validator code;
- leak-check regex could cause false positives;
- force replacement had narrow rollback risk;
- Stage 3 docs and split-file behavior were inconsistent.

These are not currently top priority under the selective-quality objective unless they cause actual output or operator harm.

---

## 11 Selective-Quality Objective and Revised QA Philosophy

### 11.1 User correction

**Status: DECIDED. Provenance: user.**

The prior audit over-optimized for “secure everything, everywhere, always.” The user explicitly corrected the target:

- optimize the package-quality distribution, not worst-case uniformity;
- ignore the bottom 20% in the top-80 mean;
- permit a separate round for poor packages;
- accept that 75% excellent packages can create major workload savings;
- keep MVP-KISS and avoid QA infrastructure that competes with writing quality.

### 11.2 Revised hard/soft boundary

**Status: assistant proposal consistent with user objective; not formally adopted in code.**

#### Hard and cheap

- job identity must match;
- formal facts must be supported;
- employment IDs must exist in baseline;
- baseline must merge;
- required channels must exist;
- files must render/open;
- internal/private material must not leak;
- one bad job must not destroy good outputs.

#### Soft review triggers

- page overrun;
- high similarity;
- generic motivation;
- weak candidate identity;
- extensive Stage 4 rewrite;
- uncertain lifecycle wording;
- missing status metadata;
- strategy changed after Stage 2;
- review status `CHECK` or `RERUN`.

#### Not a production gate

- exact review-heading order;
- perfect `_DONE.md` syntax;
- equal bullet counts or section lengths;
- all jobs finishing in one batch;
- strict preservation of Stage 2 strategy;
- uniform package structure;
- metadata reproducibility.

### 11.3 Revised Stage 4 authority

**Status: PROPOSED; not implemented.**

Stage 4 should be allowed to:

- change candidate identity;
- change headline;
- replace main evidence;
- add another baseline-known employment route;
- restructure application and channels;
- conduct full rewrite;
- use targeted source verification.

Limits remain factual truth and interview defensibility.

### 11.4 Revised finalizer behavior

**Status: PROPOSED.**

Per-job output classes:

- `DELIVERED_READY`
- `DELIVERED_CHECK`
- `DELIVERED_RERUN`
- `FAILED`

Batch should preserve every usable package even if another job fails. Page-budget exceedance should normally produce a review classification, not discard otherwise strong output.

---

## 12 Proposed P0.8 Selective Quality MVP

### 12.1 Status and authority

**Status: PROPOSED. Provenance: assistant.**

The user asked for a from-scratch redesign. The assistant produced a high-level design, but the user did not explicitly adopt or implement it before requesting this KB.

### 12.2 Proposed architecture

```text
Stage 1 — Decision Architecture
  GPT-5.6 Sol Max
  candidate-blind vacancy understanding internally
  + candidate retrieval
  + evidence selection
  + package strategy

Stage 2 — Native Package Writer
  GPT-5.6 Terra Max
  complete package
  + quality-oriented self-edit

Stage 3 — Final Writer & Selective Review
  GPT-5.6 Sol Max
  independent strategic correction
  + final persuasion edit
  + READY/CHECK/RERUN

Finalizer
  deterministic truth checks
  + baseline merge
  + DOCX/PDF
  + partial success
```

### 12.3 Proposed cluster model

- approximately four strategy-coherent clusters;
- normal size 8–10 jobs;
- normal upper limit 12;
- same cluster follows through all three stages;
- no macrocluster/minicluster hierarchy;
- no `MINICLUSTER_SPLIT.json`;
- no evidence lanes;
- no `advance.ps1`;
- no 20→10 copy step.

Suggested cluster families, subject to actual portfolio:

- analytics, BI and decision support;
- process, project and improvement;
- digitalization, AI and business development;
- adjacent/stretch/mixed roles.

### 12.4 Proposed Stage 1 — Decision Architecture

One Sol Max chat per cluster.

Internal Phase A, before candidate facts:

- employer problem;
- decision tests;
- must-haves;
- selection regime;
- seniority interpretation;
- channel and limits;
- hiring-risk model.

Internal Phase B:

- retrieve candidate evidence;
- select primary identity;
- create explicit CV headline;
- choose shortlist thesis;
- choose two complementary evidence bridges;
- choose support evidence and alternative route;
- identify objection/reframe;
- allocate channels;
- classify compute/review route.

Proposed outputs:

- `cluster_strategy.md`
- per-job `job_identity.json`
- per-job `blueprint.md`

Proposed classification:

- `PRIME`
- `STANDARD`
- `MANUAL_LATER`

This is not GO/NO-GO; every job is produced.

### 12.5 Proposed Stage 2 — Native Package Writer

One Terra Max chat per cluster.

- process jobs in priority order: PRIME, STANDARD, MANUAL_LATER;
- write complete dynamic package JSON;
- use explicit headline;
- write CV profile, competencies, employment overrides, application and portal answers;
- quality-oriented self-edit rather than compliance-heavy audit;
- internally generate multiple headline/opening candidates only for PRIME jobs and retain the best one;
- perform short mechanical validation at end.

Output:

- per-job `draft_package.json`.

### 12.6 Proposed Stage 3 — Final Writer & Selective Review

One Sol Max chat per cluster.

- independently determine best end state before reading/editing draft;
- treat blueprint as strong hypothesis, not immutable contract;
- preserve good text;
- fully rewrite when needed;
- change identity/evidence/channel when source-supported;
- run first-20-seconds, employer-swap, Bokmål rhythm, `jeg`/`vi`, motivation and interview-hook checks;
- produce concise triage.

Outputs:

- `final_package.json`
- `review.json`

Proposed review schema:

```json
{
  "status": "READY | CHECK | RERUN",
  "confidence": "HIGH | MEDIUM | LOW",
  "reasons": ["maximum three short concrete reasons"]
}
```

### 12.7 Proposed repository simplification

```text
Jobbsok_26/
  AGENTS.md
  START_HERE.md
  requirements.txt
  context/
  stages/
    01_strategy/AGENTS.md
    02_write/AGENTS.md
    03_final/AGENTS.md
  schemas/
    package.schema.json
    job_identity.schema.json
    review.schema.json
  runs/
    <batch>/<cluster>/
      input/jobs/
      01_strategy/
      02_write/
      03_final/
      rendered/
  scripts/
    ingest.py
    finalize.py
```

### 12.8 Proposed script set

#### `ingest.py`

- validate IDs;
- normalize vacancy;
- create run structure;
- create/validate job identity;
- report mechanical unusability;
- no semantic decisions.

#### `finalize.py`

- validate only cheap hard boundaries;
- merge baseline;
- render original masters;
- preserve partial success;
- support targeted rerender:

```powershell
python scripts\finalize.py <cluster> --job <job_id> --force
```

### 12.9 Proposed removal from P0.7

- separate candidate-blind stage;
- 2×20/4×10 topology;
- evidence lanes;
- macro/minicluster IDs;
- `MINICLUSTER_SPLIT.json`;
- `advance.ps1`;
- strict batch gates;
- per-job `_DONE.md` as release proof;
- obligatory review headings;
- no-new-employment-ID after Stage 2/3;
- global PASS as primary production outcome;
- extensive synthetic uniformity testing.

### 12.10 Proposed retained P0.7 strengths

- candidate authorities;
- `CV_BASELINE.md`;
- original Word masters;
- dynamic CV merge;
- `job_identity.json`;
- package schema foundation;
- one job completed before next;
- internal Phase A/B;
- Norwegian persuasion core;
- portal limits;
- per-job transactional rendering;
- manual final approval;
- no API runner;
- no automated submission;
- no memory/cache;
- no agents/subagents.

---

## 13 Model Selection, Reasoning Effort and Credit Allocation

### 13.1 Current P0.7 routing

**Status: CURRENT implementation.**

- Stage 1: Terra Max.
- Stage 2: Sol Max.
- Stage 3: Terra XHigh, selective Max.
- Stage 4: Sol XHigh, selective Max.

### 13.2 Reported relative pricing

**Status: chat-reported current pricing; time-sensitive and requires re-verification before future execution.**

Relative rate card represented in the conversation:

| Model | Input credits/M | Cached input | Output credits/M | Relative to Sol |
|---|---:|---:|---:|---:|
| Luna | 25 | 2.5 | 150 | 0.20× |
| Terra | 62.5 | 6.25 | 375 | 0.50× |
| Sol | 125 | 12.5 | 750 | 1.00× |

### 13.3 Hybrid-model exploration

Historical exploration considered:

- Luna for coarse preparation;
- Terra for long-context retrieval because Luna reportedly lagged badly in long-context retrieval benchmarks;
- Sol for non-linear strategy, psychology and final wording;
- two prompts per stage in the same chat;
- `stgX-L` and `stgX-S`;
- Ultra effort for cheap Luna runs;
- larger clusters enabled by consistent high effort.

Final P0.7 rejected dual-prompt as default and selected single-prompt stages.

### 13.4 Quality-first compute allocation

**Status: PROPOSED.**

The latest objective implies effort should be allocated by expected marginal quality gain, not only by difficulty.

Possible classes:

- `PRIME_MAX`: clear evidence path and high potential for exceptional package; invest more compute.
- `STANDARD_XHIGH`: normal good route.
- `MANUAL_LATER`: complete standard pass, no automatic rescue loop.

The user has not yet adopted exact labels or routing.

### 13.5 Proposed P0.8 routing

- Stage 1 Sol Max.
- Stage 2 Terra Max.
- Stage 3 Sol Max.

Reasoning:

- eliminate separate Terra vacancy stage;
- concentrate Sol on decision architecture and final persuasion;
- use Terra Max for output-heavy drafting;
- establish quality baseline before testing lower efforts.

### 13.6 Required empirical decision rule

Model/effort changes should be evaluated by:

- median package quality;
- top-80 mean;
- submit-ready share;
- human edit minutes;
- credits per ready package;
- quality degradation by job order;
- actual Stage 3/4 rewrite value.

No final model/effort choice is empirically validated because no real batch has yet been run in the available evidence.

---

## 14 Cluster, Batch and Context Design

### 14.1 Historical topologies

| Version | Stage 1–2 | Stage 3–4 | Normal prompts | Status |
|---|---:|---:|---:|---|
| P0.6 | 4 macro × ~10 | 8 mini × ~5 | 24 | SUPERSEDED |
| P0.7 | 2 macro × ~20 | 4 mini × ~10 | 12 | CURRENT implementation |
| Proposed P0.8 | 4 clusters × ~8–10 through all stages | same clusters | 12 | PROPOSED |

### 14.2 Cluster purpose

The user’s cluster concept is not arbitrary batch partitioning. A cluster represents a role type so retrieval can be done once and the shared context reused across similar vacancies.

Benefits:

- fewer repeated searches;
- less context reloading;
- better cross-job evidence visibility;
- easier variation control;
- lower credit usage;
- more coherent batch strategy.

Risks:

- cluster homogenization;
- evidence-pair repetition;
- wrong shared identity;
- job-position effects in long runs;
- one heterogeneous job contaminating the shared strategy;
- late-job degradation.

### 14.3 P0.7 mitigations

- evidence lanes;
- 10+10 and 5+5 waves;
- midpoint reviews;
- one job completed before opening next;
- reopen source/blueprint per job;
- record used evidence pairs, candidate identities and repeated openings;
- split when more than three fundamentally different candidate identities are needed.

### 14.4 Proposed P0.8 simplification

- four coherent clusters rather than two large macroclusters;
- same cluster through all three stages;
- 8–10 normal size, 12 upper normal limit;
- cluster by employer problem, candidate identity, evidence pool, selection regime and channel;
- order PRIME before STANDARD before MANUAL_LATER;
- accept that weak late jobs may become RERUN rather than redesigning the entire batch.

### 14.5 Open cluster decision

**Status: OPEN.**

No real pilot has established whether 20-job, 10-job or 8–10-job clusters maximize the user’s quality objective. The next design should treat cluster size as an empirical parameter, not doctrine.

---

## 15 Stage Contracts and Artifact Model

### 15.1 P0.7 artifact chain

```text
vacancy.pdf / vacancy.md
→ job_identity.json
→ vacancy_analysis.md
→ CLUSTER_EVIDENCE_BASE.md
→ MINICLUSTER_SPLIT.json
→ package_blueprint.md
→ draft_package.json
→ final_package.json
→ review_flags.md
→ rendered DOCX/PDF
```

Supporting state:

- `BATCH_STATUS.md`
- `_DONE.md`
- `BLOCKED.md`

### 15.2 Artifact roles

| Artifact | Role | Current issue/value |
|---|---|---|
| `job_identity.json` | Cross-stage identity anchor | High-value; retain |
| `vacancy_analysis.md` | Candidate-blind employer decision model | Valuable cognition; separate file may be removable in P0.8 |
| `CLUSTER_EVIDENCE_BASE.md` | Shared source-grounded evidence universe | Strong in cluster architecture; may simplify to `cluster_strategy.md` |
| `MINICLUSTER_SPLIT.json` | Stage 2→3 split | Becomes unnecessary if one cluster topology is retained |
| `package_blueprint.md` | Per-job identity, thesis, evidence and channels | High-value; retain in simplified form |
| `draft_package.json` | Complete Writer output | Retain |
| `final_package.json` | Final employer-facing content object | Retain |
| `review_flags.md` | Private review guidance | Replace or simplify to `review.json` if selective triage adopted |
| `BATCH_STATUS.md` | Recovery and progress | Useful but should remain simple |
| `_DONE.md` | Completion marker | Low direct quality value; not worth heavy parser work absent failures |
| `BLOCKED.md` | Mechanical blocker explanation | Useful for job-local failure |

### 15.3 Package schema direction

Current schema supports:

- `source_stage`
- `job_id`
- `batch_id`
- `employer`
- `title`
- `baseline_version`
- dynamic CV profile;
- key competencies;
- employment overrides;
- application;
- portal answers.

High-value proposed addition:

```json
"headline": {
  "type": "string",
  "minLength": 15,
  "maxLength": 120
}
```

Rationale: connect Stage 2 candidate identity directly to the top CV signal rather than deriving the headline from three competency labels.

---

## 16 Deterministic Scripts, Rendering and Operator Workflow

### 16.1 Current operator boundary

**Status: CURRENT.**

- Model work happens manually in separate Work/Codex chats.
- Scripts never call models.
- User manually selects model and effort.
- Files are copied/split between stage folders.
- Final review and submission are manual.

### 16.2 Current P0.7 operator flow

1. Prepare 40 approved vacancies in two macroclusters.
2. Run `ingest.py`.
3. Run two Terra Max Stage 1 chats.
4. Copy Stage 1 output to Stage 2.
5. Run two Sol Max Stage 2 chats.
6. Run `advance.ps1` twice to create four miniclusters.
7. Run four Terra Stage 3 chats.
8. Copy Stage 3 output to Stage 4.
9. Run four Sol Stage 4 chats.
10. Run finalizer `--check-only` and render.
11. Manually review.

### 16.3 Recovery

Current recovery uses filesystem presence and status files rather than session orchestration.

Continuation prompt concept:

- continue same stage/cluster;
- preserve jobs with valid current-stage artifacts;
- complete remaining/incomplete jobs only;
- reopen each job’s inputs;
- update status;
- do not start next stage.

### 16.4 Proposed P0.8 operator flow

1. Ingest four clusters of 8–10 jobs.
2. Run four Sol Max strategy chats.
3. Run four Terra Max writer chats.
4. Run four Sol Max final chats.
5. Finalize all mechanically valid packages.
6. Review READY quickly, CHECK locally, RERUN separately.

Scripts reduced to:

- `ingest.py`
- `finalize.py`

### 16.5 Rendering design

**Status: CURRENT / STRONG.**

- original content-control Word masters preserved;
- full CV generated from static baseline plus dynamic zones;
- employer-facing text separated from private flags;
- DOCX and PDF generated;
- selectable PDF text checked;
- page size A4;
- no generic replacement template.

### 16.6 Rendering improvement priorities

**Status: OPEN / HIGH VALUE.**

- remove forced two-page sparse layout;
- let content flow naturally within maximum two pages;
- reduce excessive bold density in earlier employment;
- improve page utilization;
- preserve professional hierarchy;
- add explicit headline;
- treat page overrun as a review trigger if quality-first design is adopted rather than silently discarding good output.

---

## 17 Testing, Pilot Design and Evaluation Metrics

### 17.1 Historical test philosophy

P0.5.3–P0.7 emphasized:

- compile/import;
- source hashes;
- schema validation;
- positive/negative ingest;
- stage artifact contracts;
- finalizer identity, limits and leakage;
- controlled E2E fixtures;
- DOCX/PDF rendering;
- visual QA;
- deterministic release packaging.

### 17.2 Current evidence limitations

- no real approved vacancy completed through all P0.7 model stages;
- no real 20-job macrocluster run;
- no actual credit measurements;
- no measured human edit time;
- no measured job-order degradation;
- no empirical comparison of XHigh versus Max;
- no evidence that current review flags identify bottom-20 packages.

### 17.3 New primary eval

**Status: DECIDED at objective level; exact rubric PROPOSED.**

Suggested package score:

| Dimension | Suggested weight |
|---|---:|
| Expected interview effect | 40% |
| Strategy and evidence selection | 30% |
| Natural persuasive Norwegian | 20% |
| Channel/employer adaptation | 10% |

Then compute:

```text
Median package quality
Mean of strongest 80%
Q_happy = mean(median, top80_mean)
```

### 17.4 Secondary metrics

- submit-ready share;
- human minutes per ready package;
- credits per ready package;
- `TailRecall20`: share of human bottom-20 packages flagged CHECK/RERUN;
- review load: share sent to CHECK/RERUN;
- Stage 4 rewrite severity;
- evidence-route changes;
- factual corrections;
- package similarity;
- quality by job position/wave.

### 17.5 Recommended pilot sequence

**Status: PROPOSED.**

1. One real vacancy through full flow.
2. One complete 8–10-job cluster or, if P0.7 retained, one 20-job macrocluster.
3. Measure quality, credits and review time.
4. Compare early and late jobs.
5. Compare model efforts only after baseline.
6. Run remaining clusters only after the first cluster establishes acceptable quality.

### 17.6 A/B candidates

- Stage 1 Terra XHigh versus Max, judged on final packages.
- Stage 4 XHigh versus Max on PRIME jobs.
- strict blueprint preservation versus strategically free final writer.
- competency-derived headline versus explicit headline.
- P0.7 20/10 topology versus P0.8 8–10 stable clusters.
- hard page gate versus delivered-with-review.

---

## 18 Deferred Architecture and Revisit Triggers

### 18.1 Explicitly deferred

- API/SDK model orchestration;
- automatic `codex exec` runners;
- session ID and automatic resume;
- SQLite/database state;
- vector database or embeddings;
- role-archetype memory/cache;
- automatic context-pack compiler;
- custom agents/subagents;
- multi-agent debate;
- automatic retries;
- LLM-as-judge stage;
- default employer web research;
- automated submission;
- best-of-N full-package generation;
- outcome-learning loop;
- automatic model router;
- Ultra as default;
- Luna as default.

### 18.2 Archetype-memory concept

**Status: explicitly parked for “next overhaul.”**

The conversation explored:

- stable role archetypes;
- preselected must-load/must-consider evidence IDs;
- trigger-based evidence loading;
- strategy priors;
- evidence-pair memory;
- negative priors with override conditions;
- human-gated memory promotion.

The user explicitly stopped this line because it was becoming overcomplicated. It must not re-enter the MVP without a later explicit decision.

### 18.3 Revisit triggers

A deferred component should be reconsidered only when:

1. a concrete recurring pilot problem is observed;
2. the current manual solution is insufficient;
3. the new mechanism can be tested;
4. net value clearly exceeds human and system complexity;
5. it improves the primary quality distribution or materially reduces user workload.

---

## User Operating Profile

### Durable profile

| Dimension | Current operating default |
|---|---|
| Name | Vegard Håland |
| Professional orientation | BI/data/IT/strategy adviser-analyst; systems thinker; evidence and audit oriented |
| Core decision style | High-agency, structure-seeking, leverage-oriented; converts ambiguity into explicit frameworks |
| Response preference | Dense, complete, literal, direct, low filler; answer first; explicit facts/assumptions/risks/status |
| Quality preference | Correctness, usefulness, completeness and low redo cost over brevity or speed |
| Architecture preference | MVP-KISS; complexity must earn its place through direct value |
| Failure mode to counter | Over-structuring and analysis loops; enforce stopping rules and reject low-leverage infrastructure |
| Writing preference | Norwegian for internal/project documents; natural Bokmål for employer-facing material |
| Technical preference | Standard/built-in, robust, audit-ready code; avoid clever fragility |
| Human/LLM cost view | Human effort and complexity are more expensive than model effort |
| Truth posture | Strong persuasion within defensible evidence; admit uncertainty; no invented formal facts |

### Project-specific operating defaults

- Primary package goal: maximize chance of interview.
- Persuasion is first, second and third, but must be Norwegian-calibrated.
- Vegard is final semantic authority and manual submitter.
- Manual review is acceptable; extensive reconstruction is not.
- A somewhat over-enthusiastic claim can be corrected downward during calibration; automatic conservative underselling is worse.
- No automatic semantic veto after a job is approved for production.
- The weakest packages can be rerun outside the main framework.
- Use actual files/code as deliverables; reports are secondary.
- Keep original professional document masters when available.
- Do not claim testing or production readiness without evidence.
- No background/asynchronous promise; complete current work or provide honest partial state.

### Recurring correction pattern

The user repeatedly rejects:

- enterprise-style reliability infrastructure for an MVP;
- architecture theatre;
- excessive QA layers;
- overlong control artifacts that compete with writing;
- automated semantic gates;
- implicit API architecture when Codex-native execution was intended;
- uniformity optimization at the expense of strong HappyPath packages;
- assistant tendency to become “system engineer-y.”

The user repeatedly favors:

- direct improvement of employer understanding, evidence choice and final prose;
- low operator friction;
- manual folder-based control when adequate;
- strong model judgment rather than hand-rolled semantic code;
- explicit deferral lists;
- real pilot evidence over speculative scaffolding.

---

## Decision Register

| Domain | Decision/change | Status | Provenance | Replaced by / consequence |
|---|---|---|---|---|
| Core product | Build a Norwegian hiring-decision/application compiler, not generic text generator | ADOPTED | Assistant proposal adopted through repeated user direction | Governs all later versions |
| Fact authority | Use three complementary authority files | ADOPTED | Assistant proposal + implemented release | Replaced sole-Work derivative design |
| Persuasion | Persuasion-first, Norwegian calibrated | DECIDED | User | Replaced conservative QA-first default |
| Semantic gating | No semantic GO/NO-GO after human `PRODUCE` | ADOPTED | User + implementation | Replaced compiler/judge veto |
| Writer | Full native-Norwegian Writer is core production phase | ADOPTED | Assistant proposal, user continued | Retained through all versions |
| Mirror | Constructive final editor, no semantic verdict | ADOPTED | Assistant proposal adapted | Later proposed to become freer final writer |
| API pipeline | Python/OpenAI multi-call pipeline is not target | REJECTED | User clarification | Replaced by manual Codex/Work stage execution |
| Physical stages | Four stage folders and local instructions | ADOPTED for P0.6/P0.7 | User + implemented | Proposed to reduce to three in P0.8 |
| P0.6 clustering | 4×10 macro; 8×5 mini; 24 prompts | SUPERSEDED | User-directed architecture | Replaced by P0.7 2×20/4×10 |
| P0.7 clustering | 2×20 macro; 4×10 mini; 12 prompts | CURRENT implementation | User-directed + implemented | Proposed P0.8 uses 4×8–10 |
| Model route P0.7 | Terra Max → Sol Max → Terra XHigh → Sol XHigh | CURRENT implementation | Assistant design adopted into release | Proposed P0.8 Sol Max → Terra Max → Sol Max |
| Dual prompt | Two prompts/models per stage | REJECTED as P0.7 default | User/assistant convergence | Single-prompt internal Phase A/B |
| Dynamic CV | Model generates only dynamic zones; baseline supplies stable chronology | ADOPTED | User executive decision + implementation | Retained and high-value |
| Finalizer reports | No `FINALIZE_REPORT.md` or output index | DECIDED / IMPLEMENTED | User | Stdout summary only |
| `advance.ps1` | Keep simple deterministic split helper | ADOPTED in P0.6/P0.7 | User | Proposed removal in P0.8 |
| Memory/cache | Role-archetype memory concept | DEFERRED | User explicitly parked | “Next overhaul” only |
| QA hardening | Strict P0.7.1 contract hardening | PARTIALLY SUPERSEDED | Assistant audit | User shifted target to top-80 quality |
| Quality objective | Maximize median + mean top 80%; weak tail may rerun | DECIDED / CURRENT | User | Reframes architecture and QA priorities |
| P0.8 architecture | Three-stage Selective Quality MVP | PROPOSED | Assistant | Awaiting user adoption/specification |
| Stage 4 freedom | Allow final writer to change valid evidence/strategy | PROPOSED | Assistant after user objective shift | Would replace strict evidence lock |
| Review triage | READY/CHECK/RERUN | PROPOSED | Assistant | Would replace verbose review headings |
| Finalizer partial success | Deliver usable jobs even if others fail | PROPOSED | Assistant | Would replace global complete-batch orientation |

---

## Artifact Register

### Current and historical release artifacts

| Domain/version | Artifact | Status | Critical identifiers/logic | Remaining issue |
|---|---|---|---|---|
| P0.5.3 | `Jobbsok_26_P0.5.3_Codex_MVP_Release.zip` | SUPERSEDED, verified | SHA `bd98fc...3ee6`; four API/model calls; 55 files | Not Codex-native target |
| P0.5.3 | `DELIVERY_REPORT.md` | HISTORICAL | Four calls, native writer, mirror, private flags, A4 masters | Real live pilot not run |
| P0.5.3 | `TEST_REPORT.md` | HISTORICAL | 21/21 PASS, offline E2E | No live model request |
| P0.5.3 | `DECISION_LOG.md` | HISTORICAL | Non-veto, complete CV, original masters | Superseded implementation mode |
| P0.5.3 | `ARCHITECTURE_SUMMARY.md` | HISTORICAL | Four call responsibilities and source boundaries | Superseded by manual stages |
| P0.6 | `Jobbsok_26_P0.6_Release.zip` | SUPERSEDED base | SHA `6b4051...2a83`; 4×10/8×5; 24 prompts | Higher operator load |
| P0.6 | `IMPLEMENTATION_REPORT.md` | HISTORICAL | Three scripts, four stages, dynamic baseline | P0.7 migrated from it |
| P0.6 | `TEST_REPORT (1).md` | HISTORICAL | 30 PASS, PowerShell blocked | P0.7 supersedes |
| P0.6 | `FILE_MANIFEST.md` | HISTORICAL | Complete file inventory | P0.7 supersedes |
| P0.7 | `Jobbsok_26_P0.7_Release.zip` | CURRENT implementation | SHA `c74565...b1a8`; 52 files; four stages | Not real-pilot validated |
| P0.7 | `AGENTS.md` | CURRENT | Universal truth/no-submit/stage boundaries | Optimization objective should be updated if P0.8 adopted |
| P0.7 | `MODEL_ROUTING.md` | CURRENT | Terra/Sol default and escalation | Time-sensitive; empirical validation absent |
| P0.7 | `START_HERE.md` | CURRENT | 12-prompt operator flow | Complex relative to proposed P0.8 |
| P0.7 | `CV_BASELINE.md@0.7.0` | CURRENT / HIGH VALUE | Complete static CV and known IDs | Update schema/headline/layout only if needed |
| P0.7 | `PACKAGE_CONTRACT.md` | CURRENT | Dynamic package JSON schema | Missing explicit headline; strict Stage 4 constraints debated |
| P0.7 | `PERSUASION_CALIBRATION.md` | CURRENT | Operator correction surface | Must learn only from explicit user calibration |
| P0.7 | Word masters | CURRENT / HIGH VALUE | Original content-control A4 masters | Page balance needs refinement |
| P0.7 | `ingest.py` | CURRENT | Deterministic vacancy extraction and validation | Reusable in P0.8 |
| P0.7 | `advance.ps1` | CURRENT | Macro→mini split | PowerShell unverified; proposed removal in P0.8 |
| P0.7 | `finalize.py` | CURRENT | Merge, validation, DOCX/PDF, batch summary | Selective delivery behavior proposed |
| P0.7 | `HYBRID_PILOT_LOG.csv` | CURRENT but unpopulated/underused | Intended model/quality pilot data | Needs top-80 quality metrics |
| Conversation | `jobbsøk_26_P0.7.md` | ADOPTED architecture specification for implemented P0.7 | Detailed 4-stage P0.7 design | Generated file not mounted in accessible attachment list; major content represented in chat/release |
| Conversation | `Jobbsok_26_P0.7_Implementation_Prompt.md` | USED / HISTORICAL | Surgical P0.6→P0.7 migration order | Implementation completed |
| Conversation | `Jobbsok_26_P0.7_Critical_Audit_and_Perfection_Recipe.md` | CURRENT audit reference, priority partly superseded | P0.7.1 findings and patch recipe | Must be reinterpreted under new objective |
| Proposed | P0.8 `cluster_strategy.md` | PROPOSED | Shared strategy and job ordering | Not specified/implemented |
| Proposed | P0.8 `blueprint.md` | PROPOSED | Employer model, identity, headline, evidence, channels, class | Not specified/implemented |
| Proposed | P0.8 `review.json` | PROPOSED | READY/CHECK/RERUN | Not validated |

### Research and guidance artifacts

| Artifact | Status/use |
|---|---|
| `deep-research-report (Local Batch Processing Architecture)(1).md` | Historical technical research on Codex stage isolation, AGENTS, Skills, CLI, state, Windows |
| `deep-research-report (Product Line Architecture and Implementation)(1).md` | Historical product-line/variant architecture research |
| `deep-research-report (Codex Batch Processing)(1).md` | Historical Codex batch architecture and optimization |
| `Pasted markdown(26).md` | Integrated improvement/architecture report framing Jobbsøk_26 as domain compiler |
| `Pasted markdown (2)(1).md` | Integrated product-line × Codex batch × framework report |
| `Norwegian_language_tone_structure_norms(4).md` | Approved advisory Bokmål runtime and style guide |
| `Norwegian_application_text_guide(4).md` | Approved advisory strategy/channel/document guide |
| `deep-research-report (Framework Architecture and Implementation Specification for a Norwegian Job Application Engineering System).md` | Evidence-first architecture report |
| `deep-research-report (Norge_LLM_kompetanse_CV_soknad_intervju_2026)(4).md` | Human-governed AI competence positioning |
| `deep-research-report (Norwegian Role-Market and Positioning Report)(4).md` | Norwegian role-market positioning |
| `deep-research-report (Norway-Specific Bokmål Style System for CVs and Job Applications)(4).md` | Norwegian language and recruiter style research |
| `deep-research-report (Norway Guide to CVs and Written Job Applications)(4).md` | Norwegian CV/application norms |
| `deep-research-report(Master Upgrade Payload).md` | Proposed hardening of Single Backbone, asymmetry and Vinklings-Matrisen |
| `deep-research-report(2).md` | Positioning and narrative architecture research |
| `deep-research-report(1).md` | Metacognition and recruiter psychology research |
| `deep-research-report (12).md` | Deep research on Codex-native stage architecture |
| `Pasted text(35).txt` | P0.5.3 MVP-KISS implementation brief |
| `Jobbsøk_26 P0.6 Fullimplementering.docx` | Previous P0.6 implementation prompt |

---

## Open/Risk/Uncertainty Register

| ID | Item | Status | Consequence / next action |
|---|---|---|---|
| O-01 | Adopt P0.8 three-stage architecture or retain/patch P0.7 | OPEN | Requires explicit user decision and final specification |
| O-02 | Best cluster size under quality objective | OPEN | Run real pilot; compare 8–10 vs 20/10 if needed |
| O-03 | Sol Max versus XHigh in final stage | OPEN | A/B on PRIME jobs; measure final quality and edit time |
| O-04 | Terra Max versus XHigh writer | OPEN | Start Max for quality baseline; lower only if no quality loss |
| O-05 | Separate candidate-blind Stage 1 value | OPEN | Proposed P0.8 integrates it internally into Sol strategy stage |
| O-06 | Stage 4 strategic freedom | OPEN / PROPOSED | Define truth boundary and strategy-delta note if adopted |
| O-07 | Review triage accuracy | OPEN | Measure TailRecall20 and review load |
| O-08 | Real production quality | NOT RUN | One real job and one full cluster required |
| O-09 | PowerShell runtime of current P0.7 `advance.ps1` | BLOCKED in tested environment | Irrelevant if P0.8 removes script; otherwise test on Windows |
| O-10 | P0.7 Stage 4 mutable-draft bypass | CURRENT defect | Either fix canonical reference or replace constraint in P0.8 |
| O-11 | CV headline | CURRENT deficiency | Add explicit schema field |
| O-12 | CV page balance | CURRENT deficiency | Redesign flow/layout; sparse CV should not be forced into two weak pages |
| O-13 | Duplicate portal question IDs | CURRENT defect | Add cheap uniqueness validation |
| O-14 | Hard page gate versus selective delivery | OPEN | Align finalizer with quality-first objective |
| O-15 | Global batch completeness versus partial delivery | OPEN | Proposed per-job delivery classes |
| O-16 | Application date reproducibility | LOW-PRIORITY OPEN | Add explicit date only if it causes real friction |
| O-17 | DOCX old metadata | LOW-PRIORITY OPEN | Polish, not quality blocker |
| O-18 | Input directory git-ignore | LOW-PRIORITY OPEN | Privacy hygiene if repository is used with Git |
| O-19 | Schema fallback drift | LOW-PRIORITY OPEN | Remove fallback or enforce keyword support only if schema evolves |
| O-20 | Archetype memory/cache | DEFERRED | Explicitly parked for next overhaul |
| O-21 | Luna economy route | DEFERRED / EXPERIMENTAL | Evaluate only after quality baseline and real credit data |
| O-22 | Full source web verification of earlier model/pricing claims | UNCERTAIN/TIME-SENSITIVE | Must be rechecked before execution, but outside this source-bound KB task |

---

## Coverage Audit

| Domain/source | Coverage | Confidence | Cause / limitation |
|---|---|---:|---|
| User’s latest quality objective | COVERED | High | Explicit full user statement accessible |
| Current P0.7 release files | COVERED | High | ZIP extracted; active text/code/report files inspected |
| P0.7 release ZIP integrity/hash | COVERED | High | Direct calculation and prior audit |
| P0.7 automated tests | COVERED | High | Release report plus prior independent rerun represented |
| P0.7 visual fixture observations | PARTIAL | Medium-high | Audit conclusions accessible; rendered page images not embedded in KB |
| P0.7 generated architecture specification | PARTIAL | Medium-high | Detailed content represented in assistant response and release; generated file itself not in current attachment list |
| P0.7 implementation prompt | PARTIAL | High | Full prompt was shown in prior assistant response; generated file not currently mounted |
| P0.7 audit report | PARTIAL | High | Major findings and recipe fully represented in assistant response; generated file not mounted |
| P0.6 release | COVERED | High | ZIP, implementation report, test report and manifest accessible |
| P0.5.3 release | COVERED | High | ZIP, reports, architecture, decision log, manifests accessible |
| Candidate authority files | SUBSTANTIALLY COVERED | High | Core metadata, chronology, evidence map, routes, claim boundaries and baseline included; every project atom and claim row is not reproduced verbatim because the KB preserves operationally distinct signal rather than duplicating source files |
| Norwegian language/application guides | SUBSTANTIALLY COVERED | High | Runtime core and key norms captured; full examples and every subsection not reproduced |
| Deep-research reports | SUBSTANTIALLY COVERED | Medium-high | Material conclusions and decisions captured; full source registers and long generic exposition omitted |
| Earlier web-search result bodies | PARTIAL | Medium | Only conclusions/citations preserved in chat; source pages not part of current source-bound corpus |
| Skipped chat messages | INACCESSIBLE | Low | Multiple transcript segments explicitly marked `Skipped N messages`; exact wording unavailable |
| Unrelated recent conversations shown in system recent-history summary | OMITTED FROM DOMAIN DETAIL | High | They are not part of the Jobbsøk_26 pre-prompt thread being canonicalized; only durable user operating preferences relevant to this project were retained |
| Deliberate compression | COVERED WITH COMPRESSION | High | Repetition, generic exposition, duplicated examples and obsolete wording removed; decisions, corrections, artifacts, exact identifiers, risks and open loops retained |

---

## Canonical Continuation State

A successor model should proceed as follows:

1. Treat `Jobbsok_26_P0.7_Release.zip` as the latest implemented baseline, not as the final desired architecture.
2. Treat the user’s selective-quality objective as the latest and highest-authority product goal.
3. Treat the three-stage P0.8 Selective Quality design as a proposal awaiting explicit adoption and detailed specification.
4. Do not reintroduce deferred memory/cache, agents, vector infrastructure, automatic routing or enterprise reliability systems.
5. Preserve source authorities, dynamic CV baseline merge, original Word masters, Norwegian persuasion core, job identity, no-submit boundary and per-job deterministic rendering.
6. Prioritize explicit headline, stronger document layout, strategic final-writer freedom, selective review triage and real quality evaluation.
7. Before implementation, convert the proposed P0.8 overview into one authoritative architecture/design/implementation specification with:
   - exact repository tree;
   - three stage contracts;
   - schemas;
   - model/effort defaults;
   - cluster policy;
   - hard versus soft checks;
   - `READY/CHECK/RERUN` contract;
   - partial-success finalizer behavior;
   - migration map from P0.7;
   - real-pilot acceptance criteria.
8. Evaluate success with median quality, top-80 mean, submit-ready share, human edit minutes, credits per ready package and bottom-tail flag recall.
