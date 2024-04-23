from abc import ABC, abstractmethod
from domain.account.AccountEntity import AccountEntity
from domain.auth.UserEntity import UserEntity


class IAccount(ABC):

    @staticmethod
    @abstractmethod
    def createAccount(account: AccountEntity) -> "UserEntity": pass

