@echo off
cd /d "%~dp0"
where pyw >nul 2>&1
if errorlevel 1 (
    echo Python 3 is required. Please install Python and try again.
    pause
    exit /b 1
)
start "" pyw -3 "%~dp0start_game.py"
