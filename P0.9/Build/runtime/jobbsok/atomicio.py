"""Atomic writes and ownership-checked promotion of employer-facing files.

Spec 5.6: deterministic operations must be safely rerunnable; writes that
could leave misleading partial files use temporary output and atomic
promotion; a failed replacement preserves prior valid outputs; no command
silently falls back to stale output.

Spec 16.6 / ACC-17: a human-edited DOCX is a post-pipeline submission
artifact. Deterministic rerender must not silently overwrite it.

P0.7's finalize.render_job promoted a whole directory -- rmtree(dest) then
os.replace(temp, dest). That destroys prior valid output before the new
output is known good, and cannot distinguish a human-edited file from a
pipeline file. Promotion here is per file and compares the destination
against the hash this pipeline last wrote, which is recorded in the render
report. No document version management is implied or built.
"""

from __future__ import annotations

import json
import os
import secrets
import tempfile
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any

from .errors import ConfigurationError

from .hashing import pretty_json_bytes, sha256_file


# --------------------------------------------------------------------------
# Atomic writes
# --------------------------------------------------------------------------

def atomic_write_bytes(path: Path, data: bytes) -> None:
    """Write via a sibling temp file plus os.replace.

    The temp file lives in the destination directory so the rename stays on
    one volume, which is what makes it atomic (GATE-08).
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        "wb",
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
        delete=False,
    )
    temporary = Path(handle.name)
    try:
        with handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink(missing_ok=True)


def atomic_write_text(path: Path, text: str) -> None:
    """UTF-8, LF line endings. Stable bytes matter because they get hashed."""
    atomic_write_bytes(path, text.encode("utf-8"))


def atomic_write_json(path: Path, value: Any) -> None:
    atomic_write_bytes(path, pretty_json_bytes(value))


def read_json(path: Path) -> Any:
    """Read JSON with a diagnostic that names the file and position."""
    path = Path(path)
    raw = path.read_text(encoding="utf-8")
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ConfigurationError(
            f"{path.name} is not valid JSON at line {exc.lineno} column "
            f"{exc.colno}: {exc.msg}"
        ) from exc


# --------------------------------------------------------------------------
# Ownership-checked promotion
# --------------------------------------------------------------------------

class Promotion(Enum):
    """What happened to one output file."""

    CREATED = "CREATED"  # destination did not exist
    REPLACED = "REPLACED"  # destination matched the hash we last wrote
    REFUSED_FOREIGN = "REFUSED_FOREIGN"  # destination changed since we wrote it
    FORCED = "FORCED"  # foreign destination replaced under explicit --force
    DIVERTED = "DIVERTED"  # written to an alternate destination instead


@dataclass(frozen=True)
class PromotionResult:
    outcome: Promotion
    destination: Path
    note: str = ""

    @property
    def promoted(self) -> bool:
        return self.outcome is not Promotion.REFUSED_FOREIGN


def promote_file(
    source: Path,
    destination: Path,
    *,
    expected_sha256: str | None,
    force: bool = False,
    alternate_destination: Path | None = None,
) -> PromotionResult:
    """Move a verified temp output into place without clobbering human edits.

    `expected_sha256` is the hash this pipeline recorded for `destination`
    on its last successful render, or None if it never wrote one. A
    destination that exists but does not match is treated as human-owned.

    The source file is left in place on refusal so the caller can report a
    real alternative rather than having silently lost the new output.
    """
    source = Path(source)
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)

    if not destination.exists():
        os.replace(source, destination)
        return PromotionResult(Promotion.CREATED, destination)

    actual = sha256_file(destination)
    if expected_sha256 is not None and actual == expected_sha256:
        os.replace(source, destination)
        return PromotionResult(Promotion.REPLACED, destination)

    reason = (
        "no prior render recorded a hash for this file"
        if expected_sha256 is None
        else "content differs from the hash this pipeline last wrote"
    )

    if force:
        os.replace(source, destination)
        return PromotionResult(
            Promotion.FORCED,
            destination,
            f"replaced under --force; {reason}",
        )

    if alternate_destination is not None:
        alternate = Path(alternate_destination)
        alternate.parent.mkdir(parents=True, exist_ok=True)
        os.replace(source, alternate)
        return PromotionResult(
            Promotion.DIVERTED,
            alternate,
            f"existing file kept; {reason}",
        )

    return PromotionResult(
        Promotion.REFUSED_FOREIGN,
        destination,
        f"existing file preserved because {reason}. "
        "Rerun with --force to overwrite it, or with --dest to write elsewhere.",
    )


# --------------------------------------------------------------------------
# Render transaction workspace
# --------------------------------------------------------------------------

class TransactionDir:
    """An isolated staging directory removed on exit.

    `inherit_parent_permissions` exists for the employer-facing render
    workspace and for nothing else. On the supported Windows target
    `tempfile.mkdtemp` creates the directory with mode 0o700, which produces a
    *protected* security descriptor -- SYSTEM, Administrators and OWNER RIGHTS
    only, no inheritance -- and a file moved out of it carries that descriptor
    to its destination. Whenever the rendering identity differs from the
    reading identity the promoted deliverable is then unreadable by the human
    (ISS-13). `Path.mkdir(mode=0o777)` inherits normally, which is the fix.

    The default stays private: on POSIX 0o700 is a genuine and intended
    permission mode, and the rollback snapshots in cli.py want that privacy.
    """

    def __init__(
        self,
        parent: Path,
        prefix: str = "render",
        *,
        inherit_parent_permissions: bool = False,
    ) -> None:
        self.parent = Path(parent)
        self.prefix = prefix
        self.inherit_parent_permissions = inherit_parent_permissions
        self.path: Path | None = None

    def __enter__(self) -> Path:
        self.parent.mkdir(parents=True, exist_ok=True)
        if not self.inherit_parent_permissions:
            self.path = Path(
                tempfile.mkdtemp(prefix=f".{self.prefix}.", dir=self.parent)
            )
            return self.path

        for _ in range(100):
            candidate = self.parent / f".{self.prefix}.{secrets.token_hex(4)}"
            try:
                candidate.mkdir(mode=0o777)
            except FileExistsError:
                continue
            self.path = candidate
            return self.path
        raise FileExistsError(
            f"Could not allocate transaction directory below {self.parent}"
        )

    def __exit__(self, *exc_info: object) -> None:
        if self.path is not None and self.path.exists():
            import shutil

            shutil.rmtree(self.path, ignore_errors=True)
