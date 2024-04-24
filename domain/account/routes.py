from flask import Flask, Blueprint, render_template, request, redirect, url_for
from domain.account.adapters.AccountAdapters import AccountAdapters
from domain.account.AccountEntity import AccountEntity
from domain.account.forms.CreateAccountForm import CreateAccountForm

account_app = Blueprint('account_app', __name__, template_folder="./templates")


@account_app.route("/account", methods=['POST', 'GET'])
def createAccount():
    form = CreateAccountForm(request.form)
    if "POST" == request.method and form.validate():
        new_account = AccountEntity()
        new_account.username = form.username.data
        new_account.email = form.email.data
        new_account.password = form.password.data
        AccountAdapters.createAccount(new_account)
        return redirect(url_for('index'))
    return render_template("account.html", form=form)
