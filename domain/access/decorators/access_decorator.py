from functools import wraps
from flask import request
from domain.access.access_interface import IAccess
from kink import di


def verifyAccessToken(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        access = di[IAccess]
        access_token = request.headers.get("Access-token")
        verification = False
        verification = access.verifyAccessToken(access_token)
        return func(*args, **kwargs)

    return wrapper
