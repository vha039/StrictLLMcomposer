"""The render transaction: DOCX generation, verification and promotion.

DEC-21 fixes the ten steps and makes one job the render transaction with
each document result independently verified. DEC-41 makes both valid DOCX
files the minimum conforming result and a failed PDF a DEGRADED render
state rather than a semantic failure. DEC-38 makes the document date
canonical at semantic finalization and preserved by a pure rerender.
ACC-17 forbids silently overwriting a human-edited deliverable.

Everything the renderer needs to know about which content goes into which
control comes from one canonical template map (Contract 13.3). Code,
documentation and tests read that same file.
"""

from __future__ import annotations

import errno
import os
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import merge as merge_module
from . import pdf as pdf_module
from .atomicio import Promotion, TransactionDir, promote_file
from .docxfill import (
    assert_no_controls,
    fill_block,
    fill_inline,
    normalized,
    read_document,
    require_template_contract,
    visible_text,
    write_filled_docx,
)
from .errors import ConfigurationError, JobError, ValidationResult
from .hashing import sha256_canonical_json, sha256_file
from .leakage import scan
from .paths import (
    MAX_PATH_CHARS,
    Layout,
    assert_writable,
    safe_filename_component,
)
from .schemas import validate_against_schema

NORWEGIAN_MONTHS = {
    1: "januar", 2: "februar", 3: "mars", 4: "april", 5: "mai", 6: "juni",
    7: "juli", 8: "august", 9: "september", 10: "oktober", 11: "november",
    12: "desember",
}

_SUBSTITUTION = re.compile(r"\{([a-z_]+(?:\[[A-Z0-9_]+\])?(?:\.[a-z_]+)?)(\|[a-z_]+)?\}")


def norwegian_long_date(iso_date: str) -> str:
    parsed = datetime.strptime(iso_date, "%Y-%m-%d").date()
    return f"{parsed.day}. {NORWEGIAN_MONTHS[parsed.month]} {parsed.year}"


# --------------------------------------------------------------------------
# Template-map expression resolution
# --------------------------------------------------------------------------

def _transform(value: str, name: str | None) -> str:
    if name in (None, ""):
        return value
    if name == "upper":
        return value.upper()
    raise ConfigurationError(f"Unknown transform {name!r} in the template map.")


def resolve_substitutions(
    template: str, effective: dict[str, Any], job: dict[str, Any]
) -> str:
    """Expand {path} / {path|transform} against the baseline and job."""

    def lookup(match: re.Match[str]) -> str:
        path, transform = match.group(1), (match.group(2) or "")[1:]
        value = ""
        if path.startswith("candidate."):
            value = str(effective["candidate"].get(path.split(".", 1)[1], "") or "")
        elif path.startswith("job."):
            value = str(job.get(path.split(".", 1)[1], "") or "")
        elif path.startswith("employment["):
            key, attribute = re.match(r"employment\[([^\]]+)\]\.(\w+)", path).groups()
            entry = merge_module.employment(effective, key)
            value = str((entry or {}).get(attribute, "") or "")
        elif path.startswith("education["):
            key, attribute = re.match(r"education\[([^\]]+)\]\.(\w+)", path).groups()
            entry = merge_module.education(effective, key)
            value = str((entry or {}).get(attribute, "") or "")
        return _transform(value, transform)

    return _SUBSTITUTION.sub(lookup, template)


def resolve_control(
    spec: dict[str, Any],
    *,
    effective: dict[str, Any],
    package: dict[str, Any],
    job: dict[str, Any],
    document_date: str | None,
    fixed_ids: set[str],
) -> list[tuple[int, str]] | str:
    """Turn one template-map control spec into fill input."""
    source = spec["source"]
    kind = spec["kind"]
    heading = spec.get("heading")
    prefix = spec.get("prefix", "")
    transform = spec.get("transform")

    def block(items: list[str], *, heading_text: str | None = None) -> list[tuple[int, str]]:
        if not items:
            return []
        if heading_text:
            return [(0, heading_text)] + [(1, item) for item in items]
        return [(0, item) for item in items]

    if source == "none":
        return "" if kind == "inline" else []

    if source.startswith("literal:"):
        value = source.split(":", 1)[1]
        return value if kind == "inline" else block([value])

    if source == "document_date":
        if not document_date:
            raise JobError(
                "No canonical document date. Run 'jobbsok finalize' before "
                "rendering; the date is assigned at semantic finalization and "
                "is never computed at render time (DEC-38)."
            )
        value = (
            norwegian_long_date(document_date)
            if transform == "norwegian_long_date"
            else document_date
        )
        return value if kind == "inline" else block([value])

    if source.startswith("job."):
        value = job.get(source.split(".", 1)[1]) or ""
        value = f"{prefix}{value}" if value else ""
        return value if kind == "inline" else block([value] if value else [])

    if source == "package.cv.headline":
        return block([_transform(effective["headline"], transform)])
    if source == "package.cv.profile":
        return block([effective["profile"]])
    if source == "package.cv.competencies":
        items = effective["competencies"]
        if transform == "join_middot":
            return block([prefix + " · ".join(items)] if items else [])
        return block(items)
    if source == "package.letter.paragraphs":
        letter = package["letter"]
        paragraphs = [
            letter["opening"], *letter["body_paragraphs"], letter["closing"]
        ]
        return block(paragraphs)

    if source.startswith("effective.employment["):
        key = re.match(r"effective\.employment\[([^\]]+)\]\.bullets", source).group(1)
        entry = merge_module.employment(effective, key)
        if entry is None:
            raise ConfigurationError(
                f"Template map references unknown employment {key!r}."
            )
        return block(entry["bullets"])

    if source == "effective.previous_employments":
        lines = []
        for entry in merge_module.previous_employments(effective, fixed_ids):
            unit = f", {entry['unit']}" if entry.get("unit") else ""
            summary = " • ".join(entry["bullets"])
            line = (
                f"{entry['period']}  |  {entry['formal_title']}, "
                f"{entry['employer']}{unit}"
            )
            lines.append(f"{line}. {summary}" if summary else line)
        return block(lines, heading_text=heading)

    if source.startswith("baseline.education["):
        key = re.match(r"baseline\.education\[([^\]]+)\]\.details", source).group(1)
        entry = merge_module.education(effective, key)
        return block(list((entry or {}).get("details") or []))

    if source.startswith("baseline.sections["):
        key = re.match(r"baseline\.sections\[([^\]]+)\]", source).group(1)
        section = effective["sections"].get(key)
        if not section or not section["items"]:
            return []
        return block(section["items"], heading_text=section["heading"].upper())

    if source == "baseline.languages":
        items = [f"{item['language']}: {item['level']}" for item in effective["languages"]]
        return block(items, heading_text=heading)

    if source == "baseline.languages_and_courses":
        languages = [f"{item['language']}: {item['level']}" for item in effective["languages"]]
        courses = list((effective["sections"].get("OTHER_COURSES") or {}).get("items") or [])
        return block(languages + courses, heading_text=heading)

    if source == "baseline.references_text":
        text = effective["references_text"]
        return block([text] if text else [], heading_text=heading)

    raise ConfigurationError(f"Unknown template-map source {source!r}.")


# --------------------------------------------------------------------------
# Preflight
# --------------------------------------------------------------------------

def preflight_templates(
    layout: Layout, template_map: dict[str, Any], effective: dict[str, Any] | None = None
) -> ValidationResult:
    """Control contract plus static baseline furniture (Spec 16.3, 4.2)."""
    result = ValidationResult()
    for name, spec in template_map["documents"].items():
        master = layout.root / spec["master"]
        expected = {tag: c["count"] for tag, c in spec["controls"].items()}
        try:
            require_template_contract(master, expected)
        except ConfigurationError as exc:
            result.add("DEC-30", spec["master"], "controls",
                       "the exact control contract in the template map", str(exc))
            continue

        if effective is None:
            continue
        text = normalized(visible_text(master)).casefold()
        for assertion in spec.get("static_baseline_assertions", []):
            expected_text = normalized(
                resolve_substitutions(assertion, effective, {})
            ).casefold()
            if expected_text and expected_text not in text:
                result.add(
                    "DEC-23", spec["master"], "static furniture",
                    f"the master to contain {expected_text!r} from the baseline",
                    "not found. The master's static furniture disagrees with "
                    "CV_BASELINE. Resolve through human-approved source/baseline "
                    "maintenance; a model stage must never correct a "
                    "baseline-owned static fact through a dynamic field.",
                )
    return result


# --------------------------------------------------------------------------
# Render transaction
# --------------------------------------------------------------------------

@dataclass
class DocumentOutcome:
    component: str
    format: str
    state: str = "NOT_ATTEMPTED"
    output_path: str | None = None
    output_sha256: str | None = None
    bytes: int | None = None
    promotion: str | None = None
    command: str | None = None
    tool_version: str | None = None
    exit_code: int | None = None
    diagnostics: list[str] = field(default_factory=list)
    page_count: int | None = None
    checks: dict[str, bool] = field(default_factory=dict)
    limitation: str | None = None
    human_action: str | None = None
    warnings: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "component": self.component,
            "format": self.format,
            "state": self.state,
            "output_path": self.output_path,
            "output_sha256": self.output_sha256,
            "bytes": self.bytes,
            "promotion": self.promotion,
            "command": self.command,
            "tool_version": self.tool_version,
            "exit_code": self.exit_code,
            "diagnostics": self.diagnostics,
            "page_count": self.page_count,
            "checks": self.checks,
            "limitation": self.limitation,
            "human_action": self.human_action,
            "warnings": self.warnings,
        }


def _page_target_warning(
    component: str,
    page_count: int | None,
    render_settings: dict[str, Any],
) -> str | None:
    target = render_settings.get("soft_warnings", {}).get(
        f"{component}_expected_max_pages"
    )
    if page_count is None or target is None or page_count <= target:
        return None
    label = "CV" if component == "cv" else "Letter"
    return (
        f"{label} rendered to {page_count} pages; editorial target is "
        f"<={target}. Review signal only."
    )


def verify_receipt(
    layout: Layout,
    context: Any,
    job: dict[str, Any],
    package: dict[str, Any],
    report: dict[str, Any],
) -> ValidationResult:
    """Prove a render receipt against current inputs and actual output bytes."""
    from .artifacts import artifact_hash

    result = ValidationResult()
    validate_against_schema(
        report, context.schemas_dir, "render_report",
        file_label="render_report.json", result=result,
    )
    binding = report.get("binding") or {}
    frozen = context.manifest["frozen_inputs"]
    finalization = package.get("finalization") or {}
    expected = {
        "run_id": context.run_id,
        "job_id": job["job_id"],
        "final_package_sha256": artifact_hash(package),
        "document_date": finalization.get("document_date"),
        "baseline_map_sha256": frozen["baseline_map"]["sha256"],
        "cv_master_sha256": frozen["templates"]["cv_master"]["sha256"],
        "letter_master_sha256": frozen["templates"]["letter_master"]["sha256"],
        "template_map_sha256": frozen["template_map"]["sha256"],
    }
    for field, value in expected.items():
        if binding.get(field) != value:
            result.add(
                "DEC-21", "render_report.json", f"binding.{field}",
                repr(value), repr(binding.get(field)),
            )
    configured = context.assets.settings["render"]
    recorded_config = binding.get("render_config") or {}
    for field in ("converter", "invocation_granularity"):
        if recorded_config.get(field) != configured.get(field):
            result.add(
                "DEC-21", "render_report.json", f"binding.render_config.{field}",
                repr(configured.get(field)), repr(recorded_config.get(field)),
            )

    template_map = context.assets.json("template_map")
    # Re-derive the canonical paths through the single producer. Rebuilding the
    # filename here by hand would disagree with a length-compacted render and
    # report a good receipt as not-current.
    canonical_paths = render_output_paths(
        template_map, job,
        layout.job_dir(context.run_id, job["job_id"]) / "out",
    )
    documents = report.get("documents") or []
    by_key: dict[tuple[str, str], dict[str, Any]] = {}
    for document in documents:
        key = (document.get("component"), document.get("format"))
        if key in by_key:
            result.add(
                "DEC-21", "render_report.json", "documents",
                "one receipt row per component/format", f"duplicate {key}",
            )
        by_key[key] = document

    expected_keys = {
        (component, extension)
        for component in template_map["documents"]
        for extension in ("docx", "pdf")
    }
    if set(by_key) != expected_keys:
        result.add(
            "DEC-21", "render_report.json", "documents",
            repr(sorted(map(str, expected_keys))), repr(sorted(map(str, by_key))),
        )

    states: dict[tuple[str, str], str | None] = {}
    for key in expected_keys:
        document = by_key.get(key) or {}
        state = document.get("state")
        states[key] = state
        if state != "OK":
            continue
        expected_path = canonical_paths[key]
        recorded_path = document.get("output_path")
        if not recorded_path or Path(recorded_path).resolve(strict=False) != expected_path.resolve(strict=False):
            result.add(
                "DEC-21", "render_report.json", f"documents[{key}].output_path",
                str(expected_path), repr(recorded_path),
            )
            continue
        try:
            if not expected_path.is_file():
                result.add(
                    "DEC-21", str(expected_path), "-", "current output present", "missing",
                )
                continue
            actual_hash = sha256_file(expected_path)
            actual_bytes = expected_path.stat().st_size
        except OSError as exc:
            observed = (
                "current output is open or locked"
                if is_lock_error(exc) else
                "could not read current output"
            )
            result.add(
                "DEC-21", str(expected_path), "-",
                "current output readable for hash and size verification",
                f"{observed}: {type(exc).__name__}: {exc}",
            )
            continue
        if document.get("output_sha256") != actual_hash:
            result.add(
                "DEC-21", str(expected_path), "sha256", actual_hash,
                repr(document.get("output_sha256")),
            )
        if document.get("bytes") != actual_bytes:
            result.add(
                "DEC-21", str(expected_path), "bytes", str(actual_bytes),
                repr(document.get("bytes")),
            )

    docx_states = [states.get((component, "docx")) for component in template_map["documents"]]
    pdf_states = [states.get((component, "pdf")) for component in template_map["documents"]]
    actual_overall = (
        "FAILED" if any(state != "OK" for state in docx_states)
        else "OK" if all(state == "OK" for state in pdf_states)
        else "DEGRADED"
    )
    if (report.get("render_state") or {}).get("overall") != actual_overall:
        result.add(
            "DEC-21", "render_report.json", "render_state.overall",
            actual_overall, repr((report.get("render_state") or {}).get("overall")),
        )
    return result


def previous_output_hashes(previous_report: dict[str, Any] | None) -> dict[str, str]:
    """What this pipeline last wrote, keyed by output filename."""
    if not previous_report:
        return {}
    mapping: dict[str, str] = {}
    for document in previous_report.get("documents", []):
        path, digest = document.get("output_path"), document.get("output_sha256")
        if path and digest:
            mapping[Path(path).name] = digest
    return mapping


#: The staging directory TransactionDir allocates under the render destination.
#: Passed to TransactionDir below so the budget and the real segment cannot drift.
RENDER_STAGING_PREFIX = "rnd"

#: Characters a staged file sits below its destination: separator, ".", prefix,
#: ".", eight hex from secrets.token_hex(4), separator.
_STAGING_OVERHEAD = 1 + 1 + len(RENDER_STAGING_PREFIX) + 1 + 8 + 1

#: Smallest employer prefix a compacted name must still carry to stay readable.
MIN_EMPLOYER_PREFIX_CHARS = 8

#: Length of the identity digest appended to a compacted name.
_IDENTITY_DIGEST_CHARS = 8


def _identity_digest(job: dict[str, Any]) -> str:
    """A stable short digest of the complete, untruncated job identity.

    Truncating the employer/title suffix can make two jobs share a prefix, so
    the digest is what keeps their filenames distinct. It is taken over the
    original strings rather than the ASCII-folded components, so employers that
    fold together still separate.
    """
    return sha256_canonical_json({
        "job_id": job["job_id"],
        "employer": job["employer"],
        "title": job["title"],
    })[:_IDENTITY_DIGEST_CHARS]


def render_output_paths(
    template_map: dict[str, Any],
    job: dict[str, Any],
    destination: Path,
) -> dict[tuple[str, str], Path]:
    """The output paths for one job at one destination, length-budgeted.

    The render transaction stages under `destination/.rnd.<8 hex>/`, so Word
    opens the staged file one directory deeper than the file the human later
    opens. Word COM is bound by Windows MAX_PATH where Python is not: a staged
    path past the limit makes Documents.Open return null and the PDF step fails
    while the DOCX succeeds. So the budget is computed against the *staged*
    path, which covers the promoted path too because it is the longer of the
    two by exactly one staging segment.

    A filename is preserved byte-for-byte whenever it fits. Only when it does
    not is the employer/title suffix truncated and an identity digest appended.
    This is the single producer of output names: render_job stages and promotes
    through it, verify_receipt re-derives the expected canonical paths through
    it, and the CLI's rollback snapshot lists them through it.
    """
    destination = Path(destination)
    suffix = (
        f"{safe_filename_component(job['employer'])}_"
        f"{safe_filename_component(job['title'])}"
    )
    variants = [
        (component, extension, spec["output_stem"])
        for component, spec in template_map["documents"].items()
        for extension in ("docx", "pdf")
    ]
    # Widest fixed part of any of the four names: stem + "_" + "." + extension.
    frame = max(len(stem) + len(extension) + 2 for _, extension, stem in variants)
    budget = (
        MAX_PATH_CHARS
        - len(str(destination.resolve(strict=False)))
        - _STAGING_OVERHEAD
    )

    if len(suffix) <= budget - frame:
        chosen = suffix
    else:
        room = budget - frame - 1 - _IDENTITY_DIGEST_CHARS
        if room < MIN_EMPLOYER_PREFIX_CHARS:
            minimum = frame + MIN_EMPLOYER_PREFIX_CHARS + 1 + _IDENTITY_DIGEST_CHARS
            raise ConfigurationError(
                "Render destination is too deep to hold a usable output name.\n"
                f"          destination: {destination} "
                f"({len(str(destination.resolve(strict=False)))} characters)\n"
                f"          room for a filename: {budget}, minimum needed: {minimum}\n"
                f"          The budget is {MAX_PATH_CHARS} characters minus the "
                f"destination minus the {_STAGING_OVERHEAD}-character staging "
                "segment, so that Word can open both the staged and the promoted "
                "file. Render to a shorter --dest, or move the run root."
            )
        chosen = f"{suffix[:room].rstrip('_')}_{_identity_digest(job)}"

    return {
        (component, extension): destination / f"{stem}_{chosen}.{extension}"
        for component, extension, stem in variants
    }


_SHARED_RENDER_ERRNOS = {
    value for value in (
        errno.ENOSPC,
        getattr(errno, "EDQUOT", None),
        errno.EROFS,
        errno.EMFILE,
        errno.ENFILE,
    ) if value is not None
}


def is_lock_error(exc: BaseException) -> bool:
    """Whether an OSError is an operating-system sharing/permission lock.

    Only these justify the operator-facing "close the open document" advice;
    every other OSError (EIO, missing path, ACL failure) must not be reported
    as an open document.
    """
    return isinstance(exc, OSError) and (
        exc.errno in (errno.EACCES, errno.EPERM)
        or getattr(exc, "winerror", None) in (5, 32)
    )


def is_shared_render_failure(exc: BaseException) -> bool:
    """Whether continuing other jobs on this process/volume is untrustworthy."""
    seen: set[int] = set()
    current: BaseException | None = exc
    while current is not None and id(current) not in seen:
        seen.add(id(current))
        if isinstance(current, MemoryError):
            return True
        if isinstance(current, OSError) and current.errno in _SHARED_RENDER_ERRNOS:
            return True
        current = current.__cause__ or current.__context__
    return False


def render_job(
    layout: Layout,
    *,
    assets: Any | None = None,
    manifest: dict[str, Any],
    job: dict[str, Any],
    package: dict[str, Any],
    baseline_map: dict[str, Any],
    template_map: dict[str, Any],
    render_settings: dict[str, Any],
    previous_report: dict[str, Any] | None = None,
    force: bool = False,
    destination: Path | None = None,
) -> dict[str, Any]:
    """Render one job as a transaction. Never raises for a PDF failure."""
    run_id = manifest["run_id"]
    job_id = job["job_id"]
    finalization = package.get("finalization") or {}
    document_date = finalization.get("document_date")
    if finalization.get("state") != "FINALIZED" or not document_date:
        raise JobError(
            f"Job {job_id} is not finalized. The employer-facing document date "
            "becomes canonical at semantic finalization, not at render time "
            "(DEC-38). Run: jobbsok finalize --run "
            f"{run_id} --job {job_id}"
        )

    masters: dict[str, Path] = {}
    for component, spec in template_map["documents"].items():
        master = (
            assets.template_path(spec["master"])
            if assets is not None else layout.root / spec["master"]
        )
        if assets is not None:
            record = next(
                record
                for record in manifest["frozen_inputs"]["templates"].values()
                if record["path"] == Path(spec["master"]).as_posix()
            )
            if not master.is_file() or sha256_file(master) != record["sha256"]:
                raise ConfigurationError(
                    f"Frozen {component} master changed before point-of-use fill."
                )
        require_template_contract(
            master, {tag: item["count"] for tag, item in spec["controls"].items()}
        )
        masters[component] = master

    effective = merge_module.effective_cv(baseline_map, package)
    out_dir = Path(destination) if destination else layout.job_dir(run_id, job_id) / "out"
    if destination is None:
        assert_writable(layout, out_dir, label="canonical render destination")
    out_dir.mkdir(parents=True, exist_ok=True)
    previous = previous_output_hashes(previous_report)

    outcomes: list[DocumentOutcome] = []
    staged_paths: dict[tuple[str, str], Path] = {}
    targets = render_output_paths(template_map, job, out_dir)
    export_mode = destination is not None

    # Stage beside the destination, not in %TEMP%: that keeps the promotion
    # rename on one volume (also in --dest export mode) and lets the staged
    # files inherit the destination's access policy, so a promoted deliverable
    # stays readable by the human when the rendering identity differs from the
    # reading identity (ISS-13, DEC-21 step 6).
    with TransactionDir(
        out_dir, prefix=RENDER_STAGING_PREFIX, inherit_parent_permissions=True
    ) as workspace:
        for component, spec in template_map["documents"].items():
            filename = targets[(component, "docx")].name
            staged = workspace / filename
            docx_outcome = DocumentOutcome(component, "docx")

            try:
                _build_document(
                    layout, spec, staged, master=masters[component],
                    effective=effective, package=package, job=job,
                    document_date=document_date,
                )
                docx_outcome.checks = _verify_docx(
                    staged, spec, effective=effective, package=package, job=job
                )
                failures = [k for k, v in docx_outcome.checks.items() if v is False]
                if failures:
                    docx_outcome.state = "FAILED"
                    docx_outcome.diagnostics.append(
                        f"DOCX verification failed: {failures}"
                    )
                else:
                    docx_outcome.state = "OK"
            except ConfigurationError:
                raise
            except Exception as exc:
                if is_shared_render_failure(exc):
                    raise ConfigurationError(
                        f"Shared render resource failure while building {job_id}: "
                        f"{type(exc).__name__}: {exc}"
                    ) from exc
                docx_outcome.state = "FAILED"
                docx_outcome.diagnostics.append(
                    f"{type(exc).__name__}: {exc}"
                )

            pdf_outcome = DocumentOutcome(component, "pdf")
            if docx_outcome.state == "OK":
                staged_pdf = staged.with_suffix(".pdf")
                conversion = pdf_module.convert(
                    staged, staged_pdf,
                    converter=render_settings["converter"],
                    timeout=render_settings["converter_timeout_seconds"],
                )
                pdf_outcome.command = conversion.command
                pdf_outcome.tool_version = conversion.tool_version
                pdf_outcome.exit_code = conversion.exit_code
                pdf_outcome.diagnostics = list(conversion.diagnostics)
                if conversion.ok:
                    checks = pdf_module.verify_pdf(staged_pdf)
                    pdf_outcome.page_count = checks.page_count
                    warning = _page_target_warning(
                        component, pdf_outcome.page_count, render_settings
                    )
                    if warning:
                        pdf_outcome.warnings.append(warning)
                    pdf_outcome.checks = {
                        "exists": checks.exists, "nonzero": checks.nonzero,
                        "openable": checks.openable,
                        "text_extractable": checks.text_extractable,
                        "no_clipped_blocks": checks.no_clipped_blocks,
                        "no_blank_page": checks.no_blank_page,
                    }
                    pdf_outcome.diagnostics += checks.diagnostics
                    leak = scan(checks.text, file_label=staged_pdf.name,
                                location="extracted text")
                    pdf_outcome.checks["no_private_token"] = leak.ok
                    if not leak.ok:
                        pdf_outcome.diagnostics += [v.observed for v in leak.errors]
                    pdf_outcome.state = "OK" if (checks.ok and leak.ok) else "DEGRADED"
                else:
                    pdf_outcome.state = "DEGRADED"
                # DEC-41: a PDF problem is never a semantic failure.
                if pdf_outcome.state != "OK":
                    pdf_outcome.limitation = (
                        "Automated PDF conversion did not produce a verified PDF. "
                        "The DOCX is valid and the semantic package is unaffected."
                    )
                    pdf_outcome.human_action = pdf_module.MANUAL_EXPORT_ACTION

            outcomes.append(docx_outcome)
            outcomes.append(pdf_outcome)
            staged_paths[(component, "docx")] = staged
            staged_paths[(component, "pdf")] = staged.with_suffix(".pdf")

        by_key = {(o.component, o.format): o for o in outcomes}

        def keep_prior(outcome: DocumentOutcome, target: Path) -> None:
            digest = previous.get(target.name)
            if digest:
                outcome.output_path = str(target)
                outcome.output_sha256 = digest
                if target.is_file() and sha256_file(target) == digest:
                    outcome.bytes = target.stat().st_size

        docx_outcomes = [by_key[(component, "docx")] for component in masters]
        ready = all(outcome.state == "OK" for outcome in docx_outcomes)
        foreign: list[tuple[DocumentOutcome, Path]] = []
        if ready and not force and not export_mode:
            for outcome in docx_outcomes:
                staged = staged_paths[(outcome.component, "docx")]
                target = out_dir / staged.name
                expected = previous.get(target.name)
                if target.is_file() and (
                    expected is None or sha256_file(target) != expected
                ):
                    foreign.append((outcome, target))

        if not ready or foreign:
            foreign_targets = {target for _, target in foreign}
            for outcome in outcomes:
                target = out_dir / staged_paths[(outcome.component, outcome.format)].name
                keep_prior(outcome, target)
                if target in foreign_targets and outcome.format == "docx":
                    outcome.promotion = Promotion.REFUSED_FOREIGN.value
                    outcome.state = "FAILED"
                    outcome.human_action = (
                        "The existing DOCX differs from the last pipeline-owned "
                        "hash and was preserved. Use --force to overwrite it or "
                        "--dest <new-directory> for a non-authoritative export."
                    )
                elif outcome.state == "OK":
                    outcome.state = "FAILED" if outcome.format == "docx" else "DEGRADED"
                    outcome.diagnostics.append(
                        "The complete DOCX generation was not promotable, so no "
                        "new sibling output was advanced."
                    )
        else:
            for outcome in docx_outcomes:
                staged = staged_paths[(outcome.component, "docx")]
                target = targets[(outcome.component, "docx")]
                if export_mode:
                    existed = target.exists()
                    target.parent.mkdir(parents=True, exist_ok=True)
                    os.replace(staged, target)
                    promotion_outcome = (
                        Promotion.REPLACED if existed else Promotion.CREATED
                    )
                    promotion_destination = target
                    promotion_note = ""
                else:
                    promotion = promote_file(
                        staged, target,
                        expected_sha256=previous.get(staged.name),
                        force=force, alternate_destination=None,
                    )
                    promotion_outcome = promotion.outcome
                    promotion_destination = promotion.destination
                    promotion_note = promotion.note
                outcome.promotion = promotion_outcome.value
                if promotion_outcome is Promotion.REFUSED_FOREIGN:
                    outcome.state = "FAILED"
                    outcome.diagnostics.append(promotion_note)
                    keep_prior(outcome, promotion_destination)
                else:
                    outcome.output_path = str(promotion_destination)
                    outcome.output_sha256 = sha256_file(promotion_destination)
                    outcome.bytes = promotion_destination.stat().st_size

            docx_promoted = all(outcome.state == "OK" for outcome in docx_outcomes)
            for component in masters:
                outcome = by_key[(component, "pdf")]
                staged = staged_paths[(component, "pdf")]
                target = out_dir / staged.name
                if not docx_promoted:
                    keep_prior(outcome, target)
                    if outcome.state == "OK":
                        outcome.state = "DEGRADED"
                    continue
                if outcome.state == "OK" and staged.is_file():
                    if export_mode:
                        existed = target.exists()
                        target.parent.mkdir(parents=True, exist_ok=True)
                        os.replace(staged, target)
                        promotion_outcome = (
                            Promotion.REPLACED if existed else Promotion.CREATED
                        )
                        promotion_destination = target
                        promotion_note = ""
                    else:
                        promotion = promote_file(
                            staged, target,
                            expected_sha256=previous.get(target.name),
                            force=force, alternate_destination=None,
                        )
                        promotion_outcome = promotion.outcome
                        promotion_destination = promotion.destination
                        promotion_note = promotion.note
                    outcome.promotion = promotion_outcome.value
                    if promotion_outcome is Promotion.REFUSED_FOREIGN:
                        outcome.state = "DEGRADED"
                        outcome.diagnostics.append(promotion_note)
                        keep_prior(outcome, target)
                    else:
                        outcome.output_path = str(promotion_destination)
                        outcome.output_sha256 = sha256_file(promotion_destination)
                        outcome.bytes = promotion_destination.stat().st_size
                elif export_mode:
                    # An explicit export replaces both DOCX files unconditionally
                    # and keeps no receipt, so a surviving sibling PDF belongs to
                    # the previous generation. Set it aside rather than leaving a
                    # mixed pair in the directory the operator submits from; it may
                    # be a manual export, so it is renamed, never deleted.
                    if target.is_file():
                        superseded = target.with_name(
                            target.stem + ".superseded" + target.suffix
                        )
                        superseded.unlink(missing_ok=True)
                        target.replace(superseded)
                        outcome.diagnostics.append(
                            "A PDF from the previous export no longer matches the "
                            f"DOCX just written; it was renamed to {superseded.name}."
                        )
                        outcome.human_action = (
                            "Export the PDF manually from the new DOCX. The "
                            f"previous-generation file is kept as {superseded.name} "
                            "and must not be submitted with the new DOCX."
                        )
                else:
                    expected = previous.get(target.name)
                    if (
                        expected and target.is_file()
                        and sha256_file(target) == expected
                    ):
                        archive = layout.job_dir(run_id, job_id) / "history" / (
                            datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ-")
                            + target.name
                        )
                        archive.parent.mkdir(parents=True, exist_ok=True)
                        target.replace(archive)

    return _build_report(
        manifest, job, package, baseline_map, template_map,
        render_settings, outcomes, document_date,
    )


def _build_document(
    layout: Layout,
    spec: dict[str, Any],
    output: Path,
    *,
    master: Path | None = None,
    effective: dict[str, Any],
    package: dict[str, Any],
    job: dict[str, Any],
    document_date: str,
) -> None:
    fixed = set((spec.get("fixed_employment_zones") or {}).values())
    fixed = {v for v in fixed if isinstance(v, str) and v.startswith("EMP_")}

    def edit(root: Any) -> None:
        for tag, control in spec["controls"].items():
            resolved = resolve_control(
                control, effective=effective, package=package, job=job,
                document_date=document_date, fixed_ids=fixed,
            )
            if control["kind"] == "inline":
                fill_inline(root, tag, resolved if isinstance(resolved, str) else "")
            else:
                fill_block(root, tag, resolved if isinstance(resolved, list) else [])

    write_filled_docx(
        master or layout.root / spec["master"], output, edit,
        title=f"{spec['output_stem']} | {effective['candidate']['full_name']} | {job['title']}",
        subject=f"Jobbsok_26 P0.9 {spec['output_stem']} for {job['employer']}",
        creator=effective["candidate"]["full_name"],
    )


def _verify_docx(
    path: Path,
    spec: dict[str, Any],
    *,
    effective: dict[str, Any],
    package: dict[str, Any],
    job: dict[str, Any],
) -> dict[str, bool]:
    """Document-specific verification, not one universal string list."""
    checks: dict[str, bool] = {}
    checks["exists"] = path.is_file()
    checks["nonzero"] = path.is_file() and path.stat().st_size > 0
    if not checks["nonzero"]:
        return checks

    root, _ = read_document(path)
    try:
        assert_no_controls(root, path.name)
        checks["no_residual_sdt"] = True
    except JobError:
        checks["no_residual_sdt"] = False
    checks["openable"] = True

    text = visible_text(path)
    folded = normalized(text).casefold()
    verification = spec.get("verification", {})

    leak = scan(text, file_label=path.name, location="document text")
    checks["no_private_token"] = leak.ok
    checks["no_placeholder"] = "{{" not in text and "}}" not in text

    def present(templates: list[str]) -> bool:
        for template in templates:
            expected = normalized(
                resolve_substitutions(template, effective, job)
            ).casefold()
            if expected and not re.search(
                rf"(?<!\w){re.escape(expected)}(?!\w)", folded
            ):
                return False
        return True

    if verification.get("identity"):
        checks["identity_present"] = present(verification["identity"])
    if verification.get("chronology_anchors"):
        checks["chronology_anchors_present"] = present(verification["chronology_anchors"])
    if verification.get("employer_addressing"):
        exact = present(verification["employer_addressing"])
        for control in spec["controls"].values():
            if control["source"] not in ("job.employer", "job.title"):
                continue
            expected = normalized(
                str(job[control["source"].split(".", 1)[1]])
            ).casefold()
            occurrences = len(re.findall(
                rf"(?<!\w){re.escape(expected)}(?!\w)", folded
            ))
            exact = exact and occurrences >= control["count"]
        checks["employer_addressing_present"] = exact
    if verification.get("headline_from") == "package.cv.headline":
        headline = normalized(effective["headline"]).casefold()
        checks["headline_present"] = (not headline) or headline in folded
    if verification.get("require_override_bullets_visible"):
        missing = []
        for override in (package.get("cv") or {}).get("employment_overrides") or []:
            for bullet in override.get("bullets") or []:
                if normalized(bullet).casefold() not in folded:
                    missing.append(override["employment_id"])
                    break
        checks["override_bullets_visible"] = not missing
    return checks


def _build_report(
    manifest: dict[str, Any],
    job: dict[str, Any],
    package: dict[str, Any],
    baseline_map: dict[str, Any],
    template_map: dict[str, Any],
    render_settings: dict[str, Any],
    outcomes: list[DocumentOutcome],
    document_date: str,
) -> dict[str, Any]:
    from .artifacts import artifact_hash
    from .manifest import read_frozen

    by_key = {(o.component, o.format): o.state for o in outcomes}
    docx_states = [by_key.get(("cv", "docx")), by_key.get(("letter", "docx"))]
    pdf_states = [by_key.get(("cv", "pdf")), by_key.get(("letter", "pdf"))]

    if any(state != "OK" for state in docx_states):
        overall = "FAILED"
    elif all(state == "OK" for state in pdf_states):
        overall = "OK"
    else:
        overall = "DEGRADED"

    frozen = manifest["frozen_inputs"]
    return {
        "artifact_role": "RENDER_REPORT",
        "binding": {
            "run_id": manifest["run_id"],
            "job_id": job["job_id"],
            "final_package_sha256": artifact_hash(package),
            "document_date": document_date,
            "baseline_map_sha256": frozen["baseline_map"]["sha256"],
            "cv_master_sha256": frozen["templates"]["cv_master"]["sha256"],
            "letter_master_sha256": frozen["templates"]["letter_master"]["sha256"],
            "template_map_sha256": frozen["template_map"]["sha256"],
            "render_config": {
                "converter": render_settings["converter"],
                "invocation_granularity": render_settings["invocation_granularity"],
                "converter_version": next(
                    (o.tool_version for o in outcomes if o.tool_version), None
                ),
            },
        },
        "render_state": {
            "cv_docx": by_key.get(("cv", "docx"), "NOT_ATTEMPTED"),
            "cv_pdf": by_key.get(("cv", "pdf"), "NOT_ATTEMPTED"),
            "letter_docx": by_key.get(("letter", "docx"), "NOT_ATTEMPTED"),
            "letter_pdf": by_key.get(("letter", "pdf"), "NOT_ATTEMPTED"),
            "overall": overall,
        },
        "documents": [o.as_dict() for o in outcomes],
        "rendered_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
