$ErrorActionPreference = "Stop"

# Garantir ambiente limpo
Remove-Item -Recurse -Force dist, build -ErrorAction SilentlyContinue | Out-Null

# Garantir PyInstaller instalado
try {
  pyinstaller --version | Out-Null
} catch {
  Write-Host "Instalando PyInstaller..."
  python -m pip install --upgrade pip pyinstaller | Out-Null
}

# Build do executável
Write-Host "Iniciando build..."
# Ícone opcional (use icon.ico se existir)
$iconArg = ""
if (Test-Path "icon.ico") {
  $iconArg = "--icon icon.ico"
  Write-Host "Usando ícone: icon.ico"
}

pyinstaller --noconfirm --onefile --windowed --name AuxiliadorAcionamentos `
  --add-data "historico;historico" `
  --add-data "config.py;." `
  --add-data "theme.py;." `
  --add-data "ui_components.py;." `
  --add-data "validators.py;." `
  $iconArg `
  main.py

Write-Host "Build concluído. Executável em dist/AuxiliadorAcionamentos.exe"


