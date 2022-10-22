from enum import Enum
from requests import post, get, put, patch
from json import dumps
from dataclasses import dataclass
from validators.users_validator import RegistrationUserResponse, UserCreate, UserLogin
from typing import TYPE_CHECKING, Any, Mapping, Optional
from abstract.baseapi import BaseAPI
from utils import RESTMethod, RESTRequest


def _jsonify_user(user) -> dict:
    return {
        'email': user.email,
        'password': user.password,
        'is_verified': user.is_verified
    }


class UserApi(BaseAPI):

    def __init__(self):
        self.headers = self.DEFAULT_HEADERS
    
    def post(self, url, data, headers, params):
        rest_request = RESTRequest(
            method=RESTMethod.POST,
            url=url,
            params=params,
            data=data,
            headers=headers,
        )
        post(
            url=url,
            data=dumps(data),
            headers=self.headers,
        )
        
    

def register_user(user: UserCreate) -> dict:
    jsonified_user = _jsonify_user(user)

    # request = RESTRequest(
    #         method=RESTMethod.POST,
    #         url='http://localhost:8002',
    #         data=jsonified_user,
    #     )
    


def get_user():
    pass
