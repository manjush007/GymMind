from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate, UserResponse
from app.database.mongodb import db_provider
import datetime

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/create", response_model=UserResponse)
def create_user(user: UserCreate):
    collection = db_provider.get_collection("users")
    
    # Check if exists
    existing = collection.find_one({"email": user.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
        
    doc = user.model_dump()
    doc["created_at"] = datetime.datetime.utcnow()
    
    result = collection.insert_one(doc)
    doc["id"] = str(result.inserted_id)
    
    return doc

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str):
    from bson.objectid import ObjectId
    collection = db_provider.get_collection("users")
    
    try:
        user = collection.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user["id"] = str(user["_id"])
        return user
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid User ID format")
