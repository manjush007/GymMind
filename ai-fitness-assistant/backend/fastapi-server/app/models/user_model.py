def serialize_user(user: dict) -> dict:
    """Convert MongoDB user document to dict, stringifying the ObjectId."""
    if not user: return {}
    return {
        "id": str(user["_id"]),
        "name": user.get("name"),
        "email": user.get("email"),
        "age": user.get("age")
    }
