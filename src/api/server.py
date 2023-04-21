from fastapi import APIRouter, FastAPI

from src.infastructure.config.environment.base import settings
from src.api.endpoints import base

def load_routes(router: APIRouter) -> APIRouter:
    router.include_router(router=base.router)
    return router

def init_api() -> FastAPI:
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        description=settings.DESCRIPTION
    )
    
    api_router = APIRouter(prefix=settings.API_PREFIX)
    app_router = load_routes(api_router)
    app.include_router(router=app_router)
    
    return app
