from abc import ABC, abstractmethod
from domain.auth.UserEntity import UserEntity


class IRepoOutput(ABC):

    @abstractmethod
    def getContributors(self, repo_name: str) -> [str]: pass

    @abstractmethod
    def getRepoContributedBy(self, username: str) -> [str]: pass

    @abstractmethod
    def setConfiguration(self, configuration: dict): pass
