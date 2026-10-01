"""Editorial signals: word counts and the formula tics these runs produced.

Counting, not detection. Nothing here fails a command, changes triage or
blocks a submission; the numbers and names are printed so the human and the
stage sessions can see what the last batch kept repeating.
"""

from __future__ import annotations

import re
from typing import Any

_WORD = re.compile(r"[0-9A-Za-zÀ-ÖØ-öø-ÿ'’-]+")


def words(text: str | None) -> int:
    return len(_WORD.findall(text or ""))


def cv_dynamic_words(cv: dict[str, Any] | None) -> int:
    cv = cv or {}
    total = words(cv.get("headline")) + words(cv.get("profile"))
    total += sum(words(item) for item in cv.get("competencies") or [])
    for override in cv.get("employment_overrides") or []:
        total += sum(words(b) for b in override.get("bullets") or [])
    total += words(cv.get("tools_line"))
    return total


def letter_words(letter: dict[str, Any] | None) -> int:
    if not letter:
        return 0
    return (
        words(letter.get("opening"))
        + sum(words(p) for p in letter.get("body_paragraphs") or [])
        + words(letter.get("closing"))
    )


def letter_text(letter: dict[str, Any] | None) -> str:
    if not letter:
        return ""
    return "\n".join(
        [letter.get("opening", "")]
        + list(letter.get("body_paragraphs") or [])
        + [letter.get("closing", "")]
    )


def cv_text(cv: dict[str, Any] | None) -> str:
    cv = cv or {}
    parts = [cv.get("headline", ""), cv.get("profile", ""), cv.get("tools_line") or ""]
    parts += list(cv.get("competencies") or [])
    for override in cv.get("employment_overrides") or []:
        parts += list(override.get("bullets") or [])
    return "\n".join(parts)


#: (name, pattern, where) - where is "letter", "opening", "closing" or "cv".
TICS: tuple[tuple[str, str, str], ...] = (
    ("stock close", r"forteller gjerne mer( om dette)? i en samtale", "closing"),
    ("«søker … fordi»", r"søker\b[^.]{0,90}\bfordi\b|grunnen til at jeg søker", "letter"),
    ("cleft motive", r"Det (som|jeg) [^.]{0,80}, er\b", "letter"),
    ("identity opening", r"^(Jeg er (samfunnsøkonom|rådgiver)|Som rådgiver)", "opening"),
    ("title restated in opening", r"søker (på )?stillingen som|Jeg søker stillingen\b", "opening"),
    ("«avviklet» ending", r"avviklet\.?\s*$", "letter"),
    ("bolt-on marker", r"\b(Jeg er også|Jeg har også|Ved siden av|I tillegg har jeg)\b", "letter"),
    ("first person in CV", r"\b(jeg|meg|min|mitt|mine)\b", "cv"),
)

#: Counted separately: one transfer bridge is fine, a refrain is not.
BRIDGE = r"(vil|kan|ville) jeg (ta med|bruke|bidra med|bygge)|jeg vil ta med"


def scan(package: dict[str, Any]) -> list[str]:
    """Signal names present in this package, with counts where they matter."""
    cv = package.get("cv") or {}
    letter = package.get("letter") or {}
    found: list[str] = []
    bodies = {
        "letter": letter_text(letter),
        "opening": letter.get("opening", "") if letter else "",
        "closing": letter.get("closing", "") if letter else "",
        "cv": cv_text(cv),
    }
    for name, pattern, where in TICS:
        text = bodies.get(where, "")
        if text and re.search(pattern, text, re.IGNORECASE | re.MULTILINE):
            found.append(name)
    bridges = len(re.findall(BRIDGE, bodies["letter"], re.IGNORECASE))
    if bridges > 1:
        found.append(f"repeated transfer bridge x{bridges}")
    return found


def first_sentence(text: str) -> str:
    parts = re.split(r"(?<=[.!?])\s+", (text or "").strip())
    return parts[0] if parts else ""


def last_sentence(text: str) -> str:
    parts = [p for p in re.split(r"(?<=[.!?])\s+", (text or "").strip()) if p]
    return parts[-1] if parts else ""
