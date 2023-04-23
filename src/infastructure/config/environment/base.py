import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    TITLE: str = "Pluto Core API"
    VERSION: str = "0.1.0"
    DESCRIPTION: str | None = ""
    DEBUG: bool = False
    API_PREFIX: str = "/api/v1"

    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://0.0.0.0:3000",
        "http://127.0.0.1:3000",
    ]
    ALLOWED_METHODS: list[str] = ["*"]
    ALLOWED_HEADERS: list[str] = ["*"]
    
    MONGO_URL: str = os.getenv("MONGO_URL")
    SALT: str = os.getenv("SALT")
    JWT_KEY: str = os.getenv("JWT_KEY")
    
settings: Settings = Settings()