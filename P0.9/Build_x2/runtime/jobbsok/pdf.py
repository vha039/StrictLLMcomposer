"""PDF conversion adapters and independent PDF verification.

DEC-41 governs everything here: valid CV and letter DOCX outputs are the
minimum conforming employer-document result. Automated PDF is a target, not
a semantic precondition. A conversion failure yields render DEGRADED with a
manual-export action; it never demotes a valid semantic package and never
creates a DOCX_ONLY mode.

GATE-03 on this machine: LibreOffice is not installed. Microsoft 365 Word
16 is, with the Word.Application COM ProgID registered, so `word_com` is
the default adapter. Each document gets its own one-shot invocation --
open read-only, export, close, quit -- with automation security forced to
disable macros. On timeout, only a new Word PID identified from the exact COM
instance may be terminated; an unproven or pre-existing Word process is never
targeted. No persistent daemon exists (Spec 16.2).

GATE-04: Word COM is inherently per-document, so combined per-job
invocation is not applicable to this adapter; the per-document posture is
retained.
"""

from __future__ import annotations

import ctypes
import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

from .errors import ConfigurationError

WD_EXPORT_FORMAT_PDF = 17
MSO_AUTOMATION_SECURITY_FORCE_DISABLE = 3


@dataclass
class ConversionResult:
    ok: bool
    output: Path | None = None
    command: str = ""
    tool_version: str | None = None
    exit_code: int | None = None
    diagnostics: list[str] = field(default_factory=list)

    def fail(self, message: str) -> "ConversionResult":
        self.ok = False
        self.diagnostics.append(message)
        return self


# --------------------------------------------------------------------------
# Adapters
# --------------------------------------------------------------------------

_WORD_SCRIPT = r"""
$ErrorActionPreference = 'Stop'
$src = $args[0]; $dst = $args[1]
$word = $null; $doc = $null
try {
    $wordPidsBefore = @(
        Get-Process WINWORD -ErrorAction SilentlyContinue |
            Select-Object -ExpandProperty Id
    )
    $word = New-Object -ComObject Word.Application
    Add-Type @'
using System;
using System.Runtime.InteropServices;
public static class JobbsokWindowProcess {
    [DllImport("user32.dll")]
    public static extern uint GetWindowThreadProcessId(IntPtr hWnd, out uint pid);
}
'@
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $word.AutomationSecurity = %(security)d
    $doc = $word.Documents.Open($src, [ref]$false, [ref]$true)
    # Application.Hwnd is absent on current Word builds and yields $null, which
    # would be a terminating cast error under 'Stop'. The document's own window
    # handle is available once Documents.Open succeeds, so ownership is resolved
    # here -- before the long export that a timeout would interrupt. If no handle
    # can be resolved the PID stays 0, $owned stays False, and nothing is ever
    # terminated (AR-20).
    [uint32]$wordPid = 0
    $hwnd = $null
    try { $hwnd = $doc.ActiveWindow.Hwnd } catch { $hwnd = $null }
    if ($null -eq $hwnd) {
        try { $hwnd = $word.Hwnd } catch { $hwnd = $null }
    }
    if ($null -ne $hwnd -and [int64]$hwnd -ne 0) {
        [void][JobbsokWindowProcess]::GetWindowThreadProcessId(
            [IntPtr][int64]$hwnd, [ref]$wordPid
        )
    }
    $owned = ($wordPid -gt 0 -and $wordPidsBefore -notcontains [int]$wordPid)
    [Console]::Out.WriteLine(
        "AUTOMATION_PID=" + $wordPid + ";OWNED=" + $owned
    )
    [Console]::Out.Flush()
    $doc.ExportAsFixedFormat($dst, %(format)d)
    Write-Output ("VERSION=" + $word.Version)
    $exit = 0
} catch {
    Write-Error $_.Exception.Message
    $exit = 1
} finally {
    if ($doc  -ne $null) { try { $doc.Close(0) } catch {} }
    if ($word -ne $null) { try { $word.Quit() }  catch {} }
} 
exit $exit
""" % {
    "security": MSO_AUTOMATION_SECURITY_FORCE_DISABLE,
    "format": WD_EXPORT_FORMAT_PDF,
}


def _automation_identity(output: str | bytes | None) -> tuple[int | None, bool]:
    if isinstance(output, bytes):
        output = output.decode("utf-8", errors="replace")
    match = re.search(
        r"AUTOMATION_PID=(\d+);OWNED=(True|False)", output or "",
        flags=re.IGNORECASE,
    )
    if match is None:
        return None, False
    return int(match.group(1)), match.group(2).casefold() == "true"


def _terminate_owned_word(pid: int) -> bool:
    """Terminate and await only the PID proven new by the COM invocation."""
    if os.name != "nt":
        return False
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.OpenProcess.argtypes = [ctypes.c_ulong, ctypes.c_int, ctypes.c_ulong]
    kernel32.OpenProcess.restype = ctypes.c_void_p
    kernel32.QueryFullProcessImageNameW.argtypes = [
        ctypes.c_void_p, ctypes.c_ulong, ctypes.c_wchar_p,
        ctypes.POINTER(ctypes.c_ulong),
    ]
    kernel32.QueryFullProcessImageNameW.restype = ctypes.c_int
    kernel32.TerminateProcess.argtypes = [ctypes.c_void_p, ctypes.c_uint]
    kernel32.TerminateProcess.restype = ctypes.c_int
    kernel32.WaitForSingleObject.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
    kernel32.WaitForSingleObject.restype = ctypes.c_ulong
    kernel32.CloseHandle.argtypes = [ctypes.c_void_p]

    process = kernel32.OpenProcess(0x00100001 | 0x1000, False, pid)
    if not process:
        return False
    try:
        image = ctypes.create_unicode_buffer(32768)
        size = ctypes.c_ulong(len(image))
        if not kernel32.QueryFullProcessImageNameW(process, 0, image, ctypes.byref(size)):
            return False
        if Path(image.value).name.casefold() != "winword.exe":
            return False
        if not kernel32.TerminateProcess(process, 1):
            return False
        return kernel32.WaitForSingleObject(process, 5000) == 0
    finally:
        kernel32.CloseHandle(process)


def convert_word_com(docx: Path, pdf: Path, *, timeout: int) -> ConversionResult:
    """One-shot Word COM export. No daemon; macros disabled; no broad process kill."""
    docx, pdf = Path(docx).resolve(), Path(pdf).resolve()
    powershell = shutil.which("powershell") or shutil.which("pwsh")
    if powershell is None:
        return ConversionResult(False).fail(
            "No PowerShell interpreter found for the Word COM adapter."
        )

    script = Path(tempfile.mkdtemp(prefix=".wordcom_")) / "export.ps1"
    script.write_text(_WORD_SCRIPT, encoding="utf-8")
    command = [
        powershell, "-NoProfile", "-NonInteractive",
        "-ExecutionPolicy", "Bypass",
        "-File", str(script), str(docx), str(pdf),
    ]
    result = ConversionResult(False, command=" ".join(command[-3:]))
    try:
        completed = subprocess.run(
            command, capture_output=True, text=True, timeout=timeout, check=False
        )
    except subprocess.TimeoutExpired as exc:
        pid, owned = _automation_identity(exc.stdout)
        if owned and pid is not None and _terminate_owned_word(pid):
            return result.fail(
                f"Word COM export timed out after {timeout}s for {docx.name}. "
                f"The ownership-proven Word automation process PID {pid} was "
                "terminated; pre-existing Word processes were not targeted."
            )
        return result.fail(
            f"Word COM export timed out after {timeout}s for {docx.name}. "
            "The PowerShell invocation was stopped, but termination of its "
            "Word automation process was not proven. Do not end unrelated "
            "Word processes; close only an automation document or process "
            "whose ownership you can identify."
        )
    except OSError as exc:
        return result.fail(f"Could not start the Word COM adapter: {exc}")
    finally:
        shutil.rmtree(script.parent, ignore_errors=True)

    result.exit_code = completed.returncode
    for line in (completed.stdout or "").splitlines():
        if line.startswith("VERSION="):
            result.tool_version = f"Word {line.split('=', 1)[1].strip()}"
    stderr = (completed.stderr or "").strip()
    if stderr:
        result.diagnostics.append(stderr.splitlines()[0][:400])

    if completed.returncode != 0:
        return result.fail(f"Word COM export returned exit code {completed.returncode}.")
    if not pdf.is_file() or pdf.stat().st_size == 0:
        return result.fail("Word COM reported success but produced no usable PDF.")
    result.ok = True
    result.output = pdf
    return result


def convert_libreoffice(docx: Path, pdf: Path, *, timeout: int) -> ConversionResult:
    """Headless soffice with an isolated per-invocation profile.

    Retained as an adapter because GATE-03's posture allows the converter to
    change without a specification amendment. Not installed on this machine.
    """
    docx, pdf = Path(docx).resolve(), Path(pdf).resolve()
    soffice = next(
        (shutil.which(n) for n in ("soffice", "soffice.com", "libreoffice")
         if shutil.which(n)),
        None,
    )
    if soffice is None:
        return ConversionResult(False).fail(
            "LibreOffice/soffice is not installed on this machine."
        )
    profile = Path(tempfile.mkdtemp(prefix=".lo_profile_"))
    command = [
        soffice, "--headless",
        f"-env:UserInstallation={profile.resolve().as_uri()}",
        "--convert-to", "pdf", "--outdir", str(pdf.parent), str(docx),
    ]
    result = ConversionResult(False, command=" ".join(command[:4]))
    try:
        completed = subprocess.run(
            command, capture_output=True, text=True, timeout=timeout, check=False
        )
    except subprocess.TimeoutExpired:
        return result.fail(f"LibreOffice conversion timed out after {timeout}s.")
    except OSError as exc:
        return result.fail(f"Could not start LibreOffice: {exc}")
    finally:
        shutil.rmtree(profile, ignore_errors=True)

    result.exit_code = completed.returncode
    produced = docx.with_suffix(".pdf")
    if produced != pdf and produced.is_file():
        produced.replace(pdf)
    if completed.returncode != 0 or not pdf.is_file() or pdf.stat().st_size == 0:
        details = (completed.stderr or completed.stdout or "no output").strip()
        return result.fail(f"LibreOffice conversion failed: {details[:400]}")
    result.ok = True
    result.output = pdf
    return result


def convert_none(docx: Path, pdf: Path, *, timeout: int) -> ConversionResult:
    """No automated conversion. Explicitly degraded, never a failure."""
    return ConversionResult(False, command="(no converter configured)").fail(
        "Automated PDF conversion is disabled by settings; export the PDF "
        "manually from Word."
    )


ADAPTERS = {
    "word_com": convert_word_com,
    "libreoffice": convert_libreoffice,
    "none": convert_none,
}


def convert(docx: Path, pdf: Path, *, converter: str, timeout: int) -> ConversionResult:
    if converter == "auto":
        for name in ("word_com", "libreoffice"):
            result = ADAPTERS[name](docx, pdf, timeout=timeout)
            if result.ok:
                return result
        return convert_none(docx, pdf, timeout=timeout)
    adapter = ADAPTERS.get(converter)
    if adapter is None:
        raise ConfigurationError(
            f"Unknown converter {converter!r}. Known: {sorted(ADAPTERS)}"
        )
    return adapter(docx, pdf, timeout=timeout)


MANUAL_EXPORT_ACTION = (
    "Save/export the PDF manually for human submission use. Automated status "
    "remains DEGRADED unless the configured converter later produces a verified "
    "current PDF."
)


# --------------------------------------------------------------------------
# Independent PDF verification
# --------------------------------------------------------------------------

@dataclass
class PdfChecks:
    exists: bool = False
    nonzero: bool = False
    openable: bool = False
    text_extractable: bool = False
    no_clipped_blocks: bool = False
    no_blank_page: bool = False
    page_count: int = 0
    text: str = ""
    diagnostics: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return all(
            (self.exists, self.nonzero, self.openable, self.text_extractable,
             self.no_clipped_blocks, self.no_blank_page)
        )


def verify_pdf(path: Path) -> PdfChecks:
    """Verify one produced PDF on its own terms.

    Page count is recorded but never enforced: DEC-24 makes page count an
    editorial signal, so P0.7's hard 2-page CV / 1-page letter caps are
    deliberately not reimplemented. A document fails only when it is
    unusable, corrupted or clipped.
    """
    import pymupdf

    checks = PdfChecks()
    path = Path(path)
    checks.exists = path.is_file()
    if not checks.exists:
        checks.diagnostics.append("PDF was not produced.")
        return checks
    checks.nonzero = path.stat().st_size > 0
    if not checks.nonzero:
        checks.diagnostics.append("PDF is zero bytes.")
        return checks

    try:
        with pymupdf.open(path) as document:
            checks.openable = True
            checks.page_count = document.page_count
            if document.page_count < 1:
                checks.diagnostics.append("PDF has no pages.")
                return checks
            texts: list[str] = []
            blank: list[int] = []
            clipped: list[int] = []
            for number, page in enumerate(document, start=1):
                rect = page.rect
                text = page.get_text("text") or ""
                texts.append(text)
                if len(text.strip()) < 10:
                    blank.append(number)
                for block in page.get_text("blocks"):
                    x0, y0, x1, y1 = block[:4]
                    if (x0 < -2 or y0 < -2
                            or x1 > rect.width + 2 or y1 > rect.height + 2):
                        clipped.append(number)
                        break
            checks.text = "\n".join(texts)
            checks.text_extractable = len(checks.text.strip()) >= 50
            checks.no_blank_page = not blank
            checks.no_clipped_blocks = not clipped
            if blank:
                checks.diagnostics.append(f"Blank or near-empty page(s): {blank}")
            if clipped:
                checks.diagnostics.append(
                    f"Text clipped outside the page on page(s): {clipped}"
                )
            if not checks.text_extractable:
                checks.diagnostics.append(
                    "PDF has too little selectable text to be parseable."
                )
    except Exception as exc:
        checks.diagnostics.append(f"PDF could not be read: {exc}")
    return checks
