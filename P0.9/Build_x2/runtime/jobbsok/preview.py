"""Unsubmitted Stage-3 preview. All rendering lives in a temporary directory."""

from __future__ import annotations

import copy
import re
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any

from . import artifacts, merge, render, signals, validate
from .atomicio import read_json
from .errors import ConfigurationError, JobError
from .hashing import sha256_canonical_json
from .manifest import find_job, frozen_path, read_frozen
from .paths import Layout


def _words(value: str) -> int:
    return len(re.findall(r"\S+", value))


def _semantic_metrics(package: dict[str, Any], baseline_map: dict[str, Any]) -> dict[str, Any]:
    effective = merge.effective_cv(baseline_map, package)
    cv, letter = package["cv"], package["letter"]
    sections = {
        "cv.headline": _words(cv["headline"]),
        "cv.profile": _words(cv["profile"]),
        "cv.competencies": sum(_words(v) for v in cv["competencies"]),
        "letter.opening": _words(letter["opening"]),
        "letter.body": sum(_words(v) for v in letter["body_paragraphs"]),
        "letter.closing": _words(letter["closing"]),
    }
    employment = []
    for row in effective["employments"]:
        bullets = row["bullets"]
        employment.append({
            "employment_id": row["employment_id"],
            "bullet_count": len(bullets),
            "word_count": sum(_words(v) for v in bullets),
            "source": "override" if row["bullet_source"] == "OVERRIDE" else "baseline",
        })
    return {"semantic_sections": sections, "employment": employment}


def _physical_metrics(report: dict[str, Any], package: dict[str, Any], target: dict[str, int]) -> dict[str, Any]:
    try:
        import pymupdf as fitz
    except ImportError as exc:
        raise ConfigurationError("PyMuPDF is required for physical preview metrics.") from exc
    result: dict[str, Any] = {
        "page_counts": {"cv": "UNKNOWN", "letter": "UNKNOWN"},
        "headline_lines": "UNKNOWN",
        "headings_after_target": [],
        "page_words": {"cv": "UNKNOWN", "letter": "UNKNOWN"},
        "render_limitation": None,
    }
    for component in ("cv", "letter"):
        record = next((d for d in report["documents"] if d["component"] == component and d["format"] == "pdf"), None)
        if not record or record["state"] != "OK" or not record.get("output_path"):
            result["render_limitation"] = (record or {}).get("limitation") or "PDF conversion unavailable"
            continue
        with fitz.open(record["output_path"]) as pdf:
            result["page_counts"][component] = len(pdf)
            result["page_words"][component] = [_words(page.get_text()) for page in pdf]
            for page_index in range(target[component], len(pdf)):
                for line in pdf[page_index].get_text().splitlines():
                    value = line.strip()
                    if 3 <= len(value) <= 70 and value == value.upper() and re.search(r"[A-ZÆØÅ]", value):
                        result["headings_after_target"].append({"document": component, "page": page_index + 1, "heading": value})
            if component == "cv" and len(pdf):
                headline = re.sub(r"\s+", " ", package["cv"]["headline"]).strip().casefold()
                if headline:
                    lines = [re.sub(r"\s+", " ", line).strip().casefold() for line in pdf[0].get_text().splitlines()]
                    for start in range(len(lines)):
                        phrase = ""
                        for end in range(start, min(start + 5, len(lines))):
                            phrase = (phrase + " " + lines[end]).strip()
                            if phrase == headline:
                                result["headline_lines"] = end - start + 1
                                break
                        if result["headline_lines"] != "UNKNOWN":
                            break
    return result


def run(
    layout: Layout, context: validate.RunContext, *, job_id: str,
    handoff: Path, semantic_file: Path, preview_date: str | None = None,
    soft_thresholds: dict[str, int] | None = None,
) -> dict[str, Any]:
    manifest = context.manifest
    job = find_job(manifest, job_id)
    envelope = artifacts.verify_handoff(
        layout, context, job_id, 3, handoff, soft_thresholds=soft_thresholds
    )
    if envelope["mode"] != "FINAL_AND_REVIEW":
        raise JobError("Preview requires a current Stage-3 FINAL_AND_REVIEW handoff.")
    source = semantic_file.resolve(strict=True)
    run_root = layout.runs.resolve()
    if source == run_root or run_root in source.parents:
        raise JobError("Preview --file must be an unsubmitted semantic return outside runs/.")
    semantic = read_json(source)
    state = artifacts.semantic_state(layout, context, job_id, soft_thresholds=soft_thresholds)
    package = artifacts.stamp_payload(context, job_id, "final_package", semantic, state)
    checked = validate.validate_artifact(
        layout, context, job_id, "final_package", package,
        soft_thresholds=soft_thresholds,
    )
    content_hash = sha256_canonical_json(semantic)
    date = preview_date or datetime.now().astimezone().date().isoformat()
    frozen = manifest["frozen_inputs"]
    hashes = {
        "baseline": frozen["baseline_map"]["sha256"],
        "cv_master": frozen["templates"]["cv_master"]["sha256"],
        "letter_master": frozen["templates"]["letter_master"]["sha256"],
        "template_map": frozen["template_map"]["sha256"],
        "settings": frozen["settings"]["sha256"],
    }
    result = {
        "valid": checked.ok,
        "candidate_content_sha256": content_hash,
        "measurement_id": sha256_canonical_json({"content": content_hash, "date": date, "frozen": hashes}),
        "preview_date": date,
        "frozen_input_hashes": hashes,
        "validation_errors": [v.render() for v in checked.errors],
        "validation_warnings": [v.render() for v in checked.warnings],
    }
    if not checked.ok:
        return result

    result.update(_semantic_metrics(package, context.baseline_map))
    result["formula_signals"] = signals.inspect_package(
        package, title=job["title"],
        effective_cv=merge.effective_cv(context.baseline_map, package),
    )
    render_package = copy.deepcopy(package)
    render_package["finalization"] = {"state": "FINALIZED", "document_date": date}
    template_map = read_json(frozen_path(layout, context.run_id, read_frozen(layout, manifest, "template_map")))
    with tempfile.TemporaryDirectory(prefix="jb-preview-") as directory:
        report = render.render_job(
            layout, assets=context.assets, manifest=manifest, job=job,
            package=render_package, baseline_map=context.baseline_map,
            template_map=template_map, render_settings=context.assets.settings["render"],
            destination=Path(directory),
        )
        if report["render_state"]["overall"] == "FAILED":
            raise ConfigurationError("Preview DOCX rendering failed: " + str(report["documents"]))
        settings = context.assets.settings["render"]["soft_warnings"]
        result.update(_physical_metrics(report, package, {
            "cv": settings["cv_expected_max_pages"],
            "letter": settings["letter_expected_max_pages"],
        }))
    return result
