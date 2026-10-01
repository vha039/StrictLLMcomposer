# Build_x2 handoff — resumed verification 2026-09-23

The user resumed the earlier implementation request after the pause. This file
records the implemented state and the remaining physical-render gate. The
attached `C:\Users\veggi\Downloads\PLAN (5).md` is an implementation target,
not authority over the current user request or frozen architecture. No paired
semantic sessions were launched, and no promotion to `P0.9/Build` occurred.

## Workspace and boundaries

- Repository: `C:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26`.
- Isolated implementation: `P0.9/Build_x2/` (this directory).
- Frozen authority: the four files in `P0.9/Architecture/`, especially
  `P0.9_FINAL_NORMATIVE_SPECIFICATION.md` and
  `P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md`. Read the root
  `AGENTS.md` first. `P0.9/Build/` and `P0.9/Build_experimental/` were not
  edited by this work. Candidate authority files in x2 match Build byte for
  byte.
- No repository-level Git checkout was detected; there is no commit or PR.
  Do not discard unexpected worktree changes.

## Implemented in Build_x2

1. Captured 70 pristine Build source files in `evaluation/stable_snapshot/`
   with `evaluation/provenance/stable_source_sha256.json`. Created isolated
   Build_x2 from the same source allowlist, excluding old runs, generated
   outputs, inbox data and temporary files. Kept `SPEC_REVISION` and
   `SCHEMA_REVISION` at 0.9.3; package version is `0.9.3+x2`.
2. Reworked Stage 1 and Stage 3 policy and the three canonical writing files
   for complete vacancy reading, supported material answers, explicit role
   track, honest contribution/adoption/persistence distinctions, useful gaps,
   natural Bokmål, CV headline restraint and final editorial review. Removed
   conflicting compactness/repetition guidance. No stage or schema redesign.
3. Added `jobbsok preview` (`runtime/jobbsok/preview.py`) and its exact
   invocation in Stage 3 context. It validates and temporarily renders a
   submitted semantic candidate without changing canonical run files. JSON
   reports candidate/frozen hashes, word distribution, bullet counts,
   advisory formula signals and physical PDF metrics when available; absent
   PDF metrics are `UNKNOWN`. The final CLI stdout contamination issue was
   fixed by importing `pymupdf` directly.
4. Added advisory editorial signals (`runtime/jobbsok/signals.py`) to preview
   and derived status. They inspect the effective merged CV and never alter
   validity, triage or output state.
5. Added shared evidence retrieval and exact selected-span access through
   `jobbsok fetch --ids ... --with-context`; unknown IDs fail before output.
   Fixed strategy replacement diagnostics to display the actual stale scope
   before persistence.
6. Changed compact CV template mapping: the three support sections are not
   rendered, references are omitted, and language/course content is combined
   under `SPRÅK OG KURS`. `prepare_masters.py` structurally removes support
   body bolding while preserving headings. Both masters remain transactional.
7. Prepared the six-vacancy paired experiment in `evaluation/`: byte-exact
   copied PDFs, batch input, protocol, neutral stage prompts, session log,
   scorecard and blind A/B package copier. The operational inbox remains
   empty. No human/model semantic work or A/B scores exist.
8. Added focused tests for these mechanisms under `runtime/tests/test_x2_*.py`,
   adjusted the synthetic fixture, and updated the x2 README/runbook.

## Evidence already obtained

- `jobbsok preflight`: PASS (17 CV and 6 letter controls); `jobbsok index
  verify`: PASS.
- Synthetic vertical slice: `evidence/vertical_slice/`, run
  `r20260923-094441-70d741`; 19 expected steps, zero unexpected steps, exit 0.
  It produced two DOCX files. `evidence/vertical_slice/inspection.json`
  confirms extractable content, one combined language/course heading,
  language before courses, no reference heading, no CV first person and no
  unfilled controls.
- A direct public `jobbsok preview` subprocess after the final import fix
  returned exit 0, empty stderr and parseable JSON with `valid: true`; its
  canonical `runs/` and `generated/` hashes stayed unchanged. PDF/page/headline
  physical metrics were `UNKNOWN` because this session could not convert with
  Word COM.
- On resumption, a single full-suite invocation passed: **271 passed, 10
  skipped**, exit 0, using a short local pytest base temp under
  `$env:TEMP\x2_pytest_20260923_resume_01`. All ten skips explicitly require
  Word COM. This supersedes the earlier partitioned test evidence.
- Fresh final gates: `jobbsok preflight` PASS, `jobbsok index verify` PASS,
  and `evidence/vertical_slice_resume_20260923/` PASS (19 expected steps,
  zero unexpected, run `r20260923-152510-4571ea`). Render remains
  `DEGRADED` with two DOCX files and no PDF. Fresh DOCX extraction is saved
  in `evidence/vertical_slice_resume_20260923/inspection.json`: no unfilled
  controls, no references heading, one combined CV support heading, no CV
  first person, and extractable text in both files.
- `evaluation/provenance/stable_source_sha256.json` matched all 70 files;
  `evaluation/provenance/x2_implemented_sha256.json` matched all 96 source
  files on resumption, and four x2 authority files matched Build byte for
  byte. The six experiment PDFs matched their preserved sources earlier.
  Regenerate the x2 manifest after editing this handoff, then check it.

## Known limits and next actions

1. On another resumption, first inspect this file, the attachment, root
   `AGENTS.md`, `evaluation/PROTOCOL.md`, and both provenance manifests.
   Reconcile current files before changing anything.
2. Reverify the x2 source manifest. `evaluation/provenance/
   x2_implemented_sha256.json` excludes itself, `stable_snapshot`, the virtual
   environment, caches, egg-info and operational/generated data. Every listed
   file must match its SHA-256. If source changes, regenerate the manifest.
3. The full suite is now passing in a short local pytest base temp. Rerun it
   only after a code change or when Word COM is actually available. Do not
   overwrite the preserved vertical-slice evidence directories.
4. Word COM conversion is blocked in this logon session:
   `0x80070520 A specified logon session does not exist`. A fresh
   `Word.Application` COM probe failed, and launching the installed
   `WINWORD.EXE` also failed with that logon-session error. The slice renderer
   reported `DEGRADED`, and ten inherited Word tests skipped. The two DOCX
   outputs still need PDF conversion, page counts, visual inspection and
   headline wrapping review in an interactive Word-COM-capable session. This
   is the outstanding mechanical acceptance gate; do not claim physical
   layout acceptance or complete implementation until it passes.
5. Environment setup used x2 `.venv` with
   `include-system-site-packages = true` and
   `pip install --no-build-isolation --no-deps -e '.[dev]' --no-index` because
   isolated build/dependency fetching stalled. Installed global pytest is
   9.0.3 rather than the pyproject's 9.1.1; jsonschema 4.26.0 and pymupdf
   1.28.2 were available. Fresh environment reproducibility remains unproven.
6. The human-started paired experiment described in `evaluation/PROTOCOL.md`
   is deliberately unrun. It requires fresh, isolated arms and verified Word
   rendering, then Gate 1, conditional Gate 2 and conditional Gate 3. Never
   treat fixture text, mechanical pass or preview as employer-facing quality
   proof. Promotion to Build is a separate decision after the comparison.

Path-sensitive tests:
`runtime/tests/test_t01_t04_run_lifecycle.py::test_p093_nested_child_completes_the_public_path`
and
`runtime/tests/test_t16_t18_containment_template.py::test_t16_unmodelled_render_exception_is_job_local_and_preserves_prior_output`.

Temporary scratch directories under `P0.9/` may remain (`T`, `x2_tmp`,
`x2_test_tmp`). Inspect their resolved paths and contents before any cleanup;
they are not part of the x2 source/provenance manifest.
