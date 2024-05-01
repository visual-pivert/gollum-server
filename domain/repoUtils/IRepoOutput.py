from abc import ABC, abstractmethod
from domain.user.user_entity import UserEntity


class IRepoOutput(ABC):

    @abstractmethod
    def getContributors(self, repo_name: str) -> [str]: pass

    @abstractmethod
    def getRepoContributedBy(self, username: str) -> [str]: pass

    @abstractmethod
    def setConfiguration(self, configuration: dict): pass
