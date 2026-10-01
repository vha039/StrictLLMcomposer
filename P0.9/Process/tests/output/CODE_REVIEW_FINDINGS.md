# Post-implementation code review — Avinor P0.9 source maintenance

Scope: the live `P0.9/Build` tree as it stands after the 29-step pass. Judged on code health, not on
provenance or spec-fidelity. Every claim below was verified against the tree, not inferred.
Interpreter: `.venv\Scripts\python.exe` (CPython 3.14.3). No Word/PDF process was started for this review.

---

## 1. Findings

Severity: **S1** = wrong behaviour or blocks work · **S2** = real defect, narrow blast radius · **S3** = correctness-neutral drift.

### F1 — Non-table `[voice]` escapes the ConfigurationError contract — **S2**

**Where** `runtime/jobbsok/settings.py:61-62`, inside `_check`:
```python
voice = data.get("voice")
if voice is not None:
    level = voice.get("social_register_calibration")
```

**Why problematic.** `settings.toml` is hand-maintained, and `[voice]` is the one value the operator is
expected to retype between runs. Every other malformed shape routes correctly: `[voice]` with a missing
key → `level is None` → `ConfigurationError`; wrong type, `True`, `2.5`, out-of-range → `ConfigurationError`.
CLI catches `JobbsokError` and exits 2 with a diagnostic. But a **non-table** `voice` — `voice = 2`,
`voice = "2"`, `voice = [1]` written in the file's root section — reaches `.get` on a non-dict and raises
`AttributeError`, which is not a `JobbsokError`: it escapes as an uncaught traceback with no diagnostic and
a different exit code. One input, two failure contracts. Trigger is narrow (requires a root-section scalar,
not the documented `[voice]` table), and the failure is loud, not silent — hence S2, not S1.

**Fix.** Inside the existing `voice is not None` branch, before `.get`:
```python
    if not isinstance(voice, dict):
        raise ConfigurationError(
            f"{path.name}: [voice] must be a TOML table containing "
            f"social_register_calibration. Found {voice!r}."
        )
```
Leave the existing integer/range clause byte-identical. No coercion, no default, no `or {}` fallback
(that would silently accept). Two lines, one file.

**Consequence of fixing.** `runtime/jobbsok/settings.py` is registered in `evidence/finalization/HASHES.sha256`
→ its digest must be refreshed in place in the same change.

---

### F2 — pytest launches Word at conftest import — **S1**

**Where** `runtime/tests/conftest.py:187-206`:
```python
def word_available() -> bool:
    if _shutil.which("powershell") is None: return False
    probe = subprocess.run(["powershell", ..., "New-Object -ComObject Word.Application", ...], timeout=60)
    return probe.returncode == 0

requires_word = pytest.mark.skipif(not word_available(), reason=...)
```

**Why problematic.** `skipif`'s condition is evaluated **at conftest import**, i.e. on every pytest
invocation — a single unrelated test, `--collect-only`, an IDE's test discovery. Consequences, in order of
cost:
1. **Non-hermetic test suite.** Merely listing tests instantiates a Word COM object. This is why full-suite
   verification keeps being deferred: you cannot run *any* test without the external side effect.
2. **Up to 60 s stall per invocation**, paid before a single test is selected.
3. **A wedged Word instance blocks collection outright** — the failure surfaces as "collection error", not
   "Word unavailable", which is a misleading diagnostic.
4. Machines without Word still pay a PowerShell process spawn on every run.

This is the single highest-cost defect in the tree: it degrades the verification loop itself.

**Fix.** Convert the helper into a session-scoped fixture; keep the probe command, its 60 s timeout and the
`$word.Quit()` teardown verbatim:
```python
@pytest.fixture(scope="session")
def word_available():
    import shutil as _shutil
    if _shutil.which("powershell") is None:
        pytest.skip("Word COM is unavailable; GATE-03 fallback is DEGRADED render state.")
    probe = subprocess.run([...unchanged...], capture_output=True, timeout=60)
    if probe.returncode != 0:
        pytest.skip("Word COM is unavailable; GATE-03 fallback is DEGRADED render state.")

requires_word = pytest.mark.usefixtures("word_available")
```
The ten existing `@requires_word` consumers are unchanged. Result: collection and non-Word tests never touch
Word; selected Word tests share exactly one probe per session.

**Accepted trade-off, state it explicitly.** Skip determination moves from collection-time to setup-time.
`--collect-only` no longer pre-marks those ten as skipped, and the skip is reported at run time instead.
No test gains or loses coverage; nothing is force-passed.

**Consequence of fixing.** `runtime/tests/conftest.py` is **not** registered in `HASHES.sha256`. Do **not**
add it — the registry lists maintained framework surfaces, and quietly widening it is a separate decision.
Leave the registry untouched for this fix.

---

### F3 — `docxfill.py` module docstring asserts the superseded letter contract — **S3**

**Where** `runtime/jobbsok/docxfill.py:11-14`:
> `CV_MASTER.docx has 17 non-data-bound SDTs (one per tag) and APPLICATION_MASTER.docx has 7 (6 unique, APP_JOB_TITLE twice)`

**Why problematic.** Zero runtime effect — `require_template_contract(path, expected)` receives `expected`
from `templates/template_map.json`, never from this text. But this is the module that *implements* the
contract, and it is now the **only place in the tree stating the old number as current fact**. The three
other descriptions were corrected (`prepare_masters.py` header, its paragraph table, the T18 assertion), and
the two remaining `7`s — `GATE-02.md:34` and the `prepared/*` inventory entries — are explicitly labelled
historical. Leaving one of four stale is strictly worse than fixing all four: it turns a consistent record
into a contradictory one, in the highest-authority location.

**Fix.** Replace that one sentence with the current fact, mirroring the wording E23 already applied:
> `CV_MASTER.docx carries 17 non-data-bound SDTs and APPLICATION_MASTER.docx carries 6, one per tag;
> neither uses w:dataBinding or docPartObj (GATE-02).`

Docstring only. No code change. `runtime/jobbsok/docxfill.py` is **not** registered in `HASHES.sha256`;
leave the registry alone.

---

### F4 — Four files flipped LF → CRLF — **S3**

**Where** `templates/template_map.json`, `runtime/tools/prepare_masters.py`,
`evidence/gates/GATE-02/inventory.json`, `evidence/finalization/HASHES.sha256`.
Cause: those four payloads end in `Path.write_text(...)`, which applies Windows newline translation. The
other twelve changed files never passed through `write_text` and remain LF.

**Why problematic.** The tree is otherwise uniformly LF. `prepare_masters.py` is now the only CRLF Python
file. Any future diff of these four shows whole-file churn instead of a readable delta, and any later
LF-normalising edit silently invalidates four registered digests.

**Why it is not urgent.** The digests were computed *after* those writes, so registry and bytes agree today.
Nothing parses these files line-sensitively (`json.loads`, Python's tokenizer, and `splitlines()` all handle
CRLF).

**Fix — two valid options, pick one; do not half-apply.**
- **(a) Leave as-is.** Accept mixed endings. Cost: permanent churn in four files.
- **(b) Normalise atomically.** Rewrite exactly those four files with `\r\n` → `\n`, then recompute their
  four entries in `HASHES.sha256` **in the same operation** — including `HASHES.sha256` itself, which is
  self-referential here and must be normalised last, after the other three digests are written.
  Note the ordering trap: `HASHES.sha256` does not register itself, so normalising it is hash-free, but the
  three entries it holds must be recomputed on post-normalisation bytes.

Recommendation: **(b)**, because it is cheap and the alternative permanently degrades diff quality on the
canonical template map. If the ordering constraint cannot be honoured in one operation, take (a) — a
half-applied normalisation leaves four stale digests, which is strictly worse than mixed endings.

**Root cause for the future.** Any payload writing a repo text file should use `write_bytes()` or
`open(..., newline="\n")`. `write_text()` is not newline-neutral on Windows.

---

### F5 — Relocated reference paragraph retains cell-tuned `spacing after=0` — **S3, observation only**

**Where** `templates/APPLICATION_MASTER.docx`, `APP_REFERENCE_OPTIONAL/sdtContent/w:p/w:pPr`:
after relocation to body level its only remaining property is `<w:spacing w:after="0"/>` (the cell-specific
`w:jc val="right"` was correctly removed).

**Why flagged.** `after=0` was tuned for a table cell. At body level the reference line now abuts the
`Title`-styled subject paragraph that follows it. In practice the `Title` style almost certainly supplies
its own spacing-before, so this is very likely fine — but it is **unverifiable without a real render**.

**Fix.** None now. This is the correct thing to look at on the next normal finalize/render, alongside the
other layout observations already queued there. Changing a spacing value on an unmeasured guess would be
worse than leaving it.

---

## 2. Verified non-issues — closed, do not re-open

| Checked | Result |
|---|---|
| `cli.py` `voice["social_register_calibration"]` direct key access | **Safe.** `load_path` always calls `_check`; `_check` rejects a `[voice]` table with a missing or invalid key before any consumer sees it. |
| `bundle["final_polish"]` vs. a schema | **No schema break.** `bundle` is only `print(json.dumps(...))`-ed to stdout in `cmd_context`; nothing validates it. |
| `[voice]` vs. manifest / branch comparison | **Unchanged by design.** `settings.snapshot()` does not include voice, so `settings_snapshot` and `branch.py`'s comparison are byte-identical to before. Dial-only tuning still needs an explicit `--from-stage 3` child. |
| A settings schema forbidding `[voice]` | **None exists.** `schemas/` has no settings schema. |
| Whole-tree import health | All `jobbsok.*` and `tools.*` modules import; all 8 test modules parse. |
| Dangling references to removed text | **Zero.** Swept the live tree for 10 strings this pass deleted (doctrine premise, ad-echo clause, realization-pass block, uniqueness goal, closing rule, gap paragraph, lifecycle example, S3 item 5, prompt voice rule, `"Stilling:"`). Only hit: a stored extracted-PDF text sample under `evidence/vertical_slice/`, which is an output artifact, not a consumer. |
| Template contract consumers | `require_template_contract` sources `expected` from `template_map.json` at runtime. No hardcoded letter count remains in executable code. |
| `template_map.json` / `inventory.json` / `prepare_masters.py` content | Diffed against pre-edit copies: exactly the intended deltas, nothing else. All four historical inventory entries byte-identical; two new keys added. |
| Registry coverage | All 16 changed paths present and hash-matching. The 17 entries that *don't* match are files this pass never touched (schemas, `render.py`, `manifest.py`, `pyproject.toml`, …) — pre-existing drift, correctly left alone. |
| Master integrity | 17 CV / 6 letter controls; competence run kept `color 17324D` + `sz 24` with only `w:b` removed; sizes 39124→39127 and 37516→37480 confirm zip compression preserved. |
| Stray build artifacts | `.pytest_cache` predates this work (2026-08-23); no new `__pycache__` written. |
| `[voice]` placement in `settings.toml` | Line 30, between `[personality]` and `[stages]`. `conftest.set_role_mapping`'s `[stages.role_mapping]` regex is unaffected. |

---

## 3. Does the fix set cohere?

**Yes, with one sequencing constraint.**

| Fix | File | Registry action | Interacts with |
|---|---|---|---|
| F1 | `runtime/jobbsok/settings.py` | refresh its existing entry **in place** | none |
| F2 | `runtime/tests/conftest.py` | **none** — not registered, do not add | none |
| F3 | `runtime/jobbsok/docxfill.py` | **none** — not registered | none |
| F4(b) | 4 files + `HASHES.sha256` | recompute 3 entries, normalise the registry last | **F1** — if both are applied, do F1 first, then F4(b), so the settings digest is computed once on final bytes |

The four touch three code files, one docstring, and provenance. None changes a public API, CLI surface,
schema, package field, manifest shape, template, policy text or rendered output. Applied together the result
is: one uniform failure contract for operator-maintained settings; a hermetic test suite that can finally be
run end-to-end without launching an external application; a single consistent statement of the 17/6 contract
across all four places that describe it; and uniform line endings with a registry that matches actual bytes.

**The one ordering rule:** F1 before F4(b). Everything else is order-independent.

**What this does not establish, before or after:** Word-open compatibility, pagination, PDF behaviour, or
any output-quality property. Those need a normal finalize/render, which is out of scope here. F2 is the
prerequisite that makes the full-suite run *possible*; it does not perform it, and the suite contains
PDF-producing cases that remain deliberately unrun.

---

## 4. Direct feedback on the GPT-6 Astra plan

**Both of its factual claims are correct and independently confirmed here** — the CRLF flip (F4) and the
import-time Word probe (F2). Its adjudication table is sound on every discard, and it is right that
`prepare_masters`' core.xml note and the voice/manifest exclusion are non-issues. Specific feedback:

1. **Its two fixes are the right two.** Astra's A = F1 and B = F2, with essentially the fix designs proposed
   here. No disagreement on substance.
2. **It under-rates F2 and over-rates F1.** F1 is a narrow-trigger, loud-failure robustness gap. F2 makes the
   entire test suite non-hermetic and is the reason full-suite verification keeps being deferred. The plan
   presents them as peers; F2 should be first and framed as the verification-loop unblocker.
3. **It missed F3.** `docxfill.py`'s docstring is the fourth description of the letter contract and the only
   one still asserting `7` as current fact — in the implementing module. Astra swept the executable
   consumers and stopped there.
4. **Its registry step is half-wrong.** Refreshing `settings.py` in place: correct. Appending
   `runtime/tests/conftest.py`: **don't**. That path has never been registered; adding it because you happened
   to edit it silently widens what the registry claims to cover. Its warning to preserve existing line
   endings when hand-editing `HASHES.sha256` is a good catch — and F4(b) here supersedes it by normalising
   deliberately rather than preserving by accident.
5. **On CRLF it is right for an incomplete reason.** "No broken endpoint demonstrated" is true but weak. The
   stronger argument for not touching it casually is that the digests were computed on the CRLF bytes, so a
   drive-by normalisation invalidates four registry entries. That converts "harmless" into "harmless unless
   you touch it wrong", which is what makes the atomic option (b) the right shape.
6. **Its `E26` blank-line finding is not a deviation.** A trailing empty line inside a fenced block encodes
   the terminating newline of the last content line. The file ends `met.\n` with a blank-line separator
   before the new heading — which is what the block specifies. Harmless either way; correctly discarded.
7. **Its "earlier E22 stop" did not happen in this tree.** E22 applied cleanly and its diff is exactly the
   three intended changes. Presenting it as a finding about this implementation is misleading.
8. **Its verification plan is good** — particularly refusing to claim a full-suite PASS and noting that
   non-Word tests still include PDF-producing cases. Keep that honesty. One addition: after F2, explicitly
   confirm that `pytest --collect-only` completes with **no** PowerShell/Word process spawned. That is the
   assertion that proves F2 actually landed, and its plan only implies it.
