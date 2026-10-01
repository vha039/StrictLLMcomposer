---
artifact: Jobbsøk_26 per-chat integration summary
chat_name: "UNAVAILABLE_TO_MODEL_UI — descriptive fallback used: Jobbsøk_26 P0.7→P0.8 architecture redesign"
reconstruction_scope: entire current chat only
archival_status: provenance-tagged state reconstruction
created_for: later inter-chat reconciliation
latest_framework_state_in_chat: "P0.8 FINAL_NORMATIVE_SPECIFICATION — specified, not implemented"
latest_implemented_release_in_chat: "P0.7"
confidence: high on terminal state; medium on earliest-chat ordering where pre-chat context was summarized rather than directly re-opened
---

# Jobbsøk_26 P0.7→P0.8 architecture redesign — integration summary

> **Important:** This is not a normal summary. It is a provenance-tagged reconstruction of the state changes, decisions, artifacts, research signals, contradictions and unresolved boundaries evidenced in this chat. Every substantive item is labelled `CONFIRMED`, `INFERRED`, `PROPOSED`, `SUPERSEDED`, `REJECTED`, `OPEN`, or `UNKNOWN`.
>
> **Filename note:** The actual visible ChatGPT UI title is not exposed to the model in this runtime. The required `[chat_name]_integration_summary.md` naming rule is therefore satisfied by a descriptive fallback rather than an invented claim about the UI title.

---

## 0. Baseline-anchor verification

The anchors below were supplied externally in the archival prompt. They are not treated as discoveries of this chat.

| Anchor | This chat | Status | Evidence from this chat | Reconciliation note |
|---|---|---|---|---|
| **P0.5.3** = superseded API/SDK four-call architecture; Structured Outputs/Pydantic/docxtpl/LLM-as-judge; 21/21 tests; offline E2E only | The chat repeatedly treats P0.5.x/API-runner/orchestrator logic as historical and outside the active path. Exact 21/21 and all P0.5.3 implementation details are not independently re-established here. | `CONFIRMED` on superseded/historical status; `SILENT` on most implementation detail | The P0.7 implementation prompt explicitly says historical P0.5.x material is migration history, never normative target state. P0.7 implementation report says historical P0.5.x API-runner was removed from active path. | Do not use this chat to prove the 21/21 figure; use sibling source if needed. |
| **P0.6** = superseded by P0.7; manual 4-stage, 4×10 macro / 8×5 mini, 24-prompt HappyPath, same 3 scripts, 30/33 tests | The chat explicitly uses P0.6 as the working implementation substrate and migrates it to P0.7 rather than rebuilding blindly. P0.7 test report records P0.6 baseline as 30 PASS + 3 PowerShell-dependent skips. | `CONFIRMED` | P0.7 implementation report: “Baseline som ble migrert: Jobbsok_26_P0.6/”; P0.7 test report: P0.6 baseline 30 PASS, 3 skips. | Chat supports P0.6 as actual prior implementation, not only design. |
| **P0.7** = implemented current release; 4 stages; Terra Max → Sol Max → Terra XHigh → Sol XHigh; 2×20 macro + 4×10 mini; 12 prompts; 3 scripts; 52 files; 32/34 tests; 2 PowerShell-blocked; no real vacancy/model pilot | The release ZIP was directly audited in this chat. Architecture, script count, file count, tests, rendering, blocked PowerShell, and lack of real model/vacancy run were all independently checked. | `CONFIRMED` and `EXTENDS` | `Jobbsok_26_P0.7_Release.zip`; SHA-256 `c74565ceb32900beba4b912e1cec93abe68039f83a29da6952f7ad9f57feb1a8`; implementation report and test report. | Chat adds specific audit findings and exact release hash. |
| **P0.8 Selective Quality MVP** = final normative spec; 3 stages Sol Max → Terra Max → Sol Max; 5×~8 jobs; 15 chats; 2 scripts; Stage 3 final authority; READY/CHECK/RERUN; partial success; `--job`; not implemented | The chat culminates in generation and verification of the final P0.8 Markdown specification. It is explicitly normative and explicitly a migration/build target, not an implementation. | `CONFIRMED` and `EXTENDS` | Generated final Markdown: 3,825 lines, 17,151 words, SHA-256 `0dddf4b4c29fcee407ff568cfc2f1629ed01d3e8aa88129497da3a1d748ec0ba`; frontmatter `status: FINAL_NORMATIVE_SPECIFICATION`, `specification_version: 0.8.0`, `last_design_review: 2026-08-04`. | This is the strongest terminal state in the chat. |
| **Redesign trigger:** optimize `Q_happy = avg(median(package_quality), mean(top_80%(package_quality)))`; bottom 20% handled separately | User explicitly corrected the prior reliability-oriented framing and made this the optimization target. | `CONFIRMED` | User: the most important thing is that the happy path “usually produces best possible application packages”; bottom 20% may be handled separately. Later final P0.8 spec formalizes `Q_happy`. | This user correction supersedes the earlier implicit uniformity/reliability objective. |
| **P0.8 non-goals:** memory/cache, vector DB, multi-agent, automatic routing, best-of-N, LLM-as-judge, retries, employer research/submission | All are explicitly removed/deferred in the P0.8 design and final spec. | `CONFIRMED` | Final P0.8 scope and deferred backlog. | Full-package best-of-N is rejected; tiny internal headline/opening variation for Priority A remains allowed. |
| **Cost hierarchy:** Human Effort > Human Complexity > LLM Complexity > LLM Effort | Repeatedly applied when choosing more prompts for quality and when rejecting QA/automation complexity. | `CONFIRMED` | User repeatedly frames MVP-KISS and human-effort priority. P0.8 moves from 12 to 15 chats because expected human-edit reduction is worth 3 extra prompts. | Treat as stable project-level principle. |
| **Candidate truth files:** `Work_experience.md`, `Education.md`, `Other_high_value_information.md`; `CV_BASELINE.md` is derived and cannot create facts | Explicitly retained through P0.7 and P0.8. | `CONFIRMED` | P0.7 hash-verifies the three authority files. P0.8 truth model explicitly subordinates `CV_BASELINE.md` to them. | Strong source-of-truth anchor. |
| **Production naming:** GPT Web/Work → Sol/Terra Max; packaged output handed to local Codex at `C:\Codex\Jobbsok_26\` | Model/workflow concept is supported; exact path conflicts with the terminal P0.8 spec command path `C:\Codex\Jobbsok_26_P0.8`. | `CONTRADICTS` on exact path; `CONFIRMED` on overall Web/Work + local file-based execution model | P0.7 START_HERE uses `C:\Codex\Jobbsok_26_P0.7`; P0.8 final spec operator commands use `C:\Codex\Jobbsok_26_P0.8`. | External anchor should be reconciled explicitly before implementation. Do not silently rewrite the terminal spec path. |

---

## 1. Evidence and authority conventions used in this reconstruction

- `[CONFIRMED]` = directly stated, generated, tested, or explicitly accepted in this chat.
- `[INFERRED]` = strongly implied by sequence or artifact relationship but not directly stated.
- `[PROPOSED]` = assistant-proposed and not yet user-adopted at that point in the chronology.
- `[SUPERSEDED]` = once active or seriously considered, later replaced by a newer decision.
- `[REJECTED]` = explicitly declined or moved out of MVP scope.
- `[OPEN]` = competing interpretations remain or a pilot is required.
- `[UNKNOWN]` = this chat does not establish the point.

Authority order applied:

1. latest explicit user correction/decision;
2. earlier unsuperseded user decision;
3. assistant proposal explicitly adopted by user;
4. assistant high-confidence assertion not contradicted;
5. assistant speculation.

No current web knowledge is used to fill historical gaps. Research findings in §8 are only findings captured during this chat.

---

# 2. Chronology and inter-chat alignment

## 2.1 Absolute anchors

| Anchor | Date/version/artifact | Evidence | Confidence |
|---|---|---|---|
| P0.6 baseline implementation | `Jobbsok_26_P0.6_Release.zip`; P0.7 report says it was the migrated baseline | P0.7 implementation report; P0.7 test report records 30 PASS + 3 PowerShell skips | High |
| Early hybrid P0.7 design | `Final_Jobbsok_26_P0.7_Hybrid_Multi-Model_Dual-Prompt_Architecture.md` | Earlier in-chat generated artifact; recorded as 2,610 lines / 8,884 words / SHA `a819aecbcdb13b9130de71ba8d92ee6ed89ab565b7b10c28390b4f48d9c702ab` | High, but superseded |
| Final single-prompt P0.7 architecture spec | `jobbsøk_26_P0.7.md` | Generated in chat after dual-pass was rejected as too complex; 3,134 lines / 9,480 words / SHA `21b8351dd5849b2f44a486baa93751f0af54017aed3ad8e553c8d92346c33cf7` | High |
| P0.7 implementation launcher | `Jobbsok_26_P0.7_Implementation_Prompt.md` | Generated in chat; 411 lines / 1,820 words / SHA `ec491040cbf72651b6ff001f923b391bbca9868e18cf4f1423e126ff2df2ddff` | High |
| P0.7 test date | 2026-08-01 | `docs/TEST_REPORT.md` inside release ZIP | High |
| P0.7 implemented release | `Jobbsok_26_P0.7_Release.zip`; 52 files | Direct ZIP audit in chat | High |
| P0.7 release hash | SHA-256 `c74565ceb32900beba4b912e1cec93abe68039f83a29da6952f7ad9f57feb1a8` | Independent checksum in chat | High |
| P0.7 critical audit | `Jobbsok_26_P0.7_Critical_Audit_and_Perfection_Recipe.md` | Generated after direct adversarial/release audit; SHA recorded in chat as `5a5e725431ccdcc6692d6c6cf6a25ec9b99d7381a2cd2a3799405cd1143e8019` | High |
| P0.8 refinement transcript | `chat-historikk_utarbeidelse_av_jobbsøk_26_P0.8.docx` | Uploaded in chat; 62 pages; contains later external/parallel refinement sequence | High |
| Final P0.8 normative specification | `Jobbsøk_26_P0.8 - arkitektur, innhold, struktur, design og detaljert filindeks med utvidede innholdsbeskrivelser.md` | Generated in chat; frontmatter `specification_version: 0.8.0`, `last_design_review: 2026-08-04` | High |
| Final P0.8 spec size | 3,825 lines; 17,151 words; 132,751 bytes | Direct file inspection | High |
| Final P0.8 spec hash | `0dddf4b4c29fcee407ff568cfc2f1629ed01d3e8aa88129497da3a1d748ec0ba` | Direct checksum | High |

## 2.2 Relative ordering

| This chat/event | Relationship | Other event/artifact | Reason | Confidence |
|---|---|---|---|---|
| P0.6 implementation | before | all P0.7 work | P0.7 is explicitly a migration from P0.6 | High |
| Dual-prompt P0.7 design | before | final single-prompt P0.7 | User questions prompt count and proposes merging passes | High |
| 4×10/8×5 P0.6 topology | before | 2×20/4×10 P0.7 topology | User asks whether larger clusters can cut prompts | High |
| P0.7 single-prompt architecture | before | P0.7 implementation | User requests final magnum-opus spec and then implementation prompt | High |
| P0.7 implementation prompt | before | `Jobbsok_26_P0.7_Release.zip` | Release is the implementation output subsequently audited | High |
| P0.7 release audit | before | selective-quality redesign | Audit initially pushes reliability hardening; user then corrects objective | High |
| Q_happy user correction | before | P0.8 redesign | Explicit trigger for redesign from uniformity/reliability toward selective quality | High |
| Initial from-scratch P0.8 3-stage 4×10 proposal | before | final 5×8 P0.8 | Attached refinement transcript explicitly changes 4×10 to 5×~8 | High |
| P0.8 refinement DOCX | before | final P0.8 Markdown | User asks to distill DOCX, then asks final full spec preserving it | High |
| Final P0.8 Markdown | after | all earlier P0.8 planning | Frontmatter states it supersedes all preliminary P0.8 brainstorming | High |
| P0.8 implementation | after? | final P0.8 spec | Not performed in this chat; only planned | `UNKNOWN` / future dependency |

## 2.3 Terminal-sequence fingerprint

Newest last. These are the strongest cross-chat matching keys.

| Seq | Speaker | Event / decision / deliverable | Version/artifact affected | Evidence anchor |
|---:|---|---|---|---|
| 1 | User | Asks whether 2×20 macro + 4×10 mini can reduce dual-pass prompt count | P0.7 hybrid design | Current-chat user turn on larger clusters |
| 2 | Assistant | Recommends 2×20/4×10 as controlled maximum under dual-pass, with internal lanes/waves | P0.7 dual-pass design | Assistant “2 XL-makroklynger × 20 / 4 miniklynger × 10” |
| 3 | User | Proposes hybrid between P0.6/P0.7: merge two prompts; stronger model once per stage | P0.7 architecture | User “slår sammen begge promptene” |
| 4 | Assistant | Recommends single-prompt 4-stage Terra→Sol→Terra→Sol; 12 chats/prompts | P0.7 single-pass architecture | Assistant routing table |
| 5 | User | Proposes role-archetype memory/cache; then explicitly says this is overcomplication and moves it to “neste overhaling” | Deferred feature scope | User “La oss legge dette i ‘neste overhaling’-boksen” |
| 6 | User | Requests final P0.7 magnum-opus architecture/spec | `jobbsøk_26_P0.7.md` | Generated artifact |
| 7 | User | Requests optimized P0.6→P0.7 implementation prompt | `Jobbsok_26_P0.7_Implementation_Prompt.md` | Generated artifact |
| 8 | User | Uploads implemented P0.7 ZIP and requests critical audit/perfection recipe | `Jobbsok_26_P0.7_Release.zip` | Direct audit; 32/34 tests, 2 blocked |
| 9 | User | Corrects objective: prioritize median + top-80% quality; bottom 20% can be rerun manually | Optimization function | Explicit user correction; redesign trigger |
| 10 | Assistant | Reframes system around selective quality, cheap integrity, READY/CHECK/RERUN, soft QA | Transitional P0.7→P0.8 thinking | Assistant selective-prediction synthesis |
| 11 | User | Requests whole flow redesigned from scratch under new objective, still MVP-KISS | P0.8 architecture | Explicit user instruction |
| 12 | Assistant | Proposes 3 stages Sol Max→Terra Max→Sol Max, initially 4×10 clusters, 2 scripts | Preliminary P0.8 | Assistant from-scratch redesign |
| 13 | User | Uploads DOCX containing further refinement and asks compressed extraction of changes + final-doc plan | P0.8 final refinement | `chat-historikk_utarbeidelse_av_jobbsøk_26_P0.8.docx` |
| 14 | Assistant | Extracts final refinements: 5×8, Priority A/B, optional Terra XHigh preflight, 53-section canonical spec plan | P0.8 final design | DOCX-derived response |
| 15 | User | Requests final complete normative P0.8 Markdown, preserving all DOCX context and planned structure | Final P0.8 spec | User final spec request |
| 16 | Assistant | Delivers final P0.8 Markdown only | `FINAL_NORMATIVE_SPECIFICATION` | Generated final file |

## 2.4 Best partial chronology / dependency sketch

```text
P0.5.3 historical API/SDK design
        |
        v
P0.6 implemented manual four-stage release
        |
        +--> P0.6 audit/hardening findings
        |
        v
Early P0.7 dual-prompt hybrid design
        |
        +--> larger 2x20 / 4x10 clusters
        |
        +--> dual-prompt judged unnecessary complexity
        v
P0.7 single-prompt four-stage design
Terra Max -> Sol Max -> Terra XHigh -> Sol XHigh
2x20 macro -> 4x10 mini / 12 prompts
        |
        +--> memory/cache idea proposed
        |        `-- user explicitly defers to next overhaul
        v
Final P0.7 architecture spec
        |
        v
P0.7 implementation prompt
        |
        v
P0.7 implemented release ZIP
        |
        v
Critical release audit
        |
        +--> initially reliability-heavy hardening recipe
        |
        v
USER CORRECTION: optimize Q_happy, not uniformity
        |
        +--> selective-quality research / defer weak tail
        |
        v
From-scratch P0.8 redesign
3 stages, initially 4x10
        |
        +--> parallel/external refinement captured in attached DOCX
        |        `-- 5x8 replaces 4x10
        |        `-- Priority A/B replaces per-job router classes
        |        `-- two scripts only
        |        `-- Stage 3 full truth-bounded authority
        |        `-- soft page budget / partial success / review queue
        v
Final P0.8 normative Markdown spec (2026-08-04)
        |
        v
[NOT DONE IN THIS CHAT]
P0.7 -> P0.8 implementation/migration
        |
        v
[PLANNED]
first real ~8-job cluster pilot
```

No total chronology is asserted between this chat and sibling chats that may have run in parallel. The attached P0.8 DOCX is itself evidence that at least one refinement thread occurred outside or parallel to the immediate local turn sequence.

---

# 3. Incoming state when substantive work began

## 3.1 Confirmed incoming state

- `[CONFIRMED]` P0.6 existed as an implemented, testable local file-based release and was the codebase substrate for P0.7.
- `[CONFIRMED]` The design trajectory had already moved away from P0.5.3’s API/SDK orchestration toward manual Codex/Work stage execution.
- `[CONFIRMED]` A P0.7 hybrid concept already existed in which different GPT-5.6 models were assigned to different cognitive tasks.
- `[CONFIRMED]` An early P0.7 artifact used **two prompts per stage instance in the same chat**, separating a cheap/first-pass model from a stronger second-pass model.
- `[CONFIRMED]` The project already followed MVP-KISS, file contracts, immutable candidate truth, dynamic CV tailoring, Word-master rendering and manual submission.
- `[CONFIRMED]` P0.6.1 hardening issues had already been identified: older-role rendering, incomplete-batch false PASS risk, identity drift, hard page-budget needs, advance guards, ingest weakness, PowerShell verification, and related mechanical issues.

## 3.2 Inferred incoming state

- `[INFERRED]` The user’s immediate concern at the start of the visible arc was that P0.7’s dual-pass design had become too interaction-heavy and likely too complicated relative to marginal quality gain.
- `[INFERRED]` No P0.7 implementation had yet been produced at the moment the user first challenged cluster size and prompt count; the release ZIP appears later after the implementation prompt.
- `[INFERRED]` The current chat inherited research and architecture work from one or more other threads; exact global ordering among those threads is not recoverable from this chat alone.

## 3.3 Unknown incoming state

- `[UNKNOWN]` Whether another builder had already begun implementing P0.7 in parallel before the final implementation prompt was generated.
- `[UNKNOWN]` The exact UI title of this chat.
- `[UNKNOWN]` Whether the local production root had already been standardized to a generic `C:\Codex\Jobbsok_26\` path or version-specific folders before this chat.

---

# 4. Evolution within this chat

| Stage | Earlier state | Trigger / new evidence | Change made | Resulting state | Status |
|---|---|---|---|---|---|
| P0.7 hybrid pass design | 4 stages × 2 prompts, 24 chats / 48 prompts under 4×10/8×5 | User asks whether cluster sizes can be enlarged | 2×20 macro and 4×10 mini proposed; still dual-pass | 24 prompts / 12 chats in dual-pass version | `SUPERSEDED` |
| Prompt architecture | Dual-prompt same-chat model switching | User proposes merging both prompts and simply using stronger single model | Remove mandatory prompt-1/prompt-2 split | Single prompt per stage instance | `ACTIVE` for P0.7 implementation, later superseded by P0.8 stage count |
| P0.7 model routing | Luna/Terra/Sol split across two passes | User prioritizes lower user burden | Stage1 Terra Max; Stage2 Sol Max; Stage3 Terra XHigh; Stage4 Sol XHigh | 12-prompt 4-stage P0.7 | `CONFIRMED` for implemented P0.7 |
| Persistent memory | No memory | User proposes archetype retrieval/strategy cache | Assistant designs curated archetype prior memory | User explicitly says overcomplication; move to later overhaul | `REJECTED` for MVP / `DEFERRED` |
| P0.7 spec | Multiple active design branches | User asks for final magnum-opus | Final single-prompt P0.7 normative design generated | `jobbsøk_26_P0.7.md` | `SUPERSEDED` by P0.8, but was authoritative for P0.7 build |
| P0.7 implementation | Spec only | User requests optimized implementation launcher | Migration-first implementation prompt generated | Builder-ready P0.7 implementation instruction | `COMPLETED` |
| P0.7 release | P0.6 codebase | Implementation run outside immediate assistant response | P0.7 release produced and uploaded | 52-file implemented release | `IMPLEMENTED` |
| P0.7 audit | Release claims 32/34 tests | User requests deep tool-handled audit | Direct ZIP/test/render/adversarial review | Strong release, but several integrity/QA issues found | `COMPLETED` |
| Quality objective | Reliability/uniformity implicitly weighted heavily | User explicitly corrects objective | Introduce `Q_happy`; bottom 20% may rerun outside main flow | Selective-quality philosophy | `ACTIVE` |
| Audit priorities | Hard QA gates and consistency strengthening | New user objective | Reclassify many QA issues as low-value/soft; preserve only cheap hard truth/useability gates | Quality-first hard/soft boundary | `ACTIVE` |
| P0.8 stage count | Four P0.7 stages | User asks redesign “from scratch” | Merge vacancy analysis + strategy into one Sol stage | Three stages: Sol→Terra→Sol | `ACTIVE` |
| P0.8 cluster size | Initial redesign proposed 4×10 | Further critical refinement in attached DOCX | Change to 5×~8; normal range 6–10 | 15 standard chats | `ACTIVE` |
| P0.8 per-job compute routing | Assistant proposed PRIME/STANDARD/MANUAL-LATER | Refinement finds this implies more routing/chats/complexity | Replace with Priority A/B affecting order and micro-refinement only | Same model/effort per cluster | `ACTIVE` |
| Stage 3 authority | Earlier evidence lock / no-new-ID logic | User quality objective + audit finding | Make truth boundary hard but strategy boundary soft | Stage 3 can change identity/headline/evidence/channel within sources | `ACTIVE` |
| Review | QA flags / confidence concepts | Selective-quality objective | READY/CHECK/RERUN, max 3 concrete reasons, no confidence score | Human review queue | `ACTIVE` |
| Side budgets | Hard CV≤2 / letter≤1 as P0.7 gate | Strong package could be discarded for 2.2 pages | Render and flag CHECK instead | Soft page budget | `ACTIVE` |
| State | `_DONE.md`, `BATCH_STATUS.md`, split/copy machinery | Three-stage one-cluster design | Artifact primary; minimal `progress.json` | No `_DONE.md`, no large status file | `ACTIVE` |
| Scripts | ingest + advance + finalize | No macro→mini transition remains | Remove `advance.ps1` | Exactly two active scripts | `ACTIVE` |
| Final spec | Detailed P0.8 plan in attached DOCX | User asks for canonical full definition | 53-section Markdown generated | P0.8 `FINAL_NORMATIVE_SPECIFICATION` | `ACTIVE`, not implemented |

---

# 5. Decision ledger

| ID | Decision / constraint | Authority | Status | Scope | Evidence | Supersedes / superseded-by |
|---|---|---|---|---|---|---|
| D-001 | Human effort dominates model/credit cost; retain MVP-KISS | USER-EXPLICIT | ACTIVE | Whole project | Repeated user framing | Foundational |
| D-002 | P0.6 is implementation substrate; migrate rather than blindly rebuild | USER-ACCEPTED-PROPOSAL | SUPERSEDED as target, ACTIVE as migration source | P0.7 implementation | P0.7 implementation prompt/report | P0.8 still uses P0.7 as source release |
| D-003 | Early P0.7 may use two prompts per stage in same chat | ASSISTANT-PROPOSAL | SUPERSEDED | Early P0.7 | Dual-prompt P0.7 artifact | Replaced by D-005 |
| D-004 | Enlarge P0.7 clusters to 2×20 macro / 4×10 mini | USER-ACCEPTED-PROPOSAL | SUPERSEDED by P0.8 | P0.7 | User asks; assistant recommends; final P0.7 adopts | Replaced by D-017 for P0.8 |
| D-005 | P0.7 single-prompt stage instances | USER-EXPLICIT / USER-ACCEPTED-PROPOSAL | ACTIVE for P0.7, SUPERSEDED structurally by P0.8 | P0.7 | User asks merge prompts; final P0.7 spec | P0.8 keeps one prompt/stage but has 3 stages |
| D-006 | P0.7 routing Terra Max → Sol Max → Terra XHigh → Sol XHigh | USER-ACCEPTED-PROPOSAL | ACTIVE for implemented P0.7; SUPERSEDED for P0.8 | P0.7 | Final P0.7 spec + release | Replaced by D-016 |
| D-007 | Persistent archetype memory/cache is not MVP scope | USER-CORRECTION | ACTIVE | P0.7/P0.8 scope | User “neste overhaling” | Explicitly deferred in P0.8 |
| D-008 | P0.6.1 mechanical hardening belongs in P0.7 | USER-ACCEPTED-PROPOSAL | IMPLEMENTED in P0.7 | P0.7 | Final P0.7 spec and implementation report | Some hardening priorities later softened in P0.8 |
| D-009 | P0.7 should be implemented as four manual physically isolated stages | USER-ACCEPTED-PROPOSAL | SUPERSEDED as future target; implemented historically | P0.7 | Release | Replaced by 3-stage P0.8 |
| D-010 | P0.7 audit initially recommends stricter integrity/status/transition hardening | ASSISTANT-HIGH-CONFIDENCE | SUPERSEDED in priority | P0.7.1 candidate plan | Critical audit report | User correction D-011 |
| D-011 | Primary objective is `Q_happy`, not uniform package quality; bottom 20% can be rerun separately | USER-CORRECTION | ACTIVE | P0.8 product objective | Explicit user correction | Supersedes reliability-first interpretation |
| D-012 | Hard blocks only protect truth/identity/mechanical usability; most semantic/format issues become soft | USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 QA | Selective-quality discussion + final spec | Supersedes many D-010 hardening instincts |
| D-013 | All user-approved jobs receive complete output if mechanically possible; no fit veto | USER-EXPLICIT / USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 | Repeatedly retained | — |
| D-014 | Rebuild P0.8 “from scratch” conceptually, while reusing directly valuable P0.7 assets | USER-EXPLICIT | ACTIVE | P0.8 redesign | User redesign request | — |
| D-015 | Three model stages are optimal balance: think → write → write finished | USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 architecture | Refined attached DOCX and final spec | Rejects 2-stage and 4-stage alternatives |
| D-016 | P0.8 model route = Sol Max → Terra Max → Sol Max for first pilot | USER-ACCEPTED-PROPOSAL | ACTIVE / PILOTDEFAULT | P0.8 | Final refinement + final spec | P0.7 model route superseded |
| D-017 | P0.8 target topology = 5 clusters × ~8 jobs; normal 6–10; 10 max standard | USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 | Attached refinement + final spec | Supersedes initial P0.8 4×10 |
| D-018 | Cluster manually by default; optional one-off Terra XHigh preflight may suggest plan but is non-authoritative and not a fourth stage | USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 preflight | Final refinement/spec | — |
| D-019 | Priority A/B replaces PRIME/STANDARD/MANUAL-LATER per-job routing | USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 within-cluster ordering | Refinement DOCX | Rejects per-job model router |
| D-020 | Priority A gets microvariation for headline/opening; Priority B does not get extra compute automatically | USER-ACCEPTED-PROPOSAL | ACTIVE | Stage 2 | Final spec | Full-package best-of-N remains rejected |
| D-021 | Stage 1 Phase A is candidate-blind; Phase B is candidate-aware, in same Sol chat | USER-ACCEPTED-PROPOSAL | ACTIVE | Stage 1 | Final spec | Replaces separate vacancy stage |
| D-022 | Stage 1 carries the heavy retrieval burden; later stages use exact cited source sections and targeted checks | USER-ACCEPTED-PROPOSAL | ACTIVE | Retrieval architecture | Refinement DOCX/final spec | Rejects repeated full-corpus retrieval |
| D-023 | Stage 3 is final strategic authority within hard truth boundaries | USER-ACCEPTED-PROPOSAL | ACTIVE | Stage 3 | Final spec | Supersedes P0.7 evidence-lock/no-new-ID-from-draft concept |
| D-024 | Review classes are READY/CHECK/RERUN; no confidence score; max 3 concrete reasons | USER-ACCEPTED-PROPOSAL | ACTIVE | Stage 3/human review | Final spec | Replaces stricter review headings/confidence concepts |
| D-025 | Side budget is soft: render usable output, mark CHECK/PAGE_BUDGET | USER-ACCEPTED-PROPOSAL | ACTIVE | Finalizer | Final spec | Supersedes P0.7 hard page veto |
| D-026 | Finalizer preserves partial success; failure of one job does not nullify good jobs | USER-ACCEPTED-PROPOSAL | ACTIVE | Finalizer | Final spec | Supersedes global-batch-PASS orientation |
| D-027 | P0.8 has exactly two active scripts: `ingest.py` and `finalize.py` | USER-ACCEPTED-PROPOSAL | ACTIVE | Repository | Final spec | `advance.ps1` removed |
| D-028 | Artifact itself is primary state; only minimal `progress.json`; no `_DONE.md`, no large `BATCH_STATUS.md` | USER-ACCEPTED-PROPOSAL | ACTIVE | Runtime/state | Final spec | P0.7 state machinery removed |
| D-029 | P0.8 has five schemas: batch plan, identity, package, progress, review | USER-ACCEPTED-PROPOSAL | ACTIVE | Data contracts | Final spec repository | — |
| D-030 | Human/operator owns irreversible boundary: approval, clustering/freeze, final semantic review, submission | USER-EXPLICIT / USER-ACCEPTED-PROPOSAL | ACTIVE | Whole system | Final spec | — |
| D-031 | P0.8 final spec must be canonical enough that builder makes no material architecture/data-contract decisions | USER-EXPLICIT | ACTIVE | Documentation | Final user request + attached plan | — |
| D-032 | Final P0.8 spec is generated but not implemented | CONFIRMED FACT | ACTIVE STATE | Project state | Final Markdown exists; no P0.8 release ZIP/build run in chat | Next step is implementation |

---

# 6. Requirements and constraints

## 6.1 Active explicit constraints

| Constraint | Tag | Current meaning |
|---|---|---|
| Optimize `Q_happy`, not batch uniformity | `explicit-active` | Median + top-80% mean dominates architecture and QA choices |
| Human effort > human complexity > LLM complexity > LLM effort | `explicit-active` | Extra model cost is acceptable if it reduces manual rework |
| MVP-KISS | `explicit-active` | Remove machinery without direct quality/usability value |
| All selected jobs are `PRODUCE` | `explicit-active` | No automated semantic fit veto |
| Candidate truth only from three authority files | `explicit-active` | Models may synthesize strongly but not create facts |
| `CV_BASELINE.md` is derived | `explicit-active` | Rendering baseline never outranks authorities |
| Strong synthesis is allowed | `explicit-active` | Employer-value framing and functional equivalence permitted within truth |
| Formal claims cannot be upgraded | `explicit-active` | No invented titles, dates, degrees, mandate, personnel responsibility or lifecycle |
| One job at a time within each stagechat | `explicit-active` | Persist/validate before opening next job |
| Natural Norwegian Bokmål | `explicit-active` | Employer-facing text should sound native, calm, specific and professionally confident |
| Channels are complementary | `explicit-active` | CV, letter and portal must not merely repeat each other |
| Stage 3 may rewrite strategy | `explicit-active` | Truth boundary hard; strategy boundary soft |
| Manual final approval and manual submission | `explicit-active` | No automatic employer interaction |
| Partial success | `explicit-active` | Good jobs survive other jobs’ failures |
| No hidden retry | `explicit-active` | Continuation/RERUN is explicit |
| Review is READY/CHECK/RERUN | `explicit-active` | Triage, not a release verdict |
| Soft side budgets | `explicit-active` | Oversize can produce CHECK instead of lost output |
| Two active scripts only | `explicit-active` | `ingest.py`, `finalize.py` |
| One cluster type | `explicit-active` | No macro/minicluster hierarchy |
| 5×~8 cluster target | `explicit-active` | Normal 6–10; 10 max standard |

## 6.2 Explicit active automation boundaries

- `[CONFIRMED]` No automatic job search in P0.8.
- `[CONFIRMED]` No automatic employer research in MVP.
- `[CONFIRMED]` No automatic submission or contact.
- `[CONFIRMED]` No automatic per-job model router.
- `[CONFIRMED]` No automatic rerun/retry loop.
- `[CONFIRMED]` No multi-agent system.
- `[CONFIRMED]` No LLM-as-judge.
- `[CONFIRMED]` No vector DB.
- `[CONFIRMED]` No persistent memory/archetype cache.
- `[CONFIRMED]` No full-package best-of-N.
- `[CONFIRMED]` Optional one-off model-assisted cluster preflight is allowed but non-authoritative.

## 6.3 Rendering and document constraints

- `[CONFIRMED]` Original Word masters remain source assets and are mutated only via copies.
- `[CONFIRMED]` P0.8 requires explicit headline support and natural 1–2 page CV flow.
- `[CONFIRMED]` No forced weak page split.
- `[CONFIRMED]` Earlier employment overrides remain supported.
- `[CONFIRMED]` PDF text must be selectable.
- `[CONFIRMED]` Private review/source IDs must not appear employer-facing.
- `[CONFIRMED]` Unit/reference are conditional display data.
- `[CONFIRMED]` Generated DOCX metadata cleanup is desirable but not a first-pilot blocker if safe output otherwise passes.

---

# 7. Artifact and source inventory

| Artifact/file | Type | Role | Version/revision | State at end of chat | Authority/source | Notes |
|---|---|---|---|---|---|---|
| `Work_experience.md` | Markdown authority | Work/project facts, contribution, lifecycle | P0.7 authority reused | `VERIFIED / REUSE_BYTE_IDENTICAL` for P0.8 target | Candidate truth | P0.7 SHA `0b39a510...a2f9d` recorded |
| `Education.md` | Markdown authority | Degrees/institutions/courses/academic facts | P0.7 authority reused | `VERIFIED / REUSE_BYTE_IDENTICAL` | Candidate truth | P0.7 SHA `75e23889...580f8` |
| `Other_high_value_information.md` | Markdown authority | Other stable candidate facts | P0.7 authority reused | `VERIFIED / REUSE_BYTE_IDENTICAL` | Candidate truth | P0.7 SHA `58a8f88f...5ae5bf8` |
| `CV_BASELINE.md` | Derived Markdown | Static CV chronology and employment IDs | P0.7 → planned P0.8 0.8.0 | `DECIDED TO ADAPT`, not implemented | Derived from authorities | Cannot create facts |
| `CV_MASTER.docx` | Word master | CV rendering | P0.7 source asset | `VERIFIED P0.7`; planned `REUSE_WITH_VERIFICATION` / adapt layout | Original asset | P0.7 SHA `c3809748...e8c5` |
| `APPLICATION_MASTER.docx` | Word master | Letter rendering | P0.7 source asset | `VERIFIED P0.7`; planned reuse/adaptation | Original asset | P0.7 SHA `dfd24125...1409` |
| `Final_Jobbsok_26_P0.7_Hybrid_Multi-Model_Dual-Prompt_Architecture.md` | Markdown spec | Early dual-prompt P0.7 design | preliminary P0.7 | `GENERATED`, `SUPERSEDED` | Assistant artifact | SHA `a819aecb...02ab` |
| `jobbsøk_26_P0.7.md` | Markdown spec | Final single-prompt P0.7 architecture | P0.7 | `GENERATED / DELIVERED`, later superseded by P0.8 | Assistant artifact adopted by user | 3,134 lines, 9,480 words, SHA `21b8351d...cf7` |
| `Jobbsok_26_P0.7_Implementation_Prompt.md` | Markdown prompt | P0.6→P0.7 builder launcher | P0.7 | `GENERATED / DELIVERED / USED AS IMPLEMENTATION BASIS` | Assistant artifact | 411 lines; SHA `ec491040...dff` |
| `Jobbsok_26_P0.7_Release.zip` | ZIP release | Implemented P0.7 codebase | P0.7 | `IMPLEMENTED / AUDITED / VERIFIED` | External builder output uploaded by user | 52 files; SHA `c74565ce...b1a8` |
| P0.7 `IMPLEMENTATION_REPORT.md` | Markdown report inside ZIP | Migration/build evidence | P0.7 | `VERIFIED` | Release | Confirms four stages, 3 scripts, 2×20/4×10 |
| P0.7 `TEST_REPORT.md` | Markdown report inside ZIP | Test evidence | P0.7 | `VERIFIED` | Release | 32 PASS, 2 BLOCKED, 0 FAIL; real model/vacancy NOT RUN |
| `Jobbsok_26_P0.7_Critical_Audit_and_Perfection_Recipe.md` | Markdown audit | Independent audit + hardening ideas | post-P0.7 | `GENERATED / DELIVERED`; much of hardening priority later superseded | Assistant audit | Identified Stage3→4 bypass, weak parsers, untested target scale, CV balance |
| `chat-historikk_utarbeidelse_av_jobbsøk_26_P0.8.docx` | DOCX transcript | External/parallel refinement of P0.8 design + final spec plan | post-redesign | `UPLOADED / READ / USED` | User-provided | 62 pages; key source for 5×8 and 53-section plan |
| `Jobbsøk_26_P0.8 - arkitektur, innhold, struktur, design og detaljert filindeks med utvidede innholdsbeskrivelser.md` | Markdown normative spec | Canonical P0.8 build/ops/acceptance spec | `0.8.0` | `GENERATED / DELIVERED / FINAL_NORMATIVE_SPECIFICATION`; **not implemented** | Assistant generated from chat + attached DOCX | 3,825 lines; 17,151 words; SHA `0dddf4b4...c0ba` |
| `MODEL_ROUTING.md` | Planned runtime doc | Volatile models/effort/A-B policy | P0.8 target | `DECIDED BUT NOT IMPLEMENTED` | P0.8 spec | Kept separate so model facts can change without architecture rewrite |
| `WRITING_STANDARD.md` | Planned context doc | Consolidated Norwegian writing standard | P0.8 target | `DECIDED BUT NOT IMPLEMENTED` | P0.8 spec | Consolidates overlapping language-core material |
| `PERSUASION_CALIBRATION.md` | Existing/adapted context doc | User-confirmed persuasion calibration | P0.8 target | `PLANNED REUSE/ADAPT` | P0.7 context | Kept separate from generic writing standard |
| `batch_plan.schema.json` | Planned JSON schema | Human-approved batch/clustering contract | 0.8.0 | `DECIDED BUT NOT IMPLEMENTED` | P0.8 spec | One of exactly five schemas |
| `job_identity.schema.json` | Planned JSON schema | Immutable job identity | 0.8.0 | `DECIDED BUT NOT IMPLEMENTED` | P0.8 spec | Replaces P0.7 identity contract naming |
| `package.schema.json` | Planned JSON schema | Shared draft/final package schema | 0.8.0 | `DECIDED BUT NOT IMPLEMENTED` | P0.8 spec | `source_stage` differentiates draft/final |
| `review.schema.json` | Planned JSON schema | READY/CHECK/RERUN | 0.8.0 | `DECIDED BUT NOT IMPLEMENTED` | P0.8 spec | No confidence/score |
| `progress.schema.json` | Planned JSON schema | Minimal stage state | 0.8.0 | `DECIDED BUT NOT IMPLEMENTED` | P0.8 spec | Artifact remains primary state |
| `scripts/ingest.py` | Python | Vacancy normalization/run setup | P0.7 exists; P0.8 adaptation planned | `IMPLEMENTED P0.7 / ADAPT_FROM_P0.7` | Release/spec | P0.8 adds batch-plan/run-layout semantics |
| `scripts/advance.ps1` | PowerShell | P0.7 Stage2→3 split | P0.7 | `IMPLEMENTED P0.7`, `REMOVE` in P0.8 | P0.7 release | PowerShell runtime test blocked in P0.7 test env |
| `scripts/finalize.py` | Python | Validate/merge/render/review queue | P0.7 exists; P0.8 rewrite/adaptation planned | `IMPLEMENTED P0.7 / ADAPT_FROM_P0.7` | Release/spec | P0.8 partial-success, soft-page, review queue, `--job` |
| `REVIEW_QUEUE.md` | Generated Markdown | Human work prioritization | P0.8 runtime | `PLANNED / GENERATED_AT_RUNTIME` | Finalizer | New P0.8 artefact |
| `PORTFOLIO_PLAN.json` | Optional generated JSON | Non-authoritative clustering suggestion | P0.8 runtime | `PLANNED OPTIONAL` | Optional Terra XHigh preflight | Never authoritative; human review required |

---

# 8. Research and external findings captured in this chat

> These are findings as represented in the chat. They are not re-verified here. Where the transcript only preserved citation IDs rather than durable URLs, the IDs are retained as provenance signals.

| Finding | Architectural / implementation implication | Source/provenance captured in chat | Confidence | Later challenged? |
|---|---|---|---|---|
| GPT-5.6 Sol/Terra/Luna were described as supporting ~1.05M context and 128K max output | Output ceiling was not the primary reason to cap cluster size at 5; larger clusters were technically feasible | Official OpenAI model pages cited in-chat, e.g. `turn749289search1`, `turn749289search3`, `turn749289search4` | High as chat finding | Cluster size later reduced for quality, not capacity |
| Terra token cost was described as ~0.5× Sol and Luna ~0.2× Sol | Terra is economically attractive for output-heavy Writer stage | Official Codex/OpenAI rate docs, e.g. `turn905612search0` | High as chat finding | No; exact rates declared volatile in P0.8 |
| Long-context benchmark signal suggested Terra near Sol on certain long-context retrieval tests and Luna materially weaker | Supported Terra/Sol hybrid rather than Luna-heavy default | OpenAI MRCR references in chat | Medium-high | Later P0.8 uses Sol for retrieval/strategy anyway |
| Higher reasoning effort should be evaluated empirically rather than assumed universally better | P0.8 Max is pilotdefault, then XHigh A/B-tested one variable at a time | OpenAI guidance cited in chat | High | No |
| “Lost in the Middle” / long-context position effects | Pushed cluster default from 10 to ~8 and encouraged ordering/distinct-job spacing | Named paper captured in attached P0.8 refinement; in-chat citation `turn986823search2` | Medium-high | No |
| Selective prediction / learning-to-defer improves quality when weak cases can be deferred | Direct conceptual basis for READY/CHECK/RERUN and `Q_happy` | SelectiveNet / learning-to-defer discussion; e.g. `turn773845search5`, `turn814876search10` | High as design analogy | No |
| Adaptive test-time compute should be concentrated where marginal gain is likely | Initially inspired PRIME/Standard routing; later simplified to Priority A/B because per-job routing was too complex | Test-time compute / routing research captured in chat | Medium-high | Per-job routing was rejected; principle survives as ordering/refinement asymmetry |
| Self-Refine-style generate→feedback→revise can improve output without another model pass | Preserved internal Phase A→Phase B within each stage while rejecting dual-prompt loops | `Self-Refine` cited in chat (`turn773845search4`) | High as design support | No |
| Full best-of-N can overfit imperfect graders / add selection burden | Full-package best-of-N rejected; tiny internal variation only for headline/opening on Priority A | In-chat best-of-N discussion, `turn582034search1` | Medium-high | No |
| Task-specific evals and human expert comparison are preferable to assuming generic benchmark transfer | P0.8 uses human `quality 1–10`, READY-rate, edit minutes, TailRecall20, credits; no LLM judge | OpenAI GDPval / eval guidance captured in chat | High | No |
| Same-stage model switching / dual passes increase user burden and repeat context | P0.7 dual-pass design collapsed to one prompt per stage | Product/workflow discussion in chat | High | No |
| More strict QA can reduce package quality when it prevents a stronger final model from correcting strategy | Stage 3 final authority, soft page budgets, partial success | Derived jointly from P0.7 audit + user objective correction | High | This is a core later correction |

Research-informed design decisions must remain subordinate to the user’s explicit objective and to local pilot results. The final P0.8 spec correctly labels model availability, effort names, credits, context and output limits as `VOLATILE`.

---

# 9. Implementation state at end of chat

## 9.1 Implemented / completed

- `[CONFIRMED]` P0.7 is fully implemented as a release folder/ZIP.
- `[CONFIRMED]` P0.7 has four physically isolated stages, three active scripts and target 2×20/4×10 topology.
- `[CONFIRMED]` P0.7 includes Word-master rendering, dynamic CV merge, identity anchor, batch completeness checks and P0.6.1 hardening.
- `[CONFIRMED]` P0.7 critical audit and P0.8 redesign work are completed as analysis/specification artifacts.
- `[CONFIRMED]` Final P0.8 normative Markdown specification has been generated.

## 9.2 Verified / evidenced

- `[CONFIRMED]` P0.7 ZIP: 52 members, CRC valid, deterministic packaging claim verified in audit context.
- `[CONFIRMED]` P0.7 tests: 32 PASS, 2 BLOCKED/skipped due no PowerShell, 0 FAIL.
- `[CONFIRMED]` P0.7 rendering: DOCX/PDF generation, selectable text, older employment override, unit/reference, letter/no-letter and portal fixtures verified.
- `[CONFIRMED]` P0.7 audit reproduced additional gaps beyond the release suite, including Stage3→4 mutable draft/reference bypass and weak textual parsing of certain status/review markers.
- `[CONFIRMED]` P0.8 final spec file exists and matches the attached final-plan structure; file statistics and hash directly checked.

## 9.3 Decided but not implemented

- `[CONFIRMED]` Entire P0.8 runtime/repository migration.
- `[CONFIRMED]` Three-stage Sol Max→Terra Max→Sol Max production flow.
- `[CONFIRMED]` 5×~8 clustering and Priority A/B ordering.
- `[CONFIRMED]` Optional non-authoritative Terra XHigh preflight.
- `[CONFIRMED]` Five P0.8 schemas.
- `[CONFIRMED]` New `WRITING_STANDARD.md` consolidation.
- `[CONFIRMED]` `REVIEW_QUEUE.md` generation.
- `[CONFIRMED]` `finalize.py --job` targeted rerender.
- `[CONFIRMED]` Soft side budgets and partial-success statuses.
- `[CONFIRMED]` Natural one-/two-page CV flow and explicit headline.
- `[CONFIRMED]` Removal of `advance.ps1` from active path.

## 9.4 In progress

- `[CONFIRMED]` None at terminal state. The design/specification phase is complete; implementation has not begun in this chat.

## 9.5 Planned

- `[CONFIRMED]` P0.7→P0.8 migration/build.
- `[CONFIRMED]` Mechanical tests and rendering validation for P0.8.
- `[CONFIRMED]` First real pilot: one coherent cluster of about eight approved jobs.
- `[CONFIRMED]` Measure `Q_happy`, READY rate, edit minutes, TailRecall20, review load and credits.
- `[CONFIRMED]` Change one pilot variable at a time; first priority is Stage 3 Sol Max vs Sol XHigh.

## 9.6 Blocked

- `[CONFIRMED]` P0.7 PowerShell runtime verification was blocked in the test environment because PowerShell was unavailable.
- `[INFERRED]` This blocker ceases to matter architecturally in P0.8 because `advance.ps1` is removed, but it remains relevant to the historical P0.7 release record.

## 9.7 Unknown

- `[UNKNOWN]` Whether P0.8 has since been implemented in another chat or local Codex session.
- `[UNKNOWN]` First real P0.8 pilot quality.
- `[UNKNOWN]` Whether Sol XHigh can replace Sol Max in Stage 3 without quality/review loss.
- `[UNKNOWN]` Whether Terra XHigh can replace Terra Max in Stage 2.
- `[UNKNOWN]` Whether cluster size 10 performs equally to 8 under real use.

---

# 10. Latest active plan / strategy at end of chat

## 10.1 Next objective

`[CONFIRMED]` **Implement P0.8 from the final normative specification using P0.7 as the source release, without reopening product architecture.**

## 10.2 Intended implementation sequence

1. `[CONFIRMED]` Inventory and archive/freeze P0.7.
2. `[CONFIRMED]` Verify hashes for the three candidate authorities and Word masters.
3. `[CONFIRMED]` Create a separate P0.8 repository tree.
4. `[CONFIRMED]` Add five schemas and the new runtime object model.
5. `[CONFIRMED]` Adapt baseline and consolidate language guidance into `WRITING_STANDARD.md` while preserving `PERSUASION_CALIBRATION.md`.
6. `[CONFIRMED]` Create three short stage instruction files plus root `AGENTS.md` and volatile `MODEL_ROUTING.md`.
7. `[CONFIRMED]` Adapt `ingest.py` and simplify/rewrite `finalize.py`; remove `advance.ps1` from active path.
8. `[CONFIRMED]` Adapt Word masters for explicit headline and natural page flow.
9. `[CONFIRMED]` Build bounded tests/fixtures tied to hard gates or direct HappyPath value.
10. `[CONFIRMED]` Produce documentation/release evidence.
11. `[CONFIRMED]` Run first real ~8-job cluster pilot.
12. `[CONFIRMED]` Evaluate local metrics and change only one variable at a time.

## 10.3 Dependencies

- `[CONFIRMED]` P0.7 source release must remain available as migration source.
- `[CONFIRMED]` Candidate authority files and Word masters must hash-match expected source versions.
- `[CONFIRMED]` Model routing facts must be re-verified because they are volatile.
- `[CONFIRMED]` Batch plan must be human-approved and frozen before Stage 1.
- `[CONFIRMED]` P0.8 must not require unresolved new architecture decisions from the builder.

## 10.4 Intended model roles

- `[CONFIRMED]` Optional preflight: Terra XHigh, once, all vacancy summaries, non-authoritative.
- `[CONFIRMED]` Stage 1: Sol Max, one chat/cluster, employer decision architecture + retrieval + strategy.
- `[CONFIRMED]` Stage 2: Terra Max, one chat/cluster, complete package + self-refinement.
- `[CONFIRMED]` Stage 3: Sol Max pilotdefault, one chat/cluster, independent final writer + selective review.
- `[CONFIRMED]` Code: deterministic ingest/finalize only.
- `[CONFIRMED]` Human: cluster approval, final semantic review, isolated RERUN, submission.

## 10.5 Stopping / acceptance criteria

- `[CONFIRMED]` Repository matches target tree.
- `[CONFIRMED]` Exactly two active scripts and three stage instruction files.
- `[CONFIRMED]` All five schemas parse and fixtures behave as intended.
- `[CONFIRMED]` Hard truth/identity/rendering boundaries are mechanically tested.
- `[CONFIRMED]` Masters are visually checked across sparse/normal/dense cases.
- `[CONFIRMED]` Operator can perform first run without new product/data-contract decisions.
- `[CONFIRMED]` First pilot measures the actual optimization function rather than generic test-count success.

---

# 11. Best-supported P0.8 reconstruction

## 11.1 Purpose and success criteria

- `[CONFIRMED]` P0.8 is the **Selective Quality MVP** for about 40 human-approved Norwegian job applications.
- `[CONFIRMED]` Primary objective:

```text
Q_happy = (Median(q) + Mean(Top80%(q))) / 2
```

- `[CONFIRMED]` `q_i` is human 1–10 overall package quality after rendering, primarily reflecting expected interview impact.
- `[CONFIRMED]` Secondary priorities: READY share → human minutes per ready package → weak-tail recall → credits per ready package → total throughput time.
- `[CONFIRMED]` Hard truth/identity/useability constraints remain non-negotiable and are not part of the weighted tie-breaker.

**Anchor check:** `CONFIRMS` and `EXTENDS` the supplied P0.8 anchor by adding the full metric and tie-breaker semantics.

## 11.2 Scope

- `[CONFIRMED]` ~40 human-approved jobs.
- `[CONFIRMED]` Cluster planning, vacancy normalization, decision strategy, CV, application letter, portal answers, selective review, DOCX/PDF, review queue, targeted rerender and pilot logging.
- `[CONFIRMED]` Five normal production clusters of ~8 jobs.
- `[CONFIRMED]` A complete package is attempted for every mechanically feasible user-selected job.

**Anchor check:** `CONFIRMS`.

## 11.3 Explicit non-goals

- `[CONFIRMED]` Automatic job search.
- `[CONFIRMED]` Automatic fit veto.
- `[CONFIRMED]` Automatic employer research.
- `[CONFIRMED]` Employer contact/submission.
- `[CONFIRMED]` Interview training.
- `[CONFIRMED]` Outcome learning that auto-mutates sources/prompts.
- `[CONFIRMED]` Memory/archetype cache.
- `[CONFIRMED]` Vector DB.
- `[CONFIRMED]` Multi-agent architecture.
- `[CONFIRMED]` Automatic model router.
- `[CONFIRMED]` Automatic retry/repair loop.
- `[CONFIRMED]` Full-package best-of-N.
- `[CONFIRMED]` LLM-as-judge.

**Anchor check:** `CONFIRMS`.

## 11.4 Core architectural principles

- `[CONFIRMED]` Three model stages: think → write → write finished.
- `[CONFIRMED]` Sol handles non-linear strategy and final persuasion; Terra handles large structured native-language package production.
- `[CONFIRMED]` One job at a time inside each cluster chat.
- `[CONFIRMED]` Source-grounded persuasion, strong synthesis, single professional backbone.
- `[CONFIRMED]` Stage 3 final authority within hard truth boundaries.
- `[CONFIRMED]` Partial success and no unnecessary uniformity.
- `[CONFIRMED]` Mechanical minimalism: code only for truth/identity/channel/rendering/useability.
- `[CONFIRMED]` Human authority at irreversible boundary.
- `[CONFIRMED]` No hidden retries.

**Anchor check:** `CONFIRMS` and `EXTENDS`.

## 11.5 Canonical source-of-truth model

- `[CONFIRMED]` `Work_experience.md` owns work/project facts, personal contribution and lifecycle.
- `[CONFIRMED]` `Education.md` owns degree/institution/course/academic facts.
- `[CONFIRMED]` `Other_high_value_information.md` owns other stable candidate facts.
- `[CONFIRMED]` `CV_BASELINE.md` is derived: it owns rendering structure/static chronology but cannot create candidate facts.
- `[CONFIRMED]` Vacancy is untrusted external input and must not override candidate truth or system instructions.
- `[CONFIRMED]` `job_identity.json` is immutable after ingest except explicit operator correction/re-ingest.
- `[CONFIRMED]` `batch_plan.json` is the human-approved batch/clustering control plane and freezes at Stage 1 start.

**Anchor check:** `CONFIRMS` and `EXTENDS`.

## 11.6 Candidate/source files and schemas

### Stable context files

- `[CONFIRMED]` `Work_experience.md`
- `[CONFIRMED]` `Education.md`
- `[CONFIRMED]` `Other_high_value_information.md`
- `[CONFIRMED]` `CV_BASELINE.md`
- `[CONFIRMED]` `WRITING_STANDARD.md` — planned consolidation of overlapping Norwegian writing guidance.
- `[CONFIRMED]` `PERSUASION_CALIBRATION.md` — retained separately for user-confirmed calibration.
- `[CONFIRMED]` `CV_MASTER.docx`
- `[CONFIRMED]` `APPLICATION_MASTER.docx`

### Exactly five schemas

- `[CONFIRMED]` `schemas/batch_plan.schema.json`
- `[CONFIRMED]` `schemas/job_identity.schema.json`
- `[CONFIRMED]` `schemas/package.schema.json`
- `[CONFIRMED]` `schemas/progress.schema.json`
- `[CONFIRMED]` `schemas/review.schema.json`

`[CONFIRMED]` Draft and final package share one package schema and differ by `source_stage`.

**Anchor check:** `EXTENDS`.

## 11.7 Context assembly / retrieval strategy

- `[CONFIRMED]` Stage 1 does the heavy candidate retrieval once per job after completing candidate-blind Phase A.
- `[CONFIRMED]` Stage 1 records only selected main evidence and realistic strong alternatives, not a broad cluster evidence dump.
- `[CONFIRMED]` Each evidence record includes evidence ID, source file/heading, core fact, personal contribution, lifecycle, safe strong formulation, relevant decision test and primary channel role.
- `[CONFIRMED]` Stage 2 reads exact source sections cited by `strategy.md` and should not reread the entire candidate corpus by default.
- `[CONFIRMED]` Stage 3 performs targeted source checks only when changing strategy/evidence.
- `[CONFIRMED]` No vector DB, embedding layer, memory cache or automated RAG subsystem in P0.8.

**Anchor check:** `EXTENDS`.

## 11.8 Research / external-information strategy

- `[CONFIRMED]` Automatic employer web research is outside P0.8.
- `[CONFIRMED]` Vacancy and operator notes are the primary employer/job inputs.
- `[INFERRED]` Manual external research may still be supplied in notes if the operator chooses, provided it does not become candidate truth; the final spec does not make this a standard stage.
- `[UNKNOWN]` Whether future bounded employer research will be activated; it is in deferred backlog with an activation criterion.

**Anchor check:** `CONFIRMS` non-goal; manual research remains `INFERRED`.

## 11.9 Vacancy intake

- `[CONFIRMED]` `ingest.py` is one of only two active scripts.
- `[CONFIRMED]` Input lives under `inbox/<batch_id>/` with human-approved `batch_plan.json` and per-job vacancy/notes files.
- `[CONFIRMED]` Optional `PORTFOLIO_PLAN.json` can be generated by a one-off Terra XHigh preflight but is never authoritative.
- `[CONFIRMED]` Ingest normalizes vacancy input, validates IDs and batch plan, creates runtime structure, writes identity and initializes progress.
- `[CONFIRMED]` Mechanically unreadable input can be blocked; semantic fit is not a blocker.

**Anchor check:** `EXTENDS`.

## 11.10 Fit analysis / positioning

- `[CONFIRMED]` No numeric fit score and no GO/NO-GO after human selection.
- `[CONFIRMED]` Stage 1 Phase A: candidate-blind dominant employer problem, 2–4 decision tests, must-haves, selection regime, seniority/autonomy, hiring risk and channel constraints.
- `[CONFIRMED]` Stage 1 Phase B: primary candidate identity, headline, shortlist thesis, two main evidence bridges, support evidence, strongest alternative route, objection/reframe, motivation bridge, channel allocation and Priority A/B.
- `[CONFIRMED]` Strategy follows a single-backbone principle: identity + dominant problem + two evidence bridges + optional controlled differentiator.

**Anchor check:** `EXTENDS`.

## 11.11 CV tailoring

- `[CONFIRMED]` Dynamic fields: explicit headline, profile, key competencies, employment overrides.
- `[CONFIRMED]` Static chronology and formal identity remain in baseline.
- `[CONFIRMED]` Older employment overrides must work.
- `[CONFIRMED]` Missing override falls back to baseline content.
- `[CONFIRMED]` Normal target is natural 1–2 page CV flow, not forced two pages.
- `[CONFIRMED]` Over-budget is soft review if document remains usable.
- `[CONFIRMED]` Stage 3 may alter headline/identity/evidence if truthful.

**Anchor check:** `EXTENDS`.

## 11.12 Application-letter generation

- `[CONFIRMED]` Stage 2 writes complete application when required.
- `[CONFIRMED]` Letter should center employer problem, motivation, 2–3 coherent evidence bridges and contribution logic.
- `[CONFIRMED]` It should not paraphrase the CV point-for-point.
- `[CONFIRMED]` Priority A gets internal comparison of three materially different application openings; only winner survives.
- `[CONFIRMED]` Stage 3 may patch or fully rewrite.
- `[CONFIRMED]` Letter page budget is normally one page but is soft if overage does not make output unusable.

**Anchor check:** `EXTENDS`.

## 11.13 Portal/form-answer handling

- `[CONFIRMED]` `job_identity.json` can require portal answers and stores portal questions/limits.
- `[CONFIRMED]` `question_id` must be unique.
- `[CONFIRMED]` `portal_required=true` requires answers to all question IDs.
- `[CONFIRMED]` Stage 2 writes direct answers to exact questions and limits.
- `[CONFIRMED]` Finalizer renders separate `portal_answers.md` when applicable.
- `[CONFIRMED]` Portal issues may generate CHECK unless they violate a required channel/hard limit enough to make package unusable.

**Anchor check:** `EXTENDS`.

## 11.14 Document/template/rendering architecture

- `[CONFIRMED]` Deterministic Word-master based rendering.
- `[CONFIRMED]` `finalize.py` copies and mutates a working master, not the original.
- `[CONFIRMED]` Content controls/tags, conditional blocks and dynamic employment sections are part of the contract.
- `[CONFIRMED]` LibreOffice conversion with timeout.
- `[CONFIRMED]` PDF page count and selectable text validated.
- `[CONFIRMED]` Employer-facing text scanned for placeholders/private IDs.
- `[CONFIRMED]` Natural page flow and explicit headline are P0.8 template changes.
- `[CONFIRMED]` DOCX metadata cleanup is desirable but not necessarily pilot-blocking.

**Anchor check:** `EXTENDS`.

## 11.15 QA / validation / provenance

- `[CONFIRMED]` Hard gates only for wrong/inconsistent identity, invalid package, unknown employment ID, unmergeable baseline, missing required channel, unsupported formal candidate facts, private/internal leakage, or unrenderable/unopenable documents.
- `[CONFIRMED]` Soft issues produce `DELIVERED_CHECK` or `DELIVERED_RERUN`, not package loss.
- `[CONFIRMED]` Stage 3 review schema has READY/CHECK/RERUN and max three concrete reasons.
- `[CONFIRMED]` No confidence score, no numeric quality score, no LLM-as-judge.
- `[CONFIRMED]` Evidence refs stay internal and support traceability.
- `[CONFIRMED]` Tests should map to actual hard boundaries or direct HappyPath value, not build a giant QA platform.

**Anchor check:** `CONFIRMS` and `EXTENDS`.

## 11.16 Human review / approval

- `[CONFIRMED]` Operator approves/finalizes `batch_plan.json` and clustering.
- `[CONFIRMED]` READY: rapid final review.
- `[CONFIRMED]` CHECK: focused local review/edit.
- `[CONFIRMED]` RERUN: separate one-job improvement chat outside normal three-stage flow.
- `[CONFIRMED]` Human owns final semantic approval and submission.
- `[CONFIRMED]` `REVIEW_QUEUE.md` exists specifically to reduce human review effort.

**Anchor check:** `CONFIRMS`.

## 11.17 Package / deliverable structure

- `[CONFIRMED]` `draft_package.json` from Stage 2.
- `[CONFIRMED]` `final_package.json` + `review.json` from Stage 3.
- `[CONFIRMED]` Rendered per job: `cv.docx`, `cv.pdf`, optional `application.docx/pdf`, optional `portal_answers.md`.
- `[CONFIRMED]` Batch-level `REVIEW_QUEUE.md`.
- `[CONFIRMED]` Per-job result statuses: `DELIVERED_READY`, `DELIVERED_CHECK`, `DELIVERED_RERUN`, `FAILED`.

**Anchor check:** `EXTENDS`.

## 11.18 Versioning / state management

- `[CONFIRMED]` `schema_version: 0.8.0` across runtime contracts.
- `[CONFIRMED]` `batch_plan.json` freezes at first Stage 1 start.
- `[CONFIRMED]` Artifact existence/validation is primary state.
- `[CONFIRMED]` Minimal `progress.json` records completed/remaining/failed/next.
- `[CONFIRMED]` Progress can be reconstructed from artifacts.
- `[CONFIRMED]` No general state machine, `_DONE.md`, large batch status or hidden retry.
- `[CONFIRMED]` Continuation resumes from first missing/invalid artifact.

**Anchor check:** `EXTENDS`.

## 11.19 Automation / model / tool responsibilities

| Responsibility | Owner | Status |
|---|---|---|
| Batch/cluster approval | Human | `CONFIRMED` |
| Vacancy normalization / run setup | `ingest.py` | `CONFIRMED` |
| Employer decision model + evidence strategy | Stage 1 Sol Max | `CONFIRMED` |
| Complete native Norwegian package | Stage 2 Terra Max | `CONFIRMED` |
| Final persuasion/strategy + review triage | Stage 3 Sol Max | `CONFIRMED` |
| Baseline merge / render / queue / partial success | `finalize.py` | `CONFIRMED` |
| Final semantic approval / submission | Human | `CONFIRMED` |
| RERUN | Separate explicit one-job chat | `CONFIRMED` |
| Automatic routing/retry/research/submission | Nobody; deferred/rejected | `CONFIRMED` |

**Anchor check:** `CONFIRMS`.

## 11.20 Implementation sequence

- `[CONFIRMED]` Wave 1: authority verification and P0.7 backup.
- `[CONFIRMED]` Wave 2: repository/contracts/schemas/baseline/writing standard/root files.
- `[CONFIRMED]` Wave 3: three stage instructions, recovery and operator prompts.
- `[CONFIRMED]` Wave 4: adapt ingest, simplify/rewrite finalizer, remove advance from active path.
- `[CONFIRMED]` Wave 5: templates/headline/natural flow/older overrides/application/portal/metadata.
- `[CONFIRMED]` Wave 6: bounded tests/fixtures for hard gates, rendering, partial success, `--job`.
- `[CONFIRMED]` Wave 7: documentation, release, hashes.
- `[CONFIRMED]` Then first real pilot.

**Anchor check:** `EXTENDS`.

## 11.21 Acceptance criteria

- `[CONFIRMED]` Target tree exactly matches documented repository.
- `[CONFIRMED]` Exactly two active scripts and three stage instructions.
- `[CONFIRMED]` All five schemas parse and fixtures pass/fail as intended.
- `[CONFIRMED]` Authorities unchanged and hash-verified.
- `[CONFIRMED]` Baseline parses and employment IDs are unique.
- `[CONFIRMED]` Rendering passes sparse/normal/dense/letter/no-letter/unit/reference/portal cases.
- `[CONFIRMED]` Partial success and single-job rerender work.
- `[CONFIRMED]` First pilot can be launched with no new design decision.
- `[CONFIRMED]` Product acceptance uses human `Q_happy`, ready rate, edit minutes, TailRecall20, review load and credits.

**Anchor check:** `EXTENDS`.

## 11.22 Known risks / open design questions

- `[OPEN]` Stage 3 Sol Max versus Sol XHigh; pilot/A-B decision.
- `[OPEN]` Stage 2 Terra Max versus Terra XHigh; later A-B.
- `[OPEN]` Whether cluster size 10 can equal ~8 on quality/review; later A-B.
- `[OPEN]` How accurately CHECK/RERUN identifies human bottom-20; must be measured.
- `[OPEN]` Whether optional Terra XHigh cluster preflight saves enough human effort to justify use.
- `[OPEN]` Exact production root path conflict: external anchor `C:\Codex\Jobbsok_26\` versus final spec `C:\Codex\Jobbsok_26_P0.8`.
- `[OPEN]` Model names/effort availability/credits/context are volatile and must be reverified.
- `[INFERRED]` Stage 3 freedom could increase factual risk if targeted source check is applied poorly; final spec mitigates by requiring known employment IDs and affected-source checking.
- `[INFERRED]` Human review quality becomes a meaningful part of the product metric because `q_i` is operator-scored.

---

# 12. Later-than-P0.8 evidence

| Later change / finding | Version/phase | Difference from P0.8 | Supersedes P0.8? | Backportable? | Confidence |
|---|---|---|---|---|---|
| No P0.9+ implementation/design is evidenced in this chat after the final P0.8 normative spec | N/A | N/A | No | N/A | High |

`[CONFIRMED]` The final event before this archival prompt is the generation of the P0.8 final normative specification. No later framework version should be silently merged into §11.

---

# 13. Open questions, contradictions and reconciliation hazards

| Issue | Competing interpretations | Best current interpretation | Evidence needed to resolve |
|---|---|---|---|
| Exact local root path | External baseline anchor says `C:\Codex\Jobbsok_26\`; P0.8 spec commands say `C:\Codex\Jobbsok_26_P0.8` | `OPEN`; architecture unaffected, implementation launcher must pick one | Later implementation prompt/release tree |
| P0.7 release date | External anchor says 2026-08-04; P0.7 test report dated 2026-08-01 and audit report was created around 2026-08-03 | Treat external anchor date as release-state anchor; test date is earlier internal evidence | P0.7 ZIP metadata or builder handoff message |
| P0.7 audit “critical Stage3→4 bypass” | Under reliability objective it was critical; under P0.8 quality objective Stage 3 intentionally may change evidence | The bug matters only as P0.7 contract mismatch; P0.8 intentionally removes that restriction and enforces baseline/source truth instead | No further evidence needed unless auditing P0.7 itself |
| Hard page budget | P0.7 hard gate vs P0.8 soft CHECK | P0.8 supersedes hard gate for future design | P0.8 implementation must encode soft semantics |
| Global completeness | P0.7 finalizer denies global PASS if any job missing vs P0.8 partial success | P0.8 supersedes as product behavior | P0.8 finalizer implementation |
| `_DONE.md` / `BATCH_STATUS.md` hardening | Audit proposed stronger parsers; later redesign deletes both | Delete rather than harden in P0.8 | P0.8 repository build |
| Per-job compute classes | PRIME/STANDARD/MANUAL-LATER proposed earlier vs Priority A/B final | Priority A/B clearly supersedes router classes | Final P0.8 spec |
| Cluster size | Initial P0.8 4×10 vs later 5×8 | 5×~8 final | Attached DOCX + final spec |
| Model effort | Earlier P0.7 Stage3/4 XHigh vs P0.8 all-Max pilot | P0.8 all-Max for first pilot; later A/B downshift | Pilot results |
| Optional cluster preflight | Could look like fourth stage | Final spec explicitly says non-authoritative optional preflight and not one of 15 production chats | Operator docs/implementation |
| `PORTFOLIO_PLAN.json` vs `batch_plan.json` | Both appear under inbox | Portfolio plan is optional suggestion; batch plan is human-approved authority | Final spec section 12/19 |
| Automatic employer research | Earlier P0.6-era research discussions existed elsewhere | Explicitly non-goal in P0.8 mainline | Future deferred decision only |
| UI chat title | User asks filename from actual visible name, runtime does not expose it | Descriptive fallback used | External reconciler can rename if UI title known |

---

# 14. Inter-chat reconciliation hooks

1. **If a sibling summary says P0.7 is still the active target architecture**, this chat is downstream if that sibling predates the explicit `Q_happy` user correction and P0.8 redesign.
2. **If a sibling summary has P0.8 as 4×10**, this chat is downstream: attached refinement explicitly replaces 4×10 with 5×~8, normal 6–10.
3. **If a sibling has PRIME/STANDARD/MANUAL-LATER**, this chat is downstream: final refinement rejects that as overcomplicated and uses Priority A/B only.
4. **If a sibling retains four stages**, compare whether it predates the user’s “redesign from scratch” request. Final P0.8 uses exactly three.
5. **If a sibling retains `advance.ps1`**, it is P0.7-era. Final P0.8 has exactly two active scripts and removes advance.
6. **If a sibling hard-fails CV>2 or letter>1**, it is earlier reliability-oriented logic. Final P0.8 uses soft page-budget review.
7. **If a sibling says Stage 3 cannot introduce new employment IDs relative to draft**, it predates the quality-first correction. P0.8 permits different baseline-known evidence with targeted source verification.
8. **If another chat contains an implemented P0.8 ZIP**, it is downstream of this chat because this chat ends with the spec only.
9. **If another chat contains the P0.8 implementation prompt**, it is likely the immediate downstream implementation handoff.
10. **If another chat shows first real ~8-job pilot metrics**, it is downstream and should be used to resolve Sol Max/XHigh, Terra Max/XHigh and cluster-size questions.
11. **If a sibling says the final P0.8 spec is shorter/different**, compare against SHA `0dddf4b4c29fcee407ff568cfc2f1629ed01d3e8aa88129497da3a1d748ec0ba` and frontmatter `FINAL_NORMATIVE_SPECIFICATION`.
12. **If another summary uses `C:\Codex\Jobbsok_26\` as canonical root**, reconcile against this spec’s `C:\Codex\Jobbsok_26_P0.8` commands before implementation.
13. **If another chat continues archetype memory/cache design**, do not backport it into P0.8 unless there is an explicit later user decision: this chat explicitly moved it to a later overhaul.
14. **If another chat says P0.7 had no real implementation**, it conflicts with this chat’s directly audited 52-file release ZIP.
15. **If another chat reports P0.7 30/33 tests**, distinguish P0.6 baseline (30 + 3 skips) from P0.7 release (32 + 2 blocked/skipped).

---

# 15. Appendix — residual signal

## 15.1 Stable terminology

- `Selective Quality MVP` = final internal product name for P0.8.
- `Q_happy` = average of median package quality and mean of top 80% package quality.
- `Priority A/B` = within-cluster quality/opportunity ordering, **not** model routing.
- `READY/CHECK/RERUN` = Stage 3 human-review triage, not quality score or release verdict.
- `DELIVERED_READY / DELIVERED_CHECK / DELIVERED_RERUN / FAILED` = finalizer delivery statuses.
- `Phase A / Phase B` = internal two-pass reasoning/edit sequence within one model chat, not separate prompts/models.
- `single-backbone` = one dominant candidate identity + employer problem + two evidence bridges.
- `partial success` = per-job deliverability survives cluster-level failures.
- `targeted source check` = Stage 3 reopens only affected sources when strategy changes.

## 15.2 Rejected or deferred alternatives worth preserving

- `[REJECTED]` Dual prompt/model switching inside each stage.
- `[REJECTED]` Four-stage P0.8 continuation of vacancy→strategy→writer→mirror.
- `[REJECTED]` Two-stage compression; judged too output-heavy and cognitively conflated.
- `[REJECTED]` 4×10 as optimal P0.8 default; technically feasible but less quality-focused than 5×8.
- `[REJECTED]` PRIME/STANDARD/MANUAL-LATER per-job model router.
- `[REJECTED]` Confidence scores.
- `[REJECTED]` Global batch-PASS as product objective.
- `[REJECTED]` Hard page veto.
- `[REJECTED]` `_DONE.md` + large `BATCH_STATUS.md` for P0.8.
- `[REJECTED]` Evidence lock that prevents final Sol from fixing strategy.
- `[DEFERRED]` Archetype memory/cache.
- `[DEFERRED]` Luna Writer.
- `[DEFERRED]` Ultra.
- `[DEFERRED]` automatic routing.
- `[DEFERRED]` full-package best-of-N.
- `[DEFERRED]` automatic employer research.
- `[DEFERRED]` outcome learning.
- `[DEFERRED]` full orchestration/vector store/LLM judge/automatic retry.

## 15.3 Quantitative anchors

- P0.7 target batch: 40 jobs.
- P0.7 topology: 2×20 macro → 4×10 mini.
- P0.7 HappyPath: 12 prompts/chats.
- P0.7 release: 52 files.
- P0.7 tests: 32 PASS + 2 BLOCKED/skipped.
- P0.8 target batch: ~40 jobs.
- P0.8 topology: 5×~8; normal range 6–10.
- P0.8 HappyPath: 15 model chats.
- P0.8 active scripts: 2.
- P0.8 stage models: Sol Max, Terra Max, Sol Max.
- Priority A: roughly first 75–80% of each cluster.
- Priority B: roughly last 20–25%.
- Review reasons: maximum 3.
- Human package score: 1–10.
- P0.8 final spec: 3,825 lines / 17,151 words.

## 15.4 Exact final P0.8 repository objects

`[CONFIRMED]` Root target includes:

```text
.gitignore
AGENTS.md
MODEL_ROUTING.md
START_HERE.md
requirements.txt
inbox/
context/
stage_instructions/
schemas/
scripts/
runs/
tests/
docs/
```

`[CONFIRMED]` Context target includes:

```text
CV_BASELINE.md
Education.md
Other_high_value_information.md
PERSUASION_CALIBRATION.md
Work_experience.md
WRITING_STANDARD.md
context/templates/APPLICATION_MASTER.docx
context/templates/CV_MASTER.docx
```

`[CONFIRMED]` Stage instructions:

```text
stage_instructions/01_strategy.md
stage_instructions/02_writer.md
stage_instructions/03_final.md
```

`[CONFIRMED]` Schemas:

```text
schemas/batch_plan.schema.json
schemas/job_identity.schema.json
schemas/package.schema.json
schemas/progress.schema.json
schemas/review.schema.json
```

`[CONFIRMED]` Scripts:

```text
scripts/ingest.py
scripts/finalize.py
```

`[CONFIRMED]` Runtime per cluster:

```text
input/jobs/<job_id>/job_identity.json
input/jobs/<job_id>/notes.md
input/jobs/<job_id>/vacancy.md
strategy/cluster_notes.md
strategy/cluster_plan.json
strategy/progress.json
strategy/jobs/<job_id>/strategy.md
drafts/progress.json
drafts/jobs/<job_id>/draft_package.json
final/progress.json
final/jobs/<job_id>/final_package.json
final/jobs/<job_id>/review.json
rendered/<job_id>/cv.docx
rendered/<job_id>/cv.pdf
rendered/<job_id>/application.docx      # conditional
rendered/<job_id>/application.pdf       # conditional
rendered/<job_id>/portal_answers.md     # conditional
```

## 15.5 Final spec internal production rule

`[CONFIRMED]` The final structural rule is:

> No file without a purpose, no contract without an owner, no output without a consumer, no hard gate without direct protection of truth or usability, and no implementation decision left to the builder if it can be decided in the specification.

This is a useful fingerprint for matching the exact final P0.8 document against sibling outputs.

---

# 16. Final state snapshot

## Apparent framework version/state

- `[CONFIRMED]` **Implemented runtime:** P0.7.
- `[CONFIRMED]` **Latest normative target:** P0.8 `0.8.0`, `FINAL_NORMATIVE_SPECIFICATION`.
- `[CONFIRMED]` **P0.8 implementation status:** not implemented in this chat.

## Most authoritative active decisions

- `[CONFIRMED]` Optimize `Q_happy`, not uniformity.
- `[CONFIRMED]` 3 stages: Sol Max → Terra Max → Sol Max.
- `[CONFIRMED]` 5 strategic clusters × ~8 jobs; normal 6–10.
- `[CONFIRMED]` Priority A/B only; no per-job model router.
- `[CONFIRMED]` Stage 3 can freely correct strategy within truth boundaries.
- `[CONFIRMED]` READY/CHECK/RERUN; max three concrete reasons; no confidence/score.
- `[CONFIRMED]` Exactly two active scripts.
- `[CONFIRMED]` Partial success, soft page budgets, targeted `--job` rerender.
- `[CONFIRMED]` Human owns cluster approval, final semantic approval and submission.

## What actually exists

- `[CONFIRMED]` P0.7 release ZIP, fully implemented and audited.
- `[CONFIRMED]` P0.7 test/render evidence.
- `[CONFIRMED]` Final P0.8 normative Markdown specification.
- `[CONFIRMED]` Attached 62-page P0.8 refinement transcript.

## What is merely planned

- `[CONFIRMED]` P0.8 repository migration/build.
- `[CONFIRMED]` P0.8 schemas, stage files, adapted scripts/templates/tests.
- `[CONFIRMED]` First real 8-job cluster pilot.
- `[CONFIRMED]` Post-pilot A/B effort/model adjustments.

## Immediate intended next step

- `[INFERRED]` Hand the final P0.8 spec plus P0.7 source release to a builder/local Codex implementation run, producing a P0.8 release without reopening architecture.
- `[CONFIRMED]` After implementation, run one real coherent cluster before scaling to all 40 jobs.

## Main unresolved questions

- `[OPEN]` Sol Max vs XHigh in Stage 3 after pilot.
- `[OPEN]` Terra Max vs XHigh in Stage 2 after pilot.
- `[OPEN]` 8 vs 10 jobs per cluster under real quality metrics.
- `[OPEN]` TailRecall20/review-load accuracy.
- `[OPEN]` Exact local root folder naming (`Jobbsok_26` vs `Jobbsok_26_P0.8`).
- `[OPEN]` Whether later sibling chats have already implemented P0.8.

## Strongest chronology clues

1. P0.7 ZIP implementation necessarily follows the P0.7 implementation prompt.
2. `Q_happy` correction necessarily follows the P0.7 audit.
3. 5×8 necessarily follows the initial P0.8 4×10 proposal.
4. Final P0.8 Markdown necessarily follows the uploaded P0.8 refinement DOCX.
5. Any implemented P0.8 release or real 8-job pilot is downstream of this chat’s terminal state.

## Confidence / caveats

- `[CONFIRMED]` High confidence on terminal P0.8 design because the final artifact was directly generated and inspected.
- `[CONFIRMED]` High confidence on P0.7 implementation because the ZIP, reports, tests and rendering were directly audited.
- `[INFERRED]` Medium confidence on the exact earliest chronology before the visible cluster-size discussion because some earlier P0.6/P0.7 state entered the chat through prior-context summaries and existing artifacts rather than being re-derived turn-by-turn here.
- `[UNKNOWN]` Global ordering against sibling chats remains intentionally unresolved where no dependency evidence exists.

---

# QC pass performed before save

- Late user corrections checked: **YES** — `Q_happy` correction and “memory → next overhaul” preserved.
- User acceptance/rejection distinguished from assistant proposal: **YES**.
- Version numbers and filenames checked: **YES**.
- External/parallel chat signal captured: **YES** — attached P0.8 DOCX.
- Final-turn-only changes checked: **YES** — 5×8, Priority A/B, final spec generation.
- Plans vs implementations separated: **YES** — P0.8 spec is not implementation.
- Superseded decisions marked: **YES**.
- Assistant proposals not silently promoted: **YES**.
- Chronology clues and terminal fingerprint included: **YES**.
- P0.9+ evidence kept out of P0.8: **YES** — none evidenced.
- Anchor contradictions flagged: **YES** — especially local path naming.
- Redundant prose reduced while retaining distinct state signal: **YES**.
