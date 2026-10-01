from __future__ import annotations

import json
from pathlib import Path
import re
import unittest

from tests.support import FINALIZE, ROOT


FIXTURES = ROOT / "tests" / "fixtures" / "stage_artifacts"


class StageArtifactTests(unittest.TestCase):
    def test_representative_stage_artifacts_have_p07_required_sections(self) -> None:
        requirements = {
            "vacancy_analysis.md": [
                "Job identity and channel",
                "Explicit vacancy facts",
                "Formal must-have requirements",
                "Preferred requirements",
                "Core responsibilities",
                "Dominant employer problem",
                "Ranked decision tests",
                "Expected seniority and collaboration signals",
                "Selection regime",
                "Channel requirements and limits",
                "Ambiguities resolved",
                "What Stage 2 must solve",
            ],
            "CLUSTER_EVIDENCE_BASE.md": [
                "Cluster definition",
                "Cluster cohesion check",
                "Shared employer problems",
                "Shared candidate routes",
                "Shared evidence atoms",
                "Evidence lane A",
                "Evidence lane B",
                "Lane-specific employer problems",
                "Lane-specific candidate routes",
                "Lane-specific evidence priorities",
                "Lane-specific writing risks",
                "Cluster-specific genericity risks",
                "Complete cluster-job matrix",
                "Recommended minicluster split",
                "Downstream model recommendations",
            ],
            "package_blueprint.md": [
                "Primary candidate identity",
                "Employer problem",
                "Shortlist thesis",
                "Main evidence 1",
                "Main evidence 2",
                "Strongest alternative route and why it loses",
                "Objection reframes",
                "CV override plan",
                "Application plan",
                "Portal plan",
                "Do not undersell",
                "Borderline claims for private review",
                "Stage 3 complexity note",
            ],
        }
        for filename, headings in requirements.items():
            text = (FIXTURES / filename).read_text(encoding="utf-8")
            for heading in headings:
                with self.subTest(filename=filename, heading=heading):
                    self.assertRegex(text, rf"(?mi)^#+\s+.*{re.escape(heading)}")

    def test_job_identity_fixture_is_complete_and_path_independent(self) -> None:
        identity_path = FIXTURES / "job_identity.json"
        identity = json.loads(identity_path.read_text(encoding="utf-8"))
        FINALIZE.validate_job_identity(
            identity,
            path=identity_path,
            expected_job_id="B01_J001_raadgiver",
            expected_mini_cluster_id="B01_C01A_process",
        )

    def test_split_is_complete_disjoint_and_valid(self) -> None:
        split = json.loads(
            (FIXTURES / "MINICLUSTER_SPLIT.json").read_text(encoding="utf-8")
        )
        self.assertRegex(
            split["macro_cluster_id"], r"^B[0-9]{2}_C[0-9]{2}_[a-z0-9_]+$"
        )
        self.assertTrue(split["A"])
        self.assertTrue(split["B"])
        jobs = split["A"] + split["B"]
        self.assertEqual(len(jobs), len(set(jobs)))
        for job in jobs:
            self.assertRegex(job, r"^B[0-9]{2}_J[0-9]{3}_[a-z0-9_]+$")

    def test_cluster_matrix_references_defined_local_evidence(self) -> None:
        text = (FIXTURES / "CLUSTER_EVIDENCE_BASE.md").read_text(encoding="utf-8")
        defined = set(re.findall(r"(?m)^##\s+(E[0-9]{2})\b", text))
        matrix_rows = [line for line in text.splitlines() if line.startswith("| B")]
        referenced = set(re.findall(r"\bE[0-9]{2}\b", "\n".join(matrix_rows)))
        self.assertTrue(referenced)
        self.assertTrue(referenced.issubset(defined))
        self.assertIn(
            "| Job | Lane | Candidate identity | Employer problem | E1 | E2 | Differentiator | Complexity |",
            text,
        )

    def test_status_done_blocked_and_private_flags_are_explicit(self) -> None:
        status = (FIXTURES / "BATCH_STATUS.md").read_text(encoding="utf-8")
        for heading in ("Wave 1", "Midpoint review", "Wave 2"):
            self.assertRegex(status, rf"(?mi)^##\s+{heading}\s*$")
        for heading in ("Completed", "Current", "Remaining", "Blocked"):
            self.assertGreaterEqual(
                len(re.findall(rf"(?mi)^###\s+{heading}\s*$", status)), 2
            )
        for field in ("Model:", "Effort:", "Target jobs:"):
            self.assertIn(field, status)
        done = (FIXTURES / "_DONE.md").read_text(encoding="utf-8")
        blocked = (FIXTURES / "BLOCKED.md").read_text(encoding="utf-8")
        for field in ("Stage:", "Status:", "Artifact:", "Job:", "Model:", "Effort:"):
            self.assertIn(field, done)
        for field in ("Stage:", "Job:", "Reason:", "Required action:"):
            self.assertIn(field, blocked)

        flags = FIXTURES / "review_flags.md"
        FINALIZE.validate_review_flags(flags)
        self.assertNotRegex(
            flags.read_text(encoding="utf-8"),
            r"(?mi)^#+\s+(?:PASS|REVISE|BLOCK)\b",
        )


if __name__ == "__main__":
    unittest.main()
