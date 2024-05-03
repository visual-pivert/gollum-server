from apiflask import HTTPError


class ContribNotFoundException(HTTPError):
    message = "Contributeurs introuvable"
    status_code = 404

class IsContribException(HTTPError):
    message = "Déja contributeur"
    status_code = 409