# 07 — Verification, acceptance and stopping plan

**Status:** planning material. Not authority.
**Purpose:** the exact mechanical tests, semantic regression checks, render and visual inspection,
A/B design, cluster gate, pass/fail criteria, and the point at which framework iteration stops.

---

## 0. What must be proven, and by what

Five mandatory outcomes and two mechanical defects. Each needs a different kind of evidence, and
conflating them is how a pass declares success it has not earned.

| Outcome | Provable mechanically? | Instrument |
|---|---|---|
| **A** readability | partly | size assertions + real PDF page count + **human visual A/B** |
| **B** earned motivation | no | Run B semantic review against a property, not a surface |
| **C** truthful leverage | no | Run B semantic review, checked **in both directions** |
| **D** punctuation | partly | deterministic-source tests + extracted full-output text + human clause-punctuation review |
| **E** professional voice | no | **blind A/B**, judged by the candidate |
| ISS-13 output ACL | partly | inheritance-mode/location test + target DACL inspection + human open |
| ISS-14 test coupling | yes | suite green with the mapping populated **and** blank |

Three of the five mandatory outcomes cannot be proven by any test. That is not a gap in the plan; it
is the nature of writing quality, and `INV-08` forbids citing engineering results as product evidence.
The plan therefore makes human judgement an explicit, scheduled acceptance step rather than an
afterthought.

---

## 1. No version control — the rollback substrate

There is no `.git` anywhere in this checkout, so `git commit` and `git diff` against history are
impossible. Before any edit:

1. Write a SHA-256 registry of the 21-path target set in `02_…md` §1, recording `ABSENT` for the new
   `policy/writing/FORFATTERSTEMME.md`.
2. Use the fixed snapshot root
   `P0.9/Process/finalization_snapshots/pre_0.9.2/`; it must not already exist. Copy the 20 existing
   targets and current header-only `pilot/PILOT_LOG.csv`, preserving relative paths, under
   `source_tree/`. Copy the four retained pilot DOCX as ordinary data copies (do not preserve their
   security descriptor) under `b0/`, and record both source and copy hashes.
3. After the pass, compare with `git diff --no-index <snapshot> <live>`.

The snapshot **is** the rollback. For the two masters, restore the snapshot copies rather than
re-running `prepare_masters` — the tool is idempotent forward, not backward.

Before relying on B0, confirm `vhaala\veggi` can open all four snapshot DOCX. Hash equality proves
content identity; openability proves the copy did not carry the protected source DACL.

Any instruction anywhere that says "commit per change" is wrong in this repository.

---

## 2. Mechanical verification

### 2.1 Test arithmetic — stated once, precisely

The suite contains **251 tests**. Two of them fail right now, for the reason Codex reproduced and this
package confirmed by source inspection (ISS-14). So:

| Point in the pass | Word COM available | No Word COM |
|---|---|---|
| **Now** | 249 passed / 2 failed / 0 skipped | 239 passed / 2 failed / 10 skipped |
| **After F2 only** | **251 / 0 / 0** | 241 passed / 10 skipped |
| **After the full change set** (+5 tests) | **256 / 0 / 0** | 246 passed / 10 skipped |

Two rules that have caused confusion before and are restated here:

- **Skips are not passes.** If a run reports skips, name each one. The ten Word-COM-scoped skips are a
  session fact, not a converter defect; do not change converter code because one context could not
  activate Word.
- **Do not restate "251" as the post-implementation target.** Five tests are added; if any proves
  redundant with existing coverage, drop it and adjust the arithmetic explicitly in
  `BUILDER_REPORT.md`.

### 2.2 Commands

Run from `C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build`. Use a fresh external
`--basetemp` each time; never reuse one from an interrupted run.

Full suite:

```powershell
.\.venv\Scripts\python.exe -m pytest runtime\tests -q -p no:cacheprovider --basetemp C:\Users\veggi\AppData\Local\Temp\jobbsok-full
```

Adversarial set:

```powershell
.\.venv\Scripts\python.exe -m pytest runtime\tests\test_t09_t12_state_evidence.py runtime\tests\test_t13_t15_merge_leakage_personality.py runtime\tests\test_t16_t18_containment_template.py runtime\tests\test_traceability.py -q -p no:cacheprovider --basetemp C:\Users\veggi\AppData\Local\Temp\jobbsok-adversarial
```

Canonical masters — write once, then dry-run once to prove idempotence:

```powershell
.\.venv\Scripts\python.exe -m tools.prepare_masters
.\.venv\Scripts\python.exe -m tools.prepare_masters --check
```

The first command writes the regenerated masters. The second must report no pending transform; two
identical dry runs add no evidence.

Baseline regeneration proof:

```powershell
.\.venv\Scripts\jobbsok.exe index build
.\.venv\Scripts\jobbsok.exe index verify
```

Template and static-furniture agreement:

```powershell
.\.venv\Scripts\jobbsok.exe preflight
```

Vertical slice, entirely outside the build tree:

```powershell
.\.venv\Scripts\python.exe -m tools.vertical_slice --out C:\Users\veggi\AppData\Local\Temp\jobbsok-vslice-evidence --workdir C:\Users\veggi\AppData\Local\Temp\jobbsok-vslice-work
```

### 2.3 Expected results

| Proof | Expected |
|---|---|
| Full suite, Word COM | **256 passed / 0 failed / 0 skipped** |
| Full suite, no COM | 246 passed / 10 skipped, each skip named |
| Adversarial set | green |
| `prepare_masters` write | both masters written; control contract preserved (17 CV / 7 letter) |
| following `prepare_masters --check` | PASS · 0 reorders · 0 font retargets · 0 page-break removals · **0 typography normalizations · 0 dash normalizations** |
| `index verify` | PASS — byte-identical regeneration of both generated maps |
| `preflight` | PASS — proves D3 and D4 landed together |
| Vertical slice | PASS · 21 steps · 0 unexpected · 4 outputs · `render overall : OK` |

### 2.4 The five new tests

| # | File | Name | Asserts |
|---|---|---|---|
| T1 | `test_t16_t18_containment_template.py` | `test_t16_master_typography_uses_the_discrete_scale` | every `w:sz` in both masters' `word/document.xml` is in `{16, 20, 24, 28, 48}` half-points; `styles.xml Normal` is 24 in both |
| T2 | `test_t16_t18_containment_template.py` | `test_t16_subordinate_zones_are_not_title_formatted` | the content paragraphs of `CV_RELEVANT_BACHELOR_SUBJECTS` and `CV_OPTIONAL_PREVIOUS_EXPERIENCE` carry no `w:b` and no `w:color` override |
| T3 | `test_t16_t18_containment_template.py` | `test_t16_masters_and_baseline_contain_no_en_or_em_dash` | zero `–`/`—` in either master's `w:t` text and in every rendered `baseline_map.json` value except `baseline_provenance` |
| T4 | `test_t19_t23_render_security.py` | `test_t19_previous_employment_line_uses_plain_punctuation` | rendered TIDLIGERE ERFARING lines contain no em dash |
| T5 | `test_t19_t23_render_security.py` | `test_t19_render_stages_beside_destination_with_inherited_permissions` | render requests an inheritance-preserving transaction under `out_dir`; the workspace is removed afterwards |

`test_traceability.py` requires new tests to keep the owning `test_tNN_` prefix; T1–T3 use `test_t16_`
and T4–T5 use `test_t19_`.

**Deliberately not a test:** an ACL assertion. It is not portable across machines and users. ISS-13 is
verified by the human step in §4.2.

---

## 3. The controlled A/B — recovered B0 and projected Run A1

### 3.1 Why only one new typography run is needed

A run's frozen manifest pins its masters, and the pilot cannot be re-rendered with changed masters.
That does **not** require an old-master replay. The current sandbox owns and can byte-read the four
pilot DOCX even though the human account is absent from their protected DACL. Before any implementation,
copy those four files into the external snapshot as **B0** and verify source/copy SHA-256 equality. A
normal copy creates new files under the snapshot's inherited access; it does not mutate the pilot.

After implementation, one fresh **A1** run renders the same semantic fields under the new masters,
baseline, punctuation code and accessible transaction path. This is the lowest-cost controlled pair:
B0 preserves the old bytes; A1 is the only new run required by frozen provenance.

### 3.2 The A1 replay recipe

Pilot semantic artifacts cannot be copied verbatim into a new run because they carry bindings and
finalization metadata. Project only their semantic fields through fresh handoffs, using
`artifacts.MECHANICAL_FIELDS`:

| Artifact | Strip; submit everything else |
|---|---|
| `strategy` | `artifact_role`, `authority`, `elasticity`, `final_writer_may_reconstruct`, `source_escape_permitted`, `binding` |
| `draft_package` | `artifact_role`, `source_stage`, `binding`, `finalization` |
| `final_package` | `artifact_role`, `source_stage`, `binding`, `finalization` |
| `review` | `artifact_role`, `binding` |

Per job, in stage order:

1. `jobbsok freeze` from a `batch_input.csv` naming the same two vacancies; cluster `verify_a1`;
   `--reviewed-by "Vegard Håland"` only after the genuine human attestation.
2. Get fresh `jobbsok context --stage 1`; use its `write.return_paths` and `write.semantic_fields`.
3. Project the pilot `strategy.json` minus its mechanical keys into that return path and execute the
   emitted `submission.command` **verbatim**.
4. Repeat for Stage 2 and Stage 3 (`final_package` + `review` together), always from fresh context.
5. Immediately `jobbsok finalize`, then `jobbsok render` for each successful Stage-3 commit.

No model calls. `used_evidence_refs` resolve because `evidence_index.json` remains byte-identical.
A1 deliberately carries the pilot's known semantic defects; holding semantic content constant is the
point. A1 is typography/punctuation/access verification, **not** acceptance of B, C or E.

### 3.3 What B0 and A1 prove

| Evidence | Proves |
|---|---|
| **B0** — hash-equal accessible copies of the retained pilot DOCX | exact old typography and static/deterministic punctuation on the real pilot content |
| **A1** — fresh projected run after the complete implementation | outcome A; deterministic/static parts of D; parseability; actual page counts; F1 output access; controlled visual comparison against B0 |

### 3.4 Mechanical acceptance from Run A1

| Check | Criterion |
|---|---|
| CV page count | normally **2** for these pilot contents. A third page is accepted only after semantic compression and canonical spacing/flow review show that forcing 2 would reduce employer-facing quality. |
| Letter page count | **1** |
| Page warning | none for either document |
| Extracted text, all four documents | zero `–`, zero `—` |
| `render_state.overall` | `OK` — both DOCX and both PDFs |
| Parseability (`GATE-06`, `DEC-39`) | identity, contact and logical reading order extractable from both PDFs |
| Identity, chronology anchors, override bullets | all `_verify_docx` checks true |
| No residual SDT or placeholder | true |

---

## 4. Human acceptance — required, not advisory

### 4.1 Typography and layout (outcome A) — and `VISUAL_HUMAN`

Open B0 and A1 side by side in the same view and zoom. Prefer PDFs if the interactive Word session
can export B0; otherwise use Word print layout for both DOCX. Judge:

- body text legible at normal reading distance and on screen;
- hierarchy visibly intact: **name > section headings > body and record titles > subordinate detail**;
- page 2 of the CV meaningfully populated rather than a stub;
- **TIDLIGERE ERFARING no longer competes with the section headings** (ISS-04) — it should read as
  clearly subordinate;
- no orphaned heading, no widow line, no clipped bullet, no blank page;
- the letter's address block reads as metadata, not as body.

This is also the moment `VISUAL_HUMAN` / `ACC-18` and Spec §16.7 are discharged — on **real content**,
which they never have been. Record the result in `BUILDER_REPORT.md`.

Guard in the other direction: if 12 pt body at `w:line="252"` reads cramped, that is the trigger for
the single canonical `w:line` adjustment held in reserve under A5. Measured, not assumed.

### 4.2 Output accessibility (ISS-13)

After A1, inspect each promoted file with `Get-Acl`: it must no longer carry the protected
creator-only DACL, and `vhaala\veggi` must have inherited/effective read access. Then, as
`vhaala\veggi`, open **both DOCX directly from `runs/<run>/jobs/<job>/out/`** in Word with no copy
step. Both conditions are required. If the sandbox owner alone can read the file, F1 did not work.

### 4.3 Professional voice (outcome E) — blind A/B

Present the pilot letter and the Run B letter for the same vacancy **side by side and unlabelled**.
Ask one question: *which is more plausibly written by me?*

This is the only honest test of outcome E, and it belongs to the candidate.

**Guard against over-application.** If the Run B letter reads as *more* performed, more analytical, or
more conspicuously styled than the pilot, the voice conditioning is too strong and
`FORFATTERSTEMME.md` must be softened — not the change set reverted. Voice that draws attention to
itself has failed on its own terms; `§ Anti-karikatur` says employer persuasion and readability
outrank visible personality.

### 4.4 Pilot log (ISS-15)

After reviewing each Run B package, append one row per job to `pilot/PILOT_LOG.csv`: triage, actual
repair scope, submit-ready, factual corrections, minutes through the submission decision, render
issues, friction, outcome. The 19 columns already exist; this is hand-written.

Without these two rows this pass has **no measurement of whether it reduced human repair effort**, and
the representative cluster will produce none either. `ACC-20` and Spec §18.3 have been owed since the
pilot.

---

## 5. Run B — semantic acceptance

Run B is a fresh freeze with fresh Stage 1/2/3 under the new policies, same two vacancies. It is the
only run that exercises outcomes B, C and E.

### 5.1 The properties, not the surfaces

The first draft of this plan required "no mission paragraph" and "letters that do not share a closing
formula or macro-structure". Both were wrong: the first bans a legitimate Avinor paragraph, the second
rewards difference for its own sake and could make one letter worse to keep it unlike the other. The
corrected criteria test properties.

**1. Earned motivation (B).**
Is every motivation sentence traceable to the actual work, the decision problem, the operating
environment, or a documented candidate motive? Where mission or societal language appears, does it
name a **causal feature of the work** — something that changes what must be done, what the constraints
are, or what "done well" means — rather than restate the employer's value proposition?

> **Avinor's societal-purpose paragraph surviving is a positive acceptance signal, not a failure.**
> Huseierne's slogan-derived motivation sentence must be gone.

**2. Truthful leverage (C), checked in both directions.**
*Upward:* the `PRJ-04` durability claim reads `fortsatt i bruk` or an equally strong evidence-defensible
form, with `om lag` and the `2,5 år senere` horizon preserved and no documentation-provenance frame.
*Downward:* no claim anywhere in either package now exceeds its authority ceiling, and each review's
`known_limitations` is still accurate. The second half matters more than the first — over-correction
into overclaiming is a worse defect than the understatement being fixed.

**3. Vacancy-driven structure (ISS-10).**
Judged on **`structure_guidance`, not the letter's silhouette**. Two jobs may legitimately converge on
the same shape if both genuinely need it. The failure signal is a `structure_guidance` that would read
identically for any employer — i.e. a letter template rather than this vacancy's argument.

**4. Authentic voice (E).**
The blind A/B of §4.3.

**5. No new generic residue (ISS-09, ISS-11).**
The three patterns named in `FORFATTERSTEMME § Mønstre som skal erstattes` are absent, *or* deliberately
retained with a better reason. **This is not a lint**; a mechanical phrase check is forbidden by
`INV-07` and Spec §10.3.

**6. Plain punctuation (D).**
All Run B employer-facing text contains zero en dash and zero em dash. Ordinary hyphens remain only
where normal Bokmål calls for them (compounds, dates and ranges), not as clause dividers. This is
checked in extracted output and by reading the sentence in context; no runtime validator is added.

**7. Regression guard.**
Nothing that was already good may get worse. Specifically, the Avinor sentence

> *"forventninger må gjøres etterprøvbare, ansvar og antakelser må være synlige, og metoden må fungere
> for dem som skal bruke den"*

is the strongest existing evidence of the candidate's professional voice. If Run B loses that quality,
the change set is over-applied.

**8. No mechanical regression.**
Both jobs reach `VALID` / `FINAL` / current final+review; render `OK`; any page warning has an explicit
human disposition; triage calibrated the same way (a shift to `CHECK` on both jobs would suggest the new rules made the model
defensive, which is itself a finding).

### 5.2 Comparison against the original pilot

Required by the stopping rule: no material regression in truth, tailoring, render stability, workflow
or handling; and the targeted defects materially improved. Compare Run B against the pilot finals on:
claim ceilings held, employer specificity, CV/letter complementarity, evidence selection quality,
`known_limitations` accuracy, and operator minutes from the pilot log.

---

## 6. Sequence

| Step | Work | Gate before proceeding |
|---|---|---|
| 0 | SHA-256 registry + external snapshot (including current pilot log); copy pilot DOCX → B0 | 21 paths recorded (`ABSENT` for new E1), 20 existing targets copied; all four B0 hashes equal their pilot sources; pilot unchanged |
| 1 | **F2** | suite **251 / 0 / 0** with COM |
| 2 | **D1, D2, F1** + T4, T5 | focused tests green; suite still green |
| 3 | policy: A3, B1–B3, C1, C2, D5, E1, E2, RUNBOOK, version bumps | `FORFATTERSTEMME.md` reviewed by Vegard; no motivation/fact claims in it |
| 4 | **D3** → `index build` → `index verify` | `index verify` PASS |
| 5 | **A1, A2, D4** via one writing `prepare_masters` run and one `--check` dry run; `preflight`; T1–T3 | dry run shows zero pending transforms; control contract preserved; **both masters open in Word**; preflight PASS |
| 6 | projected **Run A1**; output DACL/openability; B0/A1 visual A/B | §3.4 mechanical + §4.1–4.2 human |
| 7 | full suite, adversarial set, vertical slice, scope gate | **256 / 0 / 0**; `06_…md` §6 budget met |
| 8 | **Run B**; semantic review; two pilot-log rows | all eight §5.1 criteria |
| 9 | one representative cluster | §7 |

---

## 7. Representative-cluster gate

The pass is not finished at Run B. One representative cluster — more than two jobs, mixed
priority — is the last gate before returning to ordinary production. It tests what two jobs cannot:

- **throughput**: whether the new policy load materially increases per-job cognitive complexity,
  refusal rate or human review burden. A fix that produces excellent two-job output and slows the
  cluster is a net regression;
- **cross-job convergence at scale** (`EXP-07`): whether letters converge once more jobs share a
  context window. Observed by the human; no detector exists and none may be built;
- **triage calibration** (`EXP-06`): whether `READY` still means what the pilot log says it meant;
- **typography under content variation**: whether a denser CV pushes past 2 pages, and whether A3's
  compression rule actually gets applied.

Write a `PILOT_LOG.csv` row for every job in the cluster.

---

## 8. Success and failure criteria

### 8.1 Success

1. Suite **256 / 0 / 0** with Word COM; skips named if run without.
2. One writing `prepare_masters` run followed by one zero-diff `--check`; control contract preserved;
   **both masters open in Word**.
3. `index verify`, `preflight` and the vertical slice PASS.
4. Run A1: pilot CVs normally 2 pages and letters 1 page; any extra page passes only under the
   readability-over-fit rule above; zero `–`/`—` in all four extracted texts; `render overall : OK`;
   parseability intact.
5. Human visual A/B: A1 more readable than B0, hierarchy intact, page 2 populated, TIDLIGERE ERFARING
   subordinate.
6. Both DOCX open directly from `out/` with no copy step.
7. Run B: all eight §5.1 criteria met, including punctuation and the regression guard.
8. Blind A/B: Run B letter judged more plausibly candidate-authored, without reading as performed.
9. Two `PILOT_LOG.csv` rows written.
10. Scope gate: changed-file list matches `02_…md` §1 exactly; `06_…md` §4 reads "No" on every row.

### 8.2 Stop and escalate

| Condition | Action |
|---|---|
| Control contract changes (≠ 17 CV / 7 letter) | the master edit is wrong; do not force it |
| Either master fails to **open in Word** | highest-risk check — the P0.7 masters parsed in LibreOffice while Word rejected them; revert the master and re-derive |
| `preflight` fails after step 6 | D3 and D4 are out of agreement; fix, never relax the assertion |
| `index verify` fails | the baseline edit broke byte-identical regeneration |
| Suite not 251/0/0 after step 1 | stop before anything else lands |
| CV renders 3+ pages | compress semantics first, then review canonical spacing/section flow; if 2 pages would lose decision signal, accept the extra usable page and record the warning. **Never** reduce main-prose type size. |
| Run B worse than the pilot on truth, tailoring or the regression guard | soften `FORFATTERSTEMME.md`; do not revert the whole set |
| Run B triage shifts to `CHECK` on both jobs | the new rules made the model defensive — a finding, not a pass |
| Any change appears to require an architecture amendment | stop; escalate against the exact governing ID with target-machine evidence. Never resolve by silent deviation. |

---

## 9. Stopping rule

### 9.0 STEP-9 viability review — plan frozen

| Adversarial question | Final answer |
|---|---|
| Does the plan solve the reproduced weaknesses rather than restate policy? | Yes. A edits the actual inline/master typography; B changes routing/salience while leaving already-sufficient doctrine alone; C adds only the missing speaker-transposition clarification; D fixes each observed source; E supplies the missing expression source; F repairs the identity boundary and test fixtures. |
| Is employer-facing quality the tiebreaker? | Yes. Readability, authentic authorship and truthful force dominate page compactness, stage symmetry and mechanism elegance. |
| Does anything weaken truth/evidence? | No. The voice file has no fact/claim/qualification/strategy authority; Stage 1 remains evidence-bound; C retains approximation, horizon and lifecycle limits; Run B checks inflation as well as attenuation. |
| Does anything blur stage ownership? | No. Stage 1 selects strategy, Stage 2 drafts, Stage 3 owns final authorship/review. The voice file is visible through existing routing, but Stage 1 is explicitly a non-consumer and no artifact ownership changes. |
| Is any complexity unnecessary? | The final scope removed three such candidates: duplicate B doctrine, a runtime dash warning and a separate A0 run. The remaining new file is the smallest reviewable candidate-specific voice source; F1's optional transaction mode is required because a path-only fix fails on Python 3.14. |
| Is any simplification too narrow? | No. B and C address both origin and final repair point; E covers authorial construction plus anti-anchoring, not cosmetic word replacement; A changes both inline CV runs and the letter's style dependency. |
| Is voice likely authentic rather than cosplay? | Plausible but empirical. It is moderate, expression-only, profile-derived, anti-caricatured and candidate-reviewed; blind Run B A/B is the release gate. |
| Is 12 pt viable without destructive loss? | Modelled yes, unproven visually. A1 measures it; compression precedes any page concession, and type never shrinks below the canonical target to force fit. |
| Can the two pilot jobs verify every change? | Yes for mechanism and the targeted semantic properties: B0/A1 verifies A, deterministic D and F1; fresh Run B verifies B, C, semantic D and E. Cluster-only recurrence/throughput claims remain explicitly unproven. |
| Is cluster throughput viable? | Unknown by design because the pilot log is empty. One representative mixed-priority cluster with a row per job is the final empirical gate; no monitoring or similarity subsystem is added. |
| What can a hostile reviewer still object to? | Voice strength, 12 pt page balance, Windows ACL behavior and the 21-file surface. Each has a bounded proof or rollback condition; `01_…md` §9 records the detailed answers. |
| What remains empirical? | Actual Word pagination/balance, candidate-authorship effect, over-application of C, target-identity ACL access and cluster throughput/convergence. These are gated, not engineered speculatively. |

No load-bearing contradiction remains. This review freezes the design; no further ideation belongs in
this pass.

**This is the final pilot-informed optimization pass.** After Run B and one representative cluster,
framework iteration stops.

Iteration may resume only on **repeated real-production evidence** of a material blocker that also
beats the smallest local remedy. A single stylistic preference, a one-off model output, or a defect
cheaper to fix by hand than to engineer away is not a blocker.

### 9.1 Deliberately deferred to real production

| Item | Why deferred |
|---|---|
| Cross-job convergence at cluster scale | `EXP-07`; two jobs cannot show it, and no detector may be built |
| Triage calibration against actual human edits | `EXP-06`; needs pilot-log rows across several clusters |
| Whether `FORFATTERSTEMME.md` needs sample grounding | profile-derived version ships first; refine only if the blind A/B shows a specific miss |
| Master line-spacing adjustment | held in reserve under A5; apply only if the visual review shows the body cramped |
| The dormant `converter = "auto"` branch | production uses `word_com`; removal would touch config, schemas, runtime and tests without helping |
| The six dead settings keys (F22) | deliberated and deferred; none causes a production failure |
| Adding `warnings` to `status --json` | needs a schema edit (F10) |
| Automatic pilot-log tooling | a RUNBOOK line is the smallest local remedy; revisit only if the rows stop being written |

### 9.2 What "done" means

> The system produces employer-facing packages whose remaining imperfections are cheaper to handle
> manually than to engineer away.

Not theoretical perfection. When Run B and the representative cluster meet §8.1, the framework work
ends and the system returns to producing real applications.
