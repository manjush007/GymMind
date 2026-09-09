@echo off
REM AI Fitness Assistant - Windows Batch Startup Script
REM This script starts the entire AI Fitness Assistant system

setlocal enabledelayedexpansion

color 0B
cls

echo.
echo ================================================
echo   AI FITNESS ASSISTANT - SYSTEM STARTUP
echo ================================================
echo.

REM Get the project root directory
for %%A in ("%cd%") do set projectRoot=%%~dpA

set backendPath=%projectRoot%backend\fastapi-server
set frontendPath=%projectRoot%frontend\react-dashboard

echo [1/3] Checking prerequisites...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9 or higher
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js ^(v14 or higher^)
    pause
    exit /b 1
)

echo Python version:
python --version
echo Node.js version:
node --version
echo.

echo [2/3] Installing dependencies ^(if needed^)...
echo.

REM Check and install backend dependencies
if not exist "%backendPath%\venv" (
    echo Creating Python virtual environment in backend...
    cd /d "%backendPath%"
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install -r requirements.txt
) else (
    echo Virtual environment already exists
)

REM Check and install frontend dependencies
if not exist "%frontendPath%\node_modules" (
    echo Installing frontend npm dependencies...
    cd /d "%frontendPath%"
    call npm install
) else (
    echo Node modules already installed
)

echo.
echo [3/3] Starting services...
echo.

REM Start Backend in a new window
echo Starting Backend Server on port 8000...
cd /d "%backendPath%"
start /t "Backend Server" cmd /k "venv\Scripts\activate.bat && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

REM Wait a bit for backend to start
timeout /t 3 /nobreak

REM Start Frontend in a new window
echo Starting Frontend Dashboard on port 3000...
cd /d "%frontendPath%"
start /t "Frontend Dashboard" cmd /k "npm start"

echo.
echo ================================================
echo   SYSTEM STARTUP COMPLETE
echo ================================================
echo.
echo Backend API:        http://localhost:8000
echo  - API Docs:        http://localhost:8000/docs
echo.
echo Frontend Dashboard: http://localhost:3000
echo.
echo MongoDB:            mongodb://localhost:27017
echo Database Name:      ai_fitness_db
echo.
echo ================================================
echo.
echo Services are now running in separate windows.
echo Close the respective windows to stop each service.
echo.
pause
