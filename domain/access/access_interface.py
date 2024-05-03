from abc import ABC, abstractmethod


class IAccess(ABC):

    @abstractmethod
    def accessToken(self, username: str, password: str) -> str: pass

    @abstractmethod
    def revokeAccessToken(self, access_token: str): pass

    @abstractmethod
    def generateToken(self, obj: dict) -> str: pass

    @abstractmethod
    def decodeAccessToken(self, access_token: str) -> dict: pass

    @abstractmethod
    def verifyAccessToken(self, access_token: str) -> bool: pass

    @abstractmethod
    def verifyContributor(self, access_token: str, repo_path: str) -> bool: pass

    @abstractmethod
    def verifyCreator(self, access_token: str, repo_path: str) -> bool: pass

    @abstractmethod
    def verifyAdmin(self, access_token: str) -> bool: pass
