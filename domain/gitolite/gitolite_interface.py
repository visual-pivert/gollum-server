from abc import ABC, abstractmethod


class IGitolite(ABC):
    @abstractmethod
    def addRepo(self, repo_path: str, username: str) -> "IGitolite": pass

    @abstractmethod
    def addRule(self, repo_path: str, rule: str) -> "IGitolite": pass

    @abstractmethod
    def removeRule(self, repo_path: str, index: int) -> "IGitolite": pass

    @abstractmethod
    def removeRepo(self, repo_path: str) -> "IGitolite": pass

    @abstractmethod
    def readConfig(self, config_path: str) -> "IGitolite": pass

    def getConfig(self, repo_path: str) -> dict: pass

    @abstractmethod
    def applyConfig(self): pass

    @abstractmethod
    def getRules(self, repo_path: str) -> list: pass

    @abstractmethod
    def getRepos(self) -> list: pass
