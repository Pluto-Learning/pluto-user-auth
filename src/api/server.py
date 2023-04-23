from fastapi import APIRouter, FastAPI

from src.infastructure.config.environment.base import settings
from src.api.endpoints import base, user

def load_routes() -> APIRouter:
    router: APIRouter = APIRouter(prefix=settings.API_PREFIX)
    router.include_router(router=base.router)
    router.include_router(router=user.router, prefix='/user')
    return router

def init_api() -> FastAPI:
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        description=settings.DESCRIPTION
    )

    app_router = load_routes()
    app.include_router(router=app_router)
    
    return app
