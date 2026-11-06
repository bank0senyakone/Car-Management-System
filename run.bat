@echo off
chcp 65001 >nul
title J&P Auto - Car Management System Launcher

echo ========================================================
echo   J&P Auto - Car Management System
echo   ກຳລັງເປີດລະບົບ Backend ແລະ Frontend...
echo ========================================================
echo.

cd /d "%~dp0"

:: ກວດສອບວ່າ Python ຖືກຕິດຕັ້ງແລ້ວຫຼືບໍ່
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] ບໍ່ພົບ Python ໃນລະບົບ! ກະລຸນາຕິດຕັ້ງ Python ກ່ອນ.
    pause
    exit /b
)

:: Run script ຫຼັກ
python run.py

if %errorlevel% neq 0 (
    echo.
    echo [!] ມີຂໍ້ຜິດພາດເກີດຂຶ້ນ.
    pause
)

