import unittest
from domain.account.account_entity import AccountEntity
from random import randint
from kink import di
from domain.account.account_interface import IAccount
from bootstrap import Bootstrap


class TestAccountAdapters (unittest.TestCase):
    def testCreateAccount(self):
        boostrap = Bootstrap()
        new_account = AccountEntity()
        new_account.username = "user-" + str(randint(1000000, 9999999))
        new_account.email = new_account.username + ".email@gmail.com"

        # TODOS: On n'oublie pas de hasher
        new_account.password = "password"

        account_adapter = di[IAccount]
        user = account_adapter.createAccount(new_account)
        self.assertTrue(user)


if __name__ == "__main__":
    unittest.main()
