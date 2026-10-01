# Jobbsøk_26 — Per-Chat Integration Summary

## Chat-title status

- `[UNKNOWN]` The actual visible UI title of this chat is not exposed to the executing model.
- `[CONFIRMED]` To avoid inventing provenance, this artifact uses the descriptive fallback title **“Jobbsøk_26 P0.7–P0.8 Selective Quality Redesign”** only for the filename and internal navigation.
- `[CONFIRMED]` This file reconstructs only the state supported by this chat plus the fixed baseline anchors supplied in the integration prompt. Where an anchor contains information not independently evidenced by this chat, that is stated explicitly.

---

# 0. Baseline-anchor cross-check

| Anchor | Chat status | Reconstruction |
|---|---|---|
| **P0.5.3** — superseded API/SDK four-call architecture; Pydantic Structured Outputs, docxtpl, LLM-as-judge; 21/21 tests; offline E2E only | **SILENT / PARTIAL CONFIRMATION** | `[CONFIRMED]` This chat treats P0.5.x as historical/superseded material and explicitly prevents old API/orchestrator/LLM-judge architecture from re-entering the active MVP. `[UNKNOWN]` The exact 21/21 count and all P0.5.3 implementation details are not independently re-established in this chat; they come from the supplied baseline anchor. |
| **P0.6** — superseded manual four-stage, 4×10 macro / 8×5 mini, 24-prompt HappyPath, same three scripts, 30/33 tests | **CONFIRMS + EXTENDS** | `[CONFIRMED]` P0.6 is the implementation substrate from which the first final P0.7 design was migrated. `[CONFIRMED]` This chat carries forward a substantial P0.6.1 hardening list: older-employment override rendering, batch completeness, identity anchoring, page budgets, advance guards, ingest hardening, timeout, review/state checks, unit/reference, layout balance. `[UNKNOWN]` The exact 30/33 count is anchor-supplied rather than re-derived here. |
| **P0.7** — implemented 2026-08-04 release, manual 4-stage physically isolated flow; Terra Max → Sol Max → Terra XHigh → Sol XHigh; 2×20 macro + 4×10 mini; 12 prompts; three scripts; 52 files; 32/34 tests, two blocked for no PowerShell; no real vacancy/model pilot | **CONFIRMS + EXTENDS** | `[CONFIRMED]` This chat independently converges on and then audits exactly this four-stage P0.7 topology. `[CONFIRMED]` The uploaded P0.7 release audit independently verified 52 files, 32/34 tests with two blocked because PowerShell was unavailable, and no real Terra/Sol vacancy production run. `[EXTENDS]` The chat found several concrete implementation weaknesses, especially the mutable Stage-4 draft-reference bypass, weak `_DONE.md`/review heading parsing, missing target-scale 20/10 stress evidence, and visually weak CV page balance. |
| **P0.8 “Selective Quality MVP” FINAL_NORMATIVE_SPECIFICATION** — dated 2026-08-04, ~3800 lines, 3 stages Sol Max → Terra Max → Sol Max, 5 clusters ~8, 15 chats, two scripts, truth-bounded Stage-3 authority, READY/CHECK/RERUN, partial-success finalizer, `--job` rerender, not implemented | **CONFIRMS DESIGN; CHAT DOES NOT INDEPENDENTLY PROVE THE FINAL SPEC ARTIFACT** | `[CONFIRMED]` The terminal design in this chat matches the three-stage, 5×~8, Sol→Terra→Sol architecture and two-script simplification. `[CONFIRMED]` The user’s final substantive request before this integration pass was to *plan* the final P0.8 architecture/specification document, explicitly not write it yet. `[INFERRED]` Therefore a sibling/later chat containing the completed `FINAL_NORMATIVE_SPECIFICATION` is downstream of this chat, even though the external anchor establishes that such a spec now exists. |
| **Redesign trigger** — optimize `Q_happy = avg(median(package_quality), mean(top_80%(package_quality)))`; bottom 20% handled separately | **CONFIRMS — USER-EXPLICIT** | `[CONFIRMED]` This was the decisive user correction that overturned the reliability/uniformity bias of the prior audit. The user explicitly stated that if ~75% of packages are top quality, the system already saves enormous human effort, and weak packages can receive another round outside the framework. |
| **P0.8 non-goals** — memory/archetype cache, vector DB, multi-agent, automatic routing, best-of-N, LLM judge, automatic retries, automatic employer research/submission | **CONFIRMS** | `[CONFIRMED]` These were repeatedly rejected or deferred in this chat. `[CONFIRMED]` An archetype-memory idea was explored in depth and then explicitly placed by the user in the “next overhaul” box because it violated MVP-KISS for the current release. |
| **Cost hierarchy** — Human Effort > Human Complexity > LLM Complexity > LLM Effort | **CONFIRMS** | `[CONFIRMED]` The user repeatedly prioritizes saved human work and simplicity over model-credit minimization. `[EXTENDS]` The later quality objective makes the hierarchy operational: model compute should be spent where it raises the strong majority’s package quality, not on forcing uniform quality in the worst tail. |
| **Candidate truth files** — `Work_experience.md`, `Education.md`, `Other_high_value_information.md`; `CV_BASELINE.md` derived only | **CONFIRMS** | `[CONFIRMED]` The P0.7 release root instructions, migration prompt, audit, and P0.8 redesign consistently preserve these three candidate authorities and the derived-baseline rule. |
| **Production naming / environment** — GPT Web → Work → GPT-5.6 Sol/Terra Max; packaged for local Codex at `C:\Codex\Jobbsok_26\` | **EXTENDS / PARTIAL CONFIRMATION** | `[CONFIRMED]` This chat repeatedly assumes manual ChatGPT Work stage chats with explicit Sol/Terra model and effort selection, plus a Windows/local repository and local scripts. `[CONFIRMED]` The audited P0.7 `START_HERE.md` used a Windows `C:\Codex\...` path. `[UNKNOWN]` The exact final P0.8 local path string from the anchor is not independently fixed by the terminal chat design. |

---

# 1. Evidence rules used in this artifact

## 1.1 Claim labels

- `[CONFIRMED]` — directly stated, delivered, or independently evidenced in this chat.
- `[INFERRED]` — strongly implied by chat evidence but not directly stated.
- `[PROPOSED]` — assistant proposal not clearly adopted by the user.
- `[SUPERSEDED]` — previously active proposal/decision later replaced.
- `[REJECTED]` — explicitly rejected.
- `[OPEN]` — unresolved at the end of the visible chat.
- `[UNKNOWN]` — no sufficient evidence in this chat.

## 1.2 Authority labels

Decision-ledger authority uses:

- `USER-EXPLICIT`
- `USER-CORRECTION`
- `USER-ACCEPTED-PROPOSAL`
- `ASSISTANT-HIGH-CONFIDENCE`
- `ASSISTANT-PROPOSAL`

## 1.3 Strongest evidence anchors

1. `[CONFIRMED]` Early P0.7 dual-pass architecture state: two prompts per stage, 24 chats / 48 prompts under original 10/5 topology.
2. `[CONFIRMED]` Prompt-consolidation discussion: larger clusters, then merged prompts.
3. `[CONFIRMED]` Memory/archetype discussion: explored, then explicitly deferred.
4. `[CONFIRMED]` `jobbsøk_26_P0.7.md`: generated full P0.7 architecture, 3,134 lines / 9,480 words; SHA-256 `21b8351dd5849b2f44a486baa93751f0af54017aed3ad8e553c8d92346c33cf7`.
5. `[CONFIRMED]` `Jobbsok_26_P0.7_Implementation_Prompt.md`: generated migration/implementation order, 411 lines / 1,820 words; SHA-256 `ec491040cbf72651b6ff001f923b391bbca9868e18cf4f1423e126ff2df2ddff`.
6. `[CONFIRMED]` User-uploaded `Jobbsok_26_P0.7_Release.zip`: audited in depth.
7. `[CONFIRMED]` `Jobbsok_26_P0.7_Critical_Audit_and_Perfection_Recipe.md`: generated audit report; SHA-256 `5a5e725431ccdcc6692d6c6cf6a25ec9b99d7381a2cd2a3799405cd1143e8019`.
8. `[CONFIRMED]` User quality-objective correction: explicit shift to median + top-80 quality.
9. `[CONFIRMED]` Full P0.8 redesign discussion: first three-stage proposal, then critique/web-validation and revised final design.
10. `[CONFIRMED]` Terminal pre-integration request: user asks to plan the final comprehensive P0.8 architecture/specification document, explicitly *not write it yet*.

---

# 2. Chronology and inter-chat alignment

## 2.1 Absolute anchors

| Anchor | Date/version/artifact | Evidence | Confidence |
|---|---|---|---|
| P0.6 exists as prior implementation substrate | P0.6 | `[CONFIRMED]` P0.7 architecture and implementation prompt explicitly say migrate/patch the working P0.6 release rather than redesign blindly. | HIGH |
| Earlier P0.7 dual-pass architecture | P0.7 intermediate | `[CONFIRMED]` Chat context records a generated `Final_Jobbsok_26_P0.7_Hybrid_Multi-Model_Dual-Prompt_Architecture.md`. | HIGH |
| Single-prompt P0.7 architecture finalized | `jobbsøk_26_P0.7.md` | `[CONFIRMED]` Generated in this chat; later used as normative implementation target. | HIGH |
| P0.7 implementation migration prompt | `Jobbsok_26_P0.7_Implementation_Prompt.md` | `[CONFIRMED]` Generated in this chat. | HIGH |
| Implemented P0.7 release reviewed | `Jobbsok_26_P0.7_Release.zip` | `[CONFIRMED]` Uploaded by user and audited. | HIGH |
| P0.7 audit report | `Jobbsok_26_P0.7_Critical_Audit_and_Perfection_Recipe.md` | `[CONFIRMED]` Generated from the uploaded release. | HIGH |
| External baseline date for current P0.7 release | 2026-08-04 | `[CONFIRMED AS EXTERNAL ANCHOR]` Supplied in integration prompt, not independently dated by visible chat. | HIGH for anchor |
| Audit report internal date | 2026-08-03 | `[CONFIRMED]` Generated audit report used this date. `[OPEN]` Differs from external 2026-08-04 release date. | MEDIUM |
| Selective-quality redesign trigger | after P0.7 audit | `[CONFIRMED]` User explicitly corrects the audit’s priority function after seeing strict QA recommendations. | HIGH |
| P0.8 three-stage redesign | P0.8 conceptual/final design in chat | `[CONFIRMED]` Developed after objective shift. | HIGH |
| External final normative P0.8 specification | 2026-08-04, ~3800 lines | `[CONFIRMED AS EXTERNAL ANCHOR]` Baseline says it exists and supersedes P0.7. `[CONFIRMED]` Visible chat ends before writing it. | HIGH |
| Current integration pass | 2026-08-21 | `[CONFIRMED]` Execution metadata for this integration turn. | HIGH |

## 2.2 Relative ordering

| This chat/event | Relationship | Other event/artifact | Reason | Confidence |
|---|---|---|---|---|
| P0.6 release | before | final single-prompt P0.7 architecture | `[CONFIRMED]` P0.7 implementation prompt explicitly migrates existing P0.6. | HIGH |
| dual-prompt P0.7 architecture | before | single-prompt P0.7 architecture | `[CONFIRMED]` User asks to merge both prompts into one stronger-model stage. | HIGH |
| 2×20 / 4×10 cluster compression discussion | before | final P0.7 architecture | `[CONFIRMED]` It becomes final P0.7 topology. | HIGH |
| archetype-memory proposal | before | final P0.7 architecture | `[CONFIRMED]` User parks it in “next overhaul”. | HIGH |
| final P0.7 architecture | before | P0.7 implementation prompt | `[CONFIRMED]` Implementation prompt points to `jobbsøk_26_P0.7.md`. | HIGH |
| P0.7 implementation prompt | before | uploaded P0.7 release | `[INFERRED]` Release is presented as resulting framework implementation. | HIGH |
| P0.7 release audit | before | selective-quality objective change | `[CONFIRMED]` User explicitly reacts to audit by correcting optimization priority. | HIGH |
| strict P0.7.1 hardening recipe | before / partly superseded by | quality-first redesign | `[CONFIRMED]` Many hardening items are demoted/deferred after user correction. | HIGH |
| quality-first P0.7 optimization | before | from-scratch P0.8 redesign | `[CONFIRMED]` User then asks to redesign entire flow. | HIGH |
| first P0.8 3-stage 4×10 concept | before | refined P0.8 5×~8 design | `[CONFIRMED]` Self-critique/web-validation changes cluster count/size and simplifies classification. | HIGH |
| refined P0.8 design | before | planned final P0.8 architecture document | `[CONFIRMED]` User says “okay bra” then asks to plan final exhaustive specification file. | HIGH |
| terminal planning request | before / depends-on | external final P0.8 spec | `[INFERRED]` A sibling/later chat containing completed spec is downstream. | HIGH |

## 2.3 Terminal-sequence fingerprint

| Seq | Speaker | Event / decision / deliverable | Version/artifact affected | Evidence anchor |
|---:|---|---|---|---|
| 1 | User | Proposes reducing dual-pass prompt count through larger main/miniclusters, initially 2×20 and 4×10. | P0.7 intermediate | Cluster-capacity request. |
| 2 | Assistant | Recommends 2×20 main + 4×10 mini with internal lanes/waves; target 24 prompts under dual-pass. | P0.7 intermediate | Capacity/quality analysis. |
| 3 | User | Suggests P0.6/P0.7 hybrid: merge both prompts, use one stronger model per stage. | P0.7 architecture | Explicit user proposal. |
| 4 | Assistant | Proposes single-prompt/two-phase P0.7: Terra Max → Sol Max → Terra XHigh → Sol XHigh, 12 chats. | P0.7 | Becomes basis for final architecture. |
| 5 | User | Explores archetype/retrieval/strategy memory, then explicitly moves it to “next overhaul”. | P0.7 scope | Explicit user deferral. |
| 6 | User + Assistant | User requests final complete MVP-KISS architecture; assistant creates `jobbsøk_26_P0.7.md`. | P0.7 normative architecture | Generated artifact. |
| 7 | User + Assistant | User requests implementation prompt; assistant creates `Jobbsok_26_P0.7_Implementation_Prompt.md`. | P0.7 implementation | Generated artifact. |
| 8 | User + Assistant | User uploads `Jobbsok_26_P0.7_Release.zip`; assistant performs release audit and creates report. | P0.7 implemented release | 52 files; 32/34; render validation; defects. |
| 9 | User | Corrects objective: top-quality majority matters most; bottom 20% can be handled outside framework. | Project objective | Explicit Q-happy intent. |
| 10 | Assistant | Reframes QA around selective prediction/defer; advocates cheap truth safeguards + soft tail triage. | P0.7 quality philosophy | Web-research-supported response. |
| 11 | User + Assistant | Direct cross-reference to current P0.7; introduces quality allocation, freer final writer, headline, READY/CHECK/RERUN, partial success. | Transitional redesign | Extensive brainstorming. |
| 12 | User | Requests full from-scratch redesign, preferably less complex. | P0.8 | Explicit redesign mandate. |
| 13 | Assistant | Proposes first P0.8: Sol Max → Terra Max → Sol Max, initially 4×10, two scripts, no `advance.ps1`. | P0.8 draft | From-scratch redesign. |
| 14 | User + Assistant | User asks for deep critique/web validation; assistant retains three stages but revises to 5×~8, Priority A/B, simple state/review. | P0.8 refined | Final polished flow. |
| 15 | User | Says “okay bra” and asks to plan the definitive exhaustive P0.8 specification, explicitly not write it yet. | P0.8 final-spec planning | Terminal substantive request. |

## 2.4 Best partial chronology

```text
P0.5.3 historical API/SDK line
        ↓ superseded
P0.6 implemented manual four-stage release
        ↓ P0.6 audit / hardening findings
P0.7 dual-prompt hybrid proposal
        ↓ prompt-count pressure
P0.7 larger clusters (2×20 / 4×10)
        ↓ user proposes merged prompts
P0.7 single-prompt four-stage architecture
Terra Max → Sol Max → Terra XHigh → Sol XHigh
        ↓ memory idea explored, explicitly deferred
final jobbsøk_26_P0.7.md
        ↓
P0.7 implementation prompt
        ↓
P0.7 implemented release ZIP
        ↓
critical release audit
        ↓
USER OBJECTIVE CORRECTION:
maximize median + top-80 quality;
weak tail handled separately
        ↓
quality-first reinterpretation of P0.7
        ↓
from-scratch P0.8 redesign
        ↓
3 stages: Sol → Terra → Sol
        ↓ self-critique + web validation
5 coherent clusters × ~8 jobs
2 scripts
READY/CHECK/RERUN
partial-success rendering
        ↓
terminal request:
PLAN final exhaustive P0.8 specification, do not write yet
        ↓
[DOWNSTREAM / SIBLING EVIDENCE EXPECTED]
P0.8 FINAL_NORMATIVE_SPECIFICATION (~3800 lines, external anchor)
```

`[OPEN]` The external anchor dates both the implemented P0.7 current release and final P0.8 specification to 2026-08-04, while this integration session is on 2026-08-21. Given the project’s explicitly non-linear chat history, do not infer total chronological order from chat date alone.

---

# 3. Incoming state

## Confirmed

- `[CONFIRMED]` A P0.7 hybrid architecture already existed in an earlier two-prompt-per-stage form.
- `[CONFIRMED]` Four logical stages and physical stage/chat separation were already established.
- `[CONFIRMED]` P0.6 supplied a working manual/file-based implementation substrate.
- `[CONFIRMED]` Candidate truth was already split across `Work_experience.md`, `Education.md`, `Other_high_value_information.md`, with `CV_BASELINE.md` derived.
- `[CONFIRMED]` P0.6 had known hardening gaps: older-employment rendering, batch completeness, identity anchoring, side budgets, ingest/advance robustness, timeout, and CV layout balance.
- `[CONFIRMED]` MVP-KISS / human-effort-first philosophy was already active.
- `[CONFIRMED]` No automatic submission was allowed.

## Inferred

- `[INFERRED]` Operator burden and Codex/Work credit use had become important enough that the user wanted fewer prompts/chats without sacrificing output quality.
- `[INFERRED]` The later selective-quality objective had not yet been explicitly formulated.

## Unknown

- `[UNKNOWN]` Exact global chronology against sibling P0.8/P0.9 chats.
- `[UNKNOWN]` Actual visible title of this chat.

---

# 4. Evolution within this chat

| Stage | Earlier state | Trigger/new evidence | Change made | Resulting state | Status |
|---|---|---|---|---|---|
| Prompt-count optimization | Dual-prompt P0.7, 48 prompts / 24 chats under 10/5 topology | User asks if larger clusters can halve prompts | 2×20 main + 4×10 mini, lanes/waves | Same dual-pass logic, 24 prompts / 12 chats | `[SUPERSEDED]` |
| P0.6/P0.7 hybridization | Two prompts/two models inside each stage | User proposes merging prompts and using stronger single models | One prompt / one model per stage, internal Phase A/B | Terra Max → Sol Max → Terra XHigh → Sol XHigh, 12 chats | `[CONFIRMED then SUPERSEDED by P0.8]` |
| Memory/archetype idea | No persistent semantic cache | User proposes stable archetypes and must-load retrieval IDs | Layered memory design explored | User explicitly defers entire concept | `[REJECTED for MVP / DEFERRED]` |
| Final P0.7 architecture | Competing P0.7 variants | User asks for final complete MVP-KISS architecture | `jobbsøk_26_P0.7.md` generated | Four-stage single-prompt P0.7 | `[SUPERSEDED by P0.8]` |
| P0.7 implementation | Architecture exists; P0.6 code exists | User asks for migration prompt | `Jobbsok_26_P0.7_Implementation_Prompt.md` generated | P0.6→P0.7 implementation contract | `[COMPLETED]` |
| P0.7 release audit | Implemented release ZIP available | User asks deep critical review | Tests/render/adversarial audit | Strong implementation + concrete weaknesses | `[COMPLETED]` |
| Strict hardening orientation | Audit recommends P0.7.1 hardening | User says quality majority matters more than uniformity | Reorders priorities toward selective quality | Hard truth/integrity stays; uniformity QA demoted | `[SUPERSEDED]` |
| Quality-first P0.7 optimization | Four-stage P0.7 retained | User asks direct cross-reference | Freer final writer, headline, soft side budgets, partial success, READY/CHECK/RERUN | Transitional quality-first P0.7 | `[SUPERSEDED]` |
| First P0.8 redesign | P0.7 remains structurally complex | User asks from-scratch redesign, simpler | Three stages, one cluster type, two scripts | First P0.8 4×10 proposal | `[SUPERSEDED]` |
| P0.8 refinement | 3-stage 4×10 | User asks falsification + web validation | 5×~8, Priority A/B, minimal state, Sol/Terra/Sol | Final chat-supported P0.8 design | `[ACTIVE]` |
| P0.8 spec planning | Refined design exists | User asks to plan definitive detailed spec, not write | Planning task initiated | Spec not written in visible chat | `[IN PROGRESS at terminal point]` |

---

# 5. Decision ledger

| ID | Decision/constraint | Authority | Status | Scope | Evidence | Supersedes/superseded-by |
|---|---|---|---|---|---|---|
| D01 | Reduce operator burden by consolidating prompts where quality is preserved. | USER-EXPLICIT | ACTIVE PRINCIPLE | Global | Repeated prompt-count/complexity requests. | — |
| D02 | P0.7 may use 2×20 macro + 4×10 mini. | USER-ACCEPTED-PROPOSAL | SUPERSEDED | P0.7 | Adopted into final P0.7. | Superseded by P0.8 single cluster type. |
| D03 | P0.7 uses one prompt/model per stage with internal Phase A/B. | USER-ACCEPTED-PROPOSAL | SUPERSEDED AS VERSION-SPECIFIC | P0.7 | User proposed merging prompts. | P0.8 reduces to three stages. |
| D04 | P0.7 route Terra Max → Sol Max → Terra XHigh → Sol XHigh. | USER-ACCEPTED-PROPOSAL | SUPERSEDED | P0.7 | Final P0.7 design/release. | P0.8 Sol → Terra → Sol. |
| D05 | Archetype/retrieval/strategy memory deferred to “next overhaul”. | USER-CORRECTION | ACTIVE NON-GOAL | MVP | Explicit user deferral. | — |
| D06 | Preserve MVP-KISS. | USER-EXPLICIT | ACTIVE | Global | Repeated. | — |
| D07 | P0.6 working code should be migrated surgically for P0.7. | USER-ACCEPTED-PROPOSAL | HISTORICAL/COMPLETED | P0.7 | Implementation prompt. | P0.8 later rebuilt from scratch but reuses strong parts. |
| D08 | P0.7 release is strong but not production-proven. | ASSISTANT-HIGH-CONFIDENCE | ACTIVE HISTORICAL FACT | P0.7 | Release audit. | — |
| D09 | Optimization objective is strong-majority quality, not uniform quality. | USER-CORRECTION | ACTIVE — HIGHEST PRIORITY | P0.8/global | Explicit Q-happy correction. | Supersedes prior reliability bias. |
| D10 | ~75% top-quality automation already creates enormous value. | USER-EXPLICIT | ACTIVE DESIGN INTENT | P0.8 | User statement. | — |
| D11 | Weak-tail packages may receive separate manual/extra round outside framework. | USER-EXPLICIT | ACTIVE | Human review | User correction. | Supersedes automatic tail rescue. |
| D12 | Hard QA focuses on cheap truth/mechanical integrity, not uniform semantic quality. | USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 QA | Quality-first discussion. | Supersedes strict P0.7.1 priority. |
| D13 | Final stage may overrule earlier strategy when truth remains intact. | USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 Stage 3 | Accepted redesign. | Supersedes P0.7 strategy lock. |
| D14 | P0.8 should be redesigned from scratch, reusing only strong naturally compatible prior components. | USER-EXPLICIT | ACTIVE | P0.8 | Explicit redesign request. | Supersedes “patch P0.7” framing. |
| D15 | P0.8 should if anything be less complex than P0.7. | USER-EXPLICIT | ACTIVE | P0.8 | Explicit. | — |
| D16 | P0.8 has three stages. | USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 | User acceptance after refined proposal. | Supersedes four-stage P0.7. |
| D17 | Stage 1 = GPT-5.6 Sol Max, Decision Architecture. | USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 | Final refined flow. | Supersedes separate Terra vacancy + Sol strategy stages. |
| D18 | Stage 2 = GPT-5.6 Terra Max, Native Package Writer. | USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 | Final refined flow. | Supersedes Terra XHigh default. |
| D19 | Stage 3 = GPT-5.6 Sol Max for MVP pilot; later A/B against XHigh. | USER-ACCEPTED-PROPOSAL | ACTIVE/EMPIRICALLY REVISABLE | P0.8 | Final refined flow. | Supersedes P0.7 Sol XHigh default. |
| D20 | Standard topology = five coherent clusters of ~8, normal range 6–10. | USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 | Final refined flow. | Supersedes 4×10 P0.8 draft and P0.7 topology. |
| D21 | Normal production = 15 core stage chats/prompts for 40 jobs. | USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 | 5 clusters × 3 stages. | Supersedes P0.7 12-prompt architecture. |
| D22 | Optional preflight may use Terra XHigh, but is not a core stage. | ASSISTANT-PROPOSAL / BROADLY ACCEPTED | PROVISIONAL | P0.8 intake | Final refined proposal. | May be omitted later. |
| D23 | Only two active scripts: `ingest.py`, `finalize.py`; no `advance.ps1`. | USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 runtime | Final refined flow + external anchor. | Supersedes P0.7 three scripts. |
| D24 | No macro/minicluster hierarchy; one coherent cluster follows all stages. | USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 | Final redesign. | Supersedes evidence-lane/split machinery. |
| D25 | No `MINICLUSTER_SPLIT.json`, evidence lanes, or Stage-transition copy script. | USER-ACCEPTED-PROPOSAL | ACTIVE | P0.8 | Final redesign. | Supersedes P0.7 transition architecture. |
| D26 | Stage 1 contains internal candidate-blind Phase A then candidate-aware Phase B. | USER-ACCEPTED-PROPOSAL | ACTIVE | Stage 1 | Preserves strongest P0.7 separation rationale. | — |
| D27 | Stage 1 outputs compact strategy, not exhaustive cluster evidence infrastructure. | USER-ACCEPTED-PROPOSAL | ACTIVE | Stage 1 | Final refined design. | Supersedes `CLUSTER_EVIDENCE_BASE.md`. |
| D28 | Use Priority A/B, not PRIME/STANDARD/MANUAL_LATER as automatic model router. | USER-ACCEPTED-PROPOSAL | ACTIVE | Ordering | Final self-critique. | Supersedes earlier classification. |
| D29 | Priority A jobs first; Priority B later, but all receive packages. | USER-ACCEPTED-PROPOSAL | ACTIVE | Stage ordering | Final refined flow. | — |
| D30 | Internal micro-variation only for high-impact fields on Priority A; no full best-of-N packages. | USER-ACCEPTED-PROPOSAL | ACTIVE/LIMITED | Stage 2 | Final refined flow. | — |
| D31 | Add explicit CV `headline`. | USER-ACCEPTED-PROPOSAL | ACTIVE | Schema/rendering | Repeated accepted recommendation. | Supersedes competency-concatenation headline. |
| D32 | Review = READY/CHECK/RERUN, max three concrete reasons, no confidence score. | USER-ACCEPTED-PROPOSAL | ACTIVE | Stage 3/human review | Final refined design. | Supersedes P0.7 review headings and intermediate confidence idea. |
| D33 | Finalizer preserves partial success. | USER-ACCEPTED-PROPOSAL | ACTIVE | Rendering | Final P0.8 design. | Supersedes global batch-completeness orientation. |
| D34 | Page budgets become soft review triggers. | USER-ACCEPTED-PROPOSAL | ACTIVE | Rendering/QA | Quality-first redesign. | Supersedes hard P0.7 side gate. |
| D35 | Finalizer supports targeted `--job` rerender. | USER-ACCEPTED-PROPOSAL | ACTIVE | Operator workflow | Final P0.8 design. | — |
| D36 | Runtime state is minimal: artifact presence + simple `progress.json`; no elaborate `_DONE.md`/BATCH_STATUS. | USER-ACCEPTED-PROPOSAL | ACTIVE | State | Final refined design. | Supersedes P0.7 status complexity. |
| D37 | No automatic employer research in MVP. | USER-ACCEPTED-PROPOSAL / PRIOR CONSTRAINT | ACTIVE | P0.8 | Repeated non-goal. | — |
| D38 | No LLM judge, automatic retries, vector DB, multi-agent, memory/cache, auto submission. | USER-EXPLICIT / USER-ACCEPTED-PROPOSAL | ACTIVE | Non-goals | Repeated. | — |
| D39 | Next task in this chat was to plan, not write, the exhaustive final P0.8 spec. | USER-EXPLICIT | ACTIVE TERMINAL PLAN | Documentation | Final substantive user request. | Downstream final spec expected. |

---

# 6. Requirements and constraints

## Explicit-active

- `[CONFIRMED]` Maximize median package quality + top-80%-mean quality.
- `[CONFIRMED]` Human effort is the dominant cost.
- `[CONFIRMED]` Human complexity is more costly than LLM complexity.
- `[CONFIRMED]` MVP-KISS: remove infrastructure without direct quality/labor value.
- `[CONFIRMED]` Every approved job still gets a complete package where mechanically possible.
- `[CONFIRMED]` Weak tail is triaged, not automatically excluded or endlessly repaired.
- `[CONFIRMED]` No automatic submission/contact.
- `[CONFIRMED]` Candidate truth only from three authority files; `CV_BASELINE.md` derived.
- `[CONFIRMED]` Strong synthesis/functional equivalence allowed; formal facts must not be invented.
- `[CONFIRMED]` Natural Norwegian Bokmål.
- `[CONFIRMED]` CV/application/portal should be complementary.
- `[CONFIRMED]` Preserve strong Word masters where useful.
- `[CONFIRMED]` Manual final semantic approval.
- `[CONFIRMED]` No model runner/API orchestration.
- `[CONFIRMED]` No memory/cache/vector/multi-agent/auto-router/LLM-judge/retry loop/full best-of-N/auto research/submission.

## Inferred

- `[INFERRED]` File-based inspectability and local recovery remain preferred.
- `[INFERRED]` Credit cost matters only after human workload and package quality.
- `[INFERRED]` The architecture should tolerate a minority of weak packages without poisoning throughput.

## Superseded

- `[SUPERSEDED]` Uniform hard semantic/QA gating across all packages.
- `[SUPERSEDED]` Global PASS as main success metric.
- `[SUPERSEDED]` Final stage may not introduce new valid baseline-backed evidence.
- `[SUPERSEDED]` Hard CV/application page budgets as non-delivery conditions.
- `[SUPERSEDED]` Separate candidate-blind Stage 1 and strategy Stage 2.
- `[SUPERSEDED]` 2×20 macro + 4×10 mini topology for P0.8.

## Unresolved

- `[OPEN]` Stage 3 Sol Max vs XHigh after pilot.
- `[OPEN]` Stage 2 Terra Max vs XHigh after pilot.
- `[OPEN]` Empirically optimal cluster size within 6–10.
- `[OPEN]` Whether optional preflight belongs in final normative MVP.

---

# 7. Artifact and source inventory

| Artifact/file | Type | Role | Version | State at end | Authority/source | Notes |
|---|---|---|---|---|---|---|
| `Work_experience.md` | Candidate authority | Work truth | Canonical | `[CONFIRMED] Existing` | Candidate truth | Immutable. |
| `Education.md` | Candidate authority | Education truth | Canonical | `[CONFIRMED] Existing` | Candidate truth | Immutable. |
| `Other_high_value_information.md` | Candidate authority | Other truth | Canonical | `[CONFIRMED] Existing` | Candidate truth | Immutable. |
| `CV_BASELINE.md` | Derived baseline | Static CV chronology/rendering | Derived | `[CONFIRMED] Existing` | Derived from truth | Never creates facts. |
| `CV_MASTER.docx` | Word master | CV rendering | Existing | `[CONFIRMED] Existing/audited` | Original asset | Reuse; rebalance layout. |
| `APPLICATION_MASTER.docx` | Word master | Letter rendering | Existing | `[CONFIRMED] Existing/audited` | Original asset | Reuse. |
| `Final_Jobbsok_26_P0.7_Hybrid_Multi-Model_Dual-Prompt_Architecture.md` | Architecture | Earlier dual-pass P0.7 | Intermediate | `[SUPERSEDED]` | Assistant artifact | Chronology marker. |
| `jobbsøk_26_P0.7.md` | Architecture | Final P0.7 spec | P0.7 | `[CONFIRMED] Generated` | User-requested assistant artifact | 3,134 lines / 9,480 words. |
| `Jobbsok_26_P0.7_Implementation_Prompt.md` | Prompt | P0.6→P0.7 migration | P0.7 | `[CONFIRMED] Generated` | User-requested artifact | 411 lines. |
| `Jobbsok_26_P0.7_Release.zip` | Release | Implemented P0.7 | P0.7 | `[CONFIRMED] Uploaded/audited` | User-provided | 52 files; 32/34. |
| P0.7 root `AGENTS.md` | Runtime instruction | Universal boundaries | P0.7 | `[VERIFIED]` | Uploaded release | Max interview probability, truth/no-submit, Phase A/B. |
| P0.7 `MODEL_ROUTING.md` | Routing | Model/effort | P0.7 | `[VERIFIED]` | Uploaded release | Terra/Sol/Terra/Sol. |
| P0.7 `START_HERE.md` | Operator guide | Topology/commands | P0.7 | `[VERIFIED]` | Uploaded release | 2×20/4×10, 12 chats. |
| `Jobbsok_26_P0.7_Critical_Audit_and_Perfection_Recipe.md` | Audit | Release review | P0.7 | `[CONFIRMED] Generated` | Assistant audit | Strict QA priority later partly superseded. |
| `strategy.md` | Planned artifact | Per-job Decision Architecture | P0.8 | `[PLANNED]` | Refined design | Replaces separate vacancy analysis + heavy blueprint/evidence base. |
| `cluster_plan.json` | Planned artifact | Cluster order/Priority | P0.8 | `[PLANNED]` | Refined design | Exact schema pending. |
| `cluster_notes.md` | Planned artifact | Minimal cross-job notes | P0.8 | `[PLANNED]` | Refined design | Compact only. |
| `progress.json` | Planned artifact | Minimal state | P0.8 | `[PLANNED]` | Refined design | Replaces `_DONE.md`/BATCH_STATUS. |
| `draft_package.json` | Planned artifact | Stage-2 package | P0.8 | `[PLANNED]` | Refined design | Terra Max output. |
| `final_package.json` | Planned artifact | Final package | P0.8 | `[PLANNED]` | Refined design | Sol Max authority. |
| `review.json` | Planned artifact | READY/CHECK/RERUN | P0.8 | `[PLANNED]` | Refined design | Max 3 reasons; no confidence. |
| `REVIEW_QUEUE.md` | Planned finalizer output | Human queue | P0.8 | `[PLANNED]` | Refined design | READY/CHECK/RERUN/FAILED. |
| `package.schema.json` | Schema | Package contract | P0.7→P0.8 | `[DECIDED, NOT IMPLEMENTED]` | P0.8 | Add headline. |
| `identity.schema.json` | Schema | Identity integrity | P0.8 | `[DECIDED, NOT IMPLEMENTED]` | Adapt P0.7 | Exact filename may vary. |
| `review.schema.json` | Schema | Review status | P0.8 | `[PLANNED]` | P0.8 | Enum + reasons. |
| `WRITING_STANDARD.md` | Context | Norwegian writing guidance | P0.8 | `[PLANNED / naming open]` | P0.8 | Consolidation candidate. |
| `PERSUASION_CALIBRATION.md` | Context | Human-confirmed calibration | Existing/adapted | `[CONFIRMED concept]` | Prior P0.7 | No automatic learning. |
| `ingest.py` | Script | Intake/run setup | P0.8 | `[DECIDED, NOT IMPLEMENTED]` | Adapt P0.7 | Active script 1. |
| `finalize.py` | Script | Hard validation/render/review queue/partial success | P0.8 | `[DECIDED, NOT IMPLEMENTED]` | Adapt P0.7 | Active script 2. |
| `advance.ps1` | Script | P0.7 transition | P0.7 | `[REJECTED for P0.8]` | P0.7 | Removed. |
| `Jobbsøk_26_P0.8: arkitektur, innhold, struktur, design og detaljert filindeks med utvidete innholdsbeskrivelser.md` | Intended normative doc | Exhaustive P0.8 spec | P0.8 | `[REQUESTED TO PLAN; NOT WRITTEN HERE]` | User terminal request | Strong chronology hook. |
| P0.8 `FINAL_NORMATIVE_SPECIFICATION` (~3800 lines) | External anchor artifact | Superseding final spec | P0.8 | `[CONFIRMED BY ANCHOR; NOT CREATED IN VISIBLE CHAT]` | External baseline | Likely downstream sibling/later output. |

---

# 8. Research and external findings

| Finding | Implication | Source/provenance | Confidence | Later challenged? |
|---|---|---|---|---|
| GPT-5.6 context/output capacity is large; output limit is not the main reason for 5-job batches. | Allowed larger-cluster exploration. | OpenAI model docs cited in chat. | HIGH | No; quality concerns later drive smaller clusters. |
| Terra costs roughly half Sol; Luna roughly one-fifth Sol under cited Codex rates. | Supported Terra for output-heavy Writer stage. | OpenAI Codex rate-card citations. | HIGH | No; cost becomes secondary to quality. |
| Long-context models can underuse information by position (“Lost in the Middle”). | Supports ~8-job P0.8 clusters rather than maximizing context size. | Research cited in final redesign. | HIGH | No. |
| Self-refinement improves outputs without separate model/stage. | Supports internal Phase A→B instead of dual-pass. | Self-Refine citation. | HIGH | No. |
| Selective prediction / learning-to-defer improves covered-subset quality. | Directly supports Q-happy and READY/CHECK/RERUN. | SelectiveNet / learning-to-defer citations. | HIGH | No. |
| Routing by expected marginal gain is more useful than generic difficulty. | Led to rejecting complicated automatic quality router. | Routing research cited. | MEDIUM-HIGH | Refined, not rejected. |
| LLM confidence is hard to calibrate. | Confidence field removed from review output. | Calibration research cited. | HIGH | No. |
| Context-specific expert evals are more useful than generic benchmarks/automatic graders alone. | P0.8 evals use real packages, edit minutes, Q-happy; no LLM judge. | OpenAI GDPval/eval guidance. | HIGH | No. |
| Full best-of-N can game imperfect graders and adds human selection cost. | Full-package best-of-N remains non-goal; only micro-variation retained. | Inference-time alignment research. | MEDIUM-HIGH | No. |
| More reasoning effort is not automatically better for every task. | Sol/Terra Max are pilot defaults subject to local A/B. | OpenAI effort/eval guidance. | HIGH | No. |

`[CONFIRMED]` Original web URLs are not present in the visible chat text available to this integration pass; source names/citation provenance are preserved without inventing URLs.

---

# 9. Implementation state at end of chat

## Implemented/completed

- `[CONFIRMED]` P0.7 full architecture document.
- `[CONFIRMED]` P0.7 implementation prompt.
- `[CONFIRMED]` P0.7 release.
- `[CONFIRMED]` P0.7 critical audit report.
- `[CONFIRMED]` P0.7 scripts/schemas/templates/instructions/tests.

## Verified

- `[CONFIRMED]` 32/34 P0.7 automated tests passed.
- `[CONFIRMED]` 2 blocked because PowerShell unavailable.
- `[CONFIRMED]` DOCX/PDF rendering exercised.
- `[CONFIRMED]` Older-employment override rendering works.
- `[CONFIRMED]` Unit/reference rendering works.
- `[CONFIRMED]` ZIP integrity/file count checked.
- `[CONFIRMED]` Stage-4 draft-reference bypass reproduced.
- `[CONFIRMED]` Weak textual review/done parsing reproduced.
- `[CONFIRMED]` CV page balance visually weak.

## Decided but not implemented

- `[CONFIRMED]` P0.8 three-stage architecture.
- `[CONFIRMED]` 5×~8 clusters, range 6–10.
- `[CONFIRMED]` Sol Max → Terra Max → Sol Max.
- `[CONFIRMED]` Two-script runtime.
- `[CONFIRMED]` `advance.ps1` removal.
- `[CONFIRMED]` compact `strategy.md`.
- `[CONFIRMED]` explicit CV headline.
- `[CONFIRMED]` simple `progress.json`.
- `[CONFIRMED]` `review.json`.
- `[CONFIRMED]` partial-success finalizer and `--job`.
- `[CONFIRMED]` soft page-budget handling.
- `[CONFIRMED]` truth-bounded Stage-3 strategic authority.

## In progress

- `[CONFIRMED]` Planning the definitive exhaustive P0.8 normative architecture/file-index document.
- `[CONFIRMED]` User explicitly instructed not to write it yet.

## Planned

- `[CONFIRMED]` P0.8 repository implementation after final spec.
- `[CONFIRMED]` First real ~8-job pilot.
- `[CONFIRMED]` A/B tests for model effort and possibly cluster size.
- `[CONFIRMED]` Q-happy / submit-ready / edit-minutes evaluation.

## Blocked

- `[CONFIRMED]` P0.7 PowerShell runtime tests in audit environment.
- `[INFERRED]` This block is less relevant to P0.8 because `advance.ps1` is removed.

## Unknown

- `[CONFIRMED]` No real P0.7 Terra/Sol production run occurred by audit point.
- `[CONFIRMED]` No real P0.7 vacancy pilot occurred.
- `[CONFIRMED FROM ANCHOR]` P0.8 is not implemented.
- `[UNKNOWN]` Exact final P0.8 field-level spec within visible chat.

---

# 10. Plan/strategy at end of chat

## Next objective

- `[CONFIRMED]` Do **not** implement immediately.
- `[CONFIRMED]` Plan the definitive file `Jobbsøk_26_P0.8: arkitektur, innhold, struktur, design og detaljert filindeks med utvidete innholdsbeskrivelser.md`.
- `[CONFIRMED]` It must define architecture, content, structure, design, detailed file index, extended file descriptions, and every object required before first run.
- `[CONFIRMED]` The planning should be from scratch and optimized for logical implementability.

## Likely implementation sequence after final spec

- `[INFERRED]` Freeze candidate authorities and masters.
- `[INFERRED]` Reuse only P0.7 assets directly compatible with P0.8.
- `[INFERRED]` Create simplified repo.
- `[INFERRED]` Consolidate instructions.
- `[INFERRED]` Revise package/identity/review schemas.
- `[INFERRED]` Adapt `ingest.py`.
- `[INFERRED]` Remove `advance.ps1`.
- `[INFERRED]` Refactor `finalize.py`.
- `[INFERRED]` Implement simple progress state.
- `[INFERRED]` Build fixtures.
- `[CONFIRMED]` Run one real ~8-job cluster.
- `[CONFIRMED]` Measure Q-happy, submit-ready, edit minutes, tail recall/review load, credits.
- `[CONFIRMED]` A/B one variable at a time.

## Model roles

- `[CONFIRMED]` Stage 1 Sol Max.
- `[CONFIRMED]` Stage 2 Terra Max.
- `[CONFIRMED]` Stage 3 Sol Max.
- `[PROVISIONAL]` Optional Terra XHigh preflight.
- `[CONFIRMED]` No runner/subagent/API model orchestration.

## Validation strategy

- `[CONFIRMED]` Hard: identity, unsupported formal facts, unknown employment IDs, baseline merge failure, required channel absence, internal leakage, unrenderable documents.
- `[CONFIRMED]` Soft: page count, genericity, strategy weakness, similarity, rewrite size, review status.
- `[CONFIRMED]` Preserve partial success.

## Acceptance

- `[CONFIRMED]` Q-happy primary metric.
- `[CONFIRMED]` Supporting metrics: median, top-80 mean, submit-ready, edit minutes, TailRecall20/review load, credits.
- `[OPEN]` No exact numeric release threshold fixed in visible chat.

---

# 11. Best-supported P0.8 reconstruction

## 11.1 Purpose & success criteria

- `[CONFIRMED]` Maximize quality of the large majority of packages, not minimum-tail quality.
- `[CONFIRMED]` `Q_happy = avg(median(q), mean(top80%(q)))`.
- `[CONFIRMED]` Bottom-tail cases may receive separate rerun/manual round.
- `[CONFIRMED]` Secondary: submit-ready share, human edit minutes, tail identification, credits.
- Anchor: **CONFIRMS**.

## 11.2 Scope

- `[CONFIRMED]` ~40 approved jobs.
- `[CONFIRMED]` 5 strategically coherent clusters, typically ~8, normal 6–10.
- `[CONFIRMED]` 3 manual model stages per cluster = 15 core chats.
- `[CONFIRMED]` Optional preflight is not core stage.
- Anchor: **CONFIRMS**.

## 11.3 Explicit non-goals

- `[CONFIRMED]` memory/cache, vector DB, multi-agent, auto router, full best-of-N, LLM judge, auto retries, auto research, auto submission, heavy orchestration.
- Anchor: **CONFIRMS**.

## 11.4 Core architectural principles

- `[CONFIRMED]` Decide → write → finalize.
- `[CONFIRMED]` One coherent cluster through all stages.
- `[CONFIRMED]` One job completely before next.
- `[CONFIRMED]` Internal Phase A/B refinement.
- `[CONFIRMED]` Truth hard; strategy soft.
- `[CONFIRMED]` Do not weaken strong packages for uniformity.
- `[CONFIRMED]` Partial success and selective human review.
- Anchor: **CONFIRMS**.

## 11.5 Canonical source-of-truth model

- `[CONFIRMED]` `Work_experience.md`, `Education.md`, `Other_high_value_information.md` own facts.
- `[CONFIRMED]` `CV_BASELINE.md` is derived.
- `[CONFIRMED]` Vacancy owns employer/job requirements.
- `[CONFIRMED]` Stage artifacts are not candidate-truth authorities.
- Anchor: **CONFIRMS**.

## 11.6 Candidate/source files & schemas

- `[CONFIRMED]` Three candidate authorities, baseline, Word masters.
- `[PROPOSED/LIKELY ACTIVE]` consolidated `WRITING_STANDARD.md`.
- `[CONFIRMED CONCEPT]` `PERSUASION_CALIBRATION.md`.
- `[CONFIRMED]` package schema revised for `headline`.
- `[CONFIRMED]` identity schema retained.
- `[CONFIRMED]` review schema = READY/CHECK/RERUN + max 3 reasons.
- `[OPEN]` exact field-level schema pending final spec.
- Anchor: **EXTENDS**.

## 11.7 Context assembly/retrieval

- `[CONFIRMED]` Stage 1 Sol Max owns broad retrieval.
- `[CONFIRMED]` Phase A candidate-blind employer model; Phase B candidate-aware strategy.
- `[CONFIRMED]` Compact selected evidence, not huge evidence base.
- `[CONFIRMED]` Preserve source file/heading, fact, contribution, lifecycle, safe formulation, decision-test relevance.
- `[CONFIRMED]` Later stages do targeted source rereads only.
- `[CONFIRMED]` No persistent semantic memory.
- Anchor: **EXTENDS**.

## 11.8 Research/external-info strategy

- `[CONFIRMED]` No automatic employer/web research in normal pipeline.
- `[CONFIRMED]` Vacancy/supplied metadata are default employer evidence.
- `[CONFIRMED]` Volatile model/pricing facts can be reverified before batch without changing architecture.
- `[OPEN]` Exact manual research exception path not specified.
- Anchor: **CONFIRMS / EXTENDS**.

## 11.9 Vacancy intake

- `[CONFIRMED]` `ingest.py` normalizes/validates vacancy/input/run structure.
- `[CONFIRMED]` Mechanical unusability only; no semantic GO/NO-GO.
- `[PROVISIONAL]` Optional Terra-XHigh clustering preflight.
- `[OPEN]` exact normalized vacancy format pending final spec.
- Anchor: **EXTENDS**.

## 11.10 Fit analysis/positioning

- `[CONFIRMED]` No fit veto or numeric fit score.
- `[CONFIRMED]` Stage 1 chooses employer problem, decision tests, selection regime, identity, shortlist thesis, evidence pair, alternative route, objection/reframe, motivation bridge, channel allocation.
- `[CONFIRMED]` Priority A/B controls ordering/attention, not automatic routing.
- Anchor: **EXTENDS**.

## 11.11 CV tailoring

- `[CONFIRMED]` Complete chronology from baseline.
- `[CONFIRMED]` Dynamic headline/profile/competencies/employment overrides.
- `[CONFIRMED]` Explicit headline separate from competency list.
- `[CONFIRMED]` Final stage may rewrite identity/headline/evidence if truth-supported.
- `[CONFIRMED]` 1–2 pages is target, not destructive hard gate.
- `[CONFIRMED]` P0.7 layout balance should be improved.
- Anchor: **EXTENDS**.

## 11.12 Application-letter generation

- `[CONFIRMED]` Terra Max writes complete natural-Bokmål letter.
- `[CONFIRMED]` Employer-specific opening, complementary evidence, causal motivation, interview hook.
- `[CONFIRMED]` Sol Max can fully rewrite.
- `[CONFIRMED]` ~1 page target, soft gate.
- `[CONFIRMED]` Avoid employer-swappable prose without forcing artificial variation.
- Anchor: **EXTENDS**.

## 11.13 Portal/form answers

- `[CONFIRMED]` Portal answers remain package fields when required.
- `[CONFIRMED]` Direct exact answer and word/char limits.
- `[CONFIRMED]` Complementary to CV/letter.
- `[CONFIRMED]` Duplicate portal IDs are a cheap validation candidate.
- `[OPEN]` exact schema pending.
- Anchor: **EXTENDS**.

## 11.14 Document/template/rendering architecture

- `[CONFIRMED]` Reuse original masters.
- `[CONFIRMED]` `finalize.py` merges baseline + final package and renders DOCX/PDF.
- `[CONFIRMED]` Partial success.
- `[CONFIRMED]` `--job` rerender.
- `[CONFIRMED]` `REVIEW_QUEUE.md`.
- `[CONFIRMED]` Outcomes conceptually: DELIVERED_READY / DELIVERED_CHECK / DELIVERED_RERUN / FAILED.
- `[CONFIRMED]` Page overflow = review signal, not deletion.
- Anchor: **CONFIRMS + EXTENDS**.

## 11.15 QA/validation/provenance

### Hard
- `[CONFIRMED]` identity;
- `[CONFIRMED]` known employment IDs;
- `[CONFIRMED]` supported formal facts;
- `[CONFIRMED]` baseline merge/completeness;
- `[CONFIRMED]` required channel existence;
- `[CONFIRMED]` no internal/private leakage;
- `[CONFIRMED]` renderability.

### Soft
- `[CONFIRMED]` page count;
- `[CONFIRMED]` genericity;
- `[CONFIRMED]` strategy weakness;
- `[CONFIRMED]` large rewrite;
- `[CONFIRMED]` cross-job similarity;
- `[CONFIRMED]` weak motivation.

- `[CONFIRMED]` No full provenance engine.
- `[CONFIRMED]` Source references retained enough to verify selected evidence.
- `[CONFIRMED]` No LLM judge.
- Anchor: **CONFIRMS**.

## 11.16 Human review/approval

- `[CONFIRMED]` READY = rapid skim.
- `[CONFIRMED]` CHECK = focused local review.
- `[CONFIRMED]` RERUN = separate improvement round.
- `[CONFIRMED]` No automatic rerun.
- `[CONFIRMED]` Final semantic approval/manual submission remains human.
- Anchor: **CONFIRMS**.

## 11.17 Package/deliverable structure

- `[CONFIRMED]` Per job: identity, strategy, draft, final, review, rendered docs.
- `[CONFIRMED]` Per cluster: cluster plan/notes, progress, rendered outputs/review queue.
- `[OPEN]` exact directory naming pending final spec.
- Anchor: **EXTENDS**.

## 11.18 Versioning/state management

- `[CONFIRMED]` Remove elaborate `_DONE.md` / BATCH_STATUS.
- `[CONFIRMED]` Minimal `progress.json` + artifact presence.
- `[CONFIRMED]` Candidate authorities/masters immutable.
- `[INFERRED]` Run folders isolated by batch/cluster/job.
- `[OPEN]` exact version/hash manifest policy pending.
- Anchor: **EXTENDS**.

## 11.19 Automation/model/tool responsibilities

- `[CONFIRMED]` Stage 1 Sol Max.
- `[CONFIRMED]` Stage 2 Terra Max.
- `[CONFIRMED]` Stage 3 Sol Max.
- `[PROVISIONAL]` optional Terra XHigh preflight.
- `[CONFIRMED]` `ingest.py`, `finalize.py`.
- `[CONFIRMED]` no `advance.ps1`.
- `[CONFIRMED]` no API runner/agent system.
- Anchor: **CONFIRMS**.

## 11.20 Implementation sequence

- `[CONFIRMED]` Complete final normative spec before implementation.
- `[INFERRED]` Freeze/reuse candidate authorities and masters.
- `[INFERRED]` Extract only compatible P0.7 code/assets.
- `[INFERRED]` Build simplified repo/instructions/schemas.
- `[INFERRED]` Refactor ingest/finalizer.
- `[INFERRED]` Add fixtures/render checks.
- `[CONFIRMED]` Run one real ~8-job cluster.
- `[CONFIRMED]` A/B one variable at a time.
- Anchor: **EXTENDS**.

## 11.21 Acceptance criteria

- `[CONFIRMED]` Q-happy primary.
- `[CONFIRMED]` median quality, top-80 mean, submit-ready rate, edit minutes, TailRecall20, review load, credits per ready package.
- `[CONFIRMED]` Truth/integrity failures remain unacceptable.
- `[OPEN]` no numeric production threshold fixed here.
- Anchor: **EXTENDS**.

## 11.22 Known risks/open design questions

- `[OPEN]` exact cluster composition / empirical optimal size;
- `[OPEN]` Sol Max vs XHigh Stage 3;
- `[OPEN]` Terra Max vs XHigh Stage 2;
- `[OPEN]` optional preflight inclusion;
- `[OPEN]` exact strategy/cluster/review/package schema definitions;
- `[OPEN]` exact final repository tree;
- `[OPEN]` review-reason code list;
- `[OPEN]` template/layout changes for sparse/dense CV;
- `[OPEN]` Q-happy scoring rubric and acceptance threshold;
- `[OPEN]` whether downstream final spec resolves all of these.
- Anchor: **EXTENDS**.

---

# 12. Later-than-P0.8 evidence

| Later change/finding | Version/phase | Difference from P0.8 | Supersedes P0.8? | Backportable? | Confidence |
|---|---|---|---|---|---|
| No explicit P0.9+ implementation/design decision is present in the visible substantive chat reconstructed here. | — | — | No | — | HIGH |
| `[UNKNOWN]` Project-level sibling chats may contain later-looking work, but this summary does not import it without evidence. | Potential sibling work | Not safe to merge | No | Reconciliation model must compare sibling summaries | HIGH |

---

# 13. Open questions, contradictions, reconciliation hazards

| Issue | Competing interpretations | Best current interpretation | Evidence needed |
|---|---|---|---|
| P0.8 final spec exists externally vs this chat ends before writing it | Anchor says final ~3800-line spec exists; visible chat only plans it | `[INFERRED]` Finished spec is downstream/sibling/later continuation | Find chat/artifact that creates final spec |
| Audit date 2026-08-03 vs P0.7 release anchor 2026-08-04 | Pre-final audit, timezone/date typo, or next-day finalization | Treat 2026-08-04 as global current-release date; preserve report date | Compare ZIP hash/manifest |
| First P0.8 4×10 vs refined 5×~8 | Both appear | `[CONFIRMED]` 4×10 superseded; 5×~8 is later accepted | Final P0.8 spec |
| PRIME/STANDARD/MANUAL_LATER vs Priority A/B | Earlier brainstorming vs final simplification | `[CONFIRMED]` Priority A/B is later accepted | Final P0.8 spec |
| Stage-3 Sol Max vs XHigh | P0.8 pilot uses Max, later A/B possible | `[CONFIRMED]` Max pilot default, empirically revisable | Real pilot |
| Hard page budget | P0.7 hard-fails; P0.8 softens | `[CONFIRMED]` Soft review in P0.8 | Final spec |
| No-new-employment-ID | P0.7 integrity rule vs P0.8 final-writer freedom | `[CONFIRMED]` P0.8 may use any truth-backed valid baseline employment route | Final spec |
| Strict `_DONE.md` parser | P0.7 audit recommendation vs P0.8 removing `_DONE.md` | `[CONFIRMED]` Not a P0.8 priority | P0.8 repo |
| Optional preflight | Included as optional assistant proposal | `[OPEN]` May be dropped | Final spec |
| Exact chat title | Not exposed | `[UNKNOWN]` | External metadata |

---

# 14. Inter-chat reconciliation hooks

1. `[CONFIRMED]` A chat containing the completed ~3800-line P0.8 final spec is likely downstream of this chat’s final planning request.
2. `[CONFIRMED]` Four-stage 2×20/4×10 Terra→Sol→Terra→Sol summaries are P0.7-era and upstream of P0.8 redesign.
3. `[CONFIRMED]` Dual-prompt P0.7 summaries are earlier still.
4. `[CONFIRMED]` `jobbsøk_26_P0.7.md` → implementation prompt → release ZIP → audit → Q-happy correction is a strong ordering chain.
5. `[CONFIRMED]` P0.7 release facts to cross-check: 52 files; 32/34 tests; two PowerShell-blocked; no real model/vacancy pilot.
6. `[CONFIRMED]` A summary presenting strict P0.7.1 hardening as current is stale unless it includes the later quality-priority correction.
7. `[CONFIRMED]` P0.8 4×10 is stale; 5×~8 is later.
8. `[CONFIRMED]` PRIME/STANDARD/MANUAL_LATER automatic routing is stale; Priority A/B is later.
9. `[CONFIRMED]` P0.8 intentionally removes `advance.ps1`, evidence lanes, macro/minicluster split, per-job `_DONE.md`, and global batch-PASS.
10. `[CONFIRMED]` P0.8 stage order is Sol Max Decision Architecture → Terra Max Native Package Writer → Sol Max Final Writer & Selective Review.
11. `[CONFIRMED]` Stage-3 strategy lock claims are P0.7 logic and superseded.
12. `[CONFIRMED]` Any sibling chat with exact P0.8 schemas/tree is likely downstream from this chat’s terminal planning point.
13. `[CONFIRMED]` P0.9+ evidence must remain outside §11 unless independently established.

---

# 15. Appendix — residual signal

## Quantitative/topology clues

- `[CONFIRMED]` P0.7 final: 2 macroclusters × ~20, 4 miniclusters × ~10, 12 prompts.
- `[CONFIRMED]` P0.8 final chat design: 5 clusters × ~8, range 6–10, 15 prompts.
- `[CONFIRMED]` User says ~75% top-quality package automation is already enormously valuable.
- `[CONFIRMED]` Q-happy combines median with mean of the strongest 80%.

## Model-route clues

- `[SUPERSEDED]` dual-pass P0.7 used mixed Luna/Terra/Sol combinations.
- `[SUPERSEDED]` final P0.7: Terra Max → Sol Max → Terra XHigh → Sol XHigh.
- `[ACTIVE P0.8]` Sol Max → Terra Max → Sol Max.
- `[PROVISIONAL]` Sol XHigh Stage 3 A/B after pilot.
- `[PROVISIONAL]` optional Terra XHigh preflight.

## Quality-policy clues

- `[CONFIRMED]` Strong packages must not be weakened for uniformity.
- `[CONFIRMED]` Hard block only for factual/mechanical unusability, not genericity/strategic imperfection.
- `[CONFIRMED]` READY/CHECK/RERUN is a review queue, not semantic veto.
- `[CONFIRMED]` RERUN is outside normal automated flow.

## Rejected/deferred alternatives

- `[REJECTED/DEFERRED]` archetype memory / stable retrieval cache / strategy-prior memory;
- `[REJECTED]` vector DB;
- `[REJECTED]` multi-agent/fan-out;
- `[REJECTED]` auto model router;
- `[REJECTED]` LLM judge;
- `[REJECTED]` automatic retry/repair;
- `[REJECTED]` full-package best-of-N;
- `[REJECTED]` automatic employer research;
- `[REJECTED]` automatic submission;
- `[SUPERSEDED]` strict P0.7 state-hardening as top priority;
- `[SUPERSEDED]` 20-job stage as final P0.8 choice.

## Strong P0.7 components to reuse

- `[CONFIRMED]` candidate authorities;
- `[CONFIRMED]` baseline parser/merge;
- `[CONFIRMED]` original Word masters;
- `[CONFIRMED]` dynamic CV overrides;
- `[CONFIRMED]` job identity concept;
- `[CONFIRMED]` package schema as starting point;
- `[CONFIRMED]` one-job-at-a-time persistence;
- `[CONFIRMED]` transactional per-job rendering;
- `[CONFIRMED]` no-submit boundary;
- `[CONFIRMED]` Norwegian persuasion calibration;
- `[CONFIRMED]` portal limit handling;
- `[CONFIRMED]` manual final semantic approval.

## P0.7 audit findings still relevant after objective shift

- `[CONFIRMED]` CV page balance should be improved.
- `[CONFIRMED]` duplicate portal IDs are a cheap worthwhile validation target.
- `[CONFIRMED]` mutable Stage-4 draft-reference logic illustrated fragility of hard strategy locks; P0.8 changes authority model instead.
- `[CONFIRMED]` No-real-pilot status is a major empirical gap; P0.8 should prioritize a real ~8-job pilot over a huge synthetic uniformity suite.

---

# 16. Final state snapshot

## Apparent framework version/state

- `[CONFIRMED]` **P0.8 Selective Quality MVP is the active target architecture.**
- `[CONFIRMED]` P0.7 is implemented and audited but architecturally superseded.
- `[CONFIRMED FROM EXTERNAL ANCHOR]` A final normative P0.8 specification exists project-wide/downstream, but P0.8 is not implemented.
- `[CONFIRMED]` This visible chat stops at planning that specification.

## Most authoritative active decisions

- `[USER-CORRECTION][ACTIVE]` Optimize median + top-80%-mean package quality.
- `[USER-EXPLICIT][ACTIVE]` Weak tail can receive separate rerun/manual round.
- `[USER-EXPLICIT][ACTIVE]` Rebuild P0.8 from scratch and simpler than P0.7.
- `[USER-ACCEPTED-PROPOSAL][ACTIVE]` Sol Max → Terra Max → Sol Max.
- `[USER-ACCEPTED-PROPOSAL][ACTIVE]` Five coherent clusters × ~8, range 6–10.
- `[USER-ACCEPTED-PROPOSAL][ACTIVE]` Two scripts only.
- `[USER-ACCEPTED-PROPOSAL][ACTIVE]` READY/CHECK/RERUN, partial success, targeted `--job`.
- `[USER-ACCEPTED-PROPOSAL][ACTIVE]` Stage 3 truth-bounded strategic authority.
- `[USER-CORRECTION][ACTIVE]` Memory/archetype cache deferred.

## What actually exists

- `[CONFIRMED]` Candidate truth files and P0.7 rendering assets.
- `[CONFIRMED]` P0.7 architecture and implementation prompt.
- `[CONFIRMED]` Implemented P0.7 release ZIP.
- `[CONFIRMED]` P0.7 audit report.
- `[CONFIRMED FROM ANCHOR]` Downstream/current-project P0.8 final normative specification exists, but not in the visible terminal state of this chat.

## What is merely planned in this chat

- `[CONFIRMED]` P0.8 repository/runtime implementation.
- `[CONFIRMED]` revised schemas/artifacts.
- `[CONFIRMED]` two-script runtime.
- `[CONFIRMED]` real ~8-job pilot.
- `[CONFIRMED]` effort A/B tests.
- `[CONFIRMED]` final detailed architecture/file-index specification was the immediate next deliverable but not yet written here.

## Immediate intended next step

- `[CONFIRMED]` **Plan the structure/content/layout of the final P0.8 normative specification, then write and implement from that document.**
- `[INFERRED]` A sibling/downstream chat likely contains the resulting ~3800-line final specification referenced by the external anchor.

## Main unresolved questions

- `[OPEN]` exact P0.8 file tree and field-level schemas;
- `[OPEN]` optional preflight inclusion;
- `[OPEN]` exact review reason codes;
- `[OPEN]` Stage-3 Sol Max vs XHigh after pilot;
- `[OPEN]` Stage-2 Terra Max vs XHigh after pilot;
- `[OPEN]` empirical optimal cluster size;
- `[OPEN]` human quality-scoring rubric / adoption threshold;
- `[OPEN]` exact CV template/layout revision.

## Strongest chronology clues

1. dual-pass P0.7 → single-prompt P0.7;
2. final P0.7 architecture → implementation prompt → release → audit;
3. audit → user Q-happy correction;
4. Q-happy correction → P0.8 from-scratch redesign;
5. 4×10 P0.8 draft → revised 5×~8 final design;
6. final design → request to plan final P0.8 normative spec;
7. any completed final P0.8 spec is likely downstream.

## Confidence/caveats

- `[CONFIRMED]` High confidence in version evolution, objective shift, P0.7 implementation/audit state, and terminal P0.8 conceptual architecture.
- `[CONFIRMED]` Medium confidence on exact intended P0.8 filenames where only assistant proposals existed before the final spec was written.
- `[UNKNOWN]` Actual visible UI chat title.
- `[CONFIRMED]` External baseline anchors are treated as fixed project-wide facts, not as discoveries of this chat.
