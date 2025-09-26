@echo off
title Auxiliador de Acionamentos
echo ===============================================
echo    AUXILIADOR DE ACIONAMENTOS
echo ===============================================
echo.
echo Verificando dependencias...
pip install -r requirements.txt --quiet
echo.
echo Iniciando programa...
python main.py
pause
