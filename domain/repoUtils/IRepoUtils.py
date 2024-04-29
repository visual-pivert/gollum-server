from abc import ABC, abstractmethod


class IRepoUtils(ABC):
    @abstractmethod
    def createRepo(self, repo_name: str): pass

    @abstractmethod
    def addRestriction(self, repo_name: str, condition: str): pass

    @abstractmethod
    def deleteRepo(self, repo_name: str): pass

    @abstractmethod
    def removeRestriction(self, repo_name: str, index: int): pass

    @abstractmethod
    def apply(self): pass

    def getState(self) -> dict: pass
