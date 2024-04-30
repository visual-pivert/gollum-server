from flask import Flask, Blueprint, render_template, request, redirect, url_for, session, flash
from kink import di
from domain.repoUtils.IRepoUtils import IRepoUtils
from domain.repoUtils.IRepoOutput import IRepoOutput

repo_app = Blueprint('repo_app', __name__, template_folder="./templates")


@repo_app.route("/", methods=['POST', 'GET'])
def home():
    # injection de dependance
    repo_utils = di[IRepoUtils]
    repo_output = di[IRepoOutput]

    repo_output.setConfiguration(repo_utils.getState())
    user_repo = repo_output.getRepoContributedBy('username2')

    return render_template("home.html", user_repo=user_repo)
