from typing import Any, Dict
from pydantic import BaseModel

from src.domain.user.model import UserRes

class ResBody(BaseModel):
    code: int
    message: str
    body: UserRes | Any | Dict[str, Any]
    