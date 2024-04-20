from abc import ABC, abstractmethod


class IFileManipulation(ABC):
    @staticmethod
    @abstractmethod
    def createDir(dir_name: str, permission: int): pass

    @staticmethod
    @abstractmethod
    def remove(path: str): pass


class IFilePermission(ABC):
    @staticmethod
    @abstractmethod
    def changePermission(file_path: str, permission: int): pass


class ICompression(ABC):
    @staticmethod
    @abstractmethod
    def compressProject(project_path: str, dist: str): pass

    @staticmethod
    @abstractmethod
    def decompressProject(): pass
    