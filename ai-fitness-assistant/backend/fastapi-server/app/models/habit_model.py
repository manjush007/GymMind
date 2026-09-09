def serialize_habit(h: dict) -> dict:
    if not h: return {}
    return {
        "id": str(h["_id"]),
        "user_id": h.get("user_id"),
        "sleep_hours": h.get("sleep_hours"),
        "stress_level": h.get("stress_level"),
        "previous_workout": h.get("previous_workout"),
        "hydration": h.get("hydration"),
        "consistency": h.get("consistency"),
        "prediction_result": h.get("prediction_result"),
        "created_at": h.get("created_at")
    }
