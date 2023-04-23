from typing import List, Optional
from bson import ObjectId
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from pymongo.errors import DuplicateKeyError

from src.domain.user.model import User

class UserRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db: AsyncIOMotorDatabase = db['user']
        self.db.create_index('username', unique=True)
        self.db.create_index('email', unique=True)
        
    async def find(self, username: str) -> Optional[User]:
        data: User = await self.db.find_one({'username': username})
        return data if data else None
    
    async def find_all(self) -> Optional[List[User]]:
        data: List[User] = await self.db.find().to_list(length=None)
        return data if data else None
    
    async def find_by_email(self, email: str) -> Optional[User]:
        data: User = await self.db.find_one({'email': email})
        return data if data else None
    
    async def find_by_id(self, user_id: ObjectId) -> Optional[User]:
        data: User = await self.db.find_one({'_id': user_id})
        return data if data else None
    
    async def create(self, user: dict) -> None:
        try:
            await self.db.insert_one(user)
        except DuplicateKeyError:
            raise HTTPException(status_code=400, detail='Username or email already exists')
        
        