from ast import Dict
import bson
from typing import Any, Optional
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: bytes
    pnumber: str
    fName: str
    lName: str
    address: str
    uType: Optional[str] = 'free'
    
class User(UserCreate):
    _id: bson.ObjectId
    
    @staticmethod
    def parse_obj(obj: 'User', **kwargs) -> dict:
        return {
            '_id': str(obj['_id']),
            'username': obj['username'],
            'email': obj['email'],
            'pnumber': obj['pnumber'],
            'fName': obj['fName'],
            'lName': obj['lName'],
            'address': obj['address'],
            'uType': obj['uType'],
        }
