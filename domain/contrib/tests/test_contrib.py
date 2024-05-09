import unittest
from bootstrap import Bootstrap
from kink import di
from domain.contrib.contrib_interface import IContrib

class TestContrib(unittest.TestCase):
    # def testAddContrib(self):
    #     bootstrap = Bootstrap()
    #     contrib = di[IContrib]
    #     contrib.addContrib('email', 'testing')


    # def testRemoveContrib(self):
    #     bootstrap = Bootstrap()
    #     contrib = di[IContrib]
    #     contrib.removeContrib('email', 'testing')

    def testListContrib(self):
        bootstrap = Bootstrap()
        contrib = di[IContrib]
        print(contrib.listContrib('testing'))


if __name__ == "__main__":
    unittest.main()