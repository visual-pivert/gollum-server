from kink import di

import sqlite3

from domain.account.IAccount import IAccount
from domain.account.adapters.AccountAdapter import AccountAdapter


class Bootstrap:
    def __init__(self):
        di["database"] = lambda _di: sqlite3.connect("/home/gollum/Project/gollum/var/database.db")
        di[IAccount] = lambda _di: AccountAdapter(_di["database"])
