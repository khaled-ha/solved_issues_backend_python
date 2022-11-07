from fastapi import APIRouter
from requests import get
from requests.exceptions import ConnectionError

healthiness = APIRouter()


@healthiness.get('/ping')
def pong():
    try:
        res = get('http://auth:8002/auth/check/ping')
        return res.json()
    except ConnectionError as connection_error:
        return {'connection_error': connection_error}
    except Exception as e:
        print(e)
