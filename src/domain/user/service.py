from typing import Optional
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase

from src.domain.user.model import User, UserCreate
from src.domain.user.repository import UserRepository
from src.infastructure.security.password import hash_psw

class UserService:
    def __init__(self, db: AsyncIOMotorDatabase):
        repo: UserRepository = UserRepository(db=db)
        self.repo: UserRepository = repo
        
    async def user(self, username: str) -> Optional[User]:
        return await self.repo.find(username)
    
    async def user_by_email(self, email: str) -> Optional[User]:
        return await self.repo.find_by_email(email)
    
    async def user_by_id(self, user_id: str) -> Optional[User]:
        conv_id: ObjectId = ObjectId(user_id)
        return await self.repo.find_by_id(conv_id)
        
    async def register_default(self, user: UserCreate) -> None:
        hashed_psw: bytes = hash_psw(user.password)
        new_user = {
            'username': user.username,
            'email': user.email,
            'password': hashed_psw,
            'pnumber': user.pnumber,
            'fName': user.fName,
            'lName': user.lName,
            'address': user.address,
            'uType': user.uType,
        }
        await self.repo.create(new_user)
