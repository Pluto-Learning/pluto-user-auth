from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any
from motor.motor_asyncio import AsyncIOMotorDatabase

from src.api.endpoints.wrapper import ResBody
from src.domain.user.model import User, UserCreate, parse_user
from src.domain.user.service import UserService
from src.infastructure.database.mongo import get_client
from src.infastructure.security.password import validate_psw

router = APIRouter()

@router.get(
    path='/', 
    status_code=200, 
    response_model=ResBody
)
async def user_handler(
    username: str, 
    db: AsyncIOMotorDatabase = Depends(get_client)
) -> Dict[str, Any]:
    if not username:
        raise HTTPException(status_code=400, detail='Invalid username param')
    
    user_service: UserService = UserService(db)
    user: User = await user_service.user(username)
    
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    return {
        'code': 200,
        'message': '',
        'body': parse_user(user)
    }
    
@router.get(
    path='/login/', 
    status_code=200, 
    response_model=ResBody
)
async def login_handler(
    username: str, password: str,
    db: AsyncIOMotorDatabase = Depends(get_client)
) -> Dict[str, Any]:
    user_service: UserService = UserService(db)
    user: User = await user_service.user(username)
    
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    if not validate_psw(password, user['password']):
        raise HTTPException(status_code=401, detail='Invalid password')
    
    return {
        'code': 200,
        'message': 'valid user credentials',
        'body': parse_user(user)
    }
    
@router.post(
    path='/register/', 
    status_code=201, 
    response_model=ResBody
)
async def register_handler(
    body: UserCreate, 
    db: AsyncIOMotorDatabase = Depends(get_client)
) -> Dict[str, Any]:    
    if not UserCreate.validate_obj(body):
        raise HTTPException(status_code=400, detail='Invalid request body or missing params')
    
    user_service: UserService = UserService(db)
    await user_service.register_default(body)
    
    return {
        'code': 201,
        'message': '',
        'body': {}
    }