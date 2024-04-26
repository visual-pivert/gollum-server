from flask import Flask, Blueprint, render_template, request, redirect, url_for, session, flash
from domain.account.adapters.AccountAdapter import AccountAdapter
from domain.account.AccountEntity import AccountEntity
from domain.auth.forms.LoginForm import LoginForm
from kink import di
from domain.auth.IAuth import IAuth

auth_app = Blueprint('auth_app', __name__, template_folder="./templates")


@auth_app.route("/login", methods=['POST', 'GET'])
def login():
    # injection de dependance
    auth = di[IAuth]

    form = LoginForm(request.form)
    if "POST" == request.method and form.validate():
        try:
            auth.login(form.username.data, form.password.data, False)
        except Exception as e:
            flash(e.args[0])


    if auth.loggedUser():
        return auth.loggedUser().username + ' <span style="color: green">CONNECTED</span>'

    return render_template("login.html", form=form)


@auth_app.route("/logout", methods=['GET'])
def logout():
    # injection de dependance
    auth = di[IAuth]
    auth.logout()
    return redirect(url_for('auth_app.login'))
