"""Advisory editorial pattern detection. Never a validation or queue input."""

from __future__ import annotations

import re
from typing import Any


def inspect_package(
    package: dict[str, Any], *, title: str = "",
    effective_cv: dict[str, Any] | None = None,
) -> list[dict[str, str]]:
    cv = package.get("cv") or {}
    letter = package.get("letter") or {}
    findings: list[dict[str, str]] = []

    def add(code: str, location: str, sample: str) -> None:
        findings.append({"code": code, "location": location, "excerpt": sample[:180]})

    cv_text = "\n".join(str(cv.get(key) or "") for key in ("headline", "profile"))
    cv_text += "\n" + "\n".join(cv.get("competencies") or [])
    bullet_rows = (
        effective_cv.get("employments") or []
        if effective_cv is not None else cv.get("employment_overrides") or []
    )
    for row in bullet_rows:
        cv_text += "\n" + "\n".join(row.get("bullets") or [])
    match = re.search(r"\b(jeg|min|mitt|mine|meg)\b", cv_text, re.I)
    if match:
        add("cv_first_person", "cv", match.group())

    opening = str(letter.get("opening") or "")
    close = str(letter.get("closing") or "")
    paragraphs = [opening, *(letter.get("body_paragraphs") or []), close]
    if re.search(r"\b(?:jeg\s+)?ser\s+frem\s+til\s+(?:å\s+høre\s+fra\s+dere|muligheten\s+til\s+å\s+utdype)\b", close, re.I):
        add("stock_close", "letter.closing", close)
    if re.search(r"\bsøker\b.{0,90}\bfordi\b", opening, re.I):
        add("seeker_because", "letter.opening", opening)
    if re.search(r"\bdet\s+er\b.{0,100}\bsom\b", opening, re.I):
        add("cleft_motive", "letter.opening", opening)
    if re.match(r"\s*(?:jeg\s+er|som\s+(?:person|fagperson)|med\s+min\s+bakgrunn)", opening, re.I):
        add("identity_opening", "letter.opening", opening)
    if title and title.casefold() in opening.casefold():
        add("title_restatement", "letter.opening", opening)
    bridges = 0
    for i, paragraph in enumerate(paragraphs):
        value = str(paragraph).strip()
        if re.search(r"\bavviklet[.!?]?\s*$", value, re.I):
            add("avviklet_ending", f"letter.paragraphs[{i}]", value)
        if re.search(r"\b(?:ta med|overføre|bruke)\s+(?:denne\s+)?erfaring(?:en)?\b", value, re.I):
            bridges += 1
        if re.search(r"\b(?:i denne rollen|hos dere|for [A-ZÆØÅ][\wÆØÅæøå-]+)\b\s*[.!?]?\s*$", value):
            add("bolt_on_marker", f"letter.paragraphs[{i}]", value)
    if bridges > 1:
        add("repeated_transfer_bridge", "letter", str(bridges))
    return findings
