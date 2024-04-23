from domain.account.IAccount import IAccount
from domain.account.AccountEntity import AccountEntity
from domain.auth.UserEntity import UserEntity
import sqlite3
import datetime


class AccountAdapters(IAccount):

    @staticmethod
    def createAccount(account: AccountEntity) -> "UserEntity":
        connector = sqlite3.connect("/home/gollum/Project/gollum/var/database.db")
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
