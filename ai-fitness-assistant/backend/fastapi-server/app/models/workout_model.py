def serialize_workout(w: dict) -> dict:
    if not w: return {}
    return {
        "id": str(w["_id"]),
        "user_id": w.get("user_id"),
        "name": w.get("name"),
        "duration": w.get("duration"),
        "score": w.get("score"),
        "tag": w.get("tag"),
        "calories_burned": w.get("calories_burned"),
        "date": w.get("date")
    }
