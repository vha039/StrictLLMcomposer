from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from tests.support import ROOT


PWSH = shutil.which("pwsh") or shutil.which("powershell")
SCRIPT = ROOT / "scripts" / "advance.ps1"


def make_advance_root(path: Path, *, fault: str | None = None) -> str:
    cluster = "B01_C01_process"
    source = path / "stg2_strategy" / "output" / cluster
    source.mkdir(parents=True)
    (path / "stg3_write" / "input").mkdir(parents=True)
    (source / "CLUSTER_EVIDENCE_BASE.md").write_text(
        "# Cluster evidence base\n\n# Evidence lane A\n\n# Evidence lane B\n",
        encoding="utf-8",
    )
    (source / "BATCH_STATUS.md").write_text(
        "# B01_C01_process — Stage 2\n\n"
        "Model: GPT-5.6 Sol\nEffort: max\nTarget jobs: 10\n\n"
        "## Wave 1\n\n### Completed\n- none\n\n### Current\n- none\n\n"
        "### Remaining\n- all\n\n### Blocked\n- none\n\n"
        "## Midpoint review\n\n- evidence pairs already used: none\n"
        "- candidate identities already used: none\n"
        "- repeated opening risks: none\n"
        "- jobs requiring escalation: none\n\n"
        "## Wave 2\n\n### Completed\n- none\n\n### Current\n- none\n\n"
        "### Remaining\n- none\n\n### Blocked\n- none\n",
        encoding="utf-8",
    )
    jobs = [f"B01_J{index:03d}_rolle" for index in range(1, 11)]
    for job in jobs:
        job_dir = source / job
        job_dir.mkdir()
        identity = {
            "job_id": job,
            "batch_id": "B01",
            "macro_cluster_id": cluster,
            "employer": "Eksempelvirksomheten AS",
            "title": "Rådgiver",
            "unit": None,
            "reference": None,
            "language": "nb-NO",
            "letter_required": True,
        }
        (job_dir / "job_identity.json").write_text(
            json.dumps(identity, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        for filename, content in (
            ("vacancy.md", "# Vacancy\n\nMeningsfull testtekst.\n"),
            ("vacancy_analysis.md", "# Job identity and channel\n"),
            ("package_blueprint.md", "# Primary candidate identity\n"),
        ):
            (job_dir / filename).write_text(content, encoding="utf-8")
        (job_dir / "_DONE.md").write_text(
            f"Stage: 2\nStatus: COMPLETED\nArtifact: package_blueprint.md\n"
            f"Job: {job}\nModel: GPT-5.6 Sol\nEffort: max\n",
            encoding="utf-8",
        )
    split = {
        "macro_cluster_id": cluster,
        "A": jobs[:5],
        "B": jobs[5:],
    }
    if fault == "overlap":
        split["B"][0] = jobs[0]
    elif fault == "missing":
        split["B"].pop()
    elif fault == "unknown":
        split["B"][-1] = "B01_J999_unknown"
    elif fault == "missing_clusterbase":
        (source / "CLUSTER_EVIDENCE_BASE.md").unlink()
    elif fault == "missing_done":
        (source / jobs[0] / "_DONE.md").unlink()
    elif fault == "bad_status":
        (source / "BATCH_STATUS.md").write_text("# incomplete\n", encoding="utf-8")
    elif fault == "blocked":
        (source / jobs[0] / "BLOCKED.md").write_text("# BLOCKED\n", encoding="utf-8")
    elif fault == "identity":
        identity_path = source / jobs[0] / "job_identity.json"
        identity = json.loads(identity_path.read_text(encoding="utf-8"))
        identity["title"] = ""
        identity_path.write_text(json.dumps(identity) + "\n", encoding="utf-8")
    elif fault == "destination":
        (path / "stg3_write" / "input" / "B01_C01A_process").mkdir()
    (source / "MINICLUSTER_SPLIT.json").write_text(
        json.dumps(split, indent=2) + "\n",
        encoding="utf-8",
    )
    return cluster


class AdvanceContractTests(unittest.TestCase):
    def test_script_contains_required_guards_and_no_model_runner(self) -> None:
        text = SCRIPT.read_text(encoding="utf-8")
        required = [
            "MINICLUSTER_SPLIT.json",
            "CLUSTER_EVIDENCE_BASE.md",
            "BATCH_STATUS.md",
            "Assert-Stage2BatchStatus",
            "Midpoint review",
            "job_identity.json",
            "vacancy_analysis.md",
            "package_blueprint.md",
            "Split/filesystem mismatch",
            "Destination exists",
            "Stage 2",
            "Stage:\\s*2",
            "_DONE.md",
            "BLOCKED.md",
            "Result: PASS",
        ]
        for item in required:
            self.assertIn(item, text)
        self.assertNotIn("openai", text.lower())
        self.assertNotIn("codex exec", text.lower())

    @unittest.skipUnless(PWSH, "PowerShell runtime not installed")
    def test_powershell_positive_split_and_copy(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            cluster = make_advance_root(root)
            completed = subprocess.run(
                [
                    PWSH,
                    "-NoProfile",
                    "-File",
                    str(SCRIPT),
                    "-Cluster",
                    cluster,
                    "-Root",
                    str(root),
                ],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            for suffix, expected_jobs in (
                ("A", [f"B01_J{index:03d}_rolle" for index in range(1, 6)]),
                ("B", [f"B01_J{index:03d}_rolle" for index in range(6, 11)]),
            ):
                destination = (
                    root / "stg3_write" / "input" / f"B01_C01{suffix}_process"
                )
                self.assertTrue((destination / "CLUSTER_EVIDENCE_BASE.md").is_file())
                for job in expected_jobs:
                    self.assertTrue((destination / job / "job_identity.json").is_file())
                    self.assertTrue(
                        (destination / job / "package_blueprint.md").is_file()
                    )
                    self.assertFalse((destination / job / "_DONE.md").exists())
                    self.assertFalse((destination / job / "BLOCKED.md").exists())

    @unittest.skipUnless(PWSH, "PowerShell runtime not installed")
    def test_powershell_rejects_incomplete_authoritative_stage2_output(self) -> None:
        for fault in (
            "overlap",
            "missing",
            "unknown",
            "missing_clusterbase",
            "missing_done",
            "bad_status",
            "blocked",
            "identity",
            "destination",
        ):
            with self.subTest(fault=fault), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                cluster = make_advance_root(root, fault=fault)
                completed = subprocess.run(
                    [
                        PWSH,
                        "-NoProfile",
                        "-File",
                        str(SCRIPT),
                        "-Cluster",
                        cluster,
                        "-Root",
                        str(root),
                    ],
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertNotEqual(completed.returncode, 0)


if __name__ == "__main__":
    unittest.main()
