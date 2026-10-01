# External review of the P0.9.3 implementation and the Astra validation pass

Reviewer: Claude Opus 5, 2026-09-07. **Read-only review. No repository file was changed by this pass.**
This document is an external report for Vegard. It is **not** a plan, not a tracker, and no runtime,
schema, test or agent may consume it. `build.md` remains the single work record; both master plans
remain the only authorities.

Scope reviewed, oldest to newest: `High-value_context_codex.md`, `P0.9.3_FINAL_SEMANTIC_PLAN.md`
(SEM), `P0.9.3_FINAL_OPERATIONAL_PLAN.md` (OPS), `IMPLEMENTATION_GOAL_PROMPT.md`,
`REVIEW_GOAL_PROMPT_CODEX.md`, `build.md`, then the live repository at
`C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\`.

---

## 1. Verdict

The implementation is **materially complete and materially correct**. The Astra validation pass
**did finish its substantive work** — it found six real defects, fixed all six, verified them, and
wrote a complete closing report into `build.md`. What it did not do is re-run the full suite after
its own repairs. I ran it. It passes.

Nothing I found blocks the separately authorized two-stage semantic run. Four residual items are
worth a decision before you start it; only one of them (F1) can plausibly degrade the output of that
run, and it is a source-content question, not a code defect.

---

## 2. Question 1 — did Astra finish the main work?

**Yes, with one gap that I have now closed.**

What the record and the repository jointly show:

| Astra deliverable | State |
|---|---|
| Read both plans, verified fingerprints | Done; both fingerprints still match the live plan files |
| Deep review of the ranked high-risk areas 1–5 | Done — the `build.md` "Depth" paragraph names each and the fixes land on exactly those surfaces |
| Defects found and fixed | **ASR-01 … ASR-06, all six FIXED and re-verified** |
| Findings deliberately not acted on | **ASR-07 … ASR-11 recorded as LEFT_ALONE with reasons** |
| `build.md` rows updated in place | Done — header/frontier, observations table, closing section |
| Final closing report | **Written in full** as `## Independent ED validation - Astra, 2026-09-07` (13 lines, complete, ends with STOP) |

So the "broke down at the report-writing stage" reading is not what the artifacts show. The report
exists and is coherent. What is missing is narrower and more specific:

> **The one real gap.** Astra's last full-suite run was *before* its repairs: `251 passed, 10 skipped,
> 1 failed (ASR-06)`. After repairing, it re-ran **one single test** and stopped. Its own record says
> so plainly: *"Combined current result: 252 passing cases and 10 COM skips; no second complete rerun
> after that targeted repair."* Between that last full run and the end, it had changed
> `evidence_index.py`, `status.py`, `cli.py`, a test file, and **all three authority files plus
> `CV_BASELINE.md` plus a regenerated index**. That is a wide blast radius to leave unre-tested.

**I closed that gap.** Full suite from `B`, after all six ASR repairs, on the current tree:

```
262 passed in 256.14s (0:04:16)
```

Zero failures, **zero skips** — Word COM was available in my session, so the DOCX *and* PDF render
gates actually executed rather than skipping. That is a wider mechanical scope than Astra's own
session achieved, and it retires ASR-10 ("ten COM cases remain unverified in this review") and the
"PDF conversion remains unverified in this session" limitation from its report.

Two honest caveats on that number. First, the suite must be run from a **short** base temp
directory: my first attempt used the session scratchpad (a deep path) and 36 tests failed on the
deliberately unchanged `MAX_PATH_CHARS = 240` guard — that is OBS-003 firing, not a defect, and the
guard message is correct and legible. Second, a passing suite proves mechanics, not semantics; it
says nothing about evidence selection or interview value.

Astra's other stated limits I verified independently and found accurate: no real run was frozen,
branched, submitted, finalized or rendered; the parent's frozen bytes are intact; both plan
fingerprints are unchanged; the deferred forecasting-authorship question is untouched.

---

## 3. Question 2 — my own review of the codebase

### 3.1 What I verified, and how

Everything below is an actual observed result on the current tree, not a re-reading of `build.md`.

**Plan-text fidelity (byte level).** I extracted all 17 `~~~text` blocks from SEM and searched for
each in the live files. **16 of 17 are byte-exact**, including the 5 681-byte complete Stage-1
instruction and the 7 767-byte Stage-3 replacement body. The 17th (V *Kanalkalibrering*) matches
word-for-word and differs only in line wrapping — exactly as ASR-09 recorded.

- The S0 amendment block is **byte-identical in SEM and OPS**, and appears **verbatim in both**
  `P0.9_FINAL_NORMATIVE_SPECIFICATION.md` and
  `P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md` under the specified heading.
- The Stage-3 `## Final polish — content lock` block is **exactly 2 103 bytes**, SHA-256
  `5da7615e…6199be7` — the recorded pre-edit value. Byte-preservation confirmed.

**Authority integrity.** Diffed all three authorities against their pre-edit frozen copies in
`runs/r20260905-005939-3eeb10/frozen/authorities/`:

- **Every ATX heading in W, E and O is unchanged in text and order.** This is the load-bearing
  requirement of SEM §4.1 — it is what keeps existing EV ordinals stable — and it holds exactly.
- Selection-metadata subtraction is precisely scoped: **exactly 10 removals each** of
  `selection_value`, `best_for_roles`, `role_signals`, `employer_problem_signals`,
  `public_narrative_potential`, `stable_claim_ids` — one per §4 record — and all ten records now
  carry exactly the four retained fields. Nothing beyond the named six was removed.
- Deleted bodies land where specified (W §0.6/§9.1/§9.2; E §0.6; O §0.5, §3.1–3.3, §10) with
  headings retained; O §4.6 and §6.7 keep their surviving factual remainder rather than being
  emptied wholesale.
- The confirmed factual updates are correctly ceilinged. PRJ-03 records hospital-wide 2026/2027 use
  and the narrow sole-coder confirmation (*"gjelder kodeendringene, ikke hele budsjettprosessen"*)
  without asserting earned trust or measured savings; PRJ-06 records completion and controller
  handover while leaving organizational use and benefits unresolved; PRJ-05's ceiling still states
  distributed coworker/AI authorship. **The deferred repository-authorship claim was not added.**

**Digest tables (the RP-03 surface Astra repaired).** I ran the real projector over all three:
**37 rows, 37 resolve to a real evidence ID, zero unresolved.** Coverage matches the plan's
inventory exactly — W 14 rows (ten projects + §1.1 split into three + §1.2), O 14 (including the
conditional §6.7), E 9 (four school records + five course groups). Non-project rows use `not
applicable` or the source's own status; the `IN_USE`-on-an-employment error the review prompt
flagged as a soft spot is gone.

**Hand-rolled parsers (`evidence_index.py`, the #1 risk area).** I exercised `parse_section_refs`,
`_matches_ref`, `ids_for_refs`, `_table_rows` and `keyword_table_ids` against the **actual retained
§0.4 tables in all three authorities**, not invented input: 41 keyword rows, **all parse, all resolve
to at least one ID, zero zero-hit or malformed rows**. Ranges (`§§4.1–4.4`, `§§6.6–6.7`, `§§0–1`,
`§§2.1–2.5`) resolve including interior children; parentheticals and post-semicolon prose are
correctly discarded; `4.1` does not swallow `4.10` (tuple comparison, not string prefix).

**Runtime and revision handling.** I grepped every call site of `active_artifacts`,
`upstream_binding`, `stale_scope_table`, `writing_policy_records`, `evaluate_staleness`,
`next_job` and `semantic_state`. **Every production caller passes the run's own manifest revision**
— `cmd_validate`, `cmd_next`, `cmd_context`, `_record_stage_failure`, `semantic_state`, `branch`.
The "defaults to new behaviour" trap the review prompt warned about has no remaining live instance.
RP-06 holds: `RunContext.stage_instruction_sha256` is still the raw frozen file SHA;
`FrozenRunAssets.stage_policy_sha256` is the separate combined hash. RP-10 holds: `write.allowed`
and `write.semantic_fields` both survive and are both emitted.

**Branch and ACC-03.** The ancestor snapshot is taken before staging, staging happens outside the
ancestor, the whole tree is re-hashed and compared **before** `staging.rename(final)`, and only the
new child destination is added. The combinations the review prompt asked about behave correctly:
absent-strategy-with-present-final degrades to REGENERATE_REQUIRED via both the currentness check
and the dependency check; EXCEPTION jobs never touch `parent_states` (no KeyError); a same-second
duplicate destination is refused by the existing `final.exists()` guard; `rebound` is always
populated before it is read because the dependency gate runs first. All **seven** live schemas plus
`parent_run_id` carry the exact nested run-reference regex from OPS §5.3.

**Legacy preservation.** I extended the prescribed read-only probe beyond the one run Astra checked:
**three historical 0.9.0 runs** (`r20260905-005939-3eeb10`, `r20260902-210926-0d1af3`,
`r20260828-213932-7f13b4`) — all CORE jobs in all three still report all four legacy artifacts
current under the legacy interpretation. `verify-integrity --run r20260905-005939-3eeb10` passes.

**Preconditions for the next step.** `check_index` reports zero violations, the stored index is
byte-reproducible from the current authorities (144 entries), `check_baseline_map` reports zero
violations, and the baseline reconciliation returns **no conflicts** — so `branch` on the intended
parent will not fail on a stale derivation hash. The three mirror pairs match their recorded hashes
(`8e39f0f0…`, `d58be16a…`, `939951733…`). Live Stage-2 files are gone; v1 and **8** historical frozen
copies are intact.

**The t05 question (review item 10).** Not a weakened test. The stale handoff is still refused with
no mutation, no history write and no failure record; the *additional* assertion is that a fresh
Stage-3 context is offered after the strategy was replaced — which is correct, because strategy
replacement stales final and review. Astra's judgment here was right.

### 3.2 Findings

| # | Severity | Finding | Disposition |
|---|---|---|---|
| **F1** | **Medium** | Asymmetric ranking metadata in `Work_experience.md` | Your decision |
| **F2** | Low–Med | Dangling `selection_value` instruction in W §0.5 | Your decision (= ASR-07) |
| **F3** | Low–Med | `PERSONALITY_PROFILE.md` names a retired stage and prescribes a schema-invalid facet shape | Your decision (extends OBS-002) |
| **F4** | Informational | Nested-child render filenames will be digest-compacted | Expectation-setting |
| **F5** | Low | One adapted test still asserts Stage-2 continuation on a 0.9.3 run | Cosmetic |
| **F6** | Low | `digest_rows` silently drops a malformed row | Recorded only |
| **F7** | Informational | RP-03 locator widened beyond the plan's literal wording | Accepted deviation |
| **F8** | Informational | RUNBOOK/STAGE1_PROMPT goal text is not verbatim from OPS §6.2 | Accepted deviation |

---

**F1 — Asymmetric ranking metadata (Medium).**
All ten `W §4` project records were stripped of the six preset ranking fields. The **BAR record**
(`W §1.1` → `#### Tidlig OUS-plassering – Barne- og ungdomsklinikken (BAR)`, ~line 176) still carries
the **full nine-field Selection metadata table**, including:

```
| `selection_value`            | `VERY_HIGH` for finance/process improvement, controller, … |
| `role_signals`               | month-end close, public accounting, periodization, … |
| `public_narrative_potential` | Main or strong second case where finance-process ownership … |
| `interview_defensibility`    | `VERY_HIGH` for the confirmed scope; … |
```

Stage 1 now reads all three authorities **in full** before ranking. Under the new route, the one
record that still asserts its own `VERY_HIGH` value and "main or strong second case" standing is the
BAR record — precisely the preset ranking that register item FLAG-02 removed everywhere else
("Remove the preset ranking row; Stage 1 ranks for the actual vacancy"). The `HIGH/VERY_HIGH`
self-rating prefixes that FLAG-02.interview_defensibility ordered stripped are also still there.

Neither model was wrong to leave it: SEM §5.1's selector says *"each W §4 Selection metadata table"*,
and the BAR record is under §1.1. This is a **scope gap in the plan**, not an implementation defect.
But it is a live selection-bias risk for exactly the run this migration exists to enable, and it is
a five-minute source edit (followed by a `CV_BASELINE` hash refresh and `index build`).

**F2 — Dangling instruction (Low–Medium).** `W §0.5` item 1 still reads
*"Bruk `selection_value` mot arbeidsgiverens faktiske problem…"*. After the §4 subtraction that field
exists on **one** record — the BAR record. So the source's own selection contract now points the
reader at the single place F1 left the ranking. The two compound. (`Education.md §3.0` also uses a
`selection_value` column, but that table is self-contained and internally consistent — leave it.)

**F3 — Personality profile coherence (Low–Medium).** `context/PERSONALITY_PROFILE.md` is a frozen
input **read by Stage 1**. It still names Stage 2 as an active consumer in three places, not the one
OBS-002 recorded:

- line 17 — `restricted_consumers: ["Stage 2 writer: distilled selected-facet guidance only"]`
- line 60 — *"Give the Stage-2 writer only distilled selected-facet guidance…"*
- line 164 — *"Do not pass MBTI/DISC/Enneagram/RIASEC labels to the Stage-2 writer by default."*

More consequential than the stale stage name: **§7's handoff YAML prescribes a facet object that the
strategy schema rejects.** It specifies `status`, `selected_facets[].relevance`,
`desired_recruiter_read`, `prevention_rule`, `channel_guidance`. `strategy.schema.json`
`personality_facets` is `additionalProperties: false` over `facet_id`, `plain_language_label`,
`evidence_refs`, `expression_ceiling`, `vacancy_relevance`, `intended_employer_interpretation`,
`misread_risk`, `expression_guardrail`. A Stage-1 model that follows §7 instead of its own frozen
instruction produces a schema-invalid return.

This is **pre-existing** and explicitly outside every named selector in both plans — neither model
was authorized to touch it. The blast radius is bounded: the Stage-1 instruction is authoritative and
correct, `write.semantic_fields` names the right keys, and validation rejects a wrong shape, so the
worst case is one rejected submission plus a bounded correction cycle. Still, it is the highest-value
remaining cleanup on the model-facing surface.

**F4 — Nested render filenames will be compacted (Informational, but plan the comparison around it).**
I computed this through the real `render_output_paths`, not by estimate. With the exact command SEM §6
prescribes (`--from-stage 1 --model-tag unknown`, component `stage1_unknown_<UTC>` = 31 chars), the
child's `out/` destination is 170–171 characters, leaving a 55–56 character filename budget. Both
jobs exceed it, so the employer/title suffix is truncated and an 8-hex identity digest appended:

```
CV_Huseiernes_Landsforbund_Strategi_5e0f0344.docx     (parent: CV_Huseiernes_Landsforbund_Strategi_og_malstyringsradgiver.docx)
CV_Avinor_AS_Seniorradgiver_Digital_T_16500c77.docx   (parent: CV_Avinor_AS_Seniorradgiver_Digital_Transformasjon.docx)
```

**Render does not refuse** — the guard never fires, the compaction path does, and OPS §5.5 explicitly
blesses that ("A short name produced by the existing function is valid"). Two practical consequences:
SEM §6's human comparison against the parent's `out/` will be comparing differently-named files, and
you must take output paths from the render receipt rather than assuming the old names. A shorter
`--model-tag` (e.g. `opus5`) buys two characters — not enough to avoid compaction.

**F5 — Stale test assertion (Low).** `test_t17_next_job_is_derived_from_current_disk_state`
(`test_t16_t18_containment_template.py:320`) calls `status_module.next_job(status, stage=2)` on a
freshly frozen — therefore 0.9.3 — run. It passes because `next_job`'s internal `wanted` map still
carries a `2:` entry, while the CLI has no `--stage 2`. It asserts nothing false; OPS §7.1 asked for
obsolete active-stage labels to be updated and this one was missed. Cosmetic.

**F6 — Silent row drop (Low).** `evidence_index.digest_rows` discards any row whose cell count is not
five (`if len(row) != len(DIGEST_KEYS): continue`) with no diagnostic. All 37 current rows are
well-formed, and the new context test asserts each source's digest array is non-empty and every
`evidence_id` resolves — so an *empty* digest cannot ship. But a **single** dropped row (one
unescaped pipe added during future source maintenance) would disappear from Stage 3's navigation
silently. Consistent with ED-1 happy-path discipline; recording it so a future maintainer knows.

**F7 — Locator widened (Informational).** OPS §4.2 says a digest row's `Source section` "identifies an
exact numbered heading". ASR-01 widened `resolve_section` to also accept an exact heading **text**,
because W §1.1's content-bearing children (`Nåværende rolle …`, `Tidlig OUS-plassering …`) are
unnumbered while RP-03 requires separate rows pointing at them. That is a genuine internal conflict in
the plan and Astra resolved it the honest way — the alternative was rows advertising facts outside
their own span. Worth knowing that the locator column is no longer numeric-only.

**F8 — Goal-text deviations (Informational).** ASR-04 replaced the RUNBOOK Stage-1 goal prompt's
*"Read compact inputs…"* sentence with mandatory full-authority reading. OPS §6.2's fenced block does
contain the stale wording, and it contradicts SEM §5.5 / OPS §4.2, so following the block verbatim
would have shipped an instruction that undercuts the entire Task-2 option (a) decision. Correct call.
Separately, `prompts/STAGE1_PROMPT.md`'s `## Goal scope` is a nine-line condensed paraphrase rather
than the lifted OPS §6.2 paragraph, and it cross-references `policy/RUNBOOK.md § Stage-bound goals`
for the full text. Defensible; flagged so it is a choice rather than an oversight.

### 3.3 What is genuinely strong

Worth saying plainly, because it is unusual at this volume of change:

- **Byte fidelity was actually achieved**, not merely claimed. 16/17 quoted blocks exact, the
  amendment verbatim in both Architecture files, and the content-lock block preserved to the byte.
- **The riskiest surface — the hand-rolled parsers — holds against real data**, not just fixtures.
  Every keyword row in every authority parses and resolves.
- **Heading stability across all three authorities is perfect**, which is the single property that
  keeps historical EV addresses meaningful.
- **The two revision interpretations are cleanly separated** and every live caller selects on the
  run's own manifest. This is the part most likely to have been botched, and it was not.
- **The digest tables are well-written**, with real ceilings that mirror the source rather than
  flattening it — including the deferred PRJ-05 authorship boundary.
- **Astra's fixes were correctly targeted.** Each of ASR-01…ASR-06 addresses a real defect, and each
  is the minimal repair. ASR-08's decision *not* to make revision arguments mandatory was right:
  I confirmed independently that no live call site is missing one.

### 3.4 Readiness for the authorized semantic run

**Ready.** No blocker. Recommended order if you want the residuals closed first:

1. Decide F1 and F2 together (remove the six ranking rows from the BAR record and fix W §0.5 item 1's
   dangling reference). If you edit `Work_experience.md`, you must refresh the three derivation hashes
   in `authorities/CV_BASELINE.md` and re-run `index build` — `branch` calls a reconciliation that
   fails on a stale baseline hash, and the failure looks unrelated to the edit.
2. Decide F3 (three stale Stage-2 mentions plus the §7 YAML shape in `PERSONALITY_PROFILE.md`).
3. Then proceed with SEM §6 / OPS §8.1 as written, expecting compacted output filenames (F4).

Note that steps 1 and 2 both touch frozen inputs and are source maintenance, not semantic work.

---

## 4. Method and limits

**What I ran.** The full suite from `B` with `-p no:cacheprovider` and a disposable short base temp;
read-only probes over the live index, authorities, digest tables, keyword tables, baseline
reconciliation and `render_output_paths`; the prescribed read-only legacy probe extended to three
historical runs; `verify-integrity` on the intended parent; SHA-256 comparisons of the three mirror
pairs and the content-lock block; a full plan-block-to-file byte comparison; and structural diffs of
all three authorities against their pre-edit frozen copies.

**What I did not do.** I changed nothing. I ran no semantic stage, no treatment, and no real-run
freeze, branch, `stage-submit`, `finalize` or `render`. I did not re-exercise the legacy `cmd_context`
payload on a disposable copy — Astra did that and reported STRATEGY, FINAL_AND_REVIEW and REVIEW_ONLY
all passing; I proofread the branch and found it correct, but I am reporting its result, not
reproducing it. I did not run `vertical_slice.py` (proofread only, as intended). I did not
re-adjudicate any register decision.

**What this review cannot tell you.** Nothing here speaks to semantic quality, evidence selection,
argument strength or interview value. A green suite and byte-exact policy text prove the machine
carries the intended instructions; only the actual Stage-1 → Stage-3 run can show whether the
instructions produce a better package.

**Disposable artifacts.** All probe scripts and the pytest base temp were written outside the
repository and removed.
