from apiflask import APIBlueprint
from domain.account.schemas.account_schema import AccountSchema
from domain.account.account_entity import AccountEntity
from kink import di
from domain.account.account_interface import IAccount

account_app = APIBlueprint('account_app', __name__)


@account_app.post("/api/signup")
@account_app.input(AccountSchema)
def signup(json_data):
    # injection de dependance
    account = di[IAccount]
    account_entity = AccountEntity()
    account_entity.username = json_data["username"]
    account_entity.password = json_data["password"]
    account_entity.email = json_data["email"]
    id = account.createAccount(account_entity)
    return {"username": account_entity.username}
