"""Copy a completed pair into blind folders; keep arm identity separately."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


def copy_pair(stable: Path, x2: Path, output: Path, arm_key: Path, first_arm: str) -> None:
    stable, x2, output, arm_key = (p.resolve() for p in (stable, x2, output, arm_key))
    if output.exists() or arm_key.exists():
        raise ValueError("Output or arm key already exists; choose fresh paths.")
    if output in arm_key.parents:
        raise ValueError("Arm key must live outside the blinded output tree.")
    mapping = {"A": first_arm, "B": "x2" if first_arm == "stable" else "stable"}
    sources = {"stable": stable, "x2": x2}
    # Validate both source sets before making an output tree.
    selected: dict[str, dict[str, Path]] = {}
    for arm, directory in sources.items():
        files = list(directory.glob("*.docx")) + list(directory.glob("*.pdf"))
        docs = [p for p in files if p.suffix.lower() == ".docx"]
        pdfs = [p for p in files if p.suffix.lower() == ".pdf"]
        if len(docs) != 2 or len(pdfs) != 2:
            raise ValueError(f"{arm}: expected exactly two DOCX and two PDF files")
        names: dict[str, Path] = {}
        for group in (docs, pdfs):
            cv = [p for p in group if p.name.casefold().startswith("cv_")]
            letter = [p for p in group if p not in cv]
            if len(cv) != 1 or len(letter) != 1:
                raise ValueError(f"{arm}: cannot identify one CV and one letter")
            for label, path in (("CV", cv[0]), ("Letter", letter[0])):
                if not path.is_file() or path.is_symlink() or path.stat().st_size == 0:
                    raise ValueError(f"{arm}: package file is missing, linked or empty: {path}")
                names[f"{label}{path.suffix.lower()}"] = path
        selected[arm] = names
    output.mkdir(parents=True)
    for blind, arm in mapping.items():
        dest = output / blind
        dest.mkdir()
        for name, path in selected[arm].items():
            shutil.copy2(path, dest / name)
    arm_key.parent.mkdir(parents=True, exist_ok=True)
    arm_key.write_text(json.dumps(mapping, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stable", type=Path, required=True, help="Stable job out/ directory")
    parser.add_argument("--x2", type=Path, required=True, help="X2 job out/ directory")
    parser.add_argument("--out", type=Path, required=True, help="New blinded pair directory")
    parser.add_argument("--arm-key", type=Path, required=True, help="Separate new key file")
    parser.add_argument("--first-arm", choices=("stable", "x2"), required=True)
    args = parser.parse_args()
    copy_pair(args.stable, args.x2, args.out, args.arm_key, args.first_arm)


if __name__ == "__main__":
    main()
