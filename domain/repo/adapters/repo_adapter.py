from kink import inject
from domain.repo.repo_interface import IRepo
from domain.gitolite.gitolite_interface import IGitolite
from domain.contrib.contrib_interface import IContrib
from domain.repo.exceptions.repo_exception import ExistRepoException, RepoNotFoundException
from os import getenv


class RepoAdapter(IRepo):

    @inject
    def __init__(self, gitolite: IGitolite, contrib: IContrib):
        self.gitolite = gitolite
        self.config_path = getenv("GIT_CONF_PATH")
        self.contrib = contrib

    def getRepoContributedBy(self, username: str) -> [str]:
        config = self.gitolite.readConfig(self.config_path).getConfig()
        repos = []
        for (repo_path, value) in config.items():
            contributors = self.contrib.listContrib(repo_path)
            if username in contributors:
                repos.append(repo_path)
        if not repos:
            raise RepoNotFoundException()
        return repos

    def getAllRepo(self) -> [str]:
        config = self.gitolite.readConfig(self.config_path).getConfig()
        repos = list(config.keys())
        if not repos:
            raise RepoNotFoundException()
        return repos

    def addRepo(self, repo_path: str, username: str):
        if repo_path in self.getAllRepo():
            raise ExistRepoException()
        self.gitolite.readConfig(self.config_path).addRepo(repo_path, username).applyConfig()

    def removeRepo(self, repo_path: str):
        if repo_path not in self.getAllRepo():
            raise RepoNotFoundException()
        self.gitolite.removeRepo(repo_path).applyConfig()

    def verifyRepoExist(self, repo_path: str):
        if repo_path not in self.getAllRepo():
            raise RepoNotFoundException()