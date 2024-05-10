from domain.contrib.contrib_interface import IContrib
from domain.gitolite.gitolite_interface import IGitolite
from domain.user.user_model_interface import IUserModel
from domain.contrib.exceptions.contrib_exception import ContribNotFoundException, IsContribException
from kink import inject
from os import getenv


class ContribAdapter(IContrib):

    @inject
    def __init__(self, gitolite: IGitolite, user_model: IUserModel):
        self.config_path = getenv("GIT_CONF_PATH")
        self.gitolite = gitolite
        self.user_model = user_model

    def addContrib(self, username: str, repo_path: str):
        config_readed = self.gitolite.readConfig(self.config_path)
        self.user_model.getUserBy('username', username) # UserNotFoundException si user introuvable
        rule = "RW     =   {}".format(username)
        if username in self.listContrib(repo_path):
            raise IsContribException()
        config_readed.addRule(repo_path, rule).applyConfig()

    def removeContrib(self, username: str, repo_path: str):
        config_readed = self.gitolite.readConfig(self.config_path)
        config = config_readed.getConfig(repo_path)
        i = 0
        is_contrib = False
        for conf in config:
            if username in conf:
                config_readed.removeRule(repo_path, i)
                is_contrib = True
            i += 1
        if not is_contrib:
            raise ContribNotFoundException()
        config_readed.applyConfig()

    def listContrib(self, repo_path: str):
        config_readed = self.gitolite.readConfig(self.config_path)
        rules = list(map(lambda el: el.split()[-1], config_readed.getRules(repo_path)))
        if not rules:
            raise ContribNotFoundException()
        return rules
