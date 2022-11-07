from fastapi import APIRouter
from api.routes.users import router as register
from api.routes.healthiness import healthiness
from api.routes.posts import post_router

router = APIRouter()
router.include_router(register, prefix='/user', tags=['users'])
router.include_router(healthiness, prefix='/check', tags=['healthiness'])
router.include_router(post_router, prefix='/posts', tags=['posts'])
