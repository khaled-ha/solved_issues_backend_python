import hashlib
from enum import Enum
from requests import post, get, put, patch
from json import dumps
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Mapping, Optional


def get_hashed_password(password: str):
    return hashlib.sha256(password.encode())


class RESTMethod(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'

    def __str__(self):
        obj_str = repr(self)
        return obj_str

    def __repr__(self):
        return self.value


@dataclass
class RESTRequest:
    method: RESTMethod
    url: Optional[str] = None
    endpoint_url: Optional[str] = None
    params: Optional[Mapping[str, str]] = None
    data: Any = None
    headers: Optional[Mapping[str, str]] = None
    is_auth_required: bool = False
    throttler_limit_id: Optional[str] = None
