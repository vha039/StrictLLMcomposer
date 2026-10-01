# `GATE-02` — Actual P0.7 masters and OOXML technique

> Historical gate evidence. It predates the final reproducible CV page-break
> rewrite. Current-tree target claims are governed by
> `evidence/gates/GATE_REPORTS.md`; the observations below are retained only
> for diagnosis and pristine-master provenance.

**Status:** PASS, after a required master repair.
**Date:** 2026-08-23
**Machine:** Windows 11 Home 10.0.26200, Microsoft 365 Apps 16.0.20228.20190,
Python 3.14.3.

## Empirical question

Do the supplied masters match the audited non-data-bound control structure,
and does fill→unwrap→assert-no-SDT work on the actual files?

## Method

1. Inventory content controls, tags, data bindings, tables, text boxes,
   duplicates and missing tags directly from `word/document.xml`.
2. Fill representative content through the rebuilt primitive, unwrap the
   controls, assert no `w:sdt` and no `{{placeholder}}` survives.
3. Open every artifact in the installed Word **without** `OpenAndRepair`,
   and export PDF.

## Observed result

### Control structure — matches, cleanly

| Master | Unique tags | Total controls | `w:dataBinding` | `docPartObj` |
|---|---:|---:|---:|---:|
| `CV_MASTER.docx` | 17 | 17 | 0 | 0 |
| `APPLICATION_MASTER.docx` | 6 | 7 (`APP_JOB_TITLE` ×2) | 0 | 0 |

No data-bound or `docPartObj` controls exist. The three `customXml/` parts
hold only an empty Word bibliography (`b:Sources`), not a binding store.
The inventory matches `templates/template_map.json` exactly, and
`require_template_contract` passes for both documents.

### The technique works

`fill → unwrap → assert-no-SDT` produced both documents with **0 residual
`w:sdt`**, **0 residual `{{ }}` placeholders**, and all zip parts preserved
(20 CV, 19 letter). Norwegian glyphs survive the round trip.

### But the supplied masters were not Word-openable

Word rejected **both** original masters, and every document derived from
them, with *"The file appears to be corrupted."* A Word-authored control
document opened normally, so Word COM itself was not the problem. Bisecting
by package part isolated two independent defects:

1. **`docProps/core.xml` — unbound `dcterms` prefix (fatal).**
   The part binds the Dublin Core terms namespace to prefix `ns2` but still
   writes `xsi:type="dcterms:W3CDTF"` inside the attribute value, leaving
   `dcterms` unbound in a QName-typed attribute. This makes the OPC
   core-properties part invalid and Word refuses the whole package. It is a
   classic lxml/python-docx round-trip artifact.
   *Swapping only this part for a valid one made the document open.*

2. **`w:pPr` child order — `spacing` before `pBdr` (schema violation).**
   One paragraph-properties block in each master orders its children
   `spacing`, `pBdr`. ECMA-376 `CT_PPr` requires `pBdr` first.

LibreOffice tolerates both. P0.7's `TEST_REPORT.md` records rendering
verified through **LibreOffice** only, which is why neither defect was ever
observed: the masters had, as far as the evidence shows, never been opened
by Word.

## Safe posture

"Reuse only after inspection; unknown/duplicate/missing required controls
fail preflight." Held. Inspection is what surfaced the defects, and the
preflight contract check is implemented and passing.

## Implemented consequence

`runtime/tools/prepare_masters.py` applies a reproducible, auditable
repair rather than a hand-edit:

- rewrites `docProps/core.xml` from scratch with canonical, fully bound OPC
  prefixes (`cp`, `dc`, `dcterms`, `dcmitype`, `xsi`), preserving values;
- reorders `w:pPr` / `w:rPr` children into ECMA-376 schema sequence across
  every document part;
- retargets absent fonts (see `GATE-05`);
- **refuses to write if the control contract changes.**

The pristine P0.7 originals are archived unmodified under
`evidence/gates/GATE-02/original_p07_masters/`. `runtime/jobbsok/docxfill.py`
builds `core.xml` canonically for every rendered document, so the defect
cannot be reintroduced downstream.

### Verification after repair

| Artifact | Word open (no repair) | Pages | PDF export |
|---|---|---:|---|
| `CV_MASTER.docx` (prepared) | OPENED | 1 | — |
| `APPLICATION_MASTER.docx` (prepared) | OPENED | 1 | — |
| `CV_filled.docx` | OPENED | 1 | 281 042 B |
| `Soknad_filled.docx` | OPENED | 1 | 189 424 B |

Control contract preserved: 17 and 7 controls, unchanged.

## Is any frozen rule impossible?

**No.** The gate's own fail consequence ("build minimal replacement masters
satisfying the same document contract") was not needed: a targeted repair of
the actual masters satisfies the same document contract while preserving the
tested layout, styles, headers and control map. Spec §22.2 and `GATE-02`
both list master files and the fill library as changeable without a
specification amendment. `DEC-30` is satisfied — the P0.7 assets were
treated as implementation capital, inspected, and adapted by fit.

## Artifacts

- `inventory.json` — before/after hashes, control counts, binding report
- `original_p07_masters/` — pristine P0.7 masters
- `artifacts/CV_filled.docx`, `artifacts/Soknad_filled.docx`
- `artifacts/CV_filled.pdf`, `artifacts/Soknad_filled.pdf`

## Note carried to the render verifier

The CV master renders the candidate name through `w:caps`, so extracted
text reads `VEGARD HÅLAND`. Document identity verification must casefold
before comparing, or it will report a false failure.

## Avinor optimisation source revision

The source-maintenance revision uses 17 CV controls and 6 letter controls,
one per tag. The optional reference is below the letter's address/date
table; the subject contains the only APP_JOB_TITLE. The CV keeps its
existing competence transform with regular text, releases the earlier-role
keepNext chain, and places earlier experience and languages before the
support sections.

The avinor_optimization entries in inventory.json record the revised source
bytes and control structure. The original_p07 and prepared entries above
remain historical observations. This addition is not a new Word-open,
pagination or PDF gate result. Those properties must be observed on the
next normally finalized and rendered package; an absent PDF page count
does not establish that a page target was met.
