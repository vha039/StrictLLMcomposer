"""Lean deterministic evidence index over the three factual authorities.

DEC-14 / Contract 11.1. Permitted purposes: source navigation,
reference-existence checks, integrity/provenance coordinates, and optional
source-stated markers copied literally.

What this generator deliberately does NOT do, because the specification
forbids it: rank, score, summarize, infer fit, infer truth, filter by
relevance, require manual curation, become a factual carrier, or assert an
exhaustive byte partition (DEC-34). It processes the full source structure
without relevance filtering, and direct source access stays unconditional
even where a passage has no convenient granular entry.

Address syntax is implementation freedom (DEC-34 residue). The chosen form
is:

    EV:WORK#file                   the mandatory per-authority root entry
    EV:WORK#preamble               text before the first heading
    EV:WORK#004-ous-kjerne         the 4th heading in document order

The ordinal makes duplicate headings unambiguous; the slug keeps the
reference readable to the human who has to audit it and to the model that
has to pick it. The EV: prefix is what keeps this namespace visibly
separate from the BL: mechanical baseline namespace (ACC-08).
"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from typing import Any

from .errors import ConfigurationError, ValidationResult
from .hashing import sha256_bytes, sha256_file

INDEX_VERSION = "0.9.0"
GENERATOR_VERSION = "evidence_index/1.0"

#: The three candidate factual authorities (INV-03). Exactly these.
SOURCE_FILES: dict[str, str] = {
    "WORK": "Work_experience.md",
    "EDU": "Education.md",
    "OTHER": "Other_high_value_information.md",
}

_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
_FENCE = re.compile(r"^\s*(```|~~~)")
#: Identifiers the sources themselves write. Copied literally, never
#: inferred and never invented.
_SOURCE_STATED_ID = re.compile(r"\b(?:CLM|EDU|PRJ|EMP|OHV)-[A-Z0-9]+(?:-[A-Z0-9]+)*\b")

_SLUG_MAX = 40


def slugify(text: str) -> str:
    """Deterministic ASCII slug. Norwegian letters fold predictably."""
    folded = unicodedata.normalize("NFKD", text)
    folded = folded.replace("ø", "o").replace("Ø", "O")
    folded = folded.replace("æ", "ae").replace("Æ", "AE")
    folded = folded.replace("å", "a").replace("Å", "A")
    ascii_text = folded.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)[:_SLUG_MAX].strip("-")
    return slug or "section"


def _headings(lines: list[str]) -> list[tuple[int, int, str]]:
    """Return (line_number, level, text) for every ATX heading.

    Fenced blocks are skipped so a '# comment' inside a code fence is not
    mistaken for structure.
    """
    found: list[tuple[int, int, str]] = []
    fence: str | None = None
    for number, line in enumerate(lines, start=1):
        fence_match = _FENCE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        if fence is not None:
            continue
        match = _HEADING.match(line)
        if match:
            found.append((number, len(match.group(1)), match.group(2)))
    return found


def _span_text(lines: list[str], start: int, end: int) -> str:
    return "\n".join(lines[start - 1 : end])


def _stated_ids(text: str) -> list[str]:
    seen: list[str] = []
    for match in _SOURCE_STATED_ID.findall(text):
        if match not in seen:
            seen.append(match)
    return seen


def build_index(authorities_dir: Path) -> dict[str, Any]:
    """Generate the index. Identical inputs produce identical output."""
    authorities_dir = Path(authorities_dir)
    sources: list[dict[str, Any]] = []
    entries: list[dict[str, Any]] = []

    for source_id, filename in SOURCE_FILES.items():
        path = authorities_dir / filename
        if not path.is_file():
            raise ConfigurationError(f"Missing candidate factual authority: {path}")

        raw = path.read_bytes()
        text = raw.decode("utf-8")
        lines = text.split("\n")
        if lines and lines[-1] == "":
            lines.pop()

        sources.append(
            {
                "source_id": source_id,
                "path": f"authorities/{filename}",
                "sha256": sha256_file(path),
                "bytes": len(raw),
                "lines": len(lines),
            }
        )

        # Mandatory file-level root entry (Contract 11.1).
        entries.append(
            {
                "evidence_id": f"EV:{source_id}#file",
                "source_id": source_id,
                "kind": "FILE",
                "heading_path": [],
                "line_start": 1,
                "line_end": max(len(lines), 1),
                "content_sha256": sha256_bytes(raw),
                "source_stated_ids": _stated_ids(text),
            }
        )

        headings = _headings(lines)

        # Optional preamble entry. Permitted as a convenience by Contract
        # 11.1; no partition theorem is implied by its presence or absence.
        first_heading_line = headings[0][0] if headings else len(lines) + 1
        if first_heading_line > 1:
            preamble = _span_text(lines, 1, first_heading_line - 1)
            if preamble.strip():
                entries.append(
                    {
                        "evidence_id": f"EV:{source_id}#preamble",
                        "source_id": source_id,
                        "kind": "PREAMBLE",
                        "heading_path": [],
                        "line_start": 1,
                        "line_end": first_heading_line - 1,
                        "content_sha256": sha256_bytes(preamble.encode("utf-8")),
                        "source_stated_ids": _stated_ids(preamble),
                    }
                )

        # Every structurally discoverable section, in document order, with
        # no relevance filtering whatsoever.
        ancestry: list[tuple[int, str]] = []
        for ordinal, (line_number, level, heading_text) in enumerate(headings, start=1):
            while ancestry and ancestry[-1][0] >= level:
                ancestry.pop()
            heading_path = [text for _, text in ancestry] + [heading_text]
            ancestry.append((level, heading_text))

            end = (
                headings[ordinal][0] - 1 if ordinal < len(headings) else len(lines)
            )
            end = max(end, line_number)
            body = _span_text(lines, line_number, end)

            entries.append(
                {
                    "evidence_id": f"EV:{source_id}#{ordinal:03d}-{slugify(heading_text)}",
                    "source_id": source_id,
                    "kind": "SECTION",
                    "heading_path": heading_path,
                    "heading_level": level,
                    "line_start": line_number,
                    "line_end": end,
                    "content_sha256": sha256_bytes(body.encode("utf-8")),
                    "source_stated_ids": _stated_ids(body),
                }
            )

    return {
        "artifact_role": "EVIDENCE_INDEX",
        "index_version": INDEX_VERSION,
        "generator_version": GENERATOR_VERSION,
        # Present and false on purpose: no byte-partition theorem is
        # asserted and no partition test exists (DEC-34).
        "partition_claim": False,
        "sources": sources,
        "entries": entries,
    }


def check_index(index: dict[str, Any], authorities_dir: Path) -> ValidationResult:
    """Mechanical checks beyond schema shape."""
    result = ValidationResult()
    label = "evidence_index.json"

    ids = [e["evidence_id"] for e in index["entries"]]
    duplicates = sorted({i for i in ids if ids.count(i) > 1})
    if duplicates:
        result.add(
            "DEC-14", label, "entries[].evidence_id",
            "unique evidence IDs", f"duplicates: {duplicates[:5]}",
        )

    # The mandatory per-authority root entry must exist for all three.
    for source_id in SOURCE_FILES:
        if f"EV:{source_id}#file" not in ids:
            result.add(
                "DEC-14", label, f"EV:{source_id}#file",
                "one file-level root entry per authority",
                "missing",
            )

    # Source bytes must still match what the index was generated from.
    for source in index["sources"]:
        path = Path(authorities_dir) / Path(source["path"]).name
        if not path.is_file():
            result.add(
                "INV-03", label, source["path"],
                "candidate factual authority present", "missing",
            )
            continue
        actual = sha256_file(path)
        if actual != source["sha256"]:
            result.add(
                "INV-03", label, source["path"],
                f"sha256 {source['sha256']}",
                f"sha256 {actual} - regenerate the index or restore the bytes",
            )
    return result


def evidence_ids(index: dict[str, Any]) -> set[str]:
    return {entry["evidence_id"] for entry in index["entries"]}


def resolve(index: dict[str, Any], evidence_id: str) -> dict[str, Any] | None:
    for entry in index["entries"]:
        if entry["evidence_id"] == evidence_id:
            return entry
    return None


# --------------------------------------------------------------------------
# Frozen-source lookup, slicing and search (OPS O2)
#
# These helpers are data- and path-driven on purpose: the caller loads the
# run, proves integrity and resolves the frozen authority paths, then passes
# the already loaded index and those paths in. Nothing here imports manifest
# or FrozenRunAssets, so there is no reverse import and no new package layer.
# --------------------------------------------------------------------------

#: The controlled agent-maintained digest table header (SEM §5.1).
DIGEST_COLUMNS = ("Record", "Source section", "Lifecycle", "Can prove", "Live ceilings")
DIGEST_KEYS = ("record", "source_section", "lifecycle", "can_prove", "live_ceilings")

_SECTION_NUMBER = re.compile(r"^(\d+(?:\.\d+)*)\.?\s")
_RANGE = re.compile(r"^(\d+(?:\.\d+)*)\s*[\u2013\u2014-]\s*(\d+(?:\.\d+)*)$")
_PLAIN = re.compile(r"^(\d+(?:\.\d+)*)$")
_PARENTHETICAL = re.compile(r"\([^)]*\)")


def ordered_evidence_ids(index: dict[str, Any]) -> list[str]:
    """Every evidence_id in frozen index order. No filtering, ever."""
    return [entry["evidence_id"] for entry in index["entries"]]


def section_tuple(heading_text: str) -> tuple[int, ...] | None:
    """(4, 10) for '4.10 `PRJ-10` — ...'; (8,) for '8. Godkjente ...'.

    Numeric tuples, never floats and never string prefixes: 4.1 is not 4.10.
    """
    match = _SECTION_NUMBER.match(heading_text.strip())
    if not match:
        return None
    return tuple(int(part) for part in match.group(1).split("."))


def _entry_section(entry: dict[str, Any]) -> tuple[int, ...] | None:
    path = entry.get("heading_path") or []
    return section_tuple(path[-1]) if path else None


def resolve_section(
    index: dict[str, Any], source_id: str, number: str | tuple[int, ...]
) -> dict[str, Any] | None:
    """Resolve an exact section number or an existing unnumbered heading."""
    wanted = (
        tuple(int(p) for p in number.split("."))
        if isinstance(number, str) and _PLAIN.fullmatch(number) else number
    )
    for entry in index["entries"]:
        if entry.get("source_id") != source_id or entry.get("kind") != "SECTION":
            continue
        heading = (entry.get("heading_path") or [""])[-1]
        if (heading == wanted if isinstance(wanted, str)
                else _entry_section(entry) == wanted):
            return entry
    return None


def parse_section_refs(text: str) -> list[tuple[tuple[int, ...], tuple[int, ...] | None]]:
    """Parse the reference syntax the retained keyword tables actually use.

    Handles the leading reference portion before a semicolon, the section and
    double-section markers, comma-separated items, integer and decimal
    sections, and inclusive sibling ranges written with an en dash or an
    ASCII hyphen. Parenthetical course/record IDs and explanatory prose are
    not section numbers (RP-09).
    """
    head = text.split(";")[0]
    head = _PARENTHETICAL.sub(" ", head)
    head = head.replace("\u00a7\u00a7", " ").replace("\u00a7", " ")
    refs: list[tuple[tuple[int, ...], tuple[int, ...] | None]] = []
    for raw in head.split(","):
        item = raw.strip().strip("`").strip()
        if not item:
            continue
        ranged = _RANGE.match(item)
        if ranged:
            low = tuple(int(p) for p in ranged.group(1).split("."))
            high = tuple(int(p) for p in ranged.group(2).split("."))
            if len(low) == len(high) and low[:-1] == high[:-1] and low <= high:
                refs.append((low, high))
            continue
        plain = _PLAIN.match(item)
        if plain:
            refs.append((tuple(int(p) for p in plain.group(1).split(".")), None))
    return refs


def _matches_ref(
    section: tuple[int, ...] | None,
    ref: tuple[tuple[int, ...], tuple[int, ...] | None],
) -> bool:
    if section is None:
        return False
    low, high = ref
    if high is None:
        # A named section includes its existing child headings by tuple prefix.
        return section[: len(low)] == low
    depth = len(low)
    if len(section) < depth or section[: depth - 1] != low[: depth - 1]:
        return False
    return low[depth - 1] <= section[depth - 1] <= high[depth - 1]


def ids_for_refs(
    index: dict[str, Any], source_id: str, text: str
) -> list[str]:
    """Resolve one keyword-table reference cell to actual IDs, in index order."""
    refs = parse_section_refs(text)
    found: list[str] = []
    for entry in index["entries"]:
        if entry.get("source_id") != source_id or entry.get("kind") != "SECTION":
            continue
        if any(
            _matches_ref(section_tuple(heading), ref)
            for heading in entry.get("heading_path", []) for ref in refs
        ):
            found.append(entry["evidence_id"])
    return found


def _table_rows(lines: list[str]) -> list[list[str]]:
    """Rows of the first markdown table in `lines`, with escaped pipes kept."""
    rows: list[list[str]] = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            if rows:
                break
            continue
        if set(stripped) <= set("|-: "):
            continue
        cells: list[str] = []
        current: list[str] = []
        i = 1
        body = stripped[1:-1] if stripped.endswith("|") else stripped[1:]
        while i <= len(body):
            char = body[i - 1]
            if char == "\\" and i < len(body) and body[i] == "|":
                current.append("|")
                i += 2
                continue
            if char == "|":
                cells.append("".join(current).strip())
                current = []
                i += 1
                continue
            current.append(char)
            i += 1
        cells.append("".join(current).strip())
        rows.append(cells)
    return rows


def _section_lines(text: str, entry: dict[str, Any]) -> list[str]:
    lines = text.splitlines()
    return lines[entry["line_start"] - 1 : entry["line_end"]]


def keyword_table_ids(
    index: dict[str, Any], source_id: str, text: str, query: str
) -> list[str]:
    """IDs reachable from this source's retained keyword table for `query`."""
    entry = resolve_section(index, source_id, "0.4")
    if entry is None:
        return []
    needle = query.casefold()
    found: list[str] = []
    for row in _table_rows(_section_lines(text, entry)):
        if len(row) < 2:
            continue
        if row[0].casefold().find(needle) < 0:
            continue
        for evidence_id in ids_for_refs(index, source_id, row[1]):
            if evidence_id not in found:
                found.append(evidence_id)
    return found


def search(
    index: dict[str, Any], sources: dict[str, str], query: str
) -> list[dict[str, Any]]:
    """Case-insensitive literal search. Never ranks, never scores.

    Matches existing heading_path text and source_stated_ids, combined with
    whatever each frozen section-0.4 keyword table routes the same literal to.
    Returns unique entries in frozen index order with a short heading label.
    """
    needle = query.casefold()
    hit_ids: set[str] = set()
    for entry in index["entries"]:
        haystack = " ".join(entry.get("heading_path") or [])
        stated = " ".join(entry.get("source_stated_ids") or [])
        if needle in haystack.casefold() or needle in stated.casefold():
            hit_ids.add(entry["evidence_id"])
    for source_id, text in sources.items():
        hit_ids.update(keyword_table_ids(index, source_id, text, query))
    return [
        {
            "evidence_id": entry["evidence_id"],
            "source_id": entry["source_id"],
            "heading": (entry.get("heading_path") or [""])[-1],
        }
        for entry in index["entries"]
        if entry["evidence_id"] in hit_ids
    ]


def slice_entry(text: str, entry: dict[str, Any]) -> str:
    """The verbatim inclusive line range for one entry.

    splitlines(keepends=True) preserves the source's own CRLF/LF and whether
    the span ended with a newline. No normalization, no re-joining with a
    chosen separator.
    """
    lines = text.splitlines(keepends=True)
    return "".join(lines[entry["line_start"] - 1 : entry["line_end"]])


def digest_rows(text: str, entry: dict[str, Any]) -> list[dict[str, str]]:
    """Project the controlled digest table inside one designated span.

    Finds exactly the maintained header; no whole-file semantic parsing and
    no inference. Cells are copied literally.
    """
    lines = _section_lines(text, entry)
    header_at = None
    for offset, line in enumerate(lines):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells == list(DIGEST_COLUMNS):
            header_at = offset
            break
    if header_at is None:
        return []
    rows = _table_rows(lines[header_at:])
    projected: list[dict[str, str]] = []
    for row in rows[1:]:
        if len(row) != len(DIGEST_KEYS):
            continue
        projected.append(dict(zip(DIGEST_KEYS, row)))
    return projected
