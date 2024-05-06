from apiflask import APIBlueprint
from flask import request
from kink import di
from domain.access.access_interface import IAccess
from domain.repo.repo_interface import IRepo
from domain.access.decorators.access_decorator import verifyAccessToken, verifyCanCreate, verifyCreator
from domain.repo.schemas.repo_schema import RepoListSchema, RepoInputSchema

repo_app = APIBlueprint('repo_app', __name__)


@repo_app.get("/api/repo/list")
@repo_app.output(RepoListSchema)
@verifyAccessToken
def listRepoContributedByUser():
    repo = di[IRepo]
    access = di[IAccess]
    username = access.decodeAccessToken(request.headers.get("Access-token"))["username"]
    the_repos = repo.getRepoContributedBy(username)
    out_repos = []
    for r in the_repos:
        out_repos.append({'repo_path': r})
    return {"repos": out_repos}


@repo_app.post("/api/repo/create")
@repo_app.input(RepoInputSchema)
@verifyCanCreate
@verifyAccessToken
def createRepo(json_data):
    repo = di[IRepo]
    access = di[IAccess]
    username = access.decodeAccessToken(request.headers.get("Access-token"))["username"]
    repo.addRepo(json_data["repo_path"], username)
    return {"message": "Repo created"}


@repo_app.delete("/api/repo/remove")
@repo_app.input(RepoInputSchema)
@verifyAccessToken
def deleteRepo(json_data):
    access = di[IAccess]
    repo = di[IRepo]
    repo.verifyRepoExist(json_data['repo_path'])
    access.verifyCreator(request.headers.get("Access-token"), json_data["repo_path"])
    repo.removeRepo(json_data["repo_path"])
    return {"message": "Repo removed"}

