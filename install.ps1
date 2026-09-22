#Requires -Version 5.1
<#
.SYNOPSIS
    Installer for Gorbe on Windows.
.DESCRIPTION
    Copies dist\gorbe.exe to %LOCALAPPDATA%\Programs\gorbe and adds it to the user PATH.
.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\install.ps1
#>

$ErrorActionPreference = "Stop"

# ── Helpers ──
function Write-Success($msg) { Write-Host "OK  $msg" -ForegroundColor Green }
function Write-Info($msg)    { Write-Host ">>  $msg" -ForegroundColor Yellow }
function Write-Err($msg)     { Write-Host "ERR $msg" -ForegroundColor Red }
function Write-Title($msg)   { Write-Host $msg -ForegroundColor Cyan }

Write-Title "Installing Gorbe"
Write-Title "-----------------------------------"

# ── Paths ──
$ScriptDir   = Split-Path -Parent $MyInvocation.MyCommand.Definition
$Binary      = Join-Path $ScriptDir "dist\gorbe.exe"
$InstallDir  = Join-Path $env:LOCALAPPDATA "Programs\gorbe"
$InstallPath = Join-Path $InstallDir "gorbe.exe"

# ── 1. Check binary exists ──
if (-not (Test-Path $Binary)) {
    Write-Err "Binary not found: $Binary"
    Write-Info "Build it first with:"
    Write-Info '  python -m PyInstaller --clean --noconfirm --onefile --name gorbe --add-data "templates;templates" main.py'
    exit 1
}

Write-Success "Binary found: $Binary"

# ── 2. Create install directory ──
if (-not (Test-Path $InstallDir)) {
    New-Item -ItemType Directory -Path $InstallDir -Force | Out-Null
    Write-Success "Created: $InstallDir"
}

# ── 3. Copy binary ──
Write-Info "Installing to $InstallPath ..."
Copy-Item -Path $Binary -Destination $InstallPath -Force
Write-Success "Installed to $InstallPath"

# ── 4. Add to user PATH ──
$UserPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($null -eq $UserPath) { $UserPath = "" }

if ($UserPath -notlike "*$InstallDir*") {
    if ([string]::IsNullOrWhiteSpace($UserPath)) {
        $NewPath = $InstallDir
    } else {
        $NewPath = "$UserPath;$InstallDir"
    }
    [Environment]::SetEnvironmentVariable("Path", $NewPath, "User")
    $env:Path += ";$InstallDir"
    Write-Success "Added to user PATH: $InstallDir"
} else {
    Write-Success "Already in PATH: $InstallDir"
}

# ── 5. Verify ──
Write-Host ""
if (Get-Command gorbe -ErrorAction SilentlyContinue) {
    Write-Success "'gorbe' command is available in current session"
} else {
    Write-Host "NOTE: 'gorbe' will be available after restarting your terminal." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Installation complete!" -ForegroundColor Green
Write-Host "  Run:  " -NoNewline -ForegroundColor Cyan
Write-Host "gorbe" -ForegroundColor Green
Write-Host "  Help: " -NoNewline -ForegroundColor Cyan
Write-Host "gorbe --help" -ForegroundColor Green
Write-Host ""
Write-Host "Restart your terminal for PATH changes to take effect." -ForegroundColor Yellow
