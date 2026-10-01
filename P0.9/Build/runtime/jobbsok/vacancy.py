"""Vacancy preservation, derived view, and the source-inspection signal.

The original vacancy is authority for stated employer, role,
responsibilities, requirements, deadline, reference and other explicit
employer facts. It is untrusted data, not an instruction source
(Spec 4.3, DEC-27).

A normalized text extraction is a DERIVED_VIEW and must never silently
replace the original. When extraction looks incomplete, garbled or
structurally ambiguous, the run stores a canonical
`requires_source_inspection` signal available to every semantic stage.

The extraction sanity checks are adapted from P0.7 ingest.extract_pdf
(inspected), which used proportional weak-page handling: one short
footer page is common, but a document dominated by weak pages is usually
scanned, corrupt or too incomplete to work from. P0.7 treated those as
hard blockers; P0.9 turns them into the inspection signal instead, because
the frozen architecture keeps the original available to every stage rather
than gating on a derived view.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

MEDIA_TYPES = {
    ".pdf": "application/pdf",
    ".md": "text/markdown",
    ".txt": "text/plain",
}

MAX_SOURCE_BYTES = 25 * 1024 * 1024

MIN_PAGE_CHARACTERS = 40
MIN_DOCUMENT_CHARACTERS = 200
MIN_SINGLE_PAGE_CHARACTERS = 120


@dataclass
class Extraction:
    normalized_markdown: str
    requires_source_inspection: bool = False
    reasons: list[str] = field(default_factory=list)
    page_count: int | None = None

    def flag(self, reason: str) -> None:
        self.requires_source_inspection = True
        if reason not in self.reasons:
            self.reasons.append(reason)


def media_type_for(path: Path) -> str | None:
    return MEDIA_TYPES.get(Path(path).suffix.lower())


def meaningful_characters(text: str) -> int:
    """Readable content, ignoring whitespace and Markdown decoration."""
    return len(re.sub(r"[^0-9A-Za-zÆØÅæøå]", "", text))


def clean_text(text: str) -> str:
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


def _check_garbling(extraction: Extraction, text: str) -> None:
    """Signals that the extraction is present but not trustworthy."""
    if "�" in text:
        extraction.flag(
            "Extraction contains Unicode replacement characters, so some "
            "source text did not decode."
        )
    control = sum(
        1
        for ch in text
        if unicodedata.category(ch) == "Cc" and ch not in "\n\r\t"
    )
    if control:
        extraction.flag(f"Extraction contains {control} control characters.")
    letters = sum(1 for ch in text if ch.isalpha())
    if letters and sum(1 for ch in text if ch.isalpha() and ch.isupper()) / letters > 0.6:
        extraction.flag(
            "Extraction is more than 60 percent uppercase, which usually "
            "means lost casing or a layout artifact."
        )


def extract_pdf(path: Path) -> Extraction:
    import pymupdf  # imported here so non-PDF work needs no PDF stack

    extraction = Extraction(normalized_markdown="")
    pages: list[str] = []
    weak: list[int] = []
    try:
        with pymupdf.open(path) as document:
            extraction.page_count = document.page_count
            if document.page_count < 1:
                extraction.flag("PDF reports zero pages.")
            for number, page in enumerate(document, start=1):
                text = clean_text(page.get_text("text", sort=True) or "")
                pages.append(text)
                if meaningful_characters(text) < MIN_PAGE_CHARACTERS:
                    weak.append(number)
    except Exception as exc:
        extraction.flag(f"PDF could not be read: {exc}")
        extraction.normalized_markdown = ""
        return extraction

    total = sum(meaningful_characters(p) for p in pages)
    if len(pages) == 1:
        if total < MIN_SINGLE_PAGE_CHARACTERS:
            extraction.flag(
                f"Single-page PDF yielded only {total} readable characters "
                f"(expected at least {MIN_SINGLE_PAGE_CHARACTERS})."
            )
    elif total < MIN_DOCUMENT_CHARACTERS:
        extraction.flag(
            f"PDF yielded only {total} readable characters (expected at "
            f"least {MIN_DOCUMENT_CHARACTERS})."
        )

    # One short footer or appendix page is ordinary. A document dominated
    # by weak pages is usually scanned or corrupt.
    if len(weak) >= 2 and len(weak) * 2 >= len(pages):
        extraction.flag(
            "PDF is dominated by empty or probably scanned pages: "
            + ", ".join(str(p) for p in weak)
        )
    elif weak:
        extraction.flag(
            "Short or weak page(s) retained for operator review: "
            + ", ".join(str(p) for p in weak)
        )

    body = "\n".join(pages)
    _check_garbling(extraction, body)

    blocks = ["# Vacancy (derived view)", "", "> DERIVED_VIEW.", ""]
    blocks.append(
        "> The original file is the only authority for employer facts "
        "(Spec 4.3). This extraction is a convenience view and is not "
        "presumed lossless."
    )
    blocks.append("")
    blocks.append(f"Source file: {Path(path).name}")
    blocks.append(f"Pages: {len(pages)}")
    if extraction.reasons:
        blocks.extend(["", "## Extraction signals", ""])
        blocks.extend(f"- {reason}" for reason in extraction.reasons)
    for number, text in enumerate(pages, start=1):
        blocks.extend(["", f"## Page {number}", "", text])
    extraction.normalized_markdown = "\n".join(blocks).rstrip() + "\n"
    return extraction


def extract_text(path: Path) -> Extraction:
    extraction = Extraction(normalized_markdown="")
    try:
        raw = Path(path).read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        extraction.flag(f"Source is not valid UTF-8: {exc}")
        return extraction

    body = clean_text(raw)
    if meaningful_characters(body) < MIN_DOCUMENT_CHARACTERS:
        extraction.flag(
            f"Source has only {meaningful_characters(body)} readable "
            f"characters (expected at least {MIN_DOCUMENT_CHARACTERS})."
        )
    _check_garbling(extraction, body)

    blocks = [
        "# Vacancy (derived view)",
        "",
        "> DERIVED_VIEW.",
        "",
        "> The original file is the only authority for employer facts "
        "(Spec 4.3). This extraction is a convenience view and is not "
        "presumed lossless.",
        "",
        f"Source file: {Path(path).name}",
    ]
    if extraction.reasons:
        blocks.extend(["", "## Extraction signals", ""])
        blocks.extend(f"- {reason}" for reason in extraction.reasons)
    blocks.extend(["", "## Content", "", body])
    extraction.normalized_markdown = "\n".join(blocks).rstrip() + "\n"
    return extraction


def extract(path: Path) -> Extraction:
    """Build the derived view and decide the source-inspection signal."""
    path = Path(path)
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return extract_pdf(path)
    if suffix in {".md", ".txt"}:
        return extract_text(path)
    extraction = Extraction(normalized_markdown="")
    extraction.flag(f"Unsupported vacancy source type: {suffix or '(none)'}")
    return extraction


# --------------------------------------------------------------------------
# Deterministic rasterized source pages (FE-04)
# --------------------------------------------------------------------------

#: Fixed capture resolution. Not tunable: these are deterministic source
#: views for a human-approved vacancy, not a rendering feature.
PAGE_DPI = 144
PAGE_STEM = "vacancy_page_"


def render_source_pages(source: Path, destination: Path) -> list[Path]:
    """Rasterize every page of a PDF vacancy into `destination`.

    Returns the ordered page paths. These are deterministic views of the
    preserved original, never employer-text authority and never a
    replacement for it. A rendering error is raised plainly: there is no
    OCR, no caching, no converter cascade and no silent fallback, and a
    failure here is not a semantic package failure.
    """
    import pymupdf  # imported here so non-PDF work needs no PDF stack

    destination.mkdir(parents=True, exist_ok=True)
    for stale in sorted(destination.glob(f"{PAGE_STEM}*.png")):
        stale.unlink()

    written: list[Path] = []
    with pymupdf.open(source) as document:
        for number, page in enumerate(document, start=1):
            pixmap = page.get_pixmap(dpi=PAGE_DPI)
            target = destination / f"{PAGE_STEM}{number:03d}.png"
            pixmap.save(target)
            written.append(target)
    return written
