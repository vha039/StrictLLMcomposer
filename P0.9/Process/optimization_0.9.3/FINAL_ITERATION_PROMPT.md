# Final Experimental Expansion iteration — prompt for Codex

Paste everything below the horizontal rule into the Codex instance that produced `P0.9.3_REVIEW_AND_IMPLEMENTATION_PLAN.md`.

---

You are running the final Experimental Expansion iteration for:

`C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26`

Use your highest available reasoning effort. **Review and validate → reconcile, optimize and expand → finalize the implementation plans.** This is review and planning. Do not implement any change, do not execute a semantic stage, and do not run a treatment.

After this iteration the project moves to test and validate, then freeze/consolidate/scaffold, then P1.0. This is the last pass in which semantic ambition is cheap. Do not let "final iteration" become an argument for premature consolidation, defensive scaffolding or a validation layer.

## 1. Objective

Your sole outcome objective is **the expected probability of an interview from a truthful, interview-defensible CV and letter.** Judge every engineering, instruction and operator change by its contribution to that.

Do not invent numerical interview probabilities or claim measured uplift. Distinguish observed behaviour, inference and editorial judgment, and say which you are doing.

**Known material falsehoods are not acceptable experimental risk, and blandness is not an acceptable cure.** When you correct an unsupported activity, relationship, attribution, comparison or status: remove or re-attribute the unsupported element, preserve the strongest supported surrounding argument, and never substitute generic language, hedging or a weaker supported claim. If a proposed restriction would prevent both an observed error and legitimate truthful writing, find a more discriminating rule.

## 2. Review inputs and their paths

All are in the repository. Nothing external is required.

| Input | Path | Status |
|---|---|---|
| Your previous plan | `P0.9/Process/optimization_0.9.3/P0.9.3_REVIEW_AND_IMPLEMENTATION_PLAN.md` | Base proposal. Not authority. |
| Independent review and diff against it | `P0.9/Process/optimization_0.9.3/P0.9.3_CLAUDE_REVIEW_AND_PLAN_DIFF.md` | Challenge it. |
| Operational expansion design | `P0.9/Process/optimization_0.9.3/User required optimizations.md` | Challenge it. |
| Repository map | root `AGENTS.md` | Read first. |
| Frozen normative specification | `P0.9/Architecture/P0.9_FINAL_NORMATIVE_SPECIFICATION.md` | Governs architecture. |
| Implementation contract | `P0.9/Architecture/P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md` | §22 prohibited redesigns. |
| Live implementation | `P0.9/Build/**` | Reproduced behaviour outranks any document. |
| Behavioural evidence | `P0.9/Build/runs/**` — eight runs | Distinguish independent executions from reused artifacts and changed inputs. |
| Prior audit | root `OPUS_P0.9.1_FINAL_POST_IMPLEMENTATION_ACCEPTANCE_AUDIT.md` | Evidence only; several findings are already resolved. |

The absent `P0.9/Process/optimization_0.9.2_final/` was deliberately never materialized. Its absence is not a defect; do not create it. Ignore `P0.7/**`, `P0.9/archive/`, the Build backup ZIP and `P0.9/Build/tmp/`. Do not inventory `.venv` or cache directories.

Authority order: this prompt and current user instruction; the normative specification; the implementation contract; root `AGENTS.md`; then plans, audits and Process material as evidence only. Reproduced current behaviour outranks a document's description of the implementation, but never silently amends a normative requirement — record that distinction when it arises.

## 3. What to do

### 3.1 Validate independently, then challenge

Verify the diff document's findings against current disk rather than accepting them. It claims, among other things:

- `PRJ-04` in `Work_experience.md` contains no workshop, training or onboarding evidence;
- the `FORFATTERSTEMME.md` authority conflict is confined to `Kanalkalibrering` and `Stabil forfatter`, and three of your five proposed voice edits therefore weaken instructions that were never ambiguous;
- three retired writing prescriptions are still live inside the protected factual inputs, including the differentiator cap verbatim;
- `Other_high_value_information.md:441-443` routes two domains to files that do not exist anywhere in the repository;
- `status.py:437` structurally prevents `next --stage 3` from returning a completed job;
- `branch.py:181-185` and `:334-348` prove parent immutability by whole-tree byte comparison, which collides with nested branch storage;
- two levels of branch nesting exceed `MAX_PATH_CHARS` for real rendered output.

Challenge its reasoning and its proposed restrictions as hard as you challenge your own. In particular, decide for yourself whether its rejection of three of your voice edits is right, or whether it has under-protected the authority boundary to preserve prose. Say which, with evidence.

**Recover valuable ideas even when you reject their proposed implementation.** A rejected mechanism often contains a correct diagnosis.

### 3.2 Reconcile

Produce one coherent position from three documents that currently overlap. Where the diff amends your plan, either accept the amendment or defeat it with evidence — do not average them. Where the two documents already agree, do not re-litigate.

Resolve every cross-document dependency explicitly, including: the ordering of the recovery-wording change against `branch --from-stage`; whether the planned two-job treatment should use `--from-stage`; and whether any goal-prompt text would let an agent cross the stage boundary.

### 3.3 Expand

Seek any remaining substantial net-positive improvement to the final application, especially in: evidence selection against the employer's actual selection decision; category legibility and argument depth; CV/letter complementarity; supported strength versus needless caution; instruction salience and ownership; schema/instruction/runtime drift; evidence-index granularity; human effort across the full freeze/branch → next → context → author → submit → finalize → render → status loop; failure and recovery coherence; and components still expressing an older semantic design.

Retain only findings that survive an explicit value-versus-cost challenge. Record what you rejected and why. Do not pad the accepted list.

## 4. Governing philosophy

Every recommendation must satisfy all four.

- **ED-1 — happy path, no defensive scaffolding.** Implement what the happy path needs or what directly improves the product. No defences against hypothetical conditions, no redundant checks of material a human already reads, no infrastructure because it might become useful.
- **ED-2 — strong coordinated treatment, not a micro-patch.** When a defect has interacting causes, fix the combination. Do not confuse "coordinated" with "rewrite everything."
- **ED-3 — large coherent clusters, minimal batched validation.** Validate at meaningful cluster boundaries, not around every edit.
- **MVP-KISS — semantically aggressive, mechanically simple.** Put ambition into the argument, evidence selection, writing and operator experience. Add mechanics only where an explicitly requested capability requires them.

Existing tests and disposable probes are permitted. Add or change a test only where the implementation needs it to resolve a concrete uncertainty or verify changed behaviour. Do not expand scaffolding, QA gates, CI, telemetry, monitoring, generic validation, configuration systems, retry frameworks or compatibility layers.

The two operational capabilities in §5 may require real CLI and runtime changes. Do not reject them because earlier semantic passes correctly introduced zero machinery. Design the minimum those capabilities require, and do not treat that exception as licence for general framework engineering.

## 5. Carried-forward requirements

**Immutable:** one instance and one chat per semantic stage. No operational feature may cross that boundary.

**Preserve:** truthful, correctly attributed, interview-defensible claims; exact candidate, employer and vacancy identity; the three factual authorities; a Bokmål CV and letter for every CORE vacancy; human approval before any external action; no deterministic model calls, employer contact or submission; Stage-3 substantive elasticity and its content-locked final polish; historical evidence and frozen source integrity.

**Do not replace the settled semantic design:** occupational legibility before differentiation; deep integrated proof units; supported judgment inside the argument; separately attributed cross-record judgment with no causal, outcome or lifecycle borrowing; proof-function-specific lifecycle; complementary CV and letter; provisional Stage-3 grounding followed by upstream option value; truthful positive gap engagement. You may challenge its *implementation*.

**Keep** the approved calibration `fortsatt i bruk om lag to og et halvt år senere`. Do not replace it with `rapportert i bruk`.

**Do not reopen:** preservation fields or logs, `decision_signal`, `krav_framing`, final-versus-strategy compliance comparison, numeric quality judges, length or density targets, AI-detector optimization, best-of-N, automatic model orchestration, additional semantic stages, or PDF repair as a semantic concern.

**The two operational expansions remain required:**

- **A — stage-bound goal operation** as an alternative to cluster-bounded work: continue through the eligible queue for one stage, across one run or an explicitly named set of runs, resuming from disk, reporting blocked work honestly, never equating success with `READY`.
- **B — stage-specific branching and deliberate stage redo**, with branches stored inside the source run at `[run]/branches/[stage_branched_from]_[executing_model]_[date-time_stamp]`, and reliable execution of "re-do stage 3 for all vacancies in run *R*".

If either conflicts with a frozen provision, name the exact governing ID and the minimum amendment. Do not bypass it silently and do not stop at declaring it impossible.

## 6. Deliverable

Produce **two complete, standalone final plans** that replace the need to combine earlier plans and diffs:

1. `P0.9/Process/optimization_0.9.3/P0.9.3_FINAL_SEMANTIC_PLAN.md`
2. `P0.9/Process/optimization_0.9.3/P0.9.3_FINAL_OPERATIONAL_PLAN.md`

Do not edit the three existing documents; supersede them. Each final plan must be executable by a fresh implementing model holding that file and the repository, with no reference to the superseded documents.

Each must specify: exact files and existing section selectors; the current wording to be replaced and its complete replacement text, or concrete code behaviour; target interactions; coherent clusters in execution order with only necessary batched verification; necessary test and fixture changes with the reason an existing test cannot cover it; exact run commands and parent/source selection; finalize, render and status behaviour; output locations; and explicit STOP conditions. "Improve X" or "review Y" is not an implementation instruction.

Require the implementing model to fix and complete the preceding implementation before new work, to incorporate a later finding at the location of the earlier fix it changes, to preserve supported persuasive strength and Stage-3 freedom, to work in large clusters, and to implement nothing rejected.

**Preserve decision-relevant reasoning inside these two documents:** observations, causal hypotheses, assumptions, uncertainty, alternatives, rejected approaches with reasons, promising unadopted ideas, and what evidence would change each recommendation. Mark what is verified, what is inferred and what is editorial judgment. Reasoning summaries, not private chain-of-thought. Exact instructions accompany that rationale; they do not replace it. Create no separate reflections file.

Before finishing, reconcile the two documents: no contradictory commands, scope rules or assumptions; no operational feature crossing the stage/chat boundary; no semantic restriction added merely to simplify orchestration; no dependency on unavailable attachments; no vague decision deferred to the implementing model; every accepted change in a coherent cluster with a concrete output benefit.

## 7. Read-only discipline

This is a read-only review of the framework. Do not modify Build, Architecture, authorities, historical runs or pilot records. Do not run `freeze`, `branch`, a semantic stage, `finalize` or `render`.

Verify side effects before calling anything you intend to treat as read-only: `status` rewrites `generated/views/<run>/status.json` and `queue.md` even with `--json`, and `context` writes a handoff and return directory. `next` and `verify-integrity` are genuinely read-only. Use disposable external copies where necessary, and do not build a persistent audit harness.

## 8. Chat output

Return only: your verdict on the diff document and on your own previous plan; the most consequential reconciled decisions; any remaining feasibility concern with the two operational capabilities and your recommended version; genuine user decisions; and links to the two final documents.

Make routine judgment calls yourself and state them. Reserve open questions for decisions that truly require the user. Do not ask whether to proceed. Complete both documents, then **STOP**.
