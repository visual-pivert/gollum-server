from abc import ABC, abstractmethod


class IFileManipulation(ABC):
    @staticmethod
    @abstractmethod
    def createDir(dir_name: str, permission: int): pass


class IFilePermission(ABC):
    @staticmethod
    @abstractmethod
    def changePermission(file_path: str, permission: int): pass


class ICompression(ABC):
    @staticmethod
    @abstractmethod
    def compressProject(project_path: str): pass

    @staticmethod
    @abstractmethod
    def decompressProject(): pass
    