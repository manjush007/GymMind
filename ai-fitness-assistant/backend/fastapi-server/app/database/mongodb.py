from pymongo import MongoClient
from app.utils.config import settings
import logging
import certifi

logger = logging.getLogger(__name__)

class DatabaseProvider:
    client: MongoClient = None
    db = None

    @classmethod
    def connect(cls):
        try:
            # Use certifi to provide Mozilla's CA Bundle for standard SSL connections
            cls.client = MongoClient(
                settings.MONGO_URI, 
                serverSelectionTimeoutMS=5000,
                tlsCAFile=certifi.where()
            )
            cls.db = cls.client[settings.DB_NAME]
            # Verify connection
            cls.client.admin.command('ping')
            logger.info("MongoDB connected successfully.")
        except Exception as e:
            logger.error(f"MongoDB connection failed: {e}")
            raise

    @classmethod
    def disconnect(cls):
        if cls.client:
            cls.client.close()
            logger.info("MongoDB disconnected.")

    @classmethod
    def get_collection(cls, collection_name: str):
        if cls.db is None:
            raise RuntimeError("Database not initialized. Call connect() first.")
        return cls.db[collection_name]

# Helper singleton instance access (though methods are classmethods)
db_provider = DatabaseProvider()
