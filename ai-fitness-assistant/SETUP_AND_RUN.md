# AI Fitness Assistant - Complete Setup & Run Guide

## 📋 Prerequisites

Before running the system, ensure you have installed:

1. **Python** (3.9 or higher)
   ```powershell
   python --version
   ```

2. **Node.js** (v14 or higher)
   ```powershell
   node --version
   npm --version
   ```

3. **MongoDB** (local installation or cloud - Atlas)
   - Local: Default at `mongodb://localhost:27017`
   - Or use MongoDB Atlas connection string in `.env`

---

## 🚀 QUICK START (Automated)

### Option 1: PowerShell Script (Recommended for Windows)
```powershell
# Navigate to project root
cd "c:\Users\hp\OneDrive\Desktop\ai healthcare (unlox)\ai-fitness-assistant"

# Run the startup script
.\START_SYSTEM.ps1
```

### Option 2: Batch File (Alternative Windows)
```bash
cd "c:\Users\hp\OneDrive\Desktop\ai healthcare (unlox)\ai-fitness-assistant"
START_SYSTEM.bat
```

---

## 🔧 MANUAL SETUP & RUN

### Step 1: Setup Backend

```powershell
# Navigate to backend directory
cd backend\fastapi-server

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Setup Frontend

```powershell
# Navigate to frontend directory (from project root)
cd frontend\react-dashboard

# Install npm dependencies
npm install
```

### Step 3: Configure Environment Variables

Create a `.env` file in `backend/fastapi-server/app/` if needed:

```env
MONGO_URI=mongodb://localhost:27017
DB_NAME=ai_fitness_db
SECRET_KEY=your-secret-key-here
```

**Note:** Default values will work if MongoDB is running locally.

### Step 4: Start MongoDB

```bash
# Make sure MongoDB is running
# If installed locally, start MongoDB service:
mongod
```

Or use MongoDB Atlas (cloud):
- Get your connection string from [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- Update `MONGO_URI` in `.env` file

### Step 5: Start Backend Server

```powershell
# From backend/fastapi-server directory (with venv activated)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Output should show:
# ✓ Uvicorn running on http://0.0.0.0:8000
# ✓ Application startup complete
```

### Step 6: Start Frontend Dashboard

**In a NEW terminal window:**

```powershell
# Navigate to frontend directory
cd frontend\react-dashboard

# Start React development server
npm start

# Browser will automatically open: http://localhost:3000
```

---

## 🌐 Access the System

Once running, open in your browser:

### Frontend Dashboard
- **URL:** http://localhost:3000
- **Pages:**
  - Dashboard (home)
  - Workouts
  - Diet Plans
  - Habits
  - Chat with AI Coach

### Backend API
- **URL:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs (Swagger UI)
- **Alternative Docs:** http://localhost:8000/redoc

### API Endpoints
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/users` | GET/POST | User management |
| `/api/workouts` | GET/POST | Workout tracking |
| `/api/diet` | GET/POST | Diet planning |
| `/api/habits` | GET/POST | Habit tracking |
| `/api/chat` | POST | AI chatbot |

---

## 📱 System Architecture

```
┌─────────────────────────────────────────┐
│      React Dashboard (Port 3000)        │
│  - Dashboard                            │
│  - Workouts                             │
│  - Diet Plans                           │
│  - Habits                               │
│  - AI Chat                              │
└────────────┬────────────────────────────┘
             │ HTTP/REST
┌────────────▼────────────────────────────┐
│    FastAPI Backend (Port 8000)          │
│  - User Routes                          │
│  - Workout Routes                       │
│  - Diet Routes                          │
│  - Habit Routes                         │
│  - Chat Routes (Gemini AI)              │
└────────────┬────────────────────────────┘
             │ PyMongo
┌────────────▼────────────────────────────┐
│    MongoDB (localhost:27017)            │
│  - Collections:                         │
│    • users                              │
│    • workouts                           │
│    • diets                              │
│    • habits                             │
└─────────────────────────────────────────┘
```

---

## 🛑 Stopping the System

### If using automated script:
- Close the Backend terminal window
- Close the Frontend terminal window

### If running manually:
- **Backend:** Press `Ctrl+C` in the backend terminal
- **Frontend:** Press `Ctrl+C` in the frontend terminal

---

## 🐛 Troubleshooting

### Issue: "MongoDB connection failed"
**Solution:**
```powershell
# Check if MongoDB is running
# If using local MongoDB:
mongod

# Or use MongoDB Atlas connection string in .env:
MONGO_URI=mongodb+srv://user:password@cluster.mongodb.net/?retryWrites=true&w=majority
```

### Issue: "Port 8000/3000 already in use"
```powershell
# Find process using port 8000 (backend)
netstat -ano | findstr :8000

# Find process using port 3000 (frontend)
netstat -ano | findstr :3000

# Kill the process
taskkill /PID <PID> /F
```

### Issue: "Python module not found"
```powershell
# Ensure virtual environment is activated
cd backend\fastapi-server
.\venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: "npm packages missing"
```powershell
cd frontend\react-dashboard
rm -r node_modules
npm install
```

---

## 📦 Technologies Stack

- **Frontend:** React 18, Chart.js, React Router, Axios
- **Backend:** FastAPI, Uvicorn, PyMongo
- **Database:** MongoDB
- **AI Model:** Google Gemini (for chatbot)
- **Pose Detection:** MediaPipe, OpenCV

---

## 📝 Environment Configuration

Create `.env` file in `backend/fastapi-server/app/`:

```env
# MongoDB Configuration
MONGO_URI=mongodb://localhost:27017
DB_NAME=ai_fitness_db

# Security
SECRET_KEY=your-secret-key-for-jwt-tokens

# Optional: Google Gemini API Key (for chatbot)
GEMINI_API_KEY=your-gemini-api-key
```

---

## ✅ Verification Checklist

- [ ] Python installed and working
- [ ] Node.js installed and working
- [ ] MongoDB running/accessible
- [ ] Backend dependencies installed
- [ ] Frontend dependencies installed
- [ ] `.env` file configured
- [ ] Backend server running on port 8000
- [ ] Frontend running on port 3000
- [ ] Can access http://localhost:3000
- [ ] Can access http://localhost:8000/docs

---

## 🎯 Next Steps

1. **Explore the Dashboard:**
   - Create a user account
   - Add workouts and diet plans
   - Track habits
   - Chat with AI coach

2. **Test API:**
   - Visit http://localhost:8000/docs
   - Try out various endpoints
   - Check responses

3. **Customize:**
   - Modify components in `frontend/src/`
   - Update models in `backend/app/models/`
   - Configure database schemas

---

## 💡 Tips

- **Development Mode:** Both frontend and backend run in hot-reload mode. Changes are reflected automatically.
- **API Testing:** Use the Swagger UI at http://localhost:8000/docs
- **Database:** Access MongoDB directly with MongoDB Compass or CLI
- **Logs:** Check terminal output for detailed logs and errors

---

## 🆘 Support

For issues or questions:
1. Check the troubleshooting section
2. Review terminal output for error messages
3. Ensure all prerequisites are installed
4. Verify MongoDB connection
5. Check firewall/antivirus settings if ports are blocked

---

**Ready to run? Start with the Quick Start section!** 🚀
