from apiflask import HTTPError


class UserNotFoundException(HTTPError):
    message = "Utilisateur introuvable"
    status_code = 404


class UsernameNotUniqueException(HTTPError):
    message = "Nom d'utilisateur non disponible"
    status_code = 409


class EmailNotUniqueException(HTTPError):
    message = "Adresse email non disponible"
    status_code = 409
