"""OOXML content-control fill, unwrap and assert.

Contract 13.4 preserves the P0.7 sequence where actual master inspection
confirms fit:

    fill expected non-data-bound SDTs
    -> unwrap controls
    -> assert no w:sdt / transient placeholder remains
    -> validate/open DOCX

Inspection of the supplied masters confirmed the fit: CV_MASTER.docx has 17
non-data-bound SDTs (one per tag) and APPLICATION_MASTER.docx has 7 (6
unique, APP_JOB_TITLE twice); neither uses w:dataBinding or docPartObj
(GATE-02).

This is not a copy of P0.7's code. The primitives were extracted and
rebuilt on stdlib zipfile + xml.etree.ElementTree, which removes the lxml
and python-docx dependencies entirely (GATE-07). ElementTree has no
getparent(), so the unwrap step builds an explicit parent map; and because
ElementTree re-serializes namespace declarations its own way, the original
root open tag is restored verbatim so Word sees exactly the namespace set
and mc:Ignorable list the master shipped with.
"""

from __future__ import annotations

import copy
import re
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from typing import Callable, Iterator
from zipfile import ZIP_DEFLATED, ZipFile

from .errors import ConfigurationError, JobError

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "dc": "http://purl.org/dc/elements/1.1/",
    "cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
    "dcterms": "http://purl.org/dc/terms/",
}
W = f"{{{NS['w']}}}"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

DOCUMENT_PART = "word/document.xml"
CORE_PART = "docProps/core.xml"

_ROOT_OPEN = re.compile(rb"<w:document\b[^>]*>")
_XMLNS_DECL = re.compile(rb'xmlns:([A-Za-z0-9_.-]+)\s*=\s*"([^"]+)"')

for _prefix, _uri in NS.items():
    ET.register_namespace(_prefix, _uri)


def _register_document_namespaces(raw: bytes) -> None:
    """Teach ElementTree every prefix the master actually uses.

    A Word document declares far more namespaces than the four this module
    names (mc, r, wp, w14, wps, ...). Without registering them ET invents
    ns0/ns1 prefixes and hoists its own xmlns declarations to the root; the
    restored root tag then does not bind them and Word rejects the file
    with an unbound prefix. Registering every declared prefix keeps the
    serialized prefixes identical to the master's.
    """
    for prefix, uri in _XMLNS_DECL.findall(raw):
        ET.register_namespace(prefix.decode("ascii"), uri.decode("utf-8"))


def _merge_root_tag(original: bytes, generated: bytes) -> bytes:
    """Original root tag plus any xmlns declaration ET added on its own."""
    declared = {prefix for prefix, _ in _XMLNS_DECL.findall(original)}
    additions = [
        b' xmlns:%s="%s"' % (prefix, uri)
        for prefix, uri in _XMLNS_DECL.findall(generated)
        if prefix not in declared
    ]
    if not additions:
        return original
    return original[:-1] + b"".join(additions) + original[-1:]


# --------------------------------------------------------------------------
# Reading and inventory
# --------------------------------------------------------------------------

def read_document(path: Path) -> tuple[ET.Element, bytes]:
    """Return the parsed document body and its original root open tag."""
    with ZipFile(path) as archive:
        raw = archive.read(DOCUMENT_PART)
    match = _ROOT_OPEN.search(raw)
    if match is None:
        raise ConfigurationError(f"{Path(path).name} has no <w:document> root.")
    _register_document_namespaces(raw)
    return ET.fromstring(raw), match.group(0)


def iter_controls(root: ET.Element) -> Iterator[tuple[str, ET.Element]]:
    """Yield (tag_value, sdt_element) for every content control."""
    for sdt in root.iter(f"{W}sdt"):
        properties = sdt.find(f"{W}sdtPr")
        if properties is None:
            continue
        tag = properties.find(f"{W}tag")
        if tag is None:
            continue
        value = tag.get(f"{W}val")
        if value is not None:
            yield value, sdt


def control_inventory(path: Path) -> Counter[str]:
    """Count content controls by tag. The GATE-02 inventory primitive."""
    root, _ = read_document(path)
    return Counter(tag for tag, _ in iter_controls(root))


def binding_report(path: Path) -> dict[str, int]:
    """Data-binding surfaces that would make the fill technique unsafe."""
    with ZipFile(path) as archive:
        raw = archive.read(DOCUMENT_PART).decode("utf-8")
        parts = archive.namelist()
    return {
        "data_bindings": raw.count("dataBinding"),
        "doc_part_obj": raw.count("docPartObj"),
        "custom_xml_parts": sum(1 for p in parts if p.startswith("customXml/")),
    }


def require_template_contract(path: Path, expected: dict[str, int]) -> None:
    """Unknown, duplicate or missing required controls fail preflight.

    Spec 16.3: delivered documents must contain no unresolved data-bound or
    transient control, and a template contract mismatch is a preflight
    failure rather than something to ignore.
    """
    path = Path(path)
    if not path.is_file():
        raise ConfigurationError(f"Missing Word master: {path}")
    actual = control_inventory(path)
    if actual != Counter(expected):
        missing = {t: n for t, n in expected.items() if actual.get(t, 0) != n}
        unknown = {t: n for t, n in actual.items() if t not in expected}
        raise ConfigurationError(
            f"{path.name} content-control contract mismatch.\n"
            f"          expected: {dict(sorted(expected.items()))}\n"
            f"          observed: {dict(sorted(actual.items()))}\n"
            f"          missing/wrong count: {missing or '{}'}\n"
            f"          unknown controls:    {unknown or '{}'}"
        )


# --------------------------------------------------------------------------
# Filling
# --------------------------------------------------------------------------

def _set_run_text(run: ET.Element, text: str) -> None:
    """Replace a run's children with text, preserving its run properties."""
    properties = run.find(f"{W}rPr")
    for child in list(run):
        if child is not properties:
            run.remove(child)
    for line_index, line in enumerate(text.split("\n")):
        if line_index:
            run.append(ET.Element(f"{W}br"))
        for piece_index, piece in enumerate(line.split("\t")):
            if piece_index:
                run.append(ET.Element(f"{W}tab"))
            node = ET.Element(f"{W}t")
            if piece.startswith(" ") or piece.endswith(" "):
                node.set(XML_SPACE, "preserve")
            node.text = piece
            run.append(node)


def _set_paragraph_text(paragraph: ET.Element, text: str) -> None:
    """Replace paragraph content with one run, keeping paragraph properties."""
    template_run = paragraph.find(f".//{W}r")
    properties = paragraph.find(f"{W}pPr")
    for child in list(paragraph):
        if child is not properties:
            paragraph.remove(child)
    run = copy.deepcopy(template_run) if template_run is not None else ET.Element(f"{W}r")
    _set_run_text(run, text)
    paragraph.append(run)


def fill_inline(root: ET.Element, tag: str, value: str) -> int:
    """Fill every inline control carrying `tag`. Returns how many were filled."""
    matches = [sdt for found, sdt in iter_controls(root) if found == tag]
    if not matches:
        raise ConfigurationError(f"Missing inline content control: {tag}")
    for sdt in matches:
        content = sdt.find(f"{W}sdtContent")
        if content is None:
            raise ConfigurationError(f"Control {tag} has no sdtContent.")
        children = list(content)
        run = copy.deepcopy(children[0]) if children else ET.Element(f"{W}r")
        if run.tag != f"{W}r":
            raise ConfigurationError(
                f"Control {tag} is not inline: its content starts with "
                f"{run.tag.rsplit('}', 1)[-1]!r}."
            )
        _set_run_text(run, value)
        for child in list(content):
            content.remove(child)
        content.append(run)
    return len(matches)


def fill_block(root: ET.Element, tag: str, items: list[tuple[int, str]]) -> None:
    """Fill a block control with (template_paragraph_index, text) pairs.

    An empty `items` list clears the control entirely, which is how an
    optional zone renders as absent rather than as a leftover placeholder.
    """
    matches = [sdt for found, sdt in iter_controls(root) if found == tag]
    if len(matches) != 1:
        raise ConfigurationError(
            f"Expected exactly one block content control {tag}; found {len(matches)}."
        )
    content = matches[0].find(f"{W}sdtContent")
    if content is None:
        raise ConfigurationError(f"Control {tag} has no sdtContent.")
    templates = [child for child in content if child.tag == f"{W}p"]
    if not templates:
        raise ConfigurationError(f"Control {tag} has no paragraph template.")

    rendered: list[ET.Element] = []
    for template_index, text in items:
        paragraph = copy.deepcopy(templates[min(template_index, len(templates) - 1)])
        _set_paragraph_text(paragraph, text)
        rendered.append(paragraph)

    for child in list(content):
        content.remove(child)
    for paragraph in rendered:
        content.append(paragraph)


# --------------------------------------------------------------------------
# Unwrap and assert
# --------------------------------------------------------------------------

def unwrap_content_controls(root: ET.Element) -> int:
    """Replace every w:sdt with its sdtContent children, innermost first.

    ElementTree has no parent pointers, so the parent map is rebuilt after
    each removal pass. Returns how many controls were unwrapped.
    """
    removed = 0
    while True:
        parents = {child: parent for parent in root.iter() for child in parent}
        controls = [e for e in root.iter(f"{W}sdt") if e in parents]
        if not controls:
            break
        # Innermost first: a control whose subtree holds no other control.
        target = None
        for control in controls:
            if not any(
                other is not control for other in control.iter(f"{W}sdt")
            ):
                target = control
                break
        if target is None:
            target = controls[-1]
        parent = parents[target]
        index = list(parent).index(target)
        content = target.find(f"{W}sdtContent")
        parent.remove(target)
        if content is not None:
            for offset, child in enumerate(list(content)):
                parent.insert(index + offset, child)
        removed += 1
    return removed


def repair_empty_table_cells(root: ET.Element) -> int:
    """Give back a paragraph to any table cell the unwrap step emptied.

    ECMA-376 CT_Tc requires a table cell to contain at least one block-level
    element. An optional block control that is the sole content of a cell
    breaks that: filling it with no items clears its sdtContent, and unwrapping
    then splices in zero children, leaving a `w:tc` holding only `w:tcPr`.
    Word refuses the whole package with "The file appears to be corrupted",
    while ElementTree parses it happily -- which is why nothing upstream
    noticed.

    In this template that is the letter's reference cell, whenever a vacancy
    carries no reference number. The CV master has no tables, so this is a
    no-op there. Returns how many cells were repaired.
    """
    repaired = 0
    for cell in root.iter(f"{W}tc"):
        if any(child.tag in (f"{W}p", f"{W}tbl") for child in cell):
            continue
        cell.append(ET.Element(f"{W}p"))
        repaired += 1
    return repaired


def assert_no_controls(root: ET.Element, label: str) -> None:
    """Fail if any w:sdt survived the unwrap step."""
    remaining = [tag for tag, _ in iter_controls(root)]
    if remaining or any(True for _ in root.iter(f"{W}sdt")):
        raise JobError(
            f"{label} still contains content controls after unwrap: "
            f"{sorted(set(remaining)) or '(untagged w:sdt)'}"
        )


# --------------------------------------------------------------------------
# Writing
# --------------------------------------------------------------------------

def write_filled_docx(
    template_path: Path,
    output_path: Path,
    edit_document: Callable[[ET.Element], None],
    *,
    title: str,
    subject: str,
    creator: str,
) -> None:
    """Fill, unwrap, assert, and write a new DOCX.

    Only word/document.xml and docProps/core.xml are rewritten; every other
    zip part is streamed through byte-identical, so styles, fonts, headers,
    numbering and relationships stay exactly as the master shipped them.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with ZipFile(template_path) as source:
        raw = source.read(DOCUMENT_PART)
        match = _ROOT_OPEN.search(raw)
        if match is None:
            raise ConfigurationError(
                f"{Path(template_path).name} has no <w:document> root."
            )
        original_open_tag = match.group(0)
        _register_document_namespaces(raw)

        root = ET.fromstring(raw)
        edit_document(root)
        unwrap_content_controls(root)
        repair_empty_table_cells(root)
        assert_no_controls(root, output_path.name)

        body = ET.tostring(root, encoding="utf-8", xml_declaration=False)
        # Restore the master's own root open tag so the namespace set and
        # mc:Ignorable list Word expects survive the round trip, keeping any
        # declaration ET added that the original did not carry.
        generated = re.match(rb"<[^>]+>", body)
        if generated is None:
            raise ConfigurationError("Serialized document has no root tag.")
        root_tag = _merge_root_tag(original_open_tag, generated.group(0))
        document_bytes = (
            b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            + root_tag
            + body[generated.end():]
        )

        core_bytes = _core_properties(source, title, subject, creator)

        with ZipFile(output_path, "w", ZIP_DEFLATED) as target:
            for item in source.infolist():
                if item.filename == DOCUMENT_PART:
                    target.writestr(item, document_bytes)
                elif item.filename == CORE_PART and core_bytes is not None:
                    target.writestr(item, core_bytes)
                else:
                    target.writestr(item, source.read(item.filename))


#: Canonical OPC core-properties field order and prefix binding.
_CORE_FIELDS = [
    ("dc", "title"), ("dc", "subject"), ("dc", "creator"),
    ("cp", "keywords"), ("dc", "description"), ("cp", "lastModifiedBy"),
    ("cp", "revision"), ("dcterms", "created"), ("dcterms", "modified"),
    ("cp", "category"),
]
_CORE_NS = {
    "cp": NS["cp"],
    "dc": NS["dc"],
    "dcterms": NS["dcterms"],
    "dcmitype": "http://purl.org/dc/dcmitype/",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance",
}


def read_core_properties(archive: ZipFile) -> dict[str, str]:
    """Read core properties as {local_name: text}, ignoring prefixes."""
    if CORE_PART not in archive.namelist():
        return {}
    root = ET.fromstring(archive.read(CORE_PART))
    values: dict[str, str] = {}
    for node in root:
        local = node.tag.rsplit("}", 1)[-1]
        values[local] = node.text or ""
    return values


def build_core_properties(values: dict[str, str]) -> bytes:
    """Emit docProps/core.xml with canonical, fully bound prefixes.

    The supplied P0.7 masters carry an lxml round-trip artifact here: the
    part binds the Dublin Core terms namespace to prefix `ns2` but still
    writes `xsi:type="dcterms:W3CDTF"` inside the attribute value, leaving
    the `dcterms` prefix unbound in a QName-typed attribute. That makes the
    OPC core-properties part invalid, and Word refuses the whole package as
    corrupted while LibreOffice ignores it -- which is why P0.7's
    LibreOffice-only verification never surfaced it (GATE-02).

    Writing the part from scratch with canonical prefixes removes the
    entire class of problem rather than patching one string.
    """
    declarations = " ".join(f'xmlns:{p}="{u}"' for p, u in _CORE_NS.items())
    parts = [
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
        f"<cp:coreProperties {declarations}>",
    ]
    for prefix, name in _CORE_FIELDS:
        text = values.get(name, "")
        escaped = (
            text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        )
        attribute = (
            ' xsi:type="dcterms:W3CDTF"' if name in ("created", "modified") else ""
        )
        parts.append(f"<{prefix}:{name}{attribute}>{escaped}</{prefix}:{name}>")
    parts.append("</cp:coreProperties>")
    return "".join(parts).encode("utf-8")


def _core_properties(
    archive: ZipFile, title: str, subject: str, creator: str
) -> bytes | None:
    if CORE_PART not in archive.namelist():
        return None
    values = read_core_properties(archive)
    values.update(
        {"title": title, "subject": subject, "creator": creator,
         "lastModifiedBy": creator}
    )
    return build_core_properties(values)


# --------------------------------------------------------------------------
# Reading rendered output
# --------------------------------------------------------------------------

def visible_text(path: Path) -> str:
    """Extract visible paragraph and table-cell text from a DOCX body."""
    root, _ = read_document(path)
    chunks: list[str] = []
    for paragraph in root.iter(f"{W}p"):
        pieces: list[str] = []
        for node in paragraph.iter():
            if node.tag == f"{W}t":
                pieces.append(node.text or "")
            elif node.tag in (f"{W}tab",):
                pieces.append("\t")
            elif node.tag in (f"{W}br", f"{W}cr"):
                pieces.append("\n")
        line = "".join(pieces).strip()
        if line:
            chunks.append(line)
    return "\n".join(chunks)


def normalized(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()
