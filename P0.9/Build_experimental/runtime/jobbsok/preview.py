"""Render the work in progress and measure it, inside the stage session.

Page count, headline line count and tail overflow are physical facts about
the rendered document. Guessing them is how three-page CVs shipped. This
renders whatever layers exist right now to a scratch folder - no receipt, no
canonical output, no finalization - and prints what the document actually
does.

If Word COM is unavailable (a sandboxed session, a locked Word), pages come
back UNKNOWN and the word counts and signals still print.
"""

from __future__ import annotations

import json
import tempfile
from datetime import date
from pathlib import Path
from typing import Any

from . import assemble as assemble_module
from . import artifacts as artifacts_module
from . import render as render_module
from . import signals
from . import pipeline
from .atomicio import atomic_write_json, read_json
from .manifest import find_job, frozen_path, read_frozen
from .paths import Layout, flatten_run_reference

TAIL_HEADINGS = (
    "TIDLIGERE ERFARING", "TILLITSVERV", "SPRÅK", "SPRÅK OG KURS", "KURS",
    "REFERANSER", "VERKTØY",
)


def _return_dir(layout: Layout, run_id: str, job_id: str, stage: int) -> Path:
    return (
        layout.generated / "returns" / flatten_run_reference(run_id) / job_id
        / f"stage{stage}"
    )


def _in_progress(layout: Layout, context: Any, job_id: str, stage: int, artifact: str):
    """A return file written but not yet submitted, else the current artifact."""
    fingerprint = pipeline.evidence_fingerprint(context, job_id, stage)
    path = _return_dir(layout, context.run_id, job_id, stage) / fingerprint[:8] / f"{artifact}.semantic.json"
    if path.is_file():
        return read_json(path), str(path)
    return artifacts_module.load(layout, context.run_id, job_id, artifact), "current artifact"


def resolve_layers(layout: Layout, context: Any, job_id: str, stage: int):
    layers, sources = {}, {}
    for name in pipeline.LAYER_ORDER:
        owner = pipeline.stage_of(name)
        if owner > stage:
            layers[name] = None
        elif owner == stage:
            layers[name], sources[name] = _in_progress(layout, context, job_id, stage, name)
        else:
            layers[name] = artifacts_module.load(layout, context.run_id, job_id, name)
            sources[name] = "current artifact"
    return layers, sources


def layer_states(layout: Layout, context: Any, job_id: str, sources: dict[str, str]) -> str:
    state = artifacts_module.semantic_state(layout, context, job_id)
    labels = []
    for name, source in sources.items():
        if source != "current artifact":
            continue
        if name in state.invalid:
            labels.append(f"{name}=INVALID")
        elif name in state.stale:
            labels.append(f"{name}=STALE ({state.stale_reason[name]})")
    return "; ".join(labels) or "current submitted layers"


def measured_hash(package: dict[str, Any]) -> str:
    return artifacts_module.artifact_hash({k: v for k, v in package.items() if k != "binding"})


def build_package(
    layout: Layout, context: Any, job_id: str, stage: int
) -> tuple[dict[str, Any], dict[str, Any]]:
    """The package as it would look if the work in progress were submitted."""
    layers, sources = resolve_layers(layout, context, job_id, stage)
    cv_draft = layers["cv_draft"]
    if cv_draft is None:
        raise FileNotFoundError(
            "No CV layer yet. Stage 1 writes cv_draft before preview can render."
        )
    advocacy, polish = layers["advocacy_draft"], layers["polish"]
    package, summary = assemble_module.assemble(cv_draft, advocacy, polish)
    package = {
        "artifact_role": "CURRENT_SEMANTIC_PACKAGE",
        "source_stage": "ASSEMBLED",
        **package,
        "finalization": {
            "state": "FINALIZED", "document_date": date.today().isoformat(),
        },
    }
    summary["sources"] = sources
    summary["state"] = layer_states(layout, context, job_id, sources)
    return package, summary


def _pdf_facts(path: Path, package: dict[str, Any], component: str) -> dict[str, Any]:
    import pymupdf

    facts: dict[str, Any] = {"pages": None}
    with pymupdf.open(path) as document:
        facts["pages"] = document.page_count
        tail: dict[str, int] = {}
        headline_lines = 0
        headline = (package.get("cv") or {}).get("headline", "").upper()
        for number, page in enumerate(document, start=1):
            text = page.get_text()
            for heading in TAIL_HEADINGS:
                if heading in text and heading not in tail:
                    tail[heading] = number
            if component == "cv" and number == 1 and headline:
                blocks = page.get_text("dict")["blocks"]
                for block in blocks:
                    for line in block.get("lines", []):
                        spans = line.get("spans", [])
                        if not spans or spans[0]["size"] < 13:
                            continue
                        text_line = "".join(s["text"] for s in spans).strip().upper()
                        if text_line and text_line in headline:
                            headline_lines += 1
        facts["tail_sections"] = tail
        if component == "cv":
            facts["headline_lines"] = headline_lines or None
    return facts


def preview(
    layout: Layout,
    context: Any,
    job_id: str,
    stage: int,
    *,
    cv_only: bool = False,
) -> dict[str, Any]:
    manifest = context.manifest
    job = find_job(manifest, job_id)
    package, summary = build_package(layout, context, job_id, stage)
    if cv_only:
        package = {**package, "letter": None}

    template_map = read_json(
        frozen_path(layout, context.run_id, read_frozen(layout, manifest, "template_map"))
    )
    destination = (
        Path(tempfile.gettempdir()) / "jbprev" / job_id[:20]
        / date.today().strftime("%m%d") / f"{abs(hash(json.dumps(package, sort_keys=True))) % 100000:05d}"
    )
    destination.mkdir(parents=True, exist_ok=True)

    metrics: dict[str, Any] = {
        "job_id": job_id,
        "stage": stage,
        "cv_dynamic_words": summary["cv_dynamic_words"],
        "letter_words": signals.letter_words(package.get("letter")),
        "signals": signals.scan(package),
        "artifact_hash": measured_hash(package),
        "sources": summary["sources"],
        "state": summary["state"],
        "documents": {},
        "destination": str(destination),
    }
    try:
        report = render_module.render_job(
            layout, assets=context.assets, manifest=manifest, job=job,
            package=package, baseline_map=context.baseline_map,
            template_map=template_map,
            render_settings=context.assets.settings["render"],
            destination=destination,
        )
    except Exception as exc:  # Word COM missing, locked, or refused
        metrics["render_error"] = f"{type(exc).__name__}: {exc}"
        _store(layout, context.run_id, job_id, metrics)
        return metrics

    for document in report["documents"]:
        if document["format"] != "pdf" or document["state"] != "OK":
            continue
        path = Path(document["output_path"])
        try:
            facts = _pdf_facts(path, package, document["component"])
        except Exception as exc:
            facts = {"pages": None, "error": f"{type(exc).__name__}: {exc}"}
        facts["warnings"] = document.get("warnings", [])
        metrics["documents"][document["component"]] = facts
    metrics["render_state"] = report["render_state"]["overall"]
    _store(layout, context.run_id, job_id, metrics)
    return metrics


def _store(layout: Layout, run_id: str, job_id: str, metrics: dict[str, Any]) -> None:
    path = (
        layout.generated / "preview" / flatten_run_reference(run_id) / f"{job_id}.json"
    )
    atomic_write_json(path, metrics)


def render_report_lines(metrics: dict[str, Any], capacity: dict[str, int]) -> list[str]:
    lines = ["state     : " + metrics["state"]]
    lines += [f"source    : {name}: {source}" for name, source in metrics["sources"].items()]
    cv = metrics["documents"].get("cv") or {}
    letter = metrics["documents"].get("letter") or {}
    pages_cv = cv.get("pages")
    pages_letter = letter.get("pages")
    if "render_error" in metrics:
        lines.append(f"pages     : UNKNOWN - {metrics['render_error']}")
    else:
        lines.append(
            f"pages     : CV {pages_cv if pages_cv else '?'}"
            f"  letter {pages_letter if pages_letter else 'n/a'}"
            f"  headline lines {cv.get('headline_lines') or '?'}"
        )
    lines.append(
        f"words     : CV {metrics['cv_dynamic_words']} dynamic "
        f"(capacity ~{capacity.get('cv_dynamic_words')})"
        f"  letter {metrics['letter_words']} (target ~{capacity.get('letter_words')})"
    )
    tail = cv.get("tail_sections") or {}
    overflow = [name for name, page in tail.items() if page and page > 2]
    lines.append(
        "overflow  : " + (", ".join(f"{n} on page {tail[n]}" for n in overflow)
                          if overflow else "none")
    )
    lines.append("signals   : " + (", ".join(metrics["signals"]) or "none"))
    return lines
