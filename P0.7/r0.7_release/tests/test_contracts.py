from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import unittest

from tests.support import FINALIZE, ROOT, example_package, identity_for_package


class ContractTests(unittest.TestCase):
    def test_candidate_authorities_and_original_masters_are_frozen(self) -> None:
        expected = {
            "Work_experience.md": (
                "0b39a5105f0d809d1bc9a917665bc69c619eb059253a779079b37304b49a2f9d"
            ),
            "Education.md": (
                "75e238890215cbc02c3bc59cdaaeb43f467ae7d512e9b5a9c4723ccc0c4580f8"
            ),
            "Other_high_value_information.md": (
                "58a8f88f9eb627847152d684b19d7938c42da7d173a57a7fff58728a25ae5bf8"
            ),
            "templates/CV_MASTER.docx": (
                "c3809748fe26dd5a7ae0a146d940a15e1b3326036ae5f7fac9fd2be02292e8c5"
            ),
            "templates/APPLICATION_MASTER.docx": (
                "dfd24125f921863da23932b8be3255df51cc8a4ee9a97c6a602a33dedb241409"
            ),
        }
        for relative, digest in expected.items():
            with self.subTest(relative=relative):
                observed = hashlib.sha256(
                    (ROOT / "context" / relative).read_bytes()
                ).hexdigest()
                self.assertEqual(observed, digest)

    def test_only_three_active_scripts_exist_and_no_orchestrator_survives(self) -> None:
        scripts = sorted(
            path.name for path in (ROOT / "scripts").iterdir() if path.is_file()
        )
        self.assertEqual(scripts, ["advance.ps1", "finalize.py", "ingest.py"])
        script_text = "\n".join(
            path.read_text(encoding="utf-8")
            for path in (ROOT / "scripts").iterdir()
            if path.is_file()
        ).lower()
        for forbidden in (
            "from openai",
            "import openai",
            "responses.parse",
            "codex exec",
            "session_id",
            "vector database",
        ):
            self.assertNotIn(forbidden, script_text)

    def test_p07_root_and_four_physical_stage_contracts(self) -> None:
        self.assertIn("P0.7", (ROOT / "AGENTS.md").read_text(encoding="utf-8"))
        routing = (ROOT / "MODEL_ROUTING.md").read_text(encoding="utf-8")
        for term in (
            "GPT-5.6 Terra",
            "GPT-5.6 Sol",
            "Stage 1 — Terra Max to Sol XHigh",
            "Stage 3 — Terra XHigh to Terra Max",
            "Stage 4 — Sol XHigh to Sol Max",
            "Stage 3 Luna Max may be tested after the first macrocluster.",
            "Ultra is deferred from the MVP.",
        ):
            self.assertIn(term, routing)
        self.assertTrue((ROOT / "docs" / "HYBRID_PILOT_LOG.csv").is_file())
        expected = {
            "stg1_analyze": ("Terra", "Max", "10+10"),
            "stg2_strategy": ("Sol", "Max", "10+10"),
            "stg3_write": ("Terra", "Extra High", "5+5"),
            "stg4_mirror": ("Sol", "Extra High", "5+5"),
        }
        found = {
            path.name for path in ROOT.iterdir()
            if path.is_dir() and path.name.startswith("stg")
        }
        self.assertEqual(found, set(expected))
        for stage, terms in expected.items():
            with self.subTest(stage=stage):
                text = (ROOT / stage / "AGENTS.md").read_text(encoding="utf-8")
                for term in (
                    *terms,
                    "Phase A",
                    "Phase B",
                    "_DONE.md",
                    "BLOCKED.md",
                    "Wave 1",
                    "Wave 2",
                    "Midpoint",
                    "BATCH_STATUS.md",
                ):
                    self.assertIn(term, text)

    def test_runtime_core_and_calibration_are_p07_and_bounded(self) -> None:
        core = (ROOT / "context" / "NORWEGIAN_APPLICATION_CORE.md").read_text(
            encoding="utf-8"
        )
        words = len(re.findall(r"\S+", core))
        self.assertGreaterEqual(words, 3000)
        self.assertLessEqual(words, 5500)
        for heading in (
            "Universal doctrine",
            "Stage 1",
            "Stage 2",
            "Stage 3",
            "Stage 4",
            "Channel complementarity",
            "Complete CV doctrine",
            "Factual and lifecycle boundaries",
            "First-20-seconds test",
            "Employer-swap test",
            "Batch variation and anti-homogenization",
        ):
            self.assertRegex(core, rf"(?mi)^#+\s+.*{re.escape(heading)}")
        calibration = (ROOT / "context" / "PERSUASION_CALIBRATION.md").read_text(
            encoding="utf-8"
        )
        for heading in (
            "APPROVED_STRONG",
            "TOO_WEAK",
            "TOO_STRONG",
            "WRONG_ROUTE",
            "WRONG_CONTRIBUTION_LEVEL",
            "WRONG_CHANNEL",
            "UNNATURAL_NORWEGIAN",
            "TOO_TECHNICAL",
            "MISSING_EMPLOYER_VALUE",
            "TEAM_CONTEXT_MISSING",
            "LIFECYCLE_MISREPRESENTATION",
        ):
            self.assertIn(f"# {heading}", calibration)

    def test_baseline_schema_example_and_identity_anchor_parse(self) -> None:
        baseline = FINALIZE.read_marked_json(
            ROOT / "context" / "CV_BASELINE.md",
            FINALIZE.BASELINE_START,
            FINALIZE.BASELINE_END,
        )
        schema = FINALIZE.read_marked_json(
            ROOT / "context" / "PACKAGE_CONTRACT.md",
            FINALIZE.SCHEMA_START,
            FINALIZE.SCHEMA_END,
        )
        FINALIZE.validate_baseline(baseline)
        package = example_package()
        FINALIZE.validate_with_schema(package, schema)
        self.assertEqual(package["contract_version"], "0.7")
        self.assertEqual(package["cv_overrides"]["baseline_version"], "0.7.0")
        identity = identity_for_package(package)
        FINALIZE.validate_job_identity(
            identity,
            path=Path("job_identity.json"),
            expected_job_id=package["job"]["job_id"],
            expected_mini_cluster_id=package["job"]["mini_cluster_id"],
        )
        self.assertEqual(
            set(package["cv_overrides"]),
            {
                "baseline_version",
                "profile",
                "key_competencies",
                "experience_overrides",
            },
        )

    def test_package_schema_rejects_static_or_invalid_identity_fields(self) -> None:
        schema = FINALIZE.read_marked_json(
            ROOT / "context" / "PACKAGE_CONTRACT.md",
            FINALIZE.SCHEMA_START,
            FINALIZE.SCHEMA_END,
        )
        package = example_package()
        package["cv_overrides"]["education"] = []
        with self.assertRaises(ValueError):
            FINALIZE.validate_with_schema(package, schema)

        package = example_package()
        del package["job"]["batch_id"]
        with self.assertRaises(ValueError):
            FINALIZE.validate_with_schema(package, schema)

        package = example_package()
        package["job"]["mini_cluster_id"] += "_" + "x" * 100
        with self.assertRaises(ValueError):
            FINALIZE.validate_with_schema(package, schema)

    def test_templates_match_controls_and_static_baseline(self) -> None:
        templates = ROOT / "context" / "templates"
        FINALIZE.require_template_contract(
            templates / "CV_MASTER.docx", FINALIZE.CV_TAGS
        )
        FINALIZE.require_template_contract(
            templates / "APPLICATION_MASTER.docx", FINALIZE.APPLICATION_TAGS
        )
        baseline = FINALIZE.read_marked_json(
            ROOT / "context" / "CV_BASELINE.md",
            FINALIZE.BASELINE_START,
            FINALIZE.BASELINE_END,
        )
        FINALIZE.validate_template_static_baseline(
            templates / "CV_MASTER.docx", baseline
        )

    def test_start_here_has_all_operator_commands(self) -> None:
        text = (ROOT / "START_HERE.md").read_text(encoding="utf-8")
        for command_or_term in (
            "scripts\\ingest.py",
            "advance.ps1",
            "stg4_mirror\\input stg4_mirror\\output output --check-only",
            "stg4_mirror\\input stg4_mirror\\output output --force",
            "BATCH_STATUS.md",
            "BLOCKED.md",
            "MODEL_ROUTING.md",
            "## Midpoint review",
            "## Wave 2",
        ):
            self.assertIn(command_or_term, text)


if __name__ == "__main__":
    unittest.main()
