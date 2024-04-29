from domain.repoUtils.IRepoOutput import IRepoOutput


class RepoOutputAdapter(IRepoOutput):

    def __init__(self):
        self.configuration = None

    def getContributors(self, repo_name: str) -> [str]:
        repo_configuration = self.configuration[repo_name]
        contributors = []
        for conf in repo_configuration:
            # On recupere le dernier element du tablreau qui represente le username
            # Et on l'ajoute de la table des contributeurs
            contributors.append(conf.split(' ')[-1])
        return contributors

    def getRepoContributedBy(self, username: str) -> [str]:
        repos = []
        for repo_name in self.configuration.keys():
            if username in self.getContributors(repo_name):
                repos.append(repo_name)
        return repos

    def setConfiguration(self, configuration: dict):
        self.configuration = configuration
