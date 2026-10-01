import json
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET

from jobbsok import render
from jobbsok.baseline import build_baseline_map, read_baseline
from jobbsok.docxfill import control_inventory
from tools.prepare_masters import prepare

ROOT = Path(__file__).resolve().parents[2]


def test_combined_languages_courses_and_no_references():
    template = json.loads((ROOT / "templates/template_map.json").read_text(encoding="utf-8"))
    controls = template["documents"]["cv"]["controls"]
    assert all(controls[f"CV_SUPPORT_SECTION_{i}"]["source"] == "none" for i in (1, 2, 3))
    assert controls["CV_OPTIONAL_LANGUAGES"]["source"] == "baseline.languages_and_courses"
    assert not any(item.get("source") == "baseline.references_text" for item in controls.values())
    baseline_path = ROOT / "authorities/CV_BASELINE.md"
    baseline = build_baseline_map(read_baseline(baseline_path), baseline_path)
    effective = render.merge_module.effective_cv(baseline, {"cv": {}})
    lines = render.resolve_control(controls["CV_OPTIONAL_LANGUAGES"], effective=effective,
                                   package={"cv": {}, "letter": {}}, job={}, document_date="2026-09-23", fixed_ids=set())
    assert lines[0] == (0, "SPRÅK OG KURS")
    assert any("Norsk" in text for _, text in lines)
    assert any("kurs" in text.casefold() for _, text in lines)


def test_prepare_unbolds_support_content_and_is_byte_idempotent(tmp_path):
    original = ROOT / "evaluation/stable_snapshot/templates/CV_MASTER.docx"
    first = tmp_path / "first/CV_MASTER.docx"
    second = tmp_path / "second/CV_MASTER.docx"
    first.parent.mkdir()
    second.parent.mkdir()
    prepare(original, first)
    prepare(first, second)
    assert first.read_bytes() == second.read_bytes()
    assert control_inventory(first) == control_inventory(original)
    w = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    with ZipFile(first) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    checked = 0
    for control in root.iter(w + "sdt"):
        props = control.find(w + "sdtPr")
        tag = props.find(w + "tag") if props is not None else None
        if tag is None or tag.get(w + "val") not in {"CV_OPTIONAL_LANGUAGES", "CV_OPTIONAL_TRUST", "CV_SUPPORT_SECTION_1"}:
            continue
        paragraphs = list(control.iter(w + "p"))
        assert len(paragraphs) == 2
        assert any(run.find(w + "rPr/" + w + "b") is not None for run in paragraphs[0].iter(w + "r"))
        assert all(run.find(w + "rPr/" + w + "b") is None for run in paragraphs[1].iter(w + "r"))
        checked += 1
    assert checked == 3
