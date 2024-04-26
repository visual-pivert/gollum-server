from kink import di

import sqlite3

from domain.account.IAccount import IAccount
from domain.account.adapters.AccountAdapter import AccountAdapter
from domain.auth.IAuth import IAuth
from domain.auth.adapters.AuthAdapter import AuthAdapter


class Bootstrap:
    def __init__(self):
        di["database"] = lambda _di: sqlite3.connect("/home/gollum/Project/gollum/var/database.db", check_same_thread=False)
        di[IAccount] = lambda _di: AccountAdapter(_di["database"])
        di[IAuth] = lambda _di: AuthAdapter(_di["database"])
