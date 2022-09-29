from fastapi import APIRouter
from app.api.routes.cleaning import router as cleanings_router
from app.api.routes.users import router as register

router = APIRouter()
router.include_router(cleanings_router, prefix="/cleanings", tags=["cleanings"])
router.include_router(register, prefix="/user", tags=["users"])