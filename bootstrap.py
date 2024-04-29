from kink import di

import sqlite3

from domain.account.IAccount import IAccount
from domain.account.adapters.AccountAdapter import AccountAdapter
from domain.auth.IAuth import IAuth
from domain.auth.adapters.AuthAdapter import AuthAdapter
from domain.repoUtils.IRepoUtils import IRepoUtils
from domain.repoUtils.IRepoOutput import IRepoOutput
from domain.repoUtils.adapters.RepoUtilsAdapter import RepoUtilsAdapter
from domain.repoUtils.adapters.RepoOutputAdapter import RepoOutputAdapter

class Bootstrap:
    def __init__(self):
        di["database"] = lambda _di: sqlite3.connect("/home/gollum/Project/gollum/var/database.db")
        di[IAccount] = lambda _di: AccountAdapter(_di["database"])
        di[IAuth] = lambda _di: AuthAdapter(_di["database"])
        di[IRepoUtils] = lambda _di: RepoUtilsAdapter("/home/gollum/Project/gollum/var/gitolite_test.conf")
        di[IRepoOutput] = lambda _di: RepoOutputAdapter()