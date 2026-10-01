# Jobbsøk_26 P0.9 — Build

Deterministic runtime for the P0.9 architecture: a human-approved opportunity
set becomes validated, reviewable Bokmål CV-plus-letter packages, with
immutable truth, job-local failure containment, manual semantic execution and
manual submission.

Governed by the frozen pair in `../Architecture/`:
`P0.9_FINAL_NORMATIVE_SPECIFICATION.md` and
`P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md`, as amended by the
explicit P0.9.3 amendment appended to both. Where this build and the
specification disagree, the specification wins.

The active semantic route is **Stage 1 → Stage 3; separate instance/chat for
each.** Stage 2 is retired for runs created at revision 0.9.3; historical
0.9.0 runs keep their own frozen three-stage route, schemas and bindings.

**Start here:** [`policy/RUNBOOK.md`](policy/RUNBOOK.md) for day-to-day use,
[`BUILDER_REPORT.md`](BUILDER_REPORT.md) for what is built, tested and still
owed.

## Setup

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -e ".[dev]"
.venv/Scripts/jobbsok preflight
```

## Layout

```text
authorities/   three factual authority files + CV baseline   (protected)
context/       rich personality profile                      (protected)
policy/        settings, writing rules, stage instructions    (control plane)
templates/     CV and letter masters + one canonical map      (control plane)
schemas/       nine canonical artifact schemas                (control plane)
runtime/       deterministic code and tests
generated/     regenerable index, baseline map, status views  (disposable)
inbox/         pre-freeze operator input
runs/<run_id>/ immutable manifest, current artifacts, renders, audit
pilot/         human-owned evaluation log                     (never read by code)
evidence/      gate reports and the vertical-slice package
```

Only the current run/job output area is model-writable. Authorities, context,
policy, templates and schemas are protected inputs, changed by the human
between runs and never by a stage.

## Commands

| Command | Purpose |
|---|---|
| `preflight` | environment, masters, template map, baseline agreement |
| `index build\|verify` | evidence index and mechanical baseline map |
| `init-input` | write an empty operator batch input |
| `freeze` | validate operator input and create one immutable run |
| `branch` | child run; the parent is never touched |
| `context` | prepare one stage's input bundle |
| `stage-submit` | write one stage-owned artifact, validated first |
| `validate` | mechanical validation with dense diagnostics |
| `finalize` | assign the canonical employer-facing document date |
| `render` | DOCX and PDF, independently verified |
| `status` | three status axes and the operator queue |
| `next` | the next job to work on, derived from disk |
| `verify-integrity` | check every manifest-frozen hash |

Exit codes: `0` success, `1` job-level failure or partial success, `2`
configuration or run-integrity problem.

## Design points worth knowing

- **Two dependencies.** `jsonschema` and `pymupdf`. OOXML work uses the
  standard library; `lxml` and `python-docx` are deliberately absent.
- **No network capability.** Asserted at AST level by the test suite. The
  package has no HTTP or model client and no submission surface.
- **A run is self-contained.** Freeze copies every hashed input into
  `runs/<run_id>/frozen/`, and commands verify those copies. Editing the
  repository between runs cannot corrupt a run already in flight.
- **Two reference namespaces.** `EV:` resolves only to the three candidate
  authorities through the evidence index; `BL:` addresses the mechanical CV
  baseline. Neither can pass as the other, and reference resolution never
  claims semantic support.
- **Three status axes, never collapsed.** A `READY` package with a degraded
  PDF is a normal state.
- **Counts are editorial.** Competency, bullet, paragraph and page counts
  emit warnings, never failures.

## Verifying

```bash
.venv/Scripts/python -m pytest runtime/tests -q
```

The current finalization baseline is 236 passing tests plus 10 explicitly
skipped target-Word tests when Word COM cannot be activated. The traceability
registry fails if a Tier-1 item or mechanically testable acceptance criterion
loses its named test; it does not upgrade helper coverage into public-command
or target-machine proof.

```bash
cd runtime && ../.venv/Scripts/python -m tools.vertical_slice
```

Runs the full Contract §19 chain on a synthetic job against the real
authorities, baseline and masters, and writes an evidence package to
`evidence/vertical_slice/`.

## Asset preparation

`runtime/tools/prepare_masters.py` reproducibly applies the required master
repairs: canonical OPC core properties, ECMA-376 child ordering, font retarget,
and removal of the single unconditional CV page-break paragraph. It refuses to
write if the content-control contract changes or the page-break target is
ambiguous. The pristine originals are archived under
`evidence/gates/GATE-02/original_p07_masters/`. See
[`evidence/gates/GATE-02/GATE-02.md`](evidence/gates/GATE-02/GATE-02.md).
