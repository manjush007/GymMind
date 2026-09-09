from pydantic import BaseModel
from typing import List

class DietRequest(BaseModel):
    user_id: str = "guest"
    weight: float
    height: float
    goal: str # e.g., "muscle_gain", "fat_loss"

class DietPlanResponse(BaseModel):
    calories: int
    protein: str
    carbs: str
    fats: str
    meals: List[str]
    goal: str
