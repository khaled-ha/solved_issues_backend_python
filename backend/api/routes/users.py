from fastapi import status, Request, Depends
from fastapi.exceptions import HTTPException
from validators.users_validator import RegistrationUserResponse, UserCreate, UserLogin, NotFoundResponse
from sqlalchemy.orm import Session 
from sqlalchemy.exc import SQLAlchemyError
from connections.session import get_db_session
from connections.auth_ping_pong import check_auth_server
from auth_server.users import UserApi
from utils import get_hashed_password
from fastapi import APIRouter
import json

from logging import getLogger

logger = getLogger(__name__)

router = APIRouter()

@router.post(
    '/register',
    status_code=status.HTTP_201_CREATED,
    response_model=RegistrationUserResponse,
    responses={
    status.HTTP_201_CREATED: {
        "model": RegistrationUserResponse,
        "description": "Created User ",
    },
    status.HTTP_404_NOT_FOUND: {
        "model": NotFoundResponse,
        "description": "Server not found",
    },
    },
)
async def register(
    request : Request,
    user_credential : UserCreate,
    db: Session = Depends(get_db_session),
    # auth_server : dict = Depends(check_auth_server)
):
    try:
        print('started')
        resp = UserApi.post(
            url='http://auth:8002/auth/user/register', 
            data = json.dumps(
                {
                    'email': user_credential.email,
                    'password': get_hashed_password(user_credential.password).hexdigest(),
                    'is_verified': True
                }
            )
        )
        print(resp)
    except Exception as e:
        raise e
    # session = get_db_session()()
    # email = session.query(User).filter(User.email==user_credential.email).first()
    # if email is not None:
    #     raise HTTPException(
    #         detail='Email already registered',
    #         status_code= status.HTTP_409_CONFLICT
    #         )
    # hashed_password = get_hashed_password(user_credential.password).hexdigest()
    # # import ipdb;ipdb.set_trace()
    # try:
    #     user = User(
    #                 # first_name =user_credential.first_name,   
    #                 # last_name= user_credential.last_name,   
    #                 email = user_credential.email,   
    #                 password = hashed_password
    #             )
    #     session.add(user)
    #     session.commit()
    #     return { "message": "User registration successful"}
    # except SQLAlchemyError as e:
    #     logger.warn(e)
    #     session.rollback()*
    pass


@router.post(
    '/login/',
    status_code=status.HTTP_200_OK
)
async def login(request: Request, user_credential: UserLogin, db: Session=Depends(get_db_session)):
    password = get_hashed_password(user_credential.password).hexdigest()
    # user = db.query(User).filter(User.email==user_credential.email, User.password==password).first()
    # if not user:
    #     raise HTTPException(
    #         status_code= status.HTTP_401_UNAUTHORIZED,
    #         detail= "Invalid Username or Password",
    #         headers={"WWW-Authenticate":"Bearer"
    #         })
    # if user.is_verified!=True:
    #     raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,detail= "Account Not Verified")
    
    # access_token = create_access_token(data={'user_id':user.id})
    # return {'access_token':access_token,'token_type': 'bearer'}
