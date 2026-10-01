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

The maintenance pass preserves the control inventory of its input masters.
The current masters carry 17 CV controls and 6 letter controls, one per tag;
templates/template_map.json owns the current render contract.

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

from jobbsok.atomicio import TransactionDir  # noqa: E402
from jobbsok.docxfill import (  # noqa: E402
    CORE_PART,
    DOCUMENT_PART,
    W,
    _register_document_namespaces,
    build_core_properties,
    control_inventory,
    normalized,
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
STYLES_PART = "word/styles.xml"

EN_DASH = "–"


# --------------------------------------------------------------------------
# Typography, emphasis and dash tables
# --------------------------------------------------------------------------
#
# ISS-01 to ISS-04: the pilot CV renders body prose at 9 pt because every
# generated paragraph inherits the master's *inline* w:sz, while the letter
# body carries no inline size and inherits styles.xml Normal at 10.5 pt. One
# mechanism alone would therefore be silently inert, so both are set here.
#
# The scale is five tiers -- 8, 10, 12, 14 and 24 pt, i.e. 16, 20, 24, 28 and
# 48 half-points -- plus one retained exception: the letter's Title style stays
# at 40 half-points (20 pt) for the subject line.
#
# The table is keyed by POSITION, never by value. A value map is not
# idempotent and is not even correct once: the same current value maps to two
# different targets (20 -> 28 for headings but -> 24 for the role line; 18 ->
# 24 for body zones but -> 20 for subordinate ones; 19 -> 24 for record titles
# but -> 20 for the two content zones). Anchors are SDT tags for the 23
# controls and transform-invariant visible-text substrings for the static
# furniture -- each verified to match exactly one paragraph, and each stopping
# short of the dash the same pass rewrites, which is what makes a second run a
# no-op.
#
# Run specs are (current half-points, target half-points, drop w:b, drop
# w:color), one per w:r in document order including runs nested in inline
# SDTs. None/None means the run is style-driven and deliberately untouched.
# No w:sz element is ever created: every run that changes size already owns
# one. w:szCs is never read, written or created -- both masters have zero.

_KEEP = (False, False)
_STRIP = (True, True)

#: CV_MASTER.docx -- all 35 body paragraphs, 41 runs.
CV_PARAGRAPHS = [
    (("text", "VEGARD HÅLAND"), [(49, 48, *_KEEP)]),
    (("sdt", "CV_FUNCTIONAL_IDENTITY", 0), [(20, 28, *_KEEP)]),
    (("sdt", "CV_VALUE_PROPOSITION", 0), [(18, 24, *_KEEP)]),
    (("text", "Oslo | +47"), [(17, 20, *_KEEP)]),
    (("text", "Profil"), [(20, 28, *_KEEP)]),
    (("sdt", "CV_PROFILE", 0), [(18, 24, *_KEEP)]),
    (("sdt", "CV_CORE_COMPETENCE", 0), [(18, 24, *_KEEP)]),
    (("sdt", "CV_TOOLS_METHODS", 0), [(18, 24, *_KEEP)]),
    (("text", "Yrkeserfaring"), [(20, 28, *_KEEP)]),
    (("text", "Rådgiver Økonomi og IKT"), [(20, 24, *_KEEP), (17, 20, *_KEEP)]),
    (("text", "Direktørens stab"), [(18, 20, *_KEEP), (17, 20, *_KEEP)]),
    (("sdt", "CV_CURRENT_ROLE_TOP_EVIDENCE", 0), [(18, 24, *_KEEP)]),
    (("sdt", "CV_SELECTED_EVIDENCE_HEADING", 0), [(18, 24, *_KEEP)]),
    (("sdt", "CV_SELECTED_EVIDENCE", 0), [(18, 24, *_KEEP)]),
    (("text", "Barne- og ungdomsklinikken"), [(18, 20, *_KEEP), (17, 20, *_KEEP)]),
    (("sdt", "CV_EARLY_ROLE_EVIDENCE", 0), [(18, 24, *_KEEP)]),
    (("text", "Utdanning"), [(20, 28, *_KEEP)]),
    (("text", "Masterprogram i kunstig intelligens"),
     [(19, 24, *_KEEP), (17, 20, *_KEEP)]),
    (("text", "Pågående."), [(17, 20, *_KEEP)]),
    (("text", "Master i samfunnsøkonomi"), [(19, 24, *_KEEP), (17, 20, *_KEEP)]),
    (("sdt", "CV_RELEVANT_MASTER_SUBJECTS", 0), [(17, 20, *_KEEP)]),
    (("text", "Bachelor i samfunnsøkonomi"), [(19, 24, *_KEEP), (17, 20, *_KEEP)]),
    # ISS-04: a content zone that inherited record-title run properties.
    (("sdt", "CV_RELEVANT_BACHELOR_SUBJECTS", 0), [(19, 20, *_STRIP)]),
    (("sdt", "CV_SUPPORT_SECTION_1", 0), [(20, 28, *_KEEP)]),
    (("sdt", "CV_SUPPORT_SECTION_1", 1), [(18, 20, *_KEEP)]),
    (("sdt", "CV_SUPPORT_SECTION_2", 0), [(20, 28, *_KEEP)]),
    (("sdt", "CV_SUPPORT_SECTION_2", 1), [(18, 20, *_KEEP)]),
    (("sdt", "CV_SUPPORT_SECTION_3", 0), [(20, 28, *_KEEP)]),
    (("sdt", "CV_SUPPORT_SECTION_3", 1), [(18, 20, *_KEEP)]),
    (("sdt", "CV_OPTIONAL_PREVIOUS_EXPERIENCE", 0), [(20, 28, *_KEEP)]),
    # ISS-04, the second one: TIDLIGERE ERFARING content.
    (("sdt", "CV_OPTIONAL_PREVIOUS_EXPERIENCE", 1), [(19, 20, *_STRIP)]),
    (("sdt", "CV_OPTIONAL_TRUST", 0), [(20, 28, *_KEEP)]),
    (("sdt", "CV_OPTIONAL_TRUST", 1), [(18, 20, *_KEEP)]),
    (("sdt", "CV_OPTIONAL_LANGUAGES", 0), [(20, 28, *_KEEP)]),
    (("sdt", "CV_OPTIONAL_LANGUAGES", 1), [(18, 20, *_KEEP)]),
]

#: APPLICATION_MASTER.docx -- all 7 body paragraphs, 5 sized runs.
#: Paragraphs 5 to 7 are style-driven (Title, Normal) and keep no inline size.
LETTER_PARAGRAPHS = [
    (("sdt", "APP_EMPLOYER", 0), [(17, 20, *_KEEP)]),
    (("sdt", "APP_UNIT_OPTIONAL", 0), [(17, 20, *_KEEP)]),
    (("text", "Oslo,"), [(17, 20, *_KEEP), (17, 20, *_KEEP)]),
    (("sdt", "APP_REFERENCE_OPTIONAL", 0), [(17, 20, *_KEEP)]),
    (("text", "Søknad"), [(None, None, *_KEEP), (None, None, *_KEEP)]),
    (("sdt", "APPLICATION_BODY", 0), [(None, None, *_KEEP)]),
    (("text", "Med vennlig hilsen"), [(None, None, *_KEEP)]),
]

#: Applied paragraph styles only: (styleId, current half-points, target).
#: The letter's Title is deliberately absent -- it stays at 40 (20 pt).
#: Latent unapplied styles, docDefaults and stylesWithEffects.xml are untouched.
CV_STYLES = [("Normal", 18, 24), ("ListBullet", 18, 24), ("Heading1", 20, 28)]
LETTER_STYLES = [("Normal", 21, 24)]

#: Outcome D: static furniture mirroring the CV_BASELINE edits, keyed to the
#: same paragraph anchors. Unit names take a comma, because a hyphen there
#: would itself be the clause-dividing hyphen outcome D prohibits. Every
#: replacement's output contains no en dash, which is what makes the pass
#: idempotent. The compound hyphen in "Barne- og" is preserved.
CV_DASHES = [
    (("text", "Rådgiver Økonomi og IKT"),
     [("03.2023" + EN_DASH + "d.d.", "03.2023-d.d.")]),
    (("text", "Direktørens stab"),
     [("Direktørens stab " + EN_DASH + " Analyseavdelingen",
       "Direktørens stab, Analyseavdelingen"),
      ("12.2023" + EN_DASH + "d.d.", "12.2023-d.d.")]),
    (("text", "Barne- og ungdomsklinikken"),
     [("Barne- og ungdomsklinikken " + EN_DASH + " Stab",
       "Barne- og ungdomsklinikken, Stab"),
      ("03.2023" + EN_DASH + "11.2023", "03.2023-11.2023")]),
    (("text", "Masterprogram i kunstig intelligens"),
     [("2024" + EN_DASH + "d.d.", "2024-d.d.")]),
    (("text", "Master i samfunnsøkonomi"),
     [("2020" + EN_DASH + "2022", "2020-2022")]),
    (("text", "Bachelor i samfunnsøkonomi"),
     [("2017" + EN_DASH + "2020", "2017-2020")]),
]
LETTER_DASHES = [
    (("text", "Søknad"), [("Søknad " + EN_DASH + " ", "Søknad: ")]),
]


class MasterRefusal(RuntimeError):
    """One master failed validation; nothing may be written for either."""

    def __init__(self, master: str, problems: list[str]) -> None:
        super().__init__(f"{master}: {len(problems)} problem(s)")
        self.master = master
        self.problems = problems


def _body_paragraphs(root: ET.Element) -> list[ET.Element]:
    body = root.find(f"{W}body")
    return list(body.iter(f"{W}p")) if body is not None else []


def _paragraph_text(paragraph: ET.Element) -> str:
    """Visible text, normalized the way static_baseline_assertions compares."""
    pieces = []
    for node in paragraph.iter():
        if node.tag == f"{W}t":
            pieces.append(node.text or "")
        elif node.tag in (f"{W}tab", f"{W}br", f"{W}cr"):
            pieces.append(" ")
    return normalized("".join(pieces))


def _resolve_anchors(root, table, problems):
    """Map every table row to a body-paragraph index, or record why not."""
    paragraphs = _body_paragraphs(root)
    texts = [_paragraph_text(p) for p in paragraphs]

    by_tag: dict[str, list[ET.Element]] = {}
    for sdt in root.iter(f"{W}sdt"):
        properties = sdt.find(f"{W}sdtPr")
        tag = None if properties is None else properties.find(f"{W}tag")
        if tag is not None and tag.get(f"{W}val") is not None:
            by_tag.setdefault(tag.get(f"{W}val"), []).append(sdt)

    # For an inline control the paragraph is the one containing it.
    owner: dict[int, int] = {}
    for index, paragraph in enumerate(paragraphs):
        for sdt in paragraph.iter(f"{W}sdt"):
            owner.setdefault(id(sdt), index)

    resolved: list[int | None] = []
    for anchor in (row[0] for row in table):
        if anchor[0] == "text":
            needle = normalized(anchor[1])
            hits = [i for i, text in enumerate(texts) if needle in text]
            if len(hits) != 1:
                problems.append(
                    f"text anchor {anchor[1]!r} matched {len(hits)} paragraphs; "
                    "exactly one is required"
                )
                resolved.append(None)
                continue
            resolved.append(hits[0])
        else:
            _, tag, ordinal = anchor
            matches = by_tag.get(tag, [])
            if len(matches) != 1:
                problems.append(
                    f"content control {tag!r} appears {len(matches)} times; "
                    "exactly one is required"
                )
                resolved.append(None)
                continue
            inner = list(matches[0].iter(f"{W}p"))
            if inner:
                if ordinal >= len(inner):
                    problems.append(
                        f"control {tag!r} holds {len(inner)} paragraph(s); "
                        f"the table asks for index {ordinal}"
                    )
                    resolved.append(None)
                    continue
                resolved.append(paragraphs.index(inner[ordinal]))
            elif id(matches[0]) in owner:
                resolved.append(owner[id(matches[0])])
            else:
                problems.append(f"inline control {tag!r} has no enclosing paragraph")
                resolved.append(None)

    known = [i for i in resolved if i is not None]
    if not problems and sorted(known) != list(range(len(paragraphs))):
        problems.append(
            f"the table resolves to {sorted(known)} but the body holds "
            f"{len(paragraphs)} paragraphs; every one must be claimed exactly once"
        )
    return paragraphs, resolved


def _plan_typography(paragraphs, resolved, table, problems):
    """Validate every run against the table. Returns queued mutations."""
    mutations = []
    visited = 0
    for (anchor, specs), index in zip(table, resolved):
        if index is None:
            continue
        where = anchor[1]
        runs = list(paragraphs[index].iter(f"{W}r"))
        if len(runs) != len(specs):
            problems.append(
                f"{where!r}: {len(runs)} run(s) present, table declares {len(specs)}"
            )
            continue
        for run, (now, target, drop_bold, drop_color) in zip(runs, specs):
            properties = run.find(f"{W}rPr")
            size = None if properties is None else properties.find(f"{W}sz")
            if target is None:
                if size is not None:
                    problems.append(
                        f"{where!r}: run declared style-driven but carries "
                        f"w:sz {size.get(f'{W}val')!r}"
                    )
                continue
            if size is None:
                problems.append(f"{where!r}: expected w:sz {now}, found none")
                continue
            visited += 1
            value = size.get(f"{W}val")
            if value not in (str(now), str(target)):
                problems.append(
                    f"{where!r}: w:sz is {value!r}; expected {now} (unconverted) "
                    f"or {target} (already converted)"
                )
                continue
            if value != str(target):
                mutations.append(("set", size, str(target)))
            for name, drop in ((f"{W}b", drop_bold), (f"{W}color", drop_color)):
                if not drop:
                    continue
                element = properties.find(name)
                if element is not None:
                    mutations.append(("remove", properties, element))
    return mutations, visited


def _plan_dashes(paragraphs, resolved, table, dash_table, problems):
    index_by_anchor = {anchor: index for (anchor, _), index in zip(table, resolved)}
    mutations = []
    for anchor, replacements in dash_table:
        index = index_by_anchor.get(anchor)
        if index is None:
            problems.append(f"dash anchor {anchor!r} did not resolve")
            continue
        nodes = list(paragraphs[index].iter(f"{W}t"))
        for old, new in replacements:
            hits = [node for node in nodes if old in (node.text or "")]
            if len(hits) == 1:
                mutations.append(("text", hits[0], (old, new)))
            elif not hits and any(new in (node.text or "") for node in nodes):
                continue  # already converted; a second run is a no-op
            else:
                problems.append(
                    f"{anchor[1]!r}: {old!r} matched {len(hits)} text node(s) and "
                    f"{new!r} is not already present"
                )
    return mutations


def _plan_styles(root, style_table, problems):
    by_id: dict[str, list[ET.Element]] = {}
    for style in root.findall(f"{W}style"):
        by_id.setdefault(style.get(f"{W}styleId"), []).append(style)
    mutations = []
    for style_id, now, target in style_table:
        matches = by_id.get(style_id, [])
        if len(matches) != 1:
            problems.append(
                f"style {style_id!r} appears {len(matches)} times; one is required"
            )
            continue
        properties = matches[0].find(f"{W}rPr")
        size = None if properties is None else properties.find(f"{W}sz")
        if size is None:
            problems.append(f"style {style_id!r} carries no w:sz")
            continue
        value = size.get(f"{W}val")
        if value not in (str(now), str(target)):
            problems.append(
                f"style {style_id!r}: w:sz is {value!r}; expected {now} or {target}"
            )
            continue
        if value != str(target):
            mutations.append(("set", size, str(target)))
    return mutations


def _commit(mutations, stats, key):
    for kind, element, argument in mutations:
        if kind == "set":
            element.set(f"{W}val", argument)
        elif kind == "remove":
            element.remove(argument)
        else:
            old, new = argument
            element.text = (element.text or "").replace(old, new, 1)
        stats[key] += 1
    return len(mutations)


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
    """Rewrite one master, preserving every part not explicitly changed.

    Every anchor is resolved and every run, style and dash validated before a
    single element is mutated, and each pass queues its mutations rather than
    applying them. A refusal therefore leaves the parsed tree untouched and
    nothing is written -- see MasterRefusal and main().
    """
    stats = {"parts_reordered": 0, "property_blocks_fixed": 0,
             "font_refs_retargeted": 0, "core_properties_rewritten": 0,
             "forced_page_breaks_removed": 0,
             "typography_normalizations": 0, "dash_normalizations": 0}
    is_cv = master.name == "CV_MASTER.docx"
    paragraph_table = CV_PARAGRAPHS if is_cv else LETTER_PARAGRAPHS
    dash_table = CV_DASHES if is_cv else LETTER_DASHES
    style_table = CV_STYLES if is_cv else LETTER_STYLES
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
                changed = 0

                if item.filename == DOCUMENT_PART:
                    problems: list[str] = []
                    paragraphs, resolved = _resolve_anchors(
                        root, paragraph_table, problems
                    )
                    typography, visited = _plan_typography(
                        paragraphs, resolved, paragraph_table, problems
                    )
                    dashes = _plan_dashes(
                        paragraphs, resolved, paragraph_table, dash_table, problems
                    )
                    present = sum(1 for _ in root.iter(f"{W}sz"))
                    if not problems and visited != present:
                        problems.append(
                            f"the table visited {visited} w:sz element(s) but the "
                            f"part holds {present}; coverage must be total"
                        )
                    if problems:
                        raise MasterRefusal(master.name, problems)
                    changed += _commit(
                        typography, stats, "typography_normalizations"
                    )
                    changed += _commit(dashes, stats, "dash_normalizations")
                    # Nothing was inserted, only w:val rewritten and two
                    # elements dropped, so ECMA-376 child order must still hold.
                    if reorder_properties(root):
                        raise MasterRefusal(
                            master.name,
                            ["the typography pass disturbed ECMA-376 child order"],
                        )
                elif item.filename == STYLES_PART:
                    problems = []
                    styles = _plan_styles(root, style_table, problems)
                    if problems:
                        raise MasterRefusal(master.name, problems)
                    changed += _commit(
                        styles, stats, "typography_normalizations"
                    )

                if fixed:
                    stats["property_blocks_fixed"] += fixed
                    stats["parts_reordered"] += 1
                if fixed or changed:
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
    if not args.check:
        archive.mkdir(parents=True, exist_ok=True)

    # Two phases: validate and stage BOTH masters, then promote both or
    # neither. Promoting the CV before the letter has even been opened would
    # let a letter-side refusal leave a new CV beside an old letter -- a mixed
    # pair that must never reach preflight or a render.
    names = ("CV_MASTER.docx", "APPLICATION_MASTER.docx")
    staged_pairs: list[tuple[Path, Path]] = []
    failed = False

    with TransactionDir(
        layout.templates,
        prefix="prepare-masters",
        inherit_parent_permissions=True,
    ) as workspace:
        for name in names:
            master = layout.templates / name
            staged = workspace / name
            before = control_inventory(master)

            original_copy = archive / name
            if not original_copy.exists() and not args.check:
                shutil.copy2(master, original_copy)

            print(f"{name}")
            try:
                stats = prepare(master, staged)
            except MasterRefusal as refusal:
                print("   REFUSING to write:")
                for problem in refusal.problems:
                    print(f"     - {problem}")
                failed = True
                continue
            except RuntimeError as exc:
                print(f"   REFUSING to write: {exc}")
                failed = True
                continue

            after = control_inventory(staged)
            staged_pairs.append((staged, master))

            print(f"   property blocks reordered : {stats['property_blocks_fixed']} "
                  f"in {stats['parts_reordered']} part(s)")
            print(f"   font references retargeted: {stats['font_refs_retargeted']}")
            print(f"   forced page breaks removed: "
                  f"{stats['forced_page_breaks_removed']}")
            print(f"   typography normalizations : "
                  f"{stats['typography_normalizations']}")
            print(f"   dash normalizations       : {stats['dash_normalizations']}")
            print(f"   core.xml rewritten canonically: "
                  f"{bool(stats['core_properties_rewritten'])}")
            print(f"   control contract preserved: {before == after} "
                  f"({sum(before.values())} controls)")

            if before != after:
                print("   REFUSING to write: the control contract changed.")
                failed = True

        if failed:
            print("\nNo master was modified: both are written together or neither is.")
            return 1

        if args.check:
            return 0

        for staged, master in staged_pairs:
            staged.replace(master)
            print(f"written: templates/{master.name} "
                  f"(P0.7 original archived under evidence/gates/GATE-02/)")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
