from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import HTTPException

from src.infastructure.config.environment.base import settings

async def get_client() -> AsyncIOMotorClient:
    try:
        client = AsyncIOMotorClient(settings.MONGO_URL)
        return client
    except:
        raise HTTPException(status_code=500, detail="Could not connect to database")
