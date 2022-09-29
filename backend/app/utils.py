import hashlib


def get_hashed_password(password: str):
    return hashlib.sha256(password.encode())