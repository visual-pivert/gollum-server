import unittest
from domain.auth.adapters.AuthAdapter import AuthAdapter
from bootstrap import Boostrap
from kink import di
from domain.auth.IAuth import IAuth


class TestAuth(unittest.TestCase):
    def testGetUserBy(self):
        bootstrap = Boostrap()
        auth = di[IAuth]
        user = auth.getUserBy('username', 'username')
        if 'username' == user.username:
            self.assertTrue(True)
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
