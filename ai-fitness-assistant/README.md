# AI Fitness Assistant

AI Fitness Assistant is a full-stack health and fitness application. It combines a React dashboard, a FastAPI backend, MongoDB persistence, workout and habit models, diet recommendations, pose-detection utilities, and an optional Gemini-powered fitness chatbot.

## Features

- Dashboard for fitness activity and progress
- Workout logging, history, and statistics
- Diet plan generation and calorie-related recommendations
- Habit prediction and habit tracking
- AI fitness chatbot with Gemini integration
- Keyword-based chatbot fallback when Gemini is unavailable or rate-limited
- Pose detection, posture analysis, and repetition counting utilities
- Interactive API documentation through FastAPI

## Technology Stack

- Frontend: React 18, React Router, Axios, Chart.js
- Backend: Python, FastAPI, Uvicorn, Pydantic
- Database: MongoDB and PyMongo
- Machine learning: NumPy, scikit-learn, MediaPipe, OpenCV
- AI chatbot: Google Gemini API

## Project Structure

```text
ai-fitness-assistant/
|-- ai_models/                 # Standalone model and data utilities
|-- backend/
|   |-- fastapi-server/
|       |-- app/               # FastAPI application, routes, schemas, services
|       |-- ai_models/         # Backend chatbot integration
|       |-- requirements.txt
|-- database/                  # Database setup and seed data
|-- docs/                      # Architecture and project documentation
|-- frontend/react-dashboard/  # React web dashboard
|-- tests/                     # Python tests
|-- SETUP_AND_RUN.md           # Expanded setup notes
|-- START_SYSTEM.ps1           # Windows startup script
|-- START_SYSTEM.bat           # Batch startup script
```

## Prerequisites

Install the following before starting:

- Python 3.9 or newer
- Node.js 14 or newer and npm
- MongoDB, either locally or through MongoDB Atlas
- Git

Check the installed versions:

```powershell
python --version
node --version
npm --version
```

## Configuration

Create `backend/fastapi-server/.env`:

```env
MONGO_URI=mongodb://localhost:27017
DB_NAME=ai_fitness_db
SECRET_KEY=replace-this-with-a-long-random-secret
GEMINI_API_KEY=your-gemini-api-key
```

`MONGO_URI`, `DB_NAME`, and `SECRET_KEY` have development defaults. `GEMINI_API_KEY` is optional, but it is required for live Gemini chatbot responses. Never commit `.env` or API keys to GitHub.

## Quick Start on Windows

From the project root, install the dependencies first:

```powershell
cd "backend\fastapi-server"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

cd "..\..\frontend\react-dashboard"
npm install
```

Make sure MongoDB is running, then start the services in separate PowerShell windows.

### Start the backend

```powershell
cd "backend\fastapi-server"
.\venv\Scripts\Activate.ps1
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Start the frontend

```powershell
cd "frontend\react-dashboard"
npm start
```

The dashboard opens at [http://localhost:3000](http://localhost:3000). The API is available at [http://localhost:8000](http://localhost:8000).

### Start everything with the Windows script

From the project root:

```powershell
.\START_SYSTEM.ps1
```

The script opens the backend and frontend in separate terminals. MongoDB must already be running.

## API Documentation

FastAPI provides interactive documentation at:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- Health check: [http://localhost:8000/](http://localhost:8000/)

The main route groups are:

| Route | Purpose |
| --- | --- |
| `POST /users/create` | Create a user |
| `GET /users/{user_id}` | Retrieve a user |
| `POST /workouts/log` | Log a workout |
| `GET /workouts/history` | Retrieve workout history |
| `GET /workouts/stats` | Retrieve workout statistics |
| `POST /diet/generate` | Generate a diet plan |
| `POST /habits/predict` | Predict habit results |
| `POST /chat/ask` | Ask the AI fitness coach |

Use `/docs` for the exact request and response schemas.

## Running Tests

From the project root, activate the backend virtual environment and run:

```powershell
cd backend\fastapi-server
.\venv\Scripts\Activate.ps1
pytest ..\..\tests -q
```

## Database

The default local MongoDB configuration uses:

```text
Host: localhost
Port: 27017
Database: ai_fitness_db
```

To use MongoDB Atlas, replace `MONGO_URI` in `.env` with the Atlas connection string. The optional seed script is located at `database/seed_data.py`.

## Troubleshooting

### MongoDB connection failed

Start MongoDB locally or verify the `MONGO_URI` value in `backend/fastapi-server/.env`. The backend checks the database connection during startup.

### Port already in use

Use another port or find and stop the process using the port:

```powershell
netstat -ano | findstr :8000
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

### Frontend cannot reach the API

Confirm that the backend is running at `http://localhost:8000`. The frontend API client is configured in `frontend/react-dashboard/src/services/api.js`.

### PowerShell does not allow virtual environment activation

Run PowerShell as your normal user and allow local scripts if needed:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## GitHub Setup

Run these commands from the `ai-fitness-assistant` folder:

```powershell
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repository>.git
git push -u origin main
```

Ensure the project `.gitignore` is inside `ai-fitness-assistant` before running `git add .`. At minimum, do not push `.env`, virtual environments, `node_modules`, Python caches, or generated build files.

## Disclaimer

This project provides fitness and wellness assistance for educational purposes. It is not a medical device and does not replace advice from a qualified healthcare professional. Consult a doctor for injuries, medical conditions, or significant changes to diet or exercise.
