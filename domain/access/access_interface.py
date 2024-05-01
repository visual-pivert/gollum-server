from abc import ABC, abstractmethod


class IAccess(ABC):

    @abstractmethod
    def accessToken(self, username: str, password: str) -> str: pass

    @abstractmethod
    def revokeAccessToken(self, access_token: str): pass

    @abstractmethod
    def generateToken(self, obj: dict) -> str: pass

    @abstractmethod
    def verifyAccessToken(self, access_token: str) -> bool: pass
