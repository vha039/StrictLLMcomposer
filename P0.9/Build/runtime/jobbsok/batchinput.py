"""Pre-freeze operator batch input.

Spec 5.1: the human approves opportunities, assigns stable job identities,
classifies each as CORE or EXCEPTION, assigns clusters/order/priority, and
identifies source files. The input may be CSV, a spreadsheet or another
simple editable format. It is compiled into the run manifest and is not
itself a second run authority afterwards.

The core inventory must not require generalized platform/channel fields.
Human notes may capture irregularities without driving core schemas
(DEC-03). There is no language column: nb-NO is stated once in policy, and
a per-job language field would be a core language branch (DEC-04).
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .errors import ValidationResult
from .paths import require_safe_component
from .errors import PathSafetyError

REQUIRED_COLUMNS = [
    "job_id",
    "employer",
    "title",
    "job_class",
    "cluster",
    "sequence",
    "priority",
    "source",
]
OPTIONAL_COLUMNS = ["unit", "reference", "deadline", "exception_note"]
ALLOWED_COLUMNS = set(REQUIRED_COLUMNS) | set(OPTIONAL_COLUMNS)

TEMPLATE_HEADER = REQUIRED_COLUMNS + OPTIONAL_COLUMNS


@dataclass
class BatchRow:
    job_id: str
    employer: str
    title: str
    job_class: str
    cluster: str
    sequence: int
    priority: str
    source: str
    unit: str | None = None
    reference: str | None = None
    deadline: str | None = None
    exception_note: str | None = None

    def to_manifest_entry(self, source_record: dict[str, Any],
                          requires_inspection: bool,
                          reasons: list[str]) -> dict[str, Any]:
        entry: dict[str, Any] = {
            "job_id": self.job_id,
            "employer": self.employer,
            "title": self.title,
            "unit": self.unit,
            "reference": self.reference,
            "deadline": self.deadline,
            "job_class": self.job_class,
            "exception_note": self.exception_note,
            "cluster": self.cluster,
            "sequence": self.sequence,
            "priority": self.priority,
            "source": source_record,
            "requires_source_inspection": requires_inspection,
        }
        if reasons:
            entry["source_inspection_reasons"] = reasons
        return entry


def _clean(value: str | None) -> str | None:
    if value is None:
        return None
    stripped = value.strip()
    return stripped or None


def read_batch_input(path: Path) -> tuple[list[BatchRow], ValidationResult]:
    """Parse and mechanically validate the operator batch input.

    Every independently detectable problem is reported in one pass rather
    than stopping at the first bad row (Contract 8.1).
    """
    path = Path(path)
    result = ValidationResult()
    label = path.name
    rows: list[BatchRow] = []

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = [f.strip() for f in (reader.fieldnames or [])]

        missing = [c for c in REQUIRED_COLUMNS if c not in fieldnames]
        if missing:
            result.add(
                "DEC-08", label, "header",
                f"columns {REQUIRED_COLUMNS}",
                f"missing {missing}",
            )
        unknown = [c for c in fieldnames if c and c not in ALLOWED_COLUMNS]
        if unknown:
            result.add(
                "DEC-03", label, "header",
                "only the approved columns; no platform, channel, portal, "
                "language or output-mode column may exist",
                f"unknown columns {unknown}",
            )
        if missing:
            return rows, result

        seen_ids: dict[str, int] = {}
        seen_sources: dict[str, str] = {}

        for line_number, raw in enumerate(reader, start=2):
            location = f"line {line_number}"
            job_id = (raw.get("job_id") or "").strip()

            if not job_id:
                result.add("DEC-08", label, location,
                           "non-empty job_id", "empty")
                continue
            try:
                require_safe_component(job_id, "job_id")
            except PathSafetyError as exc:
                result.add("INV-05", label, f"{location}.job_id",
                           "filesystem-safe stable identity", str(exc))
                continue
            if job_id != job_id.lower() or not job_id[0].isalnum():
                result.add("DEC-08", label, f"{location}.job_id",
                           "lowercase identity starting with a letter or digit",
                           repr(job_id))
                continue
            if job_id in seen_ids:
                result.add(
                    "ACC-02", label, f"{location}.job_id",
                    "every approved opportunity represented exactly once",
                    f"{job_id!r} already used on line {seen_ids[job_id]}",
                )
                continue
            seen_ids[job_id] = line_number

            employer = (raw.get("employer") or "").strip()
            title = (raw.get("title") or "").strip()
            for field, value in (("employer", employer), ("title", title)):
                if len(value) < 2:
                    result.add("ACC-10", label, f"{location}.{field}",
                               "exact employer/title identity, at least 2 characters",
                               repr(value))

            job_class = (raw.get("job_class") or "").strip().upper()
            if job_class not in {"CORE", "EXCEPTION"}:
                result.add("DEC-03", label, f"{location}.job_class",
                           "CORE or EXCEPTION", repr(job_class))

            cluster = (raw.get("cluster") or "").strip().lower()
            if not cluster:
                result.add("DEC-12", label, f"{location}.cluster",
                           "human-assigned cluster", "empty")

            sequence_raw = (raw.get("sequence") or "").strip()
            try:
                sequence = int(sequence_raw)
                if sequence < 1:
                    raise ValueError
            except ValueError:
                result.add("DEC-12", label, f"{location}.sequence",
                           "positive integer", repr(sequence_raw))
                sequence = 0

            priority = (raw.get("priority") or "NORMAL").strip().upper()
            if priority not in {"HIGH", "NORMAL", "LOW"}:
                result.add("DEC-12", label, f"{location}.priority",
                           "HIGH, NORMAL or LOW", repr(priority))

            source = (raw.get("source") or "").strip()
            if not source:
                result.add("CTR-01", label, f"{location}.source",
                           "path to the original vacancy file", "empty")
            else:
                normalized = source.replace("\\", "/").lower()
                if normalized in seen_sources:
                    result.add(
                        "INV-05", label, f"{location}.source",
                        "each vacancy source used by exactly one job",
                        f"{source!r} already used by job "
                        f"{seen_sources[normalized]!r}",
                    )
                seen_sources[normalized] = job_id

            exception_note = _clean(raw.get("exception_note"))
            if job_class == "EXCEPTION" and not exception_note:
                result.add(
                    "DEC-03", label, f"{location}.exception_note",
                    "a human-readable reason for every EXCEPTION",
                    "empty",
                )

            rows.append(
                BatchRow(
                    job_id=job_id,
                    employer=employer,
                    title=title,
                    job_class=job_class if job_class in {"CORE", "EXCEPTION"} else "CORE",
                    cluster=cluster,
                    sequence=sequence,
                    priority=priority if priority in {"HIGH", "NORMAL", "LOW"} else "NORMAL",
                    source=source,
                    unit=_clean(raw.get("unit")),
                    reference=_clean(raw.get("reference")),
                    deadline=_clean(raw.get("deadline")),
                    exception_note=exception_note,
                )
            )

    if not rows and not result.errors:
        result.add("DEC-08", label, "-", "at least one approved opportunity",
                   "no data rows")
    return rows, result


def write_template(path: Path) -> None:
    """Emit an empty operator batch-input file with the approved columns."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        csv.writer(handle).writerow(TEMPLATE_HEADER)
