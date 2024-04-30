import unittest
from bootstrap import Bootstrap
from kink import di
from domain.auth.IAuth import IAuth


class TestAuth(unittest.TestCase):
    def testGetUserBy(self):
        bootstrap = Bootstrap()
        auth = di[IAuth]
        user = auth.getUserBy('username', 'username')
        if 'username' == user.username:
            self.assertTrue(True)

    def testCreateJwt(self):
        bootstrap = Bootstrap()
        auth = di[IAuth]
        jwt = auth.createJwt({"username": "username", "password": "password"})
        print(jwt)
        self.assertTrue(jwt)


if __name__ == "__main__":
    unittest.main()
