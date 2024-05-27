from apiflask import HTTPError


class RepoNotFoundException(HTTPError):
    message = "Repo introuvable"
    status_code = 404


class ExistRepoException(HTTPError):
    message = "Repo déjà existant"
    status_code = 409


class CommandErrorException(HTTPError):
    message = "Commande introuvable"
    status_code = 404
