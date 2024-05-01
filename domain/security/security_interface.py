from abc import ABC, abstractmethod


class ISecurity(ABC):
    @abstractmethod
    def checkPassword(self, password: str, hashed_password: str) -> bool: pass
