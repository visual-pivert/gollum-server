from domain.user.user_model_interface import IUserModel
from domain.user.user_entity import UserEntity
from kink import inject
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

        user = self.makeUser(user_fetched) if user_fetched else None
        return user

    def updateAccessToken(self, username: str, new_access_token: str|None):
        connector = self.database
        cursor = connector.cursor()

        query = "UPDATE Users SET access_token = ? WHERE username = ?"
        cursor.execute(query, (new_access_token, username))
        connector.commit()

    def addUser(self, user: UserEntity) -> int:
        connector = self.database
        cursor = connector.cursor()
        query = "INSERT INTO Users(username, created_at, password, email, slug, access_token) VALUES(?, ?, ?, ?, ?, ?)"
        timestamp = datetime.datetime.now().timestamp()

        # cyphered_password -> str
        cyphered_password = bcrypt.hashpw(user.password.encode('utf8'), bcrypt.gensalt()).decode("utf-8")
        cursor.execute(query, (user.username, timestamp, cyphered_password, user.email, user.username,
                               user.access_token))

        last_id = cursor.lastrowid
        connector.commit()
        return last_id

    def makeUser(self, user_data: tuple, user_metadata=None) -> UserEntity:
        if user_metadata is None:
            user_metadata = {}
        user = UserEntity()
        user.id = user_data[0]
        user.username = user_data[1]
        user.created_at = user_data[2]
        user.password = user_data[3]
        user.email = user_data[4]
        user.slug = user_data[5]
        user.access_token = user_data[6]
        user.meta = user_metadata
        return user
