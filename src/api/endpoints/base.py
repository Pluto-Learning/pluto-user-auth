from fastapi import APIRouter
from typing import Dict, Any

from src.infastructure.config.environment.base import settings

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