"""
TODO Taylor: Write a description here

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji (taylor.ji719@gmail.com)
# Student number1: A01304056

UML diagram: https://app.diagrams.net/#G1DUxHF4SH4QveN8GbqGaHewuu07bC5lDG
"""


class Bank:

    def __init__(self, account_number="", balance=0.0, bank_name=""):
        self._account_number = account_number
        self._balance = balance
        self._bank_name = bank_name

    def is_enough_balance(self, transaction):
        """
        TODO Taylor: Write a description here
        :param transaction:
        :return:
        """
        """
        Check if the user has enough balance to add a new transaction
        """
        is_enough = False
        if self._balance >= transaction.get_dollar_amount():
            is_enough = True
        else:
            print("Out of Balance. You cannot add a new transaction")
        return is_enough

    def update_balance(self, transaction):
        self.set_balance(self.get_balance() - transaction.get_dollar_amount())

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def get_bank_name(self):
        return self._bank_name

    def set_account_number(self, account_number):
        self._account_number = account_number

    def set_balance(self, balance):
        self._balance = balance

    def __str__(self):
        statement = f"Account number: {self.get_account_number()}," \
                    f"Balance {self.get_balance()}"
        return statement

    def set_bank_name(self, bank_name):
        self._bank_name = bank_name
