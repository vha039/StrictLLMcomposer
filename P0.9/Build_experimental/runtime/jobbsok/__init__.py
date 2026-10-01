"""Jobbsok_26 P0.9 deterministic runtime.

Experimental Relay revision: four human-started stages (SCOUT, ARCHITECT,
ADVOCATE, EDITOR) writing layered artifacts that the tool assembles into
the final package. Legacy 0.9.0/0.9.3 runs are not interpreted here.

These constants describe the revision a NEW run freezes. Interpretation of an
existing run always comes from that run's own manifest revision, never from
these values.

This package makes no network requests and no model calls (Spec 17.2).
"""

SPEC_REVISION = "0.10.0-exp"
SCHEMA_REVISION = "0.10.0-exp"
