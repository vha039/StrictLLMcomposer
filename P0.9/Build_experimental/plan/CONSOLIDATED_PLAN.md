# Relay — consolidated implementation plan

Supersedes `plan/NEXT_DEVELOPMENT_PLAN.md`. Adjudicates it against
`reviews/CODEX_DIFF_REVIEW.md`; every disputed premise was re-verified in the
repository. Self-contained: implement from this file plus the repository.

## 0. Working rules

Root: `C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build_experimental`.
Run everything as `.\.venv\Scripts\jobbsok.exe <cmd>`. `import jobbsok` must
resolve inside this tree.

Orientation, if needed: `reviews/ONBOARDING_BRIEF.md` (what this is),
`AGENTS.md` (stage behaviour), `runtime/jobbsok/pipeline.py` (artifact and
stage registry — everything derives from it).

| # | Constraint |
|---|---|
| 1 | Never modify, write through to, or execute code from `..\Build`. |
| 2 | No QA frameworks, test suites, generic preflight, compat/migration layers, defensive scaffolding. Checks **intrinsic to an existing mechanism** are in scope — several items below enforce declarations the schemas already make; they are not new scaffolding and must not be cut as such. |
| 3 | Stages stay separate, human-started sessions. No orchestration, scheduler, model client or network call. |
| 4 | `authorities/` and `context/` are user-owned facts — never edit a fact nugget. `policy/`, `schemas/`, `prompts/`, `runtime/` are agent-owned. |
| 5 | Move superseded files to `archive_0.9.3/`; never delete. Leave `runs/` except where an item names a run. |
| 6 | Artifacts change only through `stage-submit`. Never hand-edit `runs/*/current/`. |

**Phase order is load-bearing.** Phase 5 (hash convention) lands *after* Phase 4
(recovery) precisely so no migration verb is needed. Do not reorder.

## 1. Comparison caveats — carry into any measurement

- Frozen `WORK` differs between `r20260914-211651-5dbd38` and
  `r20260916-184816-a1ea76` by the corrected BAR digest sentence
  (`frozen/authorities/Work_experience.md:66`). EDU and OTHER hashes match.
  Confound wherever early-role ownership is assessed.
- `rung`'s Norwegian was scored CV-only; the Relay's is LETTER_AND_CV. Hold
  delivery constant or report the two separately.
- No interview outcomes exist. Report paired document differences and explicit
  editorial judgments; do not report calibrated probabilities.
- Counts must come from the runtime counters (`signals.cv_dynamic_words`,
  `signals.letter_words`, `signals.letter_text`), not ad-hoc regex.

---

# Phase 1 — submit correctness

Nothing else is safe until these land. All in `runtime/jobbsok/cli.py`
(`cmd_stage_submit`, `build_parser`) unless stated.

### 1.1 · Scope `--reject` and `--finalize-render` to Stage 3
**Now:** `_write_set(stage, reject)` ignores `reject` for stages 0–2, and the
`if reject:` block after `submit_many` discards `polish` and `final_package`
unconditionally. `stage-submit --stage 1 --reject` therefore writes
brief+cv_draft and then deletes a published package.
**Change:** in `build_parser`, reject both flags for `--stage != 3` before any
work. In `cmd_stage_submit`, guard the discard block with `stage == 3`.
**Verify:** `stage-submit --stage 1 --reject` exits non-zero, no file touched.

### 1.2 · Publish and rejection are mutually exclusive
**Now:** the publish path never inspects `triage`. A Stage-3 submit without
`--reject` carrying `triage: RERUN` writes polish + final + review, and
`cmd_finalize` then finalizes it.
**Change:** on the publish path refuse `triage == "RERUN"` ("use `--reject`").
Keep the existing converse check. In `cmd_finalize` and `cmd_render`, refuse
when the job's current review is RERUN.
**Verify:** publish with RERUN refuses; `finalize` on a RERUN job refuses.

### 1.3 · `--fingerprint` required on every semantic submit
**Now:** the parser defaults it to `None` and the comparison is skipped when
absent, so `--file` bypasses the stale-context handshake entirely.
**Change:** make `--fingerprint` required for `stage-submit`, including with
`--file`. Reuse after an upstream change becomes an explicit owning-stage
decision against a fresh bundle.
**Verify:** submit without `--fingerprint` refuses; with a stale one, refuses
naming the current fingerprint.

### 1.4 · Rejection stays usable after publication
**Change:** a Stage-3 rejection archives, rather than silently drops, the
pipeline-owned deliverables it withdraws: move `polish` and `final_package` to
`history/` (already the behaviour of `artifacts.discard`) **and** move the
job's pipeline-written `out/` products (`CV_*`, `Soknad_*`, `form_answers.md`,
receipt) to `out/withdrawn/<timestamp>/`. Print each path. Leave any file the
receipt does not name — those are the human's.
**Why:** decline must remain available after a publish; withdrawal must be
visible rather than leaving stale deliverables on disk.
**Verify:** publish a job, reject it, confirm `current/` has review only and
`out/withdrawn/<ts>/` holds the previous documents.
**Note:** this also closes the standing "leftover `Soknad_*` after a CV-only
republish" item in `HANDOVER.md` — apply the same withdrawal on republish when
the new delivery drops a document the previous receipt named.

### 1.5 · Warn on newly stale downstream work
**Change:** before persistence, compute which existing artifacts owned by
stages **below** this one will become stale under the proposed write (compare
proposed input identities to current), and print:
```
[WARN] this submit will stale: advocacy_draft (Stage 2), polish (Stage 3)
       downstream work exists for this job
```
Not a gate. **Do not** add `superseded_downstream` or any other binding
metadata — `history/` already preserves the previous bytes and extra binding
fields are themselves a downstream change.
**Verify:** re-submitting a brief on a job that has an advocacy draft prints
the warning and still succeeds.

---

# Phase 2 — one currency definition

The defect: `binding.inputs` records an artifact's declared inputs, but
staleness only compares the *stage-level* fingerprint, which
`binding_for` filters to `STAGES[stage].requires`. Consequences, all verified:
`cv_draft` never goes stale when `brief` changes (it declares `brief` as an
input but Stage 1 requires only `scout`); `review` on a publish never binds the
`final_package` it approves, because `final_package ∉ STAGES[3].requires`.

### 2.1 · Bind every declared input; fingerprint per artifact
`runtime/jobbsok/pipeline.py`, `runtime/jobbsok/artifacts.py`.

- `binding_for`: delete the `stage_upstream` filter. `binding.inputs` carries
  every key in `ARTIFACTS[name].inputs` that exists.
- Add `pipeline.artifact_fingerprint(context, job_id, artifact, *, upstream)` —
  same body as `evidence_fingerprint` but keyed on the artifact's own inputs.
  Store **this** in `binding.evidence_fingerprint`.
- Keep `pipeline.evidence_fingerprint(context, job_id, stage)` unchanged as the
  *bundle* fingerprint: it names the returns directory and is the
  `--fingerprint` handshake. Two fingerprints, two jobs, no overlap.
- `ARTIFACTS["review"].inputs` gains `final_package`.

### 2.2 · `_stale_reason` checks inputs, then facts
`runtime/jobbsok/artifacts.py`.

```python
def _stale_reason(context, job_id, artifact, payload):
    binding = payload.get("binding") or {}
    stored  = binding.get("inputs") or {}
    current = pipeline.upstream_hashes(context, job_id, artifact)
    keys = set(stored) | set(current)
    if artifact == "review" and "final_package" not in stored:
        keys.discard("final_package")      # a rejection review binds no final
    moved = sorted(k for k in keys if stored.get(k) != current.get(k))
    if moved:
        return "inputs changed: " + ", ".join(moved)
    if binding.get("evidence_fingerprint") != pipeline.artifact_fingerprint(
            context, job_id, artifact, upstream=stored):
        return "frozen facts or the vacancy changed since this artifact was written"
    return None
```
**Message rule (replaces the rejected `DECISION_FIELDS` idea):** name the moved
artifacts factually and point at the evidence, e.g.
`inputs changed: brief — previous copy in history/20260916T220553Z_brief.json`.
Never classify a field name as safe; `employer_problem`, `reserve`, `traps` and
`stances[].line` all have substantive roles in `policy/stages/stage1_architect.md`.

### 2.3 · Preserve the finalize property
`artifact_hash` excludes `finalization` for `artifact_role ==
"CURRENT_SEMANTIC_PACKAGE"`. With 2.1 making `review` bind `final_package`,
this exclusion is what stops `finalize` from staling the review it just
published. **Do not remove it**, and re-check it survives Phase 5.
**Verify:** publish, then finalize; `status` must still show the review current.

### 2.4 · Stage-3 diagnostic bundle (relaxed context, narrowly)
`cmd_context`. Refuse as today when a required artifact is **missing**. When a
required artifact is **stale or invalid**, refuse for stages 0–2 as today; for
**Stage 3 only**, issue a diagnostic bundle:
- per-input `{state, reason}` under `upstream_state`;
- `write.allowed: ["review"]`, `write.blocked: {"polish": "<reason>"}`;
- `commands.submit` is the `--reject` form only;
- **omit** `assembled_draft` and `draft_summary` — do not build an
  apparently-current draft from stale layers.
**Why:** the stage whose job is to decline must be able to see what it is
declining. Publish eligibility is not granted.

---

# Phase 3 — merge and declarations

### 3.1 · Empty arrays clear, as the docstring already says
`runtime/jobbsok/assemble.py`.
- `merge_cv`: `employment_overrides: []` present in the patch clears all
  overrides back to baseline. A per-employment `bullets: []` clears that
  employment's bullets (already the merge-by-id behaviour once the outer case
  is fixed).
- `assemble`: replace `if polish.get("form_answers"):` with
  `if "form_answers" in polish:` so `[]` clears. Same for the advocacy layer.
**Verify:** merge a polish with both arrays empty; the result carries neither.

### 3.2 · Enforce the keystone and change declarations
`runtime/jobbsok/validate.py`, at Stage-2 and Stage-3 submit.
Enforces declarations the schemas already require — not new scaffolding.
- `advocacy_draft.keystones[].id` unique; each `text` must appear verbatim in
  the document named by its `document` field in the **assembled** package.
- `polish.keystone_disposition` covers every upstream keystone id exactly once.
  A `KEPT` disposition requires the keystone text still present in the
  assembled package. `REWORDED` is not text-checked — function preservation is
  the editor's judgment.
- Every field the polish actually changed (as `assemble._changed_fields`
  computes) must appear in `polish.changes[].field` with a reason.
`assemble` currently only prints `undeclared` in the summary; that stays, but
submit now refuses.

### 3.3 · Delivery consistency
`runtime/jobbsok/validate.py`, at Stage-2 submit and at final assembly, against
`brief.delivery`:

| delivery | requires |
|---|---|
| `LETTER_AND_CV` | `letter` non-null with opening, ≥1 body paragraph, closing |
| `CV_ONLY` | `letter: null` |
| `CV_PLUS_FORM_ANSWERS` | `letter: null`; one `form_answers` entry per `scout.submission.screening_questions`; if the scout recorded none, refuse with "no source questions recorded" rather than accepting an invented set |

**Verify:** the real Abacus brief says `LETTER_AND_CV`; an advocacy with
`letter: null` must now refuse (it validates today).

### 3.4 · `review` schema conditionals
`schemas/review.schema.json`. The conditional the design assumed is absent —
`required` is just `[artifact_role, binding, triage, reasons,
known_limitations]`. Add:
- `triage == "RERUN"` → `rerun_stage` required, enum `[1, 2]`;
  `binding.inputs` must **not** contain `final_package`.
- `triage != "RERUN"` → `rerun_stage` absent or null; `binding.inputs` **must**
  contain `final_package`.

### 3.5 · Preview and assemble resolve the same layers
`runtime/jobbsok/preview.py:_in_progress`, `cli.py` (`cmd_assemble`,
`cmd_context` Stage-3 branch).
**Now:** `_in_progress` does `sorted(base.rglob(...))[-1]` — the
lexicographically last fingerprint directory, which is not the current one.
Stortinget's current Stage-2 fingerprint is `a06a3e44` while the selected
return sits under `229c697b`. `assemble` meanwhile prefers the current polish
over a newer return — preview and publish disagree about what the text is.
**Change:** one resolver used by `preview`, `assemble` and the Stage-3 bundle:
- for the **active** stage, the return under the *current bundle fingerprint*
  directory only; if absent, the current artifact;
- for **upstream** layers, the submitted artifact in `current/` — never a
  return directory;
- Stage 3's base draft is cv_draft ⊕ advocacy_draft; a polish return applies
  only when it is the active stage's return at the current fingerprint.
**Verify:** with a return present at a stale fingerprint, `preview` uses the
current artifact and says so.

### 3.6 · Preview metrics carry what they measured
`preview.py` writes `generated/preview/<run>/<job>.json`; `status.py:152-174`
imports it unconditionally. Store the `artifact_hash` of the measured package
in that file and have `status` label the metrics stale when it no longer
matches the package it is reporting on. A banner alone does not identify what
was rendered.

### 3.7 · State labels on the read-only views
`preview`, `assemble --dry-run`, `register`: one line naming any stale or
invalid layer in the text being shown. `register.md` gains a `state` column.
`register` governs cross-job differentiation; it must not present superseded
text as the cluster's variation baseline.

---

# Phase 4 — bundle completeness

### 4.1 · Navigation in Stage-2 and Stage-3 bundles
`cli.py:cmd_context`. `digests.md`, `retrieval.md` and `catalog.md` are written
only in the stage 0 and 1 branches, yet `AGENTS.md` tells every stage the
catalog and retrieval index "are already in the bundle". Add all three to the
stage 2 and stage 3 branches (same `cards_module` calls).

### 4.2 · The scoped pack matches the brief
`cards.py:default_ids`, stage 2. Currently `units + judgment + reserve +
stances + distinctiveness`. Add `brief["outside_scout_refs"]` and
`letter_plan.paragraphs[].refs`. Measured shortfall today: Stortinget 12 of 14
brief refs reach the Stage-2 pack, Norwegian 11 of 13, EIE 13 of 14.

### 4.3 · Documentation matches behaviour
- `AGENTS.md`: the retrieval paragraph is true only after 4.1 — land together.
  Add to **Never**: "re-submit an upstream artifact once a downstream stage has
  started without telling the operator what it invalidates."
  Add to the refusal table: `publish refused: triage is RERUN` → use `--reject`;
  `--reject is Stage 3 only`.
- `README.md` / `HANDOVER.md`: correct the `stage-submit` row to note
  publish/reject exclusivity, and strike the resolved `Soknad_*` open item
  (closed by 1.4).

---

# Phase 5 — the evidence leak (highest value)

The measured regression: adoption/persistence facts appear in the counterpart
letters (8 phrase matches across 4 sentences) and in **zero** Relay letters.

**The cause is policy, not schema.** Verified: the facts were present at every
upstream point — Norwegian's `current/brief.json:40` carries completion and
controller handover, and its delivered
`generated/returns/.../stage2/ab9b3af1/inputs/cards_scoped.md:87,117-121,155`
carries sole-coder, hospital-wide use and handover. Meanwhile
`policy/writing/WRITING_DOCTRINE.md:295-297` says «En statusopplysning som
allerede står i CV-en gjentas ikke i brevet», and the Relay CVs carry
hospital-wide use in 3 of 4 jobs. **The letters obeyed the doctrine.**

### 5.1 · WRITING_DOCTRINE — selective repetition
`policy/writing/WRITING_DOCTRINE.md:295-297`. Replace the categorical
prohibition with, in Norwegian, in the file's register:
- a status or qualifier **may** be repeated across CV and letter when it
  carries the letter's argument, and must be repeated when the letter would
  otherwise be misleading without it;
- each document must be independently truthful — a qualifier that scopes a
  claim travels with the claim into every document that makes it;
- what stays prohibited is the *decorative* repeat: restating CV content that
  does no argumentative work.

### 5.2 · Stage 2 playbook
`policy/stages/stage2_advocate.md:18-20,31-37`.
- Write from the **full referenced cards**; the brief guides selection, it is
  not the text to paraphrase.
- Carry a decisive outcome — who took the work up, whether it is still running
  — into the delivered argument when it strengthens it. Judge the *delivered
  combination* (CV + letter + form answers), not the letter alone.
- Repeat vocabulary the vacancy screens on when it is supported. The Abacus
  letter moved «prosjektnulling, periodisering, reversering, avsetninger,
  bilagsflyt» into the CV and lost its strongest qualification signal on the
  highest-fit vacancy in the cluster.
- Restore a quoted fact **with the scope the authority gives it**: «i praksis
  eneste kodende utvikler **for kodeendringene** … innenfor en bred
  interessentprosess på ca. 50 personer». Neither the bare claim nor a hedge
  that drops the fact.
- Remove the contradiction with 5.1 at the same time.

### 5.3 · Stage 3 playbook
`policy/stages/stage3_editor.md:30-36`. The overstatement/understatement pass
already exists. Add: judge omission **across the delivered combination**, and
treat lost decisive evidence as an editorial defect when it is material — not
every absent outcome as a truth failure. Read for repeated generalising
sentences directly in the voice pass.
**Explicitly not added:** an impersonal-sentence counter. The proxy rewards
pronouns and penalises legitimate employer-fact sentences. The observed 14→27
is descriptive only.

### 5.4 · Stage 1 sequencing
`policy/stages/stage1_architect.md` and `prompts/STAGE1_ARCHITECT.md`, one
paragraph:
> Do the cluster-level tightening pass **before** submitting, not after the
> register view at the end of the cluster. If you revise a brief after
> submitting it, say so in the session report and name what it invalidated.

With 1.5's warning this closes the 16 September sequencing failure from both
ends. No lock, no scheduler.

---

# Phase 6 — recover the `rung` cluster

Run `r20260916-184816-a1ea76`, cluster `rung`, four jobs. State: 16
schema-valid artifacts; all four `advocacy_draft` stale; four unsubmitted
Stage-3 returns under `generated/returns/<run>/<job>/stage3/<fp8>/`.

Live `brief.schema.json` edits would **not** invalidate the existing briefs —
`validate.py:45` and `manifest.py:128-129` select the **frozen** schemas — but
no brief schema change is proposed, so the point is moot.

### 6.1 · Per-job disposition of the saved Stage-3 returns
Stage 1's second pass rewrote `stances[].line` — the prescribed NAME_ONCE
sentence — for two jobs, and in one case made the *same* repair Stage 3 later
made independently:

| Job | Second brief pass | Saved Stage-3 return |
|---|---|---|
| stortinget | `stances[].line`: «det jeg tar med, er» → «Med meg tar jeg» | K4 REWORDED repairs the same cleft. **Do not reuse blind** — reusing either double-repairs or reverts Stage 1's wording. Stage 2 and Stage 3 must re-read the current line. |
| eie | `stances[].line` rewritten (Core / EIE 365 sentence) | K3 REWORDED touches the same sentence. Same treatment. |
| norwegian | no `stances` change | reusable after Stage 3 re-reads the assembly |
| abacus | no `stances` change | reusable after Stage 3 re-reads the assembly |

### 6.2 · Sequence
1. **Stage 1 session** — for each job, `context --stage 1`, confirm the brief
   and CV layer still stand, resubmit. To resubmit unchanged content, strip the
   tool-owned keys first (the submit refuses a payload containing them):
   ```powershell
   python -c "import json,io,sys; p=sys.argv[1]; d=json.load(io.open(p,encoding='utf-8')); [d.pop(k,None) for k in ('artifact_role','binding','finalization')]; io.open(sys.argv[2],'w',encoding='utf-8',newline='\n').write(json.dumps(d,ensure_ascii=False,indent=2))" runs\r20260916-184816-a1ea76\jobs\<JOB>\current\brief.json <RETURN_DIR>\brief.semantic.json
   ```
   Then the printed `commands.submit`. This is the owning stage taking
   responsibility; no new verb is introduced.
2. **Stage 2 session** — `context --stage 2` per job. Review the current brief,
   in particular `stances[].line` for stortinget and eie. Carry the existing
   letter across where it still fits; apply 5.1–5.2 — add the decisive outcome
   and, for Abacus, the finance-process vocabulary. Submit.
3. **Stage 3 session** — `context --stage 3`, inspect the resulting assembly,
   reuse the saved returns only where 6.1 says they apply, re-run the four
   passes, submit with `--finalize-render`.
4. **Render and read the page counts.** This is the one unverified knock-out
   cue: the editor measured the pre-polish draft, and no post-polish render
   exists. CV over two pages is ×0.70, letter over one page ×0.75.
5. Before anything is sent, two human calls: Stortinget's deadline
   (14 September) has passed; Norwegian is delivered as LETTER_AND_CV where the
   ad says "upload an updated copy of your CV".

---

# Phase 7 — hash convention (after Phase 6 only)

### 7.1 · `artifact_hash` excludes provenance
`artifacts.py:38`. Exclude `binding` and `artifact_role`; keep the
`finalization` exclusion for `CURRENT_SEMANTIC_PACKAGE` (2.3).
```python
SEMANTIC_EXCLUDED = ("binding", "artifact_role")
```
**Why now and not earlier:** identity becomes what the stage wrote, so a
sibling resubmitted unchanged stops cascading. Landing it after Phase 6 means
no migration sweep and no `rebind` verb — the rejected `rebind --all` was only
ever needed as this item's migration.
**Correction to the earlier plan:** an identical resubmit against identical
inputs already produces an identical hash (`binding_for` carries no timestamp).
The cascade is real only when an input moved.
**Apply to new runs.** Existing runs keep their stored values; anything still
open when this lands is resubmitted by its owning stage.

---

# Phase 8 — `branch` (independent; fix before next use)

Two verified defects in `branch.py:199-211`:
- **Laundering.** The parent payload's `binding` is replaced with
  `binding_for(child_context, …)` — which embeds the *new* frozen facts —
  **before** `_stale_reason` is called on it. The test then compares the new
  binding against the new facts and returns `None`. With `--refresh-inputs`, an
  old Scout is stamped as having consumed facts it never saw. `binding_for`
  also overwrites `policy_fingerprint`, losing the reused content's provenance.
- **Unresolvable children.** `_stale_reason` recomputes with `upstream=None`,
  which loads through `layout.run_dir(child_id)` — a path that does not exist
  until `staging.rename(final)` at `branch.py:229`. Every artifact with inputs
  therefore reports `upstream changed` and is dropped.

**Change:** decide reusability **before** rebinding. For each artifact, compare
the parent's recorded inputs against the child's *already-accepted* artifacts
in staging (translating parent hashes to their reused child equivalents), and
against the child's frozen facts. Drop from the first failing stage downward.
Only then stamp, preserving the original `policy_fingerprint`.
**Correctness is established by execution, not by reading** — exercise on a
throwaway branch of `r20260916-185207-a37938` with a deliberately altered
frozen file, and confirm reuse and drop both occur.

---

# Phase 9 — measure on `runf`

Fresh freeze, Phases 1–7 in place, cluster `runf` (Tieto, BearingPoint, Amesto,
Visma) end to end. It is the better test: three of its four CVs ran to three
pages in the counterpart corpus, and Visma is a genuine CV-only instrument
(«Vi krever selvfølgelig ikke søknadsbrev» plus application questions), so it
exercises `CV_PLUS_FORM_ANSWERS` and 3.3 for the first time.

Report paired differences only, per §1: adoption sentences per delivered
package; CV and letter words from the runtime counters; rendered page counts;
distinct opening/closing moves; and the editorial judgments behind each.
Do not optimise for the counts.

---

# Adjudication ledger — rejected, do not re-add

| Proposal | Verdict | Verified reason |
|---|---|---|
| `jobbsok rebind` (esp. `--all`) | **REJECT** | Owning-stage `context` + `stage-submit --file` already covers it (`cli.py:322-327,369-396`). It was only needed as Phase 7's migration; reordering removes the need. Cross-stage mutation of another stage's artifact contradicts `AGENTS.md:122-126`. |
| `DECISION_FIELDS` + auto-route to rebind | **REJECT** | Field names cannot establish semantic equivalence. `employer_problem`, `reserve`, `traps` have substantive roles (`stage1_architect.md:37-43,62-66`), and the actual history changed `stances[].line`. |
| `brief.units[].evidence_quote` + substring gate | **REJECT** | A substring check cannot enforce scope: bare «i praksis eneste kodende utvikler» *is* a substring of the scoped PRJ-03 card, as is every truncation of any valid quote. `cards.py:115-140` already supplies digest, boundaries and source text. |
| `brief.units[].outcome` (required-nullable) | **REJECT** | Redundant carrier — Norwegian's `brief.json:40` already carries the handover. A null does not force useful selection. Also conflates handover with organizational adoption (`authorities/Work_experience.md:573-578` distinguishes them). |
| `judgment` required + `judgment_absent_reason` | **REJECT** | Premise false: all 4 current and 6 historical briefs carry a populated `judgment` with refs and ceiling. |
| `letter_plan.paragraphs[].carries[]` | **REJECT** | Duplicates `units[].placement` and `paragraphs[].job/unit_ids`. A blanket OUTCOME requirement is wrong for CV-only delivery. |
| `impersonal_sentences` / antithesis counters | **REJECT** | Proxy rewards pronouns and penalises legitimate employer-fact sentences. Keep 14→27 as description only. |
| `superseded_downstream` in bindings | **REJECT** | New audit metadata that is itself a binding change; `history/` already preserves the bytes. Keep the warning (1.5), drop the field. |
| Blanket ban on rejecting a published job | **REJECT** | Decline must stay usable after publication; 1.4's explicit withdrawal is the right mechanism. |
| IOI / expected-chance deltas as findings | **REJECT** | Uncalibrated logistic, no observed outcomes, confounded delivery. Paired differences only. |

---

# Expected end state

- `stage-submit` cannot cross stage boundaries, cannot publish rejected work,
  and cannot accept a return prepared against a context it never saw.
- One currency definition: every declared input is bound and checked; `review`
  binds the `final_package` it approves; `finalize` still does not stale it.
- `preview`, `assemble`, the Stage-3 bundle and `status` all describe the same
  text, and say when that text is stale or unmeasured.
- Empty arrays clear. Keystones, dispositions, change reasons and delivery mode
  are enforced rather than merely declared.
- Stages 2 and 3 receive the navigation the documentation already promises, and
  the Stage-2 pack covers every ref the brief names.
- The doctrine permits the repetition the argument needs; each document is
  independently truthful.
- `rung` is published and rendered with measured page counts; `runf` is the
  clean measurement.
- `branch` reuses or drops on evidence, and launders nothing.
