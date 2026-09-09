from fastapi import APIRouter
from app.schemas.habit_schema import HabitInput, HabitPredictionResponse
from app.services.habit_service import analyze_habit

router = APIRouter(prefix="/habit", tags=["Habit"])

@router.post("/predict", response_model=HabitPredictionResponse)
def predict_habit(req: HabitInput):
    return analyze_habit(req)
