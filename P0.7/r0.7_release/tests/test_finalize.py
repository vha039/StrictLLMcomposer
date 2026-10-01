from __future__ import annotations

from copy import deepcopy
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from tests.support import (
    FINALIZE,
    ROOT,
    example_package,
    identity_for_package,
    locate_soffice,
    make_package,
    make_project_root,
    make_text_pdf,
    write_stage4_fixture,
)


class FinalizeValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.baseline = FINALIZE.read_marked_json(
            ROOT / "context" / "CV_BASELINE.md",
            FINALIZE.BASELINE_START,
            FINALIZE.BASELINE_END,
        )
        cls.schema = FINALIZE.read_marked_json(
            ROOT / "context" / "PACKAGE_CONTRACT.md",
            FINALIZE.SCHEMA_START,
            FINALIZE.SCHEMA_END,
        )

    def validate(self, package, *, draft=None, identity=None) -> None:
        if draft is None:
            draft = deepcopy(package)
            draft["source_stage"] = "STAGE3_DRAFT"
        FINALIZE.validate_package(
            package,
            schema=self.schema,
            baseline=self.baseline,
            job_id=package["job"]["job_id"],
            identity=(
                identity if identity is not None else identity_for_package(package)
            ),
            mini_cluster_id=package["job"]["mini_cluster_id"],
            draft=draft,
        )

    def test_valid_letter_and_no_letter_packages(self) -> None:
        self.validate(example_package())
        self.validate(
            make_package(
                "B99_J002_virksomhetsstyring",
                letter_required=False,
                sparse=True,
            )
        )

    def test_rejects_contract_identity_and_cross_stage_failures(self) -> None:
        mutations = []

        package = example_package()
        package["unknown"] = True
        mutations.append((package, None))

        package = example_package()
        del package["job"]["batch_id"]
        mutations.append((package, identity_for_package(example_package())))

        package = example_package()
        package["source_stage"] = "STAGE3_DRAFT"
        mutations.append((package, None))

        package = example_package()
        package["cv_overrides"]["baseline_version"] = "0.6.0"
        mutations.append((package, None))

        package = example_package()
        package["job"]["letter_required"] = False
        mutations.append((package, None))

        package = example_package()
        package["cv_overrides"]["experience_overrides"][0]["employment_id"] = "EMP_UNKNOWN"
        mutations.append((package, None))

        package = example_package()
        identity = identity_for_package(package)
        identity["employer"] = "Feil arbeidsgiver"
        mutations.append((package, identity))

        for index, (mutant, identity) in enumerate(mutations):
            with self.subTest(index=index):
                with self.assertRaises(FINALIZE.JobValidationError):
                    self.validate(mutant, identity=identity)

    def test_rejects_limits_placeholders_and_internal_metadata(self) -> None:
        package = example_package()
        package["portal_answers"][0]["max_words"] = 1
        with self.assertRaises(FINALIZE.JobValidationError):
            self.validate(package)

        package = example_package()
        package["portal_answers"][0]["max_chars"] = 10
        with self.assertRaises(FINALIZE.JobValidationError):
            self.validate(package)

        package = example_package()
        package["application"]["opening"] += " TODO"
        with self.assertRaises(FINALIZE.JobValidationError):
            self.validate(package)

        package = example_package()
        package["application"]["opening"] += " CLM-SECRET-001"
        with self.assertRaises(FINALIZE.JobValidationError):
            self.validate(package)

        package = example_package()
        package["application"]["opening"] += " single backbone"
        with self.assertRaises(FINALIZE.JobValidationError):
            self.validate(package)

    def test_stage4_cannot_introduce_new_employment_id(self) -> None:
        final = example_package()
        draft = deepcopy(final)
        draft["source_stage"] = "STAGE3_DRAFT"
        draft["cv_overrides"]["experience_overrides"] = draft["cv_overrides"][
            "experience_overrides"
        ][:1]
        with self.assertRaises(FINALIZE.JobValidationError):
            self.validate(final, draft=draft)

    def test_check_only_requires_expected_completed_identity_done_and_flags(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = make_project_root(Path(temporary) / "project")
            expected = project / "stg4_mirror" / "input"
            source = project / "stg4_mirror" / "output"
            write_stage4_fixture(expected, source, example_package())
            write_stage4_fixture(
                expected,
                source,
                make_package(
                    "B99_J002_virksomhetsstyring",
                    letter_required=False,
                    sparse=True,
                ),
                flag_count=0,
            )
            output_root = project / "rendered"
            result = FINALIZE.finalize(
                input_root=expected,
                source_root=source,
                output_root=output_root,
                project_root=project,
                check_only=True,
                force=False,
                soffice_path=None,
            )
            self.assertEqual(result, 0)
            self.assertFalse(output_root.exists())

    def test_missing_completion_never_returns_global_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = make_project_root(Path(temporary) / "project")
            expected = project / "stg4_mirror" / "input"
            source = project / "stg4_mirror" / "output"
            write_stage4_fixture(expected, source, example_package(), final_package=False)
            capture = io.StringIO()
            with patch("sys.stdout", capture):
                result = FINALIZE.finalize(
                    input_root=expected,
                    source_root=source,
                    output_root=project / "rendered",
                    project_root=project,
                    check_only=True,
                    force=False,
                    soffice_path=None,
                )
            self.assertEqual(result, 1)
            stdout = capture.getvalue()
            self.assertIn("Expected jobs: 1", stdout)
            self.assertIn("Completed packages: 0", stdout)
            self.assertIn("Missing: 1", stdout)
            self.assertIn("Result: PARTIAL_FAILURE", stdout)
            self.assertNotIn("Result: PASS", stdout)

    def test_expected_job_folder_without_identity_cannot_be_silently_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = make_project_root(Path(temporary) / "project")
            expected = project / "stg4_mirror" / "input"
            source = project / "stg4_mirror" / "output"
            write_stage4_fixture(expected, source, example_package())
            missing_anchor = (
                expected
                / "B99_C01A_process_digitalization"
                / "B99_J002_unanchored"
            )
            missing_anchor.mkdir(parents=True)
            with self.assertRaises(FINALIZE.CommonConfigurationError):
                FINALIZE.finalize(
                    input_root=expected,
                    source_root=source,
                    output_root=project / "rendered",
                    project_root=project,
                    check_only=True,
                    force=False,
                    soffice_path=None,
                )

    def test_stage4_blockers_done_identity_and_review_heading_are_job_failures(self) -> None:
        cases = (
            {"done": False},
            {"input_blocked": True},
            {"output_blocked": True},
            {
                "output_identity": {
                    **identity_for_package(example_package()),
                    "title": "Feil tittel",
                }
            },
        )
        for kwargs in cases:
            with self.subTest(kwargs=kwargs), tempfile.TemporaryDirectory() as temporary:
                project = make_project_root(Path(temporary) / "project")
                expected = project / "stg4_mirror" / "input"
                source = project / "stg4_mirror" / "output"
                write_stage4_fixture(expected, source, example_package(), **kwargs)
                result = FINALIZE.finalize(
                    input_root=expected,
                    source_root=source,
                    output_root=project / "rendered",
                    project_root=project,
                    check_only=True,
                    force=False,
                    soffice_path=None,
                )
                self.assertEqual(result, 1)

        with tempfile.TemporaryDirectory() as temporary:
            project = make_project_root(Path(temporary) / "project")
            expected = project / "stg4_mirror" / "input"
            source = project / "stg4_mirror" / "output"
            _, job_dir = write_stage4_fixture(expected, source, example_package())
            (job_dir / "review_flags.md").write_text("# Must verify\n", encoding="utf-8")
            self.assertEqual(
                FINALIZE.finalize(
                    input_root=expected,
                    source_root=source,
                    output_root=project / "rendered",
                    project_root=project,
                    check_only=True,
                    force=False,
                    soffice_path=None,
                ),
                1,
            )

    def test_converter_timeout_and_pdf_page_limits_are_explicit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            docx_path = directory / "test.docx"
            docx_path.write_bytes(b"not used because converter is mocked")
            with patch.object(
                FINALIZE.subprocess,
                "run",
                side_effect=subprocess.TimeoutExpired(["soffice"], 1),
            ):
                with self.assertRaisesRegex(FINALIZE.JobValidationError, "timed out"):
                    FINALIZE.convert_to_pdf(docx_path, sys.executable, timeout_seconds=1)

            three_pages = directory / "three_pages.pdf"
            make_text_pdf(three_pages, ["Dette er selekterbar tekst. " * 8] * 3)
            with self.assertRaisesRegex(FINALIZE.JobValidationError, "page limit"):
                FINALIZE.validate_pdf(three_pages, maximum_pages=2)
            with self.assertRaisesRegex(FINALIZE.JobValidationError, "page limit"):
                FINALIZE.validate_pdf(three_pages, maximum_pages=1)

    def test_cli_configuration_error_exits_two(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = make_project_root(Path(temporary) / "project")
            expected = project / "stg4_mirror" / "input"
            source = project / "stg4_mirror" / "output"
            write_stage4_fixture(expected, source, example_package())
            baseline_path = project / "context" / "CV_BASELINE.md"
            baseline_path.write_text(
                baseline_path.read_text(encoding="utf-8").replace(
                    '"baseline_version": "0.7.0"',
                    '"baseline_version": "BROKEN"',
                    1,
                ),
                encoding="utf-8",
            )
            completed = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts" / "finalize.py"),
                    str(expected),
                    str(source),
                    str(project / "rendered"),
                    "--root",
                    str(project),
                    "--check-only",
                ],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 2)
            self.assertIn("FINALIZE CONFIGURATION ERROR", completed.stdout)


@unittest.skipUnless(locate_soffice(), "LibreOffice/soffice runtime not installed")
class FinalizeRenderingTests(unittest.TestCase):
    def test_dense_sparse_letter_no_letter_older_override_unit_reference_and_force(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = make_project_root(Path(temporary) / "project")
            expected = project / "stg4_mirror" / "input"
            source = project / "stg4_mirror" / "output"
            dense = example_package()
            dense["cv_overrides"]["experience_overrides"].append(
                {
                    "employment_id": "EMP_TKS_HEIS",
                    "bullets": [
                        "Bidro i praktisk monteringsarbeid og leveranseoppgaver med vekt på sikker utførelse og koordinering."
                    ],
                }
            )
            sparse = make_package(
                "B99_J002_virksomhetsstyring",
                letter_required=False,
                sparse=True,
            )
            write_stage4_fixture(expected, source, dense)
            write_stage4_fixture(expected, source, sparse, flag_count=0)

            result = FINALIZE.finalize(
                input_root=expected,
                source_root=source,
                output_root=project / "rendered",
                project_root=project,
                check_only=False,
                force=False,
                soffice_path=locate_soffice(),
            )
            self.assertEqual(result, 0)
            dense_output = project / "rendered" / dense["job"]["job_id"]
            sparse_output = project / "rendered" / sparse["job"]["job_id"]
            dense_cv = next(dense_output.glob("CV_*.docx"))
            dense_cv_pdf = next(dense_output.glob("CV_*.pdf"))
            dense_application = next(dense_output.glob("Application_*.docx"))
            dense_application_pdf = next(dense_output.glob("Application_*.pdf"))
            sparse_cv = next(sparse_output.glob("CV_*.docx"))
            sparse_cv_pdf = next(sparse_output.glob("CV_*.pdf"))
            self.assertEqual(FINALIZE.validate_pdf(dense_cv_pdf, maximum_pages=2), 2)
            self.assertEqual(FINALIZE.validate_pdf(sparse_cv_pdf, maximum_pages=2), 2)
            self.assertEqual(FINALIZE.validate_pdf(dense_application_pdf, maximum_pages=1), 1)
            self.assertFalse(list(sparse_output.glob("Application_*")))
            self.assertTrue((dense_output / "Portal_answers.md").is_file())
            self.assertFalse((sparse_output / "Portal_answers.md").exists())
            self.assertTrue((dense_output / "_private" / "review_flags.md").is_file())

            dense_text = FINALIZE.visible_docx_text(dense_cv)
            app_text = FINALIZE.visible_docx_text(dense_application)
            self.assertIn(
                "Bidro i praktisk monteringsarbeid og leveranseoppgaver",
                dense_text,
            )
            self.assertIn("Eksempelavdeling", app_text)
            self.assertIn("Referanse: 12345", app_text)
            for employer_file in (
                dense_cv,
                dense_application,
                sparse_cv,
                dense_cv_pdf,
                dense_application_pdf,
                sparse_cv_pdf,
            ):
                if employer_file.suffix == ".docx":
                    text = FINALIZE.visible_docx_text(employer_file)
                else:
                    with FINALIZE.pymupdf.open(employer_file) as document:
                        text = "\n".join(page.get_text() for page in document)
                self.assertNotRegex(text, r"CLM-|review flag|package_blueprint|\\{\\{")

            no_force = FINALIZE.finalize(
                input_root=expected,
                source_root=source,
                output_root=project / "rendered",
                project_root=project,
                check_only=False,
                force=False,
                soffice_path=locate_soffice(),
            )
            self.assertEqual(no_force, 1)
            with_force = FINALIZE.finalize(
                input_root=expected,
                source_root=source,
                output_root=project / "rendered",
                project_root=project,
                check_only=False,
                force=True,
                soffice_path=locate_soffice(),
            )
            self.assertEqual(with_force, 0)
            self.assertFalse((project / "rendered" / "FINALIZE_REPORT.md").exists())
            self.assertFalse((project / "rendered" / "INDEX.md").exists())


if __name__ == "__main__":
    unittest.main()
