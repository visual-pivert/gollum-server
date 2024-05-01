from kink import di

import sqlite3

from domain.account.account_interface import IAccount
from domain.account.adapters.account_adapter import AccountAdapter
from domain.repoUtils.IRepoUtils import IRepoUtils
from domain.repoUtils.IRepoOutput import IRepoOutput
from domain.repoUtils.adapters.RepoUtilsAdapter import RepoUtilsAdapter
from domain.repoUtils.adapters.RepoOutputAdapter import RepoOutputAdapter
from domain.access.access_interface import IAccess
from domain.access.adapters.access_adatapter import AccessAdapter
from domain.user.user_model_interface import IUserModel
from domain.user.adapters.user_model_adapter import UserModelAdapter
from domain.security.security_interface import ISecurity
from domain.security.adapters.security_adapter import SecurityAdapter


class Bootstrap:
    def __init__(self):
        di["database"] = lambda _di: sqlite3.connect("/home/gollum/Project/gollum/var/database.db")
        di[IAccount] = lambda _di: AccountAdapter()
        di[IRepoUtils] = lambda _di: RepoUtilsAdapter("/home/gollum/Project/gollum/var/gitolite_test.conf")
        di[IRepoOutput] = lambda _di: RepoOutputAdapter()

        di[IAccess] = lambda _di: AccessAdapter()
        di[IUserModel] = lambda _di: UserModelAdapter(_di["database"])
        di[ISecurity] = lambda _di: SecurityAdapter()
