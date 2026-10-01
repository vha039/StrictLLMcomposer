# Final plan consolidation — prompt for Codex

Paste everything below the horizontal rule into the Codex instance that authored `P0.9.3_REVIEW_AND_IMPLEMENTATION_PLAN.md`.

---

You are producing the **final** implementation plans for:

`C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26`

Highest available reasoning effort. This is adjudication, consolidation and planning. **Do not implement anything, do not execute a semantic stage, do not run a treatment.**

## 0. Termination contract — read this before anything else

This is the last planning pass. It converges or it fails.

**You have a fixed deliverable set: two documents, named in §7. Not three. Not "as many as the work requires."**

**One-pass adjudication.** Every item in the input registers gets exactly one disposition — ACCEPT, AMEND, REJECT or DEFER — recorded once with its reasoning. You do not revisit a decided item to improve its wording, and you do not reopen it because a later item made you think of something adjacent. Reopen only when disk evidence directly contradicts the decision.

**DEFER is a success state.** An item that is real but not worth this pass is deferred with a reason. That is a complete answer, not an unfinished one.

**Bounded discovery.** You are expected to notice new things while verifying — that vigilance is wanted. But a new finding goes into the discovery register with a disposition and stops there. **A finding never spawns a new investigation, a new sweep, a new document, or a re-adjudication of settled items.**

**Verification depth limit.** Verify what would change a decision. Do not verify what merely confirms a decision you have already made, and do not re-verify what a prior pass verified unless you have reason to doubt it.

**Forbidden loop shapes**, explicitly: another full-framework sweep; a third planning document; reopening a decided item for polish; "one more consistency pass"; deferring the stopping test until the plan feels complete. Completeness is defined in §8 and is objective.

## 1. Inputs and their status

Read in this order. Status is binding — do not read superseded documents.

| Document | Path under `P0.9/Process/optimization_0.9.3/` | Status |
|---|---|---|
| **Consolidated final input** | `P0.9.3_CONSOLIDATED_FINAL_INPUT.md` | **Read first.** Carries every decision register, all new facts, and the Stage-2 analysis. |
| Your base plan | `P0.9.3_REVIEW_AND_IMPLEMENTATION_PLAN.md` | Live. The substrate you are consolidating. |
| Operational design | `User required optimizations.md` | Live. Amended by the consolidated input §5.4. |
| Framework enhancements | `IDENTIFIED_FRAMEWORK_ENHANCEMENTS.md` | Live **except FE-01**, which is replaced. |
| User answers | `User clarifications, optimizations, expansions, decisions and other user-work.md` | Live as provenance; its answers are already integrated into the consolidated input. |
| Prior review diff | `P0.9.3_CLAUDE_REVIEW_AND_PLAN_DIFF.md` | **SUPERSEDED. Do not read.** Its content is folded into the consolidated input, with four items reversed. |
| Prior handoff prompt | `FINAL_ITERATION_PROMPT.md` | **SUPERSEDED by this prompt. Do not read.** |

Repository authority, in order: this prompt and current user instruction; `P0.9/Architecture/P0.9_FINAL_NORMATIVE_SPECIFICATION.md`; `P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md`; root `AGENTS.md`; then all Process material as evidence only. **Reproduced behaviour in `P0.9/Build/` outranks every document including this one**, but never silently amends a normative requirement — record that distinction when it arises.

Ignore `P0.7/**`, `P0.9/archive/`, the Build backup ZIP and `P0.9/Build/tmp/`. Do not inventory `.venv` or caches. `P0.9/Process/optimization_0.9.2_final/` was deliberately never created; its absence is not a defect.

## 2. What changed since you wrote your plan

Five things. Each is verified against disk in the consolidated input; verify anything that would change a decision.

**2.1 Stage 2's necessity is now the central question, with measurement.** Draft → final letter retention across every completed run: 20.4%, 24.2%, 14.3%, 24.8%, **92.4%, 77.0%**, 18.6%, 33.0%, 9.3%, 13.7%. The two bold outliers are the treatment run, where one model authored Stages 2 and 3 in a single session — the configuration `Spec:313` forbids in production. **Excluding it, Stage 3 discards 67–91% of the draft, median ≈ 79%.**

The structural argument matters more than the measurement: `final_package.json` requires complete `cv` and `letter`, so Stage 3 emits the same output volume whether it inherits a perfect draft or none. **A draft cannot absorb output tokens the schema forces Stage 3 to write anyway.** Stage 2's stated cost rationale was unachievable before any model ran.

Stage 2 is also the only traced defect-injection point: D1, D2 and both fabrications in `r20260905-115243`'s drafts originated there, and Stage 3 *strengthened* D1 rather than catching it.

**2.2 Six new candidate facts** from the user (consolidated input §4). Two consequences you must not miss: `ENH-02` **reverses** the prior recommendation to soften `i praksis eneste kodende utvikler` — the strong wording is confirmed correct and the Avinor `CHECK` resolves by confirmation. `ENH-05` records the 2027 budgeting tool as **in hospital-wide use**, which converts the Avinor carrying case into a materially stronger two-act arc.

**2.3 The user widened agent authority.** In the user's words: *"what is mine is the adding, removal and change of actual experience or other facts about me… unless it concerns changes to the actual `[ID] – [Experience]` nuggets, you and any other agent are free to change it however you see fit without even explicitly informing me."* Every routing table, retrieval index, provenance map, selection-metadata block and instruction **inside** the authorities is agent-owned. Only factual nuggets and their ceilings are user-owned.

**2.4 A retrieval architecture replaces FE-01.** `evidence_index.json` already stores `line_start`/`line_end` per entry, so a ~30-line `fetch.py` can return verbatim frozen source by `EV:` id. The bundle then carries an id list only (~2,400 tokens against 22,900). Three earlier recommendations are reversed by this: the slim-index proposal, the cut of the three retrieval indexes (they become the fetch search index), and the classification of line ranges as noise.

**2.5 Sequencing reversed.** Hold-inputs-fixed made sense when the facts were stable. `ENH-02/04/05` change what is *true*, so a comparison against stale facts tests the wrong package.

## 3. The one decision that changes the plan's shape

**Decide first, before writing anything: is Stage 2 cut or retained?**

Everything else composes either way, but your base plan places a substantial share of the complete-proposition correction in `stage2_package_writer.md` — the routing table, the composition order, the `## Truth` replacement. **If Stage 2 is cut, those edits address a file that will not exist**, and the correction must be relocated into Stage 1 (what `role` may assert) and Stage 3 (authoring and pre-lock repair).

Settle this before drafting Cluster 1 or you will write that cluster twice.

The consolidated input recommends cutting, with the amendment surface enumerated in its §1.6. `Spec §22.1` freezes **"three-stage semantics"** (line 1218), so cutting requires an explicit amendment — name it, do not bypass it silently. If you retain Stage 2 against that recommendation, defeat the structural argument in §2.1 with evidence, not preference, and say what Stage 2 will do that justifies ~95,000 tokens and a chat per job.

Stage 2's mechanical rules must survive either way. The CV **full-replacement** override semantics — absent versus present-empty — is the one rule whose violation yields a valid artifact and a wrong document, and it currently lives only in the file that may be deleted. Losing it in the migration would be the worst possible outcome of this pass.

## 4. Adjudication protocol

Every item below gets one recorded disposition. Cite the repository file and line that supports it where the decision turns on current behaviour.

**Registers you must clear completely:**

1. Your base plan's own D1–D4 and E1–E2.
2. Consolidated input §6.1 — nine items carried forward from the superseded diff.
3. Consolidated input §6.2 — four reversals.
4. Consolidated input §6.3 — six new structural items, N-01 through N-06.
5. Consolidated input §6.4 — eight authority-maintenance items, ordered by value.
6. Consolidated input §6.5 — context reduction, including the `{!}` items the user delegated to you and the `FLAG-02` field-by-field call.
7. Consolidated input §7 — ten proposed improvements, P-01 through P-10.
8. Consolidated input §8 — four open decisions.
9. `User required optimizations.md` §A (goal mode) and §B (`--from-stage`, branch namespace, `ACC-03` proof scope).
10. `IDENTIFIED_FRAMEWORK_ENHANCEMENTS.md` FE-02 through FE-09, FE-01 having been replaced.

**Adjudication standard.** ED-1 happy path, no defensive scaffolding. ED-2 coordinated treatment, not a micro-patch, and not "rewrite everything" either. ED-3 large coherent clusters, minimal batched validation. MVP-KISS semantically aggressive, mechanically simple. Rank by `AGENTS.md`'s optimization order: truthful package quality ≫ low human effort > simple robust implementation > model cost > reversibility.

**Challenge the recommendations you are given.** The consolidated input contains verified findings, inference and editorial judgment, and marks which is which. Two of its better outcomes came from the user overturning its author. Extend the same treatment to it: recover a valuable diagnosis even when rejecting its proposed implementation.

**Do not re-adjudicate the settled semantic design** — occupational legibility before differentiation; deep integrated proof units; supported judgment inside the argument; separately attributed cross-record judgment with no causal, outcome or lifecycle borrowing; proof-function-specific lifecycle; complementary CV and letter; provisional Stage-3 grounding then upstream option value; truthful positive gap engagement. You may find its *implementation* wrong; you may not replace the design.

**Preserved absolutely:** truthful, correctly attributed, interview-defensible claims; exact candidate, employer and vacancy identity; the three factual authorities as the only source of candidate facts; Bokmål CV and letter for every CORE vacancy; human approval before external action; no deterministic model calls, employer contact or submission; Stage-3 elasticity and its content-locked polish; **one instance and one chat per semantic stage**; historical evidence and frozen source integrity; the approved calibration `fortsatt i bruk om lag to og et halvt år senere`.

**Do not reopen:** preservation fields or logs, `decision_signal`, `krav_framing`, final-versus-strategy comparators, numeric quality judges, length or density targets, AI-detector optimization, best-of-N, automatic model orchestration, additional semantic stages, PDF repair as a semantic concern, or a knowledge graph over the authorities.

**One conflict you must not resolve alone.** `ENH-05` describes the forecasting work as a "self-developed python repository", while `Work §4.5` records distributed authorship — a coworker created the original XGBoost and much of the feature work. That touches a factual nugget, which is user-owned. Raise it as an open question; do not reconcile it silently in either direction.

## 5. Vigilance, bounded

Keep looking for substantial net-positive improvements while you verify and cross-reference — especially in evidence selection against the employer's actual decision, category legibility and argument depth, CV/letter complementarity, supported strength versus needless caution, instruction salience and ownership, schema/instruction/runtime drift, human effort across the full operator loop, and components still expressing an older semantic design.

**But route every discovery through the register in §0.** Record it, disposition it, move on. If a discovery would change a decision you already made, that is the one legitimate reason to reopen — do so once, note it, and continue.

Retain only findings that survive an explicit value-versus-cost challenge, and record what you rejected. Do not pad the accepted list to look thorough.

## 6. Read-only discipline

Do not modify `Build`, `Architecture`, authorities, historical runs or pilot records. Do not run `freeze`, `branch`, a semantic stage, `finalize` or `render`.

Verify side effects before treating anything as read-only: `status` rewrites `generated/views/<run>/status.json` and `queue.md` even with `--json`, and `context` writes a handoff and return directory. `next` and `verify-integrity` are genuinely read-only. Use disposable copies outside `Build` where necessary; build no persistent audit harness.

## 7. Deliverables — exactly two

1. `P0.9/Process/optimization_0.9.3/P0.9.3_FINAL_SEMANTIC_PLAN.md`
2. `P0.9/Process/optimization_0.9.3/P0.9.3_FINAL_OPERATIONAL_PLAN.md`

Each must be **standalone**: executable by a fresh implementing model holding that one file and the repository, with no reference to any superseded document and no need to combine plans and diffs. Supersede the existing documents; do not edit them.

Each must specify: exact files and existing section selectors; the current wording to be replaced and its complete replacement text, or concrete code behaviour; target interactions; coherent clusters in execution order with only necessary batched verification; necessary test and fixture changes with the reason an existing test cannot cover each one; exact run commands and parent/source selection; finalize, render and status behaviour; output locations; explicit STOP conditions. *"Improve X"* or *"review Y"* is not an implementation instruction.

Require the implementing model to fix and complete the preceding implementation before new work, to incorporate a later finding at the location of the earlier fix it changes, to preserve supported persuasive strength and Stage-3 freedom, to work in large clusters, and to implement nothing rejected.

**Carry the reasoning, not just the instructions.** Inside these two documents, preserve: observations, causal hypotheses, assumptions, uncertainty, alternatives considered, rejected approaches with reasons, promising unadopted ideas, and what evidence would change each recommendation. Mark what is verified, what is inferred and what is editorial judgment. Concise reasoning summaries, not private chain-of-thought. **Create no separate reflections or register file** — that material lives beside the decisions it explains.

Include the full adjudication table: every item from §4's ten registers, its disposition, and one line of reasoning.

## 8. Stopping test — objective, not aesthetic

You are done when all five hold:

1. Every item in §4's ten registers has exactly one recorded disposition.
2. The Stage-2 decision is made, and every consequence of it is reflected in both documents — including relocation of the base plan's Stage-2 edits if it is cut.
3. Both documents are internally consistent and mutually consistent: no contradictory commands, scope rules or assumptions; no operational feature crossing the one-chat-per-stage boundary; no semantic restriction added merely to simplify orchestration; no dependency on unavailable attachments.
4. Every accepted change belongs to a named cluster with an execution position and a concrete output benefit.
5. Open questions are limited to decisions that genuinely require the user.

When those five hold, **STOP**. Do not add a further pass because the plan could be marginally better. It always could.

## 9. Chat output

Return only: your Stage-2 decision and its single strongest justification; the most consequential dispositions, including anything where you overruled the consolidated input; any remaining feasibility concern with the operational capabilities and your recommended version; genuine user decisions; and links to the two final documents.

Make routine judgment calls yourself and state them. Do not ask whether to proceed. Complete both documents, then STOP.
