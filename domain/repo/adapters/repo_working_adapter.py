from domain.repo.repo_working_interface import IRepoWorking
from git import Repo
from git import GitCommandError
from domain.repo.exceptions.repo_exception import CommandErrorException

class RepoWorkingAdapter(IRepoWorking):

    def __init__(self):
        self.repo_dir = ""

    # @Deprecated
    def getTreeDirectory(self, repo_path: str, branch_name: str, dir_path: str = "") -> list:
        repo = Repo(self.mpath(repo_path))
        try:
            if not dir_path:
                config_files = repo.git.execute(['git', 'ls-tree', branch_name]).split('\n')
            else:
                config_files = repo.git.execute(['git', 'ls-tree', "{}:{}".format(branch_name, dir_path)]).split('\n')
            out = []
            for config_file in config_files:
                splitted = config_file.split()
                print("+++++++++++++++")
                print(splitted)
                out.append({ 'name': ' '.join(splitted[3:]), 'type': splitted[1] })
            return out
        except GitCommandError:
            raise CommandErrorException()

    # @Deprecated
    def getBlobFile(self, repo_path: str, branch_name: str, file_path: str) -> str:
        repo = Repo(self.mpath(repo_path))
        try:
            out = repo.git.execute(
                ['git', 'show', '{}:{}'.format(branch_name, file_path)]
            )
            return out
        except GitCommandError:
            raise CommandErrorException
        

    def editFile(self, repo_path: str, branch_name: str, file_path: str):
        pass

    # @Deprecated
    def listCommit(self, repo_path: str, branch: str) -> list:
        repo = Repo(self.mpath(repo_path))
        out = repo.git.execute(
            ['git', 'log', branch,'--pretty=format:%H%x00%ad%x00%s%x00%D%x00%b%x00%an%x00%ae', '--date=iso-strict']
        )
        commits = []
        for line in out.split('\n'):
            if line.strip():  # Ignorer les lignes vides
                parts = line.split('\x00')
                commit = {
                    "hash": parts[0],
                    "date": parts[1],
                    "message": parts[2],
                    "refs": parts[3],
                    "body": parts[4],
                    "author_name": parts[5],
                    "author_email": parts[6]
                }
                commits.append(commit)
        
        return commits

    # @Deprecated
    def listBranches(self, repo_path: str) -> list:
        repo = Repo(self.mpath(repo_path))
        out = repo.git.branch().replace('* ','').strip().split('\n')
        return out

    def setRepoDir(self, repo_dir: str) -> IRepoWorking:
        self.repo_dir = repo_dir
        return self

    # make path
    def mpath(self, repo_path: str):
        return self.repo_dir + '/' + repo_path + ".git"
