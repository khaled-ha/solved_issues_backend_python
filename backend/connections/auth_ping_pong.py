from requests import get


def check_auth_server():
    try:
        res = get('http://auth:8002/auth/check/ping')
        return res.json()
    except ConnectionError as connection_error:
        return {'connection_error': connection_error}
    except Exception as e:
        print(e)
