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

from . import artifacts as artifacts_module
from . import assemble as assemble_module
from . import cards as cards_module
from . import pipeline
from . import preview as preview_module
from . import signals as signals_module
from . import evidence_index as index_module
from . import manifest as manifest_module
from . import branch as branch_module
from . import ioenc
from . import render as render_module
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
        from_stage=args.from_stage, label=args.label,
        refresh_inputs=args.refresh_inputs, moment=_moment(args),
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
    wanted = list(pipeline.all_artifacts())
    if args.artifact and args.artifact != "all":
        wanted = [pipeline.canonical_name(args.artifact)]
    jobs = [find_job(manifest, args.job)] if args.job else manifest["jobs"]

    failures = 0
    checked = 0
    for job in jobs:
        if job["job_class"] == "EXCEPTION":
            continue
        job_id = job["job_id"]
        state = artifacts_module.semantic_state(
            layout, context, job_id, soft_thresholds=thresholds
        )
        for name in wanted:
            payload = state.loaded.get(name)
            if payload is None:
                continue
            checked += 1
            result = validate_module.validate_artifact(
                layout, context, job_id, name, payload, soft_thresholds=thresholds
            )
            label = f"{job_id}/{pipeline.ARTIFACTS[name].filename}"
            if result.ok:
                warnings = len(result.warnings)
                print(f"[PASS] {label}" + (f"  ({warnings} warning(s))" if warnings else ""))
                if warnings:
                    print(result.render())
            else:
                failures += 1
                print(f"[FAIL] {label}")
                print(result.render())
            if name in state.stale:
                print(f"[STALE] {label}: {state.stale_reason.get(name)}")

    print(f"\nChecked {checked} artifact(s); {failures} failed.")
    return EXIT_JOB_FAILURE if failures else EXIT_OK


def _returns_dir(layout: Layout, run_id: str, job_id: str, stage: int) -> Path:
    return (
        layout.generated / "returns" / flatten_run_reference(run_id) / job_id
        / f"stage{stage}"
    )


def _read_return(
    layout: Layout, run_id: str, job_id: str, stage: int, artifact: str,
    fingerprint: str, explicit: str | None = None,
) -> dict[str, Any]:
    if explicit:
        return read_json(Path(explicit))
    path = (
        _returns_dir(layout, run_id, job_id, stage) / fingerprint[:8]
        / f"{artifact}.semantic.json"
    )
    if not path.is_file():
        raise JobError(
            f"Missing return file for {artifact}: {path}\n"
            "Write the semantic fields there (the exact path is in the context "
            "bundle's write.return_paths), or pass --file."
        )
    return read_json(path)


def _write_set(stage: int, reject: bool) -> tuple[str, ...]:
    if stage == 3:
        return ("review",) if reject else ("polish", "review")
    return pipeline.STAGES[stage].writes


def cmd_stage_submit(args: argparse.Namespace) -> int:
    if args.stage != 3 and (args.reject or args.finalize_render):
        raise JobError("--reject and --finalize-render are Stage 3 only.")
    layout = _layout(args)
    manifest, context = _context(layout, args.run)
    job = find_job(manifest, args.job)
    job_id = job["job_id"]
    stage = args.stage
    reject = stage == 3 and bool(getattr(args, "reject", False))
    if job["job_class"] == "EXCEPTION":
        raise JobError(f"{job_id} is an EXCEPTION job and has no core stages.")

    thresholds = _thresholds(context)
    state = artifacts_module.semantic_state(
        layout, context, job_id, soft_thresholds=thresholds
    )
    missing = [
        name for name in pipeline.STAGES[stage].requires
        if state.loaded.get(name) is None or (not reject and not state.current(name))
    ]
    if missing:
        raise JobError(
            f"Stage {stage} needs current {', '.join(missing)}. Run the earlier "
            "stage first, or re-run context to see what moved."
        )

    fingerprint = pipeline.evidence_fingerprint(context, job_id, stage)
    if args.fingerprint != fingerprint[:8]:
        raise JobError(
            f"The context changed while this stage was working: the bundle was "
            f"issued at {args.fingerprint} and the current evidence fingerprint "
            f"is {fingerprint[:8]}. Re-run:\n"
            f"  jobbsok context --run {args.run} --job {job_id} --stage {stage}"
        )

    write_set = _write_set(stage, reject)
    returns = {
        name: _read_return(
            layout, context.run_id, job_id, stage, name, fingerprint,
            args.file if (args.file and len(write_set) == 1) else None,
        )
        for name in write_set
    }

    result = ValidationResult()
    payloads: dict[str, dict[str, Any]] = {}
    upstream = pipeline.upstream_hashes(context, job_id, write_set[0])

    for name in write_set:
        if name == "review":
            continue
        payload = artifacts_module.stamp(
            context, job_id, name, returns[name], upstream=dict(upstream)
        )
        payloads[name] = payload
        upstream[name] = artifacts_module.artifact_hash(payload)
        result.extend(
            validate_module.validate_artifact(
                layout, context, job_id, name, payload, soft_thresholds=thresholds
            ).violations
        )

    if stage == 3 and not reject:
        package_fields, summary = assemble_module.assemble(
            state.loaded["cv_draft"], state.loaded["advocacy_draft"], payloads["polish"]
        )
        final = artifacts_module.stamp(
            context, job_id, "final_package", package_fields, upstream=dict(upstream)
        )
        payloads["final_package"] = final
        upstream["final_package"] = artifacts_module.artifact_hash(final)
        result.extend(
            validate_module.validate_artifact(
                layout, context, job_id, "final_package", final,
                soft_thresholds=thresholds,
            ).violations
        )
    else:
        summary = None

    if "review" in write_set:
        review_upstream = dict(upstream)
        if reject:
            review_upstream.pop("final_package", None)
        review = artifacts_module.stamp(
            context, job_id, "review", returns["review"], upstream=review_upstream
        )
        payloads["review"] = review
        result.extend(
            validate_module.validate_artifact(
                layout, context, job_id, "review", review, soft_thresholds=thresholds
            ).violations
        )
        if reject and review.get("triage") != "RERUN":
            raise JobError("--reject requires the review's triage to be RERUN.")
        if not reject and review.get("triage") == "RERUN":
            raise JobError("publish refused: triage is RERUN; use --reject.")

    if not result.ok:
        _emit(result, header="Submission refused before persistence:")
        return EXIT_JOB_FAILURE

    changed = {
        name for name, payload in payloads.items()
        if state.digest(name) != artifacts_module.artifact_hash(payload)
    }
    downstream = []
    for name, spec in pipeline.ARTIFACTS.items():
        owner = spec.owner_stage if spec.owner_stage is not None else 3
        if owner > stage and state.loaded.get(name) and name not in state.stale and changed.intersection(spec.inputs):
            downstream.append(f"{name} (Stage {owner})")
    if downstream:
        print("[WARN] this submit will stale: " + ", ".join(downstream))
        print("       downstream work exists for this job")

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    if stage == 3:
        old_final = state.loaded.get("final_package") or {}
        new_final = payloads.get("final_package") or {}
        if reject or (old_final.get("letter") and not new_final.get("letter")) or (
            old_final.get("form_answers") and not new_final.get("form_answers")
        ):
            _withdraw_outputs(layout, context.run_id, job_id, timestamp)
    written = artifacts_module.submit_many(
        layout, context.run_id, job_id, payloads, timestamp=timestamp
    )
    if stage == 3 and reject:
        for name in ("polish", "final_package"):
            if state.loaded.get(name) is None:
                continue
            artifacts_module.discard(
                layout, context.run_id, job_id, name, timestamp=timestamp
            )
            print(f"[WITHDRAW] {name} -> history/{timestamp}_{name}.json")

    for item in written:
        print(f"[COMMIT] {item.artifact} -> {item.path}")
        if item.superseded:
            print(f"         superseded copy in history/{item.superseded.name}")
    if summary is not None:
        print()
        print(assemble_module.render_summary(summary))
        answers = payloads["final_package"].get("form_answers")
        if answers:
            path = _write_form_answers(layout, context.run_id, job, answers)
            print(f"form answers -> {path}")
    _emit(result)

    if getattr(args, "finalize_render", False) and not reject:
        finalize_args = argparse.Namespace(
            root=args.root, run=args.run, job=job_id, date=None,
            reviewed_by="operator",
        )
        code = cmd_finalize(finalize_args)
        if code != EXIT_OK:
            return code
        render_args = argparse.Namespace(
            root=args.root, run=args.run, job=job_id, force=False, dest=None,
        )
        return cmd_render(render_args)
    return EXIT_OK


def _write_form_answers(
    layout: Layout, run_id: str, job: dict[str, Any], answers: list[dict[str, Any]]
) -> Path:
    lines = [f"# Form answers - {job['employer']}, {job['title']}", ""]
    for item in answers:
        lines.append(f"**{item['question']}**")
        lines.append("")
        lines.append(item["answer"])
        lines.append("")
    path = layout.job_dir(run_id, job["job_id"]) / "out" / "form_answers.md"
    atomic_write_text(path, "\n".join(lines))
    atomic_write_json(path.parent / "form_answers.receipt.json", {
        "output_path": str(path), "output_sha256": sha256_file(path),
    })
    return path


def _withdraw_outputs(layout: Layout, run_id: str, job_id: str, timestamp: str) -> None:
    job_dir = layout.job_dir(run_id, job_id)
    out = job_dir / "out"
    receipt = job_dir / "current" / "render_report.json"
    form_receipt = out / "form_answers.receipt.json"
    records = (read_json(receipt).get("documents") or []) if receipt.is_file() else []
    if form_receipt.is_file():
        records.append(read_json(form_receipt))
    paths = []
    for record in records:
        if not record.get("output_path"):
            continue
        path = Path(record["output_path"])
        if path.resolve().parent != out.resolve():
            raise JobError(f"Receipt output is outside this job's out directory: {path}")
        if path.is_file():
            paths.append(path)
    paths += [p for p in (receipt, form_receipt) if p.is_file()]
    destination = out / "withdrawn" / timestamp
    for path in dict.fromkeys(paths):
        destination.mkdir(parents=True, exist_ok=True)
        target = destination / path.name
        path.rename(target)
        print(f"[WITHDRAW] {path} -> {target}")


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
    if (state.loaded.get("review") or {}).get("triage") == "RERUN":
        raise JobError("finalize refused: triage is RERUN.")
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
                    for _name in pipeline.all_artifacts():
                        artifacts_module.load(layout, context.run_id, job_id, _name)
                except ConfigurationError as exc:
                    raise JobError(
                        f"malformed job-local semantic state: {exc}"
                    ) from exc
                semantic_state = artifacts_module.semantic_state(
                    layout, context, job_id, soft_thresholds=_thresholds(context)
                )
                if (semantic_state.loaded.get("review") or {}).get("triage") == "RERUN":
                    raise JobError("render refused: triage is RERUN.")
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
    job = status_module.next_job(status, stage=args.stage, cluster=args.cluster)
    if job is None:
        print("Nothing outstanding for that selection.")
        return EXIT_OK
    stage = job["next_stage"]
    print(f"Next job : {job['job_id']}")
    print(f"  employer/title : {job['employer']} - {job['title']}")
    print(f"  cluster        : {job['cluster']} (sequence {job['sequence']})")
    print(f"  production     : {job['production_state']} "
          f"(highest valid stage: {job['highest_valid_stage'] or '-'})")
    print(f"  triage         : {job['semantic_triage'] or '-'}")
    print(f"  next stage     : {stage if stage is not None else 'finalize/render'}")
    print(f"  action         : {job['recommended_action']}")
    if job.get("signals"):
        print(f"  signals        : {'; '.join(job['signals'])}")
    if stage is not None:
        print()
        print(f"  jobbsok context --run {args.run} --job {job['job_id']} --stage {stage}")
    return EXIT_OK


#: The mandatory global boundary sections every Stage-3 author fetches and
#: Stage 1 has already read in full. Resolved structurally from the frozen
#: index, never from a hardcoded historical ordinal ID. A parent section span
#: stops at the next heading, so the §10 children are named explicitly.
MANDATORY_SOURCE_SECTIONS: tuple[tuple[str, str], ...] = (
    ("WORK", "8"), ("WORK", "10.1"), ("WORK", "10.2"),
    ("EDU", "4.2"), ("EDU", "4.3"),
    ("OTHER", "0.3"), ("OTHER", "4.5"),
)

#: Where each authority keeps its agent-maintained digest table.
DIGEST_SECTIONS: dict[str, str] = {"WORK": "0.3", "OTHER": "0.2", "EDU": "0.5"}


def _policy_markdown(context: Any, stage: int) -> str:
    """The policy sections this stage consumes, assembled verbatim."""
    spec = pipeline.STAGES[stage]
    parts = [f"# Policy for stage {stage} ({spec.key})", ""]
    records = {
        Path(record["path"]).name: record
        for record in context.manifest["frozen_inputs"]["writing_policy"]
    }
    for filename, headings in spec.policy.items():
        record = records.get(filename)
        if record is None:
            parts.append(f"policy_missing: {filename}")
            continue
        text = (
            context.assets.run_dir / "frozen" / record["path"]
        ).read_bytes().decode("utf-8")
        if headings == "ALL":
            parts.append(text.strip())
            parts.append("")
            continue
        lines = text.splitlines()
        heads = index_module._headings(lines)
        for wanted in headings:
            found = None
            for position, (line_no, level, title) in enumerate(heads):
                if wanted.casefold() in title.casefold():
                    end = len(lines)
                    for later_line, later_level, _ in heads[position + 1:]:
                        if later_level <= level:
                            end = later_line - 1
                            break
                    found = "\n".join(lines[line_no - 1:end]).strip()
                    break
            if found is None:
                parts.append(f"policy_missing: {filename} / {wanted}")
            else:
                parts.append(found)
            parts.append("")
    return "\n".join(parts)


def _personality_distilled(strategy: dict[str, Any] | None) -> list[dict[str, Any]]:
    """The selected facets as behaviour, without the private facet labels."""
    facets = ((strategy or {}).get("distinctiveness") or {}).get("facets") or []
    return [{"behaviour": facet.get("behaviour")} for facet in facets]


def _rerun_advice(state: Any, stage: int) -> str | None:
    review = state.loaded.get("review")
    if not review or review.get("triage") != "RERUN":
        return None
    if review.get("rerun_stage") != stage:
        return None
    lines = ["# The editor sent this job back to you", ""]
    for reason in review.get("reasons") or []:
        lines.append(f"- {reason['reason']} -> {reason['recommended_action']}")
    for note in review.get("notes") or []:
        lines.append(f"- note: {note}")
    return "\n".join(lines) + "\n"


def cmd_context(args: argparse.Namespace) -> int:
    layout = _layout(args)
    manifest, context = _context(layout, args.run)
    job = find_job(manifest, args.job)
    job_id = job["job_id"]
    stage = args.stage
    if job["job_class"] == "EXCEPTION":
        raise JobError(
            f"{job_id} is an EXCEPTION job: handle it outside the core pipeline."
        )
    spec = pipeline.STAGES[stage]
    thresholds = _thresholds(context)
    state = artifacts_module.semantic_state(
        layout, context, job_id, soft_thresholds=thresholds
    )
    missing = [name for name in spec.requires if state.loaded.get(name) is None]
    unavailable = [name for name in spec.requires if not state.current(name)]
    diagnostic = stage == 3 and bool(unavailable) and not missing
    if stage != 3:
        missing = unavailable
    if missing:
        raise JobError(
            f"Stage {stage} ({spec.key}) needs current {', '.join(missing)} for "
            f"{job_id}. Run the earlier stage first."
        )

    fingerprint = pipeline.evidence_fingerprint(context, job_id, stage)
    base = _returns_dir(layout, context.run_id, job_id, stage) / fingerprint[:8]
    inputs_dir = base / "inputs"
    inputs_dir.mkdir(parents=True, exist_ok=True)

    def write(name: str, text: str) -> str:
        path = inputs_dir / name
        atomic_write_text(path, text)
        return str(path)

    run_id = context.run_id
    frozen = lambda *keys: str(
        frozen_path(layout, run_id, read_frozen(layout, manifest, *keys))
    )
    read: dict[str, Any] = {
        "playbook": frozen("stage_instructions", f"stage{stage}"),
        "policy": write("policy.md", _policy_markdown(context, stage)),
        "vacancy": str(
            layout.job_dir(run_id, job_id) / "derived" / "vacancy_normalized.md"
        ),
    }
    optional: dict[str, Any] = {
        "vacancy_original": str(
            layout.job_dir(run_id, job_id) / "source"
            / Path(job["source"]["relpath"]).name
        ),
        "authorities": {
            key: frozen("authorities", key) for key in ("WORK", "EDU", "OTHER")
        },
        "note": (
            "Fetch anything you need: jobbsok cards --run RUN --ids EV:... "
            "or --search \"literal\". Nothing is refused; declare what you used "
            "beyond the brief in outside_brief_refs."
        ),
    }

    if stage == 0:
        read["digests"] = write("digests.md", cards_module.digests(context))
        read["retrieval_index"] = write(
            "retrieval.md", cards_module.retrieval_index(context)
        )
        read["catalog"] = write("catalog.md", cards_module.catalog(context))
        read["baseline_projection"] = project_baseline_map(context.baseline_map)
    elif stage == 1:
        scout = state.loaded["scout"]
        read["scout"] = str(
            artifacts_module.artifact_path(layout, run_id, job_id, "scout")
        )
        core = [item["ref"] for item in (scout.get("triage") or {}).get("core") or []]
        read["cards"] = write(
            "cards_core.md", cards_module.pack(context, core, title="Core evidence")
        )
        reserve_lines = ["# Reserve evidence (demoted, not dropped)", ""]
        for item in (scout.get("triage") or {}).get("reserve") or []:
            reserve_lines.append(f"- {item['ref']} - {item['why']}")
        read["reserve"] = write("reserve.md", "\n".join(reserve_lines) + "\n")
        read["digests"] = write("digests.md", cards_module.digests(context))
        read["retrieval_index"] = write(
            "retrieval.md", cards_module.retrieval_index(context)
        )
        read["catalog"] = write("catalog.md", cards_module.catalog(context))
        read["baseline_projection"] = project_baseline_map(context.baseline_map)
        read["facets"] = write("facets.md", cards_module.facet_projection(context))
        read["capacity"] = settings_module.capacity(context.assets.settings)
        optional["personality_profile"] = frozen("personality_profile")
        optional["facet_index_full"] = frozen("personality_facet_index")
    elif stage == 2:
        brief = state.loaded["brief"]
        read["brief"] = str(
            artifacts_module.artifact_path(layout, run_id, job_id, "brief")
        )
        read["cv_draft"] = str(
            artifacts_module.artifact_path(layout, run_id, job_id, "cv_draft")
        )
        scout = dict(state.loaded.get("scout") or {})
        scout.pop("triage", None)
        read["scout_facts"] = write(
            "scout_facts.json", json.dumps(scout, ensure_ascii=False, indent=2)
        )
        read["cards"] = write(
            "cards_scoped.md",
            cards_module.pack(
                context, cards_module.default_ids(context, job_id, 2),
                title="Evidence named in the brief",
            ),
        )
        read["capacity"] = settings_module.capacity(context.assets.settings)
    else:
        if not diagnostic:
            package, summary = preview_module.build_package(layout, context, job_id, 3)
            read["assembled_draft"] = write(
                "assembled_draft.json",
                json.dumps(
                    {k: v for k, v in package.items() if k not in ("finalization",)},
                    ensure_ascii=False, indent=2,
                ),
            )
            read["draft_summary"] = assemble_module.render_summary(summary)
        else:
            for name in spec.requires:
                read[name] = str(artifacts_module.artifact_path(layout, run_id, job_id, name))
        read["brief"] = str(
            artifacts_module.artifact_path(layout, run_id, job_id, "brief")
        )
        scout = dict(state.loaded.get("scout") or {})
        scout.pop("triage", None)
        read["scout_facts"] = write(
            "scout_facts.json", json.dumps(scout, ensure_ascii=False, indent=2)
        )
        read["cards"] = write(
            "cards_used.md",
            cards_module.pack(
                context, cards_module.default_ids(context, job_id, 3),
                title="Evidence used by the draft",
            ),
        )
        read["keystones"] = (state.loaded.get("advocacy_draft") or {}).get(
            "keystones"
        ) or []
        read["personality_distilled"] = _personality_distilled(state.loaded.get("brief"))
        read["voice_level"] = settings_module.voice_level(context.assets.settings)
        read["capacity"] = settings_module.capacity(context.assets.settings)

    if stage in (2, 3):
        read["digests"] = write("digests.md", cards_module.digests(context))
        read["retrieval_index"] = write("retrieval.md", cards_module.retrieval_index(context))
        read["catalog"] = write("catalog.md", cards_module.catalog(context))

    register_path = layout.generated / "views" / flatten_run_reference(run_id) / (
        f"register_{job['cluster']}.md"
    )
    if stage >= 1:
        atomic_write_text(register_path, _register_markdown(layout, context, job["cluster"]))
        read["register"] = str(register_path)
    advice = _rerun_advice(state, stage)
    if advice:
        read["rerun_advice"] = write("rerun_advice.md", advice)

    write_paths = {
        name: str(base / f"{name}.semantic.json")
        for name in _write_set(stage, diagnostic)
    }
    bundle = {
        "artifact_role": "STAGE_CONTEXT",
        "run_id": run_id,
        "job": {
            "job_id": job_id, "employer": job["employer"], "title": job["title"],
            "cluster": job["cluster"], "deadline": job.get("deadline"),
            "unit": job.get("unit"), "reference": job.get("reference"),
        },
        "stage": stage,
        "stage_key": spec.key,
        "configured_model": manifest["settings_snapshot"]["role_mapping"].get(spec.key),
        "evidence_fingerprint": fingerprint,
        "read": read,
        "optional": optional,
        "write": {
            "allowed": list(_write_set(stage, diagnostic)),
            "return_paths": write_paths,
            "schema_paths": {
                name: str(context.schemas_dir / f"{pipeline.ARTIFACTS[name].schema}.schema.json")
                for name in _write_set(stage, diagnostic)
            },
            "tool_owned_fields": sorted(pipeline.TOOL_FIELDS),
        },
        "commands": {
            "cards": f"jobbsok cards --run {run_id} --ids \"EV:...\"",
            "search": f"jobbsok cards --run {run_id} --search \"literal\"",
            "preview": f"jobbsok preview --run {run_id} --job {job_id} --stage {stage}",
            "assemble_dry": f"jobbsok assemble --run {run_id} --job {job_id} --dry-run",
            "register": f"jobbsok register --run {run_id} --cluster {job['cluster']}",
            "submit": (
                f"jobbsok stage-submit --run {run_id} --job {job_id} --stage {stage} "
                f"--fingerprint {fingerprint[:8]}"
                + (" --reject" if diagnostic else " --finalize-render" if stage == 3 else "")
            ),
        },
    }
    if diagnostic:
        bundle["upstream_state"] = {
            name: {
                "state": "INVALID" if name in state.invalid else "STALE" if name in state.stale else "CURRENT",
                "reason": state.stale_reason.get(name) or ("schema or reference validation failed" if name in state.invalid else None),
            }
            for name in spec.requires
        }
        bundle["write"]["blocked"] = {
            "polish": "requires current valid " + ", ".join(unavailable)
        }
    if stage == 3:
        bundle["commands"]["reject"] = (
            f"jobbsok stage-submit --run {run_id} --job {job_id} --stage 3 "
            f"--fingerprint {fingerprint[:8]} --reject"
        )

    if args.stats:
        rows = []
        for key, value in read.items():
            if isinstance(value, str) and Path(value).is_file():
                size = Path(value).stat().st_size
            else:
                size = len(json.dumps(value, ensure_ascii=False))
            rows.append((key, size))
        total = sum(size for _, size in rows)
        print("# context size")
        for key, size in sorted(rows, key=lambda item: -item[1]):
            print(f"  {key:22s} {size:8d} bytes  ~{size // 3.3:7.0f} tokens")
        print(f"  {'TOTAL':22s} {total:8d} bytes  ~{total // 3.3:7.0f} tokens")
        print()
    print(json.dumps(bundle, indent=2, ensure_ascii=False))
    return EXIT_OK


# --------------------------------------------------------------------------
# Cards, preview, assemble, register
# --------------------------------------------------------------------------

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


def cmd_cards(args: argparse.Namespace) -> int:
    layout = _layout(args)
    manifest, context = _context(layout, args.run)
    if args.search:
        hits = cards_module.search(context, args.search)
        for hit in hits:
            print(f"{hit['evidence_id']}  [{hit['source_id']}]  {hit['heading']}")
        print(f"\n{len(hits)} match(es). Fetch with --ids.")
        return EXIT_OK
    if args.ids:
        ids = [item.strip() for item in args.ids.split(",") if item.strip()]
        resolved: list[str] = []
        for item in ids:
            if item.startswith("EV:"):
                resolved.append(item)
                continue
            hits = cards_module.search(context, item)
            if not hits:
                print(f"(no evidence resolves {item!r})")
            resolved.extend(hit["evidence_id"] for hit in hits)
        text = cards_module.pack(context, resolved, full=args.full)
    else:
        if not (args.job and args.stage is not None):
            raise JobError("Pass --ids, --search, or both --job and --stage.")
        ids = cards_module.default_ids(context, args.job, args.stage)
        text = cards_module.pack(context, ids, full=args.full,
                                 title=f"Default pack for stage {args.stage}")
    if args.out:
        atomic_write_text(Path(args.out), text)
        print(f"wrote {args.out} ({len(text)} bytes)")
    else:
        print(text)
    return EXIT_OK


def cmd_preview(args: argparse.Namespace) -> int:
    layout = _layout(args)
    manifest, context = _context(layout, args.run)
    metrics = preview_module.preview(
        layout, context, args.job, args.stage, cv_only=args.cv_only
    )
    capacity = settings_module.capacity(context.assets.settings)
    for line in preview_module.render_report_lines(metrics, capacity):
        print(line)
    print(f"files     : {metrics['destination']}")
    return EXIT_OK


def cmd_assemble(args: argparse.Namespace) -> int:
    layout = _layout(args)
    manifest, context = _context(layout, args.run)
    job_id = args.job
    layers, sources = preview_module.resolve_layers(layout, context, job_id, 3)
    cv_draft = (
        read_json(Path(args.cv)) if args.cv else layers["cv_draft"]
    )
    if cv_draft is None:
        raise JobError("No CV layer yet; Stage 1 writes cv_draft.")
    advocacy = (
        read_json(Path(args.advocacy)) if args.advocacy
        else layers["advocacy_draft"]
    )
    polish = (
        read_json(Path(args.polish)) if args.polish else layers["polish"]
    )
    for name, explicit in (("cv_draft", args.cv), ("advocacy_draft", args.advocacy), ("polish", args.polish)):
        if explicit:
            sources[name] = str(explicit)
    print("state     : " + preview_module.layer_states(layout, context, job_id, sources))
    for name, source in sources.items():
        print(f"source    : {name}: {source}")
    package, summary = assemble_module.assemble(cv_draft, advocacy, polish)
    print(assemble_module.render_summary(summary))
    print()
    cv = package["cv"]
    print(f"CV headline : {cv.get('headline')}")
    print(f"CV profile  : {cv.get('profile')}")
    if package.get("letter"):
        letter = package["letter"]
        print()
        print(letter["opening"])
        for paragraph in letter["body_paragraphs"]:
            print()
            print(paragraph)
        print()
        print(letter["closing"])
    return EXIT_OK


def _register_markdown(layout: Layout, context: Any, cluster: str | None) -> str:
    """What every letter in this cluster already does, so the next one differs."""
    manifest = context.manifest
    lines = [f"# Variation register - cluster {cluster or 'all'}", ""]
    lines += ["| job | state |", "|---|---|"]
    for job in manifest["jobs"]:
        if cluster and job["cluster"] != cluster:
            continue
        state = artifacts_module.semantic_state(layout, context, job["job_id"])
        labels = [f"{name}=INVALID" for name in sorted(state.invalid)]
        labels += [f"{name}=STALE" for name in sorted(state.stale - state.invalid)]
        label = "; ".join(labels) or ("CURRENT" if any(state.loaded.values()) else "NOT_STARTED")
        lines.append(f"| {job['job_id']} | {label} |")
    lines.append("")
    for job in manifest["jobs"]:
        if cluster and job["cluster"] != cluster:
            continue
        job_id = job["job_id"]
        brief = artifacts_module.load(layout, context.run_id, job_id, "brief") or {}
        final = artifacts_module.load(layout, context.run_id, job_id, "final_package")
        draft = artifacts_module.load(layout, context.run_id, job_id, "advocacy_draft")
        letter = (final or draft or {}).get("letter") or {}
        distinct = brief.get("distinctiveness") or {}
        lines.append(f"## {job_id} - {job['employer']}, {job['title']}")
        lines.append("")
        if brief:
            lines.append(f"- track: {(brief.get('position') or {}).get('track')}")
            lines.append(f"- delivery: {brief.get('delivery')}")
            lines.append(
                f"- moves: opening {distinct.get('opening_move')}, "
                f"closing {distinct.get('closing_move')}"
            )
            lines.append(f"- motive: {distinct.get('motive')}")
            facets = ", ".join(
                f"{facet['facet_id']} ({facet['behaviour'][:60]})"
                for facet in distinct.get("facets") or []
            )
            lines.append(f"- facets: {facets or '-'}")
            fact = brief.get("employer_fact") or {}
            lines.append(f"- employer fact: {fact.get('fact', '-')}")
            if brief.get("outside_scout_refs"):
                lines.append(
                    f"- outside scout: {', '.join(brief['outside_scout_refs'])}"
                )
        if letter:
            lines.append(f"- first sentence: {signals_module.first_sentence(letter.get('opening', ''))}")
            lines.append(f"- last sentence: {signals_module.last_sentence(letter.get('closing', ''))}")
        package = final or {"cv": (artifacts_module.load(
            layout, context.run_id, job_id, "cv_draft") or {}).get("cv"), "letter": letter}
        found = signals_module.scan(package)
        lines.append(f"- signals: {', '.join(found) if found else 'none'}")
        lines.append("")
    return "\n".join(lines)


def cmd_register(args: argparse.Namespace) -> int:
    layout = _layout(args)
    manifest, context = _context(layout, args.run)
    text = _register_markdown(layout, context, args.cluster)
    path = layout.generated / "views" / flatten_run_reference(context.run_id) / (
        f"register_{args.cluster or 'all'}.md"
    )
    atomic_write_text(path, text)
    print(text)
    print(f"(wrote {path})")
    return EXIT_OK


# --------------------------------------------------------------------------
# Parser
# --------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="jobbsok",
        description="Jobbsok_26 Relay runtime (experimental). Four human-started "
                    "stages; no network requests and no model calls.",
    )
    parser.add_argument("--root", default=None, help="Build root (default: discover).")
    sub = parser.add_subparsers(dest="command", required=True)
    stages = list(pipeline.STAGE_ORDER)

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
    fr.add_argument("--reviewed-by", required=True)
    fr.add_argument("--at", default=None)
    fr.set_defaults(handler=cmd_freeze)

    br = sub.add_parser("branch", help="Create a child run; the parent is untouched.")
    br.add_argument("--run", required=True)
    br.add_argument("--reviewed-by", required=True)
    br.add_argument("--from-stage", type=int, choices=stages, default=None,
                    help="First stage to execute again.")
    br.add_argument("--label", default=branch_module.DEFAULT_LABEL,
                    help="Short label for the child namespace.")
    br.add_argument("--refresh-inputs", action="store_true",
                    help="Re-collect the factual inputs from the repository and "
                         "drop artifacts whose evidence fingerprint changed.")
    br.add_argument("--at", default=None)
    br.set_defaults(handler=cmd_branch)

    vi = sub.add_parser("verify-integrity", help="Check every manifest-frozen hash.")
    vi.add_argument("--run", required=True)
    vi.set_defaults(handler=cmd_verify_integrity)

    va = sub.add_parser("validate", help="Validate current semantic artifacts.")
    va.add_argument("--run", required=True)
    va.add_argument("--job", default=None)
    va.add_argument("--artifact", default="all",
                    choices=["all", *pipeline.all_artifacts(), *pipeline.ALIASES])
    va.set_defaults(handler=cmd_validate)

    ss = sub.add_parser("stage-submit", help="Validate and commit one stage's layers.")
    ss.add_argument("--run", required=True)
    ss.add_argument("--job", required=True)
    ss.add_argument("--stage", required=True, type=int, choices=stages)
    ss.add_argument("--fingerprint", required=True,
                    help="The 8-character evidence fingerprint from the bundle.")
    ss.add_argument("--file", default=None,
                    help="Explicit return file (single-artifact stages only).")
    ss.add_argument("--reject", action="store_true",
                    help="Stage 3: submit a RERUN review only; publish nothing.")
    ss.add_argument("--finalize-render", action="store_true",
                    help="Stage 3: finalize and render immediately after publishing.")
    ss.set_defaults(handler=cmd_stage_submit)

    ct = sub.add_parser("context", help="Prepare one stage's input bundle.")
    ct.add_argument("--run", required=True)
    ct.add_argument("--job", required=True)
    ct.add_argument("--stage", required=True, type=int, choices=stages)
    ct.add_argument("--stats", action="store_true",
                    help="Print the size of every bundle item first.")
    ct.set_defaults(handler=cmd_context)

    cd = sub.add_parser("cards", help="Evidence cards: section text plus ceilings.")
    cd.add_argument("--run", required=True)
    cd.add_argument("--ids", default=None, help="Comma-separated EV: or source ids.")
    cd.add_argument("--search", default=None, help="Literal, case-insensitive.")
    cd.add_argument("--job", default=None)
    cd.add_argument("--stage", type=int, choices=stages, default=None)
    cd.add_argument("--full", action="store_true", help="Keep selection metadata.")
    cd.add_argument("--out", default=None)
    cd.set_defaults(handler=cmd_cards)

    pv = sub.add_parser("preview", help="Render the work in progress and measure it.")
    pv.add_argument("--run", required=True)
    pv.add_argument("--job", required=True)
    pv.add_argument("--stage", required=True, type=int, choices=stages)
    pv.add_argument("--cv-only", action="store_true")
    pv.set_defaults(handler=cmd_preview)

    asm = sub.add_parser("assemble", help="Merge the layers and show the result.")
    asm.add_argument("--run", required=True)
    asm.add_argument("--job", required=True)
    asm.add_argument("--dry-run", action="store_true",
                     help="Accepted for symmetry; assemble never writes.")
    asm.add_argument("--cv", default=None)
    asm.add_argument("--advocacy", default=None)
    asm.add_argument("--polish", default=None)
    asm.set_defaults(handler=cmd_assemble)

    rg = sub.add_parser("register", help="Cluster variation register.")
    rg.add_argument("--run", required=True)
    rg.add_argument("--cluster", default=None)
    rg.set_defaults(handler=cmd_register)

    fi = sub.add_parser("finalize", help="Assign the canonical document date.")
    fi.add_argument("--run", required=True)
    fi.add_argument("--job", required=True)
    fi.add_argument("--date", default=None)
    fi.add_argument("--reviewed-by", default="operator")
    fi.set_defaults(handler=cmd_finalize)

    rd = sub.add_parser("render", help="Render finalized jobs to DOCX and PDF.")
    rd.add_argument("--run", required=True)
    rd.add_argument("--job", default=None)
    rd.add_argument("--force", action="store_true")
    rd.add_argument("--dest", default=None)
    rd.set_defaults(handler=cmd_render)

    st = sub.add_parser("status", help="Derive the status axes and the queue.")
    st.add_argument("--run", required=True)
    st.add_argument("--json", action="store_true")
    st.set_defaults(handler=cmd_status)

    nx = sub.add_parser("next", help="Find the next job to work on.")
    nx.add_argument("--run", required=True)
    nx.add_argument("--stage", type=int, choices=stages, default=None)
    nx.add_argument("--cluster", default=None)
    nx.set_defaults(handler=cmd_next)

    return parser


def main(argv: list[str] | None = None) -> int:
    ioenc.install()
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "stage-submit" and args.stage != 3:
        if args.reject or args.finalize_render:
            parser.error("--reject and --finalize-render are Stage 3 only")
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
