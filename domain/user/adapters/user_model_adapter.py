from domain.user.user_model_interface import IUserModel
from domain.user.user_entity import UserEntity
from domain.user.exceptions.user_exception import UsernameNotUniqueException, EmailNotUniqueException, UserNotFoundException
from kink import inject
from sqlite3 import IntegrityError
import bcrypt
import datetime


class UserModelAdapter(IUserModel):

    @inject
    def __init__(self, database):
        self.database = database

    def getUserBy(self, field: str, value: str) -> UserEntity:
        connector = self.database
        cursor = connector.cursor()

        query = "SELECT * FROM Users WHERE {} = ?".format(field)
        cursor.execute(query, (value,))

        user_fetched = cursor.fetchone()

        if not user_fetched:
            raise UserNotFoundException()

        user = self.makeUser(user_fetched) if user_fetched else None
        return user

    def updateAccessToken(self, username: str, new_access_token: str | None):
        connector = self.database
        cursor = connector.cursor()

        query = "UPDATE Users SET access_token = ? WHERE username = ?"
        cursor.execute(query, (new_access_token, username))
        connector.commit()

    def listUser(self) -> [UserEntity]:
        connector = self.database
        cursor = connector.cursor()

        query = "SELECT * FROM Users"
        cursor.execute(query)

        users = cursor.fetchall()

        if not users:
            raise UserNotFoundException()

        the_users = []
        for user in users:
            the_users.append(self.makeUser(user))
        return the_users

    def addUser(self, user: UserEntity) -> int:
        connector = self.database
        cursor = connector.cursor()
        query = "INSERT INTO Users(username, created_at, password, email, slug, access_token) VALUES(?, ?, ?, ?, ?, ?)"
        timestamp = datetime.datetime.now().timestamp()

        # cyphered_password -> str
        cyphered_password = bcrypt.hashpw(user.password.encode('utf8'), bcrypt.gensalt()).decode("utf-8")
        try:
            cursor.execute(query, (user.username, timestamp, cyphered_password, user.email, user.username,
                                   user.access_token))
        except IntegrityError as e:
            if 'username' in e.args[0]:
                raise UsernameNotUniqueException()
            if 'email' in e.args[0]:
                raise EmailNotUniqueException()

        last_id = cursor.lastrowid
        connector.commit()
        return last_id

    def deleteUserBy(self, field: str, value: str):
        connector = self.database
        cursor = connector.cursor()
        query = "DELETE FROM Users WHERE {}=?".format(field)

        cursor.execute(query, (value,))
        connector.commit()

    def makeUser(self, user_data: tuple, user_metadata=None) -> UserEntity:
        if user_metadata is None:
            user_metadata = {}
        user = UserEntity()
        user.id = user_data[0] if 0 in range(len(user_data)) else None
        user.username = user_data[1] if 1 in range(len(user_data)) else None
        user.created_at = user_data[2] if 2 in range(len(user_data)) else None
        user.password = user_data[3] if 3 in range(len(user_data)) else None
        user.email = user_data[4] if 4 in range(len(user_data)) else None
        user.slug = user_data[5] if 5 in range(len(user_data)) else None
        user.access_token = user_data[6] if 6 in range(len(user_data)) else None
        user.meta = user_metadata
        return user
