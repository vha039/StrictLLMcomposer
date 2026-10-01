# Final mechanical status — 2026-08-25

## Decision

`BLOCKED_USER`

All accepted mechanical corrections pass the full suite, retained vertical
slice and disposable public-command fault probes. `GO_FOR_TWO_JOB_SMOKE` is
withheld only for:

1. current-tree target Word/PDF/long-path/font/glyph and forced-timeout proof
   in a usable interactive logon session;
2. sparse/normal/dense human visual acceptance;
3. actual role surfaces and file-access/privacy/retention/training facts;
4. a fresh independent review of the repaired bytes.

The open human Word process survived every attempted probe, but the shell could
not create an automation Word process, so forced-timeout cleanup and open-file
byte survival remain unproved. No real vacancy or model chat was consumed.

## Current mechanical evidence

- suite (finalization session, no Word COM): 236 passed; 10 target-Word
  tests skipped; 79.83 s;
- suite (interactive target session, 2026-08-25): **246 passed; 0 skipped;
  228.76 s** — every previously skipped Word test executed and passed;
- vertical slice: 21 expected outcomes; 0 unexpected; two DOCX;
- render fault probes: exact rollback for held document, local exceptions,
  shared ENOSPC and receipt-write failure; peer containment verified;
- repeated explicit export: two successes; canonical hashes unchanged;
- Stage 3: emitted commands and review-only recovery complete; injected
  second-write failure restores the prior pair/history;
- freeze/branch: staged copy mutation exposes nothing; parent unchanged;
- formats: retained typed corpus passes and invalid lexical dates are refused;
- source hygiene: `framework.zip` absent; no committed probe harness.

See `BUILDER_REPORT.md`, `evidence/gates/GATE_REPORTS.md`, and the three
finalization audits. `evidence/finalization/HASHES.sha256` is generated last.

---

## Addendum — interactive target session, 2026-08-25

The finalization session could not activate Word COM, so the ten `@requires_word`
tests skipped there. Executed in an ordinary interactive Windows session they
initially exposed a regression introduced by the automation-ownership change:
`Application.Hwnd` is `$null` on this Microsoft 365 Word build, so
`[IntPtr]$word.Hwnd` was a terminating cast error under `$ErrorActionPreference =
'Stop'` and **every** PDF conversion failed (suite: 242 passed, 3 failed, 1
skipped).

Repaired in `runtime/jobbsok/pdf.py`: the automation window handle is now resolved
from `$doc.ActiveWindow.Hwnd` after `Documents.Open` — before the export a timeout
would interrupt — with a guarded fallback to `$word.Hwnd` and then to no handle at
all. An unresolved handle leaves the PID at 0 and `OWNED` false, so nothing is ever
terminated (`AR-20`). `AutomationSecurity` is still applied before any document is
opened.

Verified in that session:

- full suite **246 passed, 0 skipped**;
- `Word.Application` activates; `VERSION=16.0`;
- direct conversion succeeds repeatedly and produces a 292 943-byte PDF;
- public `render` returns `CV: OK/OK  letter: OK/OK`; status render axis `OK` with
  four surfaced outputs and a receipt that verifies;
- automation ownership now resolves — `AUTOMATION_PID=<pid>;OWNED=True` — and the
  operator's unrelated live Word session was untouched by every probe;
- forced timeout during the open phase leaves ownership unproven, kills nothing and
  reports that truthfully.

`DOD-18` (human visual QA), `DOD-19` (GATE-10 account facts) and `DOD-25`
(independent review) remain open; they are not mechanically closable.

---

## Addendum 2 — flagged-issue closeout, 2026-08-25

Six externally flagged issues were re-validated against the tree; five warranted
code changes and all were repaired and reproduced through public paths.

- **Stale export PDFs (P1).** Reproduced: a repeated `--dest` export with the
  converter unavailable replaced both DOCX files while both previous-generation
  PDFs survived, leaving mixed generations where the operator submits from.
  `render.py` now sets an unmatched sibling aside as `<stem>.superseded.pdf` —
  renamed, never deleted, since it may be a manual export — and names it in the
  operator action. No current-looking stale PDF remains.
- **Shared vs job-local failure at the render boundary (P2).** An invalid frozen
  schema was reported as `malformed job-local semantic state` with rc=1. Only this
  job's own current artifacts are now pre-read as job-local; a shared
  `ConfigurationError` propagates and aborts globally with rc=2. Malformed job JSON
  still stays job-local at rc=1 and `status` remains contained.
- **Lock during rollback-snapshot creation (P2).** If the lock strikes before the
  snapshot exists, the planned target set is now used as the fallback, so the
  operator still receives the close-and-retry diagnostic rather than a raw
  `PermissionError`. Verified: rc=1, outputs unchanged.
- **Stage-3 history residue (P2).** Injected `ENOSPC` on the second history copy
  previously left an orphan archive. The archive loop now removes what it created
  before propagating. Verified: no residue, current artifacts unchanged.
- **Over-broad lock advice (P3).** `verify_receipt` classified every `OSError` as an
  open document. It now uses an errno/winerror predicate (`EACCES`/`EPERM`,
  WinError 5/32); `EIO`, `ENOENT` and other failures get the generic message.

Note on real Word: Microsoft Word denies read access to an open `.docx`, a stronger
lock than a plain read handle. The render rollback was re-verified under real Word —
prior CV, letter and receipt all byte-identical, correct diagnostic, no stray files.

`DOD-16B` is now genuinely proved rather than inferred. With an unrelated human Word
session open, a forced timeout during export resolved ownership and terminated only
automation PID 24508 — *"pre-existing Word processes were not targeted"* — leaving the
human session and every pre-existing process untouched and no orphan behind. A
timeout during the open phase leaves ownership unproven and terminates nothing.
`AR-01/03/16/20`, `DOD-16` and the traceability rows are reconciled to that evidence.

Full suite after all changes: **246 passed, 0 skipped**, 223.28 s.
