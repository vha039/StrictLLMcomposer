from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import re
import tempfile
import unicodedata

import pymupdf


MACRO_CLUSTER_RE = re.compile(r"^B[0-9]{2}_C[0-9]{2}_[a-z0-9_]+$")
JOB_RE = re.compile(r"^B[0-9]{2}_J[0-9]{3}_[a-z0-9_]+$")
MIN_PAGE_CHARACTERS = 40
MIN_DOCUMENT_CHARACTERS = 200
MIN_SINGLE_PAGE_CHARACTERS = 120
MAX_MACRO_CLUSTER_ID_LENGTH = 100
MAX_JOB_ID_LENGTH = 120


class IngestError(RuntimeError):
    """A job-local input problem; run() returns exit code 1."""


class IngestConfigurationError(RuntimeError):
    """A repository or ID contract problem; the CLI returns exit code 2."""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def meaningful_characters(text: str) -> int:
    """Count readable content, not whitespace or Markdown decoration."""

    return len(re.sub(r"[^0-9A-Za-zÆØÅæøå]", "", text))


def clean_page_text(text: str) -> str:
    normalized = unicodedata.normalize("NFC", text).replace("\x00", "")
    lines: list[str] = []
    previous_blank = False
    for raw_line in normalized.splitlines():
        line = re.sub(r"[ \t]+", " ", raw_line).strip()
        if line:
            lines.append(line)
            previous_blank = False
        elif not previous_blank:
            lines.append("")
            previous_blank = True
    return "\n".join(lines).strip()


def extract_pdf(pdf_path: Path) -> tuple[list[str], list[str]]:
    """Extract selectable text with proportional weak-page handling.

    A single short page is a warning when the document as a whole is
    meaningful. Several weak/empty pages are a genuine usability blocker.
    """

    pages: list[str] = []
    weak_pages: list[int] = []
    try:
        with pymupdf.open(pdf_path) as document:
            if document.page_count < 1:
                raise IngestError("PDF contains no pages.")
            for page_number, page in enumerate(document, start=1):
                text = clean_page_text(page.get_text("text", sort=True) or "")
                pages.append(text)
                if meaningful_characters(text) < MIN_PAGE_CHARACTERS:
                    weak_pages.append(page_number)
    except IngestError:
        raise
    except Exception as exc:
        raise IngestError(f"PDF could not be read: {exc}") from exc

    total = sum(meaningful_characters(page) for page in pages)
    if len(pages) == 1:
        if total < MIN_SINGLE_PAGE_CHARACTERS:
            raise IngestError(
                "Single-page PDF has too little selectable text "
                f"({total} characters; minimum {MIN_SINGLE_PAGE_CHARACTERS})."
            )
    elif total < MIN_DOCUMENT_CHARACTERS:
        raise IngestError(
            "PDF has too little selectable text "
            f"({total} characters; minimum {MIN_DOCUMENT_CHARACTERS})."
        )

    # One short footer/appendix page is common. A document dominated by weak
    # pages is usually scanned, corrupt, or too incomplete for Stage 1.
    if len(weak_pages) >= 2 and len(weak_pages) * 2 >= len(pages):
        raise IngestError(
            "PDF has too many empty or probably scanned pages: "
            + ", ".join(str(page) for page in weak_pages)
        )

    warnings: list[str] = []
    if total < MIN_DOCUMENT_CHARACTERS:
        warnings.append(
            "Short single-page source accepted after selectable-text check."
        )
    if weak_pages:
        warnings.append(
            "Short/weak page(s) retained for operator review: "
            + ", ".join(str(page) for page in weak_pages)
        )
    return pages, warnings


def render_vacancy_markdown(
    pdf_path: Path,
    pages: list[str],
    warnings: list[str],
) -> str:
    blocks = [
        "# Vacancy",
        "",
        f"Source file: {pdf_path.name}",
        f"SHA-256: {sha256(pdf_path)}",
        f"Pages: {len(pages)}",
    ]
    if warnings:
        blocks.extend(["", "## Extraction notes", "", *[f"- {item}" for item in warnings]])
    for page_number, text in enumerate(pages, start=1):
        blocks.extend(["", f"## Page {page_number}", "", text])
    return "\n".join(blocks).rstrip() + "\n"


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w",
        encoding="utf-8",
        newline="\n",
        dir=path.parent,
        prefix=f"{path.name}.",
        suffix=".tmp",
        delete=False,
    ) as handle:
        temporary = Path(handle.name)
        handle.write(text)
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def discover_jobs(input_root: Path) -> list[tuple[Path, Path]]:
    if not input_root.is_dir():
        raise IngestConfigurationError(
            f"Stage 1 input root does not exist: {input_root}"
        )

    cluster_dirs = sorted(path for path in input_root.iterdir() if path.is_dir())
    if not cluster_dirs:
        raise IngestConfigurationError(
            f"No macro-cluster directories found below {input_root}."
        )

    discovered: list[tuple[Path, Path]] = []
    seen_job_ids: dict[str, Path] = {}
    for cluster_dir in cluster_dirs:
        if (
            not MACRO_CLUSTER_RE.fullmatch(cluster_dir.name)
            or len(cluster_dir.name) > MAX_MACRO_CLUSTER_ID_LENGTH
        ):
            raise IngestConfigurationError(f"Invalid macro-cluster ID: {cluster_dir.name}")
        batch_id = cluster_dir.name.split("_", 1)[0]
        job_dirs = sorted(path for path in cluster_dir.iterdir() if path.is_dir())
        if not job_dirs:
            raise IngestConfigurationError(
                f"Macro-cluster contains no job folders: {cluster_dir}"
            )
        for job_dir in job_dirs:
            if (
                not JOB_RE.fullmatch(job_dir.name)
                or len(job_dir.name) > MAX_JOB_ID_LENGTH
            ):
                raise IngestConfigurationError(f"Invalid job ID: {job_dir.name}")
            if not job_dir.name.startswith(f"{batch_id}_"):
                raise IngestConfigurationError(
                    f"Job {job_dir.name} has a different batch prefix than "
                    f"macro-cluster {cluster_dir.name}."
                )
            previous = seen_job_ids.get(job_dir.name)
            if previous is not None:
                raise IngestConfigurationError(
                    f"Duplicate job ID {job_dir.name}: {previous} and {job_dir}"
                )
            seen_job_ids[job_dir.name] = job_dir
            discovered.append((cluster_dir, job_dir))
    return discovered


def _valid_markdown(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise IngestError(f"vacancy.md is not valid UTF-8: {exc}") from exc
    if meaningful_characters(text) < MIN_DOCUMENT_CHARACTERS:
        raise IngestError(
            "vacancy.md has too little readable content "
            f"({meaningful_characters(text)} characters; minimum "
            f"{MIN_DOCUMENT_CHARACTERS})."
        )
    return True


def _single_vacancy_pdf(job_dir: Path) -> Path:
    pdfs = sorted(job_dir.glob("*.pdf"))
    if len(pdfs) != 1 or pdfs[0].name != "vacancy.pdf":
        raise IngestError(
            "Job requires exactly one source PDF named vacancy.pdf."
        )
    return pdfs[0]


def ingest_job(job_dir: Path, *, force: bool) -> str:
    vacancy_md = job_dir / "vacancy.md"
    if vacancy_md.is_file():
        try:
            _valid_markdown(vacancy_md)
        except IngestError:
            if not force and vacancy_md.stat().st_size > 0:
                raise IngestError(
                    "Existing vacancy.md is not meaningful; use --force with a "
                    "valid vacancy.pdf to replace it."
                )
        else:
            if not force:
                return "REUSED"

    pdf_path = _single_vacancy_pdf(job_dir)
    pages, warnings = extract_pdf(pdf_path)
    atomic_write_text(vacancy_md, render_vacancy_markdown(pdf_path, pages, warnings))
    return "EXTRACTED"


def run(input_root: Path, *, force: bool = False) -> tuple[int, dict[str, int]]:
    jobs = discover_jobs(input_root)
    clusters = {cluster.name for cluster, _ in jobs}
    counts = {"reused": 0, "extracted": 0, "blocked": 0}

    for cluster_dir, job_dir in jobs:
        try:
            status = ingest_job(job_dir, force=force)
            counts[status.lower()] += 1
            print(f"[{status}] {cluster_dir.name}/{job_dir.name}")
        except IngestError as exc:
            counts["blocked"] += 1
            print(f"[BLOCKED] {cluster_dir.name}/{job_dir.name}: {exc}")

    print()
    print("INGEST SUMMARY")
    print(f"Clusters found: {len(clusters)}")
    print(f"Jobs found: {len(jobs)}")
    print(f"Existing vacancy.md reused: {counts['reused']}")
    print(f"PDFs extracted: {counts['extracted']}")
    print(f"Blocked: {counts['blocked']}")
    print(f"Result: {'PASS' if counts['blocked'] == 0 else 'PARTIAL_FAILURE'}")
    return (0 if counts["blocked"] == 0 else 1), counts


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate Stage 1 input and extract selectable-text vacancy PDFs."
    )
    parser.add_argument(
        "input_root",
        nargs="?",
        default="stg1_analyze/input",
        help="Stage 1 input root.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing vacancy.md from its vacancy.pdf.",
    )
    args = parser.parse_args()
    try:
        exit_code, _ = run(Path(args.input_root).resolve(), force=args.force)
    except IngestConfigurationError as exc:
        print(f"INGEST CONFIGURATION ERROR: {exc}")
        raise SystemExit(2) from exc
    except Exception as exc:
        print(f"INGEST ERROR: {exc}")
        raise SystemExit(2) from exc
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
