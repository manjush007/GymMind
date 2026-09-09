def serialize_diet(d: dict) -> dict:
    if not d: return {}
    return {
        "id": str(d["_id"]),
        "user_id": d.get("user_id"),
        "weight": d.get("weight"),
        "height": d.get("height"),
        "goal": d.get("goal"),
        "calories": d.get("calories"),
        "plan": d.get("plan"), # The object returned by diet generator
        "created_at": d.get("created_at")
    }
