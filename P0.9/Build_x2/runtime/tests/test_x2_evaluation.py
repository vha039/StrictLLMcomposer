import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "evaluation"))
from make_pairs import copy_pair


def test_blinding_copies_exact_package_bytes_and_keeps_key_separate(tmp_path):
    stable = tmp_path / "stable"
    x2 = tmp_path / "x2"
    stable.mkdir()
    x2.mkdir()
    for arm, root in (("stable", stable), ("x2", x2)):
        for label in ("CV", "Soknad"):
            for suffix in (".docx", ".pdf"):
                (root / f"{label}_sample{suffix}").write_bytes(f"{arm}-{label}-{suffix}".encode())
    pair = tmp_path / "blind" / "pair1"
    key = tmp_path / "keys" / "pair1.json"
    copy_pair(stable, x2, pair, key, "x2")
    assert json.loads(key.read_text()) == {"A": "x2", "B": "stable"}
    assert (pair / "A/CV.pdf").read_bytes() == (x2 / "CV_sample.pdf").read_bytes()
    assert (pair / "B/Letter.docx").read_bytes() == (stable / "Soknad_sample.docx").read_bytes()
    assert not (pair / "pair1.json").exists()
