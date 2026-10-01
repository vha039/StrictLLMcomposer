"""Deterministic hashing.

Two distinct hash kinds, deliberately not interchangeable:

* sha256_file  -- byte identity of a frozen input (authorities, vacancy
  originals, templates, policy, schemas). Spec 5.2 binds these into the
  manifest; a mismatch is a run-integrity failure.
* sha256_canonical_json -- semantic identity of a model-authored artifact.
  Used for the fixed upstream-hash comparisons behind the static staleness
  table (DEC-26). Canonical serialization means reformatting a strategy
  file does not read as a semantic change (Contract 17.1 test 3).
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

_CHUNK = 1024 * 1024


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(_CHUNK), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json_bytes(value: Any) -> bytes:
    """Stable UTF-8 serialization: sorted keys, compact, one trailing newline."""
    text = json.dumps(
        value,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
    )
    return (text + "\n").encode("utf-8")


def sha256_canonical_json(value: Any) -> str:
    return sha256_bytes(canonical_json_bytes(value))


def pretty_json_bytes(value: Any) -> bytes:
    """Human-inspectable serialization for files written to disk."""
    text = json.dumps(value, indent=2, ensure_ascii=False, sort_keys=False)
    return (text + "\n").encode("utf-8")
