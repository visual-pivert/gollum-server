from apiflask import APIBlueprint, abort
from flask import request
from domain.access.access_interface import IAccess
from domain.access.schemas.access_schema import AccessSchema
from kink import di

access_app = APIBlueprint('access_app', __name__)


@access_app.post("/access")
@access_app.input(AccessSchema)
def access(json_data):
    access = di[IAccess]
    access_token = access.accessToken(json_data['username'], json_data['password'])
    if access_token:
        out = {
            'username': json_data['username'],
            'access_token': access_token
        }
        return out
    return abort(401)


@access_app.get("/revoke")
def revoke():
    access = di[IAccess]
    access_token = request.headers.get('Access-token')
    if access_token:
        access.revokeAccessToken(access_token)
        return {"message": "Token revoked"}
    return{"message": "No token revoked"}

