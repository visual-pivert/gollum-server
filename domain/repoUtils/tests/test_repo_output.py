import unittest
from domain.repoUtils.adapters.RepoOutputAdapter import RepoOutputAdapter


class TestRepoOutput(unittest.TestCase):
    def testGetContributors(self):
        print("------GET CONTRIBUTORS----------")
        repo_output = RepoOutputAdapter()
        repo_output.setConfiguration({'gitolite-admin': ['RW+     =   admin', 'RW+     =   repo'], 'testing': ['RW+     =   @all'], 'new_repo': ['RW+     =   repo']})
        contributors = repo_output.getContributors('gitolite-admin')
        print(contributors)


    def testGetRepoContributedBy(self):
        print("----------GET REPO CONTRIBUTED BY------------")
        repo_output = RepoOutputAdapter()
        repo_output.setConfiguration({'gitolite-admin': ['RW+     =   admin', 'RW+     =   repo'], 'testing': ['RW+     =   @all'],'new_repo': ['RW+     =   repo']})
        repos = repo_output.getRepoContributedBy('repo')
        print(repos)


if __name__ == "__main__":
    unittest.main()