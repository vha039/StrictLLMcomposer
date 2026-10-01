/GOAL

You are GPT-6 Astra (Extra High), reviewing an implementation another model
(Claude Opus 5, Extra) just completed. Your job is to validate that work, find
and fix what is actually wrong, and finish. This is an ED-phase validation pass,
not pre-production hardening. Productivity and completion matter: a clean
happy-path exercise plus correct-looking code is sufficient evidence of success
at this stage.

## Working environment

Repository R: `C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26`
Build B: `R\P0.9\Build`

Use PowerShell, UTF-8, and `B\.venv\Scripts\python.exe` / `B\.venv\Scripts\jobbsok.exe`.
Run commands from B unless a path says otherwise. Python is 3.14, pytest 9.1.1.
Do not inventory `.venv`, `__pycache__` or `.pytest_cache`.

**There is no git in this repository.** There is no diff to review against and
`git diff` will not work. Review the current files directly.

**Encoding trap that cost the previous model several cycles:** this shell
mangles non-ASCII characters and backslash escapes inside heredocs. When you
need a script containing Norwegian text, `\n`, or `\r\n`, write it to a file
first and run the file. Do not pipe it through a heredoc.

## The only authorities

1. `R\P0.9\Process\optimization_0.9.3\P0.9.3_FINAL_SEMANTIC_PLAN.md`
   (SHA-256 `fa7284bb2a558cfc8f1eba563da064dd3ec6297d166f9dacf9390c6cef96ce38`)
2. `R\P0.9\Process\optimization_0.9.3\P0.9.3_FINAL_OPERATIONAL_PLAN.md`
   (SHA-256 `eb731b73a36cfc7b36eee80cb3f325b5c8f2cd466e99af00a7351797db3fc38f`)

Read both completely before judging anything. Verify those fingerprints first;
if they differ, the plans changed and your review baseline is different from the
implementation's.

The work record is `R\P0.9\Process\optimization_0.9.3\build.md` — 419 change
rows, all marked VERIFIED/MATCHED, plus nine boundary checks and an observations
table. **It is disposable agent memory, not authority and not evidence.** Use it
as an index into what was claimed and where, then check the claim against the
actual file. A row marked VERIFIED is a claim, not a proof. Runtime, schemas,
config and tests must never read it.

Do **not** read: `P0.9.3_CONSOLIDATED_FINAL_INPUT.md`,
`P0.9.3_REVIEW_AND_IMPLEMENTATION_PLAN.md`, `User required optimizations.md`,
`IDENTIFIED_FRAMEWORK_ENHANCEMENTS.md`, `User clarifications…`,
`P0.9.3_CLAUDE_REVIEW_AND_PLAN_DIFF.md`, `FINAL_ITERATION_PROMPT.md`,
`P0.9.3_ISSUE_LIST_CLAUDE.md`, the High-value_context files, `P0.7/**`,
`P0.9/archive/`, `P0.9/build archive/`, or `Build/tmp/`. The adjudication
register inside the semantic plan is closed: use its dispositions, never reopen
them.

## What was implemented

Two plans, executed as clusters S0/O0 → semantic S1 → semantic S2 → operational
O1 → O2 → O3 → O4. In one sentence each:

- **S0/O0** — an explicit P0.9.3 amendment appended once to the normative
  specification and the implementation contract; root `AGENTS.md` frontier and
  source-maintenance sentence updated; D/K/V and S1/S3 front matter set to 0.9.3.
- **S1** — confirmed candidate facts applied across `authorities/` (2027
  budgeting arc, PRJ-06 completion/controller handover, the AI-superuser
  designation, Alberta English 30-1), retired prescriptions removed, surgical
  replacements in doctrine/persuasion/voice.
- **S2** — named section bodies deleted with all ATX headings and order
  preserved; 60 ranking/CLM rows removed from the ten `W §4` records; the
  personality profile reduced to §§0/1/4/7; three agent-maintained digest tables
  authored; keyword references repaired; `CV_BASELINE.md` derivation hashes
  refreshed; `index build` run once; both stage instructions fully replaced;
  operator prompts and three mirrors updated.
- **O1** — Stage 2 retired for new runs: two fixed revision interpretations
  selected from each run's own manifest, live schemas/bindings/staleness/queue/
  branch migrated to Stage 1 → Stage 3, legacy 0.9.0 behaviour preserved.
- **O2** — `runtime/tools/fetch.py` plus shared frozen-slice/search helpers in
  `evidence_index.py`; the new context bundle (mandatory full Stage-1
  authorities, Stage-3 digests, baseline projection for both stages, rasterized
  vacancy pages).
- **O3** — `--from-stage 1|3`, `--model-tag`, one-level nested branch references
  through seven schemas and the generated-path consumers, full ACC-03 ancestor
  protection, goal prompts and recovery wording.
- **O4** — fixture/test adaptation plus five new behaviour cases; one batched
  suite run.

Recorded evidence at handover: full suite **262 passed, 0 failed, 0 skipped**
(Word COM is available on this machine, so the render gates actually ran rather
than skipping — the historical baseline was 247 pass / 10 skip); the prescribed
read-only legacy probe reports `legacy current artifacts preserved` for both
CORE jobs of `r20260905-005939-3eeb10`; `verify-integrity` on that run passes;
the three mirrors match by SHA-256.

**Two defects were found and fixed immediately before handover** — treat them as
evidence that this class of error exists rather than as the last of them:

1. `cmd_validate` called `evaluate_staleness()` without `spec_revision`, so a
   legacy 0.9.0 run would have been evaluated with the new binding table.
   Fixed by passing `manifest["spec_revision"]`.
2. `_vacancy_pages` ran for legacy runs too, adding a 0.9.3-only key to the
   historical bundle and writing new PNGs into a historical run's `derived/`.
   Fixed by gating it behind `not legacy`.

## Your mandate

1. **Validate the implementation** against both plans: exact replacement blocks,
   named removals, preserved interactions, emitted interfaces, mirrors and
   concrete code behaviour.
2. **Find and fix issues, bugs and faulty or clearly sub-optimal code**, strictly
   within the bounds of the plans. Outside those bounds you may make
   optimizations only if they are: decided up front (you state exactly what you
   will do before doing it), clearly bounded, minimal, extremely high confidence
   and high value. Anything else is recorded, not implemented.
3. **Hunt for blockers** — defects that would break the next authorized step
   (the two-stage semantic run described in SEM §6 / OPS §8). Where you can
   define a clean bounded fix, implement it. Where you cannot, state the exact
   dependency and stop expanding.
4. **Stay productive.** Do not re-derive the design, re-adjudicate settled
   decisions, or re-verify what a passing happy path already demonstrates. Avoid
   duplicating the previous model's checks: read what it claims, then spot-check
   the claim rather than rebuilding the whole verification.

### Mode switching

Choose your depth per area by expected value — roughly P(error) × cost(error),
with honest diminishing returns. Spend your compute where that product is
largest, not evenly.

- **Shallow** (default): read the code, confirm it looks correct, exercise the
  obvious failure modes, move on. If the happy path works and the code reads
  correctly, that is a pass at this stage. Use this for mechanical edits,
  one-line constants, text replacements and anything the suite already covers
  end to end.
- **Deep**: reserved for the broadest, highest-risk surfaces. Reason about
  higher-order effects, comorbid failures, multivariate interactions and
  non-linear behaviour; trace multi-file interactions and call sequences; check
  compatibility across the two revision interpretations; think about what
  happens on the second and third invocation, not just the first. Use it on the
  ranked list below and anywhere your own reading raises the error probability.

Switch modes mid-file when the evidence justifies it. Announce a switch to deep
in one line so the reasoning is auditable.

## Ranked low-confidence areas — where to look hardest

Ranked by the previous model's own assessment of P(error) × cost(error). Items
1–5 deserve deep mode.

1. **Hand-rolled parsers in `runtime/jobbsok/evidence_index.py`.**
   `_table_rows`, `parse_section_refs`, `_matches_ref`, `ids_for_refs`,
   `keyword_table_ids`, `search` and `digest_rows` are all new, and were tested
   against only a handful of inputs. Specific untested edges: escaped pipes
   inside a real source cell; unbalanced or nested parentheses in a `Hent` cell;
   an en dash appearing in prose rather than as a range; a table whose rows are
   preceded or followed by other pipe-leading text; a range whose endpoints have
   different depths; `§§0–1` style integer ranges including section 0. The
   `stripped[1:-1] if stripped.endswith("|") else stripped[1:]` slice in
   `_table_rows` and the index arithmetic that follows it deserve a careful read.
   Verify against the actual retained `§0.4` tables in all three authorities,
   not against invented input.

2. **The legacy 0.9.0 branch of `cmd_context` is entirely unexercised.**
   No test freezes a 0.9.0 run, and the previous model deliberately never called
   `context` against the historical run because `context` writes. So that whole
   payload path is proofread-only, and it is exactly the compatibility promise
   the migration rests on. If you can exercise it safely — for example by
   copying a historical run into a disposable layout outside `runs/` and running
   `context` there — that is high-value. **Do not run `context` or `status`
   against a real historical run in place.**

3. **Digest table content fidelity (RP-03).** The three tables under `W §0.3`,
   `O §0.2` and `E §0.5` were authored by hand. Every `Can prove` and
   `Live ceilings` cell must be supported by that row's exact non-recursive
   section span — not by a child section, not by the file as a whole. One known
   soft spot: the `W §1.1` row uses lifecycle `IN_USE` for an employment record,
   where the plan says non-project records copy the source's actual status or use
   `not applicable`; a controlled project-lifecycle token may be the wrong choice
   there. Check the `O §6.7` row too: it exists only because a factual ceiling
   survived the authorized deletion.

4. **Byte-exact fidelity of the quoted `~~~text` blocks.** The previous model
   verified that each block is *present*, not that it matches the plan
   character for character. Diff the plan's fenced blocks against the files for:
   the S0 amendment (in both Architecture files), the complete Stage-1
   instruction, the Stage-3 replacement body, the Stage-3 `## Completion and
   continuation` tail, the I-6 Norwegian block (which appears twice in
   `Other_high_value_information.md` — once as prose, once flattened into a table
   cell), the D `Integrert bevisenhet` replacement, and the K insertions.
   The Stage-3 `## Final polish — content lock` block must be byte-identical to
   the pre-edit original; its recorded SHA-256 is
   `5da7615e0301271c1df051a88d1684134bf2198b88e65119a965b1ccb6199be7` over 2103
   bytes, measured from the heading to the byte before `## Completion`.

5. **`runtime/jobbsok/branch.py` disposition and rebind interaction.** Reason
   about combinations rather than the single path the tests cover: a legacy
   parent plus `--from-stage`; a parent whose strategy is ABSENT but whose final
   exists; branch-of-branch with `--from-stage 1`; two branches created inside
   the same UTC second (the destination component has one-second resolution, and
   the existing duplicate-destination refusal is the only guard); `REGENERATE_REQUIRED`
   ordering versus the `DEPENDENCIES` check versus the `rebound` dict that the
   final's rebind reads. Also confirm the ACC-03 ancestor snapshot really is
   taken before staging and compared before `staging.rename(final)`.

6. **Revision-selection defaults are a trap.** `evaluate_staleness(...,
   spec_revision=None)` and `status.next_job(..., spec_revision=None)` both
   default to *new* behaviour when the argument is omitted. One caller had
   already been missed (fixed above). Grep every call site of both functions and
   of `active_artifacts`, `upstream_binding`, `stale_scope_table` and
   `writing_policy_records`, and confirm each one passes the run's own manifest
   revision. Consider whether making the parameter required is a bounded,
   high-confidence improvement; if you think so, decide it up front and do it in
   one pass including the test call sites.

7. **`_add_retrieval_payload` shape and cost.** It emits all 144 evidence IDs,
   the Stage-3 digests, the mandatory refs, `optional_source_access` and the
   inline baseline projection with every default bullet. Confirm the bundle is
   well-formed, that no emitted path escapes the run directory, that Stage 1 gets
   `read.authorities` while Stage 3 does not, and that nothing in the payload
   silently caps or truncates a source the plan requires read in full.

8. **`vacancy.render_source_pages`.** Only ever run against a synthetic two-page
   PDF built inside a test. The unlink-then-regenerate semantics, the behaviour
   when `derived/` already holds unrelated files, and the failure surface when
   PyMuPDF raises are proofread-only.

9. **`runtime/tools/vertical_slice.py`.** Edited to the 1 → 3 sequence and never
   executed — correctly, because the plan does not authorize running it against
   Build/evidence. It is pure proofreading. If you run it, use a disposable
   working directory.

10. **Adapted test semantics.** Several assertions were rewritten; the risk is an
    adapted test that now asserts something weaker than it used to. Look
    specifically at: the t05 stale-handoff case (a Stage-3 context refusal became
    an expected re-offer after the strategy was replaced — confirm that is
    genuinely correct behaviour and not a weakened test), the t01 ACC-03
    assertion (now permits additions under `branches/`), and the t23 stage loop.

11. **The `## Goal scope` section added to `prompts/STAGE1_PROMPT.md`.** The plan
    says to use "the same scope paragraph" from OPS §6.2; the previous model
    wrote a condensed paraphrase rather than lifting the paragraph verbatim.
    Judge whether that satisfies the clause.

12. **`AGENTS.md` "Start here" pointer.** The plan specified only the active-task
    frontier sentence and the source-maintenance sentence, and said "No other
    root-document cleanup". The previous model also repointed the adjacent
    "Start here for that task" line from the superseded roadmap to the two
    P0.9.3 plans, on the grounds that the old pointer became false. Confirm you
    agree, or revert it.

## Operating rules you must not break

- **No real-run semantic work.** Do not execute a semantic stage, a treatment, a
  production freeze/branch, or a real-run `stage-submit`/`finalize`/`render`. Do
  not author a job package. SEM §6 and OPS §8 require separate authorization
  that this prompt does not grant.
- **`status` (including `--json`) and `context` write.** `next` and
  `verify-integrity` are read-only. Never point a writing command at a real
  historical run. To inspect legacy behaviour use the read-only probe in OPS §7,
  or a disposable copy.
- **Preserve historical and frozen data.** `runs/**` frozen bytes, manifests,
  render receipts and the eight historical frozen Stage-2 instruction copies stay
  exactly as they are. `P0.9/Process/operator_prompts/STAGE2_PROMPT.md` (v1) is
  deliberately preserved.
- **Do not edit either plan** and do not reopen the adjudication register.
- **The deferred factual question stays deferred**: the "self-developed
  forecasting repository" authorship versus the existing coworker/coding-agent
  attribution in `W §4.5` is the user's to answer. Do not choose it.
- **Do not touch** `MAX_PATH_CHARS`, `render_output_paths`, the Word COM path,
  fonts or templates. Do not add a dependency engine, a version framework, an
  orchestration layer, a configuration surface, defensive scaffolding, a second
  tracker, a progress file or a new test file. Do not broaden QA gates.
- **Model identity is not stage configuration.** You are the reviewing model;
  that does not change `SOL_CLASS` or any configured stage mapping.
- **The separate-instance-and-chat boundary between semantic stages 1 and 3 is
  immutable.**

## Things worth knowing before you start

- **If you change any of the three authority files** (`Work_experience.md`,
  `Education.md`, `Other_high_value_information.md`), you must refresh the three
  derivation hashes in `authorities/CV_BASELINE.md` and re-run
  `.\.venv\Scripts\jobbsok.exe index build`. Freeze and branch both call a
  reconciliation that fails on a stale baseline hash, so skipping this breaks the
  suite in a way that looks unrelated.
- **If you change `prompts/STAGE1_PROMPT.md`, `prompts/STAGE3_PROMPT.md` or
  `policy/writing/FORFATTERSTEMME.md`**, recopy them byte-for-byte to
  `R\P0.9\Process\operator_prompts\v2\`. Exactly three active mirror pairs exist;
  current hashes are `8e39f0f0…`, `d58be16a…` and `939951733…`.
- **Two different hashes exist and must stay different** (RP-06):
  `RunContext.stage_instruction_sha256` is the raw frozen instruction *file* SHA
  recorded in artifact bindings; `FrozenRunAssets.stage_policy_sha256` is the
  combined instruction + selected policies + role + configured model (+ Stage-1
  profile/facets) used in the handoff envelope. Do not merge or rename them.
- **`write.allowed` and `write.semantic_fields` are both real and both required**
  (RP-10). An earlier planning note calling `semantic_fields` a mistake was
  itself the mistake.
- **Path budget**: `MAX_PATH_CHARS = 240` is deliberately unchanged, so under a
  deep temporary root a nested branch reference can exhaust it and `render`
  refuses with "too deep to hold a usable output name". That is the guard
  working, not a bug. On the real machine the same path is roughly 233
  characters.
- **`--dest` on `render` is an explicit non-authoritative export**: it writes no
  canonical receipt. That surprised the previous model; do not read a missing
  receipt after `--dest` as a defect.
- The suite is `.\.venv\Scripts\python.exe -m pytest runtime/tests -q` from B and
  takes about four minutes. Run it once at the end of your changes, not per edit.
  Rerun only what a repair invalidates.
- The previous model left a disposable 286-check cross-reference script under its
  own temp scratchpad. Do not depend on it existing; if you want that breadth,
  derive your own checks from the plans.

## Deliverable

Work in coherent batches. For anything you change:

- Update the affected `build.md` rows in place — state, target evidence, and the
  check result with its real limitation. Keep the existing state vocabulary
  (TODO → IN_PROGRESS → APPLIED → VERIFIED; BLOCKED for a real dependency) and
  the MATCHED/GAP final cross-check. Add new findings you deliberately did not
  act on to the Observations table as LEFT_ALONE. Do not create a second record.
- If you find a claim in `build.md` that the repository does not support, mark
  that row GAP with the evidence, fix it, then re-mark it — do not quietly
  correct the prose.

Finish with a short report: what you validated and at what depth, every defect
found with its severity and disposition, every fix applied, anything you
deliberately left alone, the actual check results with their limitations, and
whether the codebase is ready for the separately authorized two-stage semantic
run. If you hit a genuine blocker, complete the independent work first, then
state the precise missing input. Never report success you did not observe.
