"""Dynamic CV merge: baseline plus model-authored zones.

DEC-23 / Contract 13.1. The baseline owns stable chronology, formal
employer/title/date/education identity and order. The model owns exactly
four zones: headline, profile, competencies and employment bullets.

Employment replacement semantics, stated once and implemented once:

* an override is keyed by a known baseline `employment_id`;
* when present, its bullet array **fully replaces** the rendered bullets
  for that employment -- no append, no positional merge, no hidden mixture;
* absence means use the baseline defaults;
* a present **empty** replacement explicitly means "render no bullets for
  this employment" and must NOT silently fall back to the defaults. The
  quality warning for that case lives in artifacts.soft_quality_warnings.

P0.7's finalize.effective_cv already had the correct
`override_map.get(id, default_bullets)` shape (inspected). What it could
not express was the explicit empty replacement, because its schema required
`minItems: 1` on bullets. That is the behavioural difference this module
implements and the tests prove with exact before/after arrays.
"""

from __future__ import annotations

from typing import Any


def effective_cv(baseline_map: dict[str, Any], package: dict[str, Any]) -> dict[str, Any]:
    """Resolve the rendered CV from baseline plus dynamic zones."""
    cv = package.get("cv") or {}
    overrides = {
        item["employment_id"]: list(item["bullets"])
        for item in (cv.get("employment_overrides") or [])
    }

    employments: list[dict[str, Any]] = []
    for entry in sorted(baseline_map["employments"], key=lambda e: e["sort_order"]):
        rendered = dict(entry)
        employment_id = entry["employment_id"]
        if employment_id in overrides:
            # Present override: full replacement, including an empty array.
            rendered["bullets"] = overrides[employment_id]
            rendered["bullet_source"] = "OVERRIDE"
        else:
            rendered["bullets"] = list(entry["default_bullets"])
            rendered["bullet_source"] = "BASELINE_DEFAULT"
        employments.append(rendered)

    return {
        "candidate": dict(baseline_map["candidate"]),
        "headline": cv.get("headline", ""),
        "profile": cv.get("profile", ""),
        "competencies": list(cv.get("competencies") or []),
        "employments": employments,
        "educations": sorted(
            baseline_map["educations"], key=lambda e: e["sort_order"]
        ),
        "languages": list(baseline_map["languages"]),
        "sections": {s["section_id"]: s for s in baseline_map["sections"]},
        "references_text": baseline_map["references_text"],
    }


def employment(effective: dict[str, Any], employment_id: str) -> dict[str, Any] | None:
    for item in effective["employments"]:
        if item["employment_id"] == employment_id:
            return item
    return None


def education(effective: dict[str, Any], education_id: str) -> dict[str, Any] | None:
    for item in effective["educations"]:
        if item["education_id"] == education_id:
            return item
    return None


def previous_employments(
    effective: dict[str, Any], fixed_ids: set[str]
) -> list[dict[str, Any]]:
    """Employments outside the master's fixed zones, in baseline order."""
    return [
        item
        for item in effective["employments"]
        if item["employment_id"] not in fixed_ids and item.get("always_include", True)
    ]


def override_bullets(package: dict[str, Any]) -> dict[str, list[str]]:
    """The raw overrides, for before/after test evidence."""
    return {
        item["employment_id"]: list(item["bullets"])
        for item in ((package.get("cv") or {}).get("employment_overrides") or [])
    }


def baseline_bullets(baseline_map: dict[str, Any]) -> dict[str, list[str]]:
    return {
        item["employment_id"]: list(item["default_bullets"])
        for item in baseline_map["employments"]
    }
