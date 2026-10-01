"""Operator command surface.

Contract 2 lists fifteen required runtime capabilities; the exact number
and spelling of commands is implementation freedom. These are task-oriented
rather than stage-shaped, because the P0.7 stage conveyor is retired.

Every command:

* forces UTF-8 output (GATE-07: this console defaults to cp1252 and would
  otherwise crash while printing a Norwegian diagnostic);
* verifies the manifest and relevant frozen hashes before acting
  (Contract 6.2);
* returns 0 on success, 1 on job-level failure or partial success, and 2 on
  a configuration or run-integrity problem;
* makes no network request and no model call.
"""

from __future__ import annotations

import argparse
import errno
import json
import shutil
import sys
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from . import X2B_REVISION
from . import artifacts as artifacts_module
from . import evidence_index as index_module
from . import manifest as manifest_module
from . import branch as branch_module
from . import failure as failure_module
from . import ioenc
from . import render as render_module
from . import preview as preview_module
from . import retrieval
from . import settings as settings_module
from . import status as status_module
from . import validate as validate_module
from . import vacancy as vacancy_module
from .atomicio import (
    TransactionDir,
    atomic_write_bytes,
    atomic_write_json,
    atomic_write_text,
    read_json,
)
from .baseline import (
    build_baseline_map,
    check_baseline_map,
    project_baseline_map,
    read_baseline,
)
from .batchinput import write_template
from .docxfill import binding_report, control_inventory
from .errors import (
    EXIT_CONFIGURATION,
    EXIT_JOB_FAILURE,
    EXIT_OK,
    ConfigurationError,
    JobError,
    JobbsokError,
    RunIntegrityError,
    ValidationResult,
)
from .evidence_index import build_index, check_index
from .hashing import pretty_json_bytes, sha256_file
from .manifest import (
    find_job,
    freeze,
    frozen_path,
    load_manifest,
    manifest_path,
    read_frozen,
    require_intact,
)
from .paths import Layout, flatten_run_reference, resolve_output_destination


def _emit(result: ValidationResult, *, header: str = "") -> None:
    if not len(result):
        return
    if header:
        print(header)
    print(result.render())
    errors, warnings = len(result.errors), len(result.warnings)
    print(f"\n{errors} error(s), {warnings} warning(s).")


def _emit_recovery(record: dict[str, Any]) -> None:
    print("Recovery:")
    print(f"  classification         : {record['classification']}")
    print(
        "  mechanical corrections : "
        f"{record['mechanical_corrections_used']}"
    )
    print(f"  semantic attempts      : {record['attempts_used']}")
    print(f"  next action            : {record['recommended_next_action']}")


def _layout(args: argparse.Namespace) -> Layout:
    return Layout.discover(Path(args.root) if args.root else None)


def _context(layout: Layout, run_id: str) -> tuple[dict[str, Any], validate_module.RunContext]:
    manifest = load_manifest(layout, run_id)
    require_intact(layout, manifest)
    return manifest, validate_module.RunContext(layout, manifest)


def _thresholds(context: validate_module.RunContext) -> dict[str, int]:
    try:
        return settings_module.soft_warnings(context.assets.settings)
    except ConfigurationError:
        return {}


def _record_stage_failure(
    layout: Layout,
    context: validate_module.RunContext,
    job_id: str,
    stage: int,
    result: ValidationResult,
    envelope: dict[str, Any],
) -> dict[str, Any]:
    existing = failure_module.load(layout, context.run_id, job_id)
    correction_limit = context.assets.settings["recovery"][
        "mechanical_correction_attempts"
    ]
    same_attempt = (
        existing is not None
        and existing.get("operation") == f"STAGE{stage}"
        and existing.get("classification") == "FAILED"
        and existing.get("semantic_attempt") == envelope.get("semantic_retry_attempt")
    )
    corrections = (
        existing.get("mechanical_corrections_used", 0) + 1
        if same_attempt else 0
    )
    attempts_used = envelope.get("semantic_retry_attempt") or 0
    retry_stages = context.assets.settings["recovery"]["retry_start_stages"]

    classification = "FAILED"
    retry_position = (
        existing.get("retry_position")
        if same_attempt and existing
        else (attempts_used - 1 if envelope.get("semantic_retry_attempt") else None)
    )
    if corrections < correction_limit:
        action = (
            "Correct the reported mechanical defects once in the same session "
            "and resubmit with the same handoff."
        )
    else:
        next_stage = failure_module.next_retry_stage(retry_stages, attempts_used)
        if next_stage == 3 and stage == 3:
            retry_position = attempts_used
            action = (
                f"Manually request fresh Stage {next_stage} context; this is the "
                "configured semantic retry and starts no model automatically."
            )
        else:
            classification = "BLOCKED_MANUAL"
            action = (
                "The bounded mechanical correction and applicable configured "
                "semantic retry are unavailable or exhausted. This run remains blocked. "
                "The human may stop the job or request branch --from-stage 1 or 3 "
                "from an intact parent; continue only in the resulting child."
            )
    state = artifacts_module.semantic_state(layout, context, job_id)
    highest = None
    ladder = (
        (("strategy", "STRATEGY"), ("draft_package", "DRAFT"),
         ("final_package", "FINAL"))
        if manifest_module.is_legacy_run(context.manifest)
        else (("strategy", "STRATEGY"), ("final_package", "FINAL"))
    )
    for name, label in ladder:
        if state.current(name):
            highest = label
        else:
            break
    return failure_module.record(
        layout, context.run_id, job_id,
        operation=f"STAGE{stage}", classification=classification, result=result,
        diagnostic_summary="Semantic stage return failed mechanical validation.",
        recommended_next_action=action,
        attempts_used=attempts_used, retry_position=retry_position,
        last_successful_stage=highest,
        mechanical_corrections_used=corrections,
        semantic_attempt=envelope.get("semantic_retry_attempt"),
    )


# --------------------------------------------------------------------------
# Commands
# --------------------------------------------------------------------------

def cmd_preflight(args: argparse.Namespace) -> int:
    layout = _layout(args)
    settings = settings_module.load(layout)
    template_map = read_json(layout.templates / "template_map.json")

    print(f"Build root       : {layout.root}")
    print(f"Python           : {sys.version.split()[0]}")
    print(f"stdout encoding  : {sys.stdout.encoding}")
    print(f"Converter        : {settings['render']['converter']} "
          f"({settings['render']['invocation_granularity']})")
    print()

    baseline_path = layout.authorities / "CV_BASELINE.md"
    baseline_map = build_baseline_map(read_baseline(baseline_path), baseline_path)
    index = build_index(layout.authorities)

    result = ValidationResult()
    result.extend(check_baseline_map(baseline_map).violations)
    result.extend(check_index(index, layout.authorities).violations)
    result.extend(
        render_module.preflight_templates(
            layout, template_map,
            effective={
                "candidate": baseline_map["candidate"],
                "employments": [
                    {**e, "bullets": e["default_bullets"]}
                    for e in baseline_map["employments"]
                ],
                "educations": baseline_map["educations"],
            },
        ).violations
    )

    for name, spec in template_map["documents"].items():
        master = layout.root / spec["master"]
        inventory = control_inventory(master)
        print(f"{name:8s} {Path(spec['master']).name:26s} "
              f"controls={sum(inventory.values()):2d}  bindings={binding_report(master)}")
    print(f"evidence index   : {len(index['entries'])} entries over "
          f"{len(index['sources'])} authorities")
    print(f"baseline map     : {len(baseline_map['employments'])} employments, "
          f"{len(baseline_map['educations'])} educations")
    print()
    _emit(result, header="Preflight findings:")
    if result.ok:
        print("Preflight PASS.")
    return EXIT_OK if result.ok else EXIT_CONFIGURATION


def cmd_index(args: argparse.Namespace) -> int:
    layout = _layout(args)
    index = build_index(layout.authorities)
    baseline_path = layout.authorities / "CV_BASELINE.md"
    baseline_map = build_baseline_map(read_baseline(baseline_path), baseline_path)
    result = check_index(index, layout.authorities)
    result.extend(check_baseline_map(baseline_map).violations)

    index_path = layout.generated / "evidence_index.json"
    map_path = layout.generated / "baseline_map.json"

    if args.action == "verify":
        for path, payload, label in (
            (index_path, index, "evidence index"),
            (map_path, baseline_map, "baseline map"),
        ):
            if not path.is_file():
                result.add("DEC-14", str(path), "-", "generated file present", "missing")
            elif path.read_bytes() != pretty_json_bytes(payload):
                result.add(
                    "DEC-14", str(path), "-",
                    "byte-identical regeneration from the same inputs",
                    f"the {label} on disk differs from a fresh generation",
                )
        _emit(result)
        print("Index verify PASS." if result.ok else "Index verify FAILED.")
        return EXIT_OK if result.ok else EXIT_CONFIGURATION

    if not result.ok:
        _emit(result)
        return EXIT_CONFIGURATION
    atomic_write_text(index_path, pretty_json_bytes(index).decode("utf-8"))
    atomic_write_text(map_path, pretty_json_bytes(baseline_map).decode("utf-8"))
    print(f"evidence_index.json : {len(index['entries'])} entries")
    print(f"baseline_map.json   : {len(baseline_map['employments'])} employments")
    return EXIT_OK


def _resolve_input(layout: Layout, value: str) -> Path:
    """Accept a path relative to the build root as well as to the cwd."""
    given = Path(value)
    if given.is_file():
        return given
    candidate = layout.root / given
    if candidate.is_file():
        return candidate
    raise ConfigurationError(
        f"No such file: {value!r}. Looked in the current directory and in "
        f"{layout.root}."
    )


def cmd_freeze(args: argparse.Namespace) -> int:
    layout = _layout(args)
    result = freeze(
        layout, _resolve_input(layout, args.input), reviewed_by=args.reviewed_by,
        moment=_moment(args),
    )
    if not result.ok:
        _emit(result.result, header="Freeze refused:")
        print("\nNo partial run was created; freeze fails atomically.")
        return EXIT_CONFIGURATION
    manifest = result.manifest
    print(f"Frozen run: {result.run_id}")
    print(f"  jobs      : {len(manifest['jobs'])} "
          f"(core {sum(1 for j in manifest['jobs'] if j['job_class'] == 'CORE')}, "
          f"exception {sum(1 for j in manifest['jobs'] if j['job_class'] == 'EXCEPTION')})")
    print(f"  manifest  : {manifest_path(layout, result.run_id)}")
    inspect = [j["job_id"] for j in manifest["jobs"] if j["requires_source_inspection"]]
    if inspect:
        print(f"  requires source inspection: {inspect}")
    _emit(result.result)
    return EXIT_OK


def cmd_branch(args: argparse.Namespace) -> int:
    layout = _layout(args)
    result = branch_module.branch(
        layout, args.run, reviewed_by=args.reviewed_by,
        from_stage=args.from_stage, model_tag=args.model_tag,
        moment=_moment(args),
    )
    if not result.ok:
        _emit(result.result, header="Branch refused:")
        return EXIT_CONFIGURATION
    print(f"Child run : {result.run_id}")
    print(f"Parent    : {args.run} (untouched)")
    for job_id, states in result.disposition.items():
        rendered = ", ".join(f"{k}={v}" for k, v in states.items())
        print(f"  {job_id}: {rendered}")
    _emit(result.result)
    return EXIT_OK


def cmd_verify_integrity(args: argparse.Namespace) -> int:
    layout = _layout(args)
    manifest = load_manifest(layout, args.run)
    from .manifest import verify_frozen

    result = verify_frozen(layout, manifest)
    _emit(result)
    if result.ok:
        print(f"Run {args.run}: all frozen inputs intact.")
        return EXIT_OK
    print(f"\nRun {args.run} FAILED its frozen-input check.")
    return EXIT_CONFIGURATION


def cmd_validate(args: argparse.Namespace) -> int:
    layout = _layout(args)
    manifest, context = _context(layout, args.run)
    thresholds = _thresholds(context)
    wanted = list(
        artifacts_module.active_artifacts(manifest.get("spec_revision"))
    )
    if args.artifact and args.artifact != "all":
        wanted = [artifacts_module.canonical_name(args.artifact)]
    jobs = [find_job(manifest, args.job)] if args.job else manifest["jobs"]

    failures = 0
    checked = 0
    for job in jobs:
        if job["job_class"] == "EXCEPTION":
            continue
        for name in wanted:
            try:
                payload = artifacts_module.load(
                    layout, manifest["run_id"], job["job_id"], name
                )
            except ConfigurationError as exc:
                failures += 1
                print(f"[FAIL] {job['job_id']}/{artifacts_module.ARTIFACTS[name][0]}")
                print(
                    "[ERROR  ] CTR-05 "
                    f"{artifacts_module.ARTIFACTS[name][0]}:-\n"
                    "          expected: parseable job-local JSON\n"
                    f"          observed: {exc}"
                )
                continue
            if payload is None:
                continue
            checked += 1
            result = validate_module.validate_artifact(
                layout, context, job["job_id"], name, payload,
                soft_thresholds=thresholds,
            )
            label = f"{job['job_id']}/{artifacts_module.ARTIFACTS[name][0]}"
            if result.ok:
                warnings = len(result.warnings)
                print(f"[PASS] {label}" + (f"  ({warnings} warning(s))" if warnings else ""))
                if warnings:
                    print(result.render())
            else:
                failures += 1
                print(f"[FAIL] {label}")
                print(result.render())
        try:
            _, stale_result = artifacts_module.evaluate_staleness(
                layout, manifest["run_id"], job["job_id"],
                spec_revision=manifest["spec_revision"],
            )
            if len(stale_result):
                print(stale_result.render())
        except ConfigurationError:
            pass  # the malformed artifact was already reported above

    print(f"\nChecked {checked} artifact(s); {failures} failed.")
    return EXIT_JOB_FAILURE if failures else EXIT_OK


def cmd_stage_submit(args: argparse.Namespace) -> int:
    layout = _layout(args)
    manifest, context = _context(layout, args.run)
    job = find_job(manifest, args.job)
    thresholds = _thresholds(context)
    envelope = artifacts_module.verify_handoff(
        layout, context, job["job_id"], args.stage, Path(args.handoff),
        soft_thresholds=thresholds,
    )
    expected = envelope["expected_artifacts"]
    if args.artifact:
        supplied_role = artifacts_module.canonical_name(args.artifact)
        if len(expected) != 1 or supplied_role != expected[0]:
            raise ConfigurationError(
                f"--artifact {supplied_role!r} does not match handoff mode "
                f"{envelope['mode']} ({expected})."
            )

    state = artifacts_module.semantic_state(
        layout, context, job["job_id"], soft_thresholds=thresholds
    )
    semantic = read_json(_resolve_input(layout, args.file))
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    if envelope["mode"] == "FINAL_AND_REVIEW":
        if not args.review_file:
            raise ConfigurationError(
                "Stage-3 FINAL_AND_REVIEW requires --review-file. Use the exact "
                "submission action printed by jobbsok context."
            )
        final_payload = artifacts_module.stamp_payload(
            context, job["job_id"], "final_package", semantic, state
        )
        review_semantic = read_json(_resolve_input(layout, args.review_file))
        review_state = artifacts_module.SemanticState(
            {**state.loaded, "final_package": final_payload},
            state.valid | {"final_package"},
            state.stale - {"final_package"},
            state.invalid - {"final_package"},
        )
        review_payload = artifacts_module.stamp_payload(
            context, job["job_id"], "review", review_semantic, review_state
        )
        final_result = validate_module.validate_artifact(
            layout, context, job["job_id"], "final_package", final_payload,
            soft_thresholds=thresholds,
        )
        review_result = validate_module.validate_artifact(
            layout, context, job["job_id"], "review", review_payload,
            soft_thresholds=thresholds,
        )
        combined = ValidationResult()
        combined.extend(final_result.violations)
        combined.extend(review_result.violations)
        if not combined.ok:
            failure = _record_stage_failure(
                layout, context, job["job_id"], args.stage, combined, envelope
            )
            _emit(combined, header="Refused: the Stage-3 pair is mechanically invalid.")
            _emit_recovery(failure)
            return EXIT_JOB_FAILURE
        submitted = artifacts_module.submit_stage3_pair(
            layout, manifest["run_id"], job["job_id"],
            final_payload=final_payload, review_payload=review_payload,
            timestamp=stamp,
        )
        for item in submitted:
            print(f"[OK] wrote {item.path}")
            if item.superseded:
                print(f"     previous version archived to {item.superseded.name}")
        failure_module.clear(layout, manifest["run_id"], job["job_id"])
        _emit(combined)
        return EXIT_OK

    if args.review_file:
        raise ConfigurationError(
            f"--review-file is not used by handoff mode {envelope['mode']}."
        )
    artifact = expected[0]
    payload = artifacts_module.stamp_payload(
        context, job["job_id"], artifact, semantic, state
    )
    result = validate_module.validate_artifact(
        layout, context, job["job_id"], artifact, payload,
        soft_thresholds=thresholds,
    )
    if not result.ok:
        failure = _record_stage_failure(
            layout, context, job["job_id"], args.stage, result, envelope
        )
        _emit(result, header=f"Refused: {artifact} is mechanically invalid.")
        _emit_recovery(failure)
        return EXIT_JOB_FAILURE

    if artifact == "strategy" and state.loaded.get("strategy") is not None:
        if artifacts_module.artifact_hash(payload) != state.digest("strategy"):
            scope = artifacts_module.stale_scope(
                "strategy", spec_revision=manifest["spec_revision"]
            )
            present = [
                name for name in ("final_package", "review")
                if state.current(name)
            ]
            receipt = layout.job_dir(manifest["run_id"], job["job_id"]) / "current" / "render_report.json"
            if receipt.is_file() and state.current("final_package"):
                present.append("render")
            print(f"Replacement impact (fixed stale scope): {', '.join(scope)}")
            print(f"Existing downstream artifacts becoming stale: {', '.join(present) or 'none'}")

    submitted = artifacts_module.submit(
        layout, manifest["run_id"], job["job_id"],
        stage=args.stage, artifact=artifact, payload=payload, timestamp=stamp,
    )
    print(f"[OK] wrote {submitted.path}")
    if submitted.superseded:
        print(f"     previous version archived to {submitted.superseded.name}")
    failure_module.clear(layout, manifest["run_id"], job["job_id"])
    _emit(result)
    return EXIT_OK


def cmd_finalize(args: argparse.Namespace) -> int:
    layout = _layout(args)
    manifest, context = _context(layout, args.run)
    job = find_job(manifest, args.job)
    if job["job_class"] == "EXCEPTION":
        raise JobError(
            f"{job['job_id']} is an EXCEPTION job and cannot be finalized in core."
        )
    state = artifacts_module.semantic_state(
        layout, context, job["job_id"], soft_thresholds=_thresholds(context)
    )
    if not state.current("final_package"):
        raise JobError(
            f"Job {job['job_id']} has no current valid final package to finalize."
        )
    if not state.current("review"):
        raise JobError(
            f"Job {job['job_id']} has no current valid Stage-3 review. Complete "
            "Stage 3 review-only before finalizing."
        )
    payload = state.loaded["final_package"]
    result = validate_module.validate_artifact(
        layout, context, job["job_id"], "final_package", payload,
        soft_thresholds=_thresholds(context),
    )
    if not result.ok:
        _emit(result, header="Refused: the final package is mechanically invalid.")
        return EXIT_JOB_FAILURE

    finalization = payload.setdefault("finalization", {"state": "DRAFT"})
    existing = finalization.get("document_date")
    chosen = args.date or existing or date.today().isoformat()
    try:
        parsed_date = date.fromisoformat(chosen)
    except ValueError as exc:
        raise JobError(
            f"Invalid document date {chosen!r}; expected canonical YYYY-MM-DD."
        ) from exc
    if parsed_date.isoformat() != chosen:
        raise JobError(
            f"Invalid document date {chosen!r}; expected canonical YYYY-MM-DD."
        )
    if existing and not args.date and finalization.get("state") == "FINALIZED":
        print(f"Already finalized on {existing}. A pure rerender preserves this "
              "date; pass --date to re-finalize explicitly.")
        return EXIT_OK

    finalization["state"] = "FINALIZED"
    finalization["document_date"] = chosen
    finalization["finalized_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    finalization["finalized_by"] = args.reviewed_by

    path = artifacts_module.artifact_path(
        layout, manifest["run_id"], job["job_id"], "final_package"
    )
    atomic_write_json(path, payload)
    print(f"Finalized {job['job_id']} with document date {chosen}.")
    print("A pure rerender preserves this date (DEC-38).")
    return EXIT_OK


def _snapshot_render_state(
    targets: list[Path],
    *,
    previous_report: dict[str, Any] | None,
    history: Path,
    workspace: Path,
) -> dict[str, Any]:
    expected = render_module.previous_output_hashes(previous_report)
    files: list[dict[str, Any]] = []
    for index, target in enumerate(dict.fromkeys(Path(path) for path in targets)):
        if target.exists() and not target.is_file():
            raise JobError(f"Render target is not a regular file: {target}")
        if not target.is_file():
            files.append({
                "path": target, "backup": None, "sha256": None, "owned": False,
            })
            continue
        before = sha256_file(target)
        backup = workspace / f"b{index}"
        shutil.copy2(target, backup)
        after = sha256_file(target)
        copied = sha256_file(backup)
        if before != after or copied != after:
            raise JobError(
                f"Render target changed while its rollback snapshot was created: {target}"
            )
        files.append({
            "path": target,
            "backup": backup,
            "sha256": after,
            "owned": expected.get(target.name) == after,
        })
    history_before = {
        path.name for path in history.iterdir() if path.is_file()
    } if history.is_dir() else set()
    return {"files": files, "history": history, "history_before": history_before}


def _restore_render_state(snapshot: dict[str, Any]) -> None:
    for record in snapshot["files"]:
        target = record["path"]
        expected = record["sha256"]
        backup = record["backup"]
        if expected is None:
            if target.exists():
                if not target.is_file():
                    raise ConfigurationError(
                        f"Cannot remove non-file created during failed render: {target}"
                    )
                target.unlink()
            continue
        if target.is_file() and sha256_file(target) == expected:
            continue
        if backup is None or not backup.is_file() or sha256_file(backup) != expected:
            raise ConfigurationError(f"Rollback backup is missing or invalid for {target}.")
        atomic_write_bytes(target, backup.read_bytes())

    history = snapshot["history"]
    if history.is_dir():
        for path in history.iterdir():
            if path.is_file() and path.name not in snapshot["history_before"]:
                path.unlink()

    for record in snapshot["files"]:
        target = record["path"]
        expected = record["sha256"]
        if expected is None:
            if target.exists():
                raise ConfigurationError(
                    f"Failed render created an output that rollback could not remove: {target}"
                )
        elif not target.is_file() or sha256_file(target) != expected:
            raise ConfigurationError(
                f"Failed render could not restore the prior bytes for {target}."
            )


def _exception_chain(exc: BaseException):
    seen: set[int] = set()
    current: BaseException | None = exc
    while current is not None and id(current) not in seen:
        seen.add(id(current))
        yield current
        current = current.__cause__ or current.__context__


def _locked_pipeline_destination(
    exc: BaseException, snapshot: dict[str, Any] | None,
    targets: list[Path] | None = None,
) -> bool:
    if snapshot is not None:
        owned = {
            Path(record["path"]).resolve(strict=False)
            for record in snapshot["files"]
            if record["owned"]
            and Path(record["path"]).suffix.lower() in (".docx", ".pdf")
        }
    else:
        # The lock can strike while the rollback snapshot is still being taken,
        # which leaves no snapshot to consult. The advice is about a render
        # destination being open, not about ownership, so the planned target set
        # is a safe fallback.
        owned = {
            Path(path).resolve(strict=False)
            for path in (targets or [])
            if Path(path).suffix.lower() in (".docx", ".pdf")
        }
    if not owned:
        return False
    for current in _exception_chain(exc):
        if not isinstance(current, OSError):
            continue
        if (
            current.errno not in (errno.EACCES, errno.EPERM)
            and getattr(current, "winerror", None) not in (5, 32)
        ):
            continue
        for value in (getattr(current, "filename", None), getattr(current, "filename2", None)):
            if value and Path(value).resolve(strict=False) in owned:
                return True
    return False


def _render_failure_scope(exc: BaseException) -> str:
    if isinstance(exc, (ConfigurationError, RunIntegrityError)):
        return "shared"
    if render_module.is_shared_render_failure(exc):
        return "shared"
    return "job"


def cmd_render(args: argparse.Namespace) -> int:
    layout = _layout(args)
    manifest, context = _context(layout, args.run)
    template_map = read_json(
        frozen_path(layout, manifest["run_id"], read_frozen(layout, manifest, "template_map"))
    )
    baseline_map = context.baseline_map
    render_settings = context.assets.settings["render"]
    jobs = [find_job(manifest, args.job)] if args.job else manifest["jobs"]
    if args.job and jobs[0]["job_class"] == "EXCEPTION":
        raise JobError(
            f"{jobs[0]['job_id']} is an EXCEPTION job and cannot be rendered in core."
        )
    export_destination = None
    if args.dest:
        export_destination, _ = resolve_output_destination(layout, args.dest)

    failures = 0
    for job in jobs:
        if job["job_class"] == "EXCEPTION":
            continue
        job_id = job["job_id"]
        report_path = layout.job_dir(manifest["run_id"], job_id) / "current" / "render_report.json"
        out_dir = (
            export_destination
            if export_destination is not None
            else layout.job_dir(manifest["run_id"], job_id) / "out"
        )
        output_paths = list(
            render_module.render_output_paths(template_map, job, out_dir).values()
        )
        history = layout.job_dir(manifest["run_id"], job_id) / "history"
        snapshot: dict[str, Any] | None = None
        report: dict[str, Any] | None = None

        with TransactionDir(
            Path(tempfile.gettempdir()), prefix=f"jb-rb-{job_id[:12]}"
        ) as rollback_workspace:
            try:
                # Only this job's own current artifacts are job-local. A shared
                # failure raised later by semantic_state -- an invalid frozen
                # schema, an unreadable frozen asset -- stays a ConfigurationError
                # and aborts the whole command rather than being blamed on one job.
                try:
                    for _name in artifacts_module.ARTIFACTS:
                        artifacts_module.load(layout, context.run_id, job_id, _name)
                except ConfigurationError as exc:
                    raise JobError(
                        f"malformed job-local semantic state: {exc}"
                    ) from exc
                semantic_state = artifacts_module.semantic_state(
                    layout, context, job_id, soft_thresholds=_thresholds(context)
                )
                if (
                    not semantic_state.current("final_package")
                    or not semantic_state.current("review")
                ):
                    raise JobError(
                        "render requires a current valid final package and current "
                        "valid review."
                    )
                package = semantic_state.loaded["final_package"]

                result = validate_module.validate_artifact(
                    layout, context, job_id, "final_package", package,
                    soft_thresholds=_thresholds(context),
                )
                if not result.ok:
                    raise JobError(
                        "final package is mechanically invalid:\n" + result.render()
                    )

                previous = None
                if export_destination is None and report_path.is_file():
                    try:
                        previous = read_json(report_path)
                    except ConfigurationError as exc:
                        raise JobError(
                            f"malformed job-local render receipt: {exc}"
                        ) from exc

                tracked = output_paths + (
                    [report_path] if export_destination is None else []
                )
                snapshot = _snapshot_render_state(
                    tracked,
                    previous_report=previous,
                    history=history,
                    workspace=rollback_workspace,
                )

                report = render_module.render_job(
                    layout, assets=context.assets, manifest=manifest, job=job,
                    package=package, baseline_map=baseline_map,
                    template_map=template_map, render_settings=render_settings,
                    previous_report=previous, force=args.force,
                    destination=export_destination,
                )
                if export_destination is None and (
                    report["render_state"]["overall"] != "FAILED"
                    or not report_path.is_file()
                ):
                    atomic_write_json(report_path, report)
                    receipt = render_module.verify_receipt(
                        layout, context, job, package, report
                    )
                    if not receipt.ok:
                        raise JobError(
                            "new render receipt failed currentness verification:\n"
                            + receipt.render()
                        )
            except Exception as exc:
                locked = _locked_pipeline_destination(exc, snapshot, output_paths)
                scope = _render_failure_scope(exc)
                try:
                    if snapshot is not None:
                        _restore_render_state(snapshot)
                except Exception as rollback_exc:
                    raise ConfigurationError(
                        f"Render failed for {job_id}, and exact rollback could not be "
                        f"proven: {rollback_exc}"
                    ) from rollback_exc

                if scope == "shared":
                    if isinstance(exc, ConfigurationError):
                        raise
                    raise ConfigurationError(
                        f"Shared render resource failure while processing {job_id}: "
                        f"{type(exc).__name__}: {exc}"
                    ) from exc

                failures += 1
                if locked:
                    print(
                        f"[FAIL] {job_id}: The destination document is open or "
                        "locked. Close the open document and retry; --force cannot "
                        "override an operating-system lock."
                    )
                else:
                    print(f"[FAIL] {job_id}: {type(exc).__name__}: {exc}")
                continue

        assert report is not None
        state = report["render_state"]
        label = f"EXPORT-{state['overall']}" if export_destination else state["overall"]
        print(f"[{label}] {job_id}"
              f"  CV: {state['cv_docx']}/{state['cv_pdf']}"
              f"  letter: {state['letter_docx']}/{state['letter_pdf']}")
        for document in report["documents"]:
            if document["state"] not in ("OK",):
                for line in document["diagnostics"][:3]:
                    print(f"       {document['component']}.{document['format']}: {line}")
                if document.get("human_action"):
                    print(f"       action: {document['human_action']}")
            elif document.get("output_path"):
                print(f"       -> {Path(document['output_path']).name} "
                      f"({document['promotion']})")
            for warning in document.get("warnings", []):
                print(
                    f"       {document['component']}.{document['format']} "
                    f"warning: {warning}"
                )
        if state["overall"] == "FAILED":
            failures += 1

    if export_destination is not None:
        print(
            "External/explicit destination was a non-authoritative human export; "
            "the canonical render receipt and status were not changed."
        )

    return EXIT_JOB_FAILURE if failures else EXIT_OK


def cmd_preview(args: argparse.Namespace) -> int:
    layout = _layout(args)
    _, context = _context(layout, args.run)
    result = preview_module.run(
        layout, context, job_id=args.job,
        handoff=Path(args.handoff), semantic_file=_resolve_input(layout, args.file),
        soft_thresholds=_thresholds(context),
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return EXIT_OK if result["valid"] else EXIT_JOB_FAILURE


def cmd_status(args: argparse.Namespace) -> int:
    layout = _layout(args)
    manifest = load_manifest(layout, args.run)
    status = status_module.derive(layout, manifest)
    views = layout.generated / "views" / flatten_run_reference(manifest["run_id"])
    atomic_write_json(views / "status.json", status)
    queue = status_module.render_queue(status)
    atomic_write_text(views / "queue.md", queue)

    if args.json:
        print(json.dumps(status, indent=2, ensure_ascii=False))
    else:
        print(queue)
        print(f"(regenerated {views / 'status.json'} and {views / 'queue.md'})")
    if not status["integrity"]["ok"]:
        return EXIT_CONFIGURATION
    return (
        EXIT_JOB_FAILURE
        if any(
            j["production_state"] == "FAILED"
            or j["render_state"].get("overall") == "FAILED"
            for j in status["jobs"]
        )
        else EXIT_OK
    )


def cmd_next(args: argparse.Namespace) -> int:
    layout = _layout(args)
    manifest = load_manifest(layout, args.run)
    status = status_module.derive(layout, manifest)
    if not status["integrity"]["ok"]:
        print("Run integrity failed; no next semantic action is safe.")
        return EXIT_CONFIGURATION
    failed_at_stage: frozenset[str] = frozenset()
    if args.stage is not None:
        failed_at_stage = frozenset(
            entry["job_id"]
            for entry in manifest["jobs"]
            for record in (
                failure_module.load(layout, manifest["run_id"], entry["job_id"]),
            )
            if record
            and record.get("classification") == "FAILED"
            and record.get("operation") == f"STAGE{args.stage}"
        )
    job = status_module.next_job(
        status, stage=args.stage, cluster=args.cluster,
        failed_at_stage=failed_at_stage,
        spec_revision=manifest["spec_revision"],
    )
    if job is None:
        print("Nothing outstanding for that selection.")
        return EXIT_OK
    print(f"Next job : {job['job_id']}")
    print(f"  employer/title : {job['employer']} — {job['title']}")
    print(f"  cluster        : {job['cluster']} (sequence {job['sequence']})")
    print(f"  production     : {job['production_state']} "
          f"(highest valid stage: {job['highest_valid_stage'] or '-'})")
    print(f"  triage         : {job['semantic_triage'] or '-'}")
    print(f"  action         : {job['recommended_action']}")
    return EXIT_OK


#: The mandatory global boundary sections every Stage-3 author fetches and
#: Stage 1 has already read in full. Resolved structurally from the frozen
#: index, never from a hardcoded historical ordinal ID. A parent section span
#: stops at the next heading, so the §10 children are named explicitly.
def _frozen_authority_text(assets: Any, source_id: str) -> str:
    return retrieval.authority_text(assets, source_id)[1]


def _add_retrieval_payload(
    layout: Layout,
    manifest: dict[str, Any],
    context: Any,
    bundle: dict[str, Any],
    stage: int,
) -> None:
    """Revision-specific factual handoff from frozen authorities.

    Stage 1 reads the three unabridged frozen authorities. The x2b Stage 3
    receives only Stage-1-selected verbatim candidate passages and the global
    boundaries; earlier 0.9.3 runs retain their frozen open-source interface.
    """
    run_id = manifest["run_id"]
    index = context.index
    read = bundle["read"]

    if stage == 3 and manifest["spec_revision"] == X2B_REVISION:
        strategy = artifacts_module.load(
            layout, run_id, bundle["job"]["job_id"], "strategy"
        )
        if strategy is None:
            raise JobError("Stage-3 evidence packet requires the current Stage-1 strategy.")
        refs = retrieval.selected_strategy_refs(index, strategy)
        global_refs = {
            entry["evidence_id"]
            for source_id, section in retrieval.MANDATORY_SOURCE_SECTIONS
            if (entry := index_module.resolve_section(index, source_id, section))
        }
        entries = []
        for ref in refs:
            entry = index_module.resolve(index, ref)
            if entry is None:
                raise JobError(f"Stage-1 selected evidence {ref!r} does not resolve.")
            if ref not in global_refs:
                entries.append(entry)
        read["selected_evidence_refs"] = refs
        read["selected_evidence"] = retrieval.with_context(
            index, context.assets, entries, include_paths=False
        )
        read["selected_evidence_note"] = (
            "Only this Stage-1-selected candidate evidence may support the final "
            "package. The passages are copied verbatim from frozen authorities. "
            "The original vacancy and mechanical CV baseline remain separate inputs. "
            "If material evidence is missing, restart Stage 1 to expand the packet."
        )
        read["baseline_map"] = project_baseline_map(context.baseline_map)
        return

    if stage == 1:
        read["authorities"] = {
            key: str(frozen_path(layout, run_id,
                                 read_frozen(layout, manifest, "authorities", key)))
            for key in ("WORK", "EDU", "OTHER")
        }
        read["authorities_note"] = (
            "Read all three in full before ranking evidence. This is a mandatory "
            "complete read, not an optional list, and no budget or cap applies."
        )

    read["evidence_ids"] = index_module.ordered_evidence_ids(index)
    read["evidence_fetch"] = {
        "command": (
            f'.\\.venv\\Scripts\\python.exe runtime/tools/fetch.py --run {run_id}'
        ),
        "ids": '--ids "<comma-separated evidence IDs, returned in request order>"',
        "search": '--search "<literal case-insensitive string>"',
        "with_context": (
            f'.\\.venv\\Scripts\\python.exe runtime/tools/fetch.py --run {run_id} '
            '--ids "<comma-separated evidence IDs>" --with-context'
        ),
    }

    mandatory: list[str] = []
    for source_id, section in retrieval.MANDATORY_SOURCE_SECTIONS:
        entry = index_module.resolve_section(index, source_id, section)
        if entry is not None:
            mandatory.append(entry["evidence_id"])
    read["mandatory_source_refs"] = mandatory

    if stage == 3:
        digests: dict[str, list[dict[str, Any]]] = {}
        for source_id, section in retrieval.DIGEST_SECTIONS.items():
            entry = index_module.resolve_section(index, source_id, section)
            if entry is None:
                digests[source_id] = []
                continue
            text = _frozen_authority_text(context.assets, source_id)
            rows = []
            for row in index_module.digest_rows(text, entry):
                resolved = index_module.resolve_section(
                    index, source_id, row["source_section"]
                )
                rows.append(
                    {**row, "evidence_id": resolved["evidence_id"] if resolved else None}
                )
            digests[source_id] = rows
        read["authority_digests"] = digests
        read["authority_digests_note"] = (
            "Agent-maintained navigation metadata copied literally from the "
            "source tables. It identifies possibilities, never selected "
            "evidence, ranking authority or factual support."
        )

    bundle["optional_source_access"] = {
        "authorities": {
            key: str(frozen_path(layout, run_id,
                                 read_frozen(layout, manifest, "authorities", key)))
            for key in ("WORK", "EDU", "OTHER")
        },
        "evidence_index": str(
            frozen_path(layout, run_id, read_frozen(layout, manifest, "evidence_index"))
        ),
        "note": (
            "Open any original frozen authority directly for a specific "
            "inquiry. There is no access restriction, budget or cap."
        ),
    }

    read["baseline_map"] = project_baseline_map(context.baseline_map)
    read["baseline_map_note"] = (
        "Mechanical chronology and inventory. Use these exact ref values for BL "
        "references; a BL ref is never factual evidence and never belongs in "
        "used_evidence_refs."
    )


def _vacancy_pages(
    layout: Layout, manifest: dict[str, Any], job: dict[str, Any], run_dir: Path
) -> list[Path]:
    """Rasterized views of a flagged PDF vacancy (FE-04).

    Regenerated whenever the flagged bundle is prepared. A rendering error
    surfaces plainly rather than pretending pages exist; it is a production
    limitation, never a semantic package failure.
    """
    if not job.get("requires_source_inspection"):
        return []
    source = run_dir / job["source"]["relpath"]
    if source.suffix.lower() != ".pdf" or not source.is_file():
        return []
    destination = run_dir / "jobs" / job["job_id"] / "derived"
    return vacancy_module.render_source_pages(source, destination)


def cmd_context(args: argparse.Namespace) -> int:
    """Prepare the input bundle for one manually initiated stage."""
    layout = _layout(args)
    manifest, context = _context(layout, args.run)
    job = find_job(manifest, args.job)
    run_id = manifest["run_id"]
    run_dir = layout.run_dir(run_id)
    stage = args.stage
    legacy = manifest_module.is_legacy_run(manifest)
    thresholds = _thresholds(context)
    envelope = artifacts_module.handoff_for(
        layout, context, job["job_id"], stage, soft_thresholds=thresholds
    )
    handoff_path = artifacts_module.write_handoff(layout, envelope)
    expected = envelope["expected_artifacts"]
    return_dir = (
        layout.generated / "returns"
        / flatten_run_reference(run_id)
        / job["job_id"]
        / handoff_path.stem
    )
    return_dir.mkdir(parents=True, exist_ok=True)
    schema_paths = {
        name: str(
            context.schemas_dir
            / f"{artifacts_module.ARTIFACTS[name][1]}.schema.json"
        )
        for name in expected
    }
    return_paths = {
        name: str(return_dir / f"{name}.semantic.json")
        for name in expected
    }
    role = manifest["settings_snapshot"]["stages"][f"stage{stage}"]
    mapping = manifest["settings_snapshot"]["stages"].get("role_mapping", {})

    bundle: dict[str, Any] = {
        "run_id": run_id,
        "job": {
            "job_id": job["job_id"], "employer": job["employer"],
            "title": job["title"], "unit": job.get("unit"),
            "reference": job.get("reference"), "deadline": job.get("deadline"),
            "cluster": job["cluster"], "sequence": job["sequence"],
            "requires_source_inspection": job["requires_source_inspection"],
            "source_inspection_reasons": job.get("source_inspection_reasons", []),
        },
        "stage": stage,
        "capability_role": role,
        "configured_model": mapping.get(role) or None,
        "handoff": {
            "path": str(handoff_path),
            "mode": envelope["mode"],
            "stage_policy_sha256": envelope["stage_policy_sha256"],
            "upstream": envelope["upstream"],
            "semantic_retry_attempt": envelope.get("semantic_retry_attempt"),
        },
        "read": {
            "stage_instruction": str(
                frozen_path(layout, run_id,
                            read_frozen(layout, manifest, "stage_instructions", f"stage{stage}"))
            ),
            "vacancy_original": str(run_dir / job["source"]["relpath"]),
            "vacancy_derived_view": str(
                run_dir / "jobs" / job["job_id"] / "derived" / "vacancy_normalized.md"
            ),
            # §3.4: the policy records this stage actually consumes. Legacy
            # runs keep the full ordered list; a 0.9.3 Stage 1 gets doctrine
            # and persuasion only, matching its governing hash.
            "writing_policy": [
                str(frozen_path(layout, run_id, record))
                for record in manifest_module.writing_policy_records(manifest, stage)
            ],
        },
        "write": {
            "allowed": expected,
            "tool_owned_fields": {
                name: sorted(artifacts_module.MECHANICAL_FIELDS[name])
                for name in expected
            },
            "semantic_fields": {
                name: artifacts_module.semantic_fields(context, name)
                for name in expected
            },
            "schema_paths": schema_paths,
            "return_paths": return_paths,
            "instruction": (
                "Return only semantic fields. Do not include tooling-owned fields; "
                "stage-submit validates and inserts canonical metadata before commit."
            ),
        },
    }

    if stage == 3 and envelope["mode"] == "FINAL_AND_REVIEW":
        voice = context.assets.settings.get("voice")
        if voice is not None:
            bundle["final_polish"] = {
                "social_register_calibration": voice["social_register_calibration"]
            }

    if legacy:
        # Historical 0.9.0 payload, unchanged: the full frozen index and all
        # three authority paths for every stage. A frozen 0.9.0 source has no
        # digest table, so it never receives the 0.9.3 retrieval interface.
        bundle["read"]["evidence_index"] = str(
            frozen_path(layout, run_id, read_frozen(layout, manifest, "evidence_index"))
        )
        bundle["read"]["authorities"] = {
            key: str(frozen_path(layout, run_id,
                                 read_frozen(layout, manifest, "authorities", key)))
            for key in ("WORK", "EDU", "OTHER")
        }
    else:
        _add_retrieval_payload(layout, manifest, context, bundle, stage)

    if not legacy:
        # read.vacancy_pages belongs to the 0.9.3 payload. A historical run
        # keeps its own bundle shape and gains no new derived writes.
        pages = _vacancy_pages(layout, manifest, job, run_dir)
        if pages:
            bundle["read"]["vacancy_pages"] = [str(path) for path in pages]

    if stage == 1:
        bundle["read"]["personality_profile"] = str(
            frozen_path(layout, run_id, read_frozen(layout, manifest, "personality_profile"))
        )
        bundle["read"]["personality_facet_index"] = str(
            frozen_path(layout, run_id,
                        read_frozen(layout, manifest, "personality_facet_index"))
        )
    else:
        # Contract 12.5/12.6: distilled selected guidance only — the six
        # expression fields. The full profile, the facet ids and their evidence
        # references are deliberately not passed to Stage 2 or Stage 3.
        strategy = artifacts_module.load(layout, run_id, job["job_id"], "strategy")
        facets = (strategy or {}).get("personality_facets") or []
        bundle["personality_distilled"] = [
            {
                "plain_language_label": facet["plain_language_label"],
                "expression_ceiling": facet["expression_ceiling"],
                "expression_guardrail": facet.get("expression_guardrail"),
                "vacancy_relevance": facet.get("vacancy_relevance"),
                "intended_employer_interpretation": facet.get(
                    "intended_employer_interpretation"
                ),
                "misread_risk": facet.get("misread_risk"),
            }
            for facet in facets
        ]
        bundle["personality_note"] = (
            "Selected-facet expression guidance only, never factual authority: "
            "it cannot originate a proposition, an evidence selection or a "
            "claim ceiling. vacancy_relevance and "
            "intended_employer_interpretation state the employer inference the "
            "expression should support; expression_ceiling, expression_guardrail "
            "and misread_risk bound how far the realization may go. The full "
            "profile is not supplied." + (
                " Stage 3 may suppress, reinterpret, replace or ignore every "
                "personality-conditioned element without justifying it."
                if stage == 3 else ""
            )
        )
        if stage >= 2:
            bundle["read"]["strategy"] = str(
                artifacts_module.artifact_path(layout, run_id, job["job_id"], "strategy")
            )
            if legacy:
                bundle["read"]["baseline_map"] = str(
                    frozen_path(layout, run_id,
                                read_frozen(layout, manifest, "baseline_map"))
                )
        if legacy and stage == 3 and envelope["mode"] == "FINAL_AND_REVIEW":
            bundle["read"]["draft_package"] = str(
                artifacts_module.artifact_path(
                    layout, run_id, job["job_id"], "draft_package"
                )
            )

    if envelope["mode"] == "REVIEW_ONLY":
        bundle["read"]["final_package"] = str(
            artifacts_module.artifact_path(
                layout, run_id, job["job_id"], "final_package"
            )
        )

    command = (
        f'.\\.venv\\Scripts\\jobbsok.exe stage-submit --run {run_id} '
        f'--job {job["job_id"]} '
        f'--stage {stage} --handoff "{handoff_path}" '
    )
    if envelope["mode"] == "FINAL_AND_REVIEW":
        command += (
            f'--file "{return_paths["final_package"]}" '
            f'--review-file "{return_paths["review"]}"'
        )
    else:
        command += f'--file "{return_paths[expected[0]]}"'
    bundle["submission"] = {"command": command}
    if stage == 3 and envelope["mode"] == "FINAL_AND_REVIEW":
        bundle["preview"] = {"command": (
            f'.\\.venv\\Scripts\\jobbsok.exe preview --run {run_id} '
            f'--job {job["job_id"]} --handoff "{handoff_path}" '
            f'--file "{return_paths["final_package"]}"'
        )}

    print(json.dumps(bundle, indent=2, ensure_ascii=False))
    return EXIT_OK


def cmd_init_input(args: argparse.Namespace) -> int:
    layout = _layout(args)
    target = layout.inbox / "batch_input.csv"
    if target.exists() and not args.force:
        print(f"{target} already exists. Pass --force to overwrite.")
        return EXIT_CONFIGURATION
    write_template(target)
    print(f"Wrote an empty operator batch input to {target}")
    return EXIT_OK


def _moment(args: argparse.Namespace) -> datetime | None:
    if not getattr(args, "at", None):
        return None
    return datetime.fromisoformat(args.at).replace(tzinfo=timezone.utc)


# --------------------------------------------------------------------------
# Parser
# --------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="jobbsok",
        description="Jobbsok_26 P0.9 deterministic runtime. Makes no network "
                    "requests and no model calls.",
    )
    parser.add_argument("--root", default=None, help="Build root (default: discover).")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("preflight", help="Check environment, masters and assets.").set_defaults(
        handler=cmd_preflight
    )

    index = sub.add_parser("index", help="Build or verify the generated maps.")
    index.add_argument("action", choices=["build", "verify"])
    index.set_defaults(handler=cmd_index)

    init = sub.add_parser("init-input", help="Write an empty operator batch input.")
    init.add_argument("--force", action="store_true")
    init.set_defaults(handler=cmd_init_input)

    fr = sub.add_parser("freeze", help="Validate operator input and freeze a run.")
    fr.add_argument("--input", required=True)
    fr.add_argument("--reviewed-by", required=True,
                    help="Human who reviewed the baseline-to-authorities reconciliation.")
    fr.add_argument("--at", default=None, help="UTC timestamp override (tests).")
    fr.set_defaults(handler=cmd_freeze)

    br = sub.add_parser("branch", help="Create a child run; the parent is untouched.")
    br.add_argument("--run", required=True, help="Parent run reference.")
    br.add_argument(
        "--reviewed-by", required=True,
        help="Who actually compared the baseline with the approved sources.",
    )
    br.add_argument(
        "--from-stage", type=int, choices=[1, 3], default=None,
        help="First stage to execute again. Omitted keeps policy-driven reuse.",
    )
    br.add_argument(
        "--model-tag", default=branch_module.DEFAULT_MODEL_TAG,
        help="Optional short operator label for the child namespace.",
    )
    br.add_argument("--at", default=None)
    br.set_defaults(handler=cmd_branch)

    vi = sub.add_parser("verify-integrity", help="Check every manifest-frozen hash.")
    vi.add_argument("--run", required=True)
    vi.set_defaults(handler=cmd_verify_integrity)

    va = sub.add_parser("validate", help="Validate current semantic artifacts.")
    va.add_argument("--run", required=True)
    va.add_argument("--job", default=None)
    va.add_argument("--artifact", default="all",
                    choices=["all", "strategy", "draft", "draft_package",
                             "final", "final_package", "review"])
    va.set_defaults(handler=cmd_validate)

    ss = sub.add_parser("stage-submit", help="Validate and commit one stage return.")
    ss.add_argument("--run", required=True)
    ss.add_argument("--job", required=True)
    ss.add_argument("--stage", required=True, type=int, choices=[1, 3])
    ss.add_argument("--artifact", default=None,
                    choices=["strategy", "draft", "draft_package",
                             "final", "final_package", "review"])
    ss.add_argument("--file", required=True)
    ss.add_argument("--review-file", default=None)
    ss.add_argument("--handoff", required=True)
    ss.set_defaults(handler=cmd_stage_submit)

    pv = sub.add_parser("preview", help="Validate and render an unsubmitted Stage-3 package in temporary storage.")
    pv.add_argument("--run", required=True)
    pv.add_argument("--job", required=True)
    pv.add_argument("--handoff", required=True)
    pv.add_argument("--file", required=True)
    pv.set_defaults(handler=cmd_preview)

    ct = sub.add_parser("context", help="Prepare one stage's input bundle.")
    ct.add_argument("--run", required=True)
    ct.add_argument("--job", required=True)
    ct.add_argument("--stage", required=True, type=int, choices=[1, 3])
    ct.set_defaults(handler=cmd_context)

    fi = sub.add_parser("finalize", help="Assign the canonical document date.")
    fi.add_argument("--run", required=True)
    fi.add_argument("--job", required=True)
    fi.add_argument("--date", default=None, help="ISO date; defaults to today.")
    fi.add_argument("--reviewed-by", default="operator")
    fi.set_defaults(handler=cmd_finalize)

    rd = sub.add_parser("render", help="Render finalized jobs to DOCX and PDF.")
    rd.add_argument("--run", required=True)
    rd.add_argument("--job", default=None)
    rd.add_argument("--force", action="store_true",
                    help="Overwrite a deliverable that was edited outside the pipeline.")
    rd.add_argument("--dest", default=None, help="Alternate output directory.")
    rd.set_defaults(handler=cmd_render)

    st = sub.add_parser("status", help="Derive the three status axes and the queue.")
    st.add_argument("--run", required=True)
    st.add_argument("--json", action="store_true")
    st.set_defaults(handler=cmd_status)

    nx = sub.add_parser("next", help="Find the next job to work on.")
    nx.add_argument("--run", required=True)
    nx.add_argument("--stage", type=int, choices=[1, 3], default=None)
    nx.add_argument("--cluster", default=None)
    nx.set_defaults(handler=cmd_next)

    return parser


def main(argv: list[str] | None = None) -> int:
    ioenc.install()
    args = build_parser().parse_args(argv)
    try:
        return args.handler(args)
    except RunIntegrityError as exc:
        print(f"RUN-INTEGRITY ERROR\n{exc}", file=sys.stderr)
        return EXIT_CONFIGURATION
    except JobbsokError as exc:
        print(f"ERROR ({type(exc).__name__})\n{exc}", file=sys.stderr)
        return exc.exit_code
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return EXIT_CONFIGURATION


if __name__ == "__main__":
    raise SystemExit(main())
