"""Evidence cards: a fact never travels without its ceiling.

A card is one frozen evidence section plus the boundary material that
governs it:

* the section text (extended to its subtree when the body is a stub);
* the digest row from WORK 0.3 / OTHER 0.2 / EDU 0.5 that points at it,
  rendered as `Lifecycle | Can prove | Live ceilings`;
* every row or bullet in the explicit boundary sections that mentions one of
  the section's own stated IDs (PRJ-, CLM-, EMP-, EDU-).

A pack ends with one Boundaries appendix: the global "explicitly forbidden"
and "unresolved" sections, verbatim.

Retrieval is never refused. A stage gets a default pack built from its own
scope, and may fetch anything else by id or literal search; what it used
beyond the brief is declared in the artifact.
"""

from __future__ import annotations

import re
from typing import Any

from . import evidence_index as index_module

#: Where each authority keeps its maintained digest table.
DIGEST_SECTIONS: dict[str, str] = {"WORK": "0.3", "OTHER": "0.2", "EDU": "0.5"}

#: Global boundary sections that govern every claim.
BOUNDARY_SECTIONS: tuple[tuple[str, str], ...] = (
    ("WORK", "8"), ("WORK", "10.1"), ("WORK", "10.2"),
    ("EDU", "4.2"), ("EDU", "4.3"),
    ("OTHER", "0.3"), ("OTHER", "4.5"),
)

#: Sections scanned for lines that mention a card's own stated IDs.
CEILING_SECTIONS: tuple[tuple[str, str], ...] = (
    ("WORK", "8"), ("WORK", "10.1"), ("WORK", "10.2"), ("EDU", "4.2"),
)

_METADATA_BLOCK = re.compile(
    r"^\*\*(Selection metadata|Kompakt evidens- og autoritetskart)\*\*.*?(?=^\*\*|\Z)",
    re.MULTILINE | re.DOTALL,
)
_STATED_ID = re.compile(r"\b(?:PRJ|CLM|EMP|EDU|OHV|ROLE|TITLE|ID)-[A-Z0-9-]+\b")


def _text(context: Any, source_id: str) -> str:
    return context.assets.path("authorities", source_id).read_bytes().decode("utf-8")


def _entry(context: Any, evidence_id: str) -> dict[str, Any] | None:
    return index_module.resolve(context.index, evidence_id)


def _subtree_span(text: str, entry: dict[str, Any]) -> tuple[int, int]:
    """Extend a stub section to everything under it."""
    lines = text.splitlines()
    level = entry.get("heading_level") or 6
    start, end = entry["line_start"], entry["line_end"]
    cursor = end
    while cursor < len(lines):
        match = re.match(r"^(#{1,6})\s", lines[cursor])
        if match and len(match.group(1)) <= level:
            break
        cursor += 1
    return start, cursor


def _body_is_stub(text: str, entry: dict[str, Any]) -> bool:
    body = index_module.slice_entry(text, entry).splitlines()[1:]
    return len([line for line in body if line.strip()]) <= 2


def _digest_line(context: Any, entry: dict[str, Any]) -> str | None:
    source_id = entry["source_id"]
    section = DIGEST_SECTIONS.get(source_id)
    if not section:
        return None
    digest_entry = index_module.resolve_section(context.index, source_id, section)
    if digest_entry is None:
        return None
    text = _text(context, source_id)
    for row in index_module.digest_rows(text, digest_entry):
        resolved = index_module.resolve_section(
            context.index, source_id, row["source_section"]
        )
        if resolved and resolved["evidence_id"] == entry["evidence_id"]:
            return (
                f"{row['lifecycle']} | can prove: {row['can_prove']} | "
                f"live ceilings: {row['live_ceilings']}"
            )
    return None


def _ceiling_lines(context: Any, entry: dict[str, Any]) -> list[str]:
    stated = set(entry.get("source_stated_ids") or [])
    text = index_module.slice_entry(_text(context, entry["source_id"]), entry)
    stated |= set(_STATED_ID.findall(text))
    if not stated:
        return []
    out: list[str] = []
    for source_id, section in CEILING_SECTIONS:
        target = index_module.resolve_section(context.index, source_id, section)
        if target is None:
            continue
        body = index_module.slice_entry(_text(context, source_id), target)
        for line in body.splitlines():
            if line.strip() and any(item in line for item in stated):
                out.append(f"{source_id} {section}: {line.strip()}")
    return out


def card(context: Any, evidence_id: str, *, full: bool = False) -> str:
    entry = _entry(context, evidence_id)
    if entry is None:
        return f"### {evidence_id}\n(unknown evidence id)\n"
    source_id = entry["source_id"]
    text = _text(context, source_id)
    if _body_is_stub(text, entry):
        start, end = _subtree_span(text, entry)
        body = "".join(text.splitlines(keepends=True)[start - 1: end])
    else:
        body = index_module.slice_entry(text, entry)
    if not full:
        body = _METADATA_BLOCK.sub("", body)
    heading = (entry.get("heading_path") or [""])[-1]
    parts = [
        f"### {evidence_id} · {source_id} {entry['line_start']}-{entry['line_end']} · {heading}"
    ]
    digest = _digest_line(context, entry)
    if digest:
        parts.append(f"*Digest:* {digest}")
    ceilings = _ceiling_lines(context, entry)
    if ceilings:
        parts.append("*Boundaries naming this record:*")
        parts.extend(f"- {line}" for line in ceilings)
    parts.append(body.strip())
    return "\n\n".join(parts).rstrip() + "\n"


def boundaries(context: Any) -> str:
    """The global boundary appendix, verbatim."""
    parts = ["## Boundaries (global, verbatim)"]
    for source_id, section in BOUNDARY_SECTIONS:
        entry = index_module.resolve_section(context.index, source_id, section)
        if entry is None:
            continue
        body = index_module.slice_entry(_text(context, source_id), entry)
        parts.append(body.strip())
    return "\n\n".join(parts).rstrip() + "\n"


def pack(
    context: Any, evidence_ids: list[str], *, full: bool = False,
    title: str = "Evidence cards", with_boundaries: bool = True,
) -> str:
    seen: list[str] = []
    for item in evidence_ids:
        if item not in seen:
            seen.append(item)
    parts = [f"# {title}", ""]
    for evidence_id in seen:
        parts.append(card(context, evidence_id, full=full))
    if with_boundaries:
        parts.append(boundaries(context))
    return "\n".join(parts)


def catalog(context: Any) -> str:
    """Every evidence ID with its heading path: the full map, always present."""
    lines = ["# Evidence catalog (ids only; fetch any of them)", ""]
    for entry in context.index["entries"]:
        heading = (entry.get("heading_path") or [""])[-1]
        lines.append(f"- {entry['evidence_id']} — {heading}")
    return "\n".join(lines) + "\n"


def digests(context: Any) -> str:
    """The three maintained digest tables, with resolved evidence ids."""
    lines = ["# Authority digests (navigation metadata, never selected evidence)", ""]
    for source_id, section in DIGEST_SECTIONS.items():
        entry = index_module.resolve_section(context.index, source_id, section)
        if entry is None:
            continue
        text = _text(context, source_id)
        lines.append(f"## {source_id} {section}")
        lines.append("")
        for row in index_module.digest_rows(text, entry):
            resolved = index_module.resolve_section(
                context.index, source_id, row["source_section"]
            )
            ref = resolved["evidence_id"] if resolved else "(unresolved)"
            lines.append(
                f"- **{row['record']}** [{ref}] — {row['lifecycle']} — can prove: "
                f"{row['can_prove']} — live ceilings: {row['live_ceilings']}"
            )
        lines.append("")
    return "\n".join(lines)


def retrieval_index(context: Any) -> str:
    """The section-0.4 keyword tables, as literal -> evidence ids."""
    lines = ["# Retrieval index (literal -> evidence ids)", ""]
    for source_id in ("WORK", "EDU", "OTHER"):
        text = _text(context, source_id)
        entry = index_module.resolve_section(context.index, source_id, "0.4")
        if entry is None:
            continue
        lines.append(f"## {source_id} 0.4")
        lines.append("")
        lines.append(index_module.slice_entry(text, entry).strip())
        lines.append("")
    return "\n".join(lines)


def search(context: Any, query: str) -> list[dict[str, Any]]:
    sources = {
        source_id: _text(context, source_id) for source_id in ("WORK", "EDU", "OTHER")
    }
    return index_module.search(context.index, sources, query)


# --------------------------------------------------------------------------
# Default packs per stage
# --------------------------------------------------------------------------


def _refs_in(payload: Any) -> list[str]:
    out: list[str] = []
    if isinstance(payload, dict):
        for value in payload.values():
            out += _refs_in(value)
    elif isinstance(payload, list):
        for item in payload:
            out += _refs_in(item)
    elif isinstance(payload, str) and payload.startswith("EV:"):
        out.append(payload)
    return out


def default_ids(context: Any, job_id: str, stage: int) -> list[str]:
    """The evidence pack a stage's bundle carries by default."""
    from . import artifacts as artifacts_module

    layout = context.layout
    run_id = context.run_id

    def load(name):
        return artifacts_module.load(layout, run_id, job_id, name)

    if stage == 0:
        return []
    if stage == 1:
        scout = load("scout") or {}
        triage = scout.get("triage") or {}
        return [item["ref"] for item in triage.get("core") or []]
    brief = load("brief") or {}
    if stage == 2:
        ids = _refs_in(brief.get("units")) + _refs_in(brief.get("judgment"))
        ids += _refs_in(brief.get("reserve")) + _refs_in(brief.get("stances"))
        ids += _refs_in(brief.get("distinctiveness"))
        ids += _refs_in(brief.get("outside_scout_refs"))
        for paragraph in (brief.get("letter_plan") or {}).get("paragraphs") or []:
            ids += _refs_in(paragraph.get("refs"))
        return ids
    cv_draft = load("cv_draft") or {}
    advocacy = load("advocacy_draft") or {}
    ids = list(cv_draft.get("used_evidence_refs") or [])
    ids += list(advocacy.get("used_evidence_refs") or [])
    ids += _refs_in(brief.get("units")) + _refs_in(brief.get("judgment"))
    return ids




def facet_projection(context: Any) -> str:
    """The closed facet set as a choosing surface, not the whole index."""
    facets = context.facets
    limit = facets.get("max_selected_facets", 3)
    lines = [
        f"# Personality facets (closed set; choose at most {limit})",
        "",
        "Pick a facet only when the evidence shows the behaviour. Show the "
        "behaviour as conduct in the argument; never name a facet or its "
        "label in a document.",
        "",
    ]
    for facet in facets["facets"]:
        if not facet.get("employer_expressible"):
            continue
        meaning = (facet.get("meaning") or "")[:220]
        label = facet["plain_language_label"]
        lines.append(f"- **{facet['facet_id']}** {label} - {meaning}")
    internal = [
        item["facet_id"] for item in facets["facets"]
        if not item.get("employer_expressible")
    ]
    joined = ", ".join(internal)
    lines += ["", f"Not employer-expressible: {joined}.", ""]
    return "\n".join(lines)
