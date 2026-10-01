import subprocess
import sys
from pathlib import Path

from jobbsok import evidence_index
from jobbsok.atomicio import read_json
from jobbsok.hashing import sha256_file
from jobbsok.manifest import frozen_path, read_frozen

SCRIPT = Path(__file__).resolve().parents[1] / "tools/fetch.py"


def _run(layout, *args):
    return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=layout.root,
                          capture_output=True, text=True, encoding="utf-8")


def test_context_fetch_verbatim_order_boundaries_and_no_write(frozen):
    layout, run_id, manifest = frozen
    index = read_json(frozen_path(layout, run_id, read_frozen(layout, manifest, "evidence_index")))
    first = evidence_index.resolve_section(index, "WORK", "4.1")
    second = evidence_index.resolve_section(index, "EDU", "0.1")
    assert first and second
    before = {str(p): sha256_file(p) for base in (layout.runs, layout.generated)
              for p in base.rglob("*") if p.is_file()}
    result = _run(layout, "--run", run_id, "--ids",
                  f"{first['evidence_id']},{second['evidence_id']}", "--with-context")
    assert result.returncode == 0, result.stderr
    assert result.stdout.index(first["evidence_id"]) < result.stdout.index(second["evidence_id"])
    work_text = (layout.run_dir(run_id) / "frozen/authorities/Work_experience.md").read_text(encoding="utf-8")
    assert evidence_index.slice_entry(work_text, first).strip() in result.stdout
    assert "matching digest row" in result.stdout
    assert "NAVIGATION: local boundary" in result.stdout
    assert "GLOBAL BOUNDARY VERBATIM" in result.stdout
    assert before == {str(p): sha256_file(p) for base in (layout.runs, layout.generated)
                      for p in base.rglob("*") if p.is_file()}


def test_context_fetch_unknown_id_has_no_partial_output(frozen):
    layout, run_id, manifest = frozen
    index = read_json(frozen_path(layout, run_id, read_frozen(layout, manifest, "evidence_index")))
    valid = index["entries"][0]["evidence_id"]
    result = _run(layout, "--run", run_id, "--ids", f"{valid},EV:WORK#missing", "--with-context")
    assert result.returncode != 0
    assert result.stdout == ""
    assert "does not resolve" in result.stderr
    search = _run(layout, "--run", run_id, "--search", "budsjett", "--with-context")
    assert search.returncode != 0
