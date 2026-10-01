[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^B[0-9]{2}_C[0-9]{2}_[a-z0-9_]+$')]
    [string]$Cluster,

    [Parameter(Mandatory = $false)]
    [string]$Root = "."
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

trap {
    Write-Output "ADVANCE ERROR: $($_.Exception.Message)"
    exit 1
}

function Assert-File {
    param([string]$Path, [string]$Label)
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "Missing ${Label}: $Path"
    }
}

function Assert-NoBlocker {
    param([string]$Path, [string]$Label)
    if (Test-Path -LiteralPath (Join-Path $Path "BLOCKED.md") -PathType Leaf) {
        throw "Active BLOCKED.md prevents advance for $Label."
    }
}

function Assert-Stage2Done {
    param([string]$Path, [string]$Job)
    Assert-File -Path $Path -Label "Stage 2 _DONE.md"
    $text = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
    if ($text -notmatch '(?m)^Stage:\s*2\s*$') {
        throw "Stage 2 _DONE.md for $Job lacks 'Stage: 2'."
    }
    foreach ($required in @("Status: COMPLETED", "package_blueprint.md", $Job, "Model:", "Effort:")) {
        if ($text -notlike "*$required*") {
            throw "Stage 2 _DONE.md for $Job lacks '$required'."
        }
    }
}

function Assert-Stage2BatchStatus {
    param([string]$Path, [string]$Cluster)
    Assert-File -Path $Path -Label "Stage 2 BATCH_STATUS.md"
    $text = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
    $escapedCluster = [regex]::Escape($Cluster)
    if ($text -notmatch "(?m)^#\s+$escapedCluster\s+—\s+Stage\s+2\s*$") {
        throw "Stage 2 BATCH_STATUS.md does not identify $Cluster and Stage 2."
    }
    foreach ($required in @(
        "Model:", "Effort:", "Target jobs:", "## Wave 1",
        "## Midpoint review", "## Wave 2"
    )) {
        if ($text -notlike "*$required*") {
            throw "Stage 2 BATCH_STATUS.md for $Cluster lacks '$required'."
        }
    }
    foreach ($heading in @("Completed", "Current", "Remaining", "Blocked")) {
        $count = [regex]::Matches($text, "(?m)^###\s+$heading\s*$").Count
        if ($count -lt 2) {
            throw "Stage 2 BATCH_STATUS.md for $Cluster lacks Wave 1/2 '$heading' sections."
        }
    }
}

function Assert-JobIdentity {
    param(
        [string]$Path,
        [string]$Job,
        [string]$ExpectedBatch,
        [string]$ExpectedMacro,
        [string]$ExpectedMini
    )
    Assert-File -Path $Path -Label "job_identity.json"
    try {
        $identity = Get-Content -LiteralPath $Path -Raw -Encoding UTF8 | ConvertFrom-Json
    } catch {
        throw "Invalid job_identity.json for ${Job}: $($_.Exception.Message)"
    }
    $expectedFields = @(
        "job_id", "batch_id", "macro_cluster_id", "employer", "title",
        "unit", "reference", "language", "letter_required"
    )
    $actualFields = @($identity.PSObject.Properties.Name)
    $missing = @($expectedFields | Where-Object { $_ -notin $actualFields })
    $extra = @($actualFields | Where-Object { $_ -notin $expectedFields })
    if ($missing.Count -gt 0 -or $extra.Count -gt 0) {
        throw "job_identity.json field mismatch for $Job. Missing: $($missing -join ', '); extra: $($extra -join ', ')"
    }
    if ($identity.job_id -ne $Job) { throw "job_identity job_id mismatch for $Job." }
    if ($identity.batch_id -ne $ExpectedBatch) { throw "job_identity batch_id mismatch for $Job." }
    if ($identity.macro_cluster_id -ne $ExpectedMacro) { throw "job_identity macro_cluster_id mismatch for $Job." }
    if ($ExpectedMini -notmatch '^(B[0-9]{2}_C[0-9]{2})[AB]_([a-z0-9_]+)$') {
        throw "Cannot derive macro cluster from mini-cluster $ExpectedMini."
    }
    if ("$($Matches[1])_$($Matches[2])" -ne $ExpectedMacro) {
        throw "Mini-cluster $ExpectedMini does not map to macro-cluster $ExpectedMacro."
    }
    if ($identity.language -ne "nb-NO") { throw "job_identity language must be nb-NO for $Job." }
    if ($identity.letter_required -isnot [bool]) { throw "job_identity letter_required must be boolean for $Job." }
    foreach ($field in @("employer", "title")) {
        if ([string]::IsNullOrWhiteSpace([string]$identity.$field)) {
            throw "job_identity $field is missing for $Job."
        }
    }
}

$rootPath = (Resolve-Path -LiteralPath $Root).Path
$source = Join-Path $rootPath "stg2_strategy\output\$Cluster"
$splitPath = Join-Path $source "MINICLUSTER_SPLIT.json"
$clusterBase = Join-Path $source "CLUSTER_EVIDENCE_BASE.md"
$batchStatus = Join-Path $source "BATCH_STATUS.md"

if (-not (Test-Path -LiteralPath $source -PathType Container)) {
    throw "Stage 2 cluster does not exist: $source"
}
if ($Cluster.Length -gt 100) {
    throw "Macro-cluster ID exceeds the 100-character path contract."
}
Assert-NoBlocker -Path $source -Label $Cluster
Assert-File -Path $splitPath -Label "split file"
Assert-File -Path $clusterBase -Label "cluster evidence base"
Assert-Stage2BatchStatus -Path $batchStatus -Cluster $Cluster

try {
    $split = Get-Content -LiteralPath $splitPath -Raw -Encoding UTF8 | ConvertFrom-Json
} catch {
    throw "Invalid MINICLUSTER_SPLIT.json: $($_.Exception.Message)"
}
if ($split.macro_cluster_id -ne $Cluster) {
    throw "Split macro_cluster_id '$($split.macro_cluster_id)' differs from '$Cluster'."
}

$a = @($split.A)
$b = @($split.B)
if ($a.Count -eq 0 -or $b.Count -eq 0) {
    throw "Split A and B must both contain at least one job."
}

$allSplitJobs = @($a + $b)
$duplicates = $allSplitJobs | Group-Object | Where-Object { $_.Count -ne 1 }
if ($duplicates) {
    throw "Split contains duplicate or overlapping jobs: $($duplicates.Name -join ', ')"
}

$jobPattern = '^B[0-9]{2}_J[0-9]{3}_[a-z0-9_]+$'
$expectedBatch = $Cluster.Substring(0, 3)
foreach ($job in $allSplitJobs) {
    if ($job -notmatch $jobPattern -or $job.Length -gt 120) { throw "Invalid job ID in split: $job" }
    if (-not $job.StartsWith("$expectedBatch`_")) {
        throw "Job $job has a different batch prefix than $Cluster."
    }
}

$sourceJobs = @(
    Get-ChildItem -LiteralPath $source -Directory |
        Where-Object { $_.Name -match $jobPattern } |
        Select-Object -ExpandProperty Name
)
$missingFromSplit = @($sourceJobs | Where-Object { $_ -notin $allSplitJobs })
$unknownInSplit = @($allSplitJobs | Where-Object { $_ -notin $sourceJobs })
if ($missingFromSplit.Count -gt 0 -or $unknownInSplit.Count -gt 0) {
    throw "Split/filesystem mismatch. Missing from split: $($missingFromSplit -join ', '); unknown in split: $($unknownInSplit -join ', ')"
}

if ($allSplitJobs.Count -ge 16) {
    if ($a.Count -lt 8 -or $a.Count -gt 12 -or $b.Count -lt 8 -or $b.Count -gt 12) {
        throw "Macro-cluster wave split must be within the P0.7 8/12 to 12/8 range."
    }
    if ($a.Count -ne $b.Count) {
        $statusText = Get-Content -LiteralPath $batchStatus -Raw -Encoding UTF8
        if ($statusText -notmatch '(?im)^.*split justification.*$') {
            throw "An asymmetric Stage 2 split requires an explicit split justification in BATCH_STATUS.md."
        }
    }
}

if ($Cluster -notmatch '^(B[0-9]{2}_C[0-9]{2})_(.+)$') {
    throw "Cannot derive mini-cluster IDs from: $Cluster"
}
$clusterPrefix = $Matches[1]
$clusterLabel = $Matches[2]
$destinations = @{
    "A" = Join-Path $rootPath "stg3_write\input\$($clusterPrefix)A_$clusterLabel"
    "B" = Join-Path $rootPath "stg3_write\input\$($clusterPrefix)B_$clusterLabel"
}

foreach ($suffix in @("A", "B")) {
    $mini = "$($clusterPrefix)$suffix`_$clusterLabel"
    foreach ($job in @($split.$suffix)) {
        $jobSource = Join-Path $source $job
        Assert-NoBlocker -Path $jobSource -Label $job
        Assert-File -Path (Join-Path $jobSource "vacancy.md") -Label "vacancy.md for $job"
        Assert-File -Path (Join-Path $jobSource "vacancy_analysis.md") -Label "vacancy_analysis.md for $job"
        Assert-File -Path (Join-Path $jobSource "package_blueprint.md") -Label "package_blueprint.md for $job"
        Assert-JobIdentity -Path (Join-Path $jobSource "job_identity.json") -Job $job -ExpectedBatch $expectedBatch -ExpectedMacro $Cluster -ExpectedMini $mini
        Assert-Stage2Done -Path (Join-Path $jobSource "_DONE.md") -Job $job
    }
}

foreach ($destination in $destinations.Values) {
    if (Test-Path -LiteralPath $destination) {
        throw "Destination exists: $destination"
    }
}

foreach ($suffix in @("A", "B")) {
    $destination = $destinations[$suffix]
    New-Item -ItemType Directory -Path $destination | Out-Null
    Copy-Item -LiteralPath $clusterBase -Destination $destination
    foreach ($job in @($split.$suffix)) {
        Copy-Item -LiteralPath (Join-Path $source $job) -Destination $destination -Recurse
    }
    Get-ChildItem -LiteralPath $destination -Recurse -File |
        Where-Object { $_.Name -in @("_DONE.md", "BLOCKED.md", "BATCH_STATUS.md") } |
        Remove-Item -Force
}

Write-Output "ADVANCE SUMMARY"
Write-Output "Source: $Cluster"
Write-Output "A: $($a.Count) jobs -> $($destinations['A'])"
Write-Output "B: $($b.Count) jobs -> $($destinations['B'])"
Write-Output "Result: PASS"
exit 0
