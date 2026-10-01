"""UTF-8 I/O harness.

GATE-07 finding on the target machine: the default console encoding is
cp1252, and printing Norwegian text (Radgiver Okonomi, ae/o/aa) raises
UnicodeEncodeError. Every entry point calls install() before producing
output, so diagnostics containing candidate or employer text never crash
the command that was supposed to report a problem.
"""

from __future__ import annotations

import sys


def install() -> None:
    """Force UTF-8 on stdout/stderr. Safe to call more than once."""
    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (ValueError, OSError):  # detached or already-closed stream
                pass
