from fastapi import APIRouter
from app.schemas.diet_schema import DietRequest, DietPlanResponse
from app.services.diet_service import create_diet_plan

router = APIRouter(prefix="/diet", tags=["Diet"])

@router.post("/generate", response_model=DietPlanResponse)
def generate_plan(req: DietRequest):
    return create_diet_plan(req)
