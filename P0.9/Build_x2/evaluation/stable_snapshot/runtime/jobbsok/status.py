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
from .manifest import is_legacy_run, verify_frozen
from .paths import Layout

#: Actionable grouping for the queue (Spec 7.6). Display order is free; the
#: grouping is what has to be useful.
QUEUE_GROUPS = [
    ("BLOCKED_MANUAL", "Blocked - needs a human decision"),
    ("FAILED", "Failed - mechanically invalid, recovery available"),
    ("RERUN", "Rerun - broader model reconstruction is more efficient"),
    ("STALE", "Stale - an upstream artifact was replaced"),
    ("CHECK", "Check - bounded local confirmation or edit"),
    ("READY", "Ready - skim and approve"),
    ("IN_PROGRESS", "In progress"),
    ("NOT_STARTED", "Not started"),
    ("EXCEPTION", "Exception - handled outside the core"),
]

_PRIORITY_ORDER = {"HIGH": 0, "NORMAL": 1, "LOW": 2}


def _failure_record(layout: Layout, run_id: str, job_id: str) -> dict[str, Any] | None:
    path = layout.job_dir(run_id, job_id) / "current" / "failure.json"
    return read_json(path) if path.is_file() else None


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


def _derive_job(
    layout: Layout,
    manifest: dict[str, Any],
    job: dict[str, Any],
    context: validate_module.RunContext,
    *,
    soft_thresholds: dict[str, int] | None,
) -> dict[str, Any]:
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
        "semantic_final_available": False,
        "render_state": {"overall": "NOT_RENDERED"},
        "stale_scope": [],
        "exception_note": job.get("exception_note"),
        "blocking": None,
        "recommended_action": None,
        "output_paths": [],
    }

    # 1. Exception removes the job from core production expectations but not
    #    from approved-opportunity reporting (Spec 7.6).
    if job["job_class"] == "EXCEPTION":
        entry["production_state"] = "EXCEPTION"
        entry["recommended_action"] = (
            "Handle separately or manually. This never blocks a core job."
        )
        return entry

    # Render state is derived independently of the semantic axes (DEC-42).
    render_issue: str | None = None
    try:
        report = _render_report(layout, run_id, job_id)
    except ConfigurationError as exc:
        report = None
        render_issue = f"Malformed job-local render receipt: {exc}"

    # 2. A current terminal blocking record wins over artifact state.
    try:
        failure = _failure_record(layout, run_id, job_id)
    except ConfigurationError as exc:
        entry["production_state"] = "FAILED"
        entry["blocking"] = f"Malformed current failure record: {exc}"
        entry["recommended_action"] = (
            "Repair or remove this job's malformed current failure record."
        )
        return entry
    try:
        semantic = artifacts_module.semantic_state(
            layout, context, job_id, soft_thresholds=soft_thresholds
        )
    except ConfigurationError as exc:
        entry["production_state"] = "FAILED"
        entry["blocking"] = f"Malformed job-local semantic state: {exc}"
        entry["recommended_action"] = (
            "Repair the named current artifact through its owning stage; "
            "other jobs remain independent."
        )
        return entry
    loaded = semantic.loaded

    if render_issue:
        entry["render_state"] = {
            "overall": "FAILED",
            "limitation": render_issue,
            "human_action": "Repair or remove this job's invalid render receipt.",
        }
    elif report:
        package = loaded.get("final_package")
        receipt = (
            render_module.verify_receipt(layout, context, job, package, report)
            if package is not None and semantic.current("final_package")
            else None
        )
        if receipt is None or not receipt.ok:
            detail = (
                receipt.errors[0].render() if receipt is not None and receipt.errors
                else "No current valid semantic final matches the receipt."
            )
            output_locked = receipt is not None and any(
                "current output is open or locked" in violation.observed
                for violation in receipt.errors
            )
            entry["render_state"] = {
                "overall": "FAILED",
                "limitation": f"Render receipt is not current: {detail}",
                "human_action": (
                    "Close the open document and rerun status; no output was "
                    "overwritten."
                    if output_locked else
                    "Rerender from the current eligible semantic final."
                ),
            }
        else:
            state = report["render_state"]
            entry["render_state"] = {
                "overall": state["overall"],
                "cv_docx": state.get("cv_docx"),
                "cv_pdf": state.get("cv_pdf"),
                "letter_docx": state.get("letter_docx"),
                "letter_pdf": state.get("letter_pdf"),
                "limitation": next(
                    (d.get("limitation") for d in report["documents"] if d.get("limitation")),
                    None,
                ),
                "human_action": next(
                    (d.get("human_action") for d in report["documents"] if d.get("human_action")),
                    None,
                ),
            }
            entry["output_paths"] = [
                d["output_path"] for d in report["documents"]
                if d.get("state") == "OK" and d.get("output_path")
            ]

    if failure and failure.get("classification") == "BLOCKED_MANUAL":
        entry["production_state"] = "BLOCKED_MANUAL"
        entry["blocking"] = failure.get("diagnostic_summary") or failure.get("operation")
        entry["recommended_action"] = failure.get("recommended_next_action")
        entry["highest_valid_stage"] = failure.get("last_successful_stage")
        return entry
    if not any(loaded.values()):
        # A failed attempt is not the same as never started (Contract 17.1
        # test 8). A stage can fail without leaving a valid artifact behind,
        # so the current failure record still decides the state here.
        if failure and failure.get("classification") == "FAILED":
            entry["production_state"] = "FAILED"
            entry["blocking"] = failure.get("diagnostic_summary")
            entry["recommended_action"] = failure.get("recommended_next_action")
            entry["highest_valid_stage"] = failure.get("last_successful_stage")
        else:
            entry["recommended_action"] = "Start Stage 1 for this job."
        return entry

    # 3-4. Shared fixed currentness: static staleness plus mechanical validity.
    stale = semantic.stale
    invalid = semantic.invalid
    valid = semantic.valid

    ladder = (
        [("strategy", "STRATEGY"), ("draft_package", "DRAFT"),
         ("final_package", "FINAL")]
        if is_legacy_run(manifest)
        else [("strategy", "STRATEGY"), ("final_package", "FINAL")]
    )
    highest = None
    for name, label in ladder:
        if name in valid and name not in stale:
            highest = label
        else:
            break
    entry["highest_valid_stage"] = highest

    if stale:
        entry["production_state"] = "STALE"
        entry["stale_scope"] = sorted(
            s for s in stale if s in ("draft_package", "final_package", "review")
        )
        entry["stale_scope"] = [
            {"draft_package": "draft", "final_package": "final", "review": "review"}[s]
            for s in entry["stale_scope"]
        ]
        entry["recommended_action"] = (
            "Re-run the owning stage for the stale artifact; do not edit it in place."
        )
    elif invalid:
        entry["production_state"] = "FAILED"
        entry["recommended_action"] = (
            f"Repair and revalidate: {', '.join(sorted(invalid))}."
        )
    elif failure and failure.get("classification") == "FAILED":
        entry["production_state"] = "FAILED"
        entry["blocking"] = failure.get("diagnostic_summary")
        entry["recommended_action"] = failure.get("recommended_next_action")
    else:
        entry["production_state"] = "VALID"

    # 5. semantic_final_available is reported explicitly, never inferred from
    #    the presence of a render file (Spec 7.5).
    entry["semantic_final_available"] = (
        loaded["final_package"] is not None
        and "final_package" in valid
        and "final_package" not in stale
    )

    # 6. Triage appears only when a current final and review both validate
    #    and bind to each other.
    review = loaded["review"]
    review_current = (
        entry["semantic_final_available"]
        and review is not None
        and "review" in valid
        and "review" not in stale
    )
    if review_current:
        expected = artifacts_module.artifact_hash(loaded["final_package"])
        if review.get("binding", {}).get("final_package_sha256") == expected:
            entry["semantic_triage"] = review["triage"]
            if not entry["recommended_action"]:
                reasons = review.get("reasons") or []
                limitations = review.get("known_limitations") or []
                actions = [
                    f"{reason['reason']} Action: {reason['recommended_action']}"
                    for reason in reasons[:3]
                ]
                actions.extend(f"Known limitation: {item}" for item in limitations)
                entry["recommended_action"] = " | ".join(actions) or "Skim and approve."

    if (
        entry["semantic_final_available"]
        and (review is None or "review" in stale)
    ):
        entry["recommended_action"] = (
            "Complete Stage 3 review-only; run context for Stage 3."
        )
    elif entry["production_state"] == "VALID" and not entry["recommended_action"]:
        nxt = {
            None: "Stage 1",
            "STRATEGY": "Stage 2" if is_legacy_run(manifest) else "Stage 3",
            "DRAFT": "Stage 3",
        }.get(highest)
        entry["recommended_action"] = f"Run {nxt}." if nxt else "Finalize and render."
    return entry


def _group_index(entry: dict[str, Any]) -> int:
    for index, (key, _) in enumerate(QUEUE_GROUPS):
        if entry["production_state"] == key:
            return index
        if entry["semantic_triage"] == key:
            return index
    if entry["production_state"] == "VALID":
        return next(i for i, (k, _) in enumerate(QUEUE_GROUPS) if k == "IN_PROGRESS")
    return len(QUEUE_GROUPS)


def _counts(manifest: dict[str, Any], jobs: list[dict[str, Any]]) -> dict[str, Any]:
    triage = {"READY": 0, "CHECK": 0, "RERUN": 0}
    render = {"NOT_RENDERED": 0, "OK": 0, "DEGRADED": 0, "FAILED": 0}
    states = {"BLOCKED_MANUAL": 0, "FAILED": 0, "STALE": 0, "NOT_STARTED": 0}
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
        "blocked_manual": states["BLOCKED_MANUAL"],
        "failed": states["FAILED"],
        "stale": states["STALE"],
        "not_started": states["NOT_STARTED"],
        "triage": triage,
        "render": render,
    }


def next_job(
    status: dict[str, Any], *, stage: int | None = None, cluster: str | None = None,
    failed_at_stage: frozenset[str] = frozenset(),
    spec_revision: str | None = None,
) -> dict[str, Any] | None:
    """The next unfinished, failed or blocked job (Contract 10.2).

    Continuation is derived from current disk state. Remembered chat
    position is never authoritative, and no completed-job history is needed.

    `failed_at_stage` names jobs whose current failure record is a FAILED
    attempt at the requested stage. A replacement attempt that fails leaves
    the older downstream artifacts current, so the stage ladder alone would
    hide the owed correction from that stage's own queue.

    `spec_revision` is the run's own manifest revision. Stage 3 waits on a
    current STRATEGY for 0.9.3 and on a current DRAFT for legacy 0.9.0.
    """
    from .manifest import LEGACY_SPEC_REVISION

    stage3_prerequisite = ("DRAFT",) if str(spec_revision) == LEGACY_SPEC_REVISION else ("STRATEGY",)
    wanted = {1: (None,), 2: ("STRATEGY",), 3: stage3_prerequisite}.get(stage or 0)
    for job in status["jobs"]:
        if cluster and job["cluster"] != cluster:
            continue
        if job["production_state"] == "EXCEPTION":
            continue
        if stage is None:
            if job["production_state"] != "VALID" or job["semantic_triage"] != "READY":
                return job
            continue
        if job["production_state"] in ("BLOCKED_MANUAL",):
            continue
        if job["job_id"] in failed_at_stage:
            return job
        if job["highest_valid_stage"] in wanted:
            return job
        if (
            stage == 3
            and job["highest_valid_stage"] == "FINAL"
            and job["semantic_triage"] is None
        ):
            return job
    return None


def render_queue(status: dict[str, Any]) -> str:
    """Disposable human view. Never stores a measurement (Spec 18.3)."""
    lines = [
        f"# Queue — run {status['run_id']}",
        "",
        f"Derived {status['derived_at']}. This view is disposable and "
        "regenerable; it is never authoritative.",
        "",
    ]
    if not status["integrity"]["ok"]:
        lines += [
            "## RUN-INTEGRITY FAILURE",
            "",
            "A manifest-frozen input no longer matches its recorded hash. This "
            "is not staleness. Restore the frozen bytes or create a child run "
            "(`jobbsok branch`). The manifest is never updated in place.",
            "",
        ]
        for mismatch in status["integrity"]["mismatches"]:
            lines.append(f"- `{mismatch['path']}`")
        lines.append("")

    counts = status["counts"]
    lines += [
        "## Counts",
        "",
        f"- approved opportunities: {counts['approved_total']}"
        f"  (core {counts['core']}, exception {counts['exception']})",
        f"- semantic final available: {counts['semantic_final_available']}",
        f"- triage: READY {counts['triage']['READY']}, "
        f"CHECK {counts['triage']['CHECK']}, RERUN {counts['triage']['RERUN']}",
        f"- render: OK {counts['render']['OK']}, "
        f"DEGRADED {counts['render']['DEGRADED']}, "
        f"FAILED {counts['render']['FAILED']}, "
        f"not rendered {counts['render']['NOT_RENDERED']}",
        f"- blocked {counts['blocked_manual']}, failed {counts['failed']}, "
        f"stale {counts['stale']}, not started {counts['not_started']}",
        "",
    ]

    grouped: dict[str, list[dict[str, Any]]] = {}
    for job in status["jobs"]:
        key = QUEUE_GROUPS[min(_group_index(job), len(QUEUE_GROUPS) - 1)][0]
        grouped.setdefault(key, []).append(job)

    for key, heading in QUEUE_GROUPS:
        entries = grouped.get(key)
        if not entries:
            continue
        lines += [f"## {heading}", ""]
        for job in entries:
            deadline = f" · frist {job['deadline']}" if job.get("deadline") else ""
            render = job["render_state"].get("overall", "NOT_RENDERED")
            lines.append(
                f"- **{job['job_id']}** — {job['employer']}, {job['title']} "
                f"[{job['priority']}{deadline}]"
            )
            lines.append(
                f"  - production: {job['production_state']}"
                f" · stage: {job['highest_valid_stage'] or '-'}"
                f" · triage: {job['semantic_triage'] or '-'}"
                f" · render: {render}"
            )
            if job.get("recommended_action"):
                lines.append(f"  - action: {job['recommended_action']}")
            if job["render_state"].get("human_action"):
                lines.append(f"  - render: {job['render_state']['human_action']}")
            for path in job.get("output_paths", []):
                lines.append(f"  - output: `{Path(path).name}`")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"
