from apiflask import APIBlueprint
from flask import request
from kink import di
from domain.contrib.contrib_interface import IContrib
from domain.contrib.schemas.contrib_schema import ContribInputSchema, ContribListSchema
from domain.access.access_interface import IAccess

contrib_app = APIBlueprint('contrib_app', __name__)


@contrib_app.get("/api/contributors/list/<path:repo_path>")
@contrib_app.output(ContribListSchema)
def listContributors(repo_path):
    contrib = di[IContrib]
    access = di[IAccess]

    # Verification
    access_token = request.headers.get("Access-token")
    access.verifyAccessToken(access_token)
    access.verifyContributor(access_token, repo_path)

    contrib_list = contrib.listContrib(repo_path)
    out = []
    for contrib in contrib_list:
        out.append({"username": contrib})
    return {"contributors": out, "status_code": 200}


@contrib_app.post("/api/contributors/add/<path:repo_path>")
@contrib_app.input(ContribInputSchema)
def addContributor(repo_path, json_data):
    contrib = di[IContrib]
    access = di[IAccess]

    # Verification
    access_token = request.headers.get("Access-token")
    access.verifyAccessToken(access_token)
    access.verifyCreator(access_token, repo_path)

    contrib.addContrib(json_data['username'], repo_path)
    return {"message": "Contributor added", "status_code": 201}


@contrib_app.delete("/api/contributors/delete/<path:repo_path>")
@contrib_app.input(ContribInputSchema)
def deleteContributor(repo_path, json_data):
    contrib = di[IContrib]
    access = di[IAccess]

    # Verification
    access_token = request.headers.get("Access-token")
    access.verifyAccessToken(access_token)
    access.verifyCreator(access_token, repo_path)

    contrib.removeContrib(json_data['username'], repo_path)
    return {"message": "Contributor removed", "status_code": 200}
