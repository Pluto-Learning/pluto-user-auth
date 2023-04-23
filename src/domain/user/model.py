from ast import Dict
from bson import ObjectId
from typing import Any, Optional
from pydantic import BaseModel, EmailStr, Field

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise TypeError('ObjectId required')
        return str(v)

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    pnumber: str
    fName: str
    lName: str
    address: str
    uType: Optional[str] = 'free'
    
    @staticmethod
    def validate_obj(obj: 'UserCreate', **kwargs) -> bool:
        if not obj:
            return False
        
        obj_encoded: Dict[str, Any] = obj.dict()
        
        for key in obj_encoded.keys():
            if not obj_encoded[key]:
                return False
            
        return True
    
class UserRes(BaseModel):
    id: PyObjectId = Field(alias="_id")
    username: str
    email: EmailStr
    pnumber: str
    fName: str
    lName: str
    address: str
    uType: Optional[str] = 'free'
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = { ObjectId: str }
    
class User(UserCreate):
    _id: PyObjectId
    password: bytes

def parse_user(obj: User, **kwargs) -> UserRes:
    return UserRes(
        id=obj['_id'],
        username=obj['username'],
        email=obj['email'],
        pnumber=obj['pnumber'],
        fName=obj['fName'],
        lName=obj['lName'],
        address=obj['address'],
        uType=obj['uType'],
    )