# Jobbsøk_26 P0.9 context package — read this first

## Current-state capsule

Jobbsøk_26 is a private, local, manually operated production system for one candidate. Its purpose is to transform human-approved Norwegian vacancies plus authoritative candidate evidence into truthful, vacancy-specific, persuasive and manually submittable application packages with minimal human rewriting. The employer-facing package—not the analysis, state, or QA machinery—is the product.

The project has four distinct version states that must not be collapsed:

| Version | Actual status | What it contributes now |
|---|---|---|
| **P0.7** | Last implemented and mechanically test-backed release | Executable engineering baseline: local files, four manual stages, deterministic ingest/advance/finalize scripts, schemas, Word masters, fixtures, tests and observed rendering behavior. |
| **P0.8.0** | Last formally adopted normative architecture; never implemented | Selective Quality redesign: `Q_happy`, three-stage Sol→Terra→Sol topology, explicit headline, elastic final writer, partial success, READY/CHECK/RERUN, dynamic CV merge and two-script target. |
| **P0.8.1** | Mature pre-implementation review/hardening; explicitly non-normative unless adopted | High-value interface repairs: canonical intake/freeze, expected-set reconciliation, mechanical-versus-semantic validation, full employment-override replacement, final evidence synchronization, repair-scope statuses, validator-before-completion and better pilot discipline. |
| **P0.9** | Current design target; materially researched and partially constrained, but not historically frozen or implemented | Later user policy, product-simplification permissions, context/personality/Luna options, fresh-runtime permission, external evidence, and a bounded set of unresolved architecture forks. |

This seven-file package is the reconciled information substrate for the next three stages. It is deliberately **future-facing**: it preserves the current authority model, candidate architecture, implementation evidence, unresolved questions, design-relevant history and research consequences while removing source-by-source repetition.

Files `19` and `20` in the source corpus were useful derived syntheses, not independent authority. Their strongest cross-source insights are retained; their unadopted choices remain labeled as synthesis or open decisions. [SRC-00: §§0.1–0.6; SRC-18: §§4, 12, 15; SRC-19: Status and §1; SRC-20: §§0–1]

## Package map

| File | Primary role |
|---|---|
| [`01_CURRENT_STATE_AUTHORITY_AND_DECISIONS.md`](01_CURRENT_STATE_AUTHORITY_AND_DECISIONS.md) | Highest-density current state: objective, version status, active decisions, constraints, non-goals and complete resolution queue. |
| [`02_P0.9_CANDIDATE_ARCHITECTURE.md`](02_P0.9_CANDIDATE_ARCHITECTURE.md) | Best-supported current architecture candidate. Concrete enough to finalize and build, but explicitly not the formally adopted P0.9 release. |
| [`03_EVOLUTION_DELTAS_AND_RATIONALE.md`](03_EVOLUTION_DELTAS_AND_RATIONALE.md) | Causal evolution, granular version deltas, mechanisms that survived or must not return, and the independent challenge of derived sources 19–20. |
| [`04_IMPLEMENTATION_BASELINE_AND_BUILD.md`](04_IMPLEMENTATION_BASELINE_AND_BUILD.md) | What P0.7 actually implemented and proved; what to reuse, adapt, rebuild or retire; target-environment verification and builder obligations. |
| [`05_EVIDENCE_CONTEXT_AND_EVALUATION.md`](05_EVIDENCE_CONTEXT_AND_EVALUATION.md) | External evidence and context-system guidance organized by design consequence, with strength, uncertainty and local-test boundaries. |
| [`99_SOURCE_CROSSWALK.md`](99_SOURCE_CROSSWALK.md) | Completeness/provenance certificate for all 20 inputs, including authority class, unique contribution, destination and treatment. |

Source references use stable identifiers such as `[SRC-06: §15]`; `99_SOURCE_CROSSWALK.md` resolves every ID to its supplied filename.

## Authority rules

Two authority questions remain separate:

1. **Project-decision authority:** later explicit user correction/decision → earlier unsuperseded user decision → adopted normative specification → explicitly adopted proposal → supported reconstruction/synthesis → unresolved idea.
2. **Empirical authority:** directly verified implementation/test evidence or primary source → strong authoritative evidence → supported research synthesis → inference → unsupported assertion.

Supersession is proposition-level, never document-level. A newer statement replaces, refines, narrows, extends or invalidates only the specific older proposition it addresses. Everything else coexists. A later research finding may correct an environment assumption without choosing product policy; a user preference may choose product policy without proving an external fact.

Labels used where needed:

- `[USER]` — explicit user decision/correction;
- `[NORMATIVE]` — inherited P0.8 rule not later superseded;
- `[VERIFIED]` — direct implementation/test evidence;
- `[RESEARCH]` — external evidence;
- `[SYNTHESIS]` — useful cross-source conclusion not historically adopted;
- `[OPEN]` — unresolved by the corpus.

## Three downstream tasks

### Step 1 — freeze the final P0.9 normative architecture

Use the package to resolve the bounded `STEP1_FREEZE` queue, explicitly adopt or reject synthesis choices, issue one internally consistent normative specification, and preserve empirical questions for implementation or experiment rather than settling them rhetorically.

**Normally read:** `00`, `01`, `02`, `03`, relevant sections of `05`, then `99` for provenance disputes.

### Step 2 — build and verify the Codex-ready repository

Use the final Step-1 specification plus the actual P0.7 release/artifacts. Reuse only after inspection. Prove the deterministic vertical slice, target Windows rendering, stage validators, one-job transaction, partial success and real model workflow. Verified runtime behavior outranks design assumptions.

**Normally read:** `00`, `01`, final Step-1 spec, `04`, implementation-relevant parts of `02` and `05`, then `99` as needed.

### Step 3 — optimize candidate/context source material

Use the final architecture and actual source corpus to improve segmentation, stable evidence addressing, source escape and retrieval only where marginal value is demonstrated. Personality remains interpretive rather than factual authority; model-generated preparation remains advisory; graph/vector machinery is not presumed necessary.

**Normally read:** `00`, `01`, context/evidence sections of `02`, all of `05`, final Step-1 spec and the verified Step-2 repository contracts.

## Carry-forward rule

- The **Step-1 final normative specification** supersedes this package wherever it explicitly resolves architecture.
- **Step-2 verified implementation and tests** supersede assumptions about actual repository, tool, model-surface and runtime behavior.
- **Step-3 verified context-system results** supersede provisional retrieval, indexing, personality and context-preparation ideas.
- Historical provenance, earlier empirical evidence and explicit rejected-regression lessons remain available unless directly corrected.

Do not reopen the original 20 documents for normal downstream work. Use them only for an unusual provenance dispute, exact historical wording, direct artifact reinspection or an edge case not represented here.
