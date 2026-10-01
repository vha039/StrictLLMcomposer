from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
from datetime import date
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unicodedata
from typing import Any
from zipfile import ZIP_DEFLATED, ZipFile

from docx import Document
from docx.shared import Mm
from lxml import etree
import pymupdf

try:
    from jsonschema import Draft202012Validator
except ImportError:  # Runtime compatibility fallback; normal installs use jsonschema.
    Draft202012Validator = None


BASELINE_START = "<!-- CV_BASELINE_DATA_START -->"
BASELINE_END = "<!-- CV_BASELINE_DATA_END -->"
SCHEMA_START = "<!-- PACKAGE_SCHEMA_START -->"
SCHEMA_END = "<!-- PACKAGE_SCHEMA_END -->"

JOB_RE = re.compile(r"^B[0-9]{2}_J[0-9]{3}_[a-z0-9_]+$")
BATCH_RE = re.compile(r"^B[0-9]{2}$")
MACRO_CLUSTER_RE = re.compile(r"^B[0-9]{2}_C[0-9]{2}_[a-z0-9_]+$")
MINI_CLUSTER_RE = re.compile(r"^(B[0-9]{2}_C[0-9]{2})[AB]_([a-z0-9_]+)$")
INTERNAL_ID_RE = re.compile(
    r"\b(?:E[0-9]{2,3}|CLM-[A-Z0-9-]+|PRJ-[0-9]{2}(?:-E[0-9]{3})?)\b"
)
INTERNAL_PHRASE_RE = re.compile(
    r"\b(?:decision test|review flag|single backbone|shortlist thesis|"
    r"cluster evidence base|package blueprint)\b",
    re.IGNORECASE,
)
PLACEHOLDER_RE = re.compile(
    r"(?:\{\{|\}\}|\{%|%\}|\bTODO\b|\bTBD\b|\[PLACEHOLDER\]|<[^>\n]{1,80}>)",
    re.IGNORECASE,
)

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "dc": "http://purl.org/dc/elements/1.1/",
    "cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
}
W = f"{{{NS['w']}}}"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"

CV_TAGS = {
    "CV_FUNCTIONAL_IDENTITY": 1,
    "CV_VALUE_PROPOSITION": 1,
    "CV_PROFILE": 1,
    "CV_CORE_COMPETENCE": 1,
    "CV_TOOLS_METHODS": 1,
    "CV_CURRENT_ROLE_TOP_EVIDENCE": 1,
    "CV_SELECTED_EVIDENCE_HEADING": 1,
    "CV_SELECTED_EVIDENCE": 1,
    "CV_EARLY_ROLE_EVIDENCE": 1,
    "CV_RELEVANT_MASTER_SUBJECTS": 1,
    "CV_RELEVANT_BACHELOR_SUBJECTS": 1,
    "CV_SUPPORT_SECTION_1": 1,
    "CV_SUPPORT_SECTION_2": 1,
    "CV_SUPPORT_SECTION_3": 1,
    "CV_OPTIONAL_PREVIOUS_EXPERIENCE": 1,
    "CV_OPTIONAL_TRUST": 1,
    "CV_OPTIONAL_LANGUAGES": 1,
}
APPLICATION_TAGS = {
    "APP_EMPLOYER": 1,
    "APP_UNIT_OPTIONAL": 1,
    "APP_DATE": 1,
    "APP_JOB_TITLE": 2,
    "APP_REFERENCE_OPTIONAL": 1,
    "APPLICATION_BODY": 1,
}

JOB_IDENTITY_FIELDS = {
    "job_id",
    "batch_id",
    "macro_cluster_id",
    "employer",
    "title",
    "unit",
    "reference",
    "language",
    "letter_required",
}
REVIEW_FLAG_HEADINGS = (
    "# Must verify",
    "# Strong but defensible",
    "# Optional polish",
)


class CommonConfigurationError(RuntimeError):
    pass


class JobValidationError(RuntimeError):
    pass


def _job_identity_label(path: Path) -> str:
    return f"job_identity.json at {path}"


def validate_job_identity(
    identity: dict[str, Any],
    *,
    path: Path,
    expected_job_id: str | None = None,
    expected_mini_cluster_id: str | None = None,
) -> None:
    """Validate the compact P0.7 identity anchor and its filesystem placement."""

    label = _job_identity_label(path)
    if set(identity) != JOB_IDENTITY_FIELDS:
        missing = sorted(JOB_IDENTITY_FIELDS - set(identity))
        extra = sorted(set(identity) - JOB_IDENTITY_FIELDS)
        raise JobValidationError(
            f"{label} has invalid fields; missing={missing}, extra={extra}."
        )
    job_id = identity["job_id"]
    batch_id = identity["batch_id"]
    macro = identity["macro_cluster_id"]
    if (
        not isinstance(job_id, str)
        or not JOB_RE.fullmatch(job_id)
        or len(job_id) > 120
    ):
        raise JobValidationError(f"{label} has invalid job_id.")
    if not isinstance(batch_id, str) or not BATCH_RE.fullmatch(batch_id):
        raise JobValidationError(f"{label} has invalid batch_id.")
    if (
        not isinstance(macro, str)
        or not MACRO_CLUSTER_RE.fullmatch(macro)
        or len(macro) > 100
    ):
        raise JobValidationError(f"{label} has invalid macro_cluster_id.")
    if not job_id.startswith(f"{batch_id}_") or not macro.startswith(f"{batch_id}_"):
        raise JobValidationError(f"{label} batch prefix differs from job or macro cluster.")
    if expected_job_id is not None and job_id != expected_job_id:
        raise JobValidationError(
            f"{label} job_id {job_id} differs from folder {expected_job_id}."
        )
    if expected_mini_cluster_id is not None:
        match = MINI_CLUSTER_RE.fullmatch(expected_mini_cluster_id)
        if match is None or len(expected_mini_cluster_id) > 101:
            raise JobValidationError(
                f"Invalid mini-cluster directory: {expected_mini_cluster_id}."
            )
        expected_macro = f"{match.group(1)}_{match.group(2)}"
        if macro != expected_macro:
            raise JobValidationError(
                f"{label} macro_cluster_id {macro} differs from mini-cluster "
                f"{expected_mini_cluster_id}."
            )
    for field in ("employer", "title"):
        value = identity[field]
        if not isinstance(value, str) or not 2 <= len(value.strip()) <= 200:
            raise JobValidationError(f"{label} has invalid {field}.")
    for field in ("unit", "reference"):
        value = identity[field]
        if value is not None and (
            not isinstance(value, str) or not 1 <= len(value.strip()) <= 200
        ):
            raise JobValidationError(f"{label} has invalid {field}.")
    if identity["language"] != "nb-NO":
        raise JobValidationError(f"{label} must use language nb-NO.")
    if not isinstance(identity["letter_required"], bool):
        raise JobValidationError(f"{label} letter_required must be boolean.")


def read_marked_json(path: Path, start: str, end: str) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if text.count(start) != 1 or text.count(end) != 1:
        raise CommonConfigurationError(
            f"{path} must contain exactly one {start}/{end} marker pair."
        )
    marked = text.split(start, 1)[1].split(end, 1)[0]
    match = re.search(r"```json\s*(.*?)\s*```", marked, flags=re.DOTALL)
    if match is None:
        raise CommonConfigurationError(f"{path} marker block lacks one JSON fence.")
    try:
        value = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise CommonConfigurationError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise CommonConfigurationError(f"Marked JSON in {path} must be an object.")
    return value


def _type_matches(value: Any, type_name: str) -> bool:
    return {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        "boolean": isinstance(value, bool),
        "null": value is None,
    }.get(type_name, False)


def _simple_validate(instance: Any, schema: dict[str, Any], path: str = "$") -> None:
    """Validate the exact keyword subset used by the P0.7 package schema."""

    if "oneOf" in schema:
        matches = 0
        messages: list[str] = []
        for option in schema["oneOf"]:
            try:
                _simple_validate(instance, option, path)
                matches += 1
            except ValueError as exc:
                messages.append(str(exc))
        if matches != 1:
            raise ValueError(
                f"{path}: expected exactly one oneOf match, got {matches}; "
                + " | ".join(messages)
            )
        return

    expected_type = schema.get("type")
    if expected_type is not None:
        accepted = expected_type if isinstance(expected_type, list) else [expected_type]
        if not any(_type_matches(instance, item) for item in accepted):
            raise ValueError(f"{path}: expected type {accepted}.")

    if "const" in schema and instance != schema["const"]:
        raise ValueError(f"{path}: expected constant {schema['const']!r}.")
    if "enum" in schema and instance not in schema["enum"]:
        raise ValueError(f"{path}: value is not in enum {schema['enum']!r}.")

    if isinstance(instance, dict):
        required = schema.get("required", [])
        missing = [name for name in required if name not in instance]
        if missing:
            raise ValueError(f"{path}: missing required properties {missing}.")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extra = sorted(set(instance) - set(properties))
            if extra:
                raise ValueError(f"{path}: unknown properties {extra}.")
        for name, value in instance.items():
            if name in properties:
                _simple_validate(value, properties[name], f"{path}.{name}")

    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            raise ValueError(f"{path}: too few items.")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            raise ValueError(f"{path}: too many items.")
        if schema.get("uniqueItems"):
            serialized = [json.dumps(item, sort_keys=True) for item in instance]
            if len(serialized) != len(set(serialized)):
                raise ValueError(f"{path}: items must be unique.")
        if "items" in schema:
            for index, value in enumerate(instance):
                _simple_validate(value, schema["items"], f"{path}[{index}]")

    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            raise ValueError(f"{path}: string is shorter than minLength.")
        if "maxLength" in schema and len(instance) > schema["maxLength"]:
            raise ValueError(f"{path}: string is longer than maxLength.")
        if "pattern" in schema and re.fullmatch(schema["pattern"], instance) is None:
            raise ValueError(f"{path}: string does not match {schema['pattern']}.")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            raise ValueError(f"{path}: number is below minimum.")


def validate_with_schema(instance: dict[str, Any], schema: dict[str, Any]) -> None:
    if Draft202012Validator is None:
        _simple_validate(instance, schema)
        return
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        raise CommonConfigurationError(f"PACKAGE_CONTRACT schema is invalid: {exc}") from exc
    errors = sorted(
        Draft202012Validator(schema).iter_errors(instance),
        key=lambda error: list(error.absolute_path),
    )
    if errors:
        details = "; ".join(
            f"{'/'.join(str(part) for part in error.absolute_path) or '$'}: "
            f"{error.message}"
            for error in errors[:8]
        )
        raise ValueError(f"Package schema validation failed: {details}")


def validate_baseline(baseline: dict[str, Any]) -> None:
    if baseline.get("baseline_version") != "0.7.0":
        raise CommonConfigurationError("CV baseline_version must be 0.7.0.")
    candidate = baseline.get("candidate")
    if not isinstance(candidate, dict):
        raise CommonConfigurationError("CV baseline candidate must be an object.")
    for field in ("full_name", "phone", "email", "location"):
        if not isinstance(candidate.get(field), str) or not candidate[field].strip():
            raise CommonConfigurationError(f"CV baseline candidate.{field} is missing.")

    employment = baseline.get("employment")
    if not isinstance(employment, list) or not employment:
        raise CommonConfigurationError("CV baseline employment must be non-empty.")
    employment_ids = [item.get("employment_id") for item in employment]
    if any(not isinstance(item, str) or not item for item in employment_ids):
        raise CommonConfigurationError("Every employment entry needs employment_id.")
    if len(employment_ids) != len(set(employment_ids)):
        raise CommonConfigurationError("CV baseline has duplicate employment IDs.")
    sort_orders = [item.get("sort_order") for item in employment]
    if len(sort_orders) != len(set(sort_orders)):
        raise CommonConfigurationError("CV baseline employment sort_order is not unique.")
    required_employment = {"EMP_OUS_ANALYSE", "EMP_OUS_BAR"}
    if not required_employment.issubset(set(employment_ids)):
        raise CommonConfigurationError(
            f"CV baseline lacks template employment IDs: {sorted(required_employment)}"
        )
    for item in employment:
        for field in (
            "employer",
            "formal_title",
            "period",
            "default_bullets",
            "always_include",
        ):
            if field not in item:
                raise CommonConfigurationError(
                    f"{item['employment_id']} lacks baseline field {field}."
                )
        if not isinstance(item["default_bullets"], list) or not item["default_bullets"]:
            raise CommonConfigurationError(
                f"{item['employment_id']} needs default_bullets."
            )

    education = baseline.get("education")
    if not isinstance(education, list) or not education:
        raise CommonConfigurationError("CV baseline education must be non-empty.")
    education_ids = [item.get("education_id") for item in education]
    if len(education_ids) != len(set(education_ids)):
        raise CommonConfigurationError("CV baseline has duplicate education IDs.")
    if not isinstance(baseline.get("languages"), list) or not baseline["languages"]:
        raise CommonConfigurationError("CV baseline languages must be non-empty.")
    if not isinstance(baseline.get("other_sections"), list):
        raise CommonConfigurationError("CV baseline other_sections must be an array.")
    if not isinstance(baseline.get("references_text"), str):
        raise CommonConfigurationError("CV baseline references_text must be a string.")


def effective_cv(
    baseline: dict[str, Any],
    package: dict[str, Any],
) -> dict[str, Any]:
    overrides = package["cv_overrides"]
    override_map = {
        item["employment_id"]: item["bullets"]
        for item in overrides["experience_overrides"]
    }
    employment: list[dict[str, Any]] = []
    for item in sorted(baseline["employment"], key=lambda value: value["sort_order"]):
        rendered = dict(item)
        rendered["bullets"] = override_map.get(
            item["employment_id"], item["default_bullets"]
        )
        employment.append(rendered)
    return {
        "candidate": baseline["candidate"],
        "profile": overrides["profile"],
        "key_competencies": overrides["key_competencies"],
        "employment": employment,
        "education": sorted(
            baseline["education"], key=lambda value: value["sort_order"]
        ),
        "languages": baseline["languages"],
        "other_sections": baseline["other_sections"],
        "references_text": baseline["references_text"],
    }


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text.strip()))


def employer_facing_text(package: dict[str, Any]) -> str:
    chunks: list[str] = [package["job"]["employer"], package["job"]["title"]]
    overrides = package["cv_overrides"]
    chunks.append(overrides["profile"])
    chunks.extend(overrides["key_competencies"])
    for item in overrides["experience_overrides"]:
        chunks.extend(item["bullets"])
    application = package["application"]
    if application:
        chunks.extend(
            [
                application["opening"],
                *application["body_paragraphs"],
                application["closing"],
            ]
        )
    for item in package["portal_answers"]:
        chunks.extend([item["question"], item["answer"]])
    return "\n".join(chunks)


def validate_visible_text(text: str, label: str) -> None:
    if PLACEHOLDER_RE.search(text):
        raise JobValidationError(f"{label} contains an unresolved placeholder.")
    if INTERNAL_ID_RE.search(text) or INTERNAL_PHRASE_RE.search(text):
        raise JobValidationError(f"{label} exposes internal evidence/strategy metadata.")


def validate_package(
    package: dict[str, Any],
    *,
    schema: dict[str, Any],
    baseline: dict[str, Any],
    job_id: str,
    identity: dict[str, Any],
    mini_cluster_id: str,
    draft: dict[str, Any] | None,
) -> None:
    try:
        validate_with_schema(package, schema)
    except CommonConfigurationError:
        raise
    except Exception as exc:
        raise JobValidationError(str(exc)) from exc

    if package["source_stage"] != "STAGE4_FINAL":
        raise JobValidationError("Finalization requires source_stage STAGE4_FINAL.")
    if package["job"]["job_id"] != job_id:
        raise JobValidationError(
            f"Package job_id {package['job']['job_id']} differs from folder {job_id}."
        )
    package_job = package["job"]
    expected_job = {
        **identity,
        "mini_cluster_id": mini_cluster_id,
    }
    for field, expected in expected_job.items():
        observed = package_job.get(field)
        if observed != expected:
            raise JobValidationError(
                f"Package job.{field} differs from job_identity.json "
                f"({observed!r} != {expected!r})."
            )
    if not package_job["mini_cluster_id"].startswith(f"{identity['batch_id']}_"):
        raise JobValidationError("Package mini_cluster_id has wrong batch prefix.")
    if package["cv_overrides"]["baseline_version"] != baseline["baseline_version"]:
        raise JobValidationError("Package baseline_version differs from CV baseline.")

    application = package["application"]
    letter_required = package["job"]["letter_required"]
    if letter_required and application is None:
        raise JobValidationError("letter_required=true requires application content.")
    if not letter_required and application is not None:
        raise JobValidationError("letter_required=false requires application=null.")

    baseline_ids = {
        item["employment_id"] for item in baseline["employment"]
    }
    override_ids = [
        item["employment_id"]
        for item in package["cv_overrides"]["experience_overrides"]
    ]
    unknown = sorted(set(override_ids) - baseline_ids)
    if unknown:
        raise JobValidationError(f"Unknown employment IDs: {unknown}")
    if len(override_ids) != len(set(override_ids)):
        raise JobValidationError("Duplicate employment IDs in CV overrides.")

    for answer in package["portal_answers"]:
        if answer["max_words"] is not None:
            observed = word_count(answer["answer"])
            if observed > answer["max_words"]:
                raise JobValidationError(
                    f"Portal {answer['question_id']} exceeds word limit "
                    f"({observed}/{answer['max_words']})."
                )
        if answer["max_chars"] is not None:
            observed = len(answer["answer"])
            if observed > answer["max_chars"]:
                raise JobValidationError(
                    f"Portal {answer['question_id']} exceeds character limit "
                    f"({observed}/{answer['max_chars']})."
                )

    validate_visible_text(employer_facing_text(package), "Employer-facing package")

    if draft is None:
        raise JobValidationError("Missing adjacent draft_package.json.")
    try:
        validate_with_schema(draft, schema)
    except Exception as exc:
        raise JobValidationError(f"Draft package is invalid: {exc}") from exc
    if draft["source_stage"] != "STAGE3_DRAFT":
        raise JobValidationError("Draft package must use source_stage STAGE3_DRAFT.")
    if draft["job"] != package["job"]:
        raise JobValidationError("Draft and final job identity differ.")
    if (
        draft["cv_overrides"]["baseline_version"]
        != package["cv_overrides"]["baseline_version"]
    ):
        raise JobValidationError("Draft and final baseline versions differ.")
    draft_ids = {
        item["employment_id"]
        for item in draft["cv_overrides"]["experience_overrides"]
    }
    final_ids = set(override_ids)
    if not final_ids.issubset(draft_ids):
        raise JobValidationError(
            "Stage 4 introduced a new employment ID not present in the draft."
        )


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise JobValidationError(f"Cannot read {path.name}: {exc}") from exc
    if not isinstance(value, dict):
        raise JobValidationError(f"{path.name} must contain one JSON object.")
    return value


def filename_component(value: str) -> str:
    ascii_text = (
        unicodedata.normalize("NFKD", value)
        .encode("ascii", "ignore")
        .decode("ascii")
    )
    compact = re.sub(r"[^A-Za-z0-9]+", "_", ascii_text).strip("_")
    return (compact or "document")[:70]


def template_tags(path: Path) -> Counter[str]:
    with ZipFile(path) as archive:
        root = etree.fromstring(archive.read("word/document.xml"))
    return Counter(root.xpath("//w:sdtPr/w:tag/@w:val", namespaces=NS))


def require_template_contract(path: Path, expected: dict[str, int]) -> None:
    if not path.is_file():
        raise CommonConfigurationError(f"Missing Word master: {path}")
    actual = template_tags(path)
    if actual != Counter(expected):
        raise CommonConfigurationError(
            f"{path.name} content-control contract mismatch. "
            f"Expected {dict(expected)}; found {dict(actual)}."
        )


def visible_docx_text(path: Path) -> str:
    document = Document(path)
    chunks = [paragraph.text for paragraph in document.paragraphs]
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                chunks.extend(paragraph.text for paragraph in cell.paragraphs)
    return "\n".join(chunk for chunk in chunks if chunk)


def normalized_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def validate_template_static_baseline(
    cv_template: Path,
    baseline: dict[str, Any],
) -> None:
    text = normalized_text(visible_docx_text(cv_template))
    candidate = baseline["candidate"]
    employment = {
        item["employment_id"]: item for item in baseline["employment"]
    }
    current = employment["EMP_OUS_ANALYSE"]
    early = employment["EMP_OUS_BAR"]
    education = {
        item["education_id"]: item
        for item in baseline["education"]
        if item.get("include_in_cv", True)
    }
    expected = [
        candidate["full_name"].upper(),
        f"{candidate['location']} | {candidate['phone']} | {candidate['email']}",
        (
            f"{current['formal_title']} | {current['employer']} "
            f"{current['employment_group_period']}"
        ),
        f"{current['unit']} {current['period']}",
        f"{early['unit']} {early['period']}",
        (
            f"{education['EDU_UIA_AI']['qualification']} | "
            f"{education['EDU_UIA_AI']['institution']} "
            f"{education['EDU_UIA_AI']['period']}"
        ),
        "Pågående.",
        (
            f"{education['EDU_NTNU_ECON']['qualification']} | "
            f"{education['EDU_NTNU_ECON']['institution']} "
            f"{education['EDU_NTNU_ECON']['period']}"
        ),
        (
            f"{education['EDU_UIB_ECON']['qualification']} | "
            f"{education['EDU_UIB_ECON']['institution']} "
            f"{education['EDU_UIB_ECON']['period']}"
        ),
    ]
    missing = [
        item for item in expected if normalized_text(item) not in text
    ]
    if missing:
        raise CommonConfigurationError(
            "CV master static furniture differs from CV baseline: "
            + "; ".join(missing)
        )


def replace_run_text(run: etree._Element, text: str) -> None:
    run_properties = run.find(f"{W}rPr")
    for child in list(run):
        if child is not run_properties:
            run.remove(child)
    lines = text.split("\n")
    for line_index, line in enumerate(lines):
        if line_index:
            run.append(etree.Element(f"{W}br"))
        pieces = line.split("\t")
        for piece_index, piece in enumerate(pieces):
            if piece_index:
                run.append(etree.Element(f"{W}tab"))
            node = etree.Element(f"{W}t")
            if piece.startswith(" ") or piece.endswith(" "):
                node.set(XML_SPACE, "preserve")
            node.text = piece
            run.append(node)


def replace_paragraph_text(paragraph: etree._Element, text: str) -> None:
    run_template = paragraph.find(".//w:r", namespaces=NS)
    paragraph_properties = paragraph.find(f"{W}pPr")
    for child in list(paragraph):
        if child is not paragraph_properties:
            paragraph.remove(child)
    run = deepcopy(run_template) if run_template is not None else etree.Element(f"{W}r")
    replace_run_text(run, text)
    paragraph.append(run)


def fill_inline(root: etree._Element, tag: str, value: str) -> None:
    matches = root.xpath(
        f'.//w:sdt[w:sdtPr/w:tag/@w:val="{tag}"]',
        namespaces=NS,
    )
    if not matches:
        raise KeyError(f"Missing inline content control: {tag}")
    for control in matches:
        content = control.find(f"{W}sdtContent")
        if content is None:
            raise ValueError(f"{tag} has no content.")
        children = list(content)
        run = deepcopy(children[0]) if children else etree.Element(f"{W}r")
        if run.tag != f"{W}r":
            raise ValueError(f"{tag} is not an inline content control.")
        replace_run_text(run, value)
        for child in list(content):
            content.remove(child)
        content.append(run)


def fill_block(
    root: etree._Element,
    tag: str,
    items: list[tuple[int, str]],
) -> None:
    matches = root.xpath(
        f'.//w:sdt[w:sdtPr/w:tag/@w:val="{tag}"]',
        namespaces=NS,
    )
    if len(matches) != 1:
        raise KeyError(f"Expected one block content control {tag}; found {len(matches)}.")
    content = matches[0].find(f"{W}sdtContent")
    if content is None:
        raise ValueError(f"{tag} has no content.")
    templates = [child for child in content if child.tag == f"{W}p"]
    if not templates:
        raise ValueError(f"{tag} has no paragraph template.")
    rendered: list[etree._Element] = []
    for template_index, text in items:
        paragraph = deepcopy(templates[min(template_index, len(templates) - 1)])
        replace_paragraph_text(paragraph, text)
        rendered.append(paragraph)
    for child in list(content):
        content.remove(child)
    for paragraph in rendered:
        content.append(paragraph)


def unwrap_content_controls(root: etree._Element) -> None:
    for control in reversed(root.xpath(".//w:sdt", namespaces=NS)):
        parent = control.getparent()
        if parent is None:
            continue
        insert_at = parent.index(control)
        content = control.find(f"{W}sdtContent")
        if content is not None:
            for child in list(content):
                content.remove(child)
                parent.insert(insert_at, child)
                insert_at += 1
        parent.remove(control)


def write_filled_docx(
    template_path: Path,
    output_path: Path,
    edit_document,
    *,
    title: str,
    subject: str,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(template_path) as source:
        document_root = etree.fromstring(source.read("word/document.xml"))
        edit_document(document_root)
        unwrap_content_controls(document_root)
        document_bytes = etree.tostring(
            document_root,
            xml_declaration=True,
            encoding="UTF-8",
            standalone="yes",
        )

        core_root = etree.fromstring(source.read("docProps/core.xml"))
        for xpath, value in (
            ("./dc:title", title),
            ("./dc:subject", subject),
            ("./dc:creator", "Vegard Håland"),
            ("./cp:lastModifiedBy", "Vegard Håland"),
        ):
            nodes = core_root.xpath(xpath, namespaces=NS)
            if nodes:
                nodes[0].text = value
        core_bytes = etree.tostring(
            core_root,
            xml_declaration=True,
            encoding="UTF-8",
            standalone="yes",
        )

        with ZipFile(output_path, "w", ZIP_DEFLATED) as target:
            for item in source.infolist():
                if item.filename == "word/document.xml":
                    target.writestr(item, document_bytes)
                elif item.filename == "docProps/core.xml":
                    target.writestr(item, core_bytes)
                else:
                    target.writestr(item, source.read(item.filename))


def cv_blocks(effective: dict[str, Any]) -> dict[str, list[tuple[int, str]]]:
    employment = {
        item["employment_id"]: item for item in effective["employment"]
    }
    current = employment["EMP_OUS_ANALYSE"]
    early = employment["EMP_OUS_BAR"]
    previous = [
        item
        for item in effective["employment"]
        if item["employment_id"] not in {"EMP_OUS_ANALYSE", "EMP_OUS_BAR"}
        and item["always_include"]
    ]
    education = {
        item["education_id"]: item
        for item in effective["education"]
        if item.get("include_in_cv", True)
    }
    other = {item["section_id"]: item for item in effective["other_sections"]}
    key_competencies = effective["key_competencies"]
    functional_identity = " | ".join(key_competencies[:3]).upper()

    previous_items: list[tuple[int, str]] = []
    if previous:
        previous_items.append((0, "TIDLIGERE ERFARING"))
        for item in previous:
            unit = f", {item['unit']}" if item.get("unit") else ""
            # P0.6.1 hardening: older employments use effective bullets too.
            # An override must never silently fall back to default_bullets.
            summary = " • ".join(item["bullets"])
            previous_items.append(
                (
                    1,
                    f"{item['period']}  |  {item['formal_title']}, "
                    f"{item['employer']}{unit} — {summary}",
                )
            )

    trust = other.get("OTHER_TRUST")
    courses = other.get("OTHER_COURSES")
    return {
        "CV_FUNCTIONAL_IDENTITY": [(0, functional_identity)],
        "CV_VALUE_PROPOSITION": [],
        "CV_PROFILE": [(0, effective["profile"])],
        "CV_CORE_COMPETENCE": [
            (0, "KJERNEOMRÅDER  " + " · ".join(key_competencies))
        ],
        "CV_TOOLS_METHODS": [],
        "CV_CURRENT_ROLE_TOP_EVIDENCE": [
            (0, item) for item in current["bullets"]
        ],
        "CV_SELECTED_EVIDENCE_HEADING": [],
        "CV_SELECTED_EVIDENCE": [],
        "CV_EARLY_ROLE_EVIDENCE": [(0, item) for item in early["bullets"]],
        "CV_RELEVANT_MASTER_SUBJECTS": [
            (0, item) for item in education["EDU_NTNU_ECON"]["details"]
        ],
        "CV_RELEVANT_BACHELOR_SUBJECTS": [
            (0, item) for item in education["EDU_UIB_ECON"]["details"]
        ],
        "CV_SUPPORT_SECTION_1": (
            [(0, courses["heading"].upper())]
            + [(1, item) for item in courses["items"]]
            if courses
            else []
        ),
        "CV_SUPPORT_SECTION_2": [
            (0, "REFERANSER"),
            (1, effective["references_text"]),
        ],
        "CV_SUPPORT_SECTION_3": [],
        "CV_OPTIONAL_PREVIOUS_EXPERIENCE": previous_items,
        "CV_OPTIONAL_TRUST": (
            [(0, trust["heading"].upper())]
            + [(1, item) for item in trust["items"]]
            if trust
            else []
        ),
        "CV_OPTIONAL_LANGUAGES": [
            (0, "SPRÅK"),
            *[
                (1, f"{item['language']}: {item['level']}")
                for item in effective["languages"]
            ],
        ],
    }


def render_cv(
    template_path: Path,
    output_path: Path,
    package: dict[str, Any],
    effective: dict[str, Any],
) -> None:
    blocks = cv_blocks(effective)

    def edit(root: etree._Element) -> None:
        for tag, items in blocks.items():
            fill_block(root, tag, items)

    write_filled_docx(
        template_path,
        output_path,
        edit,
        title=f"CV – Vegard Håland – {package['job']['title']}",
        subject=f"Jobbsøk_26 P0.7 CV for {package['job']['employer']}",
    )


def render_application(
    template_path: Path,
    output_path: Path,
    package: dict[str, Any],
) -> None:
    application = package["application"]
    if application is None:
        raise ValueError("Package has no application content.")
    job = package["job"]
    norwegian_months = {
        1: "januar",
        2: "februar",
        3: "mars",
        4: "april",
        5: "mai",
        6: "juni",
        7: "juli",
        8: "august",
        9: "september",
        10: "oktober",
        11: "november",
        12: "desember",
    }
    today = date.today()
    document_date = f"{today.day}. {norwegian_months[today.month]} {today.year}"

    def edit(root: etree._Element) -> None:
        fill_inline(root, "APP_EMPLOYER", job["employer"])
        unit = job.get("unit")
        fill_block(
            root,
            "APP_UNIT_OPTIONAL",
            [(0, str(unit))] if unit else [],
        )
        fill_inline(root, "APP_DATE", document_date)
        fill_inline(root, "APP_JOB_TITLE", job["title"])
        reference = job.get("reference")
        fill_block(
            root,
            "APP_REFERENCE_OPTIONAL",
            [(0, f"Referanse: {reference}")] if reference else [],
        )
        paragraphs = [
            application["opening"],
            *application["body_paragraphs"],
            application["closing"],
        ]
        fill_block(root, "APPLICATION_BODY", [(0, item) for item in paragraphs])

    write_filled_docx(
        template_path,
        output_path,
        edit,
        title=f"Søknad – {job['title']} – Vegard Håland",
        subject=f"Jobbsøk_26 P0.7 application for {job['employer']}",
    )


def validate_rendered_docx(
    path: Path,
    *,
    baseline: dict[str, Any],
    effective: dict[str, Any],
) -> None:
    with ZipFile(path) as archive:
        root = etree.fromstring(archive.read("word/document.xml"))
        if root.xpath(".//w:sdt", namespaces=NS):
            raise JobValidationError(f"{path.name} still contains content controls.")
    text = visible_docx_text(path)
    validate_visible_text(text, path.name)
    if "CV_" in path.name:
        candidate = baseline["candidate"]
        required = [
            candidate["full_name"],
            candidate["phone"],
            candidate["email"],
            "Master i samfunnsøkonomi",
            "Bachelor i samfunnsøkonomi",
        ]
        for item in effective["employment"]:
            if item["always_include"]:
                required.extend([item["employer"], item["formal_title"]])
        folded_text = text.casefold()
        missing = [item for item in required if item.casefold() not in folded_text]
        if missing:
            raise JobValidationError(
                f"{path.name} lacks baseline CV content: {sorted(set(missing))}"
            )
    document = Document(path)
    for section in document.sections:
        if abs(section.page_width - Mm(210)) > Mm(1):
            raise JobValidationError(f"{path.name} is not A4 width.")
        if abs(section.page_height - Mm(297)) > Mm(1):
            raise JobValidationError(f"{path.name} is not A4 height.")


def validate_override_bullets_visible(path: Path, package: dict[str, Any]) -> None:
    """Prove every selected employment override reached the rendered CV."""

    rendered = normalized_text(visible_docx_text(path)).casefold()
    missing: list[str] = []
    for override in package["cv_overrides"]["experience_overrides"]:
        for bullet in override["bullets"]:
            if normalized_text(bullet).casefold() not in rendered:
                missing.append(override["employment_id"])
                break
    if missing:
        raise JobValidationError(
            "Schema-allowed employment overrides were not rendered: "
            + ", ".join(sorted(set(missing)))
        )


def locate_soffice(explicit: str | None) -> str:
    if explicit:
        path = Path(explicit)
        if not path.is_file():
            raise CommonConfigurationError(f"Configured soffice does not exist: {path}")
        return str(path)
    for name in ("soffice", "soffice.com", "libreoffice"):
        located = shutil.which(name)
        if located:
            return located
    raise CommonConfigurationError(
        "LibreOffice/soffice not found. Install it or pass --soffice."
    )


def convert_to_pdf(docx_path: Path, soffice: str, timeout_seconds: int = 120) -> Path:
    output_dir = docx_path.parent
    profile = Path(tempfile.mkdtemp(prefix=".lo_profile_", dir=output_dir))
    command = [
        soffice,
        "--headless",
        f"-env:UserInstallation={profile.resolve().as_uri()}",
        "--convert-to",
        "pdf",
        "--outdir",
        str(output_dir),
        str(docx_path),
    ]
    try:
        try:
            completed = subprocess.run(
                command,
                text=True,
                capture_output=True,
                check=False,
                timeout=timeout_seconds,
            )
        except subprocess.TimeoutExpired as exc:
            raise JobValidationError(
                f"PDF conversion timed out for {docx_path.name} after "
                f"{timeout_seconds} seconds."
            ) from exc
        except OSError as exc:
            raise JobValidationError(
                f"Could not start PDF converter for {docx_path.name}: {exc}"
            ) from exc
    finally:
        shutil.rmtree(profile, ignore_errors=True)
    pdf_path = docx_path.with_suffix(".pdf")
    if completed.returncode != 0 or not pdf_path.is_file() or pdf_path.stat().st_size == 0:
        details = (completed.stderr or completed.stdout or "no converter output").strip()
        raise JobValidationError(
            f"PDF conversion failed for {docx_path.name}: {details}"
        )
    return pdf_path


def validate_pdf(path: Path, *, maximum_pages: int | None = None) -> int:
    try:
        with pymupdf.open(path) as document:
            if document.page_count < 1:
                raise JobValidationError(f"{path.name} has no pages.")
            all_text: list[str] = []
            for page in document:
                rect = page.rect
                if abs(rect.width - 595.28) > 3 or abs(rect.height - 841.89) > 3:
                    raise JobValidationError(f"{path.name} contains a non-A4 page.")
                page_text = page.get_text("text") or ""
                if len(page_text.strip()) < 10:
                    raise JobValidationError(f"{path.name} contains a blank page.")
                for block in page.get_text("blocks"):
                    x0, y0, x1, y1 = block[:4]
                    tolerance = 2
                    if (
                        x0 < -tolerance
                        or y0 < -tolerance
                        or x1 > rect.width + tolerance
                        or y1 > rect.height + tolerance
                    ):
                        raise JobValidationError(
                            f"{path.name} contains clipped text outside the A4 page."
                        )
                all_text.append(page_text)
            text = "\n".join(all_text)
            if len(text.strip()) < 100:
                raise JobValidationError(f"{path.name} has insufficient selectable text.")
            validate_visible_text(text, path.name)
            if maximum_pages is not None and document.page_count > maximum_pages:
                raise JobValidationError(
                    f"{path.name} exceeds page limit "
                    f"({document.page_count}/{maximum_pages})."
                )
            return document.page_count
    except JobValidationError:
        raise
    except Exception as exc:
        raise JobValidationError(f"Cannot validate PDF {path.name}: {exc}") from exc


def write_portal_answers(path: Path, package: dict[str, Any]) -> None:
    blocks = ["# Portalsvar"]
    for item in package["portal_answers"]:
        blocks.extend(
            [
                "",
                f"## {item['question_id']}",
                "",
                f"**Spørsmål:** {item['question']}",
                "",
                item["answer"],
            ]
        )
        limits: list[str] = []
        if item["max_words"] is not None:
            limits.append(
                f"{word_count(item['answer'])}/{item['max_words']} ord"
            )
        if item["max_chars"] is not None:
            limits.append(
                f"{len(item['answer'])}/{item['max_chars']} tegn"
            )
        if limits:
            blocks.extend(["", f"_Grensekontroll: {'; '.join(limits)}._"])
    path.write_text("\n".join(blocks).rstrip() + "\n", encoding="utf-8")


def review_flag_count(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    return len(re.findall(r"(?m)^##\s+F[0-9]+\b", text))


def validate_review_flags(path: Path) -> None:
    if not path.is_file():
        raise JobValidationError("Missing review_flags.md.")
    text = path.read_text(encoding="utf-8")
    missing = [heading for heading in REVIEW_FLAG_HEADINGS if heading not in text]
    if missing:
        raise JobValidationError(
            "review_flags.md lacks mandatory heading(s): " + ", ".join(missing)
        )
    if re.search(r"(?mi)^#{1,3}\s*(?:PASS|REVISE|BLOCK)\b", text):
        raise JobValidationError(
            "review_flags.md must not use semantic PASS/REVISE/BLOCK verdicts."
        )


def render_job(
    *,
    package: dict[str, Any],
    baseline: dict[str, Any],
    templates_dir: Path,
    output_root: Path,
    review_flags: Path,
    force: bool,
    soffice: str,
    converter_timeout_seconds: int = 120,
) -> dict[str, Any]:
    job = package["job"]
    job_id = job["job_id"]
    destination = output_root / job_id
    if destination.exists() and not force:
        raise JobValidationError(
            f"Output exists for {job_id}; rerun with --force after review."
        )
    validate_review_flags(review_flags)

    effective = effective_cv(baseline, package)
    temporary = Path(
        tempfile.mkdtemp(prefix=f".{job_id}.", dir=output_root)
    )
    try:
        suffix = (
            f"{filename_component(job['employer'])}_"
            f"{filename_component(job['title'])}"
        )
        cv_docx = temporary / f"CV_{suffix}.docx"
        render_cv(
            templates_dir / "CV_MASTER.docx",
            cv_docx,
            package,
            effective,
        )
        validate_rendered_docx(cv_docx, baseline=baseline, effective=effective)
        validate_override_bullets_visible(cv_docx, package)
        cv_pdf = convert_to_pdf(
            cv_docx,
            soffice,
            timeout_seconds=converter_timeout_seconds,
        )
        cv_pages = validate_pdf(cv_pdf, maximum_pages=2)

        application_pages: int | None = None
        if job["letter_required"]:
            application_docx = temporary / f"Application_{suffix}.docx"
            render_application(
                templates_dir / "APPLICATION_MASTER.docx",
                application_docx,
                package,
            )
            validate_rendered_docx(
                application_docx,
                baseline=baseline,
                effective=effective,
            )
            application_pdf = convert_to_pdf(
                application_docx,
                soffice,
                timeout_seconds=converter_timeout_seconds,
            )
            application_pages = validate_pdf(application_pdf, maximum_pages=1)

        if package["portal_answers"]:
            write_portal_answers(temporary / "Portal_answers.md", package)

        private_dir = temporary / "_private"
        private_dir.mkdir()
        shutil.copy2(review_flags, private_dir / "review_flags.md")

        if destination.exists():
            if destination.parent.resolve() != output_root.resolve():
                raise JobValidationError("Refusing to replace output outside output root.")
            shutil.rmtree(destination)
        os.replace(temporary, destination)
        return {
            "cv_pages": cv_pages,
            "application_pages": application_pages,
            "portal_answers": len(package["portal_answers"]),
            "flags": review_flag_count(destination / "_private" / "review_flags.md"),
        }
    finally:
        if temporary.exists():
            shutil.rmtree(temporary, ignore_errors=True)


def discover_expected_jobs(input_root: Path) -> dict[str, Path]:
    """The Stage 4 input identities define the authoritative expected set."""

    if not input_root.is_dir():
        raise CommonConfigurationError(f"Stage 4 input root is missing: {input_root}")
    job_directories = sorted(
        path
        for path in input_root.rglob("*")
        if path.is_dir() and JOB_RE.fullmatch(path.name)
    )
    if not job_directories:
        raise CommonConfigurationError(
            f"No valid job folders found below {input_root}."
        )
    jobs: dict[str, Path] = {}
    for directory in job_directories:
        job_id = directory.name
        path = directory / "job_identity.json"
        if not path.is_file():
            raise CommonConfigurationError(
                f"Expected Stage 4 job folder lacks job_identity.json: {directory}"
            )
        if job_id in jobs:
            raise CommonConfigurationError(
                f"Duplicate expected job identity for {job_id}: {jobs[job_id]} and {path}"
            )
        jobs[job_id] = directory
    return jobs


def discover_completed_packages(source_root: Path) -> dict[str, Path]:
    if not source_root.is_dir():
        raise CommonConfigurationError(f"Stage 4 output root is missing: {source_root}")
    packages: dict[str, Path] = {}
    for path in sorted(source_root.rglob("final_package.json")):
        job_id = path.parent.name
        if not JOB_RE.fullmatch(job_id):
            raise CommonConfigurationError(
                f"Final package is not in a valid job folder: {path}"
            )
        if job_id in packages:
            raise CommonConfigurationError(f"Duplicate final package for {job_id}.")
        packages[job_id] = path
    return packages


def validate_stage4_done(path: Path, job_id: str) -> None:
    if not path.is_file():
        raise JobValidationError("Missing Stage 4 _DONE.md.")
    text = path.read_text(encoding="utf-8")
    required = (
        "Status: COMPLETED",
        "final_package.json",
        "review_flags.md",
        job_id,
        "Model:",
        "Effort:",
    )
    missing = [item for item in required if item not in text]
    if re.search(r"(?m)^Stage:\s*4\s*$", text) is None:
        missing.insert(0, "Stage: 4")
    if missing:
        raise JobValidationError(
            "Stage 4 _DONE.md lacks required evidence: " + ", ".join(missing)
        )


def active_blocker(job_dir: Path) -> bool:
    return (job_dir / "BLOCKED.md").is_file()


def finalize(
    *,
    input_root: Path,
    source_root: Path,
    output_root: Path,
    project_root: Path,
    check_only: bool,
    force: bool,
    soffice_path: str | None,
) -> int:
    context = project_root / "context"
    templates = context / "templates"
    baseline = read_marked_json(
        context / "CV_BASELINE.md", BASELINE_START, BASELINE_END
    )
    schema = read_marked_json(
        context / "PACKAGE_CONTRACT.md", SCHEMA_START, SCHEMA_END
    )
    validate_baseline(baseline)
    require_template_contract(templates / "CV_MASTER.docx", CV_TAGS)
    require_template_contract(
        templates / "APPLICATION_MASTER.docx", APPLICATION_TAGS
    )
    validate_template_static_baseline(templates / "CV_MASTER.docx", baseline)

    expected_jobs = discover_expected_jobs(input_root)
    packages = discover_completed_packages(source_root)
    if not check_only:
        output_root.mkdir(parents=True, exist_ok=True)
    soffice = None if check_only else locate_soffice(soffice_path)
    validated = 0
    rendered = 0
    missing = 0
    failures: list[tuple[str, str]] = []

    print("FINALIZE")
    extra = sorted(set(packages) - set(expected_jobs))
    for job_id in extra:
        failures.append((job_id, "Final package is not present in Stage 4 input."))
        print(f"[FAIL] {job_id} reason=Final package is not present in Stage 4 input.")

    for job_id, expected_dir in sorted(expected_jobs.items()):
        try:
            input_identity_path = expected_dir / "job_identity.json"
            input_identity = load_json(input_identity_path)
            mini_cluster_id = expected_dir.parent.name
            validate_job_identity(
                input_identity,
                path=input_identity_path,
                expected_job_id=job_id,
                expected_mini_cluster_id=mini_cluster_id,
            )
            if active_blocker(expected_dir):
                raise JobValidationError("Active BLOCKED.md in Stage 4 input.")

            final_path = packages.get(job_id)
            if final_path is None:
                missing += 1
                output_candidate = source_root / mini_cluster_id / job_id
                if active_blocker(output_candidate):
                    raise JobValidationError("Active BLOCKED.md in Stage 4 output.")
                raise JobValidationError("Missing final_package.json for expected job.")
            if final_path.parent.parent.name != mini_cluster_id:
                raise JobValidationError(
                    "Final package mini-cluster path differs from Stage 4 input."
                )
            output_dir = final_path.parent
            if active_blocker(output_dir):
                raise JobValidationError("Active BLOCKED.md in Stage 4 output.")
            output_identity_path = output_dir / "job_identity.json"
            output_identity = load_json(output_identity_path)
            validate_job_identity(
                output_identity,
                path=output_identity_path,
                expected_job_id=job_id,
                expected_mini_cluster_id=mini_cluster_id,
            )
            if output_identity != input_identity:
                raise JobValidationError(
                    "Stage 4 output job_identity.json differs from Stage 4 input."
                )
            validate_stage4_done(output_dir / "_DONE.md", job_id)
            package = load_json(final_path)
            draft_path = output_dir / "draft_package.json"
            draft = load_json(draft_path) if draft_path.is_file() else None
            validate_package(
                package,
                schema=schema,
                baseline=baseline,
                job_id=job_id,
                identity=input_identity,
                mini_cluster_id=mini_cluster_id,
                draft=draft,
            )
            flags_path = output_dir / "review_flags.md"
            validate_review_flags(flags_path)
            validated += 1
            if check_only:
                print(
                    f"[PASS] {job_id} CHECK_ONLY "
                    f"Portal={len(package['portal_answers'])} "
                    f"Flags={review_flag_count(flags_path)}"
                )
                continue

            result = render_job(
                package=package,
                baseline=baseline,
                templates_dir=templates,
                output_root=output_root,
                review_flags=flags_path,
                force=force,
                soffice=soffice or "",
            )
            rendered += 1
            application = (
                str(result["application_pages"]) + "p"
                if result["application_pages"] is not None
                else "none"
            )
            print(
                f"[PASS] {job_id} CV={result['cv_pages']}p "
                f"Application={application} "
                f"Portal={result['portal_answers']} Flags={result['flags']}"
            )
        except Exception as exc:
            failures.append((job_id, str(exc)))
            print(f"[FAIL] {job_id} reason={exc}")

    print()
    print("SUMMARY")
    print(f"Expected jobs: {len(expected_jobs)}")
    print(f"Completed packages: {len(packages)}")
    print(f"Validated: {validated}")
    print(f"Rendered: {rendered}")
    print(f"Missing: {missing}")
    print(f"Failed: {len(failures)}")
    print(f"Output root: {output_root}")
    result = "PASS" if not failures else "PARTIAL_FAILURE"
    print(f"Result: {result}")
    return 0 if not failures else 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate and render P0.7 Stage 4 packages."
    )
    parser.add_argument(
        "input_root",
        nargs="?",
        default="stg4_mirror/input",
    )
    parser.add_argument(
        "source_root",
        nargs="?",
        default="stg4_mirror/output",
    )
    parser.add_argument("output_root", nargs="?", default="output")
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root containing context/ and scripts/.",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Validate without writing output files.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace exact existing per-job output after a successful temp render.",
    )
    parser.add_argument(
        "--soffice",
        default=None,
        help="Explicit LibreOffice/soffice executable.",
    )
    args = parser.parse_args()
    if args.check_only and args.force:
        parser.error("--force has no effect with --check-only.")

    project_root = Path(args.root).resolve()
    input_root = (
        Path(args.input_root).resolve()
        if Path(args.input_root).is_absolute()
        else (project_root / args.input_root).resolve()
    )
    source_root = (
        Path(args.source_root).resolve()
        if Path(args.source_root).is_absolute()
        else (project_root / args.source_root).resolve()
    )
    output_root = (
        Path(args.output_root).resolve()
        if Path(args.output_root).is_absolute()
        else (project_root / args.output_root).resolve()
    )
    try:
        exit_code = finalize(
            input_root=input_root,
            source_root=source_root,
            output_root=output_root,
            project_root=project_root,
            check_only=args.check_only,
            force=args.force,
            soffice_path=args.soffice,
        )
    except CommonConfigurationError as exc:
        print(f"FINALIZE CONFIGURATION ERROR: {exc}")
        raise SystemExit(2) from exc
    except Exception as exc:
        print(f"FINALIZE CONFIGURATION ERROR: {exc}")
        raise SystemExit(2) from exc
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
