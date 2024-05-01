import unittest
from bootstrap import Bootstrap
from kink import di
from domain.security.security_interface import ISecurity

class TestSecurity(unittest.TestCase):
    def testCheckPassword(self):
        bootstrap = Bootstrap()
        security = di[ISecurity]
        verified_password = security.checkPassword('password', '$2b$12$6dxc5A9K4W1psKGzxYr7a.m3Syc4JiHa1L3heuQ4ZZ2atOKo07S3y')
        print(verified_password)
        self.assertTrue(verified_password)


if __name__ == "__main__":
    unittest.main()