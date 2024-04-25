import unittest
from domain.account.adapters.AccountAdapter import AccountAdapter
from domain.account.AccountEntity import AccountEntity
from random import randint


class TestAccountAdapters (unittest.TestCase):
    def testCreateAccount(self):
        account = AccountEntity()
        account.username = "user-" + str(randint(1000000, 9999999))
        account.email = account.username + ".email@gmail.com"

        # TODOS: On n'oublie pas de hasher
        account.password = "password"

        user = AccountAdapter.createAccount(account)
        self.assertTrue(user)


if __name__ == "__main__":
    unittest.main()
