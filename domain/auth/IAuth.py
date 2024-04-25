from abc import ABC, abstractmethod
from domain.auth.UserEntity import UserEntity


class IAuth (ABC):

    @abstractmethod
    def login(self, username: str, password: str, remember: bool): pass

    @abstractmethod
    def logout(self): pass

    @abstractmethod
    def loggedUser(self) -> "UserEntity": pass
