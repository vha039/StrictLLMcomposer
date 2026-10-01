"""Shared, read-only navigation over frozen authority text."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from . import evidence_index as index_module
from .errors import ConfigurationError
from .paths import resolve_within

MANDATORY_SOURCE_SECTIONS: tuple[tuple[str, str], ...] = (
    ("WORK", "8"), ("WORK", "10.1"), ("WORK", "10.2"),
    ("EDU", "4.2"), ("EDU", "4.3"),
    ("OTHER", "0.3"), ("OTHER", "4.5"),
)
DIGEST_SECTIONS = {"WORK": "0.3", "OTHER": "0.2", "EDU": "0.5"}


def authority_text(assets: Any, source_id: str) -> tuple[Path, str]:
    record = assets.manifest["frozen_inputs"]["authorities"].get(source_id)
    if record is None:
        raise ConfigurationError(f"{source_id!r} is not a frozen factual authority.")
    root = assets.run_dir / "frozen"
    path = resolve_within(root, root / record["path"], label="frozen authority path")
    return path, path.read_bytes().decode("utf-8")


def selected_strategy_refs(index: dict[str, Any], strategy: dict[str, Any]) -> list[str]:
    """The Stage-1 evidence selection, with the non-negotiable global boundaries."""
    refs: list[str] = []
    for item in strategy.get("evidence_plan") or []:
        refs.extend(item.get("evidence_refs") or [])
    for item in strategy.get("material_requirements") or []:
        refs.extend(item.get("evidence_refs") or [])
    for item in strategy.get("personality_facets") or []:
        refs.extend(item.get("evidence_refs") or [])
    refs.extend((strategy.get("counterfactual_route") or {}).get("evidence_refs") or [])
    for source_id, section in MANDATORY_SOURCE_SECTIONS:
        entry = index_module.resolve_section(index, source_id, section)
        if entry is not None:
            refs.append(entry["evidence_id"])
    return list(dict.fromkeys(refs))


def _passage(
    path: Path, text: str, entry: dict[str, Any], label: str, *,
    include_paths: bool = True,
) -> str:
    location = str(path) if include_paths else entry["source_id"]
    return (
        f"\n[{label}] {entry['evidence_id']}\n"
        f"{location} lines {entry['line_start']}-{entry['line_end']}\n"
        f"{index_module.slice_entry(text, entry)}"
    )


def with_context(
    index: dict[str, Any], assets: Any, entries: list[dict[str, Any]], *,
    include_paths: bool = True,
) -> str:
    """Return exact requested spans, source navigation, then global boundaries."""
    cache: dict[str, tuple[Path, str]] = {}

    def source(source_id: str) -> tuple[Path, str]:
        if source_id not in cache:
            cache[source_id] = authority_text(assets, source_id)
        return cache[source_id]

    output: list[str] = []
    for entry in entries:
        source_id = entry["source_id"]
        path, text = source(source_id)
        output.append(_passage(
            path, text, entry, "REQUESTED VERBATIM SPAN",
            include_paths=include_paths,
        ))

        digest = index_module.resolve_section(index, source_id, DIGEST_SECTIONS[source_id])
        if digest:
            for row in index_module.digest_rows(text, digest):
                resolved = index_module.resolve_section(index, source_id, row["source_section"])
                if resolved and resolved["evidence_id"] == entry["evidence_id"]:
                    for line_number, line in enumerate(text.splitlines(keepends=True), 1):
                        if not digest["line_start"] <= line_number <= digest["line_end"]:
                            continue
                        if line.lstrip().startswith("|") and line.strip().strip("|").split("|")[0].strip() == row["record"]:
                            location = str(path) if include_paths else source_id
                            output.append(
                                f"\n[NAVIGATION: matching digest row] {location} "
                                f"line {line_number}\n{line}"
                            )
                            break

        ids = entry.get("source_stated_ids") or []
        selected = set(range(entry["line_start"], entry["line_end"] + 1))
        for line_number, line in enumerate(text.splitlines(keepends=True), 1):
            if line_number in selected or not any(token in line for token in ids):
                continue
            folded = line.casefold()
            if any(term in folded for term in ("ceiling", "claim boundary", "påstandsgrense", "ikke", "uavklart", "grense")):
                location = str(path) if include_paths else source_id
                output.append(f"\n[NAVIGATION: local boundary] {location} line {line_number}\n{line}")

    for source_id, section in MANDATORY_SOURCE_SECTIONS:
        entry = index_module.resolve_section(index, source_id, section)
        if entry is not None:
            path, text = source(source_id)
            output.append(_passage(
                path, text, entry, "GLOBAL BOUNDARY VERBATIM",
                include_paths=include_paths,
            ))
    return "\n".join(output).rstrip() + "\n"
