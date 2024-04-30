from apiflask import APIBlueprint, abort
from domain.account.adapters.AccountAdapter import AccountAdapter
from domain.account.AccountEntity import AccountEntity
from domain.auth.forms.LoginForm import LoginForm
from domain.auth.exceptions.LoginException import LoginException
from kink import di
from domain.auth.IAuth import IAuth

auth_app = APIBlueprint('auth_app', __name__)


@auth_app.post("/login")
@auth_app.input(LoginForm)
def login(json_data):
    # injection de dependance
    auth = di[IAuth]
    try:
        return auth.login(json_data['username'], json_data['password'], False)
    except LoginException as e:
        abort(401)


@auth_app.get("/logout/<string:access_token>")
def logout(access_token):
    # injection de dependance
    auth = di[IAuth]
    auth.logout(access_token)
    return {"message": "logged out"}
