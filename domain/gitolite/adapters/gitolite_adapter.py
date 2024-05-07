from domain.gitolite.gitolite_interface import IGitolite
from domain.repo.exceptions.repo_exception import RepoNotFoundException
import re


class GitoliteAdapter(IGitolite):

    def __init__(self):
        self.config = None
        self.config_path = ""

    def addRepo(self, repo_path: str, username: str) -> "IGitolite":
        self.config[repo_path] = ["RW+     =   {}".format(username)]
        return self

    def addRule(self, repo_path: str, rule: str) -> "IGitolite":
        self.config[repo_path].append(rule)
        return self

    def removeRule(self, repo_path: str, index: int) -> "IGitolite":
        self.config[repo_path].pop(index)
        return self

    def removeRepo(self, repo_path: str) -> "IGitolite":
        self.config.pop(repo_path)
        return self

    def readConfig(self, config_path: str) -> "IGitolite":
        out = {}
        repo_name = ""
        self.config_path = config_path
        file = open(config_path, 'r')
        lines = file.readlines()
        for line in lines:
            if re.search("^repo", line):
                splitted_line = line.split(' ')
                repo_name = splitted_line[1].strip()
                out[repo_name] = []
            else:
                if repo_name:
                    out[repo_name].append(line.strip())

                    # enlever les valeurs vides dans le tableau
                    out[repo_name] = list(filter(lambda x: x != '', out[repo_name]))

        file.close()
        self.config = out
        return self

    def getConfig(self, repo_path: str = ""):
        if not repo_path:
            return self.config
        else:
            if repo_path in self.config:
                return self.config[repo_path]
            else:
                raise RepoNotFoundException()

    def applyConfig(self):
        file = open(self.config_path, "w")
        compiled = self.compileConfig()
        file.write(compiled)
        file.close()

    def compileConfig(self):
        out = ""
        for (key, values) in self.config.items():
            repo_str = "repo {}\n".format(key)
            restriction_str = ""
            for value in values:
                restriction_str = restriction_str + "\t" + value + "\n"
            out = out + "\n" + repo_str + restriction_str
        return out

    def getRules(self, repo_path: str) -> list:
        if repo_path not in self.config.keys():
            raise RepoNotFoundException()
        return self.config[repo_path]

    def getRepos(self) -> list:
        return self.config.keys()
