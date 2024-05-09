from domain.security.security_interface import ISecurity
import bcrypt


class SecurityAdapter(ISecurity):
    def checkPassword(self, password: str, hashed_password: str) -> bool:
        _password = bcrypt.hashpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
        return hashed_password.encode('utf-8') == _password
