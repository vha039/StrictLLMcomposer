# P0.9 finalization gate reports

**Regenerated:** 2026-08-28  
**Build:** specification/schema revision `0.9.0`  
**Target:** Windows 11 + Microsoft 365 Word 16

Evidence labels are literal: `STATIC_CODE`, `PUBLIC_CLI`,
`PUBLIC_CLI_FAULT_PROBE`, `ARTIFACT_HASH`, `TARGET_WINDOWS`, `VISUAL_HUMAN`
and `USER_ACCOUNT`.

## GATE-01 — Stage surface and same-session validation

**Status:** `PASS_PUBLIC_CLI`; real-model behavior remains smoke scope.

- Context emits frozen inputs, semantic-only fields, current handoff and a
  venv-qualified PowerShell command.
- The emitted commands completed Stage 1, Stage 2, normal Stage 3 and
  review-only recovery in a disposable build.
- Finalization refuses until current final and review both exist. Stale/wrong
  handoffs mutate nothing. No deterministic component starts a model.

## GATE-02 — Masters and OOXML technique

**Status:** `PASS_STATIC/PUBLIC_CLI`; target Word follows GATE-03.

`tools.prepare_masters --check` reports zero remaining changes and exact CV
17/letter 7 controls. Point-of-use frozen-master hash and control checks remain
blocking. Stdlib OOXML, untouched-part and root-tag preservation are unchanged.

## GATE-03 — Automated PDF conversion on target Windows

**Status:** `BLOCKED_USER` target execution; degradation path
`PASS_PUBLIC_CLI`.

- Word COM remains one read-only, macro-disabled instance per document.
- The script records pre-existing Word PIDs and resolves the exact COM HWND PID.
  Timeout cleanup is permitted only for a new PID still identified as
  `WINWORD.EXE`; an unproven/pre-existing process is never targeted.
- A non-Word PID guard passed. The live shell could not create COM or an
  isolated `/x` Word process because no usable logon session was available.
- Human PID 20604 and `Utviklingssamtale_strategidokument.docx` remained
  present with unchanged length/mtime, but the open file could not be hashed;
  forced-timeout and byte-survival claims remain unproved.
- Converter failure leaves both DOCX current in the retained slice and render
  `DEGRADED`; the manual-PDF message no longer promises adoption.

Required closure: run target Word long-name/PDF/font/glyph and forced-timeout
checks in an unlocked interactive execution context.

## GATE-04 — Converter granularity

**Status:** `PASS_STATIC`; target execution follows GATE-03.

Word remains one short-lived invocation per document; no daemon/shared instance.

## GATE-05 — Fonts, glyphs and layout

**Status:** `PASS_STATIC`; `BLOCKED_USER` for `VISUAL_HUMAN`.

Calibri/Norwegian-capable references and all controls remain. The forced CV
break remains absent. Sparse/normal/dense target Word/PDF visual inspection is
still required; no page/count cap or semantic truncation was added.

## GATE-06 — Parseability and identity

**Status:** `PASS_PUBLIC_CLI` for DOCX; target PDF follows GATE-03.

The fresh slice produces and independently verifies both DOCX files: exact
identity/addressing/chronology, override visibility, complete letter controls,
no residual controls/placeholders and no private-token leakage.

## GATE-07 — Dependencies, Unicode, paths and formats

**Status:** `PASS_DETERMINISTIC`; Word-specific long-path follows GATE-03.

- Production dependencies remain exactly `jsonschema==4.26.0` and
  `pymupdf==1.28.2`; OOXML remains stdlib.
- UTF-8 and Norwegian filename folding pass.
- The common validator enforces default formats plus a local RFC3339
  `date-time` checker. Twenty retained typed artifacts validate; impossible
  dates and malformed timestamps are rejected.
- Handoff digest shortening and short transaction staging remain intact.

## GATE-08 — Commit integrity and safe writes

**Status:** `PASS_PUBLIC_CLI_FAULT_PROBE`.

- One CLI boundary snapshots the exact four outputs plus receipt in
  `TransactionDir`, classifies before rollback, verifies restoration, then
  continues a local peer or aborts shared failure.
- Holding the changed-generation letter open, with and without `--force`,
  leaves the prior CV/letter/receipt byte-identical, emits close/retry with no
  foreign-edit advice, and permits the healthy peer to complete.
- Unmodelled promotion and malformed receipt are job-local. Promotion ENOSPC
  and receipt-write ENOSPC restore then exit 2 before a peer.
- Live locked `status` returns a clean unreadable/currentness failure, not a
  traceback or overwrite recommendation.
- Foreign DOCX no-clobber and protected/traversal/reparse refusals remain.
- Explicit export twice returns 0 both times and leaves canonical
  output/receipt/history hashes unchanged.

## GATE-09 — Deterministic vertical slice

**Status:** `PASS_PUBLIC_CLI`.

Retained run `r20260824-220210-918545`: 21 expected outcomes, 0 unexpected;
healthy job `CHECK`/`VALID`/`DEGRADED`; poisoned peer `FAILED`/`NOT_RENDERED`;
exact manifest, fixtures, semantic returns, diagnostics, output hashes and two
DOCX are retained. This proves mechanics, not semantic quality or target PDF.


## GATE-10 — Role mapping, file access and privacy

**Status:** `PASS_USER_VERIFIED`.

Actual role mapping:
- `SOL_CLASS`: "Codex / GPT-5.6 Sol"
- `TERRA_CLASS`: "Codex / GPT-5.6 Terra"

File access:
- Local Codex session operating directly on the Jobbsøk_26 repository.
- Confirmed read/write access to the project workspace and ability to execute
  the repository CLI.
- Stage context is derived from current/frozen repository files; no
  cross-session conversational memory is relied upon.

Retention:
- Signed-in Codex chats remain in account history until deleted.
- User-deleted chats are scheduled for permanent deletion within 30 days,
  subject to documented safety/security/legal exceptions.

Training/data use:
- ChatGPT Business/Codex business inputs and outputs are not used to train or
  improve OpenAI models by default.
- No explicit training opt-in is used for this workflow.

Context/privacy:
- Each semantic stage is run in a fresh agent session.
- Only repository context required by that stage is supplied.
- The deterministic Jobbsøk runtime itself performs no model calls, network
  actions, employer contact or submission.

Verified by human operator: 2026-08-28

---

## GATE-11 — Bounded recovery

**Status:** `PASS_PUBLIC_CLI/STATIC_CODE`.

Mechanical correction and manually initiated semantic retry remain distinct.
Exhaustion reaches `BLOCKED_MANUAL`; no scheduler, fourth stage or retry engine.

## Summary

| Gate | Status |
|---|---|
| GATE-01 | PASS public operator loop |
| GATE-02 | PASS static/public; target Word owed |
| GATE-03 | PASS target Word (2026-08-25 interactive session); degradation PASS |
| GATE-04 | PASS static |
| GATE-05 | PASS static; **BLOCKED_USER** visual |
| GATE-06 | PASS DOCX and target PDF (2026-08-25 interactive session) |
| GATE-07 | PASS deterministic; target Word long-path owed |
| GATE-08 | PASS public fault probes |
| GATE-09 | PASS fresh retained slice |
| GATE-10 | PASS user-verified account/surface facts (2026-08-28) |
| GATE-11 | PASS public/static |

Overall pre-pilot closure: `GO_FOR_TWO_JOB_PILOT`. The remaining real-job
visual/semantic quality evidence belongs to the two-job pilot; no run was frozen
by this closure check.

---

## Addendum — target-session evidence, 2026-08-25

The finalization session could not activate Word COM. In an ordinary interactive
Windows session on the same machine the full suite runs **246 passed, 0 skipped**,
after repairing a Word-automation regression described in
`evidence/finalization/FINAL_STATUS.md`.

- `GATE-03`: `Word.Application` activates (`VERSION=16.0`); conversion produces a
  verified PDF; forced timeout reports truthfully and terminates nothing whose
  ownership is unproven.
- `GATE-05`: font/glyph target behaviour passes
  (`test_t19_norwegian_glyphs_survive_to_the_pdf`); sparse/normal/dense **visual
  human** judgement remains `BLOCKED_USER`.
- `GATE-06`: DOCX and PDF extraction both verified on target.
- `GATE-07`: realistic long Norwegian employer/title path converts successfully
  (`test_t19_public_word_render_handles_realistic_long_norwegian_names`).
- `GATE-10` was closed as `PASS_USER_VERIFIED` on 2026-08-28 from the actual
  account/surface facts recorded in the gate above.
