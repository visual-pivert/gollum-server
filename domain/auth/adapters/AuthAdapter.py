from domain.auth.IAuth import IAuth
from domain.auth.UserEntity import UserEntity
from domain.auth.exceptions.LoginException import LoginException
from kink import inject
import json
from random import randint
import datetime
import base64
import bcrypt


class AuthAdapter(IAuth):
    @inject
    def __init__(self, database):
        self.database = database

    def login(self, username: str, password: str, remember: bool):
        user_who_log = self.getUserBy('username', username)
        exp_date = int(datetime.datetime.now().timestamp()) + datetime.timedelta(days=3).seconds
        if user_who_log and self.verifyPassword(password, user_who_log.password):
            access_token = self.createJwt({'username': username, 'exp_date': exp_date})
            # update de l'access token dans la base de donnee
            self.updateAccessToken(username, access_token)
            out = {
                'username': username,
                'email': user_who_log.email,
                'access_token': access_token
            }
            return out
        else:
            raise LoginException("Nom d'utilisateur ou mot de passe incorrecte")

    def logout(self, access_token=""):
        # suppression de l'access token
        user_who_logged_out = self.getUserBy('access_token', access_token)
        self.updateAccessToken(user_who_logged_out.username, None)

    def loggedUser(self) -> UserEntity | None:
        pass

    def createJwt(self, data: dict) -> str:
        timestamp = int(datetime.datetime.now().timestamp())
        data['_id'] = randint(10000, 99999)
        data['_timestamp'] = timestamp

        # Conversion string -> bytes pour b64encode
        jsoned = json.dumps(data).encode('utf-8')

        # Conversion Bytes -> string
        return base64.urlsafe_b64encode(jsoned).decode('utf-8')

    def getUserBy(self, field: str, value: any) -> UserEntity:
        connector = self.database
        cursor = connector.cursor()

        query = "SELECT * FROM Users WHERE {} = ?".format(field)
        cursor.execute(query, (value,))

        user_fetched = cursor.fetchone()

        user = UserEntity.makeUser(user_fetched) if user_fetched else None
        return user

    def updateAccessToken(self, username: str, access_token: str|None):
        connector = self.database
        cursor = connector.cursor()

        query = "UPDATE Users SET access_token = ? WHERE username = ?"
        cursor.execute(query, (access_token, username))

        connector.commit()

    def verifyPassword(self, password: str, hashed_password: str) -> bool:
        _password = bcrypt.hashpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
        return hashed_password.encode('utf-8') == _password
