Listed directory P0.9
Searched for files: *
Searched for files: *
Searched for files: *.ps1
Searched for files: *
Searched for files: *
Searched for files: *
Searched for files: *
Searched for files: *test*
Searched for files: *
Viewed P0.9_FINAL_NORMATIVE_SPECIFICATION.md:1-400
Viewed P0.9_FINAL_NORMATIVE_SPECIFICATION.md:401-800
Viewed P0.9_FINAL_NORMATIVE_SPECIFICATION.md:801-1259
Viewed P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md:1-300
Viewed P0.9_FINAL_IMPLEMENTATION_AND_VERIFICATION_CONTRACT.md:301-600
Viewed BUILDER_REPORT.md:1-214
Viewed P0.9_FINAL_DECISION_AND_ADOPTION_RECORD.md:1-200
Searched for files: *
Searched for files: *
Viewed pyproject.toml:1-39
Searched for files: *
Searched for files: *slice*
Viewed errors.py:1-124
Viewed paths.py:1-318
Viewed ioenc.py:1-25
Viewed hashing.py:1-55
Viewed atomicio.py:1-198
Viewed settings.py:1-131
Viewed schemas.py:1-126
Viewed batchinput.py:1-236
Viewed manifest.py:1-490
Viewed baseline.py:1-212
Viewed evidence_index.py:1-258
Viewed vacancy.py:1-215
Viewed artifacts.py:1-268
Viewed validate.py:1-353
Viewed merge.py:1-103
Viewed docxfill.py:1-449
Viewed pdf.py:1-295
Viewed render.py:1-582
Viewed failure.py:1-111
Viewed status.py:1-409
Viewed leakage.py:1-186
Viewed branch.py:1-249
Viewed cli.py:1-702
Viewed conftest.py:1-177
Searched for files: *
Viewed test_t01_t04_run_lifecycle.py:1-250
Viewed test_t05_t08_ownership_schema_failure.py:1-250
Viewed test_t09_t12_state_evidence.py:1-250
Viewed test_t16_t18_containment_template.py:1-250
Viewed test_t19_t23_render_security.py:1-250
Searched for "manifest_sha256"
Viewed package.schema.json:1-184
Ran command: `python -c "
import sys
from pathlib import Path
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime')
from conftest import make_build_root, FIXED_MOMENT
from jobbsok.manifest import freeze, load_manifest
from jobbsok.atomicio import read_json
from jobbsok import branch as branch_module
from jobbsok import artifacts as artifacts_module
from jobbsok import status as status_module
import tempfile, shutil

tmp = Path(tempfile.mkdtemp())
layout = make_build_root(tmp)
res = freeze(layout, layout.inbox / 'batch_input.csv', reviewed_by='Test', moment=FIXED_MOMENT)
run_id = res.run_id
from tools.make_fixtures import build
fdir = layout.root / 'fixtures'
build(layout, run_id, fdir)
job_id = 'testetaten_radgiver'

for stage, art, fn in [(1, 'strategy', 'strategy.valid.json'), (2, 'draft_package', 'draft_package.json'), (3, 'final_package', 'final_package.json'), (3, 'review', 'review.json')]:
    artifacts_module.submit(layout, run_id, job_id, stage=stage, artifact=art, payload=read_json(fdir / fn), timestamp='20260823T060000Z')

st_parent = status_module.derive(layout, load_manifest(layout, run_id))
print('Parent status:', st_parent['jobs'][0]['production_state'], st_parent['jobs'][0]['highest_valid_stage'])

# Now branch!
br_res = branch_module.branch(layout, run_id, reviewed_by='Test', moment=FIXED_MOMENT)
child_id = br_res.run_id
print('Branch res ok:', br_res.ok, 'disposition:', br_res.disposition)

st_child = status_module.derive(layout, load_manifest(layout, child_id))
print('Child status:', st_child['jobs'][0]['production_state'], st_child['jobs'][0]['highest_valid_stage'])
print('Child stale scope:', st_child['jobs'][0]['stale_scope'])
print('Child recommended action:', st_child['jobs'][0]['recommended_action'])
shutil.rmtree(tmp)
"`
Ran command: `python -c "
import sys
from pathlib import Path
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime')
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime\tests')
from conftest import make_build_root, FIXED_MOMENT
from jobbsok.manifest import freeze, load_manifest
from jobbsok.atomicio import read_json
from jobbsok import branch as branch_module
from jobbsok import artifacts as artifacts_module
from jobbsok import status as status_module
import tempfile, shutil

tmp = Path(tempfile.mkdtemp())
layout = make_build_root(tmp)
res = freeze(layout, layout.inbox / 'batch_input.csv', reviewed_by='Test', moment=FIXED_MOMENT)
run_id = res.run_id
from tools.make_fixtures import build
fdir = layout.root / 'fixtures'
build(layout, run_id, fdir)
job_id = 'testetaten_radgiver'

for stage, art, fn in [(1, 'strategy', 'strategy.valid.json'), (2, 'draft_package', 'draft_package.json'), (3, 'final_package', 'final_package.json'), (3, 'review', 'review.json')]:
    artifacts_module.submit(layout, run_id, job_id, stage=stage, artifact=art, payload=read_json(fdir / fn), timestamp='20260823T060000Z')

st_parent = status_module.derive(layout, load_manifest(layout, run_id))
print('Parent status:', st_parent['jobs'][0]['production_state'], 'highest_stage:', st_parent['jobs'][0]['highest_valid_stage'], 'triage:', st_parent['jobs'][0]['semantic_triage'])

# Now branch!
br_res = branch_module.branch(layout, run_id, reviewed_by='Test', moment=FIXED_MOMENT)
child_id = br_res.run_id
print('Branch res ok:', br_res.ok, 'disposition:', br_res.disposition)

st_child = status_module.derive(layout, load_manifest(layout, child_id))
print('Child status:', st_child['jobs'][0]['production_state'], 'highest_stage:', st_child['jobs'][0]['highest_valid_stage'], 'triage:', st_child['jobs'][0]['semantic_triage'])
print('Child stale scope:', st_child['jobs'][0]['stale_scope'])
print('Child recommended action:', st_child['jobs'][0]['recommended_action'])
shutil.rmtree(tmp)
"`
Searched for files: *python.exe*
Ran command: `Get-Command python*, uv*, pytest* | Select-Object Name, Source`
Ran command: `Get-ChildItem -Path C:\Users\veggi\.virtualenvs, C:\Users\veggi\.venv, C:\Users\veggi\AppData\Local\Programs, C:\Users\veggi\AppData\Local\uv, C:\Users\veggi\.cargo\bin -ErrorAction SilentlyContinue`
Ran command: `C:\Users\veggi\AppData\Local\Python\bin\python.exe -m pip list`
Ran command: `Get-ChildItem -Path C:\Users\veggi\.cargo\bin\uv.exe, C:\Users\veggi\AppData\Local\Microsoft\WinGet\Packages\*, C:\Users\veggi\.local\bin\* -ErrorAction SilentlyContinue`
Ran command: `Get-ChildItem -Path C:\Users\veggi\AppData\ -Filter "jsonschema*" -Recurse -ErrorAction SilentlyContinue | Select-Object -First 10 FullName`
Ran command: `Get-Command uv -ErrorAction SilentlyContinue`
Searched for files: *venv*
Ran command: `c:\Users\veggi\miniforge3\python.exe -m pip list`
Ran command: `Get-ChildItem c:\Users\veggi\miniforge3\envs\`
Ran command: `C:\Users\veggi\AppData\Local\Python\bin\python.exe -m pip install jsonschema pymupdf`
Ran command: `python -m pytest runtime/tests -q`
Ran command: `python -c "
import sys
from pathlib import Path
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime')
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime\tests')
from conftest import make_build_root, FIXED_MOMENT
from jobbsok.manifest import freeze, load_manifest
from jobbsok.atomicio import read_json
from jobbsok import branch as branch_module
from jobbsok import artifacts as artifacts_module
from jobbsok import status as status_module
import tempfile, shutil

tmp = Path(tempfile.mkdtemp())
layout = make_build_root(tmp)
res = freeze(layout, layout.inbox / 'batch_input.csv', reviewed_by='Test', moment=FIXED_MOMENT)
run_id = res.run_id
from tools.make_fixtures import build
fdir = layout.root / 'fixtures'
build(layout, run_id, fdir)
job_id = 'testetaten_radgiver'

for stage, art, fn in [(1, 'strategy', 'strategy.valid.json'), (2, 'draft_package', 'draft_package.json'), (3, 'final_package', 'final_package.json'), (3, 'review', 'review.json')]:
    artifacts_module.submit(layout, run_id, job_id, stage=stage, artifact=art, payload=read_json(fdir / fn), timestamp='20260823T060000Z')

st_parent = status_module.derive(layout, load_manifest(layout, run_id))
print('Parent status:', st_parent['jobs'][0]['production_state'], 'highest_stage:', st_parent['jobs'][0]['highest_valid_stage'], 'triage:', st_parent['jobs'][0]['semantic_triage'])

# Now branch!
br_res = branch_module.branch(layout, run_id, reviewed_by='Test', moment=FIXED_MOMENT)
child_id = br_res.run_id
print('Branch res ok:', br_res.ok, 'disposition:', br_res.disposition)

st_child = status_module.derive(layout, load_manifest(layout, child_id))
print('Child status:', st_child['jobs'][0]['production_state'], 'highest_stage:', st_child['jobs'][0]['highest_valid_stage'], 'triage:', st_child['jobs'][0]['semantic_triage'])
print('Child stale scope:', st_child['jobs'][0]['stale_scope'])
print('Child recommended action:', st_child['jobs'][0]['recommended_action'])
shutil.rmtree(tmp)
"`
Used tool: manage_task
Used tool: manage_task
Ran command: `python -c "
import sys, os
from pathlib import Path
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime')
from jobbsok.paths import is_reparse_point, resolve_within, Layout

p = Path(r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build')
print('Path:', p)
print('is_symlink:', p.is_symlink())
print('isjunction:', os.path.isjunction(p))
st = os.lstat(p)
print('st_reparse_tag:', hex(getattr(st, 'st_reparse_tag', 0)))
print('is_reparse_point:', is_reparse_point(p))

layout = Layout(p)
try:
    res = resolve_within(layout.policy, layout.policy / 'settings.toml')
    print('resolve_within success:', res)
except Exception as e:
    print('resolve_within failed:', e)
"`
Ran command: `python -c "
import subprocess

ps_test = '''
$w1 = New-Object -ComObject Word.Application
$p1 = (Get-Process -Name WINWORD).Id
$w2 = New-Object -ComObject Word.Application
$p2 = (Get-Process -Name WINWORD).Id
Write-Output \"P1: $p1, P2: $p2\"
$w1.Quit()
$w2.Quit()
'''
res = subprocess.run(['powershell', '-NoProfile', '-Command', ps_test], capture_output=True, text=True)
print(res.stdout)
print(res.stderr)
"`
Ran command: `python -c "
import subprocess

ps_test = '''
$w1 = New-Object -ComObject Word.Application
$p1 = (Get-Process -Name WINWORD).Id
$w2 = New-Object -ComObject Word.Application
$p2 = (Get-Process -Name WINWORD).Id
Write-Output \"P1: $p1, P2: $p2\"
$w1.Quit()
$w2.Quit()
'''
p = subprocess.run(['powershell', '-NoProfile', '-Command', ps_test], capture_output=True, text=True)
print(p.stdout)
print(p.stderr)
"`
Ran command: `powershell -NoProfile -Command "
$w1 = New-Object -ComObject Word.Application
$p1 = (Get-Process -Name WINWORD).Id
$w2 = New-Object -ComObject Word.Application
$p2 = (Get-Process -Name WINWORD).Id
Write-Host ('P1=' + ($p1 -join ',') + ' P2=' + ($p2 -join ','))
$w1.Quit()
$w2.Quit()
"`
Ran command: `python -c "
import sys
from pathlib import Path
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime')
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime\tests')
from conftest import make_build_root, FIXED_MOMENT
from jobbsok.manifest import freeze, load_manifest
from jobbsok import status as status_module
import tempfile, shutil

tmp = Path(tempfile.mkdtemp())
layout = make_build_root(tmp)
res = freeze(layout, layout.inbox / 'batch_input.csv', reviewed_by='Test', moment=FIXED_MOMENT)
run_id = res.run_id

# Plant a malformed JSON file in current/
strat_path = layout.job_dir(run_id, 'testetaten_radgiver') / 'current' / 'strategy.json'
strat_path.write_text('{ unclosed json: ', encoding='utf-8')

try:
    st = status_module.derive(layout, load_manifest(layout, run_id))
    print('Derived status successfully:', st)
except Exception as e:
    print('CRASHED on malformed JSON with:', type(e).__name__, e)

shutil.rmtree(tmp)
"`
Ran command: `python -c "
import sys
from pathlib import Path
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime')
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime\tests')
from conftest import make_build_root, FIXED_MOMENT
from jobbsok.manifest import freeze, load_manifest
from jobbsok import status as status_module
import tempfile, shutil

tmp = Path(tempfile.mkdtemp())
layout = make_build_root(tmp)
res = freeze(layout, layout.inbox / 'batch_input.csv', reviewed_by='Test', moment=FIXED_MOMENT)
run_id = res.run_id

# Plant a JSON array in current/
strat_path = layout.job_dir(run_id, 'testetaten_radgiver') / 'current' / 'strategy.json'
strat_path.write_text('[1, 2, 3]', encoding='utf-8')

try:
    st = status_module.derive(layout, load_manifest(layout, run_id))
    print('Derived status successfully:', st)
except Exception as e:
    print('CRASHED on JSON array with:', type(e).__name__, e)

shutil.rmtree(tmp)
"`
Ran command: `python -c "
from pathlib import Path
from zipfile import ZipFile
import sys
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime')
from jobbsok.docxfill import read_core_properties

for name in ('CV_MASTER.docx', 'APPLICATION_MASTER.docx'):
    p = Path(r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\templates') / name
    with ZipFile(p) as z:
        print(name, read_core_properties(z))
"`
Ran command: `python -c "
from pathlib import Path
from zipfile import ZipFile

p = Path(r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\templates\CV_MASTER.docx')
with ZipFile(p) as z:
    raw = z.read('docProps/core.xml')
    print(raw.decode('utf-8'))
"`
Ran command: `python -c "
from pathlib import Path
from zipfile import ZipFile

p = Path(r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\templates\CV_MASTER.docx')
with ZipFile(p) as z:
    raw = z.read('docProps/core.xml')
    print(repr(raw))
"`
Ran command: `python -c "
import sys
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime')
from jobbsok.leakage import scan

res = scan('Erfaring fra EDU-01 og EMP-01 i prosjektet.', file_label='test', location='test')
print('Errors:', [v.observed for v in res.errors])
"`
Viewed stage3_final_writer_review.md:1-120
Ran command: `python -c "
import sys
from pathlib import Path
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime')
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime\tests')
from conftest import make_build_root, FIXED_MOMENT
from jobbsok.manifest import freeze, load_manifest
from jobbsok.atomicio import read_json, atomic_write_json
from jobbsok import artifacts as artifacts_module
from jobbsok import status as status_module
from jobbsok import render as render_module
import tempfile, shutil

tmp = Path(tempfile.mkdtemp())
layout = make_build_root(tmp)
res = freeze(layout, layout.inbox / 'batch_input.csv', reviewed_by='Test', moment=FIXED_MOMENT)
run_id = res.run_id
from tools.make_fixtures import build
fdir = layout.root / 'fixtures'
build(layout, run_id, fdir)
job_id = 'testetaten_radgiver'

for stage, art, fn in [(1, 'strategy', 'strategy.valid.json'), (2, 'draft_package', 'draft_package.json'), (3, 'final_package', 'final_package.json'), (3, 'review', 'review.json')]:
    artifacts_module.submit(layout, run_id, job_id, stage=stage, artifact=art, payload=read_json(fdir / fn), timestamp='20260823T060000Z')

# Finalize
fp = artifacts_module.load(layout, run_id, job_id, 'final_package')
fp['finalization'] = {'state': 'FINALIZED', 'document_date': '2026-08-23', 'finalized_at': '2026-08-23T06:00:00Z', 'finalized_by': 'Test'}
atomic_write_json(artifacts_module.artifact_path(layout, run_id, job_id, 'final_package'), fp)

# Fake/write a render report
rep = {
    'artifact_role': 'RENDER_REPORT',
    'binding': {
        'run_id': run_id, 'job_id': job_id,
        'final_package_sha256': artifacts_module.artifact_hash(fp),
        'document_date': '2026-08-23',
        'baseline_map_sha256': '0'*64, 'cv_master_sha256': '0'*64,
        'letter_master_sha256': '0'*64, 'template_map_sha256': '0'*64,
        'render_config': {'converter': 'none', 'invocation_granularity': 'per_document'}
    },
    'render_state': {'cv_docx': 'OK', 'cv_pdf': 'DEGRADED', 'letter_docx': 'OK', 'letter_pdf': 'DEGRADED', 'overall': 'DEGRADED'},
    'documents': [{'component': 'cv', 'format': 'docx', 'state': 'OK', 'output_path': 'out/CV.docx'}],
    'rendered_at': '2026-08-23T06:00:00Z'
}
atomic_write_json(layout.job_dir(run_id, job_id) / 'current' / 'render_report.json', rep)

st1 = status_module.derive(layout, load_manifest(layout, run_id))
print('Render state before edit:', st1['jobs'][0]['render_state'])

# Now edit final_package.json (e.g. change headline)
fp['cv']['headline'] = 'Endret overskrift som krever ny rendering'
atomic_write_json(artifacts_module.artifact_path(layout, run_id, job_id, 'final_package'), fp)

st2 = status_module.derive(layout, load_manifest(layout, run_id))
print('Render state after final_package edited:', st2['jobs'][0]['render_state'])
print('Output paths reported after edit:', st2['jobs'][0]['output_paths'])

shutil.rmtree(tmp)
"`
Viewed template_map.json:1-236
Ran command: `python -c "
import inspect
from pathlib import Path
import sys
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime')
import jobbsok

runtime_dir = Path(r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime\jobbsok')
for py_file in runtime_dir.glob('*.py'):
    text = py_file.read_text(encoding='utf-8')
    if 'failure' in text:
        matches = [line.strip() for line in text.splitlines() if 'failure' in line and not line.strip().startswith('#') and not line.strip().startswith('\"\"\"')]
        if matches:
            print(py_file.name, matches)
"`
Ran command: `python -c "
from pathlib import Path
runtime_dir = Path(r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime\jobbsok')
for py_file in runtime_dir.glob('*.py'):
    text = py_file.read_text(encoding='utf-8')
    if 'failure' in text:
        for i, line in enumerate(text.splitlines(), 1):
            if 'record(' in line or 'failure.' in line or 'failure_' in line:
                print(f'{py_file.name}:{i}: {line.strip()}')
"`
Viewed test_t05_t08_ownership_schema_failure.py:240-335
Ran command: `python -c "
import xml.etree.ElementTree as ET
import sys
sys.path.insert(0, r'c:\Users\veggi\OneDrive\Documents\Codex\Jobbsøk_26\P0.9\Build\runtime')
from jobbsok.docxfill import _set_run_text, W

r = ET.Element(f'{W}r')
try:
    _set_run_text(r, 'Test med formfeed \x0c og esc \x1b')
    s = ET.tostring(r, encoding='utf-8')
    print('Serialized:', s)
except Exception as e:
    print('Failed with:', type(e).__name__, e)
"`
Ran command: `python -c "
import subprocess

script = r'''
Write-Output (\"ARG0: \" + $args[0])
Write-Output (\"ARG1: \" + $args[1])
'''
cmd = ['powershell', '-NoProfile', '-NonInteractive', '-Command', script, 'first_arg', 'second_arg']
res = subprocess.run(cmd, capture_output=True, text=True)
print('STDOUT:', res.stdout)
print('STDERR:', res.stderr)
print('RETURNCODE:', res.returncode)
"`
Created test_args.py
Ran command: `python C:\Users\veggi\.gemini\antigravity\brain\ceddaf9e-918e-4117-8aab-b0356368b374\scratch\test_args.py`
Viewed pdf.py:1-100
Viewed pdf.py:90-140
Created test_word_orphan.py
Ran command: `python C:\Users\veggi\.gemini\antigravity\brain\ceddaf9e-918e-4117-8aab-b0356368b374\scratch\test_word_orphan.py`
Searched for files
Searched for files: *
Viewed P0.9_FINAL_CRITIQUE_ADJUDICATION_AND_CLOSURE_MATRIX.md:1-100

# Red-Team Audit Report: Jobbsøk_26 P0.9 Implementation

**Scope:** Adversarial negative-space exploration of `P0.9/Build/` (runtime, lifecycle, render transaction, state axes, Word COM/PowerShell integration, branching, failure models, schema boundaries). Tested strictly on scratch copies without modifying canonical files.

---

## 1. Adversarial Findings & Counterexample Matrix

| ID | Attacked State / Transition | Reproduction / Evidence | Consequence | Disposition | Severity | Confidence | Best Action | Regression Risk |
|---|---|---|---|---|---|---|---|---|
| **RT-01** | Child run rebind cascade across multi-stage artifacts during `jobbsok branch` | Branching a staged run with 4 valid artifacts (`strategy`, `draft_package`, `final_package`, `review`) marks all artifacts `REUSED`. `branch.py` rebinds `strategy.json` (`binding.run_id`, `binding.manifest_sha256`), altering its canonical hash. However, `branch.py` does **not** update `binding.strategy_sha256` in `draft_package.json`, `binding.draft_sha256` in `final_package.json`, or `binding.final_package_sha256` in `review.json`. | Running [`jobbsok status`](file:///c:/Users/veggi/OneDrive/Documents/Codex/Jobbs%C3%B8k_26/P0.9/Build/runtime/jobbsok/cli.py#L427) on the child immediately reports `production_state: STALE`, `stale_scope: ['draft', 'final', 'review']`, `highest_valid_stage: STRATEGY`, and `triage: None`. Artifact reuse across runs is completely broken on the very first status check. | **FIX** | **HIGH** | **HIGH** | In [`branch.py`](file:///c:/Users/veggi/OneDrive/Documents/Codex/Jobbs%C3%B8k_26/P0.9/Build/runtime/jobbsok/branch.py#L225), perform a topological propagation pass over `REUSED` artifacts: update `draft_package.binding.strategy_sha256` to the child `strategy` hash, `final_package.binding.draft_sha256` to the child `draft` hash, and `review.binding.final_package_sha256` to the child `final` hash before computing final hashes. | Low |
| **RT-02** | Staleness blindness for `render_report.json` in status derivation | Finalize and render a job (`render_state: OK`, output path `out/CV.docx`). Then modify `final_package.json` (e.g. edit headline/bullets). [`status_module.derive`](file:///c:/Users/veggi/OneDrive/Documents/Codex/Jobbs%C3%B8k_26/P0.9/Build/runtime/jobbsok/status.py#L125) reads `current/render_report.json` without verifying `report["binding"]["final_package_sha256"] == artifact_hash(loaded["final_package"])`. | Status and queue view continue reporting `render_state: OK` with output paths pointing to `out/CV.docx`, completely hiding the fact that rendered files in `out/` are stale and reflect the superseded final package. | **FIX** | **HIGH** | **HIGH** | In [`status.py`](file:///c:/Users/veggi/OneDrive/Documents/Codex/Jobbs%C3%B8k_26/P0.9/Build/runtime/jobbsok/status.py#L147-L168), compare `render_report["binding"]["final_package_sha256"]` against current `final_package`. If mismatched, set `render_state["overall"] = "STALE"` (or `"NOT_RENDERED"`) and suppress/flag `output_paths`. | Low |
| **RT-03** | Partial promotion & silent deliverable divergence under human edit collision | Manually edit `out/CV_...docx`. Rerun `jobbsok render`. [`promote_file`](file:///c:/Users/veggi/OneDrive/Documents/Codex/Jobbs%C3%B8k_26/P0.9/Build/runtime/jobbsok/atomicio.py#L107) returns `REFUSED_FOREIGN` for the DOCX. However, `pdf_module.convert` previously converted the *temporary pipeline staged DOCX* to a temporary PDF, which `promote_file` then promotes into `out/CV_...pdf` (overwriting or creating it). | `out/CV_...docx` contains human-edited text while `out/CV_...pdf` is updated with automated pipeline text. The deliverables in `out/` silently contradict each other. | **FIX** | **MEDIUM** | **HIGH** | In [`render_job`](file:///c:/Users/veggi/OneDrive/Documents/Codex/Jobbs%C3%B8k_26/P0.9/Build/runtime/jobbsok/render.py#L380), if a component's DOCX promotion is refused/diverted (`REFUSED_FOREIGN`), abort promotion of the corresponding PDF from the staging directory. | Low |
| **RT-04** | Tooling crash on malformed or non-object JSON generated by model stages | Plant malformed JSON (e.g. `{ unclosed: `) or a JSON array (`[1, 2, 3]`) in `current/strategy.json`. Run `jobbsok status`, `jobbsok validate`, or `jobbsok next`. [`artifacts.load()`](file:///c:/Users/veggi/OneDrive/Documents/Codex/Jobbs%C3%B8k_26/P0.9/Build/runtime/jobbsok/artifacts.py#L106) calls `read_json()`, raising uncaught `ValueError` or `AttributeError: 'list' object has no attribute 'get'`. | Tooling crashes with Python traceback instead of gracefully recording `production_state: FAILED` with a `CTR-02` schema violation. | **FIX** | **MEDIUM** | **HIGH** | In [`artifacts.py`](file:///c:/Users/veggi/OneDrive/Documents/Codex/Jobbs%C3%B8k_26/P0.9/Build/runtime/jobbsok/artifacts.py#L106), catch `ValueError` and validate top-level `dict` type; return a structured invalid-file representation so [`validate_artifact`](file:///c:/Users/veggi/OneDrive/Documents/Codex/Jobbs%C3%B8k_26/P0.9/Build/runtime/jobbsok/validate.py#L328) and `status.py` report `FAILED` cleanly. | Low |
| **RT-05** | Write root containment escape via `jobbsok render --dest` | Pass `--dest ../../../policy` or any arbitrary path to `jobbsok render`. [`cmd_render`](file:///c:/Users/veggi/OneDrive/Documents/Codex/Jobbs%C3%B8k_26/P0.9/Build/runtime/jobbsok/cli.py#L399) passes `destination=Path(args.dest)` straight to `render_job`, which calls `out_dir.mkdir()` and writes deliverables without checking `assert_writable`. | Violates Spec §17.2 / Contract §15 by permitting rendering writes outside approved write roots (e.g. overwriting policy or authorities). | **FIX** | **MEDIUM** | **HIGH** | Enforce [`assert_writable(layout, destination)`](file:///c:/Users/veggi/OneDrive/Documents/Codex/Jobbs%C3%B8k_26/P0.9/Build/runtime/jobbsok/paths.py#L254) on `args.dest` in `cli.py` / `render.py`. | Low |
| **RT-06** | Orphaned `WINWORD.EXE` process leak on PowerShell timeout | In [`pdf.py`](file:///c:/Users/veggi/OneDrive/Documents/Codex/Jobbs%C3%B8k_26/P0.9/Build/runtime/jobbsok/pdf.py#L99), when `subprocess.run(timeout=timeout)` expires, Python terminates `powershell.exe`. Because `WINWORD.EXE` is managed out-of-process by DCOM under `svchost.exe`, killing `powershell.exe` leaves `WINWORD.EXE` running invisibly in the background. | Orphaned Word instances accumulate, consume memory, and hold open file locks on documents in `out/`. | **IMPROVE** | **LOW** | **HIGH** | In `pdf.py`, on `TimeoutExpired`, explicitly terminate any child/associated `WINWORD.EXE` or attach Word to a Windows Job Object configured with `KillOnJobClose`. | Low |
| **RT-07** | Omission of hyphenated claim IDs (`EMP-`, `EDU-`) in leakage regex | `evidence_index.py` defines source claim ID tokens with pattern `\b(?:CLM\|EDU\|PRJ\|EMP\|OHV)-...`. In [`leakage.py`](file:///c:/Users/veggi/OneDrive/Documents/Codex/Jobbs%C3%B8k_26/P0.9/Build/runtime/jobbsok/leakage.py#L56), pattern 5 only checks `(?:CLM\|PRJ\|OHV)-...` while pattern 3 checks `(?:EMP\|EDU\|SEC)_...` (with underscores). `scan("Erfaring fra EDU-01 og EMP-01")` returns 0 errors. | Hyphenated source claim identifiers (`EMP-OUS-01`, `EDU-MAST-01`) pass through to employer-facing text undetected. | **FIX** | **LOW** | **HIGH** | Add `EDU` and `EMP` to the hyphenated pattern in `leakage.py`. | Low |
| **RT-08** | Runtime CLI disconnected from `failure.py` record lifecycle | [`failure.py`](file:///c:/Users/veggi/OneDrive/Documents/Codex/Jobbs%C3%B8k_26/P0.9/Build/runtime/jobbsok/failure.py) defines `record()` and `clear()`, and `status.py` reads `failure.json`. However, no command in `cli.py` (e.g. `cmd_stage_submit`) ever calls `failure.record()` or `failure.clear()`. Only test `test_t08` calls them manually. | Failed `stage-submit` commands do not persist a `failure.json` record on disk; status derivation relies exclusively on artifact absence/invalidation. | **IMPROVE** | **LOW** | **HIGH** | Invoke `failure.record()` in `cmd_stage_submit` on mechanical rejection, and `failure.clear()` on successful submission. | Low |
| **RT-09** | Post-freeze immutable inbox isolation | Once a run freezes, runtime commands resolve inputs exclusively from `runs/<run_id>/frozen/` and `jobs/<job_id>/source/`. Any subsequent modification or deletion in `inbox/` has zero impact on active runs. | Preserves absolute run immutability against external workspace mutations. | **KEEP** | **INFO** | **HIGH** | Retain as designed. | N/A |
| **RT-10** | Date separation from semantic hash (`DEC-38`) | [`artifacts.artifact_hash`](file:///c:/Users/veggi/OneDrive/Documents/Codex/Jobbs%C3%B8k_26/P0.9/Build/runtime/jobbsok/artifacts.py#L112) excludes `finalization` when computing `final_package` hash. Assigning `document_date` via `finalize` preserves `review.json` validity while properly updating `render_report.json`. | Eliminates redundant re-reviews on date assignment. | **KEEP** | **INFO** | **HIGH** | Retain as designed. | N/A |

---

## 2. Novel Pre-Smoke Blockers

1. **RT-01 (Child Branch Staleness Cascade):**
   - *Why it blocks:* Branching is the sole normative mechanism to update inputs or retry jobs. In the current implementation, every child run immediately marks all inherited artifacts as `STALE`, forcing full regeneration from Stage 1 even when all governing inputs are identical.

2. **RT-02 (Stale Render Report Concealment):**
   - *Why it blocks:* If `final_package.json` is modified after an initial render, `jobbsok status` and `views/queue.md` still report `render_state: OK` and reference the old output deliverables, leading operators to submit outdated CV/letter documents.

---

## 3. Positive Deviations Not to Fix

1. **RT-09 (Zero Inbox Dependency Post-Freeze):** Tooling strictly severs ties with `inbox/` after freeze; all operations bind to frozen copies.
2. **RT-10 (Clean Hash Decoupling for Date Finalization):** `artifact_hash` strips `finalization` before hashing, allowing `jobbsok finalize` to assign document dates without invalidating `review.json`.
3. **Graceful PDF Degradation (`DEC-41`):** Word COM failures or missing converters record `DEGRADED` in `render_state` and output actionable manual instructions without failing the overall command or corrupting the semantic status.

---

## 4. Highest-Value Missing Adversarial Tests

1. **Metamorphic Branch-Status Roundtrip (`test_adversarial_branch_status_reused`):**
   - Stage a complete run (Stages 1–3 + review).
   - Execute `jobbsok branch` without changing governing inputs.
   - Assert `status.derive(child_run)` returns `production_state == "VALID"`, `highest_valid_stage == "FINAL"`, and `stale_scope == []`.
2. **Deliverable Divergence on Human DOCX Edit (`test_adversarial_render_refused_foreign_pdf_isolation`):**
   - Render a job. Manually modify `out/CV_...docx`.
   - Re-run `render_job`.
   - Assert that `out/CV_...docx` is preserved AND that `out/CV_...pdf` is NOT overwritten with non-matching pipeline text.
3. **Corrupted / Truncated JSON Robustness (`test_adversarial_malformed_artifact_json`):**
   - Write `{ invalid_json: ` to `current/strategy.json`.
   - Assert `jobbsok status` and `jobbsok validate` return exit code 1 with clean `CTR-02` diagnostics rather than unhandled Python exceptions.
4. **Render Axis Invalidation on Semantic Update (`test_adversarial_render_staleness`):**
   - Render a job to completion (`render_state: OK`).
   - Resubmit a modified `final_package.json`.
   - Assert `status.derive()` sets `render_state.overall == "STALE"` (or `"NOT_RENDERED"`) and does not report outdated deliverables as current.

---

## 5. Strongly Supported Architecture-Change Candidates

1. **Topological Hash Propagation in Branching (`DEC-40` Refinement):**
   - Specify that child-local rebind must re-link the internal chain (`strategy_sha256` in draft, `draft_sha256` in final, `final_package_sha256` in review) in topological order during the rebind transaction so that inherited valid artifacts remain valid in the child.
2. **Coupled Promotion for Multi-Format Render Deliverables (`DEC-41` Refinement):**
   - Specify that deliverable promotion is atomic per document component: if DOCX promotion is refused due to human edits (`REFUSED_FOREIGN`), automated PDF promotion for that component must be blocked to prevent split-brain deliverables.