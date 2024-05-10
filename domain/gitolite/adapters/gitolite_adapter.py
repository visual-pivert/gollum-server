from domain.gitolite.gitolite_interface import IGitolite
from domain.repo.exceptions.repo_exception import RepoNotFoundException
import re
from git import Repo
from os import getenv, chmod
import shutil
import subprocess


class GitoliteAdapter(IGitolite):

    def __init__(self):
        self.config = None
        self.config_path = ""
        self.commit_message = ""

    def addRepo(self, repo_path: str, username: str) -> "IGitolite":
        self.config[repo_path] = ["RW+ 	= 	{}".format(username)]
        self.commit_message += "REPO ADDED: {} create {}\n".format(username, repo_path)
        return self

    def addRule(self, repo_path: str, rule: str) -> "IGitolite":
        self.config[repo_path].append(rule)
        self.commit_message += "RULE ADDED: add {} to {}\n".format(rule, repo_path)
        return self

    def removeRule(self, repo_path: str, index: int) -> "IGitolite":
        the_rule = self.config[repo_path][index]
        self.config[repo_path].pop(index)
        self.commit_message += "RULE ADDED: remove {} to {}\n".format(the_rule, repo_path)
        return self

    def removeRepo(self, repo_path: str) -> "IGitolite":
        self.config.pop(repo_path)
        
        # Suppression du depot git
        repo_dir = getenv("REPO_DIR")
        shutil.rmtree(repo_dir + repo_path + ".git")
        
        self.commit_message += "REPO DELETED: Creator remove {}\n".format(repo_path)
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
        
        subprocess.run(['gitolite', 'setup'])
        subprocess.run(['chmod', '777', '-R', getenv('GIT_COMPILED_CONF_PATH')])
        subprocess.run(['chmod', '777', '-R', getenv('REPO_DIR')])
        
        #self.pushConfig()
        

    def pushConfig(self):
        repo_path = getenv("GIT_ADMIN_REPO")
        password = getenv("USER_PASS")
        repo = Repo(repo_path)
        repo.git.add(update=True)
        repo.index.commit(self.commit_message)
        subprocess.run(['sshpass', '-p', password, 'git', '-C', repo_path, 'push'])

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
