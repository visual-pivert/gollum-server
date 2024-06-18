import unittest
from bootstrap import Bootstrap
from kink import di
from domain.repo.repo_interface import IRepo

class TestRepo(unittest.TestCase):
    
    # def testGetRepoContributedBy(self):
    #     bootstrap = Bootstrap()
    #     repo = di[IRepo]
    #     repos = repo.getRepoContributedBy("username")
    #     print(repos)

    # def testGetAllRepo(self):
    #     bootstrap = Bootstrap()
    #     repo = di[IRepo]
    #     repos = repo.getAllRepo()
    #     print(repos)

    def testAddRepo(self):
        bootstrap = Bootstrap()
        repo = di[IRepo]
        repo.addRepo('my_repo_tesssseeeedddddt', 'username')
        repos = repo.getAllRepo()
        print(repos)

    # def testRemoveRepo(self):
    #     bootstrap = Bootstrap()
    #     repo = di[IRepo]
    #     repo.removeRepo('my_project_2')

if __name__ == "__main__":
    unittest.TestCase()