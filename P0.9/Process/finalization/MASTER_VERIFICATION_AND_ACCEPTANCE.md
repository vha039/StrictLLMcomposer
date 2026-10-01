# MASTER VERIFICATION AND ACCEPTANCE

**Status:** reconciled master verification plan. Not authority.
**Companions:** `MASTER_IMPLEMENTATION_PLAN.md` (what to do) ·
`MASTER_RECONCILIATION_LEDGER.md` (why).

---

## 0. What must be proven, and by what

| Outcome | Mechanically provable? | Instrument |
|---|---|---|
| **A** readability | partly | size/format assertions + real PDF page count + **human visual A/B** |
| **B** earned motivation | no | Run B semantic review against a property, not a surface |
| **C** truthful leverage | no | Run B semantic review, checked **in both directions** |
| **D** punctuation | partly | build-time tests on the deterministic sources + **extracted-text checks in A1 and Run B** |
| **E** professional voice | no | **blind A/B**, judged by the candidate |
| ISS-13 output access | partly | structural test + **target `Get-Acl`** + human open |
| ISS-14 test coupling | yes | suite green with the mapping populated **and** blank |

Three of five mandatory outcomes cannot be proven by any test. That is the nature of writing quality,
and `INV-08` forbids citing engineering results as product evidence. Human judgement is therefore a
scheduled acceptance step, not an afterthought.

---

## 1. Rollback substrate and the B0 precondition

No `.git`, so the snapshot is the rollback.

1. SHA-256 registry of the **21-path target set**, recording `ABSENT` for the new
   `policy/writing/FORFATTERSTEMME.md`.
2. `P0.9/Process/finalization_snapshots/pre_0.9.2/` — **must not already exist**. Copy the 20 existing
   targets and the header-only `pilot/PILOT_LOG.csv` under `source_tree/`, preserving relative paths.
3. **B0 is already present.** The human has placed readable copies of both pilot vacancy folders —
   including all four rendered DOCX — at `P0.9/Process/finalization/test-run output/`. Copy those four
   files into `pre_0.9.2/b0/` and record their hashes.

**Verified from a `vhaala\veggi` session:** all four copies open and read normally, while the
originals under `runs/…/out/` still raise `PermissionError [Errno 13]` — ISS-13 reproduced once more,
and the reason B0 had to come from somewhere other than the canonical path.

Identity of the copies is established by content and formatting, not by hash:

| Check | Result |
|---|---|
| CV profile, CV bullet, letter mission paragraph, `var rapportert i bruk om lag 2,5 år senere` present | ✓ matches `final_package.json` |
| CV run sizes | `{8.5, 9.0, 9.5, 10.0, 24.5}` — exactly the master's inline values |
| Letter body runs | inherit from `styles.xml` (no inline size), as designed |
| Residual SDTs / placeholders | 0 / none |
| CV dashes | **15 en, 4 em** — matches the predicted deterministic sources exactly |
| Letter dashes | **1 en** (`Søknad – `), 0 em |

**Caveat, stated rather than glossed:** byte-identity to the originals cannot be proven from a `veggi`
session, because the originals are unreadable there. Content and formatting identity are proven and
are what B0 is for. A session running as `vhaala\CodexSandboxOnline` could hash both sides if
byte-identity is ever needed.

**Run A0 fallback — not required.** Retained only for the case where the `test-run output/` copies
turn out to be missing or not the pilot's output: freeze `verify_a0` over the same two vacancies after
step 2, replay the pilot semantics (§3.2), `finalize`, `render`, export PDFs. Costs one extra run and
works for any identity.

Rollback: restore from `source_tree/`. For the masters restore the snapshot copies —
`prepare_masters` is idempotent forward, not backward.

---

## 2. Mechanical verification

### 2.1 Test arithmetic — stated once

The suite contains **251 tests**; two fail today (ISS-14).

| Point | Word COM | No Word COM |
|---|---|---|
| **Now** | 249 passed / 2 failed / 0 skipped | 239 passed / 2 failed / 10 skipped |
| **After F2 only** | **251 / 0 / 0** | 241 passed / 10 skipped |
| **After the full change set** (**+5**) | **256 / 0 / 0** | 246 passed / 10 skipped |

- **Skips are not passes.** Name each. The ten Word-COM-scoped skips are a session fact, not a
  converter defect.
- **Do not restate "251" as the post-implementation target.** Five tests are added. If one proves
  redundant, drop it and adjust the arithmetic explicitly in `BUILDER_REPORT.md`.
- **COM is a provisional gate, not a hard blocker.** After F2, either `251 / 0 / 0` (COM available) or
  `241 / 0 / 10 named COM skips` (COM unavailable) permits all subsequent independent work. A
  provisional pass never counts as final acceptance: the interactive `251/0/0`, then `256/0/0`, the
  Word-open check, the A1 render with real page counts and the cross-identity open must all land
  before the pass is complete. Stalling the whole sequence on a session fact is the failure this rule
  prevents.

### 2.2 Commands

From `C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build`. Fresh external `--basetemp` each
time; never reuse one from an interrupted run.

```powershell
.\.venv\Scripts\python.exe -m pytest runtime\tests -q -p no:cacheprovider --basetemp C:\Users\veggi\AppData\Local\Temp\jobbsok-full
```

```powershell
.\.venv\Scripts\python.exe -m pytest runtime\tests\test_t09_t12_state_evidence.py runtime\tests\test_t13_t15_merge_leakage_personality.py runtime\tests\test_t16_t18_containment_template.py runtime\tests\test_traceability.py -q -p no:cacheprovider --basetemp C:\Users\veggi\AppData\Local\Temp\jobbsok-adversarial
```

Masters — **write once, then dry-run once**. Two dry runs prove nothing, because `--check` does not
write:

```powershell
.\.venv\Scripts\python.exe -m tools.prepare_masters
.\.venv\Scripts\python.exe -m tools.prepare_masters --check
```

```powershell
.\.venv\Scripts\jobbsok.exe index build
.\.venv\Scripts\jobbsok.exe index verify
```

```powershell
.\.venv\Scripts\jobbsok.exe preflight
```

```powershell
.\.venv\Scripts\python.exe -m tools.vertical_slice --out C:\Users\veggi\AppData\Local\Temp\jobbsok-vslice-evidence --workdir C:\Users\veggi\AppData\Local\Temp\jobbsok-vslice-work
```

### 2.3 Expected results

| Proof | Expected |
|---|---|
| Full suite, Word COM | **256 passed / 0 failed / 0 skipped** |
| Full suite, no COM | 246 passed / 10 skipped, each named |
| Adversarial set | green |
| `prepare_masters` write | both masters written; control contract preserved (**17 CV / 7 letter**) |
| following `prepare_masters --check` | PASS · 0 reorders · 0 font retargets · 0 page-break removals · **0 typography normalizations · 0 dash normalizations** |
| `index verify` | PASS — byte-identical regeneration of both generated maps |
| `preflight` | PASS — proves D3 and D4 landed together |
| Vertical slice | PASS · 21 steps · 0 unexpected · 4 outputs · `render overall : OK` |

### 2.4 The five new tests

`test_traceability.py` requires new tests to keep the owning `test_tNN_` prefix.

| # | File | Name | Asserts |
|---|---|---|---|
| T1 | `test_t16_t18_containment_template.py` | `test_t16_master_typography_uses_the_discrete_scale` | **two assertions.** (a) every inline `w:sz` in both masters' `word/document.xml` is in `{16, 20, 24, 28, 48}` half-points. (b) every **applied** `styles.xml` style holds its intended value: CV `Normal`/`ListBullet` = 24, CV `Heading1` = 28, letter `Normal` = 24, and **letter `Title` = 40 — the deliberately retained 20 pt subject line, asserted as an explicit named exception, not silently ignored.** Latent unapplied styles are out of scope. |
| T2 | `test_t16_t18_containment_template.py` | `test_t16_subordinate_zones_are_not_title_formatted` | the content paragraphs of `CV_RELEVANT_BACHELOR_SUBJECTS` and `CV_OPTIONAL_PREVIOUS_EXPERIENCE` carry no `w:b` and no `w:color` override |
| T3 | `test_t16_t18_containment_template.py` | `test_t16_masters_and_baseline_contain_no_en_or_em_dash` | zero `–`/`—` in either master's `w:t` text and in every rendered `baseline_map.json` value except `baseline_provenance` |
| T4 | `test_t19_t23_render_security.py` | `test_t19_previous_employment_line_uses_plain_punctuation` | rendered TIDLIGERE ERFARING lines contain no em dash |
| T5 | `test_t19_t23_render_security.py` | `test_t19_render_stages_beside_destination_with_inherited_permissions` | render requests an inheritance-preserving transaction under `out_dir`; the workspace is removed afterwards |

**Deliberately not a test:** a DACL assertion. It is not portable across machines and identities, and a
structural test cannot cross the identity boundary that defines ISS-13. That check is §4.2.

**Deliberately not added:** a render-time punctuation warning or normalizer. Outcome D says not to
assume a validator is needed; after D1–D4 every deterministic source is fixed, T3 guards the static
side at build time, and no model-generated dash has ever been observed. The residual risk is covered
by §3.4 and §5.1 at zero code cost.

---

## 3. The controlled A/B — B0 and A1

### 3.1 Why one new typography run suffices

A run's frozen manifest pins its masters; `render_job` raises `ConfigurationError` when a live master's
hash differs from the frozen record. The pilot therefore cannot be re-rendered with the new
typography — by design. But it does not follow that an old-master replay is needed: if B0 can be
recovered as accessible hash-equal copies of the retained pilot DOCX (§1), the "before" side already
exists on real content. Only **A1** is then required.

If the §1 gate fails, **A0** supplies the same "before" at the cost of one extra run.

### 3.2 The replay recipe (A0 and A1)

Pilot artifacts **cannot be copied verbatim** — they carry a `binding` pinned to the pilot manifest,
strategy and draft hashes, plus a `finalization` block, and the stage instructions forbid returning
those. Project only the semantic fields through fresh handoffs, stripping exactly the keys in
`artifacts.MECHANICAL_FIELDS`:

| Artifact | Strip; submit everything else |
|---|---|
| `strategy` | `artifact_role`, `authority`, `elasticity`, `final_writer_may_reconstruct`, `source_escape_permitted`, `binding` |
| `draft_package` | `artifact_role`, `source_stage`, `binding`, `finalization` |
| `final_package` | `artifact_role`, `source_stage`, `binding`, `finalization` |
| `review` | `artifact_role`, `binding` |

Per job, in stage order:

1. `jobbsok freeze` from a `batch_input.csv` naming the same two vacancies; cluster `verify_a1` (or
   `verify_a0`); `--reviewed-by "Vegard Håland"` only after a genuine human attestation.
2. `jobbsok context --stage 1`; use its `write.return_paths` and `write.semantic_fields`.
3. Project the pilot `strategy.json` minus its mechanical keys into that return path; run the emitted
   `submission.command` **verbatim**.
4. Repeat for Stage 2 and Stage 3 (`final_package` + `review` together), always from fresh context.
5. `jobbsok finalize`, then `jobbsok render`.

**No model calls.** `used_evidence_refs` resolve because `evidence_index.json` is byte-identical.
The replay **deliberately carries the pilot's known semantic defects** — holding content constant is
the point. A1 verifies typography, punctuation and access; it is **not** acceptance of B, C or E.

### 3.3 What each side proves

| Evidence | Proves |
|---|---|
| **B0** — hash-equal accessible copies of the retained pilot DOCX (or the A0 render) | the exact old typography and deterministic punctuation on real pilot content |
| **A1** — fresh projected run after the complete implementation | outcome A; the deterministic half of D; parseability; real page counts; F1 output access; the controlled visual comparison against B0 |

### 3.4 Mechanical acceptance from A1

| Check | Criterion |
|---|---|
| CV page count | **normally 2**. A third page is accepted only after editorial compression and canonical spacing review show that forcing 2 would reduce employer-facing quality (`DEC-24`). |
| Letter page count | **1** |
| Page warning | none for either document |
| **Extracted text, all four documents** | **zero `–`, zero `—`** |
| `render_state.overall` | `OK` — both DOCX and both PDFs |
| Parseability (`GATE-06`, `DEC-39`) | identity, contact and logical reading order extractable from both PDFs |
| Identity, chronology anchors, override bullets | all `_verify_docx` checks true |
| Residual SDT or placeholder | none |

---

## 4. Human acceptance — required, not advisory

### 4.1 Typography and layout (outcome A), and `VISUAL_HUMAN`

Open B0 and A1 side by side at the same zoom. Prefer PDFs; otherwise Word print layout for both DOCX.
Judge:

- body text legible at normal reading distance and on screen;
- hierarchy visibly intact: **name > section headings > body and record titles > subordinate detail**;
- CV page 2 meaningfully populated rather than a stub;
- **TIDLIGERE ERFARING no longer competes with the section headings** — it should read as clearly
  subordinate;
- no orphaned heading, no widow line, no clipped bullet, no blank page;
- the letter's address block reads as metadata, not body.

This discharges `VISUAL_HUMAN` / `ACC-18` and Spec §16.7 on **real content**, which they never have
been. Record the result in `BUILDER_REPORT.md`.

Guard in the other direction: if 12 pt at `w:line="252"` reads cramped, that is the trigger for the
single canonical `w:line` adjustment held in reserve under A5 — measured, not assumed.

### 4.2 Output accessibility (ISS-13) — both checks required

1. `Get-Acl` on each promoted file: it must **not** carry the protected creator-only descriptor
   (`SYSTEM` / `Administrators` / `OWNER RIGHTS` with no `(I)`), and `vhaala\veggi` must have
   inherited effective read access.
2. As `vhaala\veggi`, open **both DOCX directly from `runs/<run>/jobs/<job>/out/`** in Word, with no
   copy step.

Both are required. If only the rendering identity can read the file, F1 did not work. The DACL check
catches a partial fix that the open test might mask when run under the wrong account.

### 4.3 Professional voice (outcome E) — blind A/B

Present the pilot letter and the Run B letter for the same vacancy **side by side and unlabelled**.
One question: *which is more plausibly written by me?*

**Guard against over-application.** If the Run B letter reads as *more* performed, more analytical or
more conspicuously styled than the pilot, the voice conditioning is too strong: soften
`FORFATTERSTEMME.md` rather than reverting the change set. Voice that draws attention to itself has
failed on its own terms.

### 4.4 Pilot log (ISS-15)

After reviewing each Run B package, append one row per job to `pilot/PILOT_LOG.csv`: triage, actual
repair scope, submit-ready, factual corrections, minutes through the submission decision, render
issues, friction, outcome. The 19 columns already exist; hand-written.

Without these rows this pass has **no measurement of whether it reduced human repair effort**, and the
representative cluster will produce none either. `ACC-20` and Spec §18.3 have been owed since the
pilot.

---

## 5. Run B — semantic acceptance

A fresh freeze with fresh Stage 1/2/3 under the new policies, same two vacancies. The only run that
exercises outcomes B, C and E.

### 5.1 Properties, not surfaces

**1. Earned motivation (B).** Is every motivation sentence traceable to the actual work, the decision
problem, the operating environment, or a documented candidate motive? Where mission or societal
language appears, does it name a **causal feature of the work** — something that changes what must be
done, what the constraints are, or what "done well" means — rather than restate the employer's value
proposition?

> **Avinor's societal-purpose paragraph surviving is a positive acceptance signal, not a failure.**
> Huseierne's slogan-derived motivation sentence must be gone.

Also check the reviews: **neither `review.reasons` may cite mission, values or purpose language as
evidence that `Arbeidsgiverbyttetesten` is passed.** That is the reproduced failure and the direct
target of the Stage-3 sentence.

**2. Truthful leverage (C), both directions.**
*Upward:* the `PRJ-04` durability claim reads `fortsatt i bruk` or an equally strong evidence-defensible
form, with `om lag` and the `2,5 år senere` horizon preserved and no documentation-provenance frame.
*Downward:* no claim anywhere exceeds its authority ceiling, and each review's `known_limitations`
remains accurate. **The downward half matters more** — over-correction into overclaiming is a worse
defect than the understatement being fixed. `PERSUASION_CALIBRATION § TOO_WEAK` now carries the
`for sterkt` boundary; check against it.

**3. Vacancy-driven structure (ISS-10).** Judged on **`structure_guidance`, not the letter's
silhouette**. Two jobs may legitimately converge if both need the same shape. The failure signal is a
`structure_guidance` that would read identically for any employer.

**4. Authentic voice (E).** The blind A/B of §4.3.

**5. Punctuation on model-generated prose (D).** Zero `–` and zero `—` in the extracted text of all
four documents, and **no hyphen used as a clause divider** in either letter. Run B is the only run
with fresh model prose, so it is the only place a model-generated dash can appear. This check exists
because no runtime warning is added; it is the substitute, and it is not optional. Judged by reading
the sentence in context, never as a string match.

**6. No new generic residue (ISS-09, ISS-11).** The five patterns named in
`FORFATTERSTEMME § Mønstre som skal erstattes` are absent, *or* deliberately retained with a better
reason. **Not a lint** — a mechanical phrase check is forbidden by `INV-07` and Spec §10.3.

**7. Regression guard.** Nothing already good may get worse. Specifically the Avinor sentence

> *"forventninger må gjøres etterprøvbare, ansvar og antakelser må være synlige, og metoden må fungere
> for dem som skal bruke den"*

is the strongest existing evidence of the candidate's professional voice. If Run B loses that quality,
the change set is over-applied.

**8. No mechanical regression.** Both jobs reach `VALID` / `FINAL` with current final+review; render
`OK`; no new page warning; triage calibrated as before. A shift to `CHECK` on **both** jobs suggests
the new rules made the model defensive — a finding, not a pass.

### 5.2 Comparison against the pilot

No material regression in truth, tailoring, render stability, workflow or handling; the targeted
defects materially improved. Compare against the pilot finals on claim ceilings held, employer
specificity, CV/letter complementarity, evidence-selection quality, `known_limitations` accuracy, and
operator minutes from the pilot log.

---

## 6. Sequence of gates

| Step | Work | Gate |
|---|---|---|
| 0 | snapshot; **B0 precondition resolved** (§1) | 21-path registry written; B0 recovered **or** A0 scheduled |
| 1 | **F2** | suite **251 / 0 / 0** with COM |
| 2 | **D1, D2, F1** + T4, T5 | focused tests green; suite green |
| 2b | *(fallback only)* **Run A0** → B0 | four accessible PDFs/DOCX |
| 3 | policy: A3, B1–B3, C1, C2, D5, E1, E2, RUNBOOK, versions | `FORFATTERSTEMME.md` reviewed by Vegard |
| 4 | **D3** → `index build` → `index verify` | `index verify` PASS |
| 5 | **A1, A2, D4** via `prepare_masters` (write, then `--check`); `preflight`; T1–T3 | control contract 17/7; **both masters open in Word**; `preflight` PASS |
| 6 | **Run A1** → render | §3.4 mechanical + §4.1 visual + §4.2 access |
| 7 | full suite, adversarial set, vertical slice, scope gate | **256 / 0 / 0**; scope budget met |
| 8 | **Run B**; semantic review; two pilot-log rows | §5.1 criteria |
| 9 | one representative cluster | §7 |

---

## 7. Representative-cluster gate

More than two jobs, mixed priority. Tests what two jobs cannot:

- **throughput** — whether the new policy load materially increases per-job complexity, refusal rate or
  human review burden. A fix that produces excellent two-job output and slows the cluster is a net
  regression;
- **cross-job convergence at scale** (`EXP-07`) — observed by the human; no detector exists and none
  may be built;
- **triage calibration** (`EXP-06`) — whether `READY` still means what the pilot log says it meant;
- **typography under content variation** — whether a denser CV passes 2 pages, and whether A3's
  compression rule is actually applied.

One `PILOT_LOG.csv` row per job.

---

## 8. Success and failure criteria

### 8.1 Success

1. Suite **256 / 0 / 0** with Word COM; skips named if run without.
2. `prepare_masters` write then `--check` clean; control contract preserved; **both masters open in
   Word**.
3. `index verify`, `preflight` and the vertical slice PASS.
4. A1: CV 2 pages (or a justified 3), letter 1 page, **zero `–`/`—` in all four extracted texts**,
   `render overall : OK`, parseability intact.
5. Visual A/B: A1 more readable than B0, hierarchy intact, page 2 populated, TIDLIGERE ERFARING
   subordinate.
6. **Both** ISS-13 checks pass: promoted-file DACL unprotected, and `vhaala\veggi` opens both DOCX
   from `out/` with no copy step.
7. Run B: all eight §5.1 criteria met, including the punctuation check and the regression guard.
8. Blind A/B: the Run B letter judged more plausibly candidate-authored, without reading as performed.
9. Two `PILOT_LOG.csv` rows written.
10. Scope gate: 22 manifest paths snapshotted, **21 final diffs**, one new file,
    `evidence_index.json` byte-identical; no prohibited redesign present.
11. **Representative cluster complete** (§7) — every job in the cluster reaches a current final and a
    rendered package; one `PILOT_LOG.csv` row per job; no material regression in truth, tailoring,
    render stability, triage calibration or throughput; and cross-job convergence acceptable on human
    reading.

**Items 1–10 are not the terminal condition.** Run B closes the two-job evidence loop; the pass is
complete only when item 11 also holds. A change set that looks excellent on two jobs and degrades at
cluster scale is a net regression, and the cluster is the only place that becomes visible.

### 8.2 Hard stops

1. Control contract changes (≠ 17 CV / 7 letter) — the master edit is wrong; do not force it.
2. Either master fails to **open in Word** — the highest-risk check; the P0.7 masters parsed in
   LibreOffice while Word rejected them.
3. `preflight` fails after step 5 — D3 and D4 disagree; fix, never relax the assertion.

### 8.3 Stop and escalate

| Condition | Action |
|---|---|
| Suite not 251/0/0 after step 1 | stop before anything else lands |
| `index verify` fails | the baseline edit broke byte-identical regeneration |
| CV 3+ pages and compression cannot reach 2 without dropping decision-relevant content | escalate; **never** reduce type size |
| Only the rendering identity can read the promoted DOCX | F1 is incomplete; do not proceed to Run B |
| Run B worse than the pilot on truth, tailoring or the regression guard | soften `FORFATTERSTEMME.md`; do not revert the set |
| Run B triage `CHECK` on both jobs | the new rules made the model defensive — a finding |
| Any change appears to require an architecture amendment | stop; escalate against the exact governing ID with target-machine evidence. Never resolve by silent deviation. |

---

## 9. Stopping rule

**Final pilot-informed optimization pass.** After Run B and one representative cluster, framework
iteration stops.

Iteration resumes only on **repeated real-production evidence** of a material blocker that also beats
the smallest local remedy. A single stylistic preference, a one-off model output, or a defect cheaper
to fix by hand than to engineer away does not qualify.

### 9.1 Deferred to real production

| Item | Why |
|---|---|
| Cross-job convergence at cluster scale | `EXP-07`; two jobs cannot show it, and no detector may be built |
| Triage calibration against actual human edits | `EXP-06`; needs pilot-log rows across several clusters |
| Sample-grounding for `FORFATTERSTEMME.md` | the profile-derived version ships first; refine only if the blind A/B shows a specific miss |
| Master line-spacing adjustment | held in reserve under A5; apply only if the visual review shows the body cramped |
| Any mechanised punctuation check | the §5.1 acceptance check is the current remedy; mechanise only on observed recurrence |
| Dormant `converter = "auto"` | production uses `word_com` |
| The six dead settings keys (F22) | deliberated and deferred |
| `warnings` in `status --json` | `status.schema.json` is closed (F10) |
| Automatic pilot-log tooling | a RUNBOOK line is the smallest local remedy |

### 9.2 What "done" means

> The system produces employer-facing packages whose remaining imperfections are cheaper to handle
> manually than to engineer away.

When Run B and the representative cluster meet §8.1, framework work ends and the system returns to
producing real applications.
