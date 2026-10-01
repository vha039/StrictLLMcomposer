# Implementation context handoff — Jobbsøk_26 P0.9

Read this once, fully, before the spec. It is the minimum model of the system needed to execute the
25 mandatory edits (29 with all optional edits) correctly. The guidance owns payloads; the current execution prompt owns scope and stopping.

---

## 1. What the system is

A 2-stage pipeline that produces **exactly two employer documents per vacancy**: one CV, one
Norwegian cover letter (`søknad`). Both Bokmål. No language/portal/channel branch, ever.

| Stage | Role | Writes | Reads |
|---|---|---|---|
| **1** Decision Architecture | strategy hypothesis | `strategy.json` | vacancy + 3 factual authorities + baseline map |
| **2** | **RETIRED** | — | — |
| **3** Elastic Final Writer + Review | the actual CV/letter + triage | `final_package.json`, `review.json` | strategy (option value, not authority) + authorities + writing policy |

Stage 3 may override Stage 1 entirely. Strategy is a hypothesis, never authority.

Then: `finalize` (assigns canonical date) → `render` (fills Word masters → .docx, optional .pdf).

**Root:** `C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build` — all relative paths below
are from there. Referred to as `B/`.

```
policy/       settings.toml · stages/stage1_decision_architecture.md
              stages/stage3_final_writer_review.md · writing/{WRITING_DOCTRINE,
              PERSUASION_CALIBRATION,FORFATTERSTEMME}.md · personality_facets.json
authorities/  Work_experience.md · Education.md · Other_high_value_information.md
              ^^ sole factual authorities; CV_BASELINE.md is derived, not factual authority.
              No plan step edits authorities/.
context/      PERSONALITY_PROFILE.md
prompts/      STAGE1_PROMPT.md · STAGE3_PROMPT.md      (operator-facing chat prompts)
templates/    CV_MASTER.docx · APPLICATION_MASTER.docx · template_map.json
schemas/      package · review · strategy · manifest · ... .schema.json   DO NOT EDIT.
runtime/      jobbsok/*.py (CLI+render+docxfill) · tools/prepare_masters.py · tests/
evidence/     gates/GATE-02/* · finalization/HASHES.sha256
runs/         r<date>-<hex>/ per run:  frozen/  jobs/  manifest.json  branches/
generated/    baseline_map.json · evidence_index.json · handoffs/ · returns/
```

**Doc shorthand used throughout the spec:** `D` = WRITING_DOCTRINE.md, `K` = PERSUASION_CALIBRATION.md,
`V` = FORFATTERSTEMME.md, `S1`/`S3` = the stage instruction files.

---

## 2. The immutability model — the single most important thing to internalise

**Selected inputs are frozen.** `manifest.py:217–270` enumerates the snapshot: authorities, baseline,
profile/facets, settings, stage/writing policy, schemas, masters/map and two generated maps.
`FrozenRunAssets` resolves those copies. Runtime code and `prompts/` are **not snapshotted**.

**Editing live `B/policy/...` leaves existing frozen policy unchanged.** Those maintained inputs
reach execution only through a new or child run (`DEC-40`).

Consequences you must act on:
- All selected edits are **source maintenance**. Frozen-input changes need a new/child run;
  runtime and operator-prompt edits take effect live. Do not exercise existing runs during maintenance.
- There is exactly **one run boundary**, at the very end, and **the human owns it**. You never run
  `freeze`, `branch`, `finalize`, `render`, or create a child.
- Never edit anything under `runs/`. Frozen bytes are evidence.

---

## 3. Why this plan exists (motivation, compressed)

Nine CV+letter packages were generated for one real vacancy (Avinor, Seniorrådgiver Digital
Transformasjon). Same candidate, **two frozen authority generations**: later confirmations entered
on 2026-09-06. Cross-generation differences do not isolate framework causation (V41).

What the corpus showed, and what the plan targets:

| Finding | Plan response |
|---|---|
| Role functions unevenly covered — deep on benefit models, thin on facilitation/communication to decision-makers | **M01** sharpen allocation in D/S1/S3 + explain omissions in existing `review.notes` |
| Poor selection can't be fixed by a late polish pass | **M02** explicit substantive pair edit **before** content lock |
| Unknown status written as negative fact (*"ikke innført"*); redundant "I lack X" clauses | **M03** K correction: unknown ≠ absent; gap rule applies to clauses, not just paragraphs |
| Absolute employer-uniqueness test forced artificial motivation | **M06** defensible role connection instead |
| No tunable control over social register / self-importance | **M04** operator dial, **content-locked final polish only** |
| Bold 78-word competence wall; duplicate letter title; low-value CV tail first | **M05** master + map + consumer maintenance |

---

## 4. The constraint constitution — why the plan looks restrained

Live rules below plus the execution scope reject schema growth, new validation machinery,
detectors and probe renders. E12a is a specified check in the **existing settings loader**.

| Rule | Source |
|---|---|
| Deterministic code must **never** fail a package because a formulation, string or character occurs | `D:40-42` |
| **No automatic similarity detector** may be built | `D:496-498` |
| Page/count targets are **editorial signals, never validation limits** | `D:331-352`, `settings.toml:72-79`, DEC-24/33 |
| Nothing may branch the product (no language/portal/channel/output-mode switch) | `settings.toml:7-9`, DEC-01/02/04 |
| `K` accepts **only explicit reusable corrections from Vegard** → Cluster B is owner-gated | `K:11`, `K:83-84` |
| Candidate facts live only in the 3 authorities | `D:21-28` |

---

## 5. Render mechanics — the parts the edits touch

```
render_job → _build_document (render.py:889) → write_filled_docx (docxfill.py:316)
  write_filled_docx calls `edit`: resolve_control → fill_inline / fill_block;
  then unwraps controls → repairs empty cells → assert_no_controls → writes ZIP.
```

- `template_map.json` is **the one canonical** package→template map. The renderer and contract checks consume it alongside the masters. Control count mismatch vs the masters = **preflight failure**, by design.
- Masters are **zip archives**. Every master edit follows: `read_document` → mutate ElementTree →
  `ET.tostring` → `_merge_root_tag` (restores the master's own root/namespace declarations) → rezip
  with every other part byte-identical. The payloads already do this; copy them exactly.
- **`_set_paragraph_text` (docxfill:176) replaces a paragraph's content with ONE run cloned from the
  first run** — inheriting that run's `rPr`. This is *why* the whole KJERNEOMRÅDER line renders bold,
  and *why* the fix is a master edit (remove `<w:b/>`) rather than a renderer change. Do not attempt
  a renderer fix; it was explicitly rejected.
- PDF conversion failure leaves `page_count: None` and no page-target warning. Successful conversion
  can still yield **DEGRADED** after verification, with a count/warning (`render.py:689–726`).
  `pdf_required = false` permits degraded PDF delivery; empty warnings never prove page fit.

---

## 6. ID systems in the spec documents

| Prefix | Meaning |
|---|---|
| `E01`–`E27`, `E04a`, `E12a` | **the atomic edits you execute** |
| `M01`–`M06` | proposals grouping the edits |
| `C01`–`C16` | reconciled weakness catalogue |
| `V01`–`V41` | verification rulings on the two source plans |
| `F01`–`F32` | conflict-register rulings |
| `R01`–`R11` | adversarial-review findings adjudicated in Step 5 |
| `W`/`P`/`O` | numbering local to the two superseded source plans — **not** your targets |

**Guidance payloads win** over master-plan payloads or provenance rows. Current execution scope
ends before the guide's child-run instructions; the human owns that subsequent operation.

---

## 7. Execution shape

**Clusters:** A (E01–E07 + E04a) → *B conditional* → C (E12–E17 + E12a) → D (E18–E27).

**Cluster B (E08–E10) is owner-gated.** Skip unless the operator states Vegard accepted the
`PERSUASION_CALIBRATION` correction. E11 needs separate acceptance and is skipped by default.
"All items" never includes B.

**Per step:** capture reversal bytes → apply payload exactly → move on. **Checks run batched at the
cluster boundary**, not per step.

**`AVINOR_ROLLBACK`** must be set before the first edit and persist across every shell call: E27
derives its changed-path list by diffing current bytes against the per-step copies there.

---

## 8. Traps

1. **Norwegian UTF-8** (`æ ø å Æ Ø Å`) is in most payloads. Never normalise, transliterate or reflow.
   Write UTF-8 explicitly; PowerShell encoding defaults vary by version.
2. **Anchor uniqueness.** The rehearsal is historical. Require each replacement anchor exactly once
   at execution time; otherwise **stop and report**, never adapt. This overrides the guide's stale-source
   instruction to reconcile. E23's assertions detect no-ops, not duplicate anchors.
3. **Master edits are paired with consumer edits.** Changing a master without `template_map.json`
   (E22), `prepare_masters.py` (E23) and the T18 assertion (E24) breaks preflight.
4. **`evidence/` is provenance, not a test result.** E25/E26/E27 *add* current measurements and must
   not overwrite or re-stamp historical GATE-02 entries.
5. Historical rehearsals covered B skipped/included and disposable fills, not Word/PDF or full pytest.
   They do not establish current preconditions; stop on a failed anchor, precondition or cluster check.

---

## 9. Boundary

**Done:** every mandatory step applied with its anchor matched once; every cluster's batched checks
passed at their real scope; reversal copies intact; Cluster D's disposable fill command passed for CV
and for letter with both null and populated reference.

**Not yours:** freeze, branch, child run, finalize, production render, Word/PDF, extra tests/fixtures,
schema fields, extra validators, payload improvements, edits to `authorities/`, `schemas/`, `runs/`
or `generated/`, or output-quality claims. The specified temporary fills, E12a and E24 are in scope.
