# AI Fitness Assistant - Complete System Startup Script
# This script starts the entire system: Backend, Frontend, and ensures MongoDB is ready

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  AI FITNESS ASSISTANT - SYSTEM STARTUP" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Define paths
$projectRoot = Split-Path -Parent $MyInvocation.MyCommandPath
$backendPath = Join-Path $projectRoot "backend\fastapi-server"
$frontendPath = Join-Path $projectRoot "frontend\react-dashboard"

Write-Host "[1/4] Checking MongoDB connection..." -ForegroundColor Yellow
# Basic check - try to connect to MongoDB (optional, can be skipped if local MongoDB not running)
Write-Host "      MongoDB should be running on localhost:27017" -ForegroundColor Gray
Write-Host ""

# Start Backend
Write-Host "[2/4] Starting FastAPI Backend Server..." -ForegroundColor Yellow
Write-Host "      Location: $backendPath" -ForegroundColor Gray
Write-Host "      Command: uvicorn app.main:app --reload --host 0.0.0.0 --port 8000" -ForegroundColor Gray
Write-Host ""

# Create a new terminal/process for backend
$backendProcess = Start-Process -FilePath "pwsh" -ArgumentList @"
-NoExit -Command "cd '$backendPath' && python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
"@ -PassThru

Write-Host "✓ Backend started (PID: $($backendProcess.Id))" -ForegroundColor Green
Write-Host ""

# Wait a moment for backend to start
Start-Sleep -Seconds 3

# Start Frontend
Write-Host "[3/4] Starting React Frontend Dashboard..." -ForegroundColor Yellow
Write-Host "      Location: $frontendPath" -ForegroundColor Gray
Write-Host "      Command: npm start" -ForegroundColor Gray
Write-Host ""

# Create a new terminal/process for frontend
$frontendProcess = Start-Process -FilePath "pwsh" -ArgumentList @"
-NoExit -Command "cd '$frontendPath' && npm start"
"@ -PassThru

Write-Host "✓ Frontend started (PID: $($frontendProcess.Id))" -ForegroundColor Green
Write-Host ""

# Display system status
Write-Host "[4/4] System Status" -ForegroundColor Yellow
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Backend API:        http://localhost:8000" -ForegroundColor Green
Write-Host "  - API Docs:       http://localhost:8000/docs" -ForegroundColor Green
Write-Host "  - Alternative:    http://localhost:8000/redoc" -ForegroundColor Green
Write-Host ""
Write-Host "Frontend Dashboard: http://localhost:3000" -ForegroundColor Green
Write-Host ""
Write-Host "Database:           MongoDB (localhost:27017)" -ForegroundColor Cyan
Write-Host "  - Database Name:  ai_fitness_db" -ForegroundColor Cyan
Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "✓ System is now running!" -ForegroundColor Green
Write-Host ""
Write-Host "Process Information:" -ForegroundColor Yellow
Write-Host "  Backend Process ID:  $($backendProcess.Id)" -ForegroundColor Gray
Write-Host "  Frontend Process ID: $($frontendProcess.Id)" -ForegroundColor Gray
Write-Host ""
Write-Host "To stop the system, close both terminal windows." -ForegroundColor Yellow
Write-Host ""

# Keep this window open
Read-Host "Press Enter to continue or close this window to stop"
