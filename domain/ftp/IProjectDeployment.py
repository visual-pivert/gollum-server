from abc import ABC, abstractmethod

from domain.ftp.IFileOperations import ICompression


class IFtp(ABC):
    @abstractmethod
    def connectFTP(self, host: str, user: str, password: str): pass

    @abstractmethod
    def disconnectFTP(self): pass

    @abstractmethod
    def send(self, project_path: str): pass


class IProjectDeployment(ABC):
    @abstractmethod
    def deployProject(self, project_path: str): pass
