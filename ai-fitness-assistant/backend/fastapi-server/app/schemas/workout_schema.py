from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class WorkoutLogBase(BaseModel):
    user_id: str
    name: str
    duration: int = Field(..., description="Duration in minutes")
    score: int = Field(..., description="Performance score out of 100")
    tag: str
    calories_burned: int
    date: Optional[datetime] = None

class WorkoutLogCreate(WorkoutLogBase):
    pass

class WorkoutLogResponse(WorkoutLogBase):
    id: str
    date: datetime

class InsightSchema(BaseModel):
    text: str
    type: str # e.g. "tip", "warning"

class WorkoutStatsResponse(BaseModel):
    total_workouts: int
    weekly_change: str
    calories_burned: int
    calories_change: str
    avg_performance: int
    performance_change: str
    streak_days: int
    streak_label: str
    weekly_performance: List[int]
    weekly_calories: List[int]
    insights: List[str]
