# P0.9 — Differential deep review: v2 report + Codex plan vs. codebase

**Date:** 2026-08-24 · **Method:** cross-reference both documents against live code; then targeted non-linear probing of interaction surfaces neither document exercised. All destructive work on disposable copies; canonical `Build/` and the four `Architecture/` files verified byte-unchanged after.

---

## 1. Adjudication of the two documents

### 1.1 v2 verification report — **materially correct**

1. CF-01…CF-05, CF-07…CF-10 — **all independently confirmed** against live code (§2).
2. §0.3 self-downgrade of Stage-3 pair atomicity HIGH→MEDIUM — **correct**; `submit_stage3_pair` prevalidates both candidates and render refuses on stale review.
3. §5.1–5.4 dismissals of my R5/R6/R7/R8 — **correct**; I concede all four.
4. §10.2 provenance call on `framework.zip` (post-run review artifact, not a Codex regression) — **correct**; I over-called it.
5. §2.1 "DOD-16 overclaimed from pasted evidence" — **correct**. I proved COM+long-path+glyph; I did **not** prove the human-session-survival subcheck.
6. Only material v2 error: Appendix B locates the interrupted-state action at `status.py` fallback only. It also propagates through `next` and is *permitted* by `cmd_finalize`; three sites, not one.

### 1.2 Codex plan — **90% correct, four structural defects**

7. Dispositions, KEEP register (AR-01…AR-20), §5 "no architecture amendment", §6 DEFER set — **all endorsed**.
8. §4 Phase 3 rollback via existing history copies — **verified implementable**; `submit_stage3_pair` already writes both history copies *before* both `atomic_write_json` calls. ~6 lines.
9. §4 Phase 4 format checker — **verified necessary**: `jsonschema` default `FormatChecker` registers `{date, email, idn-email, ipv4, ipv6, regex, time, uuid}`. **`date-time` is absent.** Passing a bare `FormatChecker()` would enforce `date` only and silently still not check `date-time`. The plan's custom RFC3339 registration is mandatory, not decorative.
10. Defects **D1–D4** below.

---

## 2. Claim-by-claim verification against live code

| Claim | Verdict | Evidence |
|---|---|---|
| CF-01 sequential promotion | **CONFIRMED** | `render.py` else-branch iterates `docx_outcomes`, `promote_file` per document; no try/except spans the loop |
| CF-02 ENOSPC flattened | **CONFIRMED** | `render.py:505-509` `except ConfigurationError: raise / except Exception as exc: docx_outcome.state="FAILED"` |
| CF-03 interrupted Stage-3 | **CONFIRMED** (reproduced) | `next` → `action: "Finalize and render."`; `finalize` rc=0 mutates date; `render` rc=1 refuses |
| CF-04 stale runbook | **CONFIRMED** | `RUNBOOK.md:69` `--artifact strategy --file strategy.json`, no `--handoff`; `cli.py:901` `--handoff required=True` |
| CF-05 bare command | **CONFIRMED** | `cli.py:812` emits `jobbsok stage-submit …` |
| CF-08 manual-PDF text | **CONFIRMED** | `pdf.py:209-212` unchanged; missing `--run`, bare exe, implies adoption |
| CF-09 no FormatChecker | **CONFIRMED** | `schemas.py:93` `Draft202012Validator(schema).iter_errors(...)`, no checker |
| CF-10 freeze/branch TOCTOU | **CONFIRMED** | `verify_frozen(layout, manifest)` — no staged-root parameter |
| NEW-R1 receipt-write gap | **CONFIRMED** | `cli.py:610` `atomic_write_json(report_path, report)` is a separate post-promotion mutation |
| NEW-R2 receipt read outside catch | **CONFIRMED** | `cli.py:593` `read_json(report_path)` sits **above** the `try:` at 594 |
| Plan Phase 2 errnos exist on Win | **CONFIRMED** | ENOSPC 28 · EDQUOT 10069 · EROFS 30 · EMFILE 24 · ENFILE 23 · EACCES 13 |
| Plan Phase 3 history-rollback feasible | **CONFIRMED** | history copies precede both writes; `superseded[name] is None` ⇒ delete-on-rollback |

---

## 3. Novel findings — neither document identified these

### N1 — CF-01's real trigger is an open Word document, not ENOSPC · **CRITICAL escalation**

Both documents reproduce CF-01 by *injecting* `OSError(28)` between promotions, and both therefore rate it as a fault-injection edge case. It is not.

Reproduced through `cli.main`, no monkeypatching, holding an ordinary read handle on the delivered letter DOCX — **exactly what Word does when the operator has the document open**:

```
before:  CV f56934f27267   letter e11a80b2233d
[legitimate Stage-3 resubmit + finalize, then render --force with letter held open]
render rc: 1 | RAW TRACEBACK ESCAPED: True
PermissionError: [WinError 5] Access is denied: '…\Soknad_…docx'
after :  CV b9a4ba1fd145   letter e11a80b2233d
>>> MIXED GENERATIONS ON DISK: True
```

1. New CV + old letter sit in `out/` as the employer package.
2. Raw traceback; rc=1; **in a multi-job run every later job is aborted**.
3. Trigger is the single most ordinary act in a one-human manual workflow: reviewing your own CV in Word, then re-rendering.
4. A live user Word session (`keywords.docx`, PID 20604) is running on this machine *right now* — this is the operator's normal state, not a lab condition.
5. Consequence for the plan: Phase 1's proof matrix (synthetic ENOSPC at promotion #1/#2) does not exercise the realistic path. A held-handle test is cheaper, needs no injection, and is a legitimate committed regression test.

### N2 — Plan phase ordering makes Phase 1 dead code for N1 · **plan defect D1**

6. `render_job` does not wrap the promotion section; `PermissionError` propagates out.
7. `cmd_render` catches **`except JobError` only** (`cli.py:604`).
8. Therefore any rollback added inside `render_job` **never executes** for the most realistic trigger unless the exception boundary is widened first.
9. The plan runs Phase 1 (rollback) *before* Phase 2 (scope/boundary). Wrong order. They are one atomic change: widen the catch, classify, rollback.

### N3 — Repeated `--dest` export always fails, with actively misleading advice · **novel**

```
1st export → [EXPORT-OK]     rc=0, 4 files
2nd export → [EXPORT-FAILED] rc=1
  "The existing DOCX was edited outside this pipeline and has been preserved.
   Use --force to overwrite it or --dest for a non-authoritative export."
```

10. Root cause: export passes no `previous_report`, so `previous` is empty, so the `foreign` precheck classifies **its own export from seconds earlier** as human-edited.
11. The remedy text tells the operator to "use `--dest`" — which is what they just did.
12. The sanctioned human-export path is effectively single-use per directory. This is `DFS-11`/`AR-11` collateral damage, not intended behaviour.

### N4 — RC-9 containment never landed at the render boundary · **broader than CF-02**

13. The finalization fixed unmodelled-exception containment for `status`, `validate`, `next`. `cmd_render` was missed.
14. CF-02 frames this as *classification* (ENOSPC mislabelled job-local). The prior defect is *containment*: non-`JobError` exceptions do not reach any handler at all.
15. Fix order: contain → classify → roll back. The plan states classification and rollback; it never states containment.

### N5 — Phase 4 has a smaller implementation than the plan proposes · **plan defect D4**

16. `FrozenRunAssets` already carries `base_dir: Path | None` and `run_dir` resolves through it (`manifest.py:101,109`).
17. Staged verification is therefore `FrozenRunAssets(layout, manifest, base_dir=staging)` — no new `run_dir=` kwarg on `verify_frozen`, no second verifier.

### N6 — Rollback directory placement is a hygiene/privacy defect · **plan defect D3**

18. Plan §4 Phase 1: *"copy … into a same-volume, short-named rollback directory under the destination."*
19. For canonical renders that is inside `out/` — an employer-delivery directory. For `--dest` it is inside the operator's chosen external folder.
20. A crash mid-rollback leaves copies of employer documents in a delivery directory with no receipt and no cleanup owner.
21. `TransactionDir` already provides same-volume short-path staging under the destination and cleans on exit. Reuse it; do not create a second convention.

### N7 — Correction to my own prior report

22. I previously reported `MANUAL_EXPORT_ACTION` as fixed. Only the **timeout** diagnostic was corrected. `pdf.py:209` is unchanged. v2's CF-08 is right; I was wrong.

### N8 — DOD-16B can close today

23. A human Word session is already open on this machine. The forced-timeout/human-session-survival subcheck is a five-minute test, not a scheduling problem.

---

## 4. Interaction effects the phase list must respect

24. **N4 → N1 → Phase 1.** Containment must precede rollback or rollback is unreachable.
25. **Phase 2 EACCES routing vs. N1.** Plan routes `EACCES/EPERM` to job-local-continue — correct — but rollback must run *first*, and the diagnostic must distinguish *"file is locked, close it and retry"* from the no-clobber message *"edited outside this pipeline."* Emitting the latter for a locked file trains the operator toward `--force`, degrading `AR-11`.
26. **N3 ∩ Phase 1.** Fixing export rollback without fixing the export ownership baseline makes the second export roll back to a state it should never have refused.
27. **CF-03 ∩ CF-07.** After a Stage-3 second-write failure (new final + old review), the correct recovery is review-only. That only works once CF-03 lands. Fixing CF-03 converts CF-07 from a data-integrity problem into an ordinary recovery path — which is exactly why v2's downgrade is right.
28. **CF-09 ∩ existing artifacts.** Enabling `FormatChecker` newly activates `date`. Every retained fixture, slice artifact and frozen manifest must be revalidated *before* the change is accepted, or the repaired build fails on its own evidence.
29. **CF-10 ∩ OneDrive.** The repository sits under a `OneDrive` path segment. Hash→copy TOCTOU is not theoretical here; sync-driven mtime/content churn is the exact failure mode.

---

## 5. Verdict

30. Both documents are honest and well-scoped. The plan is implementable as written and contains no architecture drift.
31. It nevertheless under-rates the one defect most likely to corrupt a real employer package, sequences its first two phases in an order that makes the fix unreachable for that defect, misses the export regression, and introduces an avoidable artifact-placement convention.
32. These are targeted amendments to a good plan — not grounds for a rewrite, and certainly not for another review cycle.
