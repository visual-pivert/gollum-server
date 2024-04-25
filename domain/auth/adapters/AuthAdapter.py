from domain.auth.IAuth import IAuth
from domain.auth.UserEntity import UserEntity
from flask import session
from kink import inject


class AuthAdapter(IAuth):
    @inject
    def __init__(self, database):
        self.database = database

    def login(self, username: str, password: str, remember: bool):
        pass

    def logout(self): pass

    def loggedUser(self) -> "UserEntity": pass

    def createJwt(self, data: dict) -> str:
        pass

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


