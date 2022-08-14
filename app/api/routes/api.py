from fastapi import APIRouter
from app.api.routes.service_info import service_info

router = APIRouter()
router.include_router(router=service_info)
