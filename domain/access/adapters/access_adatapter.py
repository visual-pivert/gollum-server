import datetime
import json
import base64
from random import randint
from domain.access.access_interface import IAccess
from domain.user.user_model_interface import IUserModel
from domain.security.security_interface import ISecurity
from kink import inject


class AccessAdapter(IAccess):

    @inject
    def __init__(self, user_model: IUserModel, security: ISecurity):
        self.user_model = user_model
        self.security = security

    def accessToken(self, username: str, password: str) -> str:
        user = self.user_model.getUserBy('username', username)
        if user and self.security.checkPassword(password, user.password):
            obj = {'username': username}
            token = self.generateToken(obj)
            self.user_model.updateAccessToken(username, token)
            return token
        return ''

    def revokeAccessToken(self, access_token: str):
        user = self.user_model.getUserBy('access_token', access_token)
        if user:
            self.user_model.updateAccessToken(user.username, None)

    def verifyAccessToken(self, access_token: str) -> bool:
        pass

    def generateToken(self, obj: dict) -> str:
        timestamp = int(datetime.datetime.now().timestamp())
        obj['_id'] = randint(10000, 99999)
        obj['_timestamp'] = timestamp

        jsoned = json.dumps(obj).encode('utf-8')

        return base64.urlsafe_b64encode(jsoned).decode('utf-8')
