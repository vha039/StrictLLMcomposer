# Current state, authority and decisions

## 1. Product objective and optimization hierarchy

### 1.1 Product contract

Jobbsøk_26 is a private, local, file-authoritative and manually controlled system for one candidate. It converts a human-approved vacancy plus authoritative candidate truth into a vacancy-specific Norwegian application package that is truthful, persuasive, coherent, editable, renderable and manually submittable. The package normally consists of a materially tailored CV and an application letter; portal handling is a current P0.9 architecture fork rather than an already adopted product fact.

The primary product is the employer-facing package. Strategy, provenance, validation, review and state artifacts exist only to protect or improve that product. [SRC-03: CORE_OBJECTIVE, PRIMARY_UTILITY, NORTH_STAR; SRC-06: §§1–5; SRC-18: §§4–5]

### 1.2 Selective-quality objective

The decisive P0.7→P0.8 shift was away from uniform completion quality and toward the quality distribution of the useful majority:

```text
Q_happy = (median(package_quality)
           + mean(top_80_percent(package_quality))) / 2
```

Operational meaning:

- maximize median package quality;
- maximize the mean quality of the strongest approximately 80%;
- do not weaken strong packages to make the batch uniform;
- identify the weak tail cheaply through `READY / CHECK / RERUN`;
- allow targeted rerun, separate handling or non-submission for disproportionate tail cases;
- regard extensive routine human rewriting as system failure;
- regard bounded final human review as necessary and acceptable.

The later user target sharpens this into approximately **30 strong packages from a batch around 40**, not 40 equally optimized packages. `Q_happy` is an evaluation function, not a model-side numeric judge. [SRC-02: §§0.2, 3–5; SRC-03: PRIMARY_UTILITY; SRC-18: D-003–D-004; SRC-19: §§1.3–1.4]

### 1.3 Current truth-safe priority order

Among alternatives that satisfy truth, identity, employer usability and human-final-authority constraints, the latest explicit P0.9 ranking is:

1. **final package quality / expected interview value**;
2. **low human effort**;
3. **fast and simple implementation**;
4. **model cost**;
5. **reversibility / optionality**.

The older cost heuristic remains useful as a secondary tie-breaker:

```text
Human Effort > Human Complexity > LLM Complexity > LLM Effort
```

It no longer outranks package quality or implementation urgency. [SRC-03: SECONDARY_OBJECTIVES_ORDER, COST_HIERARCHY; SRC-18: D-010 and §5.1]

### 1.4 Truth and persuasion posture

Truth is a hard ceiling, not a reason for timid writing. The system may select the strongest accurate professional identity, use functional equivalence, expose documented leadership or ownership, translate sector experience, emphasize scope and consequence, and formulate future contribution. It may not invent or silently upgrade formal title, date, degree, institution, result, metric, personnel responsibility, mandate, lifecycle, ownership or production status.

The target voice is direct native Bokmål with calm professional weight: strong work language and evidence, restrained self-evaluation, one dominant backbone, explicit personal contribution where supported, collective attribution where appropriate, and no imported corporate hype. [SRC-03: TRUTH_AUTHORITY, PERSUASION_POSTURE, NORWEGIAN_LANGUAGE, SINGLE_BACKBONE]

---

## 2. Version-state table

| Version/state | Authority/status | Implemented? | Mechanically tested? | Real model/product pilot? | Current use |
|---|---|---:|---:|---:|---|
| **P0.5.3** | Superseded historical API/SDK compiler architecture | Yes, historically | 21/21 reported deterministic/offline tests | No real production run | Regression history only: proves API/structured-output/compiler direction was tried and rejected as non-Codex-native for this project. |
| **P0.6** | Superseded manual four-stage implementation | Yes, historically | 30/33 reported; PowerShell-dependent gaps | No established real production pilot | Migration history and earlier implementation patterns only. |
| **P0.7** | **Latest verified executable release** | **Yes** | **32 PASS / 2 SKIP / 0 FAIL on 34 tests; controlled E2E/render fixtures** | **No real Terra/Sol vacancy production run** | Engineering baseline and source of reusable assets, defects, tests and concrete template behavior. |
| **P0.8.0** | **Latest formally adopted normative architecture**; `FINAL_NORMATIVE_SPECIFICATION` | No | Specification/test plan only | No | Inherited normative control wherever later user decisions do not supersede it. |
| **P0.8.1** | Consolidated pre-implementation hardening, `NON_NORMATIVE_UNTIL_ADOPTED` | No | No implementation | No | Strong source of contract repairs and pilot discipline; each mechanism must be explicitly selected, not assumed adopted. |
| **P0.9 pre-lock** | Current project phase; user policy + research + option-space work | No | Several proposed spikes, none represented as completed here | No | Decision basis for final architecture freeze. |
| **Source 20 candidate** | `DERIVED_FINAL_CANDIDATE_FOR_ADOPTION` | No | No | No | Strong integrated candidate, challenged proposition-by-proposition; not historical P0.9 authority. |

Provenance anchors represented in the corpus:

- P0.7 release ZIP SHA-256: `c74565ceb32900beba4b912e1cec93abe68039f83a29da6952f7ad9f57feb1a8`;
- P0.8.0 normative specification: 3,825 lines / 17,151 words, SHA-256 `0dddf4b4c29fcee407ff568cfc2f1629ed01d3e8aa88129497da3a1d748ec0ba`.

These identify the historical artifacts; Step 2 must hash the actual supplied copies rather than assume filename identity.

[SRC-00: §0.1 and Part II; SRC-05: §§0, 7, 9; SRC-06: front matter; SRC-08: front matter; SRC-18: §§0, 8, 15; SRC-19: §§2–3; SRC-20: front matter and §0]

---

## 3. Active decision ledger

States:

- `LOCKED` — explicit current user decision or unsuperseded normative invariant;
- `STRONG_DEFAULT` — best-supported candidate, but final P0.9 must explicitly adopt or reject it;
- `OPEN` — real architecture choice remains;
- `VERIFY` — architecture may be stable, but actual behavior must be tested;
- `EXPERIMENTAL` — optional hypothesis requiring comparative evidence.

### 3.1 Product, scope and economics

| ID | Decision | Authority | State | Consequence |
|---|---|---|---|---|
| `D-002` | Truth, factual identity, employer usability and human irreversible authority are hard constraints. | `[USER]` | `LOCKED` | No quality or simplicity gain can justify fabricated or inflated claims, broken deliverables or autonomous submission. |
| `D-003/004` | Optimize the strong majority; approximately 30 strong packages from ~40 is acceptable, with selective tail handling. | `[USER]` | `LOCKED` | Architecture must not overinvest in universal rescue, uniformity or heavy QA at the expense of strong-package quality. |
| `D-005` | System is reusable for the same candidate over several future batches, potentially long-term; it is not a multi-candidate product. | `[USER]` | `LOCKED` | Stable source IDs, policies and modest reusable abstractions are justified; onboarding/platform generality is not. |
| `D-006` | Jobs are normally frozen before production; late changes are exceptional. | `[USER]` | `LOCKED` | A run freeze and explicit stale detection are required; silent mid-run mutation is not. |
| `D-007/009` | Human capacity is roughly 5–10 h/week and approximately 10–20 total human minutes per submitted package. | `[USER]` | `LOCKED` | Review/status design, portal handling and prompt count must be judged against real human throughput. |
| `D-008` | First batch is urgent: desired submission window 1–4 weeks; some meaningful deadlines may be under two weeks. | `[USER]` | `LOCKED` | Pre-lock experiments and architecture polish must have high expected decision value; optional features cannot block baseline delivery. |
| `D-010` | Truth-safe priority is quality > human effort > implementation speed > model cost > reversibility. | `[USER]` | `LOCKED` | Reversibility alone cannot justify abstraction; model cost is subordinate to quality and human work. |
| `D-011` | Core **may** be invariant tailored CV + application. | `[USER]` permission | `OPEN` | Strong simplification candidate, not an adopted boundary. Requires Step-1 decision informed by the vacancy inventory. |
| `D-012` | Portal answers **may** be detached into a downstream workflow. | `[USER]` permission | `OPEN` | Source 20’s detachment is a synthesis choice, not a historical user decision. |
| `D-013` | P0.9 v1 **may** be Bokmål-only. | `[USER]` permission | `OPEN` | Confirm actual language mix before freezing; nonconforming vacancies may use exception handling. |
| `D-014` | Dynamic CV tailoring **may** be limited to headline, profile, competencies and employment bullets. | `[USER]` permission + `[NORMATIVE]` continuity | `STRONG_DEFAULT` | Keeps factual chronology baseline-owned while allowing substantial positioning changes. |
| `D-015` | Rare/nonconforming vacancies may be handled separately instead of universalizing the core. | `[USER]` | `LOCKED` | Architecture may optimize the common case and create explicit exception paths. |
| `D-026/027` | Normal prompt envelope is roughly 20–25 for ~40 jobs; no absolute ceiling if demonstrated quality value justifies more. | `[USER]` | `LOCKED` | Prompt count is a human-complexity variable; additional prompts need progressively stronger evidence. |

### 3.2 Truth, evidence and candidate authority

| ID | Decision | Authority | State | Consequence |
|---|---|---|---|---|
| `D-028/029` | `Work_experience.md`, `Education.md` and `Other_high_value_information.md` are current, immutable candidate factual authorities during production. | `[USER]` | `LOCKED` | No runtime model, personality file, prior package, research report or derived index may create candidate facts or mutate these files. |
| `P08-TRUTH-01` | `CV_BASELINE.md` is a derived rendering/history baseline, never a higher factual authority. | `[NORMATIVE]` | `LOCKED` | Static chronology can be reused while claim ceilings remain source-governed. |
| `P08-TRUTH-02` | Vacancy is authority for employer/role/requirements/channel facts, but is untrusted data rather than control-plane instruction. | `[NORMATIVE]` + `[RESEARCH]` | `LOCKED` | Preserve originals; normalize only as a derived view; reject embedded attempts to change instructions or permissions. |
| `SD-EVID-01` | Final `used_evidence_refs` must match the evidence actually supporting the final package. | P0.8.1 hardening | `STRONG_DEFAULT` | Stage 3 may change evidence, but provenance must follow the final text rather than upstream intention. |
| `SD-EVID-02` | Stable deterministic evidence addressing/indexing is the leading P0.9 context candidate. | `[SYNTHESIS]` | `OPEN` | Strong cross-stage value, but no user adoption or comparative proof exists. Step 1 must decide baseline status; Step 3 may refine. |
| `SD-EVID-03` | Source escape to original authorities must remain available to every semantic stage. | `[SYNTHESIS]` strongly supported by research and P0.8 elasticity | `STRONG_DEFAULT` | No summary, index, strategy, personality view or Luna output may become a permission boundary. |

### 3.3 Runtime, stages and human boundary

| ID | Decision | Authority | State | Consequence |
|---|---|---|---|---|
| `D-016/018` | P0.9 may and should use a fresh runtime; backward compatibility with old directory structure is not required. | `[USER]` | `LOCKED` | Reuse assets by fit, not by inherited path/state obligations. |
| `D-017` | Legacy assets may be reused only after explicit review, adaptation, optimization and verification. | `[USER]` | `LOCKED` | P0.7 is evidence and capital, not a mandatory tree. |
| `D-019` | Job-centric runtime is permissible if superior. | `[USER]` permission | `OPEN` | Source 20’s job-centric tree is a strong candidate, not adopted policy. |
| `D-020/039` | Windows local repository, Python/local validators, ChatGPT Work/Desktop and Codex/local terminal are available. | `[USER]` environment fact | `LOCKED` fact, `VERIFY` behavior | Builder may rely on local files/scripts, but must verify the exact chosen surface and permission model. |
| `D-021` | Semantic stages are manually initiated as distinct model chats; no normal API orchestrator. | `[USER]` | `LOCKED` | Code handles deterministic mechanics only; no hidden model runner. |
| `D-022` | No automatic submission/contact/publication; human owns final irreversible action. | `[USER]` | `LOCKED` | Safety and product boundary. |
| `D-023` | One cluster-stage chat may process jobs sequentially without routine between-job confirmation; each job persists before the next. | `[USER]` | `LOCKED` | One-job transaction and continuation/reconciliation are core runtime requirements. |
| `P08-STAGE-01` | Three core stages remain the current control: Sol decision architecture → Terra package writer → Sol final writer/review. | `[NORMATIVE]` unsuperseded | `STRONG_DEFAULT` | No later user decision adds/removes a core semantic stage; final P0.9 should explicitly ratify or change it. |
| `D-025` | Final Sol is `ELASTIC` within immutable truth ceilings. | `[USER]` | `LOCKED` | Strategy/draft are hypotheses and inputs, never semantic authority over the final writer. |
| `SD-RUNTIME-01` | One frozen run manifest plus job-centric transactions and derived status is the leading state design. | `[SYNTHESIS]` | `OPEN` | Strong simplification, but final Step 1 must choose it over stage-centric P0.8/P0.8.1 control. |
| `SD-RUNTIME-02` | Expected jobs must come from frozen intake/manifest, never directory discovery. | P0.8.1 hardening | `STRONG_DEFAULT` | Missing output cannot silently disappear; partial success remains explicit. |
| `SD-RUNTIME-03` | Static invalidation classes should report stale scope without an automatic dependency engine. | `[SYNTHESIS]` | `STRONG_DEFAULT` | Preserves observability and run integrity without building state orchestration. |

### 3.4 Validation, review, repair and rerun

| ID | Decision | Authority | State | Consequence |
|---|---|---|---|---|
| `D-024` | A model may invoke supplied deterministic validators/scripts and repair/revalidate in the same session. | `[USER]` permission | `LOCKED` permission, `VERIFY` workflow | Enables bounded local repair without automatic model orchestration. |
| `P08-VAL-01` | Deterministic mechanics, semantic truth policy and soft quality/review are separate validation classes. | P0.8.1 hardening | `STRONG_DEFAULT` | Python must not pretend keyword or schema checks prove factual meaning or persuasive quality. |
| `SD-VAL-02` | Stage artifacts should validate successfully before completion. | P0.8.1 hardening | `STRONG_DEFAULT` | Prevents `_DONE`/heading theatre and stale progress. |
| `SD-VAL-03` | Maximum two same-session repair attempts, then explicit failure and continuation, is the leading bounded protocol. | N-04 synthesis + user permission | `OPEN` | Attempt count was not user-locked; Step 1 should adopt or adjust, Step 2 verify ergonomics. |
| `P08-REV-01` | Operator statuses are `READY / CHECK / RERUN`; no numeric model quality/confidence score. | `[NORMATIVE]` | `LOCKED` control | Status predicts remaining repair scope, not objective quality. |
| `SD-REV-02` | `READY`, `CHECK` and `RERUN` should be defined by repair scope. | P0.8.1 hardening | `STRONG_DEFAULT` | Enables calibration against actual human work. |
| `SD-RERUN-01` | RERUN should be one job, separate manual chat, Sol-class final reconstruction with targeted source access. | P0.8.1 hardening | `STRONG_DEFAULT` | Not a standard fourth stage and never automatic. |
| `P08-PARTIAL-01` | One weak/failed job must not invalidate successful jobs. | `[NORMATIVE]` | `LOCKED` | Per-job delivery states and transaction isolation. |

### 3.5 Documents, rendering and channels

| ID | Decision | Authority | State | Consequence |
|---|---|---|---|---|
| `D-040/041` | LibreOffice is not currently installed but can be installed; ordinary DOCX→PDF works, while headless behavior is unverified. | `[USER]` environment fact | `VERIFY` | Target-Windows headless preflight is mandatory before production assumptions. |
| `P07-RENDER-01` | Existing P0.7 Word masters and fill→unwrap→validate→render technique have controlled fixture evidence. | `[VERIFIED]` direct audit | `VERIFY` for reuse | Generic content-control warnings do not justify discarding the actual masters; target behavior and ATS parsing remain open. |
| `SD-RENDER-02` | Treat one job as the render transaction and verify every document output independently; isolate converter state. | P0.8.1/research synthesis | `STRONG_DEFAULT` | Actual one-process-per-job versus per-document policy is Step-2 evidence. |
| `P08-RENDER-03` | Sparse CV may be one page; normal/dense CV usually two; overflow is normally a review issue, not automatic semantic deletion. | `[NORMATIVE]` | `LOCKED` control | Protects content quality and page balance. |
| `OPEN-PORTAL` | Integrated portal versus detached downstream portal remains unresolved. | `[OPEN]` | `OPEN` | Exact portal limits are hard whenever portal output exists; actual vacancy inventory must drive the boundary. |

### 3.6 Personality, context preparation and evaluation

| ID | Decision | Authority | State | Consequence |
|---|---|---|---|---|
| `D-030` | Personality source is a composite, self-synthesized interpretive profile. | `[USER]` fact | `LOCKED` fact | Treat as calibrated context, not psychometric proof. |
| `D-031` | Personality must be optional and controlled through `SETTINGS.md` if implemented. | `[USER]` | `LOCKED` boundary | Pipeline must work fully with it off. |
| `D-032` | Personality default ON/OFF is unresolved. | `[OPEN]` | `OPEN` | Source 20’s default OFF is an interim synthesis, not a user decision. |
| `D-046–048` | Personality is interpretive, never factual; 0–3 facets and 20 PF IDs are proposed interfaces, not adopted contracts. | Source profile + assistant synthesis | `EXPERIMENTAL` | Final architecture should preserve the boundary and leave exact granularity contingent on marginal value. |
| `LUNA-01` | Luna/job-local preparation is optional only; no default global pass, no employer-facing prose, no factual authority, no source exclusion. | `[RESEARCH]` + synthesis | `EXPERIMENTAL` | Compare only against deterministic-index/direct-source control; fail open. |
| `D-033` | Up to roughly 3–4 small, high-decision-value pre-architecture tests are acceptable. | `[USER]` | `LOCKED` budget | Does not require running them all; urgent deadlines raise the bar. |
| `D-034–037` | Historical applications/interview conversion are not comparable; first-batch feedback is available; week-later self-rating repeatability expected around 7/10. | `[USER]` | `LOCKED` evaluation facts | Use current batch calibration, qualitative notes and material differences; avoid pseudo-precision. |
| `D-038` | Blinding preference is unresolved. | `[OPEN]` | `OPEN` | Use only when low-friction and decision-relevant; do not assume a user mandate. |

---

## 4. Active non-goals and regression firewall

These remain outside P0.9 core unless a named observed failure demonstrates material value:

- API/model-call orchestration as the normal workflow;
- multi-agent debate, generalized agents or subagent framework;
- vector database, embeddings, GraphRAG, semantic cache or heavyweight retrieval platform;
- role/archetype memory or cross-job personality memory;
- automatic model routing;
- LLM-as-judge core stage or numeric fit/quality gate;
- automatic semantic retries or hidden rerun loop;
- full-package best-of-N generation;
- broad/default employer research pipeline;
- automatic job search, employer contact or submission;
- database/event-sourced runtime or automatic dependency engine;
- generalized claim graph/provenance platform;
- model-generated settings compiler or prompt cache;
- global cheap-model relevance filter or source exclusion;
- mandatory Luna or personality dependency;
- typography auto-fit engine, persistent LibreOffice daemon or premature render service;
- n-gram/similarity hard gate before recurrent convergence is observed;
- semantic truth validator that claims to prove free-text factuality;
- universal handling of rare channels/languages/candidate types;
- per-job copies of all candidate authorities;
- `_DONE.md`, substring/heading completion theatre, or stale progress as authority.

[SRC-03: NON_GOALS; SRC-06: §§3–5, 51; SRC-08: scope firewall; SRC-10: parked/rejected options; SRC-18: §5.2; SRC-20: §27]

---

## 5. Resolution queue

Every unresolved item has exactly one primary resolution owner. Interim rules prevent silent invention without masquerading as final decisions.

| ID | Question | State | Resolution owner | Blocking? | Interim rule |
|---|---|---|---|---:|---|
| `RQ-01` | Is the P0.9 core invariant CV+application, or must portal answers remain a core required output? | `OPEN` | `STEP1_FREEZE` | Yes for intake/schema/tree | Leading candidate: detach portal after approved package; validate against actual vacancy inventory before adoption. Until frozen, preserve portal as an isolated optional branch rather than duplicating channel state throughout core. |
| `RQ-02` | Is P0.9 v1 strictly `nb-NO`? | `OPEN` | `STEP1_FREEZE` | Yes for core schema/prompts | Derive actual language mix; use Bokmål-only core if non-Norwegian jobs are absent or explicitly exception-handled. |
| `RQ-03` | Which runtime/state design is normative: stage-centric P0.8/P0.8.1 or fresh job-centric manifest/artifact reconciliation? | `OPEN` | `STEP1_FREEZE` | Yes | Leading candidate: one frozen run manifest, job-centric current artifacts, derived status and static stale reporting. A tiny no-model spike may inform but is not mandatory if architecture judgment is clear. |
| `RQ-04` | What is the canonical strategy serialization and target size? | `OPEN` | `STEP1_FREEZE` | Yes for schemas/prompts | Preserve the semantic contract independent of serialization. Control is stable-label Markdown; leading challenger is structured decision core plus prose and deterministic human view. Run a two-job falsification test only if the choice remains materially uncertain. |
| `RQ-05` | Do Priority A/B, opportunity prediction, special treatment or model-generated cluster planning survive? | `OPEN` | `STEP1_FREEZE` | Moderate | Keep human priority/deadline and human-fixed clustering. Do not differentiate model treatment unless Step 1 explicitly adopts a measurable reason. |
| `RQ-06` | Is a deterministic evidence index baseline core or a Step-3 enhancement? | `OPEN` | `STEP1_FREEZE` | Moderate | Treat as strongest low-risk candidate; it must be lossless, non-semantic, source-linked and regenerable. Do not add relevance scoring. |
| `RQ-07` | What personality default and runtime interface should ship? | `OPEN` | `STEP1_FREEZE` | No for baseline | Require an off-safe toggle. Interim baseline may run OFF; exact 0–3-facet/PF-ID protocol remains experimental until adopted or supported by a small test. |
| `RQ-08` | Should Luna/job-local context preparation exist in v1? | `EXPERIMENTAL` | `STEP3_EXPERIMENT` | No | OFF and absent from baseline dependency. Test only after deterministic/direct-source control exists and deadlines permit. |
| `RQ-09` | What bounded validator repair attempt count should be normative? | `OPEN` | `STEP1_FREEZE` | Low | Leading rule: two repair attempts, then explicit stage/job failure and continue. No validator-triggered model calls. |
| `RQ-10` | Exact cluster count, size and order? | `VERIFY` | `STEP3_EXPERIMENT` | No for initial build | Start from P0.8 control of roughly five clusters × eight jobs, normal 6–10; measure early/late degradation and convergence. |
| `RQ-11` | Which selected Work/Codex surface actually supports file access, local validation and same-session repair reliably? | `VERIFY` | `STEP2_VERIFY` | Yes before live stages | Choose the real execution surface, run one deliberately invalid artifact through validator→repair→revalidate, document permissions and operator flow. |
| `RQ-12` | Can the P0.7 masters and OOXML content-control technique be reused safely on the target machine? | `VERIFY` | `STEP2_VERIFY` | Yes for rendering | Inspect exact assets; test fill→unwrap→DOCX/PDF, fonts, Norwegian glyphs, headers, sparse/normal/dense layouts and extraction. |
| `RQ-13` | One isolated LibreOffice invocation per job or per document? | `VERIFY` | `STEP2_VERIFY` | No for architecture | Job is the transaction; each output is independently verified. Use the simplest invocation strategy that passes target-Windows tests. |
| `RQ-14` | What actual channel/platform/sector distribution exists? | `VERIFY` | `STEP1_FREEZE` | Yes for product boundary | Produce one row per vacancy before final freeze; actual facts override estimates (`~20%` portal, uncertain public-sector share). Step 2 later verifies implementation-specific limits and channel behavior. |
| `RQ-15` | Does personality improve current package quality enough to justify default/use? | `EXPERIMENTAL` | `STEP3_EXPERIMENT` | No | Compare 2–3 representative jobs OFF/ON without simultaneously changing strategy format or Luna. |
| `RQ-16` | Does structured strategy improve the system or inflate upstream authority? | `EXPERIMENTAL` | `STEP3_EXPERIMENT` | No after a reversible serialization choice | Compare final quality, writer coherence, repair burden and appropriate Stage-3 reconstruction—not schema validity alone. Step 1 still owns the initial serialization decision through `RQ-04`. |
| `RQ-17` | Does deterministic indexing outperform direct source navigation, and does Luna add value beyond it? | `EXPERIMENTAL` | `STEP3_EXPERIMENT` | No | Compare direct/index first; Luna only as an incremental third condition. `outside_prep` is diagnostic, not recall proof. |
| `RQ-18` | How well do READY/CHECK/RERUN predict human repair scope? | `EXPERIMENTAL` | `STEP3_EXPERIMENT` | No | Calibrate on the first comparable batch using total human handling time and qualitative errors. |
| `RQ-19` | Do adapted DOCX/PDF outputs preserve critical identity/contact content and logical reading order in target parsers/portals? | `VERIFY` | `STEP2_VERIFY` | Yes before production submission | Run representative extraction and actual-channel smoke tests; move/duplicate critical header content into normal flow if needed. |
| `RQ-20` | Which volatile model/product names, prices, effort modes and file-context behavior hold at build time? | `VERIFY` | `STEP2_VERIFY` | Yes for runbook, not conceptual architecture | Reverify first-party product facts immediately before implementation/production; preserve role split if names change. |
| `RQ-21` | Is cross-cluster phrase convergence materially harmful? | `EXPERIMENTAL` | `STEP3_EXPERIMENT` | No | Human batch spot-check first; automate only after recurrent observed failure demonstrates a precise low-cost control. |
| `RQ-22` | Which historical candidate-source gaps and claim-index deltas can now be verified and incorporated? | `VERIFY` | `STEP3_EXPERIMENT` | No for baseline; may affect prominent claims | Inspect current authority files for BAR/`PRJ-01..07`/education details and `CLM-BAR-*`/`CLM-PRJ10-*` index sync. Until verified, omit exact scale/results/lifecycle details or retain the documented ceiling. |

---

## 6. Epistemic boundaries to preserve

1. **Permission is not selection.** The user allowed detached portal, Bokmål-only v1, narrow dynamic CV and job-centric state; the corpus does not show those choices being formally adopted.
2. **Hardening is not historical norm.** P0.8.1’s repairs are often excellent, but `NON_NORMATIVE_UNTIL_ADOPTED` remains consequential.
3. **Structure is not semantic authority.** A schema-valid strategy remains a hypothesis; a validator pass remains mechanical evidence only.
4. **Research constrains; it does not choose.** Public-sector rules, portal variability, lost-in-the-middle, SDT risks and model benchmarks inform design but do not independently settle product policy.
5. **Direct implementation evidence can beat generic warnings.** The actual P0.7 master structure and controlled render tests are more specific than general “avoid content controls” advice, while target-machine and ATS behavior still require verification.
6. **Optional quality mechanisms must be attributable.** Personality and Luna cannot be mandatory merely because they are plausible or cheap.
7. **Current package versus future authority.** This document is the reconciled pre-freeze state. The final Step-1 specification must explicitly promote, reject or leave configurable every consequential synthesis choice.
