import datetime
from app.database.mongodb import db_provider
from app.schemas.habit_schema import HabitInput
from ai_models.habit_prediction.predictor import predict_skip_probability

def analyze_habit(req: HabitInput) -> dict:
    """Run ML prediction and save habit log."""
    
    features = {
        "sleep_hours": req.sleep_hours,
        "stress_level": req.stress_level,
        "previous_workout": req.previous_workout,
        "hydration": req.hydration,
        "consistency": req.consistency
    }
    
    prediction = predict_skip_probability(features)
    
    doc = {
        "user_id": req.user_id,
        "sleep_hours": req.sleep_hours,
        "stress_level": req.stress_level,
        "previous_workout": req.previous_workout,
        "hydration": req.hydration,
        "consistency": req.consistency,
        "prediction_result": prediction,
        "created_at": datetime.datetime.utcnow()
    }
    
    collection = db_provider.get_collection("habit_data")
    collection.insert_one(doc)
    
    return prediction
