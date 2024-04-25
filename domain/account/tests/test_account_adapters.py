import unittest
from domain.account.adapters.AccountAdapter import AccountAdapter
from domain.account.AccountEntity import AccountEntity
from random import randint
from kink import di
from domain.account.IAccount import IAccount
from bootstrap import Bootstrap


class TestAccountAdapters (unittest.TestCase):
    def testCreateAccount(self):
        boostrap = Bootstrap()
        account = AccountEntity()
        account.username = "user-" + str(randint(1000000, 9999999))
        account.email = account.username + ".email@gmail.com"

        # TODOS: On n'oublie pas de hasher
        account.password = "password"

        account_adapter = di[IAccount]
        user = account_adapter.createAccount(account)
        self.assertTrue(user)


if __name__ == "__main__":
    unittest.main()
