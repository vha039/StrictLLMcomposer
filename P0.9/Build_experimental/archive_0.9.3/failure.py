"""The current failure/blocking record.

CTR-03 / DEC-07 / Contract 5.6. One minimal CURRENT representation that
status derivation reads without consulting history. At most one record
exists per job at a time; a successful current replacement clears or
supersedes it, and the superseded copy may be archived.

This is deliberately not an event log, not a retry engine, and not a
workflow-state object. Attempts are recorded because bounded recovery must
be visible (ACC-14), not because anything here advances automatically.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .atomicio import atomic_write_json, read_json
from .errors import ValidationResult
from .paths import Layout

FILENAME = "failure.json"


def path_for(layout: Layout, run_id: str, job_id: str) -> Path:
    return layout.job_dir(run_id, job_id) / "current" / FILENAME


def load(layout: Layout, run_id: str, job_id: str) -> dict[str, Any] | None:
    path = path_for(layout, run_id, job_id)
    return read_json(path) if path.is_file() else None


def record(
    layout: Layout,
    run_id: str,
    job_id: str,
    *,
    operation: str,
    classification: str,
    result: ValidationResult | None = None,
    diagnostic_summary: str = "",
    recommended_next_action: str,
    attempts_used: int = 0,
    retry_position: int | None = None,
    mechanical_corrections_used: int = 0,
    semantic_attempt: int | None = None,
    last_successful_stage: str | None = None,
    applies_to_hashes: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Write or replace the current failure record for one job."""
    payload: dict[str, Any] = {
        "artifact_role": "CURRENT_FAILURE",
        "run_id": run_id,
        "job_id": job_id,
        "operation": operation,
        "classification": classification,
        "applies_to_hashes": applies_to_hashes or {},
        "violations": [
            {
                "contract_id": v.contract_id,
                "file": v.file,
                "location": v.location,
                "expected": v.expected,
                "observed": v.observed,
                "severity": v.severity,
            }
            for v in (result.violations if result else [])
        ],
        "diagnostic_summary": diagnostic_summary,
        "attempts_used": attempts_used,
        "retry_position": retry_position,
        "mechanical_corrections_used": mechanical_corrections_used,
        "semantic_attempt": semantic_attempt,
        "last_successful_stage": last_successful_stage,
        "recommended_next_action": recommended_next_action,
        "recorded_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    atomic_write_json(path_for(layout, run_id, job_id), payload)
    return payload


def clear(layout: Layout, run_id: str, job_id: str, *, archive: bool = True) -> bool:
    """Clear the current record after a successful replacement.

    The superseded record may move to bounded audit history, which status
    never reads (DEC-07).
    """
    path = path_for(layout, run_id, job_id)
    if not path.is_file():
        return False
    if archive:
        history = layout.job_dir(run_id, job_id) / "history"
        history.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        (history / f"{stamp}_{FILENAME}").write_bytes(path.read_bytes())
    path.unlink()
    return True


def next_retry_stage(
    retry_start_stages: list[int], attempts_used: int
) -> int | None:
    """Which standard stage the operator should restart next, if any.

    DEC-36 / Contract 9.2: this only tells or scaffolds the operator. It
    never calls a model, never advances automatically, and never becomes a
    retry engine. When the configured path is exhausted the job becomes
    BLOCKED_MANUAL and independent jobs keep processing.
    """
    if attempts_used >= len(retry_start_stages):
        return None
    return retry_start_stages[attempts_used]
