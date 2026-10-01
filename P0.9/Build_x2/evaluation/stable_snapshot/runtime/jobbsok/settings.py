"""Frozen run settings.

policy/settings.toml is control plane. The subset a run depends on is
snapshotted into the manifest at freeze and becomes immutable for that run
(DEC-40). Tuning applies to a new or child run only; the value frozen into
an existing run never changes in place (Spec 15.2).

Read with stdlib tomllib. No configuration framework, no settings
compiler, no surface without a current consumer (Spec 3, Contract 21).
"""

from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any

from .errors import ConfigurationError
from .paths import Layout

SETTINGS_NAME = "settings.toml"

CONVERTERS = {"word_com", "libreoffice", "none", "auto"}
GRANULARITIES = {"per_document", "per_job"}
ROLES = {"SOL_CLASS", "TERRA_CLASS"}


def load(layout: Layout) -> dict[str, Any]:
    return load_path(layout.policy / SETTINGS_NAME)


def load_path(path: Path) -> dict[str, Any]:
    """Load settings from an explicit live or frozen path."""
    if not path.is_file():
        raise ConfigurationError(f"Missing settings: {path}")
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        raise ConfigurationError(f"{path.name} is not valid TOML: {exc}") from exc
    _check(data, path)
    return data


def _check(data: dict[str, Any], path: Path) -> None:
    product = data.get("product", {})
    if product.get("language") != "nb-NO":
        raise ConfigurationError(
            f"{path.name}: [product].language must be 'nb-NO'. The P0.9 core "
            "has no language branch (DEC-04); a non-Bokmal vacancy is an "
            "EXCEPTION in the manifest."
        )

    personality = data.get("personality", {})
    max_facets = personality.get("max_selected_facets")
    if max_facets != 3:
        raise ConfigurationError(
            f"{path.name}: [personality].max_selected_facets must be 3. The "
            "zero-to-three bound is the frozen interface (DEC-35, Spec 9.4)."
        )

    voice = data.get("voice")
    if voice is not None:
        if not isinstance(voice, dict):
            raise ConfigurationError(
                f"{path.name}: [voice] must be a TOML table containing "
                f"social_register_calibration. Found {voice!r}."
            )
        level = voice.get("social_register_calibration")
        if isinstance(level, bool) or not isinstance(level, int) or not 0 <= level <= 3:
            raise ConfigurationError(
                f"{path.name}: [voice].social_register_calibration must be an "
                "integer 0..3. FORFATTERSTEMME.md defines exactly those levels. "
                f"Found {level!r}."
            )

    stages = data.get("stages", {})
    # The active route is Stage 1 then Stage 3 (P0.9.3 amendment). A frozen
    # 0.9.0 settings file still carries stage2; accept and validate it when
    # present so historical runs stay readable, but never require it.
    for key in ("stage1", "stage3"):
        role = stages.get(key)
        if role not in ROLES:
            raise ConfigurationError(
                f"{path.name}: [stages].{key} must be a capability role "
                f"{sorted(ROLES)}, not a commercial model name (DEC-31). "
                f"Found {role!r}."
            )
    legacy_role = stages.get("stage2")
    if legacy_role is not None and legacy_role not in ROLES:
        raise ConfigurationError(
            f"{path.name}: legacy [stages].stage2 must be a capability role "
            f"{sorted(ROLES)}. Found {legacy_role!r}."
        )

    recovery = data.get("recovery", {})
    retry = recovery.get("retry_start_stages", [])
    if not isinstance(retry, list) or any(s not in (1, 2, 3) for s in retry):
        raise ConfigurationError(
            f"{path.name}: [recovery].retry_start_stages must be a list of "
            f"stage numbers from 1..3. Found {retry!r}."
        )
    attempts = recovery.get("mechanical_correction_attempts", 1)
    if not isinstance(attempts, int) or attempts < 0:
        raise ConfigurationError(
            f"{path.name}: [recovery].mechanical_correction_attempts must be a "
            f"non-negative integer. Found {attempts!r}."
        )

    render = data.get("render", {})
    if render.get("converter") not in CONVERTERS:
        raise ConfigurationError(
            f"{path.name}: [render].converter must be one of "
            f"{sorted(CONVERTERS)}. Found {render.get('converter')!r}."
        )
    if render.get("invocation_granularity") not in GRANULARITIES:
        raise ConfigurationError(
            f"{path.name}: [render].invocation_granularity must be one of "
            f"{sorted(GRANULARITIES)}."
        )
    timeout = render.get("converter_timeout_seconds")
    if not isinstance(timeout, int) or timeout < 1:
        raise ConfigurationError(
            f"{path.name}: [render].converter_timeout_seconds must be a "
            f"positive integer. Found {timeout!r}."
        )


def snapshot(data: dict[str, Any]) -> dict[str, Any]:
    """The subset frozen into the manifest."""
    stages = data["stages"]
    recovery = data["recovery"]
    render = data["render"]
    return {
        "language": data["product"]["language"],
        "personality": {
            "max_selected_facets": data["personality"]["max_selected_facets"],
        },
        "stages": {
            "stage1": stages["stage1"],
            "stage3": stages["stage3"],
            "role_mapping": dict(stages.get("role_mapping", {})),
        },
        "recovery": {
            "mechanical_correction_attempts": recovery["mechanical_correction_attempts"],
            "retry_start_stages": list(recovery["retry_start_stages"]),
        },
        "render": {
            "converter": render["converter"],
            "invocation_granularity": render["invocation_granularity"],
            "converter_timeout_seconds": render["converter_timeout_seconds"],
        },
    }


def soft_warnings(data: dict[str, Any]) -> dict[str, int]:
    """Editorial thresholds. These emit WARNING and never fail a command."""
    return dict(data.get("render", {}).get("soft_warnings", {}))
