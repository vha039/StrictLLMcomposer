"""Jobbsok_26 P0.9 deterministic runtime.

Governed by P0.9_FINAL_NORMATIVE_SPECIFICATION.md (FROZEN_NORMATIVE) and
its subordinate implementation contract, as amended by the explicit P0.9.3
amendment "active stages, retrieval and branch storage".

These constants describe the revision a NEW run freezes. Interpretation of an
existing run always comes from that run's own manifest revision, never from
these values.

This package makes no network requests and no model calls (Spec 17.2).
"""

X2B_REVISION = "0.9.3+x2b"
SPEC_REVISION = X2B_REVISION
SCHEMA_REVISION = X2B_REVISION
