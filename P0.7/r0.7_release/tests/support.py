from __future__ import annotations

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import shutil
import sys
from typing import Any

import pymupdf


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str):
    path = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(f"p07_{name}", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


INGEST = load_script("ingest")
FINALIZE = load_script("finalize")


def make_text_pdf(path: Path, pages: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    document = pymupdf.open()
    for content in pages:
        page = document.new_page(width=595.28, height=841.89)
        result = page.insert_textbox(
            pymupdf.Rect(50, 50, 545, 792),
            content,
            fontsize=10,
            fontname="helv",
        )
        if result < 0:
            document.close()
            raise RuntimeError("Test PDF text did not fit on the page.")
    document.save(path)
    document.close()


def example_package() -> dict[str, Any]:
    return json.loads(
        (ROOT / "context" / "templates" / "EXAMPLE_FINAL_PACKAGE.json")
        .read_text(encoding="utf-8")
    )


def make_package(
    job_id: str,
    *,
    letter_required: bool,
    sparse: bool = False,
    source_stage: str = "STAGE4_FINAL",
) -> dict[str, Any]:
    package = deepcopy(example_package())
    batch_id = job_id[:3]
    package["source_stage"] = source_stage
    package["job"].update(
        {
            "job_id": job_id,
            "batch_id": batch_id,
            "macro_cluster_id": f"{batch_id}_C01_process_digitalization",
            "mini_cluster_id": f"{batch_id}_C01A_process_digitalization",
            "employer": (
                "Eksempelvirksomheten AS"
                if not sparse
                else "Norsk Driftsutvikling AS"
            ),
            "title": (
                "Seniorrådgiver prosess og analyse"
                if not sparse
                else "Rådgiver virksomhetsstyring"
            ),
            "unit": None if sparse else "Eksempelavdeling",
            "reference": None if sparse else "12345",
            "letter_required": letter_required,
        }
    )
    if sparse:
        package["cv_overrides"] = {
            "baseline_version": "0.7.0",
            "profile": (
                "Samfunnsøkonom og rådgiver med erfaring fra økonomiprosesser, "
                "styringsinformasjon og forbedringsarbeid i et komplekst "
                "sykehusmiljø. Arbeider strukturert med behov, kontroller og "
                "leveranser som skal fungere for brukerne i ordinær drift."
            ),
            "key_competencies": [
                "Virksomhetsstyring og økonomiforståelse",
                "Behovsavklaring og prosessforbedring",
                "Kvalitetssikring og dokumentasjon",
                "Power BI og Excel",
            ],
            "experience_overrides": [
                {
                    "employment_id": "EMP_OUS_ANALYSE",
                    "bullets": [
                        (
                            "Utvikler beslutningsstøtte som gjør økonomi, "
                            "aktivitet og bemanning mer tilgjengelig for ledere."
                        ),
                        (
                            "Avklarer behov og etablerer kontroller, dokumentasjon "
                            "og overlevering i tverrfaglige leveranser."
                        ),
                    ],
                }
            ],
        }
    if not letter_required:
        package["application"] = None
    package["portal_answers"] = [] if sparse else package["portal_answers"]
    return package


def identity_for_package(package: dict[str, Any]) -> dict[str, Any]:
    job = package["job"]
    return {
        field: job[field]
        for field in (
            "job_id",
            "batch_id",
            "macro_cluster_id",
            "employer",
            "title",
            "unit",
            "reference",
            "language",
            "letter_required",
        )
    }


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def review_flags_text(flag_count: int = 1) -> str:
    blocks = ["# Must verify"]
    for index in range(1, flag_count + 1):
        blocks.extend(
            [
                "",
                f"## F{index} — Formulering i CV-profil",
                "",
                "Reason: Kontroller styrkegraden mot kandidatmyndigheten.",
                "",
                "Suggested action: Behold eller juster den lokaliserte formuleringen.",
            ]
        )
    blocks.extend(["", "# Strong but defensible", "", "# Optional polish"])
    return "\n".join(blocks).rstrip() + "\n"


def write_stage4_fixture(
    input_root: Path,
    source_root: Path,
    package: dict[str, Any],
    *,
    flag_count: int = 1,
    final_package: bool = True,
    done: bool = True,
    input_blocked: bool = False,
    output_blocked: bool = False,
    input_identity: dict[str, Any] | None = None,
    output_identity: dict[str, Any] | None = None,
) -> tuple[Path, Path]:
    mini = package["job"]["mini_cluster_id"]
    job_id = package["job"]["job_id"]
    expected_dir = input_root / mini / job_id
    output_dir = source_root / mini / job_id
    expected_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    identity = identity_for_package(package)
    write_json(expected_dir / "job_identity.json", input_identity or identity)
    write_json(output_dir / "job_identity.json", output_identity or identity)
    if input_blocked:
        (expected_dir / "BLOCKED.md").write_text(
            "# BLOCKED\n\nStage: 4\nJob: " + job_id + "\n",
            encoding="utf-8",
        )
    if output_blocked:
        (output_dir / "BLOCKED.md").write_text(
            "# BLOCKED\n\nStage: 4\nJob: " + job_id + "\n",
            encoding="utf-8",
        )

    draft = deepcopy(package)
    draft["source_stage"] = "STAGE3_DRAFT"
    write_json(output_dir / "draft_package.json", draft)
    if final_package:
        final = deepcopy(package)
        final["source_stage"] = "STAGE4_FINAL"
        write_json(output_dir / "final_package.json", final)
    (output_dir / "review_flags.md").write_text(
        review_flags_text(flag_count),
        encoding="utf-8",
    )
    if done:
        (output_dir / "_DONE.md").write_text(
            "\n".join(
                [
                    "Stage: 4",
                    "Status: COMPLETED",
                    "Artifact: final_package.json; review_flags.md; job_identity.json",
                    f"Job: {job_id}",
                    "Model: GPT-5.6 Sol",
                    "Effort: xhigh",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    return expected_dir, output_dir


def make_project_root(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ROOT / "context", path / "context")
    for relative in (
        "stg1_analyze/input",
        "stg1_analyze/output",
        "stg2_strategy/input",
        "stg2_strategy/output",
        "stg3_write/input",
        "stg3_write/output",
        "stg4_mirror/input",
        "stg4_mirror/output",
    ):
        (path / relative).mkdir(parents=True, exist_ok=True)
    return path


def locate_soffice() -> str | None:
    for candidate in (
        shutil.which("soffice"),
        shutil.which("soffice.com"),
        "/opt/codex/runtimes/codex-primary-runtime/dependencies/bin/override/soffice",
    ):
        if candidate and Path(candidate).is_file():
            return str(candidate)
    return None
