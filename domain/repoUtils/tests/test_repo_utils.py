import unittest
from domain.repoUtils.adapters.RepoUtilsAdapter import RepoUtilsAdapter

class TestRepoUtils(unittest.TestCase):
    def testCreateRepo(self):
        pass

    def testParse(self):
        print("-----TEST PARSE-----")
        filepath = "/home/gollum/Project/gollum/domain/repoUtils/tests/gitolite_test.conf"
        file = open(filepath, 'r')
        config = RepoUtilsAdapter.parse(file)
        print(config)

    def testDump(self):
        print("-----TEST DUMP-----")
        config = {'gitolite-admin': ['RW+     =   admin', 'RW+     =   repo'], 'testing': ['RW+     =   @all']}
        dumped = RepoUtilsAdapter.dump(config)
        print(dumped)

    def testRepoUtilsScenar(self):
        print("------TEST ALL------")
        filepath = "/home/gollum/Project/gollum/domain/repoUtils/tests/gitolite_test.conf"
        repo_utils = RepoUtilsAdapter(filepath)

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