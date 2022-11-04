from fastapi import status, Request, Depends
from fastapi.exceptions import HTTPException
from validators.users_validator import RegistrationUserResponse, UserCreate, UserLogin
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from connections.session import get_db_session
from backend.models.posts import User
from utils import get_hashed_password
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
    request: Request, user_credential: UserCreate, db: Session = Depends(get_db_session)
):
    session = get_db_session()()
    email = session.query(User).filter(User.email == user_credential.email).first()
    if email is not None:
        raise HTTPException(
            detail='Email already registered', status_code=status.HTTP_409_CONFLICT
        )
    hashed_password = get_hashed_password(user_credential.password).hexdigest()
    # import ipdb;ipdb.set_trace()
    try:
        user = User(
            # first_name =user_credential.first_name,
            # last_name= user_credential.last_name,
            email=user_credential.email,
            password=hashed_password,
        )
        session.add(user)
        session.commit()
        return {'message': 'User registration successful'}
    except SQLAlchemyError as e:
        logger.warn(e)
        session.rollback()


@router.post('/login/', status_code=status.HTTP_200_OK)
async def login(
    request: Request, user_credantial: UserLogin, db: Session = Depends(get_db_session)
):
    password = get_hashed_password(user_credantial.password).hexdigest()
    user = (
        db.query(User)
        .filter(User.email == user_credantial.email, User.password == password)
        .first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid Username or Password',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    if user.is_verified != True:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Account Not Verified'
        )

    access_token = create_access_token(data={'user_id': user.id})
    return {'access_token': access_token, 'token_type': 'bearer'}
