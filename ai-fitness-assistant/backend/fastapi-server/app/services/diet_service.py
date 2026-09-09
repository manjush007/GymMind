import datetime
from app.database.mongodb import db_provider
from app.schemas.diet_schema import DietRequest
from ai_models.diet_recommendation.diet_generator import generate_diet_plan

def create_diet_plan(req: DietRequest) -> dict:
    """Generate diet plan using AI module and save to DB."""
    plan_data = generate_diet_plan(req.weight, req.height, req.goal)
    
    doc = {
        "user_id": req.user_id,
        "weight": req.weight,
        "height": req.height,
        "goal": req.goal,
        "calories": plan_data["calories"],
        "plan": plan_data,
        "created_at": datetime.datetime.utcnow()
    }
    
    # Save to db
    collection = db_provider.get_collection("diet_logs")
    result = collection.insert_one(doc)
    doc["_id"] = result.inserted_id
    
    return plan_data
