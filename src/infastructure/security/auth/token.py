from datetime import timedelta
from fastapi import HTTPException
import datetime
import jwt

from src.infastructure.config.environment.base import settings

def generate_token(data: dict) -> str:
    data_copy: dict = data.copy()
    data_copy.update({'exp': datetime.utcnow() + timedelta(days=1)})
    return jwt.encode(data_copy, settings.JWT_KEY, algorithm='HS256')

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.JWT_KEY, algorithms=["HS256"])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")