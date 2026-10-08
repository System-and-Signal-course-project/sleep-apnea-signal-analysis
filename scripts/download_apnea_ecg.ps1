$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $PSScriptRoot
$dataDir = Join-Path $projectRoot "data\raw\apnea-ecg"
New-Item -ItemType Directory -Force -Path $dataDir | Out-Null

$url = "https://physionet.org/files/apnea-ecg/1.0.0/"

Write-Host "Downloading PhysioNet Apnea-ECG Database to $dataDir"
Write-Host "The complete database is about 580.6 MB uncompressed."

wget.exe -r -N -c -np --directory-prefix=$dataDir $url

Write-Host "Download complete. Raw data remains ignored by Git."
