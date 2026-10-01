"""Private-material scans for employer-facing text.

Spec 14.2 / Contract 8.2 permit a narrow, high-precision check that no
known private/control token, internal path or internal ID appears in
employer-facing fields. Everything else is out of bounds:

* "Lexical checks MUST be narrow and high precision. A stock phrase or
  ordinary employer word MUST NOT fail merely because it appears in a
  style-warning list." (Spec 14.2)
* "Do not convert stock/cliche phrase guidance into a regex failure."
  (Contract 8.2)
* `brenner for` is explicitly named as a semantic guidance issue that must
  not fail deterministic validation (Spec 10.3).

So: reference syntaxes, template tags, facet codes, filesystem paths and
closed-set typology labels are rejected, because none of them has a
legitimate employer-facing use in a Norwegian CV or letter. Ordinary
Norwegian and English work vocabulary is not touched at all.

Adapted from P0.7 finalize.validate_visible_text (inspected), with the
token sets retuned for P0.9 namespaces and a false-positive fixture corpus
kept alongside the tests.
"""

from __future__ import annotations

import re
from typing import Iterable

from .errors import ValidationResult

#: Reference syntaxes owned by this system. None is employer-facing.
_PATTERNS: list[tuple[str, re.Pattern[str], str]] = [
    (
        "factual evidence reference",
        re.compile(r"\bEV:(?:WORK|EDU|OTHER)#[A-Za-z0-9._-]+"),
        "an EV: evidence reference is a private audit coordinate",
    ),
    (
        "mechanical baseline reference",
        re.compile(r"\bBL:(?:EMP|EDU|SEC)_[A-Z0-9_]+"),
        "a BL: baseline reference is a private mechanical coordinate",
    ),
    (
        "baseline identifier",
        re.compile(r"\b(?:EMP|EDU|SEC)[_-][A-Z][A-Z0-9_-]{2,}"),
        "a baseline identifier is internal structure",
    ),
    (
        "personality facet code",
        re.compile(r"\bPF-[0-9]{2}\b"),
        "facet codes are private interpretive context",
    ),
    (
        "source-stated claim identifier",
        re.compile(r"\b(?:CLM|PRJ|OHV)-[A-Z0-9]+(?:-[A-Z0-9]+)*\b"),
        "source-stated identifiers are provenance, not employer text",
    ),
    (
        "template control tag",
        re.compile(r"\b(?:CV_[A-Z_]{3,}|APP_[A-Z_]{3,}|APPLICATION_BODY)\b"),
        "template control tags must never survive into content",
    ),
    (
        "unresolved placeholder",
        re.compile(r"\{\{|\}\}|\{%|%\}|\[PLACEHOLDER\]"),
        "an unresolved placeholder means the fill step did not complete",
    ),
    (
        "filesystem path",
        re.compile(r"[A-Za-z]:\\[\\A-Za-z0-9_.-]+|(?:^|\s)(?:runs|authorities|generated)/[A-Za-z0-9_./-]+"),
        "internal paths must not appear in employer text",
    ),
    (
        "run identifier",
        re.compile(r"\br[0-9]{8}-[0-9]{6}-[a-f0-9]{6}\b"),
        "run identifiers are internal state",
    ),
]

#: Closed-set typology labels. Loaded from policy/personality_facets.json at
#: call time so the policy file stays the single source of truth; this list
#: is only the fallback used when no policy is supplied.
_DEFAULT_TYPOLOGY = (
    "MBTI", "DISC", "Enneagram", "RIASEC", "Big Five", "HEXACO", "Socionics",
)

#: Phrases that MUST NOT fail. These are semantic writing-guidance issues
#: owned by policy and the human, never mechanical failures. The test suite
#: asserts each of these passes (Contract 17.1 test 14).
KNOWN_GOOD_PHRASES = (
    "brenner for",
    "jeg brenner for faget",
    "utviklet beslutningsstøtte",
    "tok hovedansvar for leveransen",
    "i et tverrfaglig team",
    "erfaring med Power BI og SQL",
    "Direktørens stab – Analyseavdelingen",
    "Master i samfunnsøkonomi",
    "strukturert og selvstendig",
    "god samarbeidsevne på tvers av fag",
)


def _typology_pattern(tokens: Iterable[str]) -> re.Pattern[str]:
    escaped = sorted((re.escape(t) for t in tokens), key=len, reverse=True)
    return re.compile(r"\b(?:" + "|".join(escaped) + r")\b")


def scan(
    text: str,
    *,
    file_label: str,
    location: str,
    typology_tokens: Iterable[str] | None = None,
    result: ValidationResult | None = None,
) -> ValidationResult:
    """Report every private-material hit in one pass."""
    result = result if result is not None else ValidationResult()

    for name, pattern, why in _PATTERNS:
        for match in pattern.finditer(text):
            result.add(
                contract_id="DEC-27",
                file=file_label,
                location=location,
                expected="no private/control token, internal path or internal ID "
                         "in employer-facing text",
                observed=f"{name}: {match.group(0).strip()!r} - {why}",
            )

    tokens = list(typology_tokens) if typology_tokens is not None else list(_DEFAULT_TYPOLOGY)
    if tokens:
        for match in _typology_pattern(tokens).finditer(text):
            result.add(
                contract_id="DEC-35",
                file=file_label,
                location=location,
                expected="no closed-set typology label in employer-facing text",
                observed=f"typology label: {match.group(0)!r}",
            )
    return result


def employer_facing_text(package: dict) -> list[tuple[str, str]]:
    """Every field that reaches the employer, with its field path.

    Deliberately excludes writer_note and every binding/provenance field:
    those are private by design and are never rendered.
    """
    chunks: list[tuple[str, str]] = []
    cv = package.get("cv") or {}
    chunks.append(("cv.headline", cv.get("headline", "")))
    chunks.append(("cv.profile", cv.get("profile", "")))
    for index, item in enumerate(cv.get("competencies") or []):
        chunks.append((f"cv.competencies[{index}]", item))
    for override in cv.get("employment_overrides") or []:
        key = override.get("employment_id", "?")
        for index, bullet in enumerate(override.get("bullets") or []):
            chunks.append((f"cv.employment_overrides[{key}].bullets[{index}]", bullet))
    letter = package.get("letter") or {}
    chunks.append(("letter.opening", letter.get("opening", "")))
    for index, paragraph in enumerate(letter.get("body_paragraphs") or []):
        chunks.append((f"letter.body_paragraphs[{index}]", paragraph))
    chunks.append(("letter.closing", letter.get("closing", "")))
    return [(where, text) for where, text in chunks if text]


def scan_package(
    package: dict,
    *,
    file_label: str,
    typology_tokens: Iterable[str] | None = None,
    result: ValidationResult | None = None,
) -> ValidationResult:
    result = result if result is not None else ValidationResult()
    for location, text in employer_facing_text(package):
        scan(
            text,
            file_label=file_label,
            location=location,
            typology_tokens=typology_tokens,
            result=result,
        )
    return result
