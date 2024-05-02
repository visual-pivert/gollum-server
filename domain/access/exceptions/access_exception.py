from apiflask import HTTPError


class AccessException(HTTPError):
    message = "Nom d'utilisateur ou mot de passe incorrecte"
    status_code = 401
