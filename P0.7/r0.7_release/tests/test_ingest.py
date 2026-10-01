from __future__ import annotations

import hashlib
from pathlib import Path
import tempfile
import unittest

from tests.support import INGEST, make_text_pdf


LONG_TEXT = (
    "Vi søker en rådgiver som kan forbedre økonomiprosesser, avklare behov "
    "med ledere og fagmiljøer og omsette komplekse datagrunnlag til tydelig "
    "beslutningsstøtte. Rollen krever strukturert gjennomføring, dokumentasjon, "
    "kvalitetssikring, samarbeid og trygg overlevering til ordinær drift. "
)


class IngestTests(unittest.TestCase):
    def test_extracts_selectable_pdf_with_page_markers_hash_and_exit_zero(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "input"
            job = root / "B01_C01_process" / "B01_J001_raadgiver"
            pdf = job / "vacancy.pdf"
            make_text_pdf(pdf, [LONG_TEXT * 2, LONG_TEXT * 2])

            exit_code, counts = INGEST.run(root)

            self.assertEqual(exit_code, 0)
            self.assertEqual(counts, {"reused": 0, "extracted": 1, "blocked": 0})
            rendered = (job / "vacancy.md").read_text(encoding="utf-8")
            self.assertIn("## Page 1", rendered)
            self.assertIn("## Page 2", rendered)
            self.assertIn(hashlib.sha256(pdf.read_bytes()).hexdigest(), rendered)

    def test_reuses_meaningful_markdown_and_requires_force_for_replacement(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "input"
            job = root / "B01_C01_process" / "B01_J001_raadgiver"
            job.mkdir(parents=True)
            vacancy = job / "vacancy.md"
            vacancy.write_text("# Vacancy\n\n" + LONG_TEXT * 2, encoding="utf-8")
            make_text_pdf(job / "vacancy.pdf", [LONG_TEXT * 3])

            self.assertEqual(INGEST.ingest_job(job, force=False), "REUSED")
            self.assertIn("Vi søker", vacancy.read_text(encoding="utf-8"))
            self.assertEqual(INGEST.ingest_job(job, force=True), "EXTRACTED")

    def test_rejects_short_markdown_but_allows_one_weak_pdf_page_when_total_is_readable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "input"
            job = root / "B01_C01_process" / "B01_J001_raadgiver"
            job.mkdir(parents=True)
            (job / "vacancy.md").write_text("# Vacancy\n\nfor kort", encoding="utf-8")
            exit_code, counts = INGEST.run(root)
            self.assertEqual(exit_code, 1)
            self.assertEqual(counts["blocked"], 1)

            (job / "vacancy.md").unlink()
            make_text_pdf(job / "vacancy.pdf", [LONG_TEXT * 2, "kort side"])
            exit_code, counts = INGEST.run(root)
            self.assertEqual(exit_code, 0)
            self.assertEqual(counts["extracted"], 1)
            rendered = (job / "vacancy.md").read_text(encoding="utf-8")
            self.assertIn("Short/weak page(s) retained", rendered)

    def test_rejects_dominated_weak_pdf_and_missing_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            job = Path(temporary) / "B01_J001_raadgiver"
            job.mkdir()
            with self.assertRaises(INGEST.IngestError):
                INGEST.ingest_job(job, force=False)
            make_text_pdf(job / "vacancy.pdf", ["for kort", "enda kort"])
            with self.assertRaises(INGEST.IngestError):
                INGEST.ingest_job(job, force=False)

    def test_discovery_validates_ids_duplicate_jobs_and_batch_prefix(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            bad = root / "invalid cluster" / "B01_J001_raadgiver"
            bad.mkdir(parents=True)
            with self.assertRaises(INGEST.IngestConfigurationError):
                INGEST.discover_jobs(root)

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for cluster in ("B01_C01_process", "B01_C02_control"):
                (root / cluster / "B01_J001_raadgiver").mkdir(parents=True)
            with self.assertRaises(INGEST.IngestConfigurationError):
                INGEST.discover_jobs(root)

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "B01_C01_process" / "B02_J001_raadgiver").mkdir(parents=True)
            with self.assertRaises(INGEST.IngestConfigurationError):
                INGEST.discover_jobs(root)

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            long_job = "B01_J001_" + "a" * 120
            (root / "B01_C01_process" / long_job).mkdir(parents=True)
            with self.assertRaises(INGEST.IngestConfigurationError):
                INGEST.discover_jobs(root)

    def test_configuration_problem_is_distinct_from_job_blocker(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaises(INGEST.IngestConfigurationError):
                INGEST.run(Path(temporary) / "missing")


if __name__ == "__main__":
    unittest.main()
