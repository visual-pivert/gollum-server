from domain.repoUtils.IRepoUtils import IRepoUtils
import re


class RepoUtilsAdapter(IRepoUtils):

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.r_file = open(file_path, 'r')
        self.parsed = RepoUtilsAdapter.parse(self.r_file)

    def createRepo(self, repo_name: str):
        if repo_name not in self.parsed.keys():
            self.parsed[repo_name] = []

    def addRestriction(self, repo_name: str, condition: str):
        self.parsed[repo_name].append(condition)

    def deleteRepo(self, repo_name: str):
        self.parsed.pop(repo_name)

    def removeRestriction(self, repo_name, index: int):
        self.parsed[repo_name].pop(index)

    def apply(self):
        file = open(self.file_path, "w")
        config_to_write = RepoUtilsAdapter.dump(self.parsed)
        file.write(config_to_write)
        file.close()

        # TODOS: Commits

    def getState(self):
        return self.parsed

    @staticmethod
    def parse(file):
        out = {}
        repo_name = ""
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
        return out

    @staticmethod
    def dump(parsed_file: dict):
        out = ""
        for (key, values) in parsed_file.items():
            repo_str = "repo {}\n".format(key)
            restriction_str = ""
            for value in values:
                restriction_str = restriction_str + "\t" + value + "\n"
            out = out + "\n" + repo_str + restriction_str
        return out
