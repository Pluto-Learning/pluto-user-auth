from fastapi import APIRouter
from typing import Dict, Any
from motor.motor_asyncio import AsyncIOMotorDatabase
from src.domain.user.model import User

from src.infastructure.config.environment.base import settings
from src.infastructure.database.mongo import get_client

router = APIRouter()

@router.get('/health')
async def health_handler() -> Dict[str, Any]:
    return {
        'status': 'OK',
        'version': settings.VERSION,
        'dependencies': [],
    }

@router.get('/')
async def root_handler() -> Dict[str, Any]:
    return {
        'code': 200,
        'message': 'Base endpoint',
        'body': {}
    }