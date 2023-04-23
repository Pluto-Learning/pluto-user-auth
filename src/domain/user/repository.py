from typing import Optional
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase

from src.domain.user.model import User

class UserRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db: AsyncIOMotorDatabase = db['user']
        self.db.create_index("username", unique=True)
        self.db.create_index("email", unique=True)
        
    async def find(self, username: str) -> Optional[dict]:
        data: User = await self.db.find_one({"username": username})
        return User.parse_obj(data) if data else None
    
    async def find_by_email(self, email: str) -> Optional[dict]:
        data: User = await self.db.find_one({"email": email})
        return User.parse_obj(data) if data else None
    
    async def find_by_id(self, user_id: str) -> Optional[dict]:
        data: User = await self.db.find_one({"_id": ObjectId(user_id)})
        return User.parse_obj(data) if data else None
    
    async def create(self, user: User) -> User:
        return
        
        