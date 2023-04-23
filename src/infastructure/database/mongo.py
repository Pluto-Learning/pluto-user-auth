from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from fastapi import HTTPException
from src.infastructure.config.environment.base import settings

async def get_client() -> AsyncIOMotorDatabase:
    try:
        client = AsyncIOMotorClient(settings.MONGO_URL)
        return client['user-auth']
    except:
        raise HTTPException(status_code=500, detail="Could not connect to database")
