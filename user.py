from enum import Enum

from bank import Bank
from budget import Budget
from transaction import Transaction


class UserTypes(Enum):
    ANGEL = "Angel"
    TROUBLE_MAKER = "Trouble Maker"
    REBEL = "Rebel"


class User:
    """
    This class manages users' information.
    """
    user_type_list = UserTypes

    def __init__(self, user_name="", user_age=0, user_type="", account_number="", balance=0, bank_name="", budget=0,
                 budget_limit=0):
        self._users = []
        self._user_name = user_name
        self._user_age = user_age
        self._user_type = user_type
        self._transaction = []
        self._budget = Budget(budget, budget_limit)
        self._bank = Bank(account_number, balance, bank_name)

    def get_user_name(self):
        return self._user_name

    def get_user_age(self):
        return self._user_age

    def get_user_type(self):
        return self._user_type

    def get_user_bank_account_number(self):
        return self._bank.get_account_number()

    def get_user_bank_balance(self):
        return self._bank.get_balance()

    def get_user_budget(self):
        return self._budget.get_total_budget()

    def get_warning_budget_limit(self):
        return self._budget.get_warning_budget_limit()

    def get_bank_name(self):
        return self._bank.get_bank_name()

    def register_user(self):
        new_user_name = input("Name: ")
        new_user_age = input("Age: ")
        new_user_type = input("Type: ")
        new_user_account_number = input("Account number: ")
        new_user_bank_name = input("Bank name: ")
        new_user_bank_balance = input("Bank balance: ")
        new_user_budget = input("Budget: ")
        new_user_budget_limit = input("Budget limit: ")

        self._users.append(
            User(user_name=new_user_name,
                 user_age=new_user_age,
                 user_type=new_user_type,
                 account_number=new_user_account_number,
                 balance=new_user_bank_balance,
                 budget=new_user_budget,
                 budget_limit=new_user_budget_limit,
                 bank_name=new_user_bank_name))

    def list_user(self):
        for user_data in self._users:
            print(user_data.get_user_name(),
                  user_data.get_user_age(),
                  user_data.get_user_type(),
                  user_data.get_user_bank_account_number(),
                  user_data.get_user_budget(),
                  user_data.get_warning_budget_limit(),
                  user_data.get_user_bank_balance(),
                  user_data.get_bank_name()
                  )

    def remove_user(self):
        pass

    def set_user_name(self, name):
        self._user_name = name

    def set_user_age(self, age):
        self._user_age = age

    def set_user_type(self, user_type):
        self._user_type = user_type

    def set_user_bank_account_number(self, account_number):
        self._bank.set_account_number(account_number)

    def set_user_bank_balance(self, balance):
        self._bank.set_balance(balance)

    def set_user_budget(self, budget):
        self._budget.set_total_budget(budget)

    def set_warning_budget_limit(self, budget_limit):
        self._budget.set_warning_budget_limit(budget_limit)

    def set_bank_name(self, bank_name):
        return self._bank.set_bank_name(bank_name)
