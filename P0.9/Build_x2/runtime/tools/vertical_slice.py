"""Run the Contract 19 deterministic vertical slice and collect its evidence.

    operator input
    -> immutable freeze + index + job scaffolding
    -> valid strategy fixture and invalid strategy fixture
    -> valid final/review fixtures
    -> full validation and current-state derivation
    -> CV baseline merge + complete letter
    -> DOCX generation and independent verification
    -> PDF attempt and OK/degraded render state
    -> status/queue generation
    -> targeted rerender with stable date
    -> one poisoned-job partial-success variant

The evidence package records input hashes, commands, exit codes,
diagnostics, output hashes, extracted text, the render report and all three
status axes.

A green slice permits two real-job smoke testing. It proves nothing about
product quality (INV-08).

Usage:
    python -m tools.vertical_slice [--out DIR]
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

RUNTIME = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RUNTIME))

from jobbsok.hashing import sha256_file  # noqa: E402
from jobbsok.paths import Layout  # noqa: E402

BUILD = RUNTIME.parent


class Slice:
    def __init__(self, workdir: Path, out: Path) -> None:
        self.workdir = workdir
        self.out = out
        self.steps: list[dict] = []
        self.layout: Layout | None = None

    # -- helpers ---------------------------------------------------------
    def run(self, *args: str, expect: int | None = 0, note: str = "") -> dict:
        command = [
            sys.executable, "-c",
            f"import sys; sys.path.insert(0, r'{RUNTIME}'); "
            "from jobbsok.cli import main; sys.exit(main())",
            "--root", str(self.workdir), *args,
        ]
        completed = subprocess.run(
            command, capture_output=True, text=True, encoding="utf-8",
            errors="replace",
        )
        step = {
            "command": "jobbsok " + " ".join(args),
            "exit_code": completed.returncode,
            "expected_exit": expect,
            "note": note,
            "stdout": completed.stdout.strip().splitlines(),
            "stderr": completed.stderr.strip().splitlines(),
        }
        step["ok"] = expect is None or completed.returncode == expect
        self.steps.append(step)
        status = "OK " if step["ok"] else "!! "
        print(f"  {status}exit={completed.returncode:<2} jobbsok {' '.join(args)}")
        if not step["ok"]:
            print("      stdout:", completed.stdout.strip()[:400])
            print("      stderr:", completed.stderr.strip()[:400])
        return step

    def context(self, run_id: str, job_id: str, stage: int) -> dict:
        step = self.run(
            "context", "--run", run_id, "--job", job_id,
            "--stage", str(stage),
        )
        if not step["ok"]:
            raise RuntimeError(f"Could not derive Stage-{stage} context.")
        return json.loads("\n".join(step["stdout"]))

    # -- the slice -------------------------------------------------------
    def execute(self) -> bool:
        print("Preparing an isolated build root...")
        self.workdir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(BUILD / "pyproject.toml", self.workdir / "pyproject.toml")
        for tree in ("authorities", "context", "policy", "templates", "schemas"):
            shutil.copytree(BUILD / tree, self.workdir / tree, dirs_exist_ok=True)
        for empty in ("generated", "runs", "inbox/vacancies", "pilot", "evidence"):
            (self.workdir / empty).mkdir(parents=True, exist_ok=True)
        shutil.copy2(
            BUILD / "runtime" / "tests" / "fixtures" / "testetaten_radgiver.md",
            self.workdir / "inbox" / "vacancies" / "testetaten_radgiver.md",
        )
        # A second CORE job, used for the poisoned-job partial-success variant.
        shutil.copy2(
            BUILD / "runtime" / "tests" / "fixtures" / "testetaten_radgiver.md",
            self.workdir / "inbox" / "vacancies" / "annen_etat.md",
        )
        (self.workdir / "inbox" / "batch_input.csv").write_text(
            "job_id,employer,title,job_class,cluster,sequence,priority,source,"
            "unit,reference,deadline,exception_note\n"
            "testetaten_radgiver,Testetaten HF,Rådgiver økonomi og analyse,CORE,"
            "c1,1,HIGH,vacancies/testetaten_radgiver.md,Økonomiavdelingen,"
            "2026/1234,2026-09-15,\n"
            "annen_etat_analytiker,Annen Etat,Analytiker,CORE,c1,2,NORMAL,"
            "vacancies/annen_etat.md,,,,\n",
            encoding="utf-8", newline="\n",
        )
        self.layout = Layout(self.workdir)

        print("\n1. preflight")
        self.run("preflight")

        print("\n2. immutable freeze + index + job scaffolding")
        self.run("index", "build")
        freeze_step = self.run(
            "freeze", "--input", str(
                (self.workdir / "inbox" / "batch_input.csv").resolve()
            ),
            "--reviewed-by", "Vertical Slice",
        )
        run_id = next(
            (line.split(":", 1)[1].strip() for line in freeze_step["stdout"]
             if line.startswith("Frozen run:")), None,
        )
        if run_id is None:
            return False
        self.run_id = run_id
        print(f"     run_id = {run_id}")
        self.run("verify-integrity", "--run", run_id)

        print("\n3. artifact fixtures")
        from tools.make_fixtures import build as build_fixtures

        fixtures = self.workdir / "fixtures"
        build_fixtures(self.layout, run_id, fixtures)
        from jobbsok.artifacts import MECHANICAL_FIELDS

        semantic: dict[str, Path] = {}
        for artifact, filename in (
            ("strategy", "strategy.valid.json"),
            ("invalid_strategy", "strategy.invalid.json"),
            ("final_package", "final_package.json"),
            ("review", "review.json"),
        ):
            payload = json.loads((fixtures / filename).read_text(encoding="utf-8"))
            canonical = "strategy" if artifact == "invalid_strategy" else artifact
            for field in MECHANICAL_FIELDS[canonical]:
                payload.pop(field, None)
            path = fixtures / f"{artifact}.semantic.json"
            path.write_text(
                json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8", newline="\n",
            )
            semantic[artifact] = path

        print("\n4. adversarial strategy must be refused")
        stage1 = self.context(run_id, "testetaten_radgiver", 1)
        self.run("stage-submit", "--run", run_id, "--job", "testetaten_radgiver",
                 "--stage", "1", "--handoff", stage1["handoff"]["path"],
                 "--file", str(semantic["invalid_strategy"]),
                 expect=1, note="adversarial fixture: must fail with dense diagnostics")

        print("\n5. valid strategy")
        stage1 = self.context(run_id, "testetaten_radgiver", 1)
        self.run("stage-submit", "--run", run_id, "--job", "testetaten_radgiver",
                 "--stage", "1", "--handoff", stage1["handoff"]["path"],
                 "--file", str(semantic["strategy"]))

        print("\n6. stage ownership is enforced")
        stage3 = self.context(run_id, "testetaten_radgiver", 3)
        self.run("stage-submit", "--run", run_id, "--job", "testetaten_radgiver",
                 "--stage", "3", "--artifact", "strategy",
                 "--handoff", stage3["handoff"]["path"],
                 "--file", str(semantic["strategy"]), expect=2,
                 note="INV-09: Stage 3 may not write the strategy")

        print("\n6b. valid final and review are committed as one pair")
        self.run("stage-submit", "--run", run_id, "--job", "testetaten_radgiver",
                 "--stage", "3", "--handoff", stage3["handoff"]["path"],
                 "--file", str(semantic["final_package"]),
                 "--review-file", str(semantic["review"]))

        print("\n7. full validation")
        self.run("validate", "--run", run_id, "--job", "testetaten_radgiver")

        print("\n8. render before finalization must be refused")
        self.run("render", "--run", run_id, "--job", "testetaten_radgiver",
                 expect=1, note="DEC-38: the date is assigned at finalization")

        print("\n9. finalize, then render")
        self.run("finalize", "--run", run_id, "--job", "testetaten_radgiver",
                 "--date", "2026-08-23", "--reviewed-by", "Vertical Slice")
        self.run("render", "--run", run_id, "--job", "testetaten_radgiver")

        print("\n10. targeted rerender with a stable date")
        self.run("render", "--run", run_id, "--job", "testetaten_radgiver",
                 note="pure rerender: the document date must not move")

        print("\n11. poisoned-job partial-success variant")
        poisoned = json.loads(
            (fixtures / "strategy.invalid.json").read_text(encoding="utf-8")
        )
        poisoned["binding"]["job_id"] = "annen_etat_analytiker"
        target = (
            self.layout.job_dir(run_id, "annen_etat_analytiker")
            / "current" / "strategy.json"
        )
        target.write_text(json.dumps(poisoned, indent=2, ensure_ascii=False),
                          encoding="utf-8", newline="\n")
        self.run("validate", "--run", run_id, expect=1,
                 note="one poisoned job; the good job must still pass")

        print("\n12. status and queue")
        self.run(
            "status", "--run", run_id, expect=1,
            note="partial success: poisoned job is visible while healthy job remains usable",
        )
        self.run("next", "--run", run_id, "--stage", "1")
        return True

    # -- evidence --------------------------------------------------------
    def collect(self) -> dict:
        import pymupdf

        layout, run_id = self.layout, self.run_id
        run_dir = layout.run_dir(run_id)
        manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))

        status = json.loads(
            (layout.generated / "views" / run_id / "status.json").read_text(
                encoding="utf-8"
            )
        )
        report_path = (
            layout.job_dir(run_id, "testetaten_radgiver") / "current"
            / "render_report.json"
        )
        render_report = json.loads(report_path.read_text(encoding="utf-8"))

        outputs = []
        extracted: dict[str, str] = {}
        out_dir = layout.job_dir(run_id, "testetaten_radgiver") / "out"
        for path in sorted(out_dir.iterdir()):
            outputs.append({
                "name": path.name, "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            })
            if path.suffix == ".pdf":
                with pymupdf.open(path) as document:
                    text = "\n".join(p.get_text("text") for p in document)
                extracted[path.name] = text

        evidence = {
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "run_id": run_id,
            "python": sys.version.split()[0],
            "input_hashes": {
                record["path"]: record["sha256"]
                for record in _iter(manifest["frozen_inputs"])
            },
            "vacancy_hashes": {
                job["job_id"]: job["source"]["sha256"] for job in manifest["jobs"]
            },
            "steps": self.steps,
            "output_hashes": outputs,
            "render_report": render_report,
            "status_axes": [
                {
                    "job_id": job["job_id"],
                    "semantic_triage": job["semantic_triage"],
                    "production_state": job["production_state"],
                    "highest_valid_stage": job["highest_valid_stage"],
                    "semantic_final_available": job["semantic_final_available"],
                    "render_state": job["render_state"]["overall"],
                }
                for job in status["jobs"]
            ],
            "counts": status["counts"],
        }

        self.out.mkdir(parents=True, exist_ok=True)
        (self.out / "slice_evidence.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8", newline="\n",
        )
        for old in self.out.glob("extracted_*.txt"):
            old.unlink()
        for name, text in extracted.items():
            (self.out / f"extracted_{name}.txt").write_text(
                text, encoding="utf-8", newline="\n"
            )
        artifacts_dir = self.out / "artifacts"
        if artifacts_dir.exists():
            shutil.rmtree(artifacts_dir)
        artifacts_dir.mkdir()
        for path in sorted(out_dir.iterdir()):
            shutil.copy2(path, artifacts_dir / path.name)
        fixtures_dir = self.out / "fixtures"
        if fixtures_dir.exists():
            shutil.rmtree(fixtures_dir)
        shutil.copytree(self.workdir / "fixtures", fixtures_dir)
        shutil.copy2(run_dir / "manifest.json", self.out / "manifest.json")
        shutil.copy2(
            layout.generated / "views" / run_id / "queue.md", self.out / "queue.md"
        )
        return evidence


def _iter(node):
    if isinstance(node, dict):
        if {"path", "sha256", "bytes"} <= set(node):
            yield node
            return
        for value in node.values():
            yield from _iter(value)
    elif isinstance(node, list):
        for item in node:
            yield from _iter(item)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=None)
    parser.add_argument("--workdir", default=None)
    args = parser.parse_args()

    out = (
        Path(args.out) if args.out else BUILD / "evidence" / "vertical_slice"
    ).resolve()
    workdir = (Path(args.workdir) if args.workdir else out / "workspace").resolve()
    if workdir.exists():
        shutil.rmtree(workdir)

    slice_run = Slice(workdir, out)
    if not slice_run.execute():
        print("\nVERTICAL SLICE FAILED before evidence collection.")
        return 1
    evidence = slice_run.collect()

    failed = [s for s in evidence["steps"] if not s["ok"]]
    print("\n" + "=" * 66)
    print(f"steps          : {len(evidence['steps'])} ({len(failed)} unexpected)")
    print(f"outputs        : {len(evidence['output_hashes'])}")
    print(f"render overall : {evidence['render_report']['render_state']['overall']}")
    for axes in evidence["status_axes"]:
        print(f"  {axes['job_id']:24s} triage={str(axes['semantic_triage']):6s} "
              f"production={axes['production_state']:14s} "
              f"render={axes['render_state']}")
    print(f"evidence       : {out / 'slice_evidence.json'}")
    print("VERTICAL SLICE " + ("PASS" if not failed else "FAILED"))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
