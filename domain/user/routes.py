from apiflask import APIBlueprint
from domain.account.schemas.account_schema import AccountSchema
from domain.user.user_model_interface import IUserModel
from domain.access.access_interface import IAccess
from domain.access.decorators.access_decorator import verifyAccessToken
from domain.user.schemas.user_schema import UserListSchema, UserInputSchema, UserOutputSchema
from kink import di
from domain.account.account_interface import IAccount

user_app = APIBlueprint('user_app', __name__)


@user_app.get("/api/users/list")
@user_app.output(UserListSchema)
@verifyAccessToken
def listUser():
    # injection de dependance
    user_model = di[IUserModel]
    users = user_model.listUser()
    out = []
    for user in users:
        out.append({
            'username': user.username,
            'email': user.email,
            'slug': user.slug
        })
    return {"users": out}


@user_app.delete("/api/users/delete")
@user_app.input(UserInputSchema)
@verifyAccessToken
def deleteUser(json_data):
    # injection de dependance
    user_model = di[IUserModel]
    user_model.deleteUserBy('username', json_data['username'])
    return {"message": "User deleted"}


@user_app.get("/api/users/get/<string:user_slug>")
@user_app.output(UserOutputSchema)
@verifyAccessToken
def getUser(user_slug):
    user_model = di[IUserModel]
    user = user_model.getUserBy('slug', user_slug)
    return {'username': user.username, 'slug': user.slug, 'email': user.email}
