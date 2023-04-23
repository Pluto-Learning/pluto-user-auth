from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any
from motor.motor_asyncio import AsyncIOMotorDatabase

from src.domain.user.model import User
from src.domain.user.service import UserService
from src.infastructure.database.mongo import get_client

router = APIRouter()

@router.get('/{username}')
async def user_handler(username: str, db: AsyncIOMotorDatabase = Depends(get_client)) -> Dict[str, Any]:
    user_service: UserService = UserService(db)
    user: User = await user_service.user(username)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        'code': 200,
        'message': '',
        'body': User.parse_obj(user)
    }