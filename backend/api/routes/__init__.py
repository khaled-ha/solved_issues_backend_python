from fastapi import APIRouter
from api.routes.users import router as register

router = APIRouter()
router.include_router(register, prefix="/user", tags=["users"])