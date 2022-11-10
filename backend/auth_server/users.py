from enum import Enum
from requests import post, get, put, patch
from json import dumps
from validators.users_validator import UserCreate
from abstract.baseapi import BaseAPI
from utils import RESTMethod, RESTRequest


def _jsonify_user(user) -> dict:
    return {
        'email': user.email,
        'password': user.password,
        'is_verified': user.is_verified,
    }


class UserApi(BaseAPI):
    def __init__(self):
        self.headers = self.DEFAULT_HEADERS

    @staticmethod
    def register_user(url, data, headers=None, params=None):
        RESTRequest(
            method=RESTMethod.POST,
            url=url,
            params=params,
            data=data,
            headers=headers,
        )
        post(
            url=url,
            data=dumps(data),
            headers=headers,
        )
