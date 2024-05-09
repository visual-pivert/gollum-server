from abc import ABC, abstractmethod


class IRepoWorking(ABC):

    @abstractmethod
    def getTreeDirectory(self, repo_path: str, branch_name: str, dir_path: str) -> list: pass

    @abstractmethod
    def getBlobFile(self, repo_path: str, branch_name: str, file_path: str) -> str: pass

    @abstractmethod
    def editFile(self, repo_path: str, branch_name: str, file_path: str): pass
    @abstractmethod
    def listCommit(self, repo_path: str, branch: str) -> list: pass

    @abstractmethod
    def listBranches(self, repo_path: str) -> list: pass

    @abstractmethod
    def setRepoDir(self, repo_dir: str) -> "IRepoWorking": pass

