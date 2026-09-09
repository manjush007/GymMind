from pydantic import BaseModel, Field

class HabitInput(BaseModel):
    user_id: str = "guest"
    sleep_hours: float
    stress_level: int = Field(..., ge=1, le=10)
    previous_workout: int = Field(..., description="1 for yes, 0 for no")
    hydration: int
    consistency: int = Field(..., ge=0, le=100)

class HabitPredictionResponse(BaseModel):
    skip_probability: float
    risk: str # "high", "medium", "low"
    recommendation: str
