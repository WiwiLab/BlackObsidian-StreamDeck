@echo off
title BlackObsidian StreamDeck

echo.
echo ============================================
echo      BlackObsidian StreamDeck
echo ============================================
echo.

python tools\generate_requirements.py

python install_requirements.py

echo.
echo Iniciando...
echo.

python main.py

pause