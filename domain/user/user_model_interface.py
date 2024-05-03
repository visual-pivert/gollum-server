from abc import ABC, abstractmethod
from domain.user.user_entity import UserEntity


class IUserModel(ABC):

    @abstractmethod
    def getUserBy(self, field: str, value: str) -> UserEntity: pass

    @abstractmethod
    def updateAccessToken(self, username: str, new_access_token: str | None): pass

    @abstractmethod
    def listUser(self) -> [UserEntity]: pass

    @abstractmethod
    def addUser(self, user: UserEntity) -> int: pass

    @abstractmethod
    def deleteUserBy(self, field: str, value: str): pass
