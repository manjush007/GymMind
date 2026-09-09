from fastapi import APIRouter
from app.schemas.workout_schema import WorkoutLogCreate, WorkoutStatsResponse
from app.services.workout_service import log_workout, get_user_workout_history, get_user_workout_stats
from typing import List
from uuid import uuid4

router = APIRouter(prefix="/workout", tags=["Workout"])

@router.post("/log")
def log_new_workout(workout: WorkoutLogCreate):
    return log_workout(workout)

@router.get("/history")
def get_history(user_id: str = "guest"):
    return get_user_workout_history(user_id)

@router.get("/stats", response_model=WorkoutStatsResponse)
def get_stats(user_id: str = "guest"):
    return get_user_workout_stats(user_id)
