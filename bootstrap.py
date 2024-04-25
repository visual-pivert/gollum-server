from kink import di

import sqlite3

from domain.account.IAccount import IAccount
from domain.account.adapters.AccountAdapters import AccountAdapters


class Boostrap:
    def __init__(self):
        di["database"] = lambda _di: sqlite3.connect("/home/gollum/Project/gollum/var/database.db")
        di[IAccount] = lambda _di: AccountAdapters(_di["database"])
