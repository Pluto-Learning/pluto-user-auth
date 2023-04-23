from bson import ObjectId
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import Optional

from src.domain.user import User
from src.infastructure.database.mongo import get_client
from src.infastructure.security.auth.token import decode_token

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_server_user(
    token: Depends(oauth_scheme), 
    db: AsyncIOMotorDatabase = Depends(get_client)
) -> Optional[User]:
    payload: dict = decode_token(token)
    user_id: str = payload.get('sub')
    
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    
    user = await db['user'].find_one({'_id': ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    
    return user

async def is_admin(user: User = Depends(get_server_user)) -> User:
    if user.utype != 'admin':
        raise HTTPException(status_code=401, detail="Invalid authentication token")
    
    return user