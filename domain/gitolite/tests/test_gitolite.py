import unittest
from kink import di
from bootstrap import Bootstrap
from domain.gitolite.gitolite_interface import IGitolite
from os import getenv


class TestGitolite(unittest.TestCase):
    def testReadConfig(self):
        bootstrap = Bootstrap()
        gitolite = di[IGitolite]
        gitolite_conf_path = getenv("GIT_CONF_PATH")
        conf = gitolite.readConfig(gitolite_conf_path).getConfig()
        print(conf)

    def testApplyConfig(self):
        bootstrap = Bootstrap()
        gitolite = di[IGitolite]
        gitolite_conf_path = getenv("GIT_CONF_PATH")
        (gitolite.readConfig(gitolite_conf_path)
         .removeRepo('my_repo')
         .applyConfig())



if __name__ == "__main__":
    unittest.main()