"""CV baseline reading and the mechanical reference namespace.

`CV_BASELINE.md` is a derived chronology/rendering baseline
(`MECHANICAL_BASELINE`). It may own stable employer/title/date/education
order, employment IDs and default rendering structure, but it never
outranks the three factual authorities and it is never factual evidence
(Spec 4.2, DEC-34).

The generated baseline map is the mechanical namespace: `BL:EMP_*`,
`BL:EDU_*`, `BL:SEC_*`. A factual `used_evidence_ref` that targets this
namespace is a validation error, which is what keeps a baseline identifier
from becoming factual evidence merely by being addressable (ACC-08).

`read_marked_json` is adapted from P0.7 finalize.read_marked_json
(inspected): the baseline JSON lives inside a fenced block between two
HTML comment markers so the file stays human-readable Markdown.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .errors import ConfigurationError, ValidationResult
from .hashing import sha256_file

BASELINE_START = "<!-- CV_BASELINE_DATA_START -->"
BASELINE_END = "<!-- CV_BASELINE_DATA_END -->"

MAP_VERSION = "0.9.0"


def read_marked_json(path: Path, start: str, end: str) -> dict[str, Any]:
    """Extract the single fenced JSON object between two markers."""
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    if text.count(start) != 1 or text.count(end) != 1:
        raise ConfigurationError(
            f"{path.name} must contain exactly one {start}/{end} marker pair."
        )
    marked = text.split(start, 1)[1].split(end, 1)[0]
    match = re.search(r"```json\s*(.*?)\s*```", marked, flags=re.DOTALL)
    if match is None:
        raise ConfigurationError(f"{path.name} marker block lacks one JSON fence.")
    try:
        value = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise ConfigurationError(f"Invalid JSON in {path.name}: {exc}") from exc
    if not isinstance(value, dict):
        raise ConfigurationError(f"Marked JSON in {path.name} must be an object.")
    return value


def read_baseline(path: Path) -> dict[str, Any]:
    return read_marked_json(Path(path), BASELINE_START, BASELINE_END)


def recorded_authority_hashes(path: Path) -> dict[str, str]:
    """Read the authority hashes the baseline author recorded.

    Contract 6.1 requires freeze to carry a recorded human-reviewed
    baseline-to-authorities reconciliation. The baseline file states the
    hashes it was derived from in a Markdown table; freeze compares those
    against the actual bytes and fails on a known conflict.
    """
    text = Path(path).read_text(encoding="utf-8")
    found: dict[str, str] = {}
    for name, digest in re.findall(
        r"\|\s*`([A-Za-z_]+\.md)`\s*\|\s*`([a-f0-9]{64})`\s*\|", text
    ):
        found[name] = digest
    return found


def build_baseline_map(baseline: dict[str, Any], baseline_path: Path) -> dict[str, Any]:
    """Project CV_BASELINE into the mechanical reference namespace."""
    candidate = baseline.get("candidate") or {}

    employments = []
    for item in sorted(
        baseline.get("employment") or [], key=lambda v: v.get("sort_order", 0)
    ):
        employments.append(
            {
                "ref": f"BL:{item['employment_id']}",
                "employment_id": item["employment_id"],
                "sort_order": item["sort_order"],
                "employer": item["employer"],
                "formal_title": item["formal_title"],
                "unit": item.get("unit"),
                "location": item.get("location"),
                "period": item["period"],
                "employment_group_period": item.get("employment_group_period"),
                "default_bullets": list(item["default_bullets"]),
                "always_include": bool(item.get("always_include", True)),
                # Inert. Carried from P0.7's authority_anchor so a human can
                # see where the baseline row came from. Never resolvable as
                # a factual evidence reference (DEC-34).
                "baseline_provenance": item.get("authority_anchor"),
            }
        )

    educations = []
    for item in sorted(
        baseline.get("education") or [], key=lambda v: v.get("sort_order", 0)
    ):
        educations.append(
            {
                "ref": f"BL:{item['education_id']}",
                "education_id": item["education_id"],
                "sort_order": item["sort_order"],
                "institution": item["institution"],
                "qualification": item["qualification"],
                "field": item.get("field"),
                "period": item["period"],
                "status": item.get("status") or None,
                "details": list(item.get("details") or []),
                "include_in_cv": bool(item.get("include_in_cv", True)),
                "baseline_provenance": item.get("authority_anchor"),
            }
        )

    sections = [
        {
            "ref": f"BL:SEC_{item['section_id']}",
            "section_id": item["section_id"],
            "heading": item["heading"],
            "items": list(item.get("items") or []),
        }
        for item in (baseline.get("other_sections") or [])
    ]

    return {
        "artifact_role": "MECHANICAL_BASELINE",
        "map_version": MAP_VERSION,
        "baseline_version": baseline.get("baseline_version", ""),
        "baseline_sha256": sha256_file(Path(baseline_path)),
        "candidate": {
            "full_name": candidate.get("full_name", ""),
            "phone": candidate.get("phone", ""),
            "email": candidate.get("email", ""),
            "location": candidate.get("location", ""),
            "linkedin": candidate.get("linkedin"),
        },
        "employments": employments,
        "educations": educations,
        "languages": list(baseline.get("languages") or []),
        "sections": sections,
        "references_text": baseline.get("references_text", ""),
    }


def check_baseline_map(baseline_map: dict[str, Any]) -> ValidationResult:
    """Mechanical checks beyond schema shape."""
    result = ValidationResult()
    label = "baseline_map.json"

    emp_ids = [e["employment_id"] for e in baseline_map["employments"]]
    duplicates = sorted({i for i in emp_ids if emp_ids.count(i) > 1})
    if duplicates:
        result.add(
            "DEC-23", label, "employments[].employment_id",
            "unique employment IDs",
            f"duplicates: {duplicates}",
        )

    orders = [e["sort_order"] for e in baseline_map["employments"]]
    if len(orders) != len(set(orders)):
        result.add(
            "DEC-23", label, "employments[].sort_order",
            "unique sort_order values",
            f"observed {orders}",
        )

    edu_ids = [e["education_id"] for e in baseline_map["educations"]]
    dup_edu = sorted({i for i in edu_ids if edu_ids.count(i) > 1})
    if dup_edu:
        result.add(
            "DEC-23", label, "educations[].education_id",
            "unique education IDs", f"duplicates: {dup_edu}",
        )

    for employment in baseline_map["employments"]:
        if not employment["default_bullets"]:
            result.add(
                "DEC-23", label, f"employments[{employment['employment_id']}]",
                "at least one default bullet, used when no override is present",
                "empty default_bullets",
            )

    for field in ("full_name", "phone", "email", "location"):
        if not baseline_map["candidate"].get(field):
            result.add(
                "DEC-23", label, f"candidate.{field}",
                "non-empty static identity/contact value", "missing or empty",
            )
    return result


def employment_ids(baseline_map: dict[str, Any]) -> set[str]:
    return {e["employment_id"] for e in baseline_map["employments"]}


def mechanical_refs(baseline_map: dict[str, Any]) -> set[str]:
    """Every valid BL: reference. Used to reject cross-namespace refs."""
    refs = {e["ref"] for e in baseline_map["employments"]}
    refs |= {e["ref"] for e in baseline_map["educations"]}
    refs |= {s["ref"] for s in baseline_map["sections"]}
    return refs


#: The exact keys projected into a stage bundle (OPS O2 4.2). Mechanical
#: chronology only: BL refs are references, never factual evidence, and the
#: frozen map itself stays the renderer/validator authority.
PROJECTED_KEYS: dict[str, tuple[str, ...]] = {
    "candidate": ("full_name", "phone", "email", "location", "linkedin"),
    "employments": (
        "ref", "employment_id", "sort_order", "employer", "formal_title",
        "unit", "location", "period", "employment_group_period",
        "default_bullets", "always_include",
    ),
    "educations": (
        "ref", "education_id", "sort_order", "institution", "qualification",
        "field", "period", "status", "details", "include_in_cv",
    ),
    "languages": ("language", "level"),
    "sections": ("ref", "section_id", "heading", "items"),
}


def _project(record: dict[str, Any], keys: tuple[str, ...]) -> dict[str, Any]:
    # Keep optional values exactly as they occur. A key the source omits is
    # omitted here too; nothing is synthesized with different semantics.
    return {key: record[key] for key in keys if key in record}


def project_baseline_map(baseline_map: dict[str, Any]) -> dict[str, Any]:
    """The compact mechanical projection both active stages receive.

    Map, hash and provenance bookkeeping is omitted; every BL ref is carried
    through unchanged, and default bullets are never hidden because a
    complete override decision depends on seeing them.
    """
    projected: dict[str, Any] = {
        "candidate": _project(
            baseline_map.get("candidate") or {}, PROJECTED_KEYS["candidate"]
        )
    }
    for group in ("employments", "educations", "languages", "sections"):
        projected[group] = [
            _project(record, PROJECTED_KEYS[group])
            for record in baseline_map.get(group) or []
        ]
    if "references_text" in baseline_map:
        projected["references_text"] = baseline_map["references_text"]
    return projected
