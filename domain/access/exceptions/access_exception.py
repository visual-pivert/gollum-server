from apiflask import HTTPError


class AccessException(HTTPError):
    message = "Nom d'utilisateur ou mot de passe incorrecte"
    status_code = 401


class InvalidAccessTokenException(HTTPError):
    message = "Token d'acces invalide"
    status = 401
