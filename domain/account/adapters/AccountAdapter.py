from domain.account.IAccount import IAccount
from domain.account.AccountEntity import AccountEntity
from domain.auth.UserEntity import UserEntity
import bcrypt
import sqlite3
import datetime
from kink import inject


class AccountAdapter(IAccount):

    @inject
    def __init__(self, database):
        self.database = database

    def createAccount(self, account: AccountEntity) -> "UserEntity":
        connector = self.database
        cursor = connector.cursor()
        query = "INSERT INTO Users(username, created_at, password, email, slug) VALUES(?, ?, ?, ?, ?)"
        timestamp = datetime.datetime.now().timestamp()

        # cyphered_password -> str
        cyphered_password = bcrypt.hashpw(account.password.encode('utf8'), bcrypt.gensalt()).decode("utf-8")
        try:
            cursor.execute(query, (account.username, timestamp, cyphered_password, account.email, account.username))
        except sqlite3.IntegrityError as e:
            if 'username' in e.args[0]:
                raise Exception("Ce nom d'utilisateur est déjà utilisé, veuillez en choisir un autre.")
            if 'email' in e.args[0]:
                raise Exception("L'adresse e-mail que vous avez entrée est déjà associée à un compte")
        last_id = cursor.lastrowid
        connector.commit()

        # Creation de l'utilisateur
        user = UserEntity()
        user.id = last_id
        user.username = account.username
        user.slug = account.username
        user.email = account.email,
        user.created_at = timestamp
        user.password = cyphered_password
        user.meta = {}

        return user
