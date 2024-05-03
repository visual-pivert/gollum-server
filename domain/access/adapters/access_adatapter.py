import datetime
import json
import base64
from random import randint
from domain.access.access_interface import IAccess
from domain.user.user_model_interface import IUserModel
from domain.access.exceptions.access_exception import AccessException
from domain.user.exceptions.user_exception import UserNotFoundException
from domain.security.security_interface import ISecurity
from domain.access.exceptions.access_exception import InvalidAccessTokenException
from kink import inject


class AccessAdapter(IAccess):

    @inject
    def __init__(self, user_model: IUserModel, security: ISecurity):
        self.user_model = user_model
        self.security = security

    def accessToken(self, username: str, password: str) -> str:
        try:
            user = self.user_model.getUserBy('username', username)
            if user and self.security.checkPassword(password, user.password):
                obj = {'username': username}
                token = self.generateToken(obj)
                self.user_model.updateAccessToken(username, token)
                return token
        except UserNotFoundException as e:
            raise AccessException()

    def revokeAccessToken(self, access_token: str):
        user = self.user_model.getUserBy('access_token', access_token)
        if user:
            self.user_model.updateAccessToken(user.username, None)

    def verifyAccessToken(self, access_token: str) -> bool:
        if access_token:
            return True
        raise InvalidAccessTokenException()

    def generateToken(self, obj: dict) -> str:
        timestamp = int(datetime.datetime.now().timestamp())
        obj['_id'] = randint(10000, 99999)
        obj['_timestamp'] = timestamp

        jsoned = json.dumps(obj).encode('utf-8')

        return base64.urlsafe_b64encode(jsoned).decode('utf-8')
