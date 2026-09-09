import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME: str = os.getenv("DB_NAME", "ai_fitness_db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "fallback_secret_key")

settings = Settings()
