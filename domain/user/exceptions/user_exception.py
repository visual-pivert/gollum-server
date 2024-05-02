from apiflask import HTTPError


class UserNotFoundException(HTTPError):
    message = "Utilisateur introuvable"
    status_code = 404


class UserNotUniqueException(HTTPError):
    pass
