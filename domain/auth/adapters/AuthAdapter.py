from domain.auth.IAuth import IAuth
from domain.auth.UserEntity import UserEntity
from domain.auth.exceptions.LoginException import LoginException
from flask import session
from kink import inject, di
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
            session['access_token'] = self.createJwt({'username': username, 'exp_date': exp_date})
        else:
            raise LoginException("Vérifier le nom d'utilisateur ou le mot de passe")

    def logout(self):
        # Is logged in?
        if "access_token" in session.keys():
            session.pop('access_token')

    def loggedUser(self) -> UserEntity | None:
        access_token = session['access_token'] if ('access_token' in session.keys()) else ""
        if access_token:
            json_data = base64.urlsafe_b64decode(access_token)
            data = json.loads(json_data)
            user = self.getUserBy('username', data["username"])
            return user
        return None

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

    def verifyPassword(self, password: str, hashed_password: str) -> bool:
        _password = bcrypt.hashpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
        return hashed_password.encode('utf-8') == _password
