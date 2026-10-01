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
    mapping = stages.get("role_mapping", {})
    if not isinstance(mapping, dict):
        raise ConfigurationError(
            f"{path.name}: [stages.role_mapping] must be a table of "
            f"capability role -> model/surface actually used. Found {mapping!r}."
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
    stages = data.get("stages", {})
    render = data["render"]
    capacity = data.get("capacity", {})
    return {
        "language": data["product"]["language"],
        "personality": {
            "max_selected_facets": data["personality"]["max_selected_facets"],
        },
        "role_mapping": dict(stages.get("role_mapping", {})),
        "capacity": {
            "cv_dynamic_words": int(capacity.get("cv_dynamic_words", 520)),
            "letter_words": int(capacity.get("letter_words", 400)),
        },
        "render": {
            "converter": render["converter"],
            "invocation_granularity": render["invocation_granularity"],
            "converter_timeout_seconds": render["converter_timeout_seconds"],
        },
    }


def capacity(data: dict[str, Any]) -> dict[str, int]:
    """Editorial capacity signals used by `preview` and the playbooks."""
    values = data.get("capacity", {})
    return {
        "cv_dynamic_words": int(values.get("cv_dynamic_words", 520)),
        "letter_words": int(values.get("letter_words", 400)),
    }


def voice_level(data: dict[str, Any]) -> int:
    return int(data.get("voice", {}).get("social_register_calibration", 2))


def soft_warnings(data: dict[str, Any]) -> dict[str, int]:
    """Editorial thresholds. These emit WARNING and never fail a command."""
    return dict(data.get("render", {}).get("soft_warnings", {}))
