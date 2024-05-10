from domain.account.account_interface import IAccount
from domain.user.user_entity import UserEntity
from domain.account.account_entity import AccountEntity
from kink import inject
from domain.user.user_model_interface import IUserModel


class AccountAdapter(IAccount):

    @inject
    def __init__(self, user_model: IUserModel):
        self.user_model = user_model

    def createAccount(self, account: AccountEntity) -> UserEntity:
        new_user = UserEntity()
        new_user.username = account.username
        new_user.password = account.password
        new_user.email = account.email
        new_user.slug = account.username
        new_user.can_create = 1 # TODO: Ceci est a modifier
        new_user.access_token = None

        last_id = self.user_model.addUser(new_user)
        the_user = self.user_model.getUserBy('id', str(last_id))

        return the_user
