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
from domain.contrib.contrib_interface import IContrib
from kink import inject
import binascii


class AccessAdapter(IAccess):

    @inject
    def __init__(self, user_model: IUserModel, security: ISecurity, contrib: IContrib):
        self.user_model = user_model
        self.security = security
        self.contrib = contrib

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
        decoded_access_token = self.decodeAccessToken(access_token)
        if 'username' in decoded_access_token.keys():
            return True
        raise InvalidAccessTokenException()

    def verifyContributor(self, access_token: str, repo_path: str) -> bool:
        decoded_access_token = self.decodeAccessToken(access_token)
        if decoded_access_token["username"] in self.contrib.listContrib(repo_path):
            return True
        raise InvalidAccessTokenException()

    # cette fonction permet de verifier si la personne est le creator du repo
    def verifyCreator(self, access_token: str, repo_path: str) -> bool:
        decoded_access_token = self.decodeAccessToken(access_token)
        print(self.contrib.listContrib(repo_path))
        if decoded_access_token["username"] == self.contrib.listContrib(repo_path)[0]:
            return True
        raise InvalidAccessTokenException()

    # Cette fonction permet de verifier si la personne peut creer des repo
    # TODO: mettre en place lorsque le base de donnée est modifier
    def verifyCanCreate(self, access_token:str):
        decoded_access_token = self.decodeAccessToken(access_token)
        user = self.user_model.getUserBy('username', decoded_access_token['username'])
        if user.can_create > 0:
            return True
        raise InvalidAccessTokenException()


    def verifyAdmin(self, access_token: str) -> bool:
        decoded_access_token = self.decodeAccessToken(access_token)
        user = self.user_model.getUserBy('username', decoded_access_token['username'])
        if user.can_create >= 2:
            return True
        raise InvalidAccessTokenException()


    def generateToken(self, obj: dict) -> str:
        timestamp = int(datetime.datetime.now().timestamp())
        obj['_id'] = randint(10000, 99999)
        obj['_timestamp'] = timestamp

        jsoned = json.dumps(obj).encode('utf-8')

        return base64.urlsafe_b64encode(jsoned).decode('utf-8')

    def decodeAccessToken(self, access_token: str) -> dict:
        if access_token:
            try:
                return dict(json.loads(base64.urlsafe_b64decode(access_token).decode('utf-8')))
            except binascii.Error as e:
                raise InvalidAccessTokenException()
        else:
            raise InvalidAccessTokenException()
