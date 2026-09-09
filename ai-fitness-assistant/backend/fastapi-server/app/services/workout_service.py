import datetime
from app.database.mongodb import db_provider
from app.schemas.workout_schema import WorkoutLogCreate
from ai_models.pose_detection.pose_detector import PoseDetector

# Initialize AI model once (lazy load ideally, but ok here)
pose_detector = PoseDetector()

def log_workout(req: WorkoutLogCreate) -> dict:
    """Save a single workout log to MongoDB."""
    doc = req.model_dump()
    doc["date"] = doc.get("date") or datetime.datetime.utcnow()
    
    collection = db_provider.get_collection("workout_logs")
    result = collection.insert_one(doc)
    doc["id"] = str(result.inserted_id)
    del doc["_id"]
    return doc

def get_user_workout_history(user_id: str):
    """Fetch history from DB descending."""
    collection = db_provider.get_collection("workout_logs")
    cursor = collection.find({"user_id": user_id}).sort("date", -1).limit(20)
    
    results = []
    for w in cursor:
        results.append({
            "id": str(w["_id"]),
            "name": w.get("name"),
            "duration": f"{w.get('duration', 0)} min",
            "score": w.get("score", 0),
            "tag": w.get("tag", "General"),
            "date": w.get("date").strftime("%b %d, %Y") if w.get("date") else "Unknown"
        })
    return results

def get_user_workout_stats(user_id: str) -> dict:
    """Mock aggregation for the dashboard for now."""
    collection = db_provider.get_collection("workout_logs")
    
    # Simple count example
    total = collection.count_documents({"user_id": user_id})
    
    # If no data, return default empty stats
    if total == 0:
        return {
            "total_workouts": 0, "weekly_change": "+0 this week",
            "calories_burned": 0, "calories_change": "+0 today",
            "avg_performance": 0, "performance_change": "+0 pts",
            "streak_days": 0, "streak_label": "Start today!",
            "weekly_performance": [],
            "weekly_calories": [],
            "insights": ["Complete a workout to get personalized AI insights!"]
        }
        
    # Example logic (in reality, run a MongoDB aggregation pipeline)
    return {
        "total_workouts": total,
        "weekly_change": "+2 this week",
        "calories_burned": total * 320, # rough estimate
        "calories_change": "+320 today",
        "avg_performance": 85,
        "performance_change": "+2 pts",
        "streak_days": 3,
        "streak_label": "Keep it up!",
        "weekly_performance": [60, 70, 75, 65, 80, 85, 90][:min(total, 7)],
        "weekly_calories": [300, 320, 350, 300, 400, 450, 420][:min(total, 7)],
        "insights": [
            "You perform 15% better on morning workouts.",
            "Protein synthesis is optimal right now. Grab a shake!"
        ]
    }
