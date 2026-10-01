# READ FIRST — Corpus Map + P0.7 Executable Baseline KB

> **Purpose of this file:** neutral navigation and epistemic control for the 20-file Jobbsøk_26 P0.9 context-curation corpus, followed by a focused historical baseline of the last verified executable framework, P0.7.
>
> **Do not treat this file's placement at `00_` as evidence that its substantive P0.7 content is more authoritative than later P0.8/P0.8.1/P0.9 material.** The `00_` prefix means only: *read the corpus map and authority rules first*.

## File navigation

1. **§0 — Corpus map and handling rules:** reading order, authority, source classes, 20-file manifest.
2. **§1 — P0.7 baseline provenance:** what was retained/omitted and why.
3. **§2–§4 — P0.7 system and evolution:** authority rules, implementation contract, P0.5.3→P0.6→P0.7 lineage.
4. **§5–§7 — Candidate/application boundaries:** authority model, claim ceilings, Norwegian CV/application doctrine.
5. **§8–§10 — Historical control registers:** relevant decisions, artifacts and open risks.
6. **§11 — Interpretation guardrails:** reusable substrate vs P0.7-specific policy that later versions may replace.


## 0. Fast operating instructions

Read this file first. Then inspect **files 02–18 broadly before using files 19–20 as analytical shortcuts**.

The intended epistemic sequence is:

```text
00  Corpus map + historical executable P0.7 baseline
 ↓
02–18  Primary historical / normative / review / research / user-decision evidence
 ↓
19  Derived cross-version analysis and direct P0.7 audit
 ↓
20  Current best derived P0.9 candidate synthesis
```

Files 19–20 are deliberately last because they are useful **derived syntheses**, not independent authority. Their polish, recency or comprehensiveness must never create circular authority over the underlying corpus.

### 0.1 Current project-state orientation

Use this only as an orientation map; verify details in the corpus:

- **P0.7:** latest actually implemented and test-backed local release represented in the corpus.
- **P0.8.0:** later formally adopted normative architecture; designed but not implemented.
- **P0.8.1:** mature preimplementation hardening/review layer; explicitly non-normative unless adopted.
- **P0.9:** current architecture target; substantially researched and partially decided, but the supplied historical corpus does not itself establish a formally frozen final P0.9 release.
- **File 20:** strongest current derived P0.9 synthesis; treat as a candidate to audit, not as pre-adopted truth.

### 0.2 Historical-label warning

The P0.7 KB reproduced/condensed later in this file was created when P0.7 was locally `CURRENT`. Therefore labels such as `CURRENT`, `CURRENT_SPEC`, `DECIDED/CURRENT`, etc. inside the P0.7 baseline mean **current at that historical P0.7 state**, not current across the later P0.8/P0.9 project.

### 0.3 Granular authority and supersession rule

Resolve authority **proposition by proposition**, never whole-document-by-whole-document.

Default precedence:

1. later explicit user correction / final decision;
2. earlier explicit user decision not superseded;
3. formally adopted normative specification within its scope/version;
4. explicitly accepted/adopted proposal;
5. verified implementation/test evidence and strong external evidence;
6. high-confidence analytical synthesis;
7. unresolved assistant proposal / hypothesis.

A newer source supersedes older information **only where it actually changes, narrows, expands, invalidates, or explicitly replaces that information**. Unaffected older information remains available.

When sources conflict, first check:

- scope;
- version;
- chronology;
- whether one statement is descriptive and the other normative;
- whether one is historical and the other current;
- whether a later statement deletes the problem surface that an earlier hardening rule addressed.

Do not silently convert an unresolved proposal into a decision.

### 0.4 Epistemic source classes

| Class | Meaning | Treatment |
|---|---|---|
| **PRIMARY / NORMATIVE** | Formally adopted specification or direct authoritative project source | Strongest historical authority within its actual scope |
| **USER-DECISION / RECONSTRUCTION** | Integration/KB material carrying explicit user decisions, corrections, chronology and terminal state | High-value for later overrides and inter-chat reconciliation; verify ambiguity against primary sources where possible |
| **REVIEW / HARDENING** | Critical review, proposed contract repair or preimplementation hardening | May refine the design but is not automatically normative |
| **RESEARCH / EVIDENCE** | External findings used to constrain decisions | Supports/weakens design assumptions; does not create user decisions |
| **INTERPRETIVE CONTEXT** | Personality/preferences/context adaptation | Bounded authority; never candidate factual authority |
| **DERIVED SYNTHESIS** | Later holistic analysis combining multiple sources | High-value shortcut/hypothesis; must not bootstrap its own authority |

### 0.5 Corpus manifest — 20 upload files

| # | Context filename | Epistemic role | Distinct reason it earns inclusion |
|---:|---|---|---|
| **00** | `00_READ_FIRST_CORPUS_MAP__P07_EXECUTABLE_BASELINE_KB.md` | Navigation + historical executable baseline | Establishes corpus handling rules and the P0.7 system that later versions evolve from |
| **02** | `02_P07_TO_P08_OBJECTIVE_SHIFT_QHAPPY_KB.md` | User-decision / evolution reconstruction | Captures the audit-driven `Q_happy` / selective-quality objective shift and causal bridge out of P0.7 |
| **03** | `03_PROJECT_INTENT_LLM_CONTEXT_REFERENCE.md` | High-density project intent | Compact objectives, constraints, design preferences and operating philosophy |
| **04** | `04_P07_P08_SELECTIVE_QUALITY_REDESIGN_HISTORY.md` | Evolution reconstruction | Preserves intermediate P0.7→P0.8 decisions before final P0.8 freeze |
| **05** | `05_P08_ARCHITECTURE_FINALIZATION_HISTORY.md` | Evolution / terminal-state reconstruction | Continues through actual P0.8 finalization; differs materially from file 04 |
| **06** | `06_P08_FINAL_NORMATIVE_SPECIFICATION.md` | **PRIMARY / NORMATIVE** | Formal P0.8.0 `FINAL_NORMATIVE_SPECIFICATION`; critical reference point for later review/deltas |
| **07** | `07_P08_CROSS_MODEL_REVIEW_ADJUDICATION.md` | Review adjudication | Resolves competing review suggestions and records which critiques survive or are rejected |
| **08** | `08_P081_CONSOLIDATED_PREIMPLEMENTATION_HARDENING.md` | Review / hardening | Strongest P0.8.1 contract-hardening source; explicitly non-normative until adopted |
| **09** | `09_P08_EXTERNAL_EVIDENCE_REVIEW.md` | Research / evidence | Tests P0.8 assumptions against external evidence and distinguishes supported vs pilot-dependent claims |
| **10** | `10_P09_BRAINSTORM_BRIEF_NON_NORMATIVE.md` | Design-space exploration | Broad P0.9 possibility space before convergence; explicitly non-normative |
| **11** | `11_P09_BRAINSTORM_REVIEW_DECISION_SPACE.md` | Structured decision space | Converts broad brainstorming into explicit forks/options/open decisions and P0.8.1 interactions |
| **12** | `12_P09_PREP_PACKAGE_V2.md` | P0.9 preparation | Later material v2 of prep package; improved research contract and decision scaffolding |
| **13** | `13_P09_ARCHITECTURE_OPTIMIZATION_CHAT_SUMMARY.md` | Parallel-chat reconstruction | Captures one P0.9 information-gathering/architecture-prep branch and its unresolved state |
| **14** | `14_P09_PARALLEL_PREP_CHAT_SUMMARY.md` | Parallel-chat reconstruction | Independent/overlapping prep branch; required to reconstruct non-linear evolution |
| **15** | `15_P09_EXTERNAL_EVIDENCE_REPORT.md` | Research / evidence | Completed P0.9 external evidence report on model/runtime/application/rendering/security/context assumptions |
| **16** | `16_PERSONALITY_CANONICAL.md` | Interpretive context | Canonical personality/work-style representation; not candidate-fact authority |
| **17** | `17_P09_PERSONALITY_FRAMEWORK_CONTEXT.md` | Proposed interpretive interface | P0.9-specific personality usage/authority boundaries and stage-consumption hypothesis |
| **18** | `18_P09_LATEST_INTEGRATION_SUMMARY_USER_DECISIONS.md` | **Later user-decision reconstruction** | High-priority terminal-state source containing later questionnaire answers, user decisions and current unresolved work |
| **19** | `19_P07_TO_LATEST_DEEP_EVOLUTION_DERIVED_ANALYSIS.md` | **DERIVED SYNTHESIS / direct audit** | Cross-version analysis plus direct inspection/test rerun of actual P0.7 build; validate consequential synthesis against sources |
| **20** | `20_P09_CURRENT_BEST_CANDIDATE_SPEC_DERIVED.md` | **DERIVED SYNTHESIS** | Strongest current integrated P0.9 candidate architecture; challenge rather than rubber-stamp |

> The absence of file number `01` is intentional: the former `01_P07_EXECUTABLE_BASELINE_KB.md` became this read-first file `00_...` so the map is encountered first without adding a 21st upload.

### 0.6 How to use files 19–20

Use them **after** broad exposure to 02–18.

They are allowed to:

- reveal cross-source patterns;
- reduce rediscovery cost;
- suggest reconciliations;
- identify likely latest-wins deltas;
- surface implementation facts discovered by direct audit.

They are **not** allowed to:

- override an explicit user decision merely by being newer;
- turn P0.8.1 proposals into adopted requirements without evidence;
- turn P0.9 open forks into settled decisions merely because a synthesis chose an option;
- erase valid older information that was never actually superseded.

### 0.7 Web-research boundary for the later context-curation run

Use the supplied corpus to reconstruct **project history, decisions and framework state**. Fresh web research must not rewrite that history.

Fresh web verification is appropriate only when a **current external fact** could materially affect the final P0.9 freeze or build, e.g. current model/Codex capabilities, current platform/tool constraints, or time-sensitive Norwegian application-channel facts. Keep such new evidence visibly separate from corpus-derived state.

---

# PART II — Focused historical baseline: Jobbsøk_26 P0.7

## 1. Provenance and scope of this baseline

This Part II is a **targeted, context-efficient extraction** from the historical file `Canonical_Conversation_KB_implementing_model_chat.md`.

It intentionally preserves the P0.7 information that can materially inform P0.9 context curation, architecture freeze or implementation:

- authority/canonicalization rules;
- P0.7 architecture and stage contracts;
- package contract;
- release/test evidence;
- exact implementation assets and hashes;
- P0.5.3→P0.6→P0.7 evolution;
- candidate-authority boundaries;
- application/CV/channel doctrine;
- relevant active decisions, artifacts and open risks.

It intentionally omits unrelated domains from the old all-purpose KB (hospital-dashboard internals, forms tooling, KAB analysis, unrelated forecasting repository detail, university complaint, health/household/hobbies, etc.). Those domains were present because the original KB canonicalized a much broader chat history; they do **not** add enough marginal value to the P0.9 context-curation task to justify their token cost here.

Detailed candidate project narratives are also compressed: P0.9 needs the **authority model, evidence ceilings and application doctrine** at this stage, not a second pseudo-authority copy of every candidate claim. The eventual context-source optimization step should operate on the actual canonical candidate source files rather than on this historical KB summary.

### 1.1 Historical source reliability

The original KB synthesized represented local workspace artifacts, release reports/manifests, candidate authority files and conversation state. Where P0.7 implementation facts are consequential, file 19 contains a later **direct build audit/test rerun** and should be used as corroboration. P0.7's own historical report nevertheless remains important because it records what the release claimed and how the architecture was intended to operate.

### 1.2 P0.7 state capsule

At the time represented by this baseline:

1. `Jobbsøk_26 P0.7` was the latest implemented local release.
2. It used a **manual, physically isolated four-stage workflow** with exactly three active scripts: `scripts/ingest.py`, `scripts/advance.ps1`, `scripts/finalize.py`.
3. Candidate facts were owned by three canonical authority files; `CV_BASELINE.md` was derived and explicitly non-authoritative.
4. The release reported **32 automatic tests passed, 2 PowerShell runtime tests blocked because PowerShell was unavailable, 0 failures**, controlled synthetic E2E success, rendered-output inspection, 52 release files and deterministic packaging.
5. **Real Terra/Sol production stages and a real vacancy pilot were not run.** P0.7 was technically implemented/test-backed, not empirically proven on live package quality.
6. Truth/source authority, bounded contribution claims, manual final review and manual submission were hard constraints.

---
## 2. Preserved P0.7 canonicalization / authority rules

### Authority and status model

- Authority order: `user correction/final choice > latest same-scope user statement > explicitly/operationally adopted output > user fact/constraint/preference > chat-contained evidence/implementation > unadopted assistant proposal > labeled inference`.
- Status vocabulary: `CURRENT`, `DECIDED`, `ADOPTED`, `PROPOSED`, `SUPERSEDED`, `REJECTED`, `UNCERTAIN`, `OPEN`.
- Adoption changes status, not provenance. An assistant proposal that was adopted remains assistant-originated with `status=ADOPTED`; provenance must never be rewritten as user-authored.
- Current authoritative state leads. Historical material is retained only when it explains a decision, correction, failure, dependency or continuation path.
- Apparent conflicts must first be resolved by scope, time, version and exception before being labeled contradictions.

### Value preservation

Protect every material user fact, expertise, goal, preference, instruction, constraint, terminology, correction pattern, project/workstream, fact/evidence/date/number/entity, decision/rationale/trade-off, requirement/acceptance criterion, implementation/architecture/process/artifact, exact identifier/path/version/field/formula/code/setting/label/product/model, dependency/risk/edge case, error/correction/rejected approach, open question/revisit trigger, and non-obvious causal or diagnostic model.

Under space pressure delete only, in order: filler, repetition, generic reconstructable explanation, duplicate examples, obsolete wording, low-value assistant exposition and low-impact detail. Do not delete a value-taxonomy item merely to shorten the file.

### Canonical integration rules

- One canonical location per fact; use cross-references elsewhere.
- Current state first; history compressed and visibly separated.
- Corrections and failures dominate the replaced approach instead of being buried as footnotes.
- Exact identifiers, formulas, paths, versions, labels and status boundaries are preserved.
- Facts, assumptions, inferences and uncertainties are separated.
- Coverage limitations must be explicit; in this optimized extraction they are stated in §1 and reinforced by the omission rationale there.

## 3. Preserved P0.7 implementation contract

### Purpose and normative precedence

- `PURPOSE`: produce complete, highly tailored Norwegian application packages that maximize interview probability for approved vacancies.
- `CURRENT_SPEC`: `upload/jobbsøk_26_P0.7.md` / locally represented P0.7 specification.
- P0.7 user-prompt precedence: current user prompt > `jobbsøk_26_P0.7.md` > three candidate authorities and original masters within their domains > compatible P0.6 code/assets > P0.6 reports/audit > historical P0.5/P0.7 drafts.
- P0.7 explicitly overrules P0.6's 4×10-/8×5 topology, the P0.6 24-prompt HappyPath, the earlier dual-prompt/multi-model P0.7 draft, and proposals requiring Luna/Ultra, memory, cache, agents or an orchestrator.
- A vacancy is already approved for production when it enters Stage 1. Stage 1 does not assess candidate fit.

### Locked architecture

| Component | Current contract |
|---|---|
| Physical stages | Four manually started, physically isolated stages |
| Prompt/model unit | One user prompt and one model per stage instance |
| Internal phase model | `Phase A → midpoint/checkpoint → Phase B source-first self-audit` in the same run |
| Stage 1 | Candidate-blind vacancy and hiring analysis; Terra Max |
| Stage 2 | Sol-owned evidence retrieval and package strategy; Sol Max |
| Stage 3 | Terra-owned native Norwegian drafting; Terra Extra High, selectively Max |
| Stage 4 | Sol-owned constructive Writer/Recruiter Mirror; Sol Extra High, selectively Max |
| Batch topology | 2 XL macroclusters of about 20 jobs; 2 evidence lanes per macrocluster; 4 miniclusters of about 10 jobs |
| Work waves | Stage 1/2: `10+10`; Stage 3/4: `5+5` |
| Standard HappyPath | 12 manually started prompts/chats: 2 Stage 1 + 2 Stage 2 + 4 Stage 3 + 4 Stage 4 |
| Identity anchor | `job_identity.json` propagated and cross-validated across stages |
| Stage 2 artifacts | `CLUSTER_EVIDENCE_BASE.md`, evidence lanes, `MINICLUSTER_SPLIT.json`, individual `package_blueprint.md` |
| Recovery | File-based `BATCH_STATUS.md`, `_DONE.md`, `BLOCKED.md` and continuation prompts |
| Rendering | Original Word-master-based DOCX/PDF rendering; manual semantic final approval |
| Submission | Always manual; never automated |

### Active scripts and active-path exclusions

Active scripts are exactly:

```text
scripts/ingest.py
scripts/advance.ps1
scripts/finalize.py
```

The active path excludes API/SDK orchestration, automatic `codex exec`, session-ID/resume systems, retry engines, databases, general state machines, semantic caches, embeddings/vector databases, `working/` layers, Luna/Ultra as default routing, subagents/custom agents, multi-agent debate, LLM-as-judge, automatic employer research, automatic submission, `FINALIZE_REPORT.md` and `output/INDEX.md` generation.

### Stage contracts

#### Stage 1 — candidate-blind vacancy analysis

- Input: one macrocluster's `vacancy.md`, optional `notes.md` and shared Norwegian-core runtime sections only.
- Forbidden: candidate authorities, candidate fit, evidence selection, package drafting and later-stage output.
- Phase A: normalize employer/title/channel, separate formal must-haves, preferences, responsibilities and marketing language; identify selection regime, dominant employer problem and ranked decision tests.
- Midpoint: save and validate `job_identity.json` and first complete `vacancy_analysis.md` against employer/title/unit/reference/language/channel.
- Phase B: reread source vacancy and notes, remove unsupported interpretations, repair missing formal requirements and channel limits, save only authoritative output.
- Required headings: `# Job identity and channel`, `# Explicit vacancy facts`, `# Formal must-have requirements`, `# Preferred requirements`, `# Core responsibilities`, `# Dominant employer problem`, `# Ranked decision tests`, `# Expected seniority and collaboration signals`, `# Selection regime and tone`, `# Channel requirements and limits`, `# Ambiguities resolved`, `# What Stage 2 must solve`.
- Mechanical block only for unreadable/substantially incomplete vacancy, missing employer/title or empty/invalid model output. A weak fit is not a Stage 1 blocker.

#### Stage 2 — evidence retrieval and strategy

- Input: complete Stage 1 output plus all three candidate authorities, `CV_BASELINE.md`, calibration and relevant runtime sections.
- Phase A: read all vacancy analyses before retrieval; build one cluster evidence universe with two evidence lanes; map candidate facts to actual hiring questions.
- Midpoint: save `CLUSTER_EVIDENCE_BASE.md` and `MINICLUSTER_SPLIT.json`; every job appears exactly once in A or B; normal split is 10/10, with explained 8/12–12/8 allowed.
- Phase B: reopen selected sources and audit personal contribution, lifecycle, channel role, redundancy and alternative route before saving each blueprint.
- A blueprint contains: primary identity, employer problem, shortlist thesis, two main evidence items, optional differentiator, strongest alternative route, objection reframes, CV override plan, application plan, portal plan, do-not-undersell items, private borderline claims and Stage 3 complexity note.
- After Stage 2, clusterbase, split and blueprints are locked; later stages may verify a concrete fact but cannot silently redo broad retrieval or strategy.

#### Stage 3 — native Norwegian drafting

- Input: one locked Stage 2 minicluster; candidate authorities only for concrete fact checking; baseline/package/calibration.
- Phase A: create schema-valid `draft_package.json` with only dynamic CV overrides and native Norwegian package content.
- Midpoint: validate schema, identity, baseline version, employment IDs, letter/portal limits and channel roles.
- Phase B: reread vacancy and evidence, audit `jeg/vi`, lifecycle, Bokmål, motivation, channel complementarity and no-new-facts.
- `profile`: route-specific identity/value proposition, not a generic biography or tool list.
- `key_competencies`: 4–8 prioritized, scannable, functionally grouped competencies.
- `experience_overrides`: only known baseline employment IDs where material value exists; normally `problem/omfang + handling + method/control + supported use/result`.
- Drafting cannot render, run Stage 4, call APIs or issue a semantic release verdict.

#### Stage 4 — constructive Writer/Recruiter Mirror

- Input: Stage 3 package, locked blueprint/evidence, relevant vacancy/analysis, package contract and calibration.
- Phase A: edit for first-20-second clarity, employer specificity, understandable value, `jeg/vi`, Bokmål rhythm and channel complementarity.
- Midpoint: save complete provisional `final_package.json`, validate schema/identity/baseline/portal limits and forbid new employment IDs.
- Phase B: reread evidence/vacancy, repair undersell, oversell, genericity, technical overload and repetition; run employer-swap and batch-variation checks.
- Stage 4 is an editor, not a judge. It must not return `PASS`, `REVISE`, `BLOCK`, `GO` or `NO-GO` as a semantic verdict.
- Private `review_flags.md` has exactly the headings `# Must verify`, `# Strong but defensible` and `# Optional polish`.
- Only mechanical unusability creates `BLOCKED.md`; one blocked job must not stop independent jobs.

### P0.7 package contract

- `contract_version`: constant `0.7`.
- `source_stage`: `STAGE3_DRAFT` or `STAGE4_FINAL`.
- Required top-level fields: `contract_version`, `source_stage`, `job`, `cv_overrides`, `application`, `portal_answers`.
- Job fields: `job_id`, `batch_id`, `macro_cluster_id`, `mini_cluster_id`, `employer`, `title`, `language`, `letter_required`; optional `unit` and `reference`.
- ID patterns: `B[0-9]{2}`, `B[0-9]{2}_C[0-9]{2}_[a-z0-9_]+`, `B[0-9]{2}_C[0-9]{2}[AB]_[a-z0-9_]+`, and `B[0-9]{2}_J[0-9]{3}_[a-z0-9_]+`.
- `language` is `nb-NO`.
- Dynamic CV fields: `baseline_version`, profile length 80–1400, 4–8 unique key competencies, 1–4 experience overrides, 1–5 bullets per override, known uppercase employment IDs only.
- `application`: object with `opening`, 1–5 `body_paragraphs` and `closing`, or `null` when `letter_required=false`.
- `portal_answers`: at most 20; every answer carries `question_id`, exact question, answer, `max_words` and `max_chars`; limits are hard.
- Unknown top-level or nested fields are rejected.
- Finalizer additionally requires complete expected-versus-finished job reconciliation, `STAGE4_FINAL`, matching `CV_BASELINE.md`, consistent identity/path/batch/cluster/employer/title, Stage 4 `_DONE.md`, no active blocker, required review headings, known employment IDs, all `always_include` roles, rendered or explicitly rejected overrides, CV ≤2 A4 pages, application ≤1 A4 page, `unit`/`reference` rendering, no internal IDs/placeholders/tags and no overwrite without `--force`.

### P0.7 release evidence

| Evidence | Result | Provenance |
|---|---|---|
| Release root | `Jobbsok_26_P0.7/` | Local artifact |
| Release ZIP | `Jobbsok_26_P0.7_Release.zip` | Local artifact |
| File count | 52 release files; 52 ZIP members | `docs/FILE_MANIFEST.md`, archive verification |
| ZIP integrity | CRC valid; no duplicate members; member order matches release | `Jobbsok_26_P0.7_Archive_Verification.json` |
| Deterministic hash | `c74565ceb32900beba4b912e1cec93abe68039f83a29da6952f7ad9f57feb1a8` | Archive verification and prior final report |
| Automated suite | 34 total; 32 PASS; 2 skipped/blocked because PowerShell absent; 0 FAIL | `docs/TEST_REPORT.md` |
| Visual QA | 5 DOCX-rendered pages and 5 finalizer-PDF pages inspected; A4, no clipping/blank error pages/tags/private flags | `docs/TEST_REPORT.md` and prior implementation output |
| Controlled E2E | Synthetic vacancy → ingest → representative Stage 1/2/3/4 → check-only → DOCX/PDF: PASS | Test report |
| Real model stages | `NOT RUN` | Test report |
| Real vacancy pilot | `NOT RUN` | Test report |
| BLOCKED_ASSET | None | Test report |
| PowerShell runtime | `BLOCKED`; exact Windows command remains `pwsh -NoProfile -File .\scripts\advance.ps1 -Cluster B01_C01_process_digitalization -Root .` | Test report |

### P0.7 implementation assets

- `context/Work_experience.md`: current work authority, content version 2.4.0, verified/updated 2026-07-29.
- `context/Education.md`: education authority, content version 2.3.0, verified 2026-07-23, updated 2026-07-26.
- `context/Other_high_value_information.md`: identity/routing/AI/workstyle authority, content version 2.3.0, verified 2026-07-23, updated 2026-07-26.
- `context/CV_BASELINE.md`: derived verified baseline 0.7.0, verified 2026-07-31.
- `context/NORWEGIAN_APPLICATION_CORE.md`, `PACKAGE_CONTRACT.md`, `PERSUASION_CALIBRATION.md`: active runtime contracts.
- `context/templates/CV_MASTER.docx` and `APPLICATION_MASTER.docx`: original A4 content-control masters.
- Four stage `AGENTS.md` files, `MODEL_ROUTING.md`, tests and fixtures.
- Frozen authority/master hashes:

```text
Work_experience.md       0b39a5105f0d809d1bc9a917665bc69c619eb059253a779079b37304b49a2f9d
Education.md             75e238890215cbc02c3bc59cdaaeb43f467ae7d512e9b5a9c4723ccc0c4580f8
Other_high_value_information.md
                         58a8f88f9eb627847152d684b19d7938c42da7d173a57a7fff58728a25ae5bf8
CV_MASTER.docx           c3809748fe26dd5a7ae0a146d940a15e1b3326036ae5f7fac9fd2be02292e8c5
APPLICATION_MASTER.docx  dfd24125f921863da23932b8be3255df51cc8a4ee9a97c6a602a33dedb241409
```

## 4. Preserved release-evolution context

### Version register

| Version/artifact | Status | What it established | Replaced by / consequence |
|---|---|---|---|
| P0.3/P0.4/P0.5 persuasion-first releases | `SUPERSEDED/HISTORICAL` | Early candidate sources, Norwegian guidance, templates and persuasion-first architecture | P0.5.2/P0.5.3 and later Codex-native releases |
| P0.5.2 Language Aligned | `SUPERSEDED` | Language-aligned production baseline and runtime/source structure | P0.5.3 production candidate |
| `Jobbsok_26_Phase_0.5.3_Production_Candidate` | `GENERATED_NOT_APPLIED` in its own release report | Enforcement, retrieval, source authority, channel roles, fail-fast, Recruiter’s Mirror, claim/status control and deterministic DOCX checks | Its active ideas were used as source for P0.6/P0.7; the candidate itself was not an active project cutover |
| `Jobbsok_26_P0.5.3_Codex_MVP_Release` | `IMPLEMENTED_HISTORICAL` | Four physically isolated model calls: vacancy analysis, evidence strategy, Norwegian writer, constructive recruiter mirror; structured outputs, source hashes, CV/application/portal model and offline E2E | API/model-orchestrator path removed from active P0.6/P0.7 path |
| P0.5.3 operational/production candidate | `SUPERSEDED` | One-message/three-pass production workflow, manual submission, three authorities, two masters | P0.6 manual four-stage system |
| P0.6 | `SUPERSEDED_BY_P0.7` | Manual four-stage physically isolated Codex flow, 24-prompt/40-job HappyPath, dynamic CV baseline merge, three scripts, original masters | P0.7 changed topology, stage waves and contract hardening |
| P0.7 | `CURRENT` | 12-prompt 2-XL/4-mini topology, 10+10/5+5 waves, identity anchor, evidence lanes, P0.6.1 hardening and current release packaging | No later implementation is present in accessible corpus |

### P0.5.3 production-candidate decisions

- Candidate facts, stable claim IDs and field schemas were explicitly unchanged.
- Canonical ownership: Project instructions for runtime/ports; `Work_experience.md` for work facts/status/ceilings; `Education.md` for degrees/study; `Other_high_value_information.md` for identity/routing/AI/workstyle; Norwegian guide for selection/channel/package QA; language norms for Bokmål; DOCX masters for layout only.
- One primary route, one employer problem, one thesis, two main cases and at most one subordinate differentiator.
- Evidence roles: `BACKBONE`, `ENABLER`, `CV_ONLY`, `RESERVE`.
- Status must remain multidimensional: delivery status, actual use/adoption, Vegard's current ownership and verified effect are separate axes.
- A new global reverse index was rejected as duplicate/overprompting; local `CROSS_REF` metadata for `PRJ-03/04/08` was piloted but not promoted because recall did not improve and precision fell to 0.789; `BRIDGES_TO` was not promoted.
- No automatic learning from approved prose; candidate source maintenance remains separate.
- P0.5.3 release report: 49/49 gates, 23/23 static QA, 21/21 regression scenarios, 7/7 script tests, 2/2 Skill validation, 18/18 visual pages, 35/35 claim IDs and 81/81 stable IDs preserved. Retrieval A/B recall/precision were 1.000/1.000; cross-reference variant C reduced precision.
- P0.5.3 release was `GENERATED, IKKE ANVENDT`; no active cutover/smoke test was claimed.

### P0.5.3 Codex MVP historical implementation

The earlier Codex-MVP release was reported with:

- four model calls and no model-based semantic veto after production;
- three separate facts authorities with SHA-256 hashes;
- vacancy, evidence strategy, Norwegian writer and constructive recruiter mirror models;
- CV, application and portal models;
- call-specific runtime cores and operational prompts;
- one operator command with safe `--resume`;
- separate `final_package.json` and `private_review_flags.json`;
- professional A4 masters;
- `responses.parse`, `text_format`, `output_parsed` and structured outputs;
- 21/21 tests, offline four-call E2E, Phase 0 smoke, 5/5 schema conversion, 6/6 visual pages, 55/55 archive members and deterministic double-build;
- ZIP SHA-256 `bd98fc1fac1124d5bca4b91f92417da54ddd810dd10de723f44bcd8c727a3ee6`;
- real vacancy/live model run not performed.

This is implementation history, not the current architecture. P0.6 removed the active API/orchestrator route.

### P0.6 historical implementation

- Manual, physically stage-isolated four-stage Codex workflow; no model runner/API orchestration, automatic semantic gate, employer research or submission.
- Candidate-blind Stage 1; cluster retrieval/blueprints Stage 2; dynamic-only native Norwegian writing Stage 3; constructive non-veto Recruiter Mirror Stage 4.
- 24 standard prompts for 40-job HappyPath: four macrocluster prompts in Stages 1–2 and eight minicluster prompts in Stages 3–4.
- Dynamic CV rendering from verified static baseline plus bounded profile, competencies and known-employment overrides.
- Exactly `ingest.py`, `advance.ps1`, `finalize.py`; strict package contract; private flags; original masters.
- P0.6 release evidence: 30 tests passed, 3 PowerShell-dependent skips, 10/10 visual pages, 49/49 files, CRC/deterministic archive, no `BLOCKED_ASSET`.
- P0.6 ZIP SHA-256 `6b40516a7fa40a07de09c8df20fa7087a1b48d02845f6a3448ea16733fc32a83`.
- P0.6 blockers: PowerShell unavailable; real vacancy and manual Stage 1–4 sessions not run.

P0.7 retained this substrate but changed the topology and hardening requirements. P0.6 remains locally available and must not be described as current.

## 5. Candidate authority model at the P0.7 baseline

### Authority files

| File | Domain owner | Current status |
|---|---|---|
| `context/Work_experience.md` | employment, projects, work-derived competence, claims, lifecycle, results and ceilings | `PRODUKSJONSKLAR`; pack 0.5.3/content 2.4.0; verified/updated 2026-07-29 |
| `context/Education.md` | degrees, study status, course evidence, academic capability and education ceilings | `PRODUKSJONSKLAR`; content 2.3.0; verified 2026-07-23, updated 2026-07-26 |
| `context/Other_high_value_information.md` | identity/contact, role positioning, languages, trust/service, AI-enabled work, workstyle and cross-file evidence rules | `PRODUKSJONSKLAR`; content 2.3.0; verified 2026-07-23, updated 2026-07-26 |

P0.7 `CV_BASELINE.md` version 0.7.0 is derived, verified 2026-07-31, and explicitly cannot create facts. Its precedence is `Work_experience.md > Education.md > Other_high_value_information.md` only for rendering reconciliation.

### Identity and contact

| Field | Approved value | Boundary |
|---|---|---|
| Name | `Vegard Håland` | Use `Haaland` only where `å` is unsupported or required |
| Phone | `+47 905 26 886` | Approved contact field |
| Email | `vegard-haaland@outlook.com` | Older Hotmail address is replaced |
| Location | `Oslo, Norge` / baseline `Oslo` | No street address, age or date of birth as standard |
| Formal title | `Rådgiver Økonomi og IKT` | Do not replace with leader/data scientist/AI engineer |
| Core thesis | `Fra uoversiktlige problemstillinger til etterprøvbare beslutningsgrunnlag.` | Adapt to vacancy; do not paste as universal prose |

### Current OUS chronology

- Employer: Oslo universitetssykehus HF, March 2023–present.
- Formal title: `Rådgiver Økonomi og IKT`.
- BAR, Stab: operational placement March–November 2023.
- Formal position change to Analyseavdelingen: 1 June 2023.
- First working day in Analyseavdelingen: 1 December 2023.
- Current operational placement: Direktørens stab, Analyseavdelingen, December 2023–present.
- Work domains: hospital finance, staffing, activity/DRG, patient flow/capacity and management information.
- Participated in the four-person founding group for Analyseavdelingen with the department leader and two colleagues.

### Stable CV employment IDs

| ID | Employer/title/unit | Period | Status/usage |
|---|---|---|---|
| `EMP_OUS_ANALYSE` | OUS — Rådgiver Økonomi og IKT; Direktørens stab – Analyseavdelingen | 12.2023–d.d.; group period 03.2023–d.d. | `CURRENT`, always include |
| `EMP_OUS_BAR` | OUS — Rådgiver Økonomi og IKT; Barne- og ungdomsklinikken – Stab | 03.2023–11.2023 | `HISTORICAL`, always include |
| `EMP_TKS_HEIS` | TKS Heis — Hjelpearbeider | 07.2015–08.2021 | `HISTORICAL`, always include; tested as older override |
| `EMP_AHLSELL` | Ahlsell — Butikkmedarbeider/vikar, Auglendsmyra, Stavanger | 02.2015–04.2015 | `HISTORICAL`, always include |
| `EMP_LUFTFORSVARET` | Luftforsvaret — Vakt- og sikringssoldat, Sola | 03.2014–02.2015 | `HISTORICAL`, always include |
| `EMP_SECTOR_ALARM` | Sector Alarm — Sikkerhetskonsulent, Stavanger | 10.2013–03.2014 | `HISTORICAL`, always include |

### Education chronology

| ID | Institution/program | Period/status | Approved use |
|---|---|---|---|
| `EDU_UIA_AI` / `EDU-001` | Universitetet i Agder — five-year master programme in artificial intelligence | 2024–d.d.; `Pågående` | Technical supplement; do not imply completion, pace or AI-engineer status |
| `EDU_NTNU_ECON` / `EDU-002` | NTNU — Master i samfunnsøkonomi | 2020–2022; `Fullført` | Strong economics, econometrics, quantitative and time-series foundation |
| `EDU_UIB_ECON` / `EDU-003` | Universitetet i Bergen — Bachelor i samfunnsøkonomi | 2017–2020; `Fullført` | Broad economics, statistics/econometrics, public economics, finance and business economics |
| `EDU_CALGARY` / `EDU-004` | Ernest Manning High School, Calgary — science and advanced mathematics | 2011–2013 | International education/English context; no Norwegian-equivalence claim |

### Languages, trust and service

- Norwegian: mother tongue.
- English: fluent written and spoken.
- Trust roles: board member/resident representative at Solheimslien student housing 10.2017–01.2019; treasurer and deputy chair 01.2019–01.2020; chair and treasurer 01.2020–08.2020.
- Course: Sanitet nivå 2, 04.2014.
- CV reference text: `Oppgis ved forespørsel.`

## 6. Candidate-evidence boundaries relevant to framework design

### Professional operating pattern

Vegard is a cross-disciplinary analyst/adviser whose work combines hospital operations, economics, BI, data, technical implementation, budgeting/forecasting, benefits work, governance and stakeholder communication. The recurring delivery pattern is:

```text
Forstå → Avgrense → Strukturere → Bygge → Kontrollere → Forbedre
```

This supports functional/technical leadership, principal implementation or integration within bounded projects. It does not establish formal line management, enterprise-architecture ownership, enterprise governance authority or sole authorship of team deliverables.

### Cross-cutting competence

- Health/economics/operations: hospital finance, staffing, activity/DRG, patient flow/capacity, public-sector and regulated context.
- BI/reporting: Power BI, DAX, Power Query M, semantic models, star schemas, decision support, data quality and user-oriented reporting.
- Data engineering/integration: SQL, schema/relational modeling, ETL/M, source precedence, null/type handling, YAML/JSON/configuration, repository structure and dependency awareness.
- Automation/implementation: strongest documented technical specialization is Excel/VBA; also formulas, named ranges, Office integration, DAX, Power Query, R, Python, Stata, Git/GitLab and testing.
- Analysis/modeling: descriptive/diagnostic/predictive/decision analysis, time-series reasoning, temporal holdouts, leakage/target controls, proxy models, scenario analysis and transparent assumptions.
- Process/digitalization: accounting/reporting automation, ERP transition tooling, requirements, workflow, standardization, onboarding, workshops and controlled implementation.
- Governance/quality: definitions, source hierarchy, audit trails, reconciliation, validation, privacy-aware review, change control, acceptance criteria, ownership and uncertainty.
- Communication: executive/managerial decision support, technical/domain translation, workshops, documentation, onboarding and handover.

### Approved measures and result ceilings

| Measure/signal | Approved use | Prohibited upgrade |
|---|---|---|
| Four-person analysis department | team/context scale | sole department ownership |
| Approx. 1.5 months/3 months BAR ramp-up | learning and takeover speed | expert-from-day-one/all-OUS close |
| REGERP tools used relatively frequently by advisers in several clinics | cross-clinic operational adoption | exact count, savings or central ERP ownership |
| Complete `budsjetthjelpeark.xlsx` built by Vegard | personal artifact ownership | ownership of inherited main models/budget |
| One rounded monthly DRG estimate matched actual | narrow forecast observation | generalized accuracy/performance |
| 80–90% dashboard DAX; almost all semantic model; most ETL/M | contribution scale | all dashboard content/visuals |
| Dashboard owner approx. Aug. 2025–Feb. 2026 | historical lifecycle | current ownership |
| Approx. 15 worksheets/78 global names | workbook scale | exact current architecture without verification |
| Approx. 20-year-old inherited tool | legacy context | original creation |
| Approx. 50 stakeholders | process scale | personal ownership of all change |
| Hospital-wide benefits framework active approx. 2.5 years later | durability/adoption | personal measured effect |
| 14/90/365-day forecasting horizons; approx. 40,000 lines | project scale | production deployment/performance |
| Five-workbook STE architecture | designed scope | completed adoption/benefits |

### Explicit work-claim prohibitions

Do not claim all-OUS month-end close, formal accounting/controller leadership, year-end close, central REGERP/Oracle ownership, all BAR projects/budget/reporting, quantified BAR savings, original budgeting-tool creation, current dashboard ownership, original XGBoost, completed Prophet/Chronos/ensemble, production forecast deployment, mature enterprise MLOps/CI/CD, enterprise Fabric/data-governance/AI-governance/security authority, sole authorship of the benefits framework, hiring authority or formal people leadership.

## 7. Norwegian application / CV / recruiter-system doctrine at P0.7

### Route and identity logic

The candidate's broad thesis is not a fixed job title. Select the narrowest route that covers the employer's decisive tests with the fewest unsupported bridges:

| Route ID | Identity direction | Primary evidence |
|---|---|---|
| `ROLE-PROCESS-01` | Economics/IT adviser with finance-process improvement, digitalization and implementation | BAR, `PRJ-03`, `PRJ-04`; support `PRJ-01/02/08` |
| `ROLE-BI-01` | Economics/BI and management-information specialist | `PRJ-01`, `PRJ-02`, OUS scope |
| `ROLE-FORECAST-01` | Economics/analytics adviser with forecasting architecture/validation | `PRJ-05`, econometrics/time-series education |
| `ROLE-BENEFITS-01` | Economics/benefits adviser using transparent assumptions and governance | `PRJ-04`, `PRJ-06` |
| `ROLE-DIGITAL-01` | Business–technology adviser for requirements, automation and controlled implementation | `PRJ-03`, `PRJ-08`, `PRJ-09` |
| `ROLE-AI-01` | Domain-heavy adviser for human-governed AI-enabled delivery | AI workflow evidence plus `PRJ-05`; subordinate unless AI is decisive |

Tie-breaker: direct criterion coverage, fewest bridges, clearest personal contribution, supported use/adoption/varighet and short interview defensibility. BI/KI must not displace more direct process/economics/change evidence.

### Candidate and education positioning

- Economics is the strongest formal base: completed NTNU economics master and UiB economics bachelor, with econometrics, applied empirical design, time-series econometrics, mathematics, public economics, labour economics, competition, finance, business economics and independent research.
- The UiA AI master's programme is ongoing and must remain `pågående`; it supplements rather than replaces work-derived technical evidence.
- Academic subjects establish formal background/exposure, not professional mastery. `INFO132` supports Python fundamentals; `IKT111`, `IKT105`, `IKT101` and `MA-180` are course-level exposure unless further evidence is available.
- For finance/process roles, lead with completed economics degrees plus direct OUS finance/process work and `PRJ-03`; do not lead with the ongoing AI programme.

### AI-enabled work positioning

The defensible AI claim is a human-governed AI-enabled delivery workflow, not generic prompt expertise:

```text
Clarify problem → structure context → define authority/constraints → decompose → delegate bounded task → require proof/tests → review exceptions → deliver/handoff → preserve human accountability
```

Safe terms: AI-assisted analysis/development, human-in-the-loop workflow, coding-agent facilitation, context/instruction design, AI-output validation, risk-aware automation and responsible GenAI adoption. Do not claim LLM engineering, enterprise AI governance, production AI deployment or sole manual authorship of agent-assisted repositories.

### Evidence and channel doctrine

- Use direct problem similarity before loose keyword matching.
- For each evidence item preserve source/heading, core fact, personal contribution, team context, lifecycle, verified use/result, employer problem, safe strong formulation and `Do not claim`.
- Normally use at most two main cases and at most one subordinate differentiator.
- Transform each case as `fact → explicit criterion/realistic need → strategic value → channel role`; do not invent hidden employer psychology.
- CV: complete, reverse-chronological, normally two A4 pages; baseline owns contact, formal chronology, education, languages, stable sections and all `always_include` roles; dynamic overrides only change profile, competencies and known employment bullets.
- Application: normally one A4 page without body headings; opening names role/problem/route; body uses one or two decisive proof passages; closing is calm and conversation-opening.
- Portal: answer the exact question first, within exact word/character limits; do not turn a single portal answer into a miniature application.
- Interview reserve: retain technical depth, alternatives, limits and extra cases in private blueprint/clusterbase rather than crowding the written package.
- Stage 4 checks first-20-second clarity, employer-swap specificity, natural Bokmål, `jeg/vi`, lifecycle, no-new-facts and variation across jobs.

### Norwegian language and persuasion calibration

- Use natural, active, calm and professionally heavy Bokmål.
- Keep actor/action/object close; use strong supported verbs; avoid unnecessary hedging.
- Avoid Americanized self-promotion, `brenner for`, hollow company praise, imported English syntax, mechanical three-part symmetry, long nominal chains, tool dumping and announcement echo.
- Strength may be stated clearly when supported; truth is the ceiling, not a reason for weak prose.
- Preserve team context near strong personal claims; do not let vague `vi` hide documented main responsibility.
- Lifecycle vocabulary must distinguish `CONCEPT`, `PILOT`, `IN_DEVELOPMENT`, `IMPLEMENTED`, `IN_USE`, `COMPLETED` and `DECOMMISSIONED`.
- Never make team work solo, active development production, a pilot an implemented standard, organizational scale a personal effect, functional influence formal authority, course content professional expertise or one observation general model accuracy.

### Current P0.7 baseline contract

The baseline version is `0.7.0`. `always_include=true` for all six employment entries, including older TKS Heis, Ahlsell, Luftforsvaret and Sector Alarm. Dynamic overrides must use known IDs, including older IDs when the schema permits them; the finalizer tests `EMP_TKS_HEIS` explicitly.

## 8. Relevant P0.7-era decision register

| Domain | Decision/change | Status | Replaced-by | Rationale/consequence |
|---|---|---|---|---|
| Jobbsøk_26 | Three candidate authorities own candidate facts | `DECIDED/CURRENT` | None | Prevents memory, vacancy text, generated prose and assistant proposals from creating facts |
| Jobbsøk_26 | `CV_BASELINE.md` is derived, not authoritative | `DECIDED/CURRENT` | None | Enables deterministic rendering without expanding factual authority |
| Jobbsøk_26 | P0.7 manual fourstage physically isolated workflow | `ADOPTED/CURRENT` | None | Locked by P0.7 user specification and implemented in release |
| Jobbsøk_26 | 2 XL macroclusters, 4 miniclusters, 12 prompts, 10+10/5+5 waves | `ADOPTED/CURRENT` | Replaces P0.6 4×10/8×5/24-prompt topology | Reduces prompt count while preserving stage isolation and batch structure |
| Jobbsøk_26 | One prompt/model per stage instance with internal Phase A/B | `ADOPTED/CURRENT` | Replaces earlier dual-prompt/multi-model draft | Keeps context continuity while enforcing checkpoint/self-audit |
| Jobbsøk_26 | Terra/Sol routing: Terra Max → Sol Max → Terra XHigh → Sol XHigh, selective Max | `ADOPTED/CURRENT` | Replaces P0.5.3 API model route | Manual model selection and stage ownership |
| Jobbsøk_26 | Exactly three active scripts | `ADOPTED/CURRENT` | Replaces API runner/orchestrator | KISS, manual operator boundary and no hidden external execution |
| Jobbsøk_26 | `job_identity.json` cross-stage anchor | `ADOPTED/CURRENT` | New in P0.7 | Prevents employer/title/path/batch/cluster drift |
| Jobbsøk_26 | `CLUSTER_EVIDENCE_BASE.md` with two lanes and individual blueprints | `ADOPTED/CURRENT` | New/expanded in P0.7 | Allows cluster-level retrieval without collapsing distinct job strategies |
| Jobbsøk_26 | Stage 4 is constructive non-veto Mirror | `DECIDED/CURRENT` | Replaces judge/gate architecture | Strongest defensible package plus private flags; no semantic PASS/NO-GO |
| Jobbsøk_26 | No automated research/submission/contact | `DECIDED/CURRENT` | None | Human responsibility and privacy/control boundary |
| Jobbsøk_26 | Original CV/application masters retained byte-identically | `ADOPTED/CURRENT` | None | Preserves professional design and controlled rendering |
| Jobbsøk_26 | P0.6 API/orchestrator removed from active path | `DECIDED/HISTORICAL` | P0.7 manual path | P0.6 migration doctrine and P0.7 specification prohibit API runner |
| Jobbsøk_26 | P0.5.3 local cross-references/BRIDGES_TO not promoted | `REJECTED/HISTORICAL` | Existing global index/owner sections | Evaluation showed no recall gain and precision loss/maintenance debt |
| Candidate | Norwegian, truthful, persuasion-first, interview-maximizing output | `DECIDED/CURRENT` | None | Persuasion operates inside factual ceilings |
| Candidate | One route, one employer problem, two main cases, at most one differentiator | `ADOPTED/CURRENT` | None | Prevents generalist blur and technical novelty bias |
| Candidate | Functional/technical lead framing allowed; formal line management not inferred | `DECIDED/CURRENT` | None | Matches documented scope and avoids title inflation |
| Candidate | OUS chronology uses operational dates for delivered work | `DECIDED/CURRENT` | None | Separates BAR, formal position change and Analyseavdelingen start |
| Candidate | BAR/PRJ-10 claim IDs approved as owner-file delta | `ADOPTED/OPEN` | Pack-level claim-index sync | New evidence is approved locally but global sync remains pending |

## 9. Relevant P0.7-era artifact register

| Domain | Artifact/implementation | Status | Critical identifiers/logic | Remaining issue |
|---|---|---|---|---|
| Jobbsøk | `Jobbsok_26_P0.7/` | `CURRENT` | Manual fourstage release; three scripts; authority files; original masters; 52-file manifest | Windows PowerShell runtime and real vacancy pilot remain |
| Jobbsøk | `Jobbsok_26_P0.7_Release.zip` | `CURRENT/LOCKED` | SHA-256 `c74565ceb32900beba4b912e1cec93abe68039f83a29da6952f7ad9f57feb1a8`; valid CRC; 52 members | Must be installed/preflighted in target Windows environment |
| Jobbsøk | `Jobbsok_26_P0.7_Archive_Verification.json` | `CURRENT/EVIDENCE` | `member_count=52`, no duplicates, deterministic rebuild | No issue beyond runtime tests |
| Jobbsøk | `Jobbsok_26_P0.7_pre_final_test_backup/` and ZIP | `BACKUP` | Separate pre-final backup of P0.7 source tree | Preserve for rollback/audit |
| Jobbsøk | `docs/IMPLEMENTATION_REPORT.md` | `CURRENT/EVIDENCE` | Inventory, migration, hardening, assets, blockers | Must remain aligned if release changes |
| Jobbsøk | `docs/TEST_REPORT.md` | `CURRENT/EVIDENCE` | 32 PASS, 2 blocked, 2 production activities not run | PowerShell/live pilot still open |
| Jobbsøk | `docs/FILE_MANIFEST.md` | `CURRENT/EVIDENCE` | Exact 52-file release manifest | Update only with a new locked build |
| Jobbsøk | `Jobbsok_26_P0.6/` and `Jobbsok_26_P0.6_Release.zip` | `SUPERSEDED/BACKUP` | 49 files; P0.6 manual 24-prompt topology; ZIP hash `6b40516a7fa40a07de09c8df20fa7087a1b48d02845f6a3448ea16733fc32a83` | Historical evidence only |
| Jobbsøk | `Jobbsok_26_P0.5.3_Codex_MVP_Release/` | `SUPERSEDED/HISTORICAL` | Four-call API/structured-output MVP; ZIP hash `bd98fc1fac1124d5bca4b91f92417da54ddd810dd10de723f44bcd8c727a3ee6` | Do not restore active API path |
| Candidate | `Work_experience.md` | `CURRENT/AUTHORITY` | `CLM-BAR-*`, `CLM-PRJ10-*`, content 2.4.0 | Pack-level claim index delta pending |
| Candidate | `Education.md` | `CURRENT/AUTHORITY` | `EDU-001`–`EDU-004`, `CLM-EDU-001/002` | Exact grade/thesis/progress details bounded |
| Candidate | `Other_high_value_information.md` | `CURRENT/AUTHORITY` | `ID-*`, `ROLE-*`, `CLM-AI-*` | Exact current role-specific use remains vacancy-dependent |
| Candidate | `CV_BASELINE.md` | `CURRENT/DERIVED` | Baseline 0.7.0; six employment IDs; `always_include` | Never elevate to fact authority |
| Candidate | `CV_MASTER.docx`, `APPLICATION_MASTER.docx` | `CURRENT/ORIGINAL ASSETS` | Content-control masters; frozen hashes in §3 | Use original-master rendering |

## 10. Relevant open/risk items carried from the P0.7 baseline

| ID | Domain | Item | Status | Risk/consequence | Next action |
|---|---|---|---|---|---|
| `OPEN-001` | P0.7 | `advance.ps1` actual runtime not executed because PowerShell is absent | `BLOCKED` | Stage 2→3 Windows gate is statically/fixture-tested, not runtime-proven here | Run exact PowerShell commands on Windows |
| `OPEN-002` | P0.7 | Real Terra/Sol manual stages not executed | `NOT RUN` | No production model-output evidence | Run one approved real vacancy only when input is ready |
| `OPEN-003` | P0.7 | Real vacancy pilot not executed | `NOT RUN` | Release proves system, not live package quality | Perform controlled pilot and manual semantic review |
| `OPEN-004` | P0.7 | Model availability/routing volatility | `OPEN` | Current model/effort assumptions can change | Verify before a new batch |
| `OPEN-005` | Candidate | `CLM-BAR-*`/`CLM-PRJ10-*` pack-level claim-index sync | `OPEN` | Retrieval index may lag approved owner-file evidence | Synchronize without renumbering IDs |
| `OPEN-006` | Candidate | Exact BAR task list, recipient counts, error categories, clinic names, tool usage counts and savings | `UNCERTAIN` | Could affect prominence of external claims | Omit or ask one targeted source-maintenance question |
| `OPEN-007` | Candidate | Exact PRJ-01 dashboard name/pages/users/current status and decommission reason | `UNCERTAIN` | Avoid over-specific lifecycle/scale claims | Retrieve before prominent use |
| `OPEN-008` | Candidate | Exact PRJ-02 report/unit/current status and support scope | `UNCERTAIN` | Avoid sole ownership/formal training claims | Retrieve if vacancy makes it decisive |
| `OPEN-009` | Candidate | PRJ-03 planned August 2026 delivery and final 2027 use | `UNCERTAIN` | Do not call active work completed | Update source authority only with evidence |
| `OPEN-010` | Candidate | PRJ-04 exact framework name, approval route, individual split and measured effect | `UNCERTAIN` | Preserve team boundary and no individual-effect claim | Retrieve if needed |
| `OPEN-011` | Candidate | PRJ-05 deployment/performance and exact language-specific authorship | `UNCERTAIN` | Prevent production/sole-author overclaim | Retain current ceiling |
| `OPEN-012` | Candidate | PRJ-06 implementation, weights, handover, adoption and realized benefits | `UNCERTAIN` | Prevent ROI/implementation overclaim | Retain design-only status |
| `OPEN-013` | Candidate | PRJ-07 platform access/scope and formal governance role | `UNCERTAIN` | Prevent platform-ownership inflation | Use exposure/pilot language |
| `OPEN-014` | Education | Exact NTNU award date, thesis, specialization, grades; UiA progress/completion; UiB average grade | `UNCERTAIN` | Formal application claims must stay conservative | Do not add until verified |

---

## 11. Interpretation guardrails for the P0.9 context-curation model

When mining this P0.7 baseline, distinguish **substrate that may remain reusable** from **P0.7 policy that later versions intentionally replaced**.

### 11.1 High-value reusable substrate candidates

These are historically important because later designs may preserve or adapt them even when stage topology changes:

- canonical candidate authority separation;
- derived-vs-authoritative source distinction;
- stable identity and employment IDs;
- explicit package schemas/contracts;
- fail-loud deterministic validation;
- expected-set reconciliation;
- source/identity checks across stage boundaries;
- original-master-based deterministic DOCX/PDF finalization;
- private review flags separate from employer-facing artifacts;
- explicit no-new-facts / claim-ceiling discipline;
- manual final semantic review and submission;
- file-based stage isolation as a proven simple operating substrate;
- strong separation between mechanical validation and semantic persuasion.

### 11.2 P0.7 mechanisms that must not be assumed current

Later files must be consulted before carrying these forward:

- four semantic stages;
- P0.7's 2-XL/4-mini topology;
- 12-prompt HappyPath;
- Terra→Sol→Terra→Sol routing;
- two evidence lanes and locked `MINICLUSTER_SPLIT.json`;
- Stage-4 role exactly as defined in P0.7;
- portal answers as mandatory core package surface;
- exact P0.7 package schema and runtime tree;
- P0.7-specific repair/finalization semantics;
- any model-routing assumption tied to 2026 availability.

### 11.3 Key historical lesson

P0.7 is valuable to P0.9 chiefly as **proof of an executable, deterministic substrate and a concrete set of safety/authority boundaries**. It should not constrain P0.9 merely because it was implemented. Conversely, later architectural elegance should not justify discarding a P0.7 mechanism that has actual implementation/test evidence unless the later design replaces its function with something at least as robust.

### 11.4 What this file deliberately does not establish

This file does **not** establish:

- the final P0.9 architecture;
- that P0.8.1 hardening was adopted;
- that every P0.7 mechanism remains desirable;
- that P0.7 model routing is still available/current;
- that live application-package quality was proven;
- that candidate facts summarized here are a substitute for the canonical candidate source files.

Use the full 20-file corpus to determine those points.
