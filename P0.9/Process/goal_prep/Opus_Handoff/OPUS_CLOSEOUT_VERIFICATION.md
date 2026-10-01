# P0.9 — Closeout verification after the second Codex run

**Date:** 2026-08-25 · **Method:** every previously-identified defect re-probed through the public CLI on disposable copies; full suite run in an ordinary interactive Windows session. Canonical `Build/`, the four `Architecture/` files and root `AGENTS.md` verified byte-unchanged after.

---

## 0. Verdict

**Every issue I raised is fixed — and the run introduced one new blocker.**

17 of 17 tracked defects verified resolved, several implemented exactly as recommended. But the new Word-process-ownership code makes **100 % of PDF conversions fail** on the target machine. Codex could not see this because its sandbox skips all Word tests; in a real session the suite is **242 passed / 3 failed / 1 skipped**, not the 236/10 its reports record.

Fix is roughly three lines. Everything else is done.

---

## 1. Previously-identified issues — all resolved

| ID | Issue | Verification | Status |
|---|---|---|---|
| **N1** | Word-style file lock → mixed generations + raw traceback | Held `open(letter,'rb')`, rendered **with and without** `--force`: no traceback, rc=1, CV/letter/receipt all byte-identical | **RESOLVED** |
| **N2 / N4** | `cmd_render` caught `JobError` only; rollback unreachable | `except Exception` at the per-job boundary; receipt read moved inside; `_snapshot_render_state` runs before first mutation | **RESOLVED** |
| **N3** | Repeated `--dest` export always failed | 3 consecutive exports to one directory: rc=0, 0, 0; canonical status untouched | **RESOLVED** |
| **N5** | Phase-4 should reuse `FrozenRunAssets.base_dir` | Adopted verbatim — `manifest.py:432`, `branch.py:349`; no new kwarg, no second verifier | **RESOLVED** |
| **N6** | Rollback dir under `out/` / user `--dest` | `TransactionDir(tempfile.gettempdir(), prefix="jb-rb-…")`; restore via `atomic_write_bytes`, so cross-volume safe | **RESOLVED** |
| **N7 / CF-08** | Misleading manual-PDF action | Exact new wording in `pdf.py` | **RESOLVED** |
| **CF-01** | Mid-promotion failure destroys prior valid set | Prior set byte-identical after every injected and natural failure | **RESOLVED** |
| **CF-02** | Shared failure flattened to job-local | ENOSPC → `ConfigurationError` rc=**2**, "Shared render resource failure"; `ValueError` → rc=**1** job-local; prior set intact in both | **RESOLVED** |
| **CF-03** | Interrupted Stage 3 said "Finalize and render" | `next`/`status` → *"Complete Stage 3 review-only; run context for Stage 3."*; `finalize` rc=1; `context` → `REVIEW_ONLY` / writes `['review']` | **RESOLVED** |
| **CF-04** | Stale runbook | `RUNBOOK.md` now documents the handoff protocol and Stage-3 modes | **RESOLVED** |
| **CF-05** | Bare `jobbsok` command | `cli.py:1013` emits `.\.venv\Scripts\jobbsok.exe stage-submit …` | **RESOLVED** |
| **CF-06** | Failed no-change rerender erased a valid receipt | Receipt preserved unchanged across both injected failures | **RESOLVED** |
| **CF-07** | Stage-3 second-write window | Injected ENOSPC on write #2 → `JobError` "prior final and review were restored"; both files byte-identical | **RESOLVED** |
| **CF-09** | `format` declared, never enforced | `FORMAT_CHECKER` wired at `schemas.py:118`; `date` and custom RFC3339 `date-time` both enforce, incl. calendar validation (`2026-13-01T…` rejected, `+02:00` accepted) | **RESOLVED** |
| **CF-10** | freeze/branch hash→copy TOCTOU | Staged verification before rename in both paths | **RESOLVED** |
| **CF-11 / R3** | `framework.zip` in the source tree | Removed; no archive in `Build/` | **RESOLVED** |
| **Addendum #4** | Lock vs no-clobber diagnostic split | *"The destination document is open or locked. Close the open document and retry; `--force` cannot override an operating-system lock."* — never the no-clobber text | **RESOLVED** |

### Regression checks — all clean

- **Branch:** fresh freeze → 3 stages via handoff → `VALID/FINAL` → branch unchanged → `REUSED ×4` → child `VALID / FINAL / semantic_final_available=True / CHECK / stale_scope []`.
- **Evidence registry:** 48/48 hashes recompute, 0 mismatched, 0 missing.
- **Architecture:** four frozen files and root `AGENTS.md` byte-unchanged.
- **AR-20:** the operator's live Word session survived every probe untouched.

---

## 2. NEW BLOCKER — Word COM PDF export is completely broken

### Symptom

Every conversion fails, deterministically:

```
attempt 1: ok=False exit=1  'export.ps1 : Cannot convert null to type "System.IntPtr".'
attempt 2: ok=False exit=1  (same)
attempt 3: ok=False exit=1  (same)
```

Full suite in an ordinary interactive session: **242 passed, 3 failed, 1 skipped** (was 246 / 0 before this run).

Failing: `test_t19_norwegian_glyphs_survive_to_the_pdf`, `test_t19_public_word_render_handles_realistic_long_norwegian_names`, `test_t21_failed_pdf_rerender_retires_prior_pipeline_pdfs`. Skipped: `test_t20_pdf_container_metadata_variation_is_documented` ("no PDF was produced").

### Root cause — `pdf.py:68-79`

```powershell
[void][JobbsokWindowProcess]::GetWindowThreadProcessId(
    [IntPtr]$word.Hwnd, [ref]$wordPid
)
```

Verified directly against this machine's Word:

```
Hwnd_raw_is_null                 = True
Hwnd_after_Visible_false_is_null = True
```

`Word.Application.Hwnd` is `$null` on Microsoft 365 Word 16. With `$ErrorActionPreference = 'Stop'`, `[IntPtr]$null` is a terminating error, caught by the script's own `catch`, → `exit 1` → the export never runs.

The ownership feature was added to satisfy AR-20 / D-07 ("kill only an ownership-proven automation PID"). It is built on a property that does not exist here, and it takes the whole PDF path down with it.

### Why Codex could not see it

Its sandbox has no usable Windows logon session, so all ten Word tests **skip**. Its reports honestly record `236 passed, 10 skipped`. The regression lives entirely inside the ten tests its environment cannot run — the exact blind spot flagged in the previous verification, this time producing a false negative instead of a false positive.

### Consequential evidence defects

1. `DOD_AUDIT.md`: *"There is no known remaining mechanically resolvable P0/P1 defect"* — false on the target machine.
2. `FINAL_STATUS.md` / `BUILDER_REPORT.md`: `236 passed, 10 skipped, 79.83 s` describes the sandbox, not the machine.
3. GATE-03/05/06 and DOD-16/17/18/23/25 remain correctly `BLOCKED_USER` — the gating is honest; only the "nothing left" claim and the counts are wrong.

### Severity

**High, release-blocking.** `DEC-41` means no employer document is corrupted and no semantic state is damaged — degradation is handled correctly throughout. But PDF is a normal target deliverable (Spec §16.1), the operator would hand-export every PDF for every job, and the target-Word evidence the remaining gates depend on cannot be produced while this stands.

### Smallest fix

Guard the handle read; the script **already** computes `$wordPidsBefore`, so the fallback exists:

```powershell
$hwnd = $null
try { $hwnd = $word.Hwnd } catch { }
if ($null -ne $hwnd -and $hwnd -ne 0) {
    [void][JobbsokWindowProcess]::GetWindowThreadProcessId([IntPtr]$hwnd, [ref]$wordPid)
}
# else: leave $wordPid = 0 -> $owned = False -> no automatic kill
```

`$owned` already requires `$wordPid -gt 0`, so an unresolved handle degrades to *"ownership not established, kill nothing"* — which is exactly the accepted AR-20 / D-07 posture. Optionally derive the PID from a post-creation `Get-Process WINWORD` diff, but only as a diagnostic hint, never as kill authority.

**Required proof:** `pytest -q` in an interactive session must return **246 passed, 0 skipped**; and one conversion must produce a verified PDF with the operator's Word session open and untouched.

---

## 3. Recommendation

Send back one bounded fix: guard the `Hwnd` read, re-run the suite in an interactive session, and correct the three evidence statements to the real-machine counts. No other work remains on my list.

After that, the outstanding items are the ones that were always genuinely human: `DOD-18` visual QA, `DOD-19` GATE-10 account facts, `DOD-16B` human-session timeout (cheap — a Word session is already open), and a fresh independent review.
