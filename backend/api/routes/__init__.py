from fastapi import APIRouter
from api.routes.users import router as register
from api.routes.healthiness import healthiness

router = APIRouter()
router.include_router(register, prefix="/user", tags=["users"])
router.include_router(healthiness, prefix='/check', tags=['healthiness'])