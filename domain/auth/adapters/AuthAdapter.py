from domain.auth.IAuth import IAuth
from domain.auth.UserEntity import UserEntity
from flask import session
from kink import inject
import json
from random import randint
import datetime
import base64


class AuthAdapter(IAuth):
    @inject
    def __init__(self, database):
        self.database = database

    def login(self, username: str, password: str, remember: bool):
        pass

    def logout(self): pass

    def loggedUser(self) -> "UserEntity": pass

    def createJwt(self, data: dict) -> str:
        timestamp = datetime.datetime.now().timestamp()
        data['_id'] = randint(10000, 99999)
        data['_timestamp'] = timestamp
        jsoned = json.dumps(data).encode('utf-8')
        return str(base64.urlsafe_b64encode(jsoned))

    def getUserBy(self, field: str, value: any) -> UserEntity:
        connector = self.database
        cursor = connector.cursor()

        query = "SELECT * FROM Users WHERE ?=?"
        cursor.execute(query, (field, value))

        user_fetched = cursor.fetchone()

        connector.commit()
        connector.close()

        user = UserEntity.makeUser(user_fetched)
        return user
