from domain.account.IAccount import IAccount
from domain.account.AccountEntity import AccountEntity
from domain.auth.UserEntity import UserEntity
import sqlite3
import datetime
from kink import inject


class AccountAdapters(IAccount):

    @inject
    def __init__(self, database):
        self.database = database

    def createAccount(self, account: AccountEntity) -> "UserEntity":
        connector = self.database
        cursor = connector.cursor()
        query = "INSERT INTO Users(username, created_at, password, email, slug) VALUES(?, ?, ?, ?, ?)"
        timestamp = datetime.datetime.now().timestamp()
        cursor.execute(query, (account.username, timestamp, account.password, account.email, account.username))
        last_id = cursor.lastrowid
        connector.commit()

        # Creation de l'utilisateur
        user = UserEntity()
        user.id = last_id
        user.username = account.username
        user.slug = account.username
        user.email = account.email,
        user.created_at = timestamp
        user.meta = {}

        return user
