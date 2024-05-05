from functools import wraps
from flask import request
from domain.access.access_interface import IAccess
from kink import di


def verifyAccessToken(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        access = di[IAccess]
        access_token = request.headers.get("Access-token")
        verification = access.verifyAccessToken(access_token)
        return func(*args, **kwargs)

    return wrapper


def verifyContributor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        access = di[IAccess]
        repo_path = kwargs.get('repo_path')
        access_token = request.headers.get("Access-token")
        verification = access.verifyContributor(access_token, repo_path)
        return func(*args, **kwargs)

    return wrapper


def verifyCreator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        access = di[IAccess]
        repo_path = kwargs.get('repo_path')
        access_token = request.headers.get("Access-token")
        verification = access.verifyCreator(access_token, repo_path)
        return func(*args, **kwargs)

    return wrapper


def verifyCanCreate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        access = di[IAccess]
        access_token = request.headers.get("Access-token")
        verification = access.verifyCanCreate(access_token)
        return func(*args, **kwargs)

    return wrapper


def verifyAdmin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        access = di[IAccess]
        access_token = request.headers.get("Access-token")
        verification = access.verifyAdmin(access_token)
        return func(*args, **kwargs)

    return wrapper
