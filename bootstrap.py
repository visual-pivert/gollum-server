from kink import di

import sqlite3

from domain.account.account_interface import IAccount
from domain.account.adapters.account_adapter import AccountAdapter
from domain.access.access_interface import IAccess
from domain.access.adapters.access_adatapter import AccessAdapter
from domain.user.user_model_interface import IUserModel
from domain.user.adapters.user_model_adapter import UserModelAdapter
from domain.security.security_interface import ISecurity
from domain.security.adapters.security_adapter import SecurityAdapter
from domain.gitolite.gitolite_interface import IGitolite
from domain.gitolite.adapters.gitolite_adapter import GitoliteAdapter
from domain.contrib.contrib_interface import IContrib
from domain.contrib.adapters.contrib_adapter import ContribAdapter
from domain.repo.repo_interface import IRepo
from domain.repo.adapters.repo_adapter import RepoAdapter


class Bootstrap:
    def __init__(self):
        di["database"] = lambda _di: sqlite3.connect("/home/gollum/Project/gollum/var/database.db")
        di[IAccount] = lambda _di: AccountAdapter()
        di[IAccess] = lambda _di: AccessAdapter()
        di[IUserModel] = lambda _di: UserModelAdapter(_di["database"])
        di[ISecurity] = lambda _di: SecurityAdapter()
        di[IGitolite] = lambda _di: GitoliteAdapter()
        di[IContrib] = lambda _di: ContribAdapter()
        di[IRepo] = lambda _di: RepoAdapter()