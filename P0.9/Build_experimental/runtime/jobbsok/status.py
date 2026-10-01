"""Derived status and the operator queue.

DEC-07: current production status derives from the immutable manifest,
current artifacts and their fixed input hashes, the current failure record
and the current render report. Audit history and human-readable markers
have no status authority whatsoever -- planting a `_DONE.md`, status prose
or a history entry changes nothing here.

DEC-42: three axes stay independent and are never collapsed into one enum.

Contract 7 fixes the precedence, and the frozen-hash sweep runs before any
job-state precedence: a manifest-frozen mismatch is a run-integrity error
requiring restoration or a child run, not ordinary STALE state.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import artifacts as artifacts_module
from . import render as render_module
from . import validate as validate_module
from .atomicio import read_json
from .errors import ConfigurationError
from .hashing import sha256_file
from .manifest import verify_frozen
from .paths import Layout

#: Actionable grouping for the queue (Spec 7.6). Display order is free; the
#: grouping is what has to be useful.
QUEUE_GROUPS = [
    ("FAILED", "Failed - mechanically invalid"),
    ("RERUN", "Rerun - broader model reconstruction is more efficient"),
    ("STALE", "Stale - an upstream artifact was replaced"),
    ("CHECK", "Check - bounded local confirmation or edit"),
    ("READY", "Ready - skim and approve"),
    ("IN_PROGRESS", "In progress"),
    ("NOT_STARTED", "Not started"),
    ("EXCEPTION", "Exception - handled outside the core"),
]

_PRIORITY_ORDER = {"HIGH": 0, "NORMAL": 1, "LOW": 2}


def _render_report(layout: Layout, run_id: str, job_id: str) -> dict[str, Any] | None:
    path = layout.job_dir(run_id, job_id) / "current" / "render_report.json"
    return read_json(path) if path.is_file() else None


def derive(
    layout: Layout,
    manifest: dict[str, Any],
    *,
    context: validate_module.RunContext | None = None,
    soft_thresholds: dict[str, int] | None = None,
) -> dict[str, Any]:
    """Build the full derived status view for one run."""
    run_id = manifest["run_id"]
    integrity = verify_frozen(layout, manifest)
    if not integrity.ok:
        jobs = []
        for job in manifest["jobs"]:
            exception = job["job_class"] == "EXCEPTION"
            jobs.append({
                "job_id": job["job_id"],
                "employer": job["employer"],
                "title": job["title"],
                "cluster": job["cluster"],
                "sequence": job["sequence"],
                "priority": job["priority"],
                "deadline": job.get("deadline"),
                "semantic_triage": None,
                "production_state": "EXCEPTION" if exception else "FAILED",
                "highest_valid_stage": None,
                "next_stage": None,
                "semantic_final_available": False,
                "render_state": {"overall": "NOT_RENDERED"},
                "stale_scope": [],
                "exception_note": job.get("exception_note"),
                "blocking": None if exception else "RUN-INTEGRITY FAILURE",
                "recommended_action": (
                    "Handle separately or manually."
                    if exception else
                    "Restore the frozen bytes or create a child run."
                ),
                "output_paths": [],
            })
        return {
            "artifact_role": "DERIVED_VIEW",
            "run_id": run_id,
            "derived_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "manifest_sha256": sha256_file(layout.run_dir(run_id) / "manifest.json"),
            "integrity": {
                "ok": False,
                "mismatches": [
                    {
                        "path": v.file,
                        "expected_sha256": v.expected,
                        "observed_sha256": v.observed[:64],
                    }
                    for v in integrity.errors
                ],
            },
            "counts": _counts(manifest, jobs),
            "jobs": jobs,
        }
    context = context or validate_module.RunContext(layout, manifest)
    if soft_thresholds is None:
        from .settings import soft_warnings
        soft_thresholds = soft_warnings(context.assets.settings)

    jobs: list[dict[str, Any]] = []
    for job in manifest["jobs"]:
        jobs.append(
            _derive_job(
                layout, manifest, job, context, soft_thresholds=soft_thresholds
            )
        )

    counts = _counts(manifest, jobs)
    return {
        "artifact_role": "DERIVED_VIEW",
        "run_id": run_id,
        "derived_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "manifest_sha256": sha256_file(layout.run_dir(run_id) / "manifest.json"),
        "integrity": {
            "ok": integrity.ok,
            "mismatches": [
                {
                    "path": v.file,
                    "expected_sha256": v.expected,
                    "observed_sha256": v.observed[:64],
                }
                for v in integrity.errors
            ],
        },
        "counts": counts,
        "jobs": sorted(
            jobs,
            key=lambda j: (
                _group_index(j),
                _PRIORITY_ORDER.get(j["priority"], 1),
                j["deadline"] or "9999-12-31",
                j["sequence"],
            ),
        ),
    }


def _preview_metrics(layout: Layout, run_id: str, job_id: str) -> dict:
    from .paths import flatten_run_reference

    path = (
        layout.generated / "preview" / flatten_run_reference(run_id) / f"{job_id}.json"
    )
    return read_json(path) if path.is_file() else {}


def _signals(
    layout: Layout, run_id: str, job_id: str, report: dict | None, package: dict | None
) -> list[str]:
    """Editorial signals, never a gate: page targets, tics, capacity."""
    out: list[str] = []
    for document in (report or {}).get("documents", []):
        for warning in document.get("warnings", []) or []:
            out.append(warning)
    metrics = _preview_metrics(layout, run_id, job_id)
    from .preview import measured_hash
    if metrics and (not package or metrics.get("artifact_hash") != measured_hash(package)):
        out.append("preview metrics STALE: measured package differs from reported package")
        return sorted(dict.fromkeys(out))
    out.extend(metrics.get("signals", []))
    cv = (metrics.get("documents") or {}).get("cv") or {}
    if cv.get("headline_lines") and cv["headline_lines"] > 1:
        out.append(f"headline renders on {cv['headline_lines']} lines")
    return sorted(dict.fromkeys(out))


def _derive_job(
    layout: Layout,
    manifest: dict[str, Any],
    job: dict[str, Any],
    context: validate_module.RunContext,
    *,
    soft_thresholds: dict[str, int] | None = None,
) -> dict[str, Any]:
    from . import pipeline

    run_id = manifest["run_id"]
    job_id = job["job_id"]
    entry: dict[str, Any] = {
        "job_id": job_id,
        "employer": job["employer"],
        "title": job["title"],
        "cluster": job["cluster"],
        "sequence": job["sequence"],
        "priority": job["priority"],
        "deadline": job.get("deadline"),
        "semantic_triage": None,
        "production_state": "NOT_STARTED",
        "highest_valid_stage": None,
        "next_stage": 0,
        "rerun_stage": None,
        "delivery": None,
        "semantic_final_available": False,
        "render_state": {"overall": "NOT_RENDERED"},
        "stale_scope": [],
        "stale_reason": None,
        "signals": [],
        "exception_note": job.get("exception_note"),
        "blocking": None,
        "recommended_action": "Run Stage 0 (SCOUT).",
        "output_paths": [],
    }
    if job["job_class"] == "EXCEPTION":
        entry.update({
            "production_state": "EXCEPTION",
            "next_stage": None,
            "recommended_action": "Handle separately or manually.",
        })
        return entry

    try:
        state = artifacts_module.semantic_state(
            layout, context, job_id, soft_thresholds=soft_thresholds
        )
    except ConfigurationError as exc:
        entry.update({
            "production_state": "FAILED",
            "next_stage": 0,
            "blocking": "malformed job-local semantic state",
            "recommended_action": str(exc),
        })
        return entry

    report = _render_report(layout, run_id, job_id)
    package = state.loaded.get("final_package")
    if package is None and state.loaded.get("cv_draft"):
        from .assemble import assemble
        fields, _ = assemble(*(state.loaded.get(name) for name in pipeline.LAYER_ORDER))
        package = {"artifact_role": "CURRENT_SEMANTIC_PACKAGE", "source_stage": "ASSEMBLED", **fields}
    entry["signals"] = _signals(layout, run_id, job_id, report, package)
    if report:
        entry["render_state"] = dict(report["render_state"])
        entry["output_paths"] = [
            d["output_path"] for d in report["documents"] if d.get("output_path")
        ]
        receipt = render_module.verify_receipt(
            layout, context, job, state.loaded.get("final_package") or {}, report
        ) if state.current("final_package") else None
        if receipt is not None and not receipt.ok:
            entry["render_state"] = {**entry["render_state"], "overall": "FAILED"}

    brief = state.loaded.get("brief")
    if brief:
        entry["delivery"] = brief.get("delivery")

    review = state.loaded.get("review")
    review_current = state.current("review")
    if review_current:
        entry["semantic_triage"] = review.get("triage")
        entry["rerun_stage"] = review.get("rerun_stage")

    entry["stale_scope"] = sorted(state.stale)
    if state.stale:
        entry["stale_reason"] = "; ".join(
            f"{name}: {reason}" for name, reason in sorted(state.stale_reason.items())
        )

    highest = None
    for stage in pipeline.STAGE_ORDER:
        writes = pipeline.STAGES[stage].writes
        if stage == 3:
            writes = tuple(w for w in writes if w != "review") + (
                ("final_package", "review") if entry["semantic_triage"] != "RERUN" else ()
            )
        if writes and all(state.current(name) for name in writes):
            highest = pipeline.STAGE_KEYS[stage]
    entry["highest_valid_stage"] = highest
    entry["semantic_final_available"] = state.current("final_package")

    if state.invalid:
        entry["production_state"] = "FAILED"
        entry["blocking"] = f"invalid: {', '.join(sorted(state.invalid))}"
    elif state.stale:
        entry["production_state"] = "STALE"
    elif any(value is not None for value in state.loaded.values()):
        entry["production_state"] = "VALID"

    def current(name: str) -> bool:
        return state.current(name)

    if review_current and entry["semantic_triage"] == "RERUN":
        entry["next_stage"] = entry["rerun_stage"]
    elif not current("scout"):
        entry["next_stage"] = 0
    elif not (current("brief") and current("cv_draft")):
        entry["next_stage"] = 1
    elif not current("advocacy_draft"):
        entry["next_stage"] = 2
    elif not (current("polish") and current("final_package") and review_current):
        entry["next_stage"] = 3
    else:
        entry["next_stage"] = None

    if entry["next_stage"] is not None:
        stage = entry["next_stage"]
        entry["recommended_action"] = (
            f"Run Stage {stage} ({pipeline.STAGE_KEYS[stage]})."
        )
        if entry["semantic_triage"] == "RERUN":
            entry["recommended_action"] += " Rejected by the editor; see review.reasons."
    elif entry["render_state"]["overall"] in ("NOT_RENDERED", "FAILED"):
        entry["recommended_action"] = "Run finalize then render."
    else:
        entry["recommended_action"] = "Read the package and decide what to send."
    return entry


def _group_index(entry: dict[str, Any]) -> int:
    order = [key for key, _ in QUEUE_GROUPS]
    return order.index(_queue_group(entry))


def _counts(manifest: dict[str, Any], jobs: list[dict[str, Any]]) -> dict[str, Any]:
    triage = {"READY": 0, "CHECK": 0, "RERUN": 0}
    render = {"NOT_RENDERED": 0, "OK": 0, "DEGRADED": 0, "FAILED": 0}
    states = {"FAILED": 0, "STALE": 0, "NOT_STARTED": 0}
    final_available = 0
    for job in jobs:
        if job["semantic_triage"] in triage:
            triage[job["semantic_triage"]] += 1
        overall = job["render_state"].get("overall", "NOT_RENDERED")
        if overall in render:
            render[overall] += 1
        if job["production_state"] in states:
            states[job["production_state"]] += 1
        final_available += 1 if job["semantic_final_available"] else 0
    return {
        "approved_total": len(manifest["jobs"]),
        "core": sum(1 for j in manifest["jobs"] if j["job_class"] == "CORE"),
        "exception": sum(1 for j in manifest["jobs"] if j["job_class"] == "EXCEPTION"),
        "semantic_final_available": final_available,
        "failed": states["FAILED"],
        "stale": states["STALE"],
        "not_started": states["NOT_STARTED"],
        "triage": triage,
        "render": render,
    }


def next_job(
    status: dict[str, Any],
    *,
    stage: int | None = None,
    cluster: str | None = None,
) -> dict[str, Any] | None:
    """The first job waiting for this stage, in queue order."""
    for entry in status["jobs"]:
        if cluster and entry["cluster"] != cluster:
            continue
        if entry["production_state"] in ("EXCEPTION",):
            continue
        if entry["next_stage"] is None:
            continue
        if stage is not None and entry["next_stage"] != stage:
            continue
        return entry
    return None


def render_queue(status: dict[str, Any]) -> str:
    """The operator queue: what each job is waiting for, and what to look at."""
    lines = [
        f"# Queue - {status['run_id']}",
        "",
        f"derived {status['derived_at']}",
        "",
    ]
    if not status["integrity"]["ok"]:
        lines += [
            "**RUN-INTEGRITY FAILURE.** A frozen input no longer matches its "
            "recorded hash. Restore the frozen bytes or create a child run.",
            "",
        ]
    grouped: dict[str, list[dict[str, Any]]] = {}
    for entry in status["jobs"]:
        grouped.setdefault(_queue_group(entry), []).append(entry)

    for key, heading in QUEUE_GROUPS:
        entries = grouped.get(key) or []
        if not entries:
            continue
        lines += [f"## {heading}", ""]
        for entry in entries:
            stage = entry.get("next_stage")
            waiting = (
                f"next: Stage {stage}" if stage is not None else "next: finalize/render"
            )
            head = (
                f"- **{entry['job_id']}** - {entry['employer']}, {entry['title']}"
                f"  [{waiting}]"
            )
            if entry.get("semantic_triage"):
                head += f" triage {entry['semantic_triage']}"
                if entry.get("rerun_stage"):
                    head += f" -> stage {entry['rerun_stage']}"
            if entry.get("delivery"):
                head += f" delivery {entry['delivery']}"
            lines.append(head)
            lines.append(
                f"    render {entry['render_state']['overall']}"
                f" | production {entry['production_state']}"
                f" | {entry['recommended_action']}"
            )
            if entry.get("signals"):
                lines.append("    signals: " + "; ".join(entry["signals"]))
            if entry.get("stale_reason"):
                lines.append(f"    stale: {entry['stale_reason']}")
        lines.append("")
    return "\n".join(lines)


def _queue_group(entry: dict[str, Any]) -> str:
    if entry["production_state"] == "EXCEPTION":
        return "EXCEPTION"
    if entry["production_state"] == "FAILED":
        return "FAILED"
    if entry.get("semantic_triage") == "RERUN":
        return "RERUN"
    if entry["production_state"] == "STALE":
        return "STALE"
    if entry.get("semantic_triage") == "CHECK":
        return "CHECK"
    if entry.get("semantic_triage") == "READY":
        return "READY"
    if entry["production_state"] == "NOT_STARTED":
        return "NOT_STARTED"
    return "IN_PROGRESS"
