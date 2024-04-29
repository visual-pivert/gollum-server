import unittest
from domain.repoUtils.adapters.RepoUtilsAdapter import RepoUtilsAdapter
from kink import di
from domain.repoUtils.IRepoUtils import IRepoUtils
from bootstrap import Bootstrap

class TestRepoUtils(unittest.TestCase):
    def testCreateRepo(self):
        pass

    def testRepoUtilsScenar(self):
        print("------TEST ALL------")
        bootstrap = Bootstrap()
        repo_utils = di[IRepoUtils]

        print("Repo created")
        repo_utils.createRepo('new_repo')
        print(repo_utils.getState())


        print("Restriction added")
        repo_utils.addRestriction('new_repo', 'RW+     =   repo')
        repo_utils.addRestriction('new_repo', 'RW+     =   to_delete')
        print(repo_utils.getState())

        print("Restriction deleted")
        repo_utils.removeRestriction('new_repo', 1)
        print(repo_utils.getState())

        print("Dump")
        print(RepoUtilsAdapter.dump(repo_utils.getState()))

        print("repo deleted")
        repo_utils.deleteRepo('new_repo')
        print(repo_utils.getState())

        print("repo updated")
        repo_utils.apply()




if __name__ == "__main__":
    unittest.main()