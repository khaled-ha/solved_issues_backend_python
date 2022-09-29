from fastapi import status, Request, Depends
from fastapi.exceptions import HTTPException
from app.validators.users_validator import RegistrationUserResponse, UserCreate
from sqlalchemy.orm import Session 
from sqlalchemy.exc import SQLAlchemyError
from app.connections.session import get_db_session
from app.models.users import User
from app.utils import get_hashed_password
from fastapi import APIRouter

from logging import getLogger

logger = getLogger(__name__)

router = APIRouter()

@router.post(
    '/register',
    status_code=status.HTTP_201_CREATED,
    response_model=RegistrationUserResponse,
)
async def register(
    request : Request,
    user_credential : UserCreate,
    db: Session = Depends(get_db_session)
):
    session = get_db_session() 
    email = session.query(User).filter(User.email==user_credential.email).first()
    if email != None:
        raise HTTPException(
            detail='Email already registered',
            status_code= status.HTTP_409_CONFLICT
            )
    hashed_password = get_hashed_password(user_credential.password).hexdigest()
    import ipdb;ipdb.set_trace()
    try:
        user = User(
                    # first_name =user_credential.first_name,   
                    # last_name= user_credential.last_name,   
                    email = user_credential.email,   
                    password = hashed_password
                )
        session.add(user)
        session.commit()
        return { "message": "User registration successful"}
    except SQLAlchemyError as e:
        logger.warn(e)
        session.rollback()