from fastapi import APIRouter, HTTPException, Request
from typing import Dict, Any, List

from src.api.endpoints.wrapper import ResBody
from src.domain.user.model import User, UserCreate, UserRes, parse_user
from src.domain.user.service import UserService
from src.infastructure.security.password import validate_psw

router = APIRouter()

@router.get(
    path='/', 
    status_code=200, 
    response_model=ResBody
)
async def user_handler(req: Request, username: str) -> Dict[str, Any]:
    if not username:
        raise HTTPException(status_code=400, detail='Invalid username param')
    
    user_service: UserService = UserService(req.app.db)
    user: User = await user_service.user(username)
    
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    return {
        'code': 200,
        'message': '',
        'body': parse_user(user)
    }

@router.get(
    path='/all/',
    status_code=200,
    response_model=ResBody
)
async def users_handler(req: Request) -> Dict[str, Any]:
    user_service: UserService = UserService(req.app.db)
    users: List[User] = await user_service.user_all()
    
    if not users:
        return {
            'code': 200,
            'message': 'No users found',
            'body': []
        }
    
    out: List[UserRes] = [parse_user(user) for user in users]
    return {
        'code': 200,
        'message': '',
        'body': out
    }

@router.get(
    path='/login/', 
    status_code=200, 
    response_model=ResBody
)
async def login_handler(req: Request, username: str, password: str) -> Dict[str, Any]:
    user_service: UserService = UserService(req.app.db)
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
async def register_handler(req: Request, body: UserCreate) -> Dict[str, Any]:    
    if not UserCreate.validate_obj(body):
        raise HTTPException(status_code=400, detail='Invalid request body or missing params')
    
    user_service: UserService = UserService(req.app.db)
    await user_service.register_default(body)
    
    return {
        'code': 201,
        'message': '',
        'body': {}
    }