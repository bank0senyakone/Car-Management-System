@echo off
chcp 65001 >nul
title J&P Auto - System Launcher (Separate Windows)

echo ========================================================
echo   J&P Auto - Car Management System
echo   ເປີດແບບແຍກ 2 ໜ້າຕ່າງ (Terminal ແຍກ Backend / Frontend)
echo ========================================================
echo.

cd /d "%~dp0"

echo [1/2] ກຳລັງເປີດ Backend ໃນໜ້າຕ່າງໃໝ່...
start "J&P Auto - Backend API (Port 8000)" cmd /k "cd /d "%~dp0backend" && python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload"

:: ລໍຖ້າ 3 ວິນາທີເພື່ອໃຫ້ Backend ພ້ອມ
timeout /t 3 /nobreak >nul

echo [2/2] ກຳລັງເປີດ Frontend...
cd /d "%~dp0frontend"
python main.py

echo.
echo Frontend ຖືກປິດແລ້ວ.
pause

