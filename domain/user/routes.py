from apiflask import APIBlueprint
from flask import request
from domain.user.user_model_interface import IUserModel
from domain.user.schemas.user_schema import UserListSchema, UserInputSchema, UserOutputSchema
from domain.access.access_interface import IAccess
from kink import di

user_app = APIBlueprint('user_app', __name__)


@user_app.get("/api/users/list")
@user_app.output(UserListSchema)
def listUser():
    # injection de dependance
    user_model = di[IUserModel]
    access = di[IAccess]

    # Verification
    access_token = request.headers.get("Access-token")
    access.verifyAccessToken(access_token)

    users = user_model.listUser()
    out = []
    for user in users:
        out.append({
            'username': user.username,
            'email': user.email,
            'slug': user.slug
        })
    return {"users": out, "status_code": 200, "message": "OK"}


@user_app.delete("/api/users/delete")
@user_app.input(UserInputSchema)
def deleteUser(json_data):
    # injection de dependance
    user_model = di[IUserModel]
    access = di[IAccess]

    # Verification
    access_token = request.headers.get("Access-token")
    access.verifyAccessToken(access_token)
    access.verifyAdmin(access_token)

    user_model.deleteUserBy('username', json_data['username'])
    return {"message": "User removed", "status_code": 200}


@user_app.get("/api/users/get/<string:user_slug>")
@user_app.output(UserOutputSchema)
def getUser(user_slug):
    user_model = di[IUserModel]
    access = di[IAccess]

    # Verification
    access_token = request.headers.get("Access-token")
    access.verifyAccessToken(access_token)

    user = user_model.getUserBy('slug', user_slug)
    return {'username': user.username, 'slug': user.slug, 'email': user.email, "status_code": 200, "message": "OK"}
