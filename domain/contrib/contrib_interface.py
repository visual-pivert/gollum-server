from abc import ABC, abstractmethod


class IContrib(ABC):
    @abstractmethod
    def addContrib(self, username: str, repo_path: str): pass

    @abstractmethod
    def removeContrib(self, username: str, repo_path: str): pass

    @abstractmethod
    def listContrib(self, repo_path: str): pass
