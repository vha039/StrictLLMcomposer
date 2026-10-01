"""Schema loading and validation.

Contract 8.1: report all practical independent violations in one pass, and
identify file, location/field, contract ID, expected and observed
condition. jsonschema's iter_errors gives us the full set rather than the
first failure, which is the behavior the contract asks for.

The schemas are control plane: they are hash-frozen into the manifest, and
every deterministic command verifies them before acting.
"""

from __future__ import annotations

import json
import re
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

from .errors import ConfigurationError, ValidationResult

#: Artifact name -> schema file. Also the canonical list of artifact kinds.
SCHEMA_FILES: dict[str, str] = {
    "manifest": "manifest.schema.json",
    "evidence_index": "evidence_index.schema.json",
    "baseline_map": "baseline_map.schema.json",
    "strategy": "strategy.schema.json",
    "package": "package.schema.json",
    "review": "review.schema.json",
    "failure": "failure.schema.json",
    "render_report": "render_report.schema.json",
    "status": "status.schema.json",
}

#: Governing spec id reported when an artifact violates its schema.
SCHEMA_CONTRACT_ID: dict[str, str] = {
    "manifest": "CTR-01",
    "evidence_index": "DEC-14",
    "baseline_map": "DEC-34",
    "strategy": "CTR-04",
    "package": "CTR-05",
    "review": "CTR-07",
    "failure": "CTR-03",
    "render_report": "DEC-21",
    "status": "DEC-42",
}

FORMAT_CHECKER = FormatChecker()
_RFC3339_DATE_TIME = re.compile(
    r"\A\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}"
    r"(?:\.\d+)?(?:[Zz]|[+-]\d{2}:\d{2})\Z"
)


@FORMAT_CHECKER.checks("date-time")
def _is_rfc3339_date_time(value: object) -> bool:
    if not isinstance(value, str):
        return True
    if _RFC3339_DATE_TIME.fullmatch(value) is None:
        return False
    normalized = value[:10] + "T" + value[11:]
    if normalized[-1] in "Zz":
        normalized = normalized[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None


@lru_cache(maxsize=None)
def _load(schema_dir: str, name: str) -> dict[str, Any]:
    if name not in SCHEMA_FILES:
        raise ConfigurationError(
            f"Unknown artifact kind {name!r}. Known: {sorted(SCHEMA_FILES)}"
        )
    path = Path(schema_dir) / SCHEMA_FILES[name]
    if not path.is_file():
        raise ConfigurationError(f"Missing schema: {path}")
    try:
        schema = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ConfigurationError(f"Schema {path.name} is not valid JSON: {exc}") from exc
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        raise ConfigurationError(f"Schema {path.name} is itself invalid: {exc}") from exc
    return schema


def load_schema(schema_dir: Path, name: str) -> dict[str, Any]:
    return _load(str(Path(schema_dir).resolve()), name)


def _pointer(error: Any) -> str:
    parts = [str(p) for p in error.absolute_path]
    return "/" + "/".join(parts) if parts else "/"


def validate_against_schema(
    instance: Any,
    schema_dir: Path,
    name: str,
    *,
    file_label: str,
    result: ValidationResult | None = None,
) -> ValidationResult:
    """Collect every schema violation in one pass."""
    result = result if result is not None else ValidationResult()
    schema = load_schema(schema_dir, name)
    contract_id = SCHEMA_CONTRACT_ID.get(name, "CTR-02")

    errors = sorted(
        Draft202012Validator(
            schema, format_checker=FORMAT_CHECKER
        ).iter_errors(instance),
        key=lambda e: (list(e.absolute_path), e.message),
    )
    for error in errors:
        expected = f"{error.validator}: {error.validator_value!r}"
        # Spec 14.3 wants the observed VALUE, not just a restatement of the
        # rule. jsonschema's const/enum messages omit it, and its messages
        # for container keywords inline the whole rejected object.
        if error.validator in ("const", "enum", "type", "pattern",
                               "minLength", "maxLength", "format"):
            observed = repr(error.instance)
        elif error.validator in ("maxItems", "minItems"):
            observed = f"{len(error.instance)} item(s)"
        elif error.validator in ("required", "additionalProperties",
                                 "minProperties", "maxProperties"):
            observed = error.message
        else:
            observed = error.message
        if len(observed) > 300:
            observed = observed[:297] + "..."
        result.add(
            contract_id=contract_id,
            file=file_label,
            location=_pointer(error),
            expected=expected,
            observed=observed,
        )
    return result


def schema_files(schema_dir: Path) -> list[Path]:
    """Every schema file, for manifest freezing."""
    return sorted(Path(schema_dir).glob("*.schema.json"))
