from bank import Bank
from budget import Budget
from transaction import Transaction


class User:
    """
    This class manages users' information.
    """

    def __init__(self, user_name, user_age, user_type, account_number, budget, balance):
        self._user_name = user_name
        self._user_age = user_age
        self._user_type = user_type
        self._transaction = Transaction()
        self._budget = Budget(budget)
        self._bank = Bank(account_number, balance)

    def get_user_name(self):
        return self._user_name

    def get_user_age(self):
        return self._user_age

    def get_user_type(self):
        return self._user_type

    def get_user_bank_account_number(self):
        return self._bank.get_account_number()

    def get_user_bank_balance(self):
        return self.get_user_bank_balance()

    def get_user_budget(self):
        pass

    def add_new_user(self):
        pass

    def remove_user(self):
        pass

    def set_user_name(self, name):
        self._user_name = name

    def set_user_age(self, age):
        self._user_age = age

    def set_user_type(self, type):
        self._user_type = type

    def set_user_bank_account_number(self, account_number):
        self._bank.set_account_number(account_number)

    def set_user_bank_balance(self, balance):
        self._bank.set_balance(balance)

    # Should be called the method from Budget class
    def set_user_budget(self):
        pass
