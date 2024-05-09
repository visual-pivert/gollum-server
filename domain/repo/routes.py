from apiflask import APIBlueprint
from flask import request
from kink import di
from domain.access.access_interface import IAccess
from domain.repo.repo_interface import IRepo
from domain.repo.schemas.repo_schema import RepoListSchema, RepoInputSchema
from domain.repo.repo_working_interface import IRepoWorking

repo_app = APIBlueprint('repo_app', __name__)


@repo_app.get("/api/repo/list")
@repo_app.output(RepoListSchema)
def listRepoContributedByUser():
    repo = di[IRepo]
    access = di[IAccess]

    # Verification
    access_token = request.headers.get("Access-token")
    access.verifyAccessToken(access_token)

    username = access.decodeAccessToken(access_token)["username"]
    the_repos = repo.getRepoContributedBy(username)
    out_repos = []
    for r in the_repos:
        out_repos.append({'repo_path': r})
    return {"repos": out_repos}


@repo_app.post("/api/repo/create")
@repo_app.input(RepoInputSchema)
def createRepo(json_data):
    repo = di[IRepo]
    access = di[IAccess]

    # Verification
    access_token = request.headers.get("Access-token")
    access.verifyAccessToken(access_token)
    access.verifyCanCreate(access_token)

    username = access.decodeAccessToken(access_token)["username"]
    repo.addRepo(json_data["repo_path"], username)
    return {"message": "Repo created"}


@repo_app.delete("/api/repo/delete")
@repo_app.input(RepoInputSchema)
def deleteRepo(json_data):
    access = di[IAccess]
    repo = di[IRepo]

    # Verification
    access_token = request.headers.get("Access-token")
    access.verifyAccessToken(access_token)
    access.verifyCreator(access_token, json_data["repo_path"])

    repo.removeRepo(json_data["repo_path"])
    return {"message": "Repo removed"}


# @Deprecated
@repo_app.get('/api/repo/get/<path:repo_path>/tree/<string:branch>', defaults={'tree_path': ''})
@repo_app.get("/api/repo/get/<path:repo_path>/tree/<string:branch>/<path:tree_path>")
def treeRepo(repo_path, branch, tree_path):
    access = di[IAccess]
    repo_working = di[IRepoWorking]

    repo_working.setRepoDir('/home/gollum/gollum_repo/')
    tree = repo_working.getTreeDirectory(repo_path, branch, tree_path)
    return {"tree": tree}


# @Deprecated
@repo_app.get("/api/repo/get/<path:repo_path>/blob/<string:branch>/<path:file_path>")
def blobRepo(repo_path, branch, file_path):
    access = di[IAccess]
    repo_working = di[IRepoWorking]

    repo_working.setRepoDir('/home/gollum/gollum_repo/')
    glob = repo_working.getBlobFile(repo_path, branch, file_path)
    return {'glob': glob}


# EDIT
@repo_app.post("/api/repo/get/<path:repo_path>/edit/<string:branch>/<path:tree_path>")
def editRepo(repo_path, tree_path):
    pass