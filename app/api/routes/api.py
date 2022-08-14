from fastapi import APIRouter
from app.api.routes.service_info import service_info
from app.api.routes.job import job

router = APIRouter()
router.include_router(router=service_info)
router.include_router(router=job)
