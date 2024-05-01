from abc import ABC, abstractmethod
from domain.account.account_entity import AccountEntity
from domain.user.user_entity import UserEntity


class IAccount(ABC):

    @abstractmethod
    def createAccount(self, account: AccountEntity) -> UserEntity: pass

