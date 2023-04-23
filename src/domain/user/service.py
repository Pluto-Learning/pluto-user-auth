from typing import Optional
from motor.motor_asyncio import AsyncIOMotorDatabase
import uuid

from src.domain.user.model import User, UserCreate
from src.domain.user.repository import UserRepository
from src.infastructure.security.password import hash_psw

class UserService:
    def __init__(self, db: AsyncIOMotorDatabase):
        user_repository: UserRepository = UserRepository(db=db)
        self.user_repository: UserRepository = user_repository
        
    async def user(self, username: str) -> Optional[dict]:
        return await self.user_repository.find(username)
    
    async def user_by_email(self, email: str) -> Optional[dict]:
        return await self.user_repository.find_by_email(email)
    
    async def user_by_id(self, user_id: str) -> Optional[dict]:
        return await self.user_repository.find_by_id(user_id)
        
    async def register_default(self, user: UserCreate) -> User:
        new_uuid: uuid.UUID = uuid.uuid4()
        hashed_psw: bytes = hash_psw(user.password)
        
        new_user: User = User(
            **user.dict(), 
            id=new_uuid, 
            password=hashed_psw
        )
        
        return await self.user_repository.create(new_user)
