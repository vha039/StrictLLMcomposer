# User-required operational expansions — implementation plan

Written 2026-09-06. Status: PLAN ONLY. Nothing here was implemented and no treatment was executed.

This document is standalone. It requires the repository and nothing else — no external master or execution document. It specifies two capabilities:

- **§A — stage-bound goal operation**, as an alternative to cluster-bounded work.
- **§B — stage-specific branching and deliberate stage redo**, with branches stored inside the source run.

Aliases: **R** = `C:/Users/veggi/OneDrive/Documents/Codex/Jobbsøk_26`, **B** = `R/P0.9/Build`. Unqualified module names are under `B/runtime/jobbsok/`. **N** = `R/P0.9/Architecture/P0.9_FINAL_NORMATIVE_SPECIFICATION.md`, **C** = `R/P0.9/Architecture/P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md`.

**Immutable throughout:** one instance and one chat per semantic stage. Neither capability may be used to author two different stages in one chat. Stage-3 finalization and rendering are deterministic production owned by the same Stage-3 task and are not a fourth stage.

## §0. What already exists, verified

Establishing this first prevents building machinery for a capability the repository already has.

| Behaviour | Current state | Evidence |
|---|---|---|
| Queue scope wider than one cluster | **Already supported.** `--cluster` is optional and defaults to `None`; `next_job` skips the cluster filter when it is falsy. `next --run R --stage 3` already walks the whole run. | `cli.py:1217` `nx.add_argument("--cluster", default=None)`; `status.py:439-440` |
| Resume after interruption | **Already correct by design.** `next` derives from disk with no session memory. | `status.py:427-435`: "Continuation is derived from current disk state. Remembered chat position is never authoritative." |
| Loop until exhausted | **Already in the operator prompts.** "Repeat until `next` reports nothing outstanding." | `B/prompts/STAGE2_PROMPT.md`, `STAGE3_PROMPT.md`, vacancy-loop sections |
| `next` writes nothing | **Confirmed read-only.** `cmd_next` derives status in memory and prints. | `cli.py:901-934` |
| Blocked jobs skipped, peers continue | **Already correct.** | `status.py:447-448` |
| `status --json` is read-only | **False.** It rewrites `generated/views/<run_id>/status.json` and `queue.md` even with `--json`. | `cli.py:874-880` |
| Redo a completed stage | **Not supported.** `next --stage 3` returns a job only when `highest_valid_stage == "DRAFT"`. A job at `FINAL` is unreachable from that queue. | `status.py:437` `wanted = {1: (None,), 2: ("STRATEGY",), 3: ("DRAFT",)}` |
| Branch that regenerates a chosen stage | **Not supported.** Artifacts are reused whenever their governing frozen inputs match; with unchanged policy, all four are `REUSED` and the child has nothing outstanding. | `branch.py:263-282`, `CONTENT_GOVERNING`, `DEPENDENCIES` at `:53-88` |
| Nested run addressing | **Blocked.** `Layout.run_dir` passes `run_id` through `require_safe_component`, which rejects `/` and `\`. | `paths.py` `run_dir`, `require_safe_component` |
| Parent tree unchanged during branch | **Enforced by whole-tree byte comparison.** Every file under the parent is hashed before and after; any new path is an `ACC-03` violation. | `branch.py:181-185` and `:334-348` |

**Consequence.** §A needs no repository change at all. §B needs two changes, one of which is three lines.

## §A — Stage-bound goal operation

### A.1 What the user asked for, and what is actually missing

The requested experience is: set a goal, and an agent continues through the eligible queue until every job in its stage and scope is processed, across one run or an explicitly named set of runs, with one chat still bound to one stage.

Every mechanical element of that already exists. The loop is in the operator prompts, the scope widening is a defaulted argument, and resumption is guaranteed because `next` reads disk rather than memory. **What is missing is not machinery. It is a prompt that states the scope, the stopping rule and the honest completion condition — and, outside this repository, a host facility that keeps re-invoking the agent.**

I cannot verify from this repository whether the operator's host provides a persistent goal facility, a `/GOAL` command or any equivalent. That is a host property, not a repository property. The design below is therefore written so it works either way: with a host goal facility it runs unattended; without one, the same prompt works as an ordinary long-running task instruction, because every wake-up re-derives position from `next`.

**Recommendation: implement §A as an operator-prompt mode only. Add no CLI option, no scope file, no progress record.** A multi-value `--run` was considered and rejected in A.6.

### A.2 Scope semantics

A goal is defined by exactly three things:

1. **One stage.** `--stage 1`, `2` or `3`. Never two.
2. **A run list.** One run id, or an explicitly ordered list of run ids. Never "all runs"; never discovered by globbing.
3. **An optional cluster filter.** Omitted means the whole run, which is the "alternative to clusters" the request asks for. A cluster may still be named when the human wants the narrower scope.

Scope is fixed when the goal is set. An agent may not add a run, widen a cluster, or move to another stage because the queue emptied.

### A.3 The loop

For each run in the stated order, in order:

~~~powershell
.\.venv\Scripts\jobbsok.exe next --run <run_id> --stage <N>
~~~

Add `--cluster <name>` only if the goal named one. Then, for the job `next` returns:

~~~powershell
.\.venv\Scripts\jobbsok.exe context --run <run_id> --job <job_id> --stage <N>
~~~

Reset completely to that bundle, author only the fields it names, and execute its printed `submission.command` verbatim. For Stage 3, immediately run that job's `finalize` and `render` before asking `next` again. Then call `next` again for the same run. When it prints `Nothing outstanding for that selection.`, move to the next run in the list. When the last run is exhausted, the loop is over.

`context` writes a handoff and a return directory; that is ordinary working behaviour, not a violation.

### A.4 Completion, blocked work and honest reporting

`next` returning nothing means **no job is currently eligible for that stage in that scope**. It does **not** mean every job succeeded. Two states are invisible to it:

- `BLOCKED_MANUAL` jobs, skipped at `status.py:447-448`;
- `EXCEPTION` jobs, skipped at `:441-442`.

A goal is therefore reported in one of three ways, and the agent must distinguish them:

| Outcome | Condition | Report |
|---|---|---|
| **Complete** | Every run's queue is empty and no job in scope is `BLOCKED_MANUAL` | Stage N finished for the named scope. List the jobs processed. |
| **Complete with exclusions** | Queues empty, but one or more jobs are `BLOCKED_MANUAL` or `EXCEPTION` | Name each excluded job and its recorded reason. State that the goal cannot complete for those jobs without a human decision. Do not call this success. |
| **Halted** | Run integrity failed, a source could not be read, or `context` refused for a reason the bundle's `Recovery` block does not resolve | Stop that run, report the exact refusal, continue with remaining runs only if the failure is job-local. |

To enumerate blocked jobs at the end without pretending a command is read-only, read the failure records directly:

~~~powershell
Get-ChildItem "runs\<run_id>\jobs\*\failure.json" | ForEach-Object { $_.FullName }
~~~

or accept that `status --run <run_id> --json` is an ordinary working command that refreshes disposable views. Either is legitimate; the second is easier and its write is disposable. What is not legitimate is describing `status` as read-only.

**Three prohibitions.** Successful processing is never defined as `READY` — triage is the model's honest judgment of remaining repair, and forcing `READY` to satisfy a goal corrupts the one signal the human relies on. A goal is never marked complete while required work is blocked. A host goal facility is never treated as permission to author a second stage in the same chat.

### A.5 Ready-to-use goal prompts

Substitute the bracketed values. These are complete; they assume no host feature beyond re-invoking the agent.

**Stage 1:**

~~~text
Goal: run Stage 1 to completion for every eligible job in run <RUN_ID>.
Working directory: C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build

This chat is bound to Stage 1 only. Never request context for another stage.

Loop:
1. .\.venv\Scripts\jobbsok.exe next --run <RUN_ID> --stage 1
2. If it prints "Nothing outstanding for that selection.", go to Finish.
3. .\.venv\Scripts\jobbsok.exe context --run <RUN_ID> --job <job_id> --stage 1
4. Reset fully to that bundle. Read every input it names. If the job carries
   requires_source_inspection, open the original vacancy and disregard any
   platform summary, match score or application tips.
5. Follow the frozen instruction the bundle names in read.stage_instruction.
   Write only write.semantic_fields to write.return_paths.
6. Execute the printed submission.command verbatim.
7. Return to step 1.

Finish: report each job processed. Then list any job in this run whose
failure.json shows BLOCKED_MANUAL, or which is EXCEPTION, and state that the
goal cannot complete for those without a human decision. Do not claim success
for excluded jobs. Do not proceed to Stage 2.
~~~

**Stage 2:** identical with `--stage 2`, and step 5 reading "Author the complete package through the routing and composition order in the frozen Stage-2 instruction."

**Stage 3, one run:**

~~~text
Goal: run Stage 3 to completion for every eligible job in run <RUN_ID>.
Working directory: C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build

This chat is bound to Stage 3 only. finalize and render belong to this stage
and are not a separate stage.

Loop:
1. .\.venv\Scripts\jobbsok.exe next --run <RUN_ID> --stage 3
2. If it prints "Nothing outstanding for that selection.", go to Finish.
3. .\.venv\Scripts\jobbsok.exe context --run <RUN_ID> --job <job_id> --stage 3
4. Obey handoff.mode. In REVIEW_ONLY, author only the review and do not touch
   the existing final.
5. Ground provisionally from the vacancy and the factual authorities, then read
   upstream as option value. Reconstruct elastically. Repair any unsupported
   proposition before fixing content, then apply the content lock.
6. Execute the printed submission.command verbatim, with both return files when
   the mode requires them.
7. Immediately, for that same job:
   .\.venv\Scripts\jobbsok.exe finalize --run <RUN_ID> --job <job_id>
   .\.venv\Scripts\jobbsok.exe render   --run <RUN_ID> --job <job_id>
   Run both for READY, CHECK and RERUN alike. A DEGRADED PDF is not a semantic
   failure; note it and continue.
8. Return to step 1.

Finish: report per job the triage, production state, render state and output
paths. List any BLOCKED_MANUAL or EXCEPTION job and state that the goal cannot
complete for it without a human decision.

Never choose READY to satisfy this goal. Triage is your honest judgment of the
repair that remains.
~~~

**Stage 3, several named runs:** the same prompt with step 1 replaced by:

~~~text
1. Process these runs in this exact order: <RUN_A>, <RUN_B>, <RUN_C>.
   For the current run, .\.venv\Scripts\jobbsok.exe next --run <current> --stage 3
   If it prints "Nothing outstanding for that selection.", advance to the next
   run in the list. When the list is exhausted, go to Finish.
~~~

### A.6 Considered and rejected

| Candidate | Why rejected |
|---|---|
| `next --run A --run B` (multi-value) | Saves one line of prompt text and adds an argument shape no other command uses. The prompt already iterates a stated list correctly. Fails MVP-KISS. |
| A `--goal` or `--scope` CLI mode that drives the loop | Would make deterministic code sequence semantic stages, which `N` forbids and which the architecture deliberately excludes. Not proposed. |
| A persisted goal or progress file | Contract §22 prohibits authoritative progress files, and `next` already re-derives position from disk. It would add a second, staler source of truth. |
| Auto-advancing to the next stage when a queue empties | Breaks the immutable one-chat-per-stage rule. |
| A `--include-blocked` flag on `next` | Blocked jobs are blocked pending a human decision; surfacing them in the work queue invites an agent to retry them. Read `failure.json` for reporting instead. |

## §B — Stage-specific branching and deliberate stage redo

### B.1 Recommendation

Two changes, implemented in this order. The first delivers the entire functional capability; the second delivers the requested organisation.

**B.1.1 — `branch --from-stage N`.** Roughly three lines of logic plus one argument. Makes "re-do Stage 3 for all vacancies in run R" work reliably, today, through ordinary branching and ordinary stage execution.

**B.1.2 — the `branches/` namespace inside the source run.** Roughly thirty lines across four modules, plus one narrowly scoped amendment to how `ACC-03` is *proven* (not to what it requires). Delivers the requested storage layout and lineage.

I recommend both. If only one is implemented, it must be B.1.1: the redo capability is the point, and the directory layout is organisation.

### B.2 B.1.1 — `branch --from-stage N`

**Semantics.** In the child, every artifact owned by a stage at or after `N` is marked `REGENERATE_REQUIRED` regardless of governing-input equality. Artifacts owned by earlier stages behave exactly as today: reused when their governing inputs match, regenerated otherwise. Default when the option is omitted: today's behaviour, unchanged.

This distinguishes the two operations the request asks to separate:

- **Branch after a completed stage and continue downstream** — `--from-stage 2` from a run whose Stage 1 is good: strategy is reused, draft and final/review are regenerated.
- **Re-execute a selected stage although valid artifacts exist for it and later** — `--from-stage 3`: strategy and draft reused, final and review regenerated, so `next --stage 3` returns every job.

**Exact implementation.** In `branch.py`, inside the per-artifact loop at `:263-282`, immediately after the `job["job_class"] != "CORE"` branch and **before** the `parent_states` and `_same_governing_inputs` checks:

~~~python
                if from_stage is not None and ARTIFACT_STAGE[artifact] >= from_stage:
                    states[artifact] = REGENERATE_REQUIRED
                    continue
~~~

`ARTIFACT_STAGE` already exists at `branch.py:79-81`. Position matters: placing it before the dependency check means a forced regeneration is not overridden, and `DEPENDENCIES` at `:83-88` still cascades correctly downward, because `ARTIFACT_FILES` is iterated in dependency order and any artifact that depends on a regenerated one already fails the `any(states.get(dependency) != REUSED ...)` test.

Add the parameter to `branch()` at `:155-161` as `from_stage: int | None = None`, and the argument in `cli.py` beside the existing branch options:

~~~python
    br.add_argument("--from-stage", type=int, choices=[1, 2, 3], default=None,
                    help="Regenerate this stage and everything after it, even "
                         "when the parent's artifacts are valid and its "
                         "governing inputs are unchanged.")
~~~

pass it through in `cmd_branch` at `cli.py:314-316`, and print it in the disposition header so the operator sees which redo was requested.

**Why this is the right shape.** It reuses ordinary branching and ordinary stage execution. It adds no `RERUN` subsystem, no scheduler, no progress file, no dependency engine and no new artifact state — `REGENERATE_REQUIRED` already exists and already means exactly this. The parent is untouched by construction. Downstream currency is automatic: a regenerated artifact is simply not written into the child, so `semantic_state` reports it absent, no `render_report.json` exists in the child, and `out/` is created empty. Nothing stale can appear current.

**Which revision is selected.** Reused artifacts are the parent's `current/` revision, as today; `history/` is not consulted. This is deliberate — the parent's current artifact is the one the human last accepted.

**Frozen versus current governing inputs.** Unchanged: a branch always re-collects the *current* live inputs, `branch.py:189`. That is why a policy change forces regeneration, and it is why `--from-stage 1` is a no-op after a policy edit. `--from-stage` never fabricates a frozen input; it only declines to reuse an artifact.

**Vacancy source identity and lineage.** Unchanged: the child copies the parent's `source/` PDF and `derived/vacancy_normalized.md`, `branch.py:250-259`, and records `parent_run_id`. Original employer documents follow the lineage exactly.

**Deliberately requesting work `next` would otherwise hide.** This is the whole point. After `branch --from-stage 3`, `highest_valid_stage` is `DRAFT`, so `next --stage 3` returns every job. No new flag on `next` is needed and none should be added.

### B.3 B.1.2 — the `branches/` namespace

**Requested layout:** `[run]/branches/[stage_branched_from]_[executing_model]_[date-time_stamp]`.

#### B.3.1 The collision, traced

`branch.py:181-185` snapshots **every file under the parent** and `:334-348` re-hashes them, flagging any path whose hash changed *or which did not exist before* as an `ACC-03` violation. Writing a child into `runs/<parent>/branches/...` makes the post-snapshot contain hundreds of new paths. Every one is reported, `result.ok` is false, the staging directory is deleted and the branch fails.

**This is an implementation-scope problem, not a requirement conflict.** `ACC-03` requires that branching leave the parent's existing content unchanged. An additive, explicitly designated child namespace changes no pre-existing byte. The current proof is stronger than the requirement: it proves *the parent directory has identical contents*, when what must be proven is *no pre-existing parent entry changed*.

**Minimum amendment, stated against the governing ID.** `ACC-03`'s proof is scoped to exclude the designated branch namespace:

~~~python
    def _parent_snapshot() -> dict[str, str]:
        return {
            rel: sha256_file(path)
            for path in sorted(parent_dir.rglob("*")) if path.is_file()
            for rel in (path.relative_to(parent_dir).as_posix(),)
            if not rel.startswith("branches/")
        }
~~~

used for both `parent_before` and `parent_after`. Every pre-existing byte is still proven unchanged; a pre-existing file that *moved into* `branches/` would still be caught, because its old path would vanish from the after-snapshot. This is the narrowest change that admits the namespace.

`verify_frozen` is unaffected: it reads only manifest-recorded frozen inputs, `manifest.py:481-531`, and never walks the run tree. **A nested branch cannot break its parent's `verify-integrity`.** Verified.

#### B.3.2 The path-length constraint decides nesting depth

`paths.py` sets `MAX_PATH_CHARS = 240`, enforced by `resolve_within` and therefore by every `assert_writable` call, including rendered output.

Measured against this repository's actual root (61 characters) and its actual longest artifact name:

| Layout | Longest real path | Result |
|---|---|---|
| Flat run | `runs\<id>\jobs\huseierne_strategi_maalstyring\out\CV_Huseiernes_Landsforbund_Strategi_og_malstyringsradgiver.docx` ≈ 202 | fits |
| One branch level, 29-char branch name | ≈ 231 | fits, 9 characters spare |
| Two branch levels | ≈ 270 | **exceeds the limit; rendering fails** |

**Decision, on evidence rather than taste: exactly one level of nesting.** A branch of a branch is stored under the **root ancestor's** `branches/` directory, while `parent_run_id` in its manifest records its true immediate parent. Lineage stays exact and complete; only the physical depth is bounded.

Because the margin at one level is nine characters, the branch component must be length-bounded. **Specify `MAX_BRANCH_COMPONENT = 32`**, validated when the name is constructed. `stage3_opus5_20260906T101500Z` is 29.

#### B.3.3 Canonical identity and addressing

A run reference is either a plain run id or exactly `<root_run_id>/branches/<branch_name>`.

In `paths.py`, replace `run_dir`'s single-component validation with a reference resolver that accepts those two shapes and validates **each component separately** with the existing `require_safe_component`:

~~~python
    def run_dir(self, run_id: str) -> Path:
        parts = str(run_id).split("/")
        if len(parts) == 1:
            return self.runs / require_safe_component(parts[0], "run_id")
        if len(parts) == 3 and parts[1] == "branches":
            root = require_safe_component(parts[0], "run_id")
            name = require_safe_component(parts[2], "branch name")
            if len(name) > MAX_BRANCH_COMPONENT:
                raise PathSafetyError(
                    f"branch name is longer than {MAX_BRANCH_COMPONENT} "
                    f"characters: {name}"
                )
            return self.runs / root / "branches" / name
        raise PathSafetyError(
            f"run reference must be '<run_id>' or "
            f"'<run_id>/branches/<name>': {run_id!r}"
        )
~~~

Every safety property is preserved: no traversal, no reserved device names, per-component charset, explicit length bound. Only one additional shape is admitted, and it is a literal one — `branches` is a fixed segment, not a wildcard.

Three consequential call sites follow:

1. **Staging path.** `branch.py:226` builds `layout.runs / f".branching-{run_id}"`. With a slashed id this creates an unintended subdirectory. Replace with a flattened token: `f".branching-{run_id.replace('/', '__')}"`.
2. **Derived views.** `cli.py:872` builds `layout.generated / "views" / manifest["run_id"]`. Apply the same flattening so views stay one directory deep.
3. **Known-runs listing.** `manifest.py:472` lists `layout.runs.glob('r*')`. Extend it to append nested branches so a mistyped reference produces a useful error:

~~~python
            f"{', '.join(sorted([p.name for p in layout.runs.glob('r*')] + [f'{p.parent.parent.name}/branches/{p.name}' for p in layout.runs.glob('r*/branches/*')])) or '(none)'}"
~~~

Everything else already addresses runs through `Layout.run_dir` / `load_manifest` and needs no change. `status`, `next`, `context`, `stage-submit`, `finalize`, `render` and `verify-integrity` all accept the branch reference as `--run` once the resolver does.

#### B.3.4 Branch name construction and the model tag

`[stage_branched_from]` is the `--from-stage` value: `stage1`, `stage2`, `stage3`, or `stage0` when `--from-stage` is omitted (an ordinary policy-driven branch).

`[date-time_stamp]` is the branch moment in the existing compact UTC form already used by `make_run_id`, `manifest.py:73-76`.

`[executing_model]` **cannot be determined by deterministic code.** `settings.toml [stages.role_mapping]` records the *configured* model for a capability role, not the model actually driving the session. Presenting the configured value as the executing model would be a false provenance claim inside a filename.

**Design: `--model-tag <tag>`, operator-asserted, validated as a path component.** The agent or human supplies its own identity. When omitted, fall back to the configured role mapping for the target stage and **record in the manifest that the tag was configured rather than asserted**, so the distinction survives. The tag is metadata for human navigation; nothing in the system trusts it.

`cmd_branch` composes and prints the full reference:

~~~text
Child run : r20260905-005939-3eeb10/branches/stage3_opus5_20260906T101500Z
Parent    : r20260905-005939-3eeb10 (untouched)
Redo from : stage 3 (final_package, review regenerated)
~~~

#### B.3.5 What is retained, rebound, excluded and regenerated

Unchanged from current branch behaviour except where `--from-stage` forces regeneration:

| Category | Behaviour |
|---|---|
| Frozen inputs | Re-collected from the **current** live repository, `branch.py:189`. Never copied from the parent. |
| Vacancy source and derived view | Copied from the parent, preserving employer-document identity. |
| Reused artifacts | Rebound to the child: new `run_id`, `manifest_sha256`, `stage_instruction_sha256`, upstream artifact hashes; then re-validated before being written. `branch.py:284-331`. |
| Regenerated artifacts | Not written. The stage authors them normally. |
| `failure.json` | Not copied. A blocked parent job starts clean in the child — this is what makes E2's recovery path work. |
| `out/`, `history/` | Created empty. No stale render receipt or deliverable can appear current. |
| Parent | Byte-identical outside `branches/`, proven by the amended snapshot. |

### B.4 Worked examples

**1. Branch after Stage 1 although Stage 2 and 3 are complete.**

~~~powershell
Set-Location -LiteralPath 'C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build'
.\.venv\Scripts\jobbsok.exe branch --run r20260905-005939-3eeb10 --from-stage 2 --model-tag opus5 --reviewed-by "Vegard Håland"
~~~

Strategy reused; draft, final and review regenerated. Continue with an ordinary Stage-2 chat, then a separate Stage-3 chat.

To rewrite the strategy itself, use `--from-stage 1`.

**2. Redo Stage 3 for every vacancy in one completed run.**

~~~powershell
.\.venv\Scripts\jobbsok.exe branch --run r20260905-115243-93c621 --from-stage 3 --model-tag opus5 --reviewed-by "Vegard Håland"
.\.venv\Scripts\jobbsok.exe verify-integrity --run r20260905-115243-93c621/branches/stage3_opus5_<stamp>
.\.venv\Scripts\jobbsok.exe next --run r20260905-115243-93c621/branches/stage3_opus5_<stamp> --stage 3
~~~

`next` now returns the first job, because final and review are absent. Run the §A.5 Stage-3 goal prompt against that reference.

**3. Redo Stage 3 across several named runs, in one Stage-3 chat.**

Take one branch per source run first — branching is deterministic tooling, not a semantic stage, so this does not violate the stage boundary:

~~~powershell
.\.venv\Scripts\jobbsok.exe branch --run <RUN_A> --from-stage 3 --model-tag opus5 --reviewed-by "Vegard Håland"
.\.venv\Scripts\jobbsok.exe branch --run <RUN_B> --from-stage 3 --model-tag opus5 --reviewed-by "Vegard Håland"
~~~

Then run the multi-run Stage-3 goal prompt from §A.5 over the two printed child references, in the stated order.

**4. Resume an interrupted operation without duplicate or skipped work.**

Re-run `next` for the current run reference. It re-derives from disk: a job whose `stage-submit` succeeded is no longer returned; a job whose submission never landed is returned again. No progress file is consulted and none exists. If the interruption happened between `stage-submit` and `finalize`/`render` in Stage 3, `next` will not return that job — check its `current/` directory for a `render_report.json` and run the two production commands if it is missing.

### B.5 Tests

Add **two** cases to the existing `runtime/tests/test_t01_t04_run_lifecycle.py`, which already exercises `freeze` and `branch` on copied fixtures. No new file, no harness.

1. `--from-stage 3` on a run with all four artifacts valid and unchanged governing inputs: assert `strategy` and `draft_package` are `REUSED`, `final_package` and `review` are `REGENERATE_REQUIRED`, and that `next --stage 3` then returns the job.
2. A branch taken into the `branches/` namespace: assert the parent's pre-existing files are byte-identical afterwards, that the parent's `verify-integrity` still passes, and that `context` resolves against the nested reference.

These resolve concrete uncertainties in changed behaviour, which is the stated bar. Nothing else in the suite changes.

### B.6 Documentation

Add one short `## Redoing a stage` section to `B/policy/RUNBOOK.md` after the branch material, and one line to the E2 recovery paragraph that the base plan rewrites, cross-referencing `--from-stage` as the explicit way to request a redo. No operator prompt needs a semantic change; the Stage-2 and Stage-3 vacancy loops already work unmodified against a branch reference.

### B.7 Considered and rejected

| Candidate | Why rejected |
|---|---|
| A `rerun` command | Contract §22 explicitly prohibits a dedicated `RERUN` subsystem. `--from-stage` reuses ordinary branching and adds no state. |
| `--force` on `next` or `context` to re-open a completed stage | Would let a stage overwrite a valid artifact in place, defeating `INV-09` stage-scoped ownership and the immutability of a committed revision. Branching keeps the parent intact, which is the property that makes redo safe. |
| Deleting the child's `final_package.json` by hand to make `next` return the job | Mutates control state outside the tooling and leaves the manifest disposition lying. Exactly the hand-editing the runbook forbids. |
| Two or more levels of nesting | Measured to exceed `MAX_PATH_CHARS` for real rendered output. Rejected on evidence. |
| Deriving `[executing_model]` from `settings.toml` | Records the configured model, not the executing one. A false provenance claim in a filename is worse than an operator-asserted tag. |
| Relaxing `MAX_PATH_CHARS` instead of bounding nesting | Trades a documented safety bound for directory aesthetics. |
| Weakening `ACC-03` to "the parent's semantic artifacts are unchanged" | Broader than needed. Scoping the *proof* to exclude an additive namespace preserves the full guarantee for every pre-existing byte. |

### B.8 Architecture escalation

One provision requires an amendment, stated precisely:

> **`ACC-03`** — parent-tree immutability during branching. Current implementation proves whole-directory byte identity (`branch.py:181-185`, `:334-348`). Requested nested storage adds files under the parent. **Minimum amendment:** scope the proof to exclude the designated `branches/` namespace, so that every path that existed before the branch is still proven unchanged, and a pre-existing file that disappeared or moved is still caught. The requirement is unchanged; only its proof is scoped. Implement `--from-stage` (B.2) independently of this amendment — it needs no architectural change at all.

`INV-09`, `DEC-38`, the frozen-input contract and the human-approval boundary are untouched by both changes.

## §C. Reconciliation with the semantic plan

Checked against `P0.9.3_REVIEW_AND_IMPLEMENTATION_PLAN.md` and `P0.9.3_CLAUDE_REVIEW_AND_PLAN_DIFF.md`:

- **No contradictory commands.** The base plan's Cluster 3 uses `branch` without `--from-stage`; that remains valid and is a no-op difference there, because the changed writing policies already force full regeneration. The diff document adds a note saying so.
- **No stage-boundary crossing.** `branch` is deterministic tooling and may be run outside a semantic chat. Every goal prompt names exactly one `--stage` and forbids requesting another.
- **No semantic restriction added for orchestration.** Neither capability changes a writing policy, a stage instruction or a claim rule.
- **No hidden dependency on unavailable attachments.** This document cites only repository files.
- **Ordering.** The base plan's Cluster 2 rewrites the recovery text that describes today's friction; §B removes that friction. Implement Cluster 2's wording first, then §B, then add §B's one-line cross-reference. The diff document records the same order.
- **`status --json` is described identically in both documents** as an ordinary working command that refreshes disposable views.

## §D. Decisions taken, and the two that are genuinely the user's

**Taken here, stated rather than deferred:** one nesting level with root-ancestor storage and exact `parent_run_id` lineage; a 32-character branch-component bound; operator-asserted `--model-tag` with a recorded configured fallback; `stage0` for a branch without `--from-stage`; reuse of the parent's `current/` revision rather than `history/`; `next` gains no flag; §A adds no CLI surface.

**Genuinely the user's:**

1. **Whether to implement B.1.2 at all.** `--from-stage` alone delivers the full redo capability with three lines and no architectural amendment. The `branches/` namespace delivers the requested organisation at the cost of ~30 lines across four modules, an `ACC-03` proof-scope amendment, and a permanent one-level nesting limit. Both are sound; the second is organisation rather than capability.
2. **Whether `--model-tag` should be required or optional.** Required makes every branch name honest at the cost of one more argument on every branch. Optional with a configured fallback is more convenient but yields names whose model tag was not asserted by the executing agent. My recommendation is optional-with-fallback, because the manifest records which of the two occurred.
