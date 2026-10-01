from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from tests.support import (
    FINALIZE,
    INGEST,
    ROOT,
    example_package,
    identity_for_package,
    locate_soffice,
    make_package,
    make_project_root,
    make_text_pdf,
    write_json,
    write_stage4_fixture,
)


VACANCY_TEXT = (
    "Eksempelvirksomheten søker en rådgiver som kan forbedre prosesser og "
    "styringsinformasjon. Rollen krever høyere utdanning, strukturert "
    "behovsavklaring, analyse, kvalitetssikring, samarbeid og trygg "
    "overlevering til ordinær drift. Kandidaten skal arbeide tett med ledere "
    "og fagmiljøer og gjøre komplekse datagrunnlag forståelige. "
)


def stage_done(stage: int, artifact: str, job_id: str) -> str:
    model = "GPT-5.6 Terra" if stage in (1, 3) else "GPT-5.6 Sol"
    effort = "max" if stage in (1, 2) else "xhigh"
    return (
        f"Stage: {stage}\n"
        "Status: COMPLETED\n"
        f"Artifact: {artifact}\n"
        f"Job: {job_id}\n"
        f"Model: {model}\n"
        f"Effort: {effort}\n"
    )


def prepare_controlled_fixture(project: Path) -> tuple[list[dict], Path, Path]:
    """Build a controlled file fixture; it does not claim model chats ran."""

    cluster = "B99_C01_process_digitalization"
    packages = [
        example_package(),
        make_package(
            "B99_J002_virksomhetsstyring",
            letter_required=False,
            sparse=True,
        ),
    ]
    packages[1]["job"]["mini_cluster_id"] = "B99_C01B_process_digitalization"
    packages[0]["cv_overrides"]["experience_overrides"].append(
        {
            "employment_id": "EMP_TKS_HEIS",
            "bullets": [
                "Bidro i praktisk monteringsarbeid og leveranseoppgaver med vekt på sikker utførelse og koordinering."
            ],
        }
    )
    jobs = [item["job"]["job_id"] for item in packages]

    stage1_input = project / "stg1_analyze" / "input" / cluster
    make_text_pdf(
        stage1_input / jobs[0] / "vacancy.pdf",
        [VACANCY_TEXT * 2, VACANCY_TEXT * 2],
    )
    second = stage1_input / jobs[1]
    second.mkdir(parents=True)
    (second / "vacancy.md").write_text(
        "# Vacancy\n\n" + VACANCY_TEXT * 2,
        encoding="utf-8",
    )
    exit_code, _ = INGEST.run(project / "stg1_analyze" / "input")
    if exit_code != 0:
        raise AssertionError("Synthetic ingest failed.")

    fixtures = ROOT / "tests" / "fixtures" / "stage_artifacts"
    stage1_output = project / "stg1_analyze" / "output" / cluster
    for package in packages:
        job = package["job"]["job_id"]
        destination = stage1_output / job
        destination.mkdir(parents=True)
        shutil.copy2(stage1_input / job / "vacancy.md", destination / "vacancy.md")
        write_json(destination / "job_identity.json", identity_for_package(package))
        shutil.copy2(fixtures / "vacancy_analysis.md", destination / "vacancy_analysis.md")
        (destination / "_DONE.md").write_text(
            stage_done(1, "vacancy_analysis.md; job_identity.json", job),
            encoding="utf-8",
        )

    stage2_output = project / "stg2_strategy" / "output" / cluster
    stage2_output.mkdir(parents=True)
    shutil.copy2(
        fixtures / "CLUSTER_EVIDENCE_BASE.md",
        stage2_output / "CLUSTER_EVIDENCE_BASE.md",
    )
    split = {"macro_cluster_id": cluster, "A": [jobs[0]], "B": [jobs[1]]}
    write_json(stage2_output / "MINICLUSTER_SPLIT.json", split)
    (stage2_output / "BATCH_STATUS.md").write_text(
        "# B99_C01_process_digitalization — Stage 2\n\n"
        "Model: GPT-5.6 Sol\nEffort: max\nTarget jobs: 2\n\n"
        "## Wave 1\n\n### Completed\n- all fixture jobs\n\n"
        "### Current\n- none\n\n### Remaining\n- none\n\n"
        "### Blocked\n- none\n\n## Midpoint review\n\n"
        "- evidence pairs already used: E01/E02\n"
        "- candidate identities already used: fixture\n"
        "- repeated opening risks: none\n"
        "- jobs requiring escalation: none\n\n"
        "## Wave 2\n\n### Completed\n- none\n\n"
        "### Current\n- none\n\n### Remaining\n- none\n\n"
        "### Blocked\n- none\n",
        encoding="utf-8",
    )
    for package in packages:
        job = package["job"]["job_id"]
        destination = stage2_output / job
        shutil.copytree(stage1_output / job, destination)
        shutil.copy2(fixtures / "package_blueprint.md", destination)
        (destination / "_DONE.md").write_text(
            stage_done(2, "package_blueprint.md; job_identity.json", job),
            encoding="utf-8",
        )

    # The fixture transfer mirrors the verified advance contract. It exists so
    # document finalization remains testable on systems without PowerShell.
    for suffix, package in (("A", packages[0]), ("B", packages[1])):
        mini = package["job"]["mini_cluster_id"]
        job = package["job"]["job_id"]
        stage3_input = project / "stg3_write" / "input" / mini
        stage3_input.mkdir(parents=True)
        shutil.copy2(stage2_output / "CLUSTER_EVIDENCE_BASE.md", stage3_input)
        shutil.copytree(stage2_output / job, stage3_input / job)
        for marker in ("_DONE.md", "BLOCKED.md", "BATCH_STATUS.md"):
            (stage3_input / job / marker).unlink(missing_ok=True)

        stage3_output = project / "stg3_write" / "output" / mini
        shutil.copytree(stage3_input, stage3_output)
        draft = deepcopy(package)
        draft["source_stage"] = "STAGE3_DRAFT"
        write_json(stage3_output / job / "draft_package.json", draft)
        (stage3_output / job / "_DONE.md").write_text(
            stage_done(3, "draft_package.json; job_identity.json", job),
            encoding="utf-8",
        )

        stage4_input = project / "stg4_mirror" / "input" / mini
        shutil.copytree(stage3_output, stage4_input)

    stage4_input_root = project / "stg4_mirror" / "input"
    stage4_output_root = project / "stg4_mirror" / "output"
    for package in packages:
        write_stage4_fixture(stage4_input_root, stage4_output_root, package)
    return packages, stage4_input_root, stage4_output_root


@unittest.skipUnless(locate_soffice(), "LibreOffice/soffice runtime not installed")
class EndToEndTests(unittest.TestCase):
    def test_controlled_e2e_fixture_reaches_check_only_docx_and_pdf(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = make_project_root(Path(temporary) / "project")
            packages, input_root, source_root = prepare_controlled_fixture(project)

            check = FINALIZE.finalize(
                input_root=input_root,
                source_root=source_root,
                output_root=project / "output",
                project_root=project,
                check_only=True,
                force=False,
                soffice_path=None,
            )
            self.assertEqual(check, 0)

            rendered = FINALIZE.finalize(
                input_root=input_root,
                source_root=source_root,
                output_root=project / "output",
                project_root=project,
                check_only=False,
                force=False,
                soffice_path=locate_soffice(),
            )
            self.assertEqual(rendered, 0)
            for package in packages:
                job_output = project / "output" / package["job"]["job_id"]
                self.assertEqual(len(list(job_output.glob("CV_*.docx"))), 1)
                self.assertEqual(len(list(job_output.glob("CV_*.pdf"))), 1)
                if package["job"]["letter_required"]:
                    self.assertEqual(len(list(job_output.glob("Application_*.docx"))), 1)
                    self.assertEqual(len(list(job_output.glob("Application_*.pdf"))), 1)
                else:
                    self.assertFalse(list(job_output.glob("Application_*")))


if __name__ == "__main__":
    unittest.main()
