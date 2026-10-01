"""One-time master preparation: schema-order repair and font retarget.

This is an asset-preparation utility, not runtime code. It exists so the
transformation applied to the supplied P0.7 masters is reproducible and
auditable rather than a hand-edit nobody can reconstruct (DEC-30: P0.7
assets are implementation capital, adapted after inspection).

Three defects were found on the target machine and are fixed here.

GATE-02 -- Word rejects both masters as corrupted.
    Each master contains one `w:pPr` whose children are ordered
    `spacing` then `pBdr`. ECMA-376 CT_PPr requires `pBdr` before
    `spacing`. Word enforces that sequence and refuses the file; LibreOffice
    tolerates it, which is why P0.7's LibreOffice-only render verification
    never caught it (P0.7 TEST_REPORT records rendering verified through
    LibreOffice). Word's own open-and-repair produces a schema-clean file,
    confirming the diagnosis. This tool reorders `w:pPr` and `w:rPr`
    children into schema sequence across every document part.

GATE-05 -- fonts referenced by the masters are not installed.
    CV_MASTER hard-codes `DejaVu Sans` in 41 document runs and 5 style
    definitions, unembedded, and DejaVu Sans is absent from this machine.
    APPLICATION_MASTER's styles reference `Aptos`, which is also absent
    (the installed Microsoft 365 build does not register it). Both would
    silently substitute and change metrics and page balance. GATE-05
    permits changing font and template styling within the semantic and
    parseability contracts without a specification amendment.

GATE-05 -- CV_MASTER contains one unconditional page-break paragraph.
    It forces sparse and normal CVs onto a poorly balanced second page before
    the first dynamic support section. The exact generated paragraph is
    removed here without adding a page-count cap, content truncation or an
    auto-fit rule.

The control contract is deliberately untouched: the 17 CV tags and the 6
unique / 7 total letter tags must survive byte-for-byte in structure, and
the tool verifies that before writing.

Usage:
    python -m tools.prepare_masters [--check]
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from jobbsok.docxfill import (  # noqa: E402
    CORE_PART,
    W,
    _register_document_namespaces,
    build_core_properties,
    control_inventory,
    read_core_properties,
)
from jobbsok.paths import Layout  # noqa: E402

# ECMA-376 CT_PPr / CT_RPr child sequences.
PPR_ORDER = [
    "pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr",
    "widowControl", "numPr", "suppressLineNumbers", "pBdr", "shd", "tabs",
    "suppressAutoHyphens", "kinsoku", "wordWrap", "overflowPunct",
    "topLinePunct", "autoSpaceDE", "autoSpaceDN", "bidi", "adjustRightInd",
    "snapToGrid", "spacing", "ind", "contextualSpacing", "mirrorIndents",
    "suppressOverlap", "jc", "textDirection", "textAlignment",
    "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr", "sectPr",
    "pPrChange",
]
RPR_ORDER = [
    "rStyle", "rFonts", "b", "bCs", "i", "iCs", "caps", "smallCaps", "strike",
    "dstrike", "outline", "shadow", "emboss", "imprint", "noProof",
    "snapToGrid", "vanish", "webHidden", "color", "spacing", "w", "kern",
    "position", "sz", "szCs", "highlight", "u", "effect", "bdr", "shd",
    "fitText", "vertAlign", "rtl", "cs", "em", "lang", "eastAsianLayout",
    "specVanish", "oMath",
]

#: Fonts absent from the target machine -> the installed replacement.
#: Calibri is chosen because it is present on every Windows install, is a
#: humanist sans in the same family as DejaVu Sans, and has full Norwegian
#: glyph coverage. GATE-05 records the visual QA that follows.
FONT_REPLACEMENTS = {
    "DejaVu Sans": "Calibri",
    "Aptos": "Calibri",
    "Aptos Display": "Calibri",
}

TARGET_PARTS = re.compile(r"^word/(document|styles|stylesWithEffects|header\d*|footer\d*|numbering|fontTable)\.xml$")
FORCED_CV_PAGE_BREAK = b'<w:p><w:r><w:br w:type="page" /></w:r></w:p>'


def reorder_properties(root: ET.Element) -> int:
    """Sort w:pPr and w:rPr children into schema sequence. Returns fixes."""
    fixed = 0
    for container, order in ((f"{W}pPr", PPR_ORDER), (f"{W}rPr", RPR_ORDER)):
        for node in root.iter(container):
            children = list(node)
            names = [c.tag.replace(W, "") for c in children]
            known = [n for n in names if n in order]
            positions = [order.index(n) for n in known]
            if positions == sorted(positions):
                continue
            # Stable sort: unknown children keep their relative position by
            # sorting on (schema index or +inf, original index).
            decorated = [
                (order.index(n) if n in order else len(order), i, c)
                for i, (n, c) in enumerate(zip(names, children))
            ]
            decorated.sort(key=lambda t: (t[0], t[1]))
            for child in children:
                node.remove(child)
            for _, _, child in decorated:
                node.append(child)
            fixed += 1
    return fixed


def retarget_fonts(raw: bytes) -> tuple[bytes, int]:
    """Replace absent font names in attribute values only."""
    text = raw.decode("utf-8")
    replaced = 0
    for absent, present in FONT_REPLACEMENTS.items():
        for attribute in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs", "w:asciiTheme",
                          "w:hAnsiTheme", "w:name", "w:val"):
            pattern = f'{attribute}="{absent}"'
            replacement = f'{attribute}="{present}"'
            count = text.count(pattern)
            if count:
                text = text.replace(pattern, replacement)
                replaced += count
    return text.encode("utf-8"), replaced


def prepare(master: Path, output: Path) -> dict[str, int]:
    """Rewrite one master, preserving every part not explicitly changed."""
    stats = {"parts_reordered": 0, "property_blocks_fixed": 0,
             "font_refs_retargeted": 0, "core_properties_rewritten": 0,
             "forced_page_breaks_removed": 0}
    with ZipFile(master) as source:
        payload: dict[str, bytes] = {}
        for item in source.infolist():
            raw = source.read(item.filename)
            if item.filename == CORE_PART:
                # The OPC core-properties part carries the unbound-dcterms
                # artifact that makes Word reject the package. Rewriting it
                # canonically is the actual GATE-02 fix.
                payload[item.filename] = build_core_properties(
                    read_core_properties(source)
                )
                stats["core_properties_rewritten"] += 1
                continue
            if TARGET_PARTS.match(item.filename):
                if master.name == "CV_MASTER.docx" and item.filename == "word/document.xml":
                    count = raw.count(FORCED_CV_PAGE_BREAK)
                    if count > 1:
                        raise RuntimeError(
                            "CV master contains multiple forced page-break paragraphs; "
                            "refusing an ambiguous template rewrite."
                        )
                    if count == 1:
                        raw = raw.replace(FORCED_CV_PAGE_BREAK, b"", 1)
                        stats["forced_page_breaks_removed"] = 1
                raw, replaced = retarget_fonts(raw)
                stats["font_refs_retargeted"] += replaced

                open_match = re.match(rb"<\?xml[^>]*\?>\s*(<[^>]+>)", raw)
                _register_document_namespaces(raw)
                root = ET.fromstring(raw)
                fixed = reorder_properties(root)
                if fixed:
                    stats["property_blocks_fixed"] += fixed
                    stats["parts_reordered"] += 1
                    body = ET.tostring(root, encoding="utf-8", xml_declaration=False)
                    if open_match:
                        original_tag = open_match.group(1)
                        generated = re.match(rb"<[^>]+>", body)
                        if generated is not None:
                            body = original_tag + body[generated.end():]
                    raw = (
                        b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                        + body
                    )
            payload[item.filename] = raw

        output.parent.mkdir(parents=True, exist_ok=True)
        with ZipFile(output, "w", ZIP_DEFLATED) as target:
            for item in source.infolist():
                target.writestr(item, payload[item.filename])
    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="Report what would change without writing.")
    args = parser.parse_args()

    layout = Layout.discover(Path(__file__).resolve().parents[2])
    archive = layout.evidence / "gates" / "GATE-02" / "original_p07_masters"
    archive.mkdir(parents=True, exist_ok=True)

    exit_code = 0
    for name in ("CV_MASTER.docx", "APPLICATION_MASTER.docx"):
        master = layout.templates / name
        before = control_inventory(master)

        original_copy = archive / name
        if not original_copy.exists() and not args.check:
            shutil.copy2(master, original_copy)

        staged = master.with_suffix(".prepared.docx")
        stats = prepare(master, staged)
        after = control_inventory(staged)

        print(f"{name}")
        print(f"   property blocks reordered : {stats['property_blocks_fixed']} "
              f"in {stats['parts_reordered']} part(s)")
        print(f"   font references retargeted: {stats['font_refs_retargeted']}")
        print(f"   forced page breaks removed: "
              f"{stats['forced_page_breaks_removed']}")
        print(f"   core.xml rewritten canonically: "
              f"{bool(stats['core_properties_rewritten'])}")
        print(f"   control contract preserved: {before == after} "
              f"({sum(before.values())} controls)")

        if before != after:
            print("   REFUSING to write: the control contract changed.")
            staged.unlink(missing_ok=True)
            exit_code = 1
            continue
        if args.check:
            staged.unlink(missing_ok=True)
        else:
            staged.replace(master)
            print(f"   written: templates/{name} "
                  f"(P0.7 original archived under evidence/gates/GATE-02/)")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
