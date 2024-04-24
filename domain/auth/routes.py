from flask import Flask, Blueprint, render_template, request, redirect, url_for
from domain.account.adapters.AccountAdapters import AccountAdapters
from domain.account.AccountEntity import AccountEntity
from domain.auth.forms.LoginForm import LoginForm

auth_app = Blueprint('auth_app', __name__, template_folder="./templates")


@auth_app.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if "POST" == request.method and form.validate():
        pass
    return render_template("login.html", form=form)
