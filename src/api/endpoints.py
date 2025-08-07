from fastapi import APIRouter

from src.api.routes.health import router as api_health_router
from src.api.routes.v1.cast import router as api_cast_router

router = APIRouter()

router.include_router(router=api_health_router)
router.include_router(router=api_cast_router)