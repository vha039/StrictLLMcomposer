"""Diagnostics and exit-code taxonomy.

Contract 8.1 requires every validator to identify file, location/field,
contract ID, expected and observed condition, to report all practical
independent violations in one pass, and to return nonzero on mechanical
failure.

Severity separates the two things the specification insists stay apart
(INV-07): ERROR is a mechanical boundary violation and fails the command;
WARNING is soft editorial guidance and never does. DEC-33 and DEC-24
depend on that split -- an unusual competency count or a three-page CV is
a WARNING, never a mechanical failure.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Iterator, Literal

Severity = Literal["ERROR", "WARNING"]

# Process exit codes. Mined from P0.7's convention, which was sound.
EXIT_OK = 0
EXIT_JOB_FAILURE = 1  # job-level failure or partial success; valid jobs survive
EXIT_CONFIGURATION = 2  # repository/run-integrity problem; nothing was processed


@dataclass(frozen=True)
class Violation:
    """One independently detectable mechanical finding."""

    contract_id: str  # governing spec id, e.g. "CTR-01", "DEC-34", "INV-09"
    file: str  # path or artifact label the finding belongs to
    location: str  # field path, JSON pointer, line, or "-"
    expected: str
    observed: str
    severity: Severity = "ERROR"

    def render(self) -> str:
        mark = "ERROR  " if self.severity == "ERROR" else "WARNING"
        return (
            f"[{mark}] {self.contract_id} {self.file}:{self.location}\n"
            f"          expected: {self.expected}\n"
            f"          observed: {self.observed}"
        )


@dataclass
class ValidationResult:
    """Accumulates every violation found in one pass."""

    violations: list[Violation] = field(default_factory=list)

    def add(
        self,
        contract_id: str,
        file: str,
        location: str,
        expected: str,
        observed: str,
        severity: Severity = "ERROR",
    ) -> None:
        self.violations.append(
            Violation(contract_id, file, location, expected, observed, severity)
        )

    def extend(self, others: Iterable[Violation]) -> None:
        self.violations.extend(others)

    @property
    def errors(self) -> list[Violation]:
        return [v for v in self.violations if v.severity == "ERROR"]

    @property
    def warnings(self) -> list[Violation]:
        return [v for v in self.violations if v.severity == "WARNING"]

    @property
    def ok(self) -> bool:
        """True when no ERROR was found. Warnings never fail a command."""
        return not self.errors

    def __iter__(self) -> Iterator[Violation]:
        return iter(self.violations)

    def __len__(self) -> int:
        return len(self.violations)

    def render(self) -> str:
        return "\n".join(v.render() for v in self.violations)


class JobbsokError(RuntimeError):
    """Base for every deliberate runtime failure."""

    exit_code = EXIT_CONFIGURATION


class ConfigurationError(JobbsokError):
    """Repository, asset or argument problem. Nothing was processed."""

    exit_code = EXIT_CONFIGURATION


class RunIntegrityError(JobbsokError):
    """A manifest-frozen input no longer matches its recorded hash.

    Spec 7.3: this is never ordinary staleness. Tooling must fail loudly and
    require restoration of the frozen bytes or creation of a child run; it
    must not normalize the mutation or update the manifest.
    """

    exit_code = EXIT_CONFIGURATION


class PathSafetyError(ConfigurationError):
    """Traversal, symlink/reparse escape, or a write outside an allowed root."""


class JobError(JobbsokError):
    """A job-local failure. Other jobs continue (INV-05, Spec 15.4)."""

    exit_code = EXIT_JOB_FAILURE
