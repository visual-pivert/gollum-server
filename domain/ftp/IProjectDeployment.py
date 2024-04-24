from abc import ABC, abstractmethod

from domain.ftp.IFileOperations import ICompression


class IFtp(ABC):
    @abstractmethod
    def connectFTP(self, host: str, user: str, password: str): pass

    @abstractmethod
    def disconnectFTP(self): pass

    @abstractmethod
    def send(self, project_path: str, project_dist): pass


class IProjectDeployment(ABC):
    @abstractmethod
    def createDecompressScript(self, file_path: str, archive_path: str): pass

    @abstractmethod
    def deployProject(self, project_path: str): pass

    @abstractmethod
    def decompressDeployedProject(self, script: str): pass
