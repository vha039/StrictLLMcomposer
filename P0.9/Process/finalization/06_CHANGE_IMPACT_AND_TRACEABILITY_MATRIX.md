# 06 — Change impact and traceability matrix

**Status:** planning material. Not authority.
**Purpose:** map every change against every affected framework surface, architecture clause, pilot
issue, test and acceptance proof — and state explicitly what is **not** touched.

---

## 1. Change → issue → outcome → file → test → acceptance

| Change | Mandatory outcome | Issue(s) | File(s) | Test(s) | Acceptance proof |
|---|---|---|---|---|---|
| A1 typography table | A | ISS-01, 03, 04, 16 | `tools/prepare_masters.py`, both masters | T1, T2 | Run A1 PDF + human visual A/B |
| A2 `styles.xml` | A | ISS-01, 02 | both masters | T1 | letter renders at 12 pt, 1 page |
| A3 doctrine paragraph | A | ISS-01, 16 | `WRITING_DOCTRINE.md` | — (semantic) | Run B: no package shrinks type to fit |
| A4 page targets unchanged | A | ISS-16 | — | existing | advisory warning fires only above target |
| A5 spacing unchanged | A | ISS-01 | — | — | visual review confirms not cramped |
| B1 Stage-1 motivation pointer | B | ISS-05 | `stage1_…md` | — (semantic) | Run B `motivation_bridge` |
| B2 Stage-3 named-section/swap-test salience | B | ISS-05 | `stage3_…md` | — (semantic) | Run B review reasoning cites no mission wording as pass evidence |
| B3 Stage-1 `structure_guidance` anti-template sentence | B, E | ISS-05, 10 | `stage1_…md` | — (semantic) | Run B `structure_guidance` |
| C1 provenance-voice clarification | C | ISS-06 | `PERSUASION_CALIBRATION.md` | — (semantic) | Run B framework claim, both directions |
| C2 symmetric repair duty | C | ISS-06 | `stage3_…md` | — (semantic) | Run B; `review.upstream_claim_repaired` may now populate |
| D1 em dash → period | D | ISS-07 | `render.py` | T4 | zero em dashes in extracted text |
| D2 metadata dashes | D | ISS-07 | `render.py` | T3 (indirect) | `docProps` inspection |
| D3 baseline normalisation | D | ISS-08 | `CV_BASELINE.md`, `baseline_map.json` | T3 | `index verify` PASS |
| D4 master furniture + leakage string | D | ISS-08 | both masters, `leakage.py` | T3 | `preflight` PASS |
| D5 `Tegnsetting` | D | ISS-12 | `WRITING_DOCTRINE.md` | — (semantic) | Run B: no clause hyphens |
| E1 expression-only `FORFATTERSTEMME.md` | E | ISS-09, 11 | new file | — (semantic) | Run B blind A/B |
| E2 Stage-2 light prior; Stage-3 ownership/anti-anchoring | E | ISS-09, 11 | `stage2_…md`, `stage3_…md` | — (semantic) | Run B |
| F1 accessible atomic staging | — | ISS-13 | `atomicio.py`, `render.py` | T5 | target DACL check + human opens both DOCX from `out/` |
| F2 fixture-owned mapping | — | ISS-14 | `conftest.py`, `test_t05_t08_…` | modified | suite 251/0/0 before anything else |
| RUNBOOK line | — | ISS-15 | `RUNBOOK.md` | — | two `PILOT_LOG.csv` rows after Run B |

Every mandatory outcome A–E is covered, and every issue in `03_…md` maps to at least one change except
ISS-16, which is explicitly **merged into A1** rather than given a redundant second remedy.

---

## 2. STEP-8 framework impact sweep

Impact-driven, not permission to reopen settled subsystems. Each row states whether a proposed change
creates or exposes a material issue, and the mitigation if so.

| Surface | Impacted? | Analysis |
|---|---|---|
| **Intake / `batch_input.csv` / freeze** | Indirect | Two new runs are frozen: projected replay A1 and fresh semantic Run B. `freeze` requires a genuine human `--reviewed-by` attestation. B0 is a byte-identical external snapshot copy of existing pilot DOCX, not a run and not a pilot mutation. |
| **Frozen-input manifest / provenance** | **Yes** | `frozen_inputs.writing_policy` gains a third element automatically (glob + unbounded array). `stage_policy_sha256` changes for all three stages in **future** runs. Existing manifests, handoffs and receipts are untouched. No schema, code or manifest change. |
| **Schemas / artifact ownership** | No | No schema is edited. `manifest.schema.json` `"const": "0.9.0"` revisions unchanged (F14). `INV-09` stage write ownership unchanged. `TOOLING_OWNED` unchanged. |
| **Stage 1 context / strategy / personality** | **Yes** | `stage1_…md` gains a field→section map and two sentences. `strategy.schema.json` unchanged; no field added, removed or retyped. The personality 0–3 facet interface is untouched. |
| **Stage 2 drafting** | **Yes, one sentence** | `stage2_…md` acknowledges `FORFATTERSTEMME.md` as a light prior. This is a stage-responsibility clarification forced by the routing reality (`01_…md` §5), not a new obligation. |
| **Stage 3 reconstruction / review** | **Yes** | Named-section salience, symmetric repair duty, independent pre-draft authorship decision and voice-file naming. Elasticity, triage semantics and `READY` calibration are unchanged. `review.schema.json` unchanged; no numeric field is added. |
| **Writing / persuasion doctrine** | **Yes** | Two insertions in `WRITING_DOCTRINE.md` (A3 and D5), one concise provenance bullet in `PERSUASION_CALIBRATION.md`, one new expression-only file. Outcome B doctrine is unchanged. No English rubric anywhere. |
| **Candidate factual authorities** | **No** | `Work_experience.md`, `Education.md`, `Other_high_value_information.md` are **not edited**. `CV_BASELINE.md` is edited, but it is a `MECHANICAL_BASELINE`, not a factual authority, and the edit is glyph-level plus two unit names. `INV-03` intact. |
| **Templates / style map / control contract** | **Yes** | Both masters regenerated. 17 CV / 7 letter controls verified before write. `template_map.json` untouched. `GATE-06` parseability re-proven by Run A1 text extraction. |
| **Finalization / date semantics** | No | `cmd_finalize` untouched. `DEC-38` date ownership untouched. Idempotence (F5) preserved. |
| **Rendering / page warnings / PDF receipts** | **Yes** | `render.py` changes D1, D2 and the F1 call site; `atomicio.py` gains one default-false transaction option. Render-state derivation, warnings, `DEC-41`, `promote_file`, `ACC-17` and `verify_receipt` are untouched. |
| **Status / next / continuation** | **Indirectly improved** | No code change. `status --json` output paths become readable once F1 lands, and `verify_receipt` can re-hash outputs again. `status.schema.json` is closed (F10) and is not edited. |
| **Recovery / failure handling** | No | `failure.py`, the bounded-recovery ladder and `BLOCKED_MANUAL` are untouched. |
| **Cross-job reset / isolation** | No | The Stage-1 and Stage-3 reset paragraphs are unchanged; the pilot showed them working (different facets, evidence order and competencies per job). B3 changes `structure_guidance` guidance, not isolation. |
| **Pilot instrumentation** | **Yes** | One RUNBOOK line plus a Run B acceptance obligation. No tooling; `[paths].pilot_log` stays unwired per the F22 deferral. |
| **Operator workflow / handling minutes** | **Improved** | F1 removes the copy-out step entirely. The pilot-log row adds ~1 minute per job and is the only instrument that will show whether the semantic changes reduced repair effort. Net effect expected negative on handling time. |
| **Security / containment** | **Improved** | Render alone opts into parent-inheriting staging under authorized `out_dir`; private rollback staging is unchanged. Canonical output remains within `runs`, and authorized `--dest` remains governed by existing resolution. |
| **Test / traceability system** | **Yes** | Five new tests plus two repaired. `test_traceability.py` keeps owning `test_tNN_` prefixes; T1–T3 use `test_t16_`, T4–T5 use `test_t19_`. Total goes 251 → 256. |
| **Architecture documents** | **No** | `P0.9/Architecture/*` is not edited. No amendment. |
| **Child runs / `branch`** | No | `branch.CONTENT_GOVERNING` already lists `("writing_policy",)` for all four artifacts, so the new file participates correctly in rebind decisions with no edit. |
| **Evidence index** | No | The three authorities are unchanged, so `evidence_index.json` regenerates byte-identical. `used_evidence_refs` resolve unchanged, which is what makes the Run A replay possible. |
| **Vertical slice / gates** | **Yes** | The slice must be re-run after the master change. `GATE-02` control contract, `GATE-05` fonts/layout and `GATE-06` parseability are re-discharged. `VISUAL_HUMAN` / `ACC-18` is discharged for the first time on real content by the B0/A1 review. |

---

## 3. Architecture clause traceability

| Clause | Relationship to this pass |
|---|---|
| Spec §22.1 frozen list | untouched. Authority precedence, product/language boundary, three-stage semantics, Stage-3 elasticity, **personality ON/0–3 interface**, job-as-transaction, artifact roles, three state axes, `READY/CHECK/RERUN`, DOCX/PDF degradation, date ownership, parseability outcome, human irreversible authority — all unchanged. |
| Spec §22.2 builder freedom | **relied on** for A1, A2, D4 (*"template layout changes proven by target-machine gates"*) and for module topology in D1, D2, F1. |
| Spec §22.3 amendments | not invoked. No frozen rule changes. |
| Spec §4.5 interpretive context | **relied on** — writing guidance and persuasion calibration are advisory and may guide expression without establishing facts. |
| Spec §10 personality interface | untouched; `01_…md` §5.4 gives the point-by-point comparison. |
| Spec §12.5 `DEC-24` page behaviour | **relied on** and refined from inside by A3; no hard limit added. |
| Spec §13 Stage 3 | elasticity preserved; C2 makes an existing repair duty symmetric. |
| Spec §16.2 `DEC-21` render transaction | **conformance increased** by F1 — step 6 says *"write to a temporary job path"*. |
| Spec §16.5 `DEC-39` parseability | re-proven by Run A1 text extraction. |
| Spec §16.7 render verification | `VISUAL_HUMAN` discharged on real content. |
| Spec §17.2 / Contract §15 containment | preserved; `runs` is already a writable root. |
| Spec §5.6 idempotency/atomicity, `GATE-08` | preserved and strengthened — the same-volume rename is now guaranteed by construction. |
| Spec §10.3 / `INV-07` | **honoured explicitly** — D5 and E1 state that style guidance must never fail deterministic validation; no runtime style warning is added. |
| `INV-03` factual authority | untouched; the authorities are not edited. |
| `INV-08` engineering ≠ product evidence | honoured; no mechanical result is cited as product quality anywhere in this package. |
| `INV-09` stage write ownership | untouched. |
| `DEC-23` baseline ownership | preserved; the human edits `CV_BASELINE.md`, no stage does. |
| `DEC-31` no fit score | untouched. |
| `DEC-35` personality ON | untouched. |
| `DEC-41` PDF degradation | untouched. |
| `DEC-42` three axes | untouched. |
| `ACC-17` human-edit protection | untouched; `promote_file` unchanged. |
| `ACC-18` / `VISUAL_HUMAN` | **discharged** by the B0/A1 review. |
| `ACC-20` / Spec §18.3 pilot log | **moved toward compliance** by the RUNBOOK line and the Run B obligation. |
| Contract §3 repository roles | **relied on** — `policy/` is *"settings, writing/persuasion rules and stage instructions"*. |
| Contract §12 personality implementation | untouched; no score, no ranking, no cross-job trait memory, no full-profile injection. |
| Contract §13.3 single template map | preserved; `template_map.json` is not edited. |
| Contract §22 prohibited redesigns | checked item by item in §4 below. |

---

## 4. Prohibited-redesign checklist

Contract §22, every item, against this change set.

| Prohibited | Present? |
|---|---|
| `letter_required`, CV-only or conditional core outputs | No |
| language / platform / portal / channel / component branches | No |
| portal answer schemas | No |
| automatic exception thresholds | No |
| same-run amend or manifest versions | No |
| event sourcing, history replay, databases, dependency engines | No |
| authoritative progress/status files or completion markers | No |
| a dedicated RERUN workflow or schema | No |
| automatic model execution / retry / orchestration | No |
| reason-count routing | No |
| hard semantic word/cardinality limits without a verified consumer | No — A3 explicitly adds none |
| exhaustive byte-partition indexing | No |
| per-job authority copies, cross-job personality memory, independent semantic memory | No — `FORFATTERSTEMME.md` is a static human-maintained control-plane input, not memory |
| model-generated settings compilers, prompt caches, source-filtering artifacts | No |
| factual evidence refs to `CV_BASELINE` | No |
| semantic support claims from reference resolution | No |
| personality OFF/stub default, trait scoring, **full-profile repeated injection** | No — see `01_…md` §5.4 |
| convergence/similarity detector | No — explicitly rejected for ISS-10 |
| PDF failure as semantic failure, `DOCX_ONLY` mode | No |
| universal body-flow identity duplication | No |
| document date at freeze or render-time drift | No |
| numeric quality/fit judge | No — E1 contains no score |
| autonomous network / contact / submission behaviour | No |
| P0.7/P0.8 compatibility for its own sake | No |
| optionality-only experiment hooks | No |

---

## 5. Unchanged surfaces — stated explicitly

### 5.1 Files not touched

`P0.9/Architecture/*` (all four) · every file in `schemas/` · `templates/template_map.json` ·
`policy/settings.toml` · `policy/personality_facets.json` · `context/PERSONALITY_PROFILE.md` ·
`authorities/Work_experience.md` · `authorities/Education.md` ·
`authorities/Other_high_value_information.md` · `runtime/jobbsok/`: `artifacts.py`,
`baseline.py`, `batchinput.py`, `branch.py`, `cli.py`, `docxfill.py`, `errors.py`,
`evidence_index.py`, `failure.py`, `hashing.py`, `ioenc.py`, `manifest.py`, `merge.py`, `paths.py`,
`pdf.py`, `schemas.py`, `settings.py`, `status.py`, `vacancy.py`, `validate.py` ·
`runtime/tools/make_fixtures.py`, `vertical_slice.py` ·
`runtime/tests/`: `test_t01_t04_…`, `test_t09_t12_…`, `test_t13_t15_…`, `test_traceability.py` ·
`runs/r20260828-213932-7f13b4/**` · `runs/r20260823-050000-fea486/**` ·
`evidence/gates/GATE-02/original_p07_masters/**` · `evidence/gates/GATE_REPORTS.md`.

Note that **`cli.py` is not edited**. No dash warning is added, and the voice file needs no context
code because `cmd_context` already emits every writing-policy path.

### 5.2 Behaviour not changed

No new command, subcommand or flag · no new schema or schema field · no new state axis or status field
· no new dependency · no new runtime module · no automatic retry or orchestration · no approval
abstraction · no hard threshold · no numeric score or LLM judge · no similarity detector · no
migration or compatibility shim · no change to triage semantics, `READY` calibration, render-state
derivation, promotion/no-clobber behaviour, date assignment, recovery ladder, cross-job reset, or
evidence-reference semantics.

### 5.3 Reproduced but deliberately not fixed

| Observation | Why left alone |
|---|---|
| Two byte-identical CV bullets across both jobs | shared facts are legitimate; these are specific, not generic wording (`03_…md` §17) |
| Avinor's societal-purpose motivation paragraph | grounded in an operating condition under the existing `Begrunnet motivasjon`; **must survive** |
| Header and footer at 8 pt | deliberately subordinate running furniture, in the user's scale |
| Six `source: none` template zones | render as absent, working as designed |
| `Heading2`, `Heading3`, `BodyText*`, `List*`, `Quote`, `MacroText`, `Caption` and all character styles | applied by no paragraph in either master |
| Dormant `converter = "auto"` | deferred; production uses `word_com` |
| Six dead settings keys (F22) | deliberated and deferred |
| Superseded receipt represented as `FAILED` | settled; a `NOT_RENDERED` variant was implemented, tested and reverted |
| `reviewed_by` / `finalized_by` naming | settled by RUNBOOK wording |

---

## 6. Scope gate

Before declaring the implementation done, confirm the changed-file list matches
`02_…md` §1 exactly — 21 implementation-controlled file diffs plus human pilot-log data; two are
regenerated binaries, while the evidence-index rewrite remains byte-identical and outside the diff —
and that §4 of this file still reads "No" on every row.

| Axis | Budget | Expected actual |
|---|---|---|
| new dependencies | 0 | 0 |
| new commands / flags | 0 | 0 |
| schema edits | 0 | 0 |
| new runtime modules | 0 | 0 |
| new status fields / state axes | 0 | 0 |
| architecture edits | 0 | 0 |
| new control-plane files | 1 | 1 (`FORFATTERSTEMME.md`) |
| edited runtime modules/tools | ≤4 | 4 (`render.py`, `atomicio.py`, `leakage.py`, `tools/prepare_masters.py`) |
| regenerated binaries | 2 | 2 (both masters) |
| new tests | 5 | 5 |
| implementation-controlled file diffs | 21 | 21 |
| human data writes after Run B | 1 | `pilot/PILOT_LOG.csv` |
