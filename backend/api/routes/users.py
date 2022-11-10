from fastapi import status, Request, Depends
from validators.users_validator import (
    RegistrationUserResponse,
    UserCreate,
    UserLogin,
    NotFoundResponse,
)
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
            'model': RegistrationUserResponse,
            'description': 'Created User ',
        },
        status.HTTP_404_NOT_FOUND: {
            'model': NotFoundResponse,
            'description': 'Server not found',
        },
    },
)
async def register(
    request: Request,
    user_credential: UserCreate,
):
    try:
        print('started')
        resp = UserApi.register_user(
            url='http://auth:8002/auth/user/register',
            data=json.dumps(
                {
                    'email': user_credential.email,
                    'password': get_hashed_password(
                        user_credential.password
                    ).hexdigest(),
                    'is_verified': True,
                }
            ),
        )
        print(resp)
    except Exception as e:
        raise e


@router.post('/login/', status_code=status.HTTP_200_OK)
async def login(request: Request, user_credential: UserLogin):
    password = get_hashed_password(user_credential.password).hexdigest()
