import unittest
from bootstrap import Bootstrap
from domain.access.access_interface import IAccess
from kink import di


class TestAccess(unittest.TestCase):
    def testGenerateToken(self):
        bootstrap = Bootstrap()
        access = di[IAccess]

        token = access.generateToken({"username": "username", "password": "password"})
        print(token)

    def testDecodeAccessToken(self):
        bootstrap = Bootstrap()
        access = di[IAccess]

        token = access.generateToken({"username": "username", "password": "password"})
        decoded = access.decodeAccessToken(token)
        print(decoded)

    def testAccessToken(self):
        bootstrap = Bootstrap()
        access = di[IAccess]

        token = access.accessToken('username', 'password')
        print(token)

    def testRevokeAccessToken(self):
        bootstrap = Bootstrap()
        access = di[IAccess]

        token = access.revokeAccessToken("eyJ1c2VybmFtZSI6ICJ1c2VybmFtZSIsICJfaWQiOiAyNjA0OCwgIl90aW1lc3RhbXAiOiAxNzE0NTgzMjM1fQ==")

if __name__ == "__main__":
    unittest.main()
