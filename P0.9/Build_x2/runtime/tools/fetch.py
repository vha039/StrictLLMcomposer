"""Read-only verbatim retrieval from one run's frozen factual authorities.

DEC-14 keeps unconditional original-source access. This command is the thin
operator/model entry point for it: give it evidence IDs and it prints the
exact frozen line ranges, or give it a literal search string and it prints
the candidate IDs the frozen index and the sources' own keyword tables
route that string to.

It writes nothing. There is no fetch log, no survival marker, no decision
cache and no extra frozen input. It never ranks, scores, summarizes,
paraphrases or attaches a relevance conclusion, and it makes no network or
model call.

Usage, from the Build root:

    .\\.venv\\Scripts\\python.exe runtime/tools/fetch.py --run <reference> \\
        --ids "EV:WORK#023-4-4-...,EV:WORK#025-4-6-..."
    .\\.venv\\Scripts\\python.exe runtime/tools/fetch.py --run <reference> \\
        --search "gevinst"
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

if __package__ in (None, ""):  # direct script execution
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from jobbsok import evidence_index as index_module
from jobbsok import retrieval
from jobbsok.errors import ConfigurationError, JobError
from jobbsok.manifest import FrozenRunAssets, load_manifest, require_intact
from jobbsok.paths import Layout

SEPARATOR = "-" * 72


def _authority_text(assets: FrozenRunAssets, source_id: str) -> tuple[Path, str]:
    return retrieval.authority_text(assets, source_id)


def _emit(text: str) -> None:
    sys.stdout.buffer.write(text.encode("utf-8"))


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="fetch.py",
        description="Verbatim read-only retrieval from a run's frozen authorities.",
    )
    parser.add_argument("--run", required=True, help="Run reference.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--ids",
        help="One comma-separated string of evidence IDs, returned in request order.",
    )
    group.add_argument("--search", help="Literal, case-insensitive search string.")
    parser.add_argument("--with-context", action="store_true", help="Append digest and source boundaries to --ids output.")
    args = parser.parse_args(argv)
    if args.with_context and args.ids is None:
        parser.error("--with-context is valid only with --ids")

    layout = Layout.discover()
    manifest = load_manifest(layout, args.run)
    require_intact(layout, manifest)
    assets = FrozenRunAssets(layout, manifest)
    index = assets.json("evidence_index")

    if args.search is not None:
        sources = {
            source_id: _authority_text(assets, source_id)[1]
            for source_id in manifest["frozen_inputs"]["authorities"]
        }
        hits = index_module.search(index, sources, args.search)
        if not hits:
            _emit(f"No frozen entry matches {args.search!r}.\n")
            return 0
        for hit in hits:
            _emit(f"{hit['evidence_id']}  [{hit['source_id']}]  {hit['heading']}\n")
        return 0

    requested = [item.strip() for item in args.ids.split(",")]
    requested = [item for item in requested if item]
    if not requested:
        raise JobError("--ids was empty after stripping whitespace.")

    entries = []
    for evidence_id in requested:
        entry = index_module.resolve(index, evidence_id)
        if entry is None:
            raise JobError(
                f"{evidence_id!r} does not resolve in this run's frozen evidence index."
            )
        entries.append(entry)
    if args.with_context:
        _emit(retrieval.with_context(index, assets, entries))
        return 0

    cache: dict[str, tuple[Path, str]] = {}
    for evidence_id, entry in zip(requested, entries):
        source_id = entry["source_id"]
        if source_id not in cache:
            cache[source_id] = retrieval.authority_text(assets, source_id)
        path, text = cache[source_id]
        # Framing only. The separators and this header are not part of the
        # claimed source span.
        _emit(
            f"{SEPARATOR}\n{evidence_id}\n{path}\n"
            f"lines {entry['line_start']}-{entry['line_end']}\n{SEPARATOR}\n"
        )
        _emit(index_module.slice_entry(text, entry))
        _emit("\n")
    return 0


def main() -> int:
    try:
        return run()
    except (ConfigurationError, JobError) as exc:
        print(f"{type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
