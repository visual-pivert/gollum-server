import unittest
from domain.repoUtils.IRepoOutput import IRepoOutput
from bootstrap import Bootstrap
from kink import di


class TestRepoOutput(unittest.TestCase):
    def testGetContributors(self):
        print("------GET CONTRIBUTORS----------")
        bootstrap = Bootstrap()
        repo_output = di[IRepoOutput]
        repo_output.setConfiguration({'gitolite-admin': ['RW+     =   admin', 'RW+     =   repo'], 'testing': ['RW+     =   @all'], 'new_repo': ['RW+     =   repo']})
        contributors = repo_output.getContributors('gitolite-admin')
        print(contributors)


    def testGetRepoContributedBy(self):
        print("----------GET REPO CONTRIBUTED BY------------")
        bootstrap = Bootstrap()
        repo_output = di[IRepoOutput]
        repo_output.setConfiguration({'gitolite-admin': ['RW+     =   admin', 'RW+     =   repo'], 'testing': ['RW+     =   @all'],'new_repo': ['RW+     =   repo']})
        repos = repo_output.getRepoContributedBy('repo')
        print(repos)


if __name__ == "__main__":
    unittest.main()