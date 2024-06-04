from apiflask import APIBlueprint
from flask import request
from kink import di
from domain.access.access_interface import IAccess
from domain.repo.repo_interface import IRepo
from domain.repo.schemas.repo_schema import RepoListSchema, RepoInputSchema
from domain.repo.repo_working_interface import IRepoWorking
from os import getenv

repo_app = APIBlueprint('repo_app', __name__)


@repo_app.get("/api/repo/list")
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
    return {"datas": out_repos, "status_code": 200, "message": "OK"}


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
    repo.addRepo(username + "/" + json_data["repo_path"], username)
    return {"message": "Repo created", "status_code": 201}


@repo_app.delete("/api/repo/delete")
@repo_app.input(RepoInputSchema)
def deleteRepo(json_data):
    access = di[IAccess]
    repo = di[IRepo]

    # Verification
    access_token = request.headers.get("Access-token")
    access.verifyAccessToken(access_token)
    
    username = access.decodeAccessToken(access_token)["username"]
    access.verifyCreator(access_token, username + "/" + json_data["repo_path"])

    repo.removeRepo(username + "/" + json_data["repo_path"])
    return {"message": "Repo removed", "status_code": 200}


# @Deprecated
@repo_app.get('/api/repo/get/<path:repo_path>/tree/<string:branch>', defaults={'tree_path': ''})
@repo_app.get("/api/repo/get/<path:repo_path>/tree/<string:branch>/<path:tree_path>")
def treeRepo(repo_path, branch, tree_path):
    access = di[IAccess]
    repo_working = di[IRepoWorking]

    # Verification
    access_token = request.headers.get("Access-Token")
    access.verifyAccessToken(access_token)
    access.verifyContributor(access_token, repo_path)

    repo_working.setRepoDir(getenv("REPO_DIR"))
    tree = repo_working.getTreeDirectory(repo_path, branch, tree_path)
    return {"datas": tree, "status_code": 200, "message": "OK"}


# @Deprecated
@repo_app.get("/api/repo/get/<path:repo_path>/blob/<string:branch>/<path:file_path>")
def blobRepo(repo_path, branch, file_path):
    access = di[IAccess]
    repo_working = di[IRepoWorking]

    # Verification
    access_token = request.headers.get("Access-Token")
    access.verifyAccessToken(access_token)
    access.verifyContributor(access_token, repo_path)

    repo_working.setRepoDir(getenv("REPO_DIR"))
    blob = repo_working.getBlobFile(repo_path, branch, file_path)
    return {'datas': {'blob': blob}, "status_code": 200, "message": "OK"}


# EDIT
@repo_app.post("/api/repo/get/<path:repo_path>/edit/<string:branch>/<path:tree_path>")
def editRepo(repo_path, tree_path):
    pass

@repo_app.get("/api/repo/branches/<path:repo_path>")
def listBranch(repo_path):
    access = di[IAccess]
    repo_working = di[IRepoWorking]

    # Verification
    access_token = request.headers.get("Access-Token")
    access.verifyAccessToken(access_token)
    access.verifyContributor(access_token, repo_path)

    repo_working.setRepoDir(getenv("REPO_DIR"))
    branch_list = repo_working.listBranches(repo_path)
    out_branch = []
    for branch in branch_list:
        out_branch.append({'branch_name': branch})

    return { 'datas': out_branch, "status_code": 200, "message": "OK"}
