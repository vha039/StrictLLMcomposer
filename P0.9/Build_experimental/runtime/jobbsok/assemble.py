"""Layer merge: cv_draft -> advocacy_draft -> polish -> final package.

Every semantic artifact is a partial package. Merging is field replacement,
the same contract `merge.effective_cv` uses one level down:

* a field present in a later layer replaces the earlier value;
* a field absent inherits;
* a present empty array clears;
* `employment_overrides` merge by `employment_id`, one entry replacing that
  employment's whole bullet array.

There is no substring matching and no op grammar, so an edit cannot fail to
apply. What each layer changed is visible in the summary instead.
"""

from __future__ import annotations

from typing import Any

from . import signals

CV_FIELDS = ("headline", "profile", "competencies", "tools_line")
LETTER_FIELDS = ("opening", "body_paragraphs", "closing")


def merge_cv(base: dict[str, Any] | None, patch: dict[str, Any] | None) -> dict[str, Any]:
    out = dict(base or {})
    if not patch:
        return out
    for field in CV_FIELDS:
        if field in patch:
            out[field] = patch[field]
    if "employment_overrides" in patch:
        merged = {
            item["employment_id"]: dict(item)
            for item in (out.get("employment_overrides") or [])
            if patch["employment_overrides"]
        }
        for item in patch["employment_overrides"]:
            merged[item["employment_id"]] = dict(item)
        out["employment_overrides"] = [
            merged[key] for key in sorted(merged)
        ]
    return out


def merge_letter(
    base: dict[str, Any] | None, patch: Any, *, patch_present: bool
) -> dict[str, Any] | None:
    if not patch_present:
        return base
    if patch is None:
        return None
    out = dict(base or {})
    for field in LETTER_FIELDS:
        if field in patch:
            out[field] = patch[field]
    return out or None


def _changed_fields(before: dict[str, Any], after: dict[str, Any], prefix: str) -> list[str]:
    changed = []
    for field in set(before) | set(after):
        if before.get(field) != after.get(field):
            changed.append(f"{prefix}.{field}")
    return sorted(changed)


def assemble(
    cv_draft: dict[str, Any],
    advocacy_draft: dict[str, Any] | None = None,
    polish: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Merge the layers into the semantic fields of a final package."""
    cv = dict(cv_draft.get("cv") or {})
    letter: dict[str, Any] | None = None
    form_answers: list[dict[str, Any]] = []
    refs: list[str] = list(cv_draft.get("used_evidence_refs") or [])
    outside: list[str] = list(cv_draft.get("outside_brief_refs") or [])
    changed: dict[str, list[str]] = {}
    writer_note = None

    if advocacy_draft is not None:
        before = dict(cv)
        cv = merge_cv(cv, advocacy_draft.get("cv"))
        letter = merge_letter(
            None, advocacy_draft.get("letter"), patch_present="letter" in advocacy_draft
        )
        if "form_answers" in advocacy_draft:
            form_answers = list(advocacy_draft["form_answers"])
        refs += list(advocacy_draft.get("used_evidence_refs") or [])
        outside += list(advocacy_draft.get("outside_brief_refs") or [])
        changed["advocacy_draft"] = _changed_fields(before, cv, "cv") + (
            ["letter"] if letter else []
        )

    if polish is not None:
        before_cv, before_letter = dict(cv), dict(letter or {})
        before_answers = list(form_answers)
        cv = merge_cv(cv, polish.get("cv"))
        letter = merge_letter(
            letter, polish.get("letter"), patch_present="letter" in polish
        )
        if "form_answers" in polish:
            form_answers = list(polish["form_answers"])
        refs += list(polish.get("added_refs") or [])
        outside += list(polish.get("outside_brief_refs") or [])
        writer_note = polish.get("writer_note")
        changed["polish"] = _changed_fields(before_cv, cv, "cv") + _changed_fields(
            before_letter, letter or {}, "letter"
        )
        if before_answers != form_answers:
            changed["polish"].append("form_answers")

    package: dict[str, Any] = {
        "cv": cv,
        "letter": letter,
        "used_evidence_refs": sorted(dict.fromkeys(refs)),
    }
    if form_answers:
        package["form_answers"] = form_answers
    if writer_note:
        package["writer_note"] = writer_note

    keystones = (advocacy_draft or {}).get("keystones") or []
    disposition = {
        item["id"]: item["disposition"]
        for item in (polish or {}).get("keystone_disposition") or []
    }
    summary = {
        "changed": changed,
        "cv_dynamic_words": signals.cv_dynamic_words(cv),
        "letter_words": signals.letter_words(letter),
        "letter": "present" if letter else "none (CV-only delivery)",
        "form_answers": len(form_answers),
        "keystones": [
            f"{item['id']} {item['function']}: {disposition.get(item['id'], 'undeclared')}"
            for item in keystones
        ],
        "outside_brief_refs": sorted(dict.fromkeys(outside)),
        "undeclared": sorted(set(changed.get("polish", [])) - {
            item["field"] for item in (polish or {}).get("changes") or []
        }),
        "signals": signals.scan(package),
    }
    return package, summary


def render_summary(summary: dict[str, Any]) -> str:
    lines = [
        f"words     : CV {summary['cv_dynamic_words']} dynamic, "
        f"letter {summary['letter_words']} ({summary['letter']})",
    ]
    for layer, fields in summary.get("changed", {}).items():
        lines.append(f"changed   : {layer}: {', '.join(fields) if fields else 'nothing'}")
    if summary.get("keystones"):
        lines.append("keystones : " + "; ".join(summary["keystones"]))
    if summary.get("outside_brief_refs"):
        lines.append("outside   : " + ", ".join(summary["outside_brief_refs"]))
    if summary.get("undeclared"):
        lines.append("undeclared: " + ", ".join(summary["undeclared"]))
    if summary.get("form_answers"):
        lines.append(f"form      : {summary['form_answers']} answer(s)")
    lines.append("signals   : " + (", ".join(summary["signals"]) or "none"))
    return "\n".join(lines)
