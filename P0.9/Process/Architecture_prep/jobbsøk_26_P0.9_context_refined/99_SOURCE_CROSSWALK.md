# Source Crosswalk and Completeness Certificate

## 0. Purpose

This file certifies that every supplied source was examined and assigned an explicit treatment. Source IDs follow the supplied filename prefix. The corpus intentionally has no source numbered 01: the former P0.7 baseline was incorporated into `SRC-00` so the map and handling rules are read first.

Treatment vocabulary:

- `FULLY_MINED` — all distinct decision-relevant signal was actively reconciled into the package;
- `SELECTIVELY_MINED` — useful unique signal was retained; repetition, process narration or superseded detail was omitted;
- `SUPERSEDED_BUT_RATIONALE_RETAINED` — active rules were replaced, but causal/rejection lessons remain;
- `DERIVED_SYNTHESIS` — used only after primary-source reconstruction; novel synthesis is labelled and historical authority is not inferred;
- `FALLBACK_ONLY` — no unique active proposition; retained only for provenance or dispute fallback.

“Represented in” names primary homes, not every incidental cross-reference.

---

## 1. All-source crosswalk

| Source ID | File | Phase / role | Authority class | Unique useful contribution | Represented in | Treatment |
|---|---|---|---|---|---|---|
| `SRC-00` | `00_READ_FIRST_CORPUS_MAP__P07_EXECUTABLE_BASELINE_KB.md` | Corpus map + P0.7 executable baseline | Navigation/control; historical implementation evidence | Establishes reading order, granular supersession, source classes, 20-file manifest and curated last-executable P0.7 system, candidate boundaries, artifacts, risks and reusable substrate | `00`, `01`, `03`, `04`, `99` | `FULLY_MINED` |
| `SRC-02` | `02_P07_TO_P08_OBJECTIVE_SHIFT_QHAPPY_KB.md` | P0.7 audit through selective-quality redesign | User-decision/evolution reconstruction | Preserves the decisive user correction from uniform reliability toward `Q_happy`, strong-majority quality, weak-tail rerun, and the causal bridge from P0.7 to the proposed/adopted P0.8 direction | `01`, `02`, `03`, `05` | `FULLY_MINED` |
| `SRC-03` | `03_PROJECT_INTENT_LLM_CONTEXT_REFERENCE.md` | Compact project intent | Authoritative intent profile | Densest source for objective, utility hierarchy, truth authority, persuasion freedom, Norwegian style, single backbone, CV/application complementarity, human/KISS constraints and non-goals | `00`, `01`, `02`, `05` | `FULLY_MINED` |
| `SRC-04` | `04_P07_P08_SELECTIVE_QUALITY_REDESIGN_HISTORY.md` | Intermediate P0.7→P0.8 redesign history | User-decision/evolution reconstruction | Captures the pre-freeze sequence, P0.7 audit defects, discarded reliability bias, proposed three-stage topology, non-goals and decisions before the final normative spec existed | `01`, `03`, `04` | `SUPERSEDED_BUT_RATIONALE_RETAINED` |
| `SRC-05` | `05_P08_ARCHITECTURE_FINALIZATION_HISTORY.md` | P0.8 finalization history | Terminal-state reconstruction with implementation evidence references | Confirms generation/verification of the 3,825-line P0.8 final normative specification, exact terminal topology/status and lineage from P0.6/P0.7 | `01`, `03`, `04`, `99` | `SELECTIVELY_MINED` |
| `SRC-06` | `06_P08_FINAL_NORMATIVE_SPECIFICATION.md` | P0.8.0 architecture/build/runtime specification | **Primary normative within P0.8 scope** | Last formally adopted complete architecture: product contract, Sol→Terra→Sol roles, ~5×8 clustering, truth/evidence model, artifacts, dynamic CV, portal/channel handling, finalization, rendering, repository, tests, pilot and acceptance contract | `01`, `02`, `03`, `04`, `05` | `FULLY_MINED` |
| `SRC-07` | `07_P08_CROSS_MODEL_REVIEW_ADJUDICATION.md` | Cross-model review resolution | Review/adjudication; non-normative | Adds precise surviving contract issues—full employment override, evidence-ref sync, RERUN route, rendering transaction, phrase drift, test tiers, small-n metric correction—and records rejected YAML/auto-fit/n-gram proposals | `02`, `03`, `04`, `05` | `FULLY_MINED` |
| `SRC-08` | `08_P081_CONSOLIDATED_PREIMPLEMENTATION_HARDENING.md` | P0.8.1 consolidated hardening | Review/hardening; explicitly `NON_NORMATIVE_UNTIL_ADOPTED` | Strongest interface-hardening corpus: canonical intake, freeze, expected set, mechanical/semantic split, replacement semantics, final refs, validators, repair scope, partial success, render transaction, metrics, operator flow and do-not-build firewall | `01`, `02`, `03`, `04`, `05` | `FULLY_MINED` |
| `SRC-09` | `09_P08_EXTERNAL_EVIDENCE_REVIEW.md` | 2026 P0.8 external evidence review | Research/evidence | Early external constraint set on model surfaces, long context, schema validation, selective review, pilot statistics, OOXML/LibreOffice, security, Norwegian practice and implementation order; useful mainly where later evidence does not supersede/correct it | `03`, `04`, `05` | `SELECTIVELY_MINED` |
| `SRC-10` | `10_P09_BRAINSTORM_BRIEF_NON_NORMATIVE.md` | Broad P0.9 option foundry | Exploratory, explicitly non-normative | Opens authenticity/personality, settings, product simplification, Luna, context-centric architectures, strategy/state alternatives, source escape, counterfactual reserve and multi-variable interactions; also preserves activation triggers and rejected framings | `01`, `02`, `03`, `05` | `SELECTIVELY_MINED` |
| `SRC-11` | `11_P09_BRAINSTORM_REVIEW_DECISION_SPACE.md` | Bounded P0.8.1 vs P0.9 optimization review | Non-normative decision basis | Independently reviews P0.8.1, normalizes colliding IDs, prunes the brainstorm, defines decision clusters/novel mechanisms, separates prediction/order/treatment and identifies high-value tests and bundle interactions | `01`, `02`, `03`, `05` | `FULLY_MINED` |
| `SRC-12` | `12_P09_PREP_PACKAGE_V2.md` | Pre-architecture uncertainty-reduction package | Preparation/proposal, not architecture | Prioritizes product boundary, human-load envelope, experiment executability, template/rendering facts and generality budget; supplies questionnaire defaults, research contract and local-test shortlist | `01`, `03`, `05` | `SELECTIVELY_MINED` |
| `SRC-13` | `13_P09_ARCHITECTURE_OPTIMIZATION_CHAT_SUMMARY.md` | Partial parallel-chat reconstruction | User/process reconstruction with coverage warning | Preserves high-value preparation rules: maximize new signal per user effort, prefill answers, use low-load interactions, write a true research prompt, and avoid turning preparation into another architecture framework | `01`, `03`, `05`, `99` | `SELECTIVELY_MINED` |
| `SRC-14` | `14_P09_PARALLEL_PREP_CHAT_SUMMARY.md` | Independent overlapping prep/review branch | Reconstruction/review | Confirms direct P0.7/P0.8 reading in the parallel branch, external capability checks, personality boundary proposal, brainstorm-review provenance and chronology; execution-error/process details with no downstream value were excluded | `03`, `05`, `99` | `SELECTIVELY_MINED` |
| `SRC-15` | `15_P09_EXTERNAL_EVIDENCE_REPORT.md` | Focused P0.9 external evidence | Research/evidence; factual authority by claim quality | Decision-critical evidence on Work/Codex/API differences, chat JSON validation, long-context risk, platform variability, public-sector qualification principle, SDT/LibreOffice constraints, security and local tests that dominate further research | `01`, `02`, `03`, `04`, `05` | `FULLY_MINED` |
| `SRC-16` | `16_PERSONALITY_CANONICAL.md` | Canonical personality/work-style profile | Interpretive context; no candidate claim authority | Supplies nuanced high-signal personality, cognition, communication, motivation, work pattern, failure modes, collaboration protocol and anti-overinterpretation boundaries | `01`, `02`, `05` | `FULLY_MINED` |
| `SRC-17` | `17_P09_PERSONALITY_FRAMEWORK_CONTEXT.md` | P0.9-specific personality interface | Proposed interpretive runtime; non-normative | Defines optional activation, evidence boundary, stable `PF-01..PF-20` facets, anti-inference index, distilled handoff and final-writer override; concrete experiment candidate rather than adopted contract | `01`, `02`, `03`, `05` | `SELECTIVELY_MINED` |
| `SRC-18` | `18_P09_LATEST_INTEGRATION_SUMMARY_USER_DECISIONS.md` | Latest user-decision and terminal-state reconstruction | **High-priority user-decision source** | Supplies current P0.9 priority order, fresh-runtime permission, human/time/deadline envelope, prompt budget, final-Sol elasticity, candidate-source confirmation, optional personality rule, environment facts, product simplification permissions, evaluation corrections and complete unresolved-state ledger | `00`, `01`, `02`, `03`, `04`, `05` | `FULLY_MINED` |
| `SRC-19` | `19_P07_TO_LATEST_DEEP_EVOLUTION_DERIVED_ANALYSIS.md` | Cross-version audit plus direct P0.7 artifact inspection | **Derived synthesis**; direct audit portions empirical | Adds high-value causal integration and direct P0.7 findings: schemas/finalizer behavior, actual master internals, SDT fill/unwrap method, test rerun and defects. Its architecture conclusions were checked against SRC-00/02–18 | `03`, `04`, `05` | `DERIVED_SYNTHESIS` |
| `SRC-20` | `20_P09_CURRENT_BEST_CANDIDATE_SPEC_DERIVED.md` | Converged P0.9 candidate for adoption | **Derived synthesis**, explicitly not historical adoption | Provides the strongest complete candidate topology and the “delete obsolete surfaces first” thesis. Useful structural synthesis was retained; choices such as portal detachment, JSON strategy, job manifest, index core, A/B removal and personality default were demoted where primary evidence left them open | `01`, `02`, `03`, `04`, `05` | `DERIVED_SYNTHESIS` |

---

## 2. Authority and role index

### 2.1 Normative versus non-normative

- **Historically normative:** `SRC-06` only for the complete P0.8.0 architecture, subject to later explicit user decisions at proposition level.
- **Implemented empirical baseline:** `SRC-00` plus direct audited implementation evidence in `SRC-19`.
- **Explicitly non-normative hardening/review:** `SRC-07`, `SRC-08`, `SRC-10`, `SRC-11`, `SRC-12`, `SRC-17`.
- **Later user-decision reconstruction:** `SRC-18`, with individual propositions carrying authority rather than the whole document automatically replacing every older rule.
- **Derived, challenge-required:** `SRC-19`, `SRC-20`.
- **Interpretive, never factual candidate authority:** `SRC-16`, `SRC-17`.

No supplied source establishes a historically adopted final P0.9 release.

### 2.2 Sources primarily valuable for chronology/evolution

`SRC-02`, `SRC-04`, `SRC-05`, `SRC-13`, `SRC-14`, `SRC-18`, and the cross-version portions of `SRC-19`.

### 2.3 Sources primarily valuable for implementation evidence

`SRC-00`, `SRC-05`, `SRC-06`, `SRC-08`, and the direct-audit portions of `SRC-19`.

### 2.4 Sources primarily valuable for external/context evidence

`SRC-09`, `SRC-15`, `SRC-16`, `SRC-17`, plus context-design option evidence in `SRC-10`–`SRC-12`.

---

## 3. Source → output completeness check

Every source has one of four outcomes:

1. **Active current rule or constraint** in `01`/`02`;
2. **Evolution/rejection rationale** in `03`;
3. **Implementation fact/obligation** in `04`;
4. **Research/context/evaluation consequence** in `05`.

No source was silently dropped. Where a source added no independent active rule, its role and exclusion reason are explicit above. Repeated conversation framing, rhetorical emphasis, source-by-source narration, inaccessible historical wording, duplicate summaries and obsolete mechanism detail with no regression value were intentionally excluded.

---

## 4. Output → source support check

The package’s consequential claims have the following primary support paths:

| Package claim family | Primary supporting sources |
|---|---|
| `Q_happy`, selective quality, truth/persuasion/KISS | `SRC-02`, `SRC-03`, `SRC-06`, `SRC-18` |
| Version state and authority | `SRC-00`, `SRC-05`, `SRC-06`, `SRC-08`, `SRC-18` |
| P0.7 implementation/test/master facts | `SRC-00`, direct-audit sections of `SRC-19` |
| Three-stage control and final-writer authority | `SRC-06`, `SRC-08`, `SRC-18` |
| P0.8.1 hardening candidates | `SRC-07`, `SRC-08` |
| P0.9 product/context/state forks | `SRC-10`, `SRC-11`, `SRC-12`, `SRC-18` |
| Latest environment/human/evaluation constraints | `SRC-18` |
| Norwegian channels, ATS, LibreOffice, model/surface and security evidence | `SRC-09`, `SRC-15`, qualified by `SRC-19` implementation inspection |
| Personality source and optional interface | `SRC-16`, `SRC-17`, `SRC-18` |
| Candidate P0.9 convergence and cross-source synthesis | `SRC-19`, `SRC-20`, explicitly labelled `[SYNTHESIS]` and challenged in `03` |

This crosswalk is the provenance certificate, not a substitute for the authority ledger in `01` or the detailed candidate in `02`.
