import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from app.database.mongodb import db_provider
from app.routers import user_routes, workout_routes, diet_routes, habit_routes, chat_routes

# Configure basic logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logging.info("Starting up FastAPI AI Fitness server...")
    db_provider.connect()
    yield
    # Shutdown
    logging.info("Shutting down server...")
    db_provider.disconnect()

app = FastAPI(
    title="AI Fitness Assistant API",
    description="Backend for AI-powered workout, diet, and habit tracking.",
    version="1.0.0",
    lifespan=lifespan
)

# Allow React dashboard
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"], # Add your frontend domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(user_routes.router)
app.include_router(workout_routes.router)
app.include_router(diet_routes.router)
app.include_router(habit_routes.router)
app.include_router(chat_routes.router)

@app.get("/")
def health_check():
    return {"status": "success", "message": "AI Fitness API is running."}
