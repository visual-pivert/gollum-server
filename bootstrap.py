from kink import di

from domain.account.IAccount import IAccount
from domain.account.adapters.AccountAdapters import AccountAdapters


class Boostrap:
    def __init__(self):
        di[IAccount] = AccountAdapters()
