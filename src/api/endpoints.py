from fastapi import APIRouter

from src.api.routes.health import router as api_health_router

router = APIRouter()

router.include_router(router=api_health_router)