from backend.app.api.server import app
from fastapi import status, Request, Depends
from backend.app.validators.users_validator import RegistrationUserResponse, UserCreate
from sqlalchemy.orm import Session 
from app.connections.session import get_db_session 

@app.post(
    '/register', 
    status_code=status.HTTP_201_CREATED,
    response_model=RegistrationUserResponse,
)
async def register(
    request : Request,
    user_credential : UserCreate,
    db: Session = Depends(get_db_session)
):
    email = None
