from domain.repo.repo_working_interface import IRepoWorking
from git import Repo


class RepoWorkingAdapter(IRepoWorking):

    def __init__(self):
        self.repo_dir = ""

    def getTreeDirectory(self, repo_path: str, branch_name: str, dir_path: str = "") -> list:
        repo = Repo(self.mpath(repo_path))
        if not dir_path:
            config_files = repo.git.execute(
                ['git', 'ls-tree', branch_name ,'--name-only']).split()
        else:
            config_files = repo.git.execute(
                ['git', 'ls-tree', "{}:{}".format(branch_name, dir_path), '--name-only']).split()
        return config_files

    def getBlobFile(self, repo_path: str, branch_name: str, file_path: str) -> str:
        repo = Repo(self.mpath(repo_path))
        out = repo.git.execute(
            ['git', 'show', '{}:{}'.format(branch_name, file_path)]
        )
        return out

    def editFile(self, repo_path: str, branch_name: str, file_path: str):
        pass

    def listCommit(self, repo_path: str, branch: str) -> list:
        repo = Repo(self.mpath(repo_path))
        out = repo.git.execute(
            ['git', 'log', "--oneline"]
        )
        return out

    def listBranches(self, repo_path: str) -> list:
        pass

    def setRepoDir(self, repo_dir: str) -> "IRepoWorking":
        pass

    def setRepoDir(self, repo_dir: str) -> IRepoWorking:
        self.repo_dir = repo_dir
        return self

    # make path
    def mpath(self, repo_path: str):
        return self.repo_dir + repo_path