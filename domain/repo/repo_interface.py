from abc import ABC, abstractmethod


class IRepo(ABC):
    @abstractmethod
    def getRepoContributedBy(self, username: str) -> [str]: pass

    @abstractmethod
    def getAllRepo(self) -> [str]: pass

    @abstractmethod
    def addRepo(self, repo_path: str, username: str): pass
