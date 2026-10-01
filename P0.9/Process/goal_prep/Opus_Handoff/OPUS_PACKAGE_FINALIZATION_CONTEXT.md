# Opus 5 Max — P0.9 Roadmap Package Finalization Context

## 0. Purpose

You are being commissioned as the **final package architect and adversarial remedy adjudicator** immediately before a GPT-5.6 Sol implementation Goal.

The materials supplied to you are **drafts**, including the proposed file set itself.

You are explicitly authorized to:
- rewrite any draft;
- move content between files;
- merge/split/remove/add files;
- alter naming or package topology;
- reject proposed mechanisms;
- change proposed strictness/authority levels;
- replace the draft Goal approach;

**when you are reasonably confident the change improves expected implementation quality, coherence, adaptability, cost or failure resistance.**

Do not preserve our structure merely because effort has already been invested in it.

The one thing to preserve is the real objective: give the implementing Sol agent enough durable structure to finish the P0.9 mechanical baseline correctly, while leaving enough implementation breathing room to exploit its own judgment and current code evidence.

---

## 1. Current project stage

The project has already undergone:

1. frozen P0.9 architecture work;
2. initial implementation;
3. a direct forensic audit;
4. six-model critical review;
5. multi-model reconciliation;
6. an Opus meta-review with additional public-path reproductions;
7. a fresh GPT-5.6 Sol Max `/plan` pass against the actual Build;
8. a further adversarial review of that plan.

The main unknown is no longer “what defects might exist?”

The dominant remaining risk is:

> a sophisticated implementation agent choosing an elegant but subtly wrong remedy, overfitting the plan, or expanding scope while trying to perfect the system.

Therefore your highest-value work is **package/control design and remedy adjudication**, not another wholesale audit.

---

## 2. Draft package supplied

Stable/control draft:
- `AGENTS.md`
- `00_READ_FIRST.md`
- `DESIRED_FINAL_STATE.md`
- `GUIDANCE_INSTRUCTIONS_AND_RULES.md`

Execution/evidence draft:
- `FINAL_EXECUTION_PLAN.md`
- `DEFINITION_OF_DONE.md`
- `EXECUTION_LEDGER.md`

Supporting project evidence:
- current P0.9 Architecture;
- current `P0.9/Build/`;
- expanded multi-model reconciliation;
- source reviews on demand;
- Codex-generated final-perfection plan;
- Sol adversarial review of that plan.

Treat all roadmap files as drafts.

---

## 3. Draft information architecture

The current proposal separates:

- root `AGENTS.md` — durable repository rules/routing;
- `00_READ_FIRST.md` — task router and context-recovery protocol;
- Desired Final State — WHAT must be true;
- Guidance — HOW to reason/choose;
- Execution Plan — preferred HOW to get there;
- Definition of Done — HOW to prove success;
- Execution Ledger — WHERE execution actually is.

The design goal is **one normative owner per kind of truth**.

A lower-level file should reference, not restate, a higher-level rule.

This is a proposal, not a constraint. Alter it if your independent analysis finds a better control architecture.

---

## 4. Strictness is a first-class design decision

The implementing agent must not experience every sentence as equally binding.

You MUST explicitly decide and communicate an optimal strictness/authority model across the final package.

The draft philosophy is:

### Hard limits
Very few.
Examples:
- truth/identity/human irreversible authority;
- no autonomous submission/model orchestration;
- approved Desired Final State;
- approved DoD proof threshold;
- explicit architecture amendments.

### Strong control rules
Rules that should usually govern execution but can have narrowly defined escape behavior.
Examples:
- scope admission;
- no silent architecture deviations;
- repository state outranks stale ledger;
- public-path evidence required for public-path claims.

### Strong priors / preferred route
Examples:
- root-cause phase order;
- preferred resolver/handoff/receipt design;
- suggested branch-hash strategy.

These should steer Sol heavily without becoming brittle scripture.

### Guidance / heuristics
Examples:
- prefer existing machinery;
- prefer mechanically boring solutions;
- avoid generic frameworks;
- targeted tests during edits.

### Drafts / options / inspiration
Mechanism candidates that Sol may replace when current evidence supports something better.

### Evidence / provenance
Review findings, reproductions and rationale. Evidence informs decisions but does not become authority merely by existing.

You are NOT required to keep this exact taxonomy.

Your final package must make the intended adherence level unmistakable.

The objective is:

> **few hard walls + strong direction + explicitly flexible implementation mechanism.**

Too rigid is bad.
Too vague is bad.
Your task is to find the optimum.

---

## 5. High-value current remedy disputes to adjudicate

Do not inherit either Codex’s plan or the Sol plan review mechanically.

### 5.1 Architecture revision strategy
Codex proposed active `0.9.1`.
Concern: simply changing revision fields could strand/misinterpret old frozen `0.9.0` authority or create needless compatibility machinery.

Decide:
- whether a normative revision is actually required;
- how exact old authority is preserved;
- whether old synthetic runs are supported/refused/migrated;
- which revision fields genuinely change.

### 5.2 Binding invariant vs token mechanism
Codex proposed a handoff token.
Underlying required property is deterministic binding ownership/current-at-birth.

Decide whether:
- token is the cleanest implementation;
- another deterministic envelope/current-context check is smaller;
- architecture should specify semantics only.

### 5.3 Render receipt vs review contents
Prior review concluded a current review is probably required to authorize render, but pure review replacement should not automatically stale unchanged employer bytes.

Verify against current architecture and code.
Prevent accidental collapse of semantic/triage/render axes.

### 5.4 Failure scope
Opus previously connected malformed input/date failures into a job-containment root cause.
Codex proposed broad `Exception` containment.

Concern:
- disk full/shared permission/common config/runtime failure may be broader than one job.

Final package should govern failure by scope, not simplistic exception class.

### 5.5 Retry semantics
Verify/falsify whether the implementation/plan risks collapsing:
- one bounded same-session mechanical correction;
- semantic/manual retry/restart.

Preserve their intended distinction if real.

### 5.6 External writes vs source maintenance
Protected run-production writes must be constrained.
But template/source-maintenance tools deliberately modify maintained source assets.

Do not make a “safe write” rule that makes legitimate maintenance impossible.

### 5.7 Word cleanup
Prior evidence showed:
- user Word session survived isolated automation;
- timeout diagnostic overstated cleanup;
- PID-difference cleanup may be useful but is not automatically proof of exact ownership.

Choose the strongest **safe** solution; truthful diagnostics are mandatory.

### 5.8 OOXML anti-regression
Protect the demonstrated property:
- target Word compatibility;
- untouched OOXML parts not accidentally reserialized/normalized.

Do not canonize a library-name ban unless independently justified.

### 5.9 Branch artifact hashing
Your prior meta-review proposed excluding run-specific identity fields from semantic `artifact_hash`; Codex adopted it.

Review your own proposal adversarially.
Inspect every consumer.
Adopt only if wrong-run/job identity remains independently enforced and no legitimate consumer needs run identity inside semantic hash.

### 5.10 Goal boundary
Current recommendation is that the implementation Goal stops at `GO_FOR_TWO_JOB_SMOKE`, not after actually running two real semantic jobs.

Verify whether this best preserves engineering-vs-product evidence separation.

---

## 6. Research you MUST perform independently

Before finalizing the package, perform a fresh current-web research pass relevant to **long-running GPT-5.6 Sol/Codex implementation control**, drawing from both official sources and experienced community/power-user evidence.

Do not merely reproduce our prior search queries or conclusions.

Highest-value information to resolve includes:

1. current behavior and best practice for Goal mode, especially persistence, completion auditing, stop/block conditions and file-referenced objectives;
2. current `AGENTS.md` loading/scoping/precedence and practical instruction-budget considerations;
3. failure modes of long-running Codex tasks under large context, repeated tool output, compaction and task-state recovery;
4. how much instruction specificity improves vs suppresses GPT-5.6 Sol coding performance;
5. evidence on progressive disclosure / repository-local state files / execution plans for long-running agents;
6. current reasoning-effort tradeoffs for GPT-5.6 Sol, particularly XHigh vs Max for a very well-specified but coupled implementation;
7. community evidence on Sol overengineering, repeated test loops, excessive refactors or scope expansion and how power users successfully constrain it;
8. whether multiple roadmap files improve retrieval/continuation or create synchronization/instruction-conflict risk;
9. current behavior around `/review`, plan/goal interaction and resuming after compaction/interruption;
10. cost/context implications of repeatedly rereading large files or logs during long agent runs.

Prior research suggested the following. **Verify or falsify them against current sources rather than assuming them:**

- leaner prompting can outperform more prescriptive prompting on GPT-5.6;
- decision-complete plans need not be implementation-prescriptive;
- progressive disclosure is preferable to giant always-loaded instruction files;
- root `AGENTS.md` should behave like a compact map/control layer, not a task manual;
- repeated accumulated context/tool output can dominate long-run token usage and degrade focus;
- compaction recovery is safer when reconstructed from repository state + compact durable task state rather than conversational memory;
- very high reasoning can increase exploration/overengineering/cost, so XHigh may be a better implementation default than Max for this prepared task;
- Goal stop conditions should live inside the Goal/control contract;
- property-based DoD is safer than “implement this exact class/helper” acceptance;
- targeted verification during edits + full suites at checkpoints is preferable to rerunning everything after every change.

If current evidence points elsewhere, change the package accordingly.

---

## 7. Intended implementing model

Expected implementer:
- GPT-5.6 Sol;
- likely Extra High reasoning rather than Max for the long execution;
- Goal mode;
- full repository access;
- one principal agent owns convergence.

This is a draft recommendation. Reassess it from current evidence.

The implementation package should not depend on hidden conversational context from these review threads.

A freshly resumed implementing agent should be able to reconstruct the task from repository-local control/evidence files.

---

## 8. Package-quality criteria

Your final package should optimize:

### Coherence
No contradictions across files.

### Single ownership
Each normative statement has one clear owner.

### Progressive disclosure
A resumed agent reads only what it needs for the current decision.

### Bounded freedom
Sol can optimize local mechanisms but cannot invent product requirements.

### Finite completion
There is a real stopping point.

### Recoverability
Compaction/interruption does not require conversation memory.

### Evidence discipline
Tests prove properties at the scope claimed.

### Context efficiency
The package does not force repeated ingestion of large reviews/logs.

### Durability
Temporary finalization rules do not accidentally govern later semantic-pilot work.

### Anti-regression
Known beneficial implementation adaptations are protected as properties, not fetishized mechanisms.

---

## 9. Preferred final outputs from you

You may change this set if a different package is clearly better.

Expected final control package:
- final root `AGENTS.md`;
- final package router/index;
- final Desired Final State;
- final guidance/rules;
- final execution plan;
- final Definition of Done;
- initialized execution ledger.

Additionally produce:
- a tiny copy-paste-ready final `/goal` command;
- a compact `PACKAGE_FINALIZATION_NOTES.md` explaining only material changes from the supplied drafts and unresolved user-owned decisions, if any.

Avoid another giant review essay.

The final package itself is the product of your pass.
