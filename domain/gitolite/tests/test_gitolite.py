import unittest
from kink import di
from bootstrap import Bootstrap
from domain.gitolite.gitolite_interface import IGitolite


class TestGitolite(unittest.TestCase):
    def testReadConfig(self):
        bootstrap = Bootstrap()
        gitolite = di[IGitolite]
        gitolite_conf_path = "/home/gollum/Project/gollum/var/gitolite_test.conf"
        conf = gitolite.readConfig(gitolite_conf_path).getConfig()
        print(conf)

    def testApplyConfig(self):
        bootstrap = Bootstrap()
        gitolite = di[IGitolite]
        gitolite_conf_path = "/home/gollum/Project/gollum/var/gitolite_test.conf"
        (gitolite.readConfig(gitolite_conf_path)
         .removeRepo('my_repo')
         .applyConfig())



if __name__ == "__main__":
    unittest.main()