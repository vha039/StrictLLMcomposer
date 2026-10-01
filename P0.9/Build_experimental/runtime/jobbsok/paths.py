"""Repository layout, safe path handling and write-permission separation.

Three obligations meet here:

* Spec 17.2 / Contract 15 -- deterministic tooling writes only under
  approved roots, rejects traversal, and deliberately handles symlinks and
  reparse points.
* Contract 3 -- authorities, context, policy, templates and schemas are
  protected; only the current run/job output area is model-writable.
* Stage write ownership lives in `pipeline.STAGES`, not here.
"""

from __future__ import annotations

import os
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

from .errors import ConfigurationError, PathSafetyError

# Windows reserved device names. A file called "NUL.json" is not a file.
_RESERVED = {
    "CON", "PRN", "AUX", "NUL",
    *(f"COM{d}" for d in "0123456789"),
    *(f"LPT{d}" for d in "0123456789"),
}
_SAFE_COMPONENT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")

#: A flat canonical run identity.
_FLAT_RUN_ID = re.compile(r"^r[0-9]{8}-[0-9]{6}-[a-f0-9]{6}$")

#: The one permitted child namespace under a root ancestor (DEC-40,
#: ACC-03). stageN is 1 or 3, or 0 when --from-stage was omitted; the
#: label is operator-asserted; the timestamp is the branch moment in UTC.
BRANCHES_DIR = "branches"
_BRANCH_COMPONENT = re.compile(r"^[a-z0-9][a-z0-9_-]{0,31}$")
#: stageN + two separators + at most eight label characters + a
#: sixteen-character timestamp.
MAX_BRANCH_COMPONENT = 32

#: One physical level only. A branch of a branch is a sibling here.
RUN_REFERENCE = re.compile(
    r"^r[0-9]{8}-[0-9]{6}-[a-f0-9]{6}"
    r"(?:/branches/[a-z0-9][a-z0-9_-]{0,31})?$"
)


def split_run_reference(reference: str) -> tuple[str, str | None]:
    """(root run id, branch component or None) for a validated reference."""
    if not isinstance(reference, str) or not reference:
        raise PathSafetyError("run reference must be a non-empty string.")
    if "\\" in reference:
        raise PathSafetyError(
            f"run reference must not contain a backslash: {reference!r}"
        )
    parts = reference.split("/")
    if len(parts) == 1:
        if not _FLAT_RUN_ID.fullmatch(parts[0]):
            raise PathSafetyError(
                f"run reference must be rYYYYMMDD-HHMMSS-xxxxxx or that "
                f"reference followed by /branches/<component>: {reference!r}"
            )
        return parts[0], None
    if len(parts) != 3 or parts[1] != BRANCHES_DIR:
        raise PathSafetyError(
            f"a child run lives at <root>/{BRANCHES_DIR}/<component> and "
            f"nowhere deeper: {reference!r}"
        )
    root, _, component = parts
    if not _FLAT_RUN_ID.fullmatch(root):
        raise PathSafetyError(
            f"run reference root must be a flat canonical run id: {reference!r}"
        )
    if len(component) > MAX_BRANCH_COMPONENT or not _BRANCH_COMPONENT.fullmatch(
        component
    ):
        raise PathSafetyError(
            f"branch component must be lowercase [a-z0-9_-] and at most "
            f"{MAX_BRANCH_COMPONENT} characters: {component!r}"
        )
    require_safe_component(root, "run reference root")
    require_safe_component(component, "branch component")
    return root, component


def flatten_run_reference(reference: str) -> str:
    """Fixed directory key for derived output: '/' becomes '__'."""
    return reference.replace("/", "__")
MAX_COMPONENT = 100
MAX_PATH_CHARS = 240  # conservative; long paths are enabled but not assumed


# --------------------------------------------------------------------------
# Repository layout
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Layout:
    """Resolved roles from Contract 3. Exact paths are implementation freedom."""

    root: Path

    @property
    def authorities(self) -> Path:
        return self.root / "authorities"

    @property
    def context(self) -> Path:
        return self.root / "context"

    @property
    def policy(self) -> Path:
        return self.root / "policy"

    @property
    def templates(self) -> Path:
        return self.root / "templates"

    @property
    def schemas(self) -> Path:
        return self.root / "schemas"

    @property
    def generated(self) -> Path:
        return self.root / "generated"

    @property
    def inbox(self) -> Path:
        return self.root / "inbox"

    @property
    def runs(self) -> Path:
        return self.root / "runs"

    @property
    def pilot(self) -> Path:
        return self.root / "pilot"

    @property
    def evidence(self) -> Path:
        return self.root / "evidence"

    @property
    def protected_roots(self) -> tuple[Path, ...]:
        """Never written by a stage or by ordinary deterministic commands.

        Maintained by the human between runs (Spec 4.1, Contract 3).
        """
        return (
            self.authorities,
            self.context,
            self.policy,
            self.templates,
            self.schemas,
        )

    @property
    def writable_roots(self) -> tuple[Path, ...]:
        return (self.generated, self.runs, self.evidence, self.pilot)

    def run_dir(self, run_id: str) -> Path:
        """The physical directory for a flat or one-level nested reference."""
        root, component = split_run_reference(run_id)
        directory = self.runs / root
        if component is not None:
            directory = directory / BRANCHES_DIR / component
        return directory

    def job_dir(self, run_id: str, job_id: str) -> Path:
        return self.run_dir(run_id) / "jobs" / require_safe_component(job_id, "job_id")

    @classmethod
    def discover(cls, start: Path | None = None) -> "Layout":
        """Find the build root by walking up for pyproject.toml + schemas/."""
        here = (start or Path.cwd()).resolve()
        for candidate in (here, *here.parents):
            if (candidate / "pyproject.toml").is_file() and (
                candidate / "schemas"
            ).is_dir():
                return cls(candidate)
        raise ConfigurationError(
            f"No Jobbsok build root found at or above {here}. "
            "Expected a directory containing pyproject.toml and schemas/."
        )


# --------------------------------------------------------------------------
# Path safety
# --------------------------------------------------------------------------

def is_reparse_point(path: Path) -> bool:
    """True for symlinks and Windows junctions/reparse points.

    Spec 17.2 requires these be handled deliberately rather than followed by
    accident. Checked per component, because a safe-looking leaf can sit
    below a junction that redirects the whole subtree.
    """
    try:
        if path.is_symlink():
            return True
    except OSError:
        return False
    isjunction = getattr(os.path, "isjunction", None)
    if isjunction is not None:
        try:
            if isjunction(path):
                return True
        except OSError:
            return False
    try:
        stat = os.lstat(path)
    except (OSError, ValueError):
        return False
    return bool(getattr(stat, "st_reparse_tag", 0))


def require_safe_component(name: str, label: str = "path component") -> str:
    """Validate a single path component with no filesystem access."""
    if not isinstance(name, str) or not name:
        raise PathSafetyError(f"{label} must be a non-empty string.")
    if "\x00" in name:
        raise PathSafetyError(f"{label} contains a NUL byte.")
    if len(name) > MAX_COMPONENT:
        raise PathSafetyError(
            f"{label} is longer than {MAX_COMPONENT} characters: {name[:40]}..."
        )
    if name in {".", ".."} or "/" in name or "\\" in name:
        raise PathSafetyError(f"{label} must not traverse directories: {name!r}")
    if name != name.strip() or name.endswith("."):
        raise PathSafetyError(
            f"{label} must not begin/end with whitespace or end with a dot: {name!r}"
        )
    if name.split(".", 1)[0].upper() in _RESERVED:
        raise PathSafetyError(f"{label} uses a reserved device name: {name!r}")
    if not _SAFE_COMPONENT.fullmatch(name):
        raise PathSafetyError(
            f"{label} must match [A-Za-z0-9][A-Za-z0-9._-]*: {name!r}"
        )
    return name


def resolve_within(root: Path, candidate: Path | str, *, label: str = "path") -> Path:
    """Resolve a candidate path and prove it stays inside the given root.

    Rejects traversal, absolute escapes, and any reparse point between the
    root and the target -- including one that redirects back inside, because
    following it silently is exactly the behavior 17.2 tells us not to have.
    """
    root_resolved = Path(root).resolve(strict=False)
    raw = Path(candidate)
    target = raw if raw.is_absolute() else root_resolved / raw

    if "\x00" in str(raw):
        raise PathSafetyError(f"{label} contains a NUL byte.")

    resolved = target.resolve(strict=False)
    if resolved != root_resolved and root_resolved not in resolved.parents:
        raise PathSafetyError(
            f"{label} escapes its allowed root.\n"
            f"          root:     {root_resolved}\n"
            f"          resolved: {resolved}"
        )
    if len(str(resolved)) > MAX_PATH_CHARS:
        raise PathSafetyError(
            f"{label} resolves to {len(str(resolved))} characters, over the "
            f"{MAX_PATH_CHARS} limit: {resolved}"
        )

    current = root_resolved
    if is_reparse_point(current):
        raise PathSafetyError(f"Allowed root is a reparse point: {current}")
    try:
        relative = resolved.relative_to(root_resolved)
    except ValueError:  # pragma: no cover - containment already proven
        raise PathSafetyError(f"{label} is not relative to {root_resolved}")
    for part in relative.parts:
        current = current / part
        if not current.exists() and not current.is_symlink():
            break
        if is_reparse_point(current):
            raise PathSafetyError(
                f"{label} passes through a symlink/reparse point: {current}"
            )
    return resolved


def assert_writable(layout: Layout, path: Path, *, label: str = "write target") -> Path:
    """Prove a write target sits under a root deterministic tooling may write."""
    resolved = Path(path).resolve(strict=False)
    for root in layout.writable_roots:
        root_resolved = root.resolve(strict=False)
        if resolved == root_resolved or root_resolved in resolved.parents:
            return resolve_within(root_resolved, resolved, label=label)
    allowed = ", ".join(str(r) for r in layout.writable_roots)
    raise PathSafetyError(
        f"{label} is outside every writable root.\n"
        f"          target:  {resolved}\n"
        f"          allowed: {allowed}"
    )


def assert_protected(layout: Layout, path: Path) -> None:
    """Raise if the given path sits inside a protected input root."""
    resolved = Path(path).resolve(strict=False)
    for root in layout.protected_roots:
        root_resolved = root.resolve(strict=False)
        if resolved == root_resolved or root_resolved in resolved.parents:
            raise PathSafetyError(
                f"Refusing to write inside a protected input root: {resolved}\n"
                f"          protected root: {root_resolved}\n"
                "          Protected inputs change only through human source "
                "maintenance between runs (Spec 4.1, Contract 3)."
            )


def resolve_output_destination(layout: Layout, value: str | Path) -> tuple[Path, bool]:
    """Resolve an explicit human export; return (path, authoritative)."""
    raw = Path(value)
    if not raw.is_absolute():
        if ".." in raw.parts:
            raise PathSafetyError(
                f"Relative output destination must not traverse with '..': {value}"
            )
        return assert_writable(
            layout, layout.root / raw, label="output destination"
        ), True

    if ".." in raw.parts:
        raise PathSafetyError(
            f"Absolute output destination must be normalized without '..': {value}"
        )
    resolved = raw.resolve(strict=False)
    root = layout.root.resolve(strict=False)
    if resolved == root or root in resolved.parents:
        return assert_writable(layout, resolved, label="output destination"), True

    if len(str(resolved)) > MAX_PATH_CHARS:
        raise PathSafetyError(
            f"output destination is longer than {MAX_PATH_CHARS} characters: {resolved}"
        )
    current = Path(resolved.anchor)
    for part in resolved.parts[1:]:
        current = current / part
        if not current.exists() and not current.is_symlink():
            break
        if is_reparse_point(current):
            raise PathSafetyError(
                f"output destination passes through a symlink/reparse point: {current}"
            )
    return resolved, False


#: Norwegian letters NFKD does not decompose. Without these, P0.7's fold
#: silently DELETES them: "Rådgiver økonomi" became "Radgiver konomi" on a
#: file the candidate sends to an employer.
_NORWEGIAN_FOLD = {
    "ø": "o", "Ø": "O", "æ": "ae", "Æ": "AE", "å": "a", "Å": "A",
    "ð": "d", "Ð": "D", "þ": "th", "Þ": "TH",
}


def safe_filename_component(value: str, *, max_length: int = 70) -> str:
    """ASCII-fold arbitrary text into a filename-safe component.

    Adapted from P0.7 finalize.filename_component (inspected), with the
    Norwegian letters mapped explicitly first. Folding is intended: output
    filenames stay portable while the documents themselves keep full
    Unicode.
    """
    for source, target in _NORWEGIAN_FOLD.items():
        value = value.replace(source, target)
    ascii_text = (
        unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    )
    compact = re.sub(r"[^A-Za-z0-9]+", "_", ascii_text).strip("_")
    result = (compact or "document")[:max_length].rstrip("_")
    if result.split(".", 1)[0].upper() in _RESERVED:
        result = f"x_{result}"
    return result or "document"
