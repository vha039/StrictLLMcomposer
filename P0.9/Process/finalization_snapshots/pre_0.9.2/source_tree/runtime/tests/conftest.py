"""Shared fixtures for the Tier-1 suite.

Every test works against a real build root copied into a temporary
directory: real authorities, real CV baseline, real masters, real policy.
Contract 17 requires tests to create and inspect actual outputs, so nothing
here is mocked.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest

RUNTIME = Path(__file__).resolve().parents[1]
BUILD_ROOT = RUNTIME.parent
sys.path.insert(0, str(RUNTIME))

from jobbsok.atomicio import read_json  # noqa: E402
from jobbsok.manifest import freeze, load_manifest  # noqa: E402
from jobbsok.paths import Layout  # noqa: E402

#: Everything a run binds to, copied so a test can mutate it freely.
COPIED_TREES = ("authorities", "context", "policy", "templates", "schemas")

FIXED_MOMENT = datetime(2026, 8, 23, 6, 0, 0, tzinfo=timezone.utc)

VACANCY = """# Rådgiver økonomi og analyse — Testetaten HF

Testetaten HF søker en rådgiver til Økonomiavdelingen som kan styrke
beslutningsgrunnlaget for økonomi, aktivitet og bemanning.

## Arbeidsoppgaver

- Utvikle og forvalte rapporter og analyser for økonomi og aktivitet.
- Kvalitetssikre datagrunnlag, avstemminger og definisjoner.
- Bidra i budsjett- og prognosearbeid.

## Kvalifikasjonskrav

- Høyere utdanning innen økonomi, statistikk eller tilsvarende.
- Erfaring med rapportering og analyse i en større virksomhet.
- Gode ferdigheter i SQL og Power BI eller tilsvarende verktøy.
- God skriftlig og muntlig framstillingsevne på norsk.

Søknadsfrist: 15.09.2026. Referanse: 2026/1234.
"""

BATCH_HEADER = (
    "job_id,employer,title,job_class,cluster,sequence,priority,source,"
    "unit,reference,deadline,exception_note\n"
)
BATCH_ROW = (
    "testetaten_radgiver,Testetaten HF,Rådgiver økonomi og analyse,CORE,c1,1,"
    "HIGH,vacancies/testetaten_radgiver.md,Økonomiavdelingen,2026/1234,"
    "2026-09-15,\n"
)


def make_build_root(tmp_path: Path) -> Layout:
    """A complete, isolated build root with the real assets."""
    root = tmp_path / "build"
    root.mkdir()
    shutil.copy2(BUILD_ROOT / "pyproject.toml", root / "pyproject.toml")
    for tree in COPIED_TREES:
        shutil.copytree(BUILD_ROOT / tree, root / tree)
    for empty in ("generated", "runs", "inbox/vacancies", "pilot", "evidence"):
        (root / empty).mkdir(parents=True, exist_ok=True)
    (root / "inbox" / "vacancies" / "testetaten_radgiver.md").write_text(
        VACANCY, encoding="utf-8", newline="\n"
    )
    (root / "inbox" / "batch_input.csv").write_text(
        BATCH_HEADER + BATCH_ROW, encoding="utf-8", newline="\n"
    )
    return Layout(root)


@pytest.fixture
def layout(tmp_path: Path) -> Layout:
    return make_build_root(tmp_path)


@pytest.fixture
def frozen(layout: Layout):
    """A frozen run with one synthetic CORE job."""
    result = freeze(
        layout, layout.inbox / "batch_input.csv",
        reviewed_by="Test Reviewer", moment=FIXED_MOMENT,
    )
    assert result.ok, result.result.render()
    return layout, result.run_id, load_manifest(layout, result.run_id)


def make_fixtures(layout: Layout, run_id: str) -> Path:
    """Generate the artifact fixtures for a run, returning their directory."""
    out = layout.root / "fixtures"
    sys.path.insert(0, str(RUNTIME))
    from tools.make_fixtures import build

    build(layout, run_id, out)
    return out


@pytest.fixture
def fixtures(frozen):
    layout, run_id, manifest = frozen
    return layout, run_id, manifest, make_fixtures(layout, run_id)


@pytest.fixture
def staged(fixtures):
    """A run with strategy, draft, final and review all submitted."""
    from jobbsok import artifacts as artifacts_module

    layout, run_id, manifest, fixture_dir = fixtures
    job_id = manifest["jobs"][0]["job_id"]
    for stage, artifact, filename in (
        (1, "strategy", "strategy.valid.json"),
        (2, "draft_package", "draft_package.json"),
        (3, "final_package", "final_package.json"),
        (3, "review", "review.json"),
    ):
        payload = read_json(fixture_dir / filename)
        result = artifacts_module.submit(
            layout, run_id, job_id, stage=stage, artifact=artifact,
            payload=payload, timestamp="20260823T060000Z",
        )
        assert result.ok, result.result.render()
    return layout, run_id, manifest, job_id, fixture_dir


def run_cli(layout: Layout, *args: str) -> subprocess.CompletedProcess:
    """Invoke the CLI in-process semantics via a subprocess, for exit codes."""
    command = [
        sys.executable, "-c",
        "import sys; sys.path.insert(0, r'%s'); "
        "from jobbsok.cli import main; sys.exit(main())" % str(RUNTIME),
        "--root", str(layout.root), *args,
    ]
    return subprocess.run(
        command, capture_output=True, text=True, encoding="utf-8",
        env={"PYTHONIOENCODING": "utf-8", "PATH": ""} | _inherit_env(),
    )


def _inherit_env() -> dict[str, str]:
    import os

    keys = ("PATH", "SYSTEMROOT", "TEMP", "TMP", "USERPROFILE", "APPDATA",
            "LOCALAPPDATA", "PATHEXT", "COMSPEC", "WINDIR")
    return {k: os.environ[k] for k in keys if k in os.environ}


def word_available() -> bool:
    """Whether the Word COM converter can run on this machine (GATE-03)."""
    import shutil as _shutil

    if _shutil.which("powershell") is None:
        return False
    probe = subprocess.run(
        ["powershell", "-NoProfile", "-NonInteractive", "-Command",
         "$word=$null; try { $word=New-Object -ComObject Word.Application; "
         "$word.DisplayAlerts=0; exit 0 } catch { exit 1 } finally { "
         "if ($word -ne $null) { try { $word.Quit() } catch {} } }"],
        capture_output=True, timeout=60,
    )
    return probe.returncode == 0


requires_word = pytest.mark.skipif(
    not word_available(),
    reason="Word COM is unavailable; GATE-03 fallback is DEGRADED render state.",
)
