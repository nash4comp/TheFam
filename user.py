from budget import Budget
from transaction import Transaction


class User:
    """
    This class manages users' information.
    """

    def __init__(self, user_name, user_age, user_type):
        self._user_name = user_name
        self._user_age = user_age
        self._user_type = user_type
        self._transaction = Transaction()
        self._budget = Budget()

    def get_user_name(self):
        return self._user_name

    def get_user_age(self):
        return self._user_age

    def get_user_type(self):
        return self._user_type

    # Should be parsed from Bank class
    def get_user_bank_account_number(self):
        pass

    # Should be parsed from Bank class
    def get_user_bank_balance(self):
        pass

    # Should be parsed from Budget class
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

    # Should be called the method from Bank class
    def set_user_bank_account_number(self, account_number):
        pass

    # Should be called the method from Bank class
    def set_user_bank_balance(self):
        self.
        pass

    # Should be called the method from Budget class
    def set_user_budget(self):
        pass
