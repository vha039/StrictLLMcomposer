"""Immutable run authority: freeze, verify and child branch.

DEC-40. Each frozen run has one canonical manifest and one immutable
run_id. After freeze nothing mutates in place: no same-run amend, no
manifest-version lineage engine, no history replay. Changing any frozen
element creates a new run with a new run_id and a parent_run_id, and the
original stays untouched.

Where a run reads its inputs from
------------------------------------
Freeze copies every hashed input into `runs/<run_id>/frozen/<repo path>`,
and every command for that run reads and verifies those copies rather than
the live repository files. This is what makes a run genuinely immutable
and self-contained:

* ordinary human source maintenance between runs (Spec 4.1) does not
  red-light runs that are already in flight;
* tampering with a run's own frozen bytes fails loudly and asks for
  restoration of the frozen bytes or a child run, which is exactly the
  remedy Spec 7.3 names;
* the parent's bytes remain readable for audit after branching.

`frozen_inputs[].path` records the repository-relative path at freeze time
for provenance and for locating the frozen copy; the live repository copy
is the maintenance surface that the NEXT freeze reads.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import SCHEMA_REVISION, SPEC_REVISION
from .atomicio import atomic_write_bytes, atomic_write_json, read_json
from .baseline import (
    build_baseline_map,
    check_baseline_map,
    read_baseline,
    recorded_authority_hashes,
)
from .batchinput import read_batch_input
from .errors import (
    ConfigurationError,
    RunIntegrityError,
    ValidationResult,
)
from .evidence_index import SOURCE_FILES, build_index, check_index
from .hashing import pretty_json_bytes, sha256_bytes, sha256_canonical_json, sha256_file
from .paths import Layout, resolve_within
from .schemas import schema_files, validate_against_schema
from . import settings as settings_module
from . import vacancy as vacancy_module

MANIFEST_NAME = "manifest.json"
FROZEN_DIR = "frozen"

#: The single legacy revision this runtime still interprets. Exactly two
#: fixed interpretations exist: legacy 0.9.0 (Stage 1 -> 2 -> 3, draft
#: bindings, full writing-policy hash), 0.9.3 (Stage 1 -> 3 with source
#: escape), and x2b (Stage 1 -> 3 with a closed evidence packet).
#: A run is always read through its own manifest revision, never through
#: the imported SPEC_REVISION constant. This is not a version framework:
#: The manifest revision keeps each frozen run on its own interpretation.
LEGACY_SPEC_REVISION = "0.9.0"

#: P0.9.3 amendment: Stage 1 consumes doctrine and persuasion; voice is
#: Stage-3-only. Stored order is preserved.
STAGE1_POLICY_FILENAMES = ("WRITING_DOCTRINE.md", "PERSUASION_CALIBRATION.md")


def is_legacy_run(manifest: dict[str, Any]) -> bool:
    """True when this run must be read with the frozen 0.9.0 interpretation."""
    return str(manifest.get("spec_revision")) == LEGACY_SPEC_REVISION


def writing_policy_records(
    manifest: dict[str, Any], stage: int
) -> list[dict[str, Any]]:
    """The writing-policy records one stage actually consumes.

    Legacy runs keep the original full ordered list for every stage, so
    their recorded handoff fingerprints stay reproducible. New runs give
    Stage 1 doctrine and persuasion only, and Stage 3 all three.
    """
    records = list(manifest["frozen_inputs"]["writing_policy"])
    if is_legacy_run(manifest) or stage != 1:
        return records
    return [
        record
        for record in records
        if Path(record["path"]).name in STAGE1_POLICY_FILENAMES
    ]


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------

def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _iso(moment: datetime) -> str:
    return moment.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def make_run_id(moment: datetime, seed: str) -> str:
    """Deterministic for a given timestamp and input fingerprint."""
    stamp = moment.astimezone(timezone.utc).strftime("%Y%m%d-%H%M%S")
    return f"r{stamp}-{sha256_bytes(seed.encode('utf-8'))[:6]}"


def _frozen_file(layout: Layout, path: Path) -> dict[str, Any]:
    path = Path(path)
    if not path.is_file():
        raise ConfigurationError(f"Cannot freeze a missing input: {path}")
    return {
        "path": path.resolve().relative_to(layout.root.resolve()).as_posix(),
        "sha256": sha256_file(path),
        "bytes": path.stat().st_size,
    }


def frozen_path(layout: Layout, run_id: str, record: dict[str, Any]) -> Path:
    """Where the run keeps its own copy of a frozen input."""
    return layout.run_dir(run_id) / FROZEN_DIR / record["path"]


@dataclass(frozen=True)
class FrozenRunAssets:
    """Single resolver for every maintained input consumed by a frozen run."""

    layout: Layout
    manifest: dict[str, Any]
    base_dir: Path | None = None

    @property
    def run_id(self) -> str:
        return self.manifest["run_id"]

    @property
    def run_dir(self) -> Path:
        return self.base_dir or self.layout.run_dir(self.run_id)

    def record(self, *keys: str) -> dict[str, Any]:
        value: Any = self.manifest["frozen_inputs"]
        for key in keys:
            value = value[key]
        if not isinstance(value, dict) or "path" not in value or "sha256" not in value:
            raise ConfigurationError(
                f"Frozen input {'/'.join(keys)} is not a file record."
            )
        return value

    def path(self, *keys: str) -> Path:
        return self.run_dir / FROZEN_DIR / self.record(*keys)["path"]

    def json(self, *keys: str) -> dict[str, Any]:
        return read_json(self.path(*keys))

    @property
    def schemas_dir(self) -> Path:
        return self.run_dir / FROZEN_DIR / "schemas"

    @property
    def settings(self) -> dict[str, Any]:
        return settings_module.load_path(self.path("settings"))

    def template_path(self, repository_path: str) -> Path:
        normalized = Path(repository_path).as_posix()
        for record in self.manifest["frozen_inputs"]["templates"].values():
            if record["path"] == normalized:
                return self.run_dir / FROZEN_DIR / record["path"]
        raise ConfigurationError(
            f"Template map references {repository_path!r}, which is not one of "
            "this run's frozen templates."
        )

    def stage_policy_sha256(self, stage: int) -> str:
        records = [self.record("stage_instructions", f"stage{stage}")]
        records.extend(writing_policy_records(self.manifest, stage))
        if stage == 1:
            records.extend((
                self.record("personality_profile"),
                self.record("personality_facet_index"),
            ))
        role = self.settings["stages"][f"stage{stage}"]
        return sha256_canonical_json({
            "files": [
                {"path": record["path"], "sha256": record["sha256"]}
                for record in records
            ],
            "capability_role": role,
            "configured_model": self.settings["stages"].get(
                "role_mapping", {}
            ).get(role) or None,
        })


# --------------------------------------------------------------------------
# Freeze
# --------------------------------------------------------------------------

@dataclass
class FreezeResult:
    run_id: str | None
    manifest: dict[str, Any] | None
    result: ValidationResult = field(default_factory=ValidationResult)

    @property
    def ok(self) -> bool:
        return self.result.ok and self.run_id is not None


def collect_frozen_inputs(layout: Layout) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    """Gather every input the run binds to, plus the two generated maps.

    Returns (frozen_inputs, evidence_index, baseline_map). The index and
    baseline map are generated here so freeze binds to bytes it produced
    rather than to whatever happened to be lying in generated/.
    """
    baseline_path = layout.authorities / "CV_BASELINE.md"
    index = build_index(layout.authorities)
    baseline_map = build_baseline_map(read_baseline(baseline_path), baseline_path)

    index_path = layout.generated / "evidence_index.json"
    baseline_map_path = layout.generated / "baseline_map.json"
    atomic_write_bytes(index_path, pretty_json_bytes(index))
    atomic_write_bytes(baseline_map_path, pretty_json_bytes(baseline_map))

    stage_dir = layout.policy / "stages"
    writing_dir = layout.policy / "writing"

    frozen_inputs = {
        "authorities": {
            source_id: _frozen_file(layout, layout.authorities / filename)
            for source_id, filename in SOURCE_FILES.items()
        },
        "cv_baseline": _frozen_file(layout, baseline_path),
        "personality_profile": _frozen_file(
            layout, layout.context / "PERSONALITY_PROFILE.md"
        ),
        "personality_facet_index": _frozen_file(
            layout, layout.policy / "personality_facets.json"
        ),
        "settings": _frozen_file(layout, layout.policy / "settings.toml"),
        "stage_instructions": {
            f"stage{n}": _frozen_file(layout, stage_dir / name)
            for n, name in (
                (1, "stage1_decision_architecture.md"),
                (3, "stage3_final_writer_review.md"),
            )
        },
        "writing_policy": [
            _frozen_file(layout, path) for path in sorted(writing_dir.glob("*.md"))
        ],
        "schemas": [_frozen_file(layout, path) for path in schema_files(layout.schemas)],
        "templates": {
            "cv_master": _frozen_file(layout, layout.templates / "CV_MASTER.docx"),
            "letter_master": _frozen_file(
                layout, layout.templates / "APPLICATION_MASTER.docx"
            ),
        },
        "template_map": _frozen_file(layout, layout.templates / "template_map.json"),
        "evidence_index": _frozen_file(layout, index_path),
        "baseline_map": _frozen_file(layout, baseline_map_path),
    }
    return frozen_inputs, index, baseline_map


def _reconciliation(
    layout: Layout, reviewed_by: str, moment: datetime
) -> tuple[dict[str, Any], list[str]]:
    """Contract 6.1: recorded human-reviewed baseline-to-authorities check.

    Freeze fails on a known conflict. The baseline file states the
    authority hashes it was derived from; if the live authorities no longer
    match, the rendered static identity/chronology/education facts may
    disagree with the sources and a human must resolve that between runs.
    """
    baseline_path = layout.authorities / "CV_BASELINE.md"
    recorded = recorded_authority_hashes(baseline_path)
    conflicts: list[str] = []
    hashes: dict[str, str] = {}

    for source_id, filename in SOURCE_FILES.items():
        actual = sha256_file(layout.authorities / filename)
        hashes[source_id] = actual
        stated = recorded.get(filename)
        if stated is None:
            conflicts.append(
                f"{filename}: CV_BASELINE.md records no derivation hash, so the "
                "baseline-to-authorities reconciliation cannot be confirmed."
            )
        elif stated != actual:
            conflicts.append(
                f"{filename}: CV_BASELINE.md was derived from {stated[:12]}... "
                f"but the authority is now {actual[:12]}.... Re-review the "
                "baseline against the authority and update the recorded hash "
                "before freezing."
            )

    record = {
        "reviewed_by": reviewed_by,
        "reviewed_at": moment.astimezone(timezone.utc).strftime("%Y-%m-%d"),
        "authority_hashes_at_review": hashes,
        "conflicts_known": conflicts,
    }
    return record, conflicts


def freeze(
    layout: Layout,
    input_path: Path,
    *,
    reviewed_by: str,
    moment: datetime | None = None,
) -> FreezeResult:
    """Validate operator input and create one immutable run.

    Fails atomically: the run is built under a temporary directory and
    renamed into place only after everything succeeds, so no partial frozen
    run can masquerade as valid (Contract 6.1).
    """
    moment = moment or utc_now()
    result = ValidationResult()

    rows, input_result = read_batch_input(Path(input_path))
    result.extend(input_result.violations)

    try:
        settings = settings_module.load(layout)
    except ConfigurationError as exc:
        result.add("CTR-01", "policy/settings.toml", "-", "readable settings", str(exc))
        return FreezeResult(None, None, result)

    frozen_inputs, index, baseline_map = collect_frozen_inputs(layout)
    result.extend(check_index(index, layout.authorities).violations)
    result.extend(check_baseline_map(baseline_map).violations)

    reconciliation, conflicts = _reconciliation(layout, reviewed_by, moment)
    for conflict in conflicts:
        result.add(
            "CTR-01", "authorities/CV_BASELINE.md", "baseline_reconciliation",
            "no known baseline-versus-authority conflict in rendered static "
            "identity, chronology or education facts",
            conflict,
        )

    # Resolve and inspect every vacancy source before creating anything.
    prepared: list[tuple[Any, Path, dict[str, Any], vacancy_module.Extraction]] = []
    for row in rows:
        if not row.source:
            continue
        try:
            source_path = resolve_within(
                layout.inbox, row.source, label=f"job {row.job_id} source"
            )
        except Exception as exc:
            result.add("CTR-01", "batch input", f"{row.job_id}.source",
                       "a vacancy file inside inbox/", str(exc))
            continue
        if not source_path.is_file():
            result.add("CTR-01", "batch input", f"{row.job_id}.source",
                       "an existing vacancy file", f"not found: {source_path}")
            continue
        media_type = vacancy_module.media_type_for(source_path)
        if media_type is None:
            result.add("ACC-19", "batch input", f"{row.job_id}.source",
                       f"one of {sorted(vacancy_module.MEDIA_TYPES)}",
                       f"unsupported type {source_path.suffix!r}")
            continue
        size = source_path.stat().st_size
        if size == 0 or size > vacancy_module.MAX_SOURCE_BYTES:
            result.add("ACC-19", "batch input", f"{row.job_id}.source",
                       f"1..{vacancy_module.MAX_SOURCE_BYTES} bytes",
                       f"{size} bytes")
            continue

        extraction = vacancy_module.extract(source_path)
        source_record = {
            "relpath": f"jobs/{row.job_id}/source/{source_path.name}",
            "sha256": sha256_file(source_path),
            "bytes": size,
            "media_type": media_type,
        }
        prepared.append((row, source_path, source_record, extraction))

    if not result.ok:
        return FreezeResult(None, None, result)

    jobs = [
        row.to_manifest_entry(record, ext.requires_source_inspection, ext.reasons)
        for row, _, record, ext in prepared
    ]

    seed = "|".join(
        [_iso(moment)]
        + sorted(job["job_id"] for job in jobs)
        + [frozen_inputs["authorities"][s]["sha256"] for s in sorted(SOURCE_FILES)]
    )
    run_id = make_run_id(moment, seed)

    manifest: dict[str, Any] = {
        "artifact_role": "RUN_MANIFEST",
        "run_id": run_id,
        "parent_run_id": None,
        "spec_revision": SPEC_REVISION,
        "schema_revision": SCHEMA_REVISION,
        "frozen_at": _iso(moment),
        "frozen_inputs": frozen_inputs,
        "settings_snapshot": settings_module.snapshot(settings),
        "baseline_reconciliation": reconciliation,
        "jobs": jobs,
    }

    validate_against_schema(
        manifest, layout.schemas, "manifest", file_label=MANIFEST_NAME, result=result
    )
    if not result.ok:
        return FreezeResult(None, None, result)

    _materialize_run(layout, run_id, manifest, prepared)
    return FreezeResult(run_id, manifest, result)


def _materialize_run(
    layout: Layout,
    run_id: str,
    manifest: dict[str, Any],
    prepared: list[tuple[Any, Path, dict[str, Any], Any]],
) -> None:
    """Build the run under a temp name, then rename it into place."""
    final = layout.run_dir(run_id)
    if final.exists():
        raise ConfigurationError(f"Run {run_id} already exists at {final}.")
    staging = layout.runs / f".freezing-{run_id}"
    if staging.exists():
        shutil.rmtree(staging)

    try:
        staging.mkdir(parents=True)
        (staging / "audit").mkdir()

        for record in _iter_frozen_records(manifest["frozen_inputs"]):
            source = layout.root / record["path"]
            target = staging / FROZEN_DIR / record["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

        for row, source_path, source_record, extraction in prepared:
            job_dir = staging / "jobs" / row.job_id
            for sub in ("source", "derived", "current", "out", "history"):
                (job_dir / sub).mkdir(parents=True, exist_ok=True)
            # Byte-for-byte preservation of the employer-fact authority.
            shutil.copy2(source_path, job_dir / "source" / source_path.name)
            if extraction.normalized_markdown:
                atomic_write_bytes(
                    job_dir / "derived" / "vacancy_normalized.md",
                    extraction.normalized_markdown.encode("utf-8"),
                )

        atomic_write_json(staging / MANIFEST_NAME, manifest)
        staged = _verify_frozen_assets(
            FrozenRunAssets(layout, manifest, base_dir=staging)
        )
        if not staged.ok:
            raise RunIntegrityError(
                f"Run {run_id} failed its staged frozen-input check:\n"
                + staged.render()
            )
        staging.rename(final)
    except Exception:
        if staging.exists():
            shutil.rmtree(staging, ignore_errors=True)
        raise


def _iter_frozen_records(node: Any):
    """Yield every {path, sha256, bytes} record in frozen_inputs."""
    if isinstance(node, dict):
        if {"path", "sha256", "bytes"} <= set(node):
            yield node
            return
        for value in node.values():
            yield from _iter_frozen_records(value)
    elif isinstance(node, list):
        for item in node:
            yield from _iter_frozen_records(item)


# --------------------------------------------------------------------------
# Load and verify
# --------------------------------------------------------------------------

def known_runs(layout: Layout) -> list[str]:
    """Flat runs and their published children. A diagnostic only.

    It never defines expected jobs or goal scope; those still come from
    each run's own manifest (DEC-08).
    """
    found: list[str] = []
    for root in sorted(layout.runs.glob("r*")):
        if (root / MANIFEST_NAME).is_file():
            found.append(root.name)
        for child in sorted((root / "branches").glob("*")):
            if (child / MANIFEST_NAME).is_file():
                found.append(f"{root.name}/branches/{child.name}")
    return found


def manifest_path(layout: Layout, run_id: str) -> Path:
    return layout.run_dir(run_id) / MANIFEST_NAME


def load_manifest(layout: Layout, run_id: str) -> dict[str, Any]:
    path = manifest_path(layout, run_id)
    if not path.is_file():
        raise ConfigurationError(
            f"No run {run_id!r} at {path.parent}. Known runs: "
            f"{', '.join(known_runs(layout)) or '(none)'}"
        )
    return read_json(path)


def manifest_sha256(layout: Layout, run_id: str) -> str:
    return sha256_file(manifest_path(layout, run_id))


def _verify_frozen_assets(assets: FrozenRunAssets) -> ValidationResult:
    """Every-command integrity check (Contract 6.2, 7).

    A mismatch is a run-integrity error, never ordinary staleness. The
    remedy is restoration of the frozen bytes or a child run; the manifest
    is never updated to match reality.
    """
    result = ValidationResult()
    manifest = assets.manifest
    run_id = assets.run_id

    for record in _iter_frozen_records(manifest["frozen_inputs"]):
        target = assets.run_dir / FROZEN_DIR / record["path"]
        if not target.is_file():
            result.add(
                "DEC-40", f"runs/{run_id}/{FROZEN_DIR}/{record['path']}", "-",
                f"frozen input present with sha256 {record['sha256'][:12]}...",
                "missing. Restore the frozen bytes or create a child run "
                "(jobbsok branch); the manifest is never updated in place.",
            )
            continue
        actual = sha256_file(target)
        if actual != record["sha256"]:
            result.add(
                "DEC-40", f"runs/{run_id}/{FROZEN_DIR}/{record['path']}", "-",
                f"sha256 {record['sha256']}",
                f"sha256 {actual}. A manifest-frozen input changed: this is a "
                "run-integrity failure, not staleness. Restore the frozen "
                "bytes or create a child run (jobbsok branch).",
            )

    for job in manifest["jobs"]:
        source = assets.run_dir / job["source"]["relpath"]
        if not source.is_file():
            result.add(
                "INV-03", job["source"]["relpath"], job["job_id"],
                "preserved original vacancy present", "missing",
            )
            continue
        actual = sha256_file(source)
        if actual != job["source"]["sha256"]:
            result.add(
                "INV-03", job["source"]["relpath"], job["job_id"],
                f"sha256 {job['source']['sha256']}",
                f"sha256 {actual}. The preserved original vacancy changed.",
            )
    return result


def verify_frozen(layout: Layout, manifest: dict[str, Any]) -> ValidationResult:
    return _verify_frozen_assets(FrozenRunAssets(layout, manifest))


def require_intact(layout: Layout, manifest: dict[str, Any]) -> None:
    """Raise RunIntegrityError unless every frozen hash still matches."""
    result = verify_frozen(layout, manifest)
    if not result.ok:
        raise RunIntegrityError(
            f"Run {manifest['run_id']} failed its frozen-input check:\n"
            + result.render()
        )


def read_frozen(layout: Layout, manifest: dict[str, Any], *keys: str) -> Any:
    """Read a frozen input record by its frozen_inputs key path."""
    node: Any = manifest["frozen_inputs"]
    for key in keys:
        node = node[key]
    return node


def load_frozen_json(layout: Layout, manifest: dict[str, Any], *keys: str) -> Any:
    record = read_frozen(layout, manifest, *keys)
    return read_json(frozen_path(layout, manifest["run_id"], record))


def core_jobs(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    return [j for j in manifest["jobs"] if j["job_class"] == "CORE"]


def exception_jobs(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    return [j for j in manifest["jobs"] if j["job_class"] == "EXCEPTION"]


def find_job(manifest: dict[str, Any], job_id: str) -> dict[str, Any]:
    for job in manifest["jobs"]:
        if job["job_id"] == job_id:
            return job
    known = ", ".join(j["job_id"] for j in manifest["jobs"])
    raise ConfigurationError(
        f"Job {job_id!r} is not in the manifest for run {manifest['run_id']}. "
        f"Expected one of: {known}"
    )
