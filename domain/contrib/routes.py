from apiflask import APIBlueprint
from kink import di
from domain.contrib.contrib_interface import IContrib
from domain.contrib.schemas.contrib_schema import ContribInputSchema, ContribListSchema
from domain.access.decorators.access_decorator import verifyAccessToken, verifyContributor, verifyCreator

contrib_app = APIBlueprint('contrib_app', __name__)


@contrib_app.get("/api/contributors/list/<string:repo_path>")
@contrib_app.output(ContribListSchema)
@verifyAccessToken
@verifyContributor
def listContributors(repo_path):
    contrib = di[IContrib]
    contrib_list = contrib.listContrib(repo_path)
    out = []
    for contrib in contrib_list:
        out.append({"username": contrib})
    return {"contributors": out}


@contrib_app.post("/api/contributors/add/<string:repo_path>")
@contrib_app.input(ContribInputSchema)
@verifyAccessToken
@verifyCreator
def addContributor(repo_path, json_data):
    contrib = di[IContrib]
    contrib.addContrib(json_data['username'], repo_path)
    return {"message": "Contributor added"}


@contrib_app.delete("/api/contributors/delete/<string:repo_path>")
@contrib_app.input(ContribInputSchema)
@verifyAccessToken
@verifyCreator
def deleteContributor(repo_path, json_data):
    contrib = di[IContrib]
    contrib.removeContrib(json_data['username'], repo_path)
    return {"message": "Contributor removed"}
