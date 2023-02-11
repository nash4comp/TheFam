"""
This file is for bank management,

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji (taylor.ji719@gmail.com)
# Student number1: A01304056

UML diagram: https://app.diagrams.net/#G1DUxHF4SH4QveN8GbqGaHewuu07bC5lDG
"""

import datetime


class Bank:
    """
    Bank class handles everything related to Bank.
    Check and update the balance.
    """

    def __init__(self, account_number="", balance=0.0, bank_name=""):
        """
        Construct Bank.
        Transaction List will contain all the approved transactions.
        :param account_number: the account number
        :param balance: the balance
        """
        self._account_number = account_number
        self._balance = balance
        self._bank_name = bank_name
        self._transaction_list = []
        self._raw_temp_time = (datetime.datetime.now())
        self._time_stamp = self._raw_temp_time.strftime("%c")

    def is_enough_balance(self, transaction):
        """
        Check if the user has enough balance to add a new transaction
        :param transaction: the transaction to be added
        Return Boolean
        """
        is_enough = False
        if self._balance >= transaction.get_dollar_amount():
            is_enough = True
        else:
            print("Out of Balance. You cannot add a new transaction")
        return is_enough

    def update_balance(self, transaction):
        """
        Update the balance by subtracting the transaction's amount
        :param transaction: the transaction to be added
        """
        self.set_balance(self.get_balance() - transaction.get_dollar_amount())

    def get_account_number(self):
        """
        Getter for account number
        """
        return self._account_number

    def get_balance(self):
        """
        Getter for balance
        """
        return self._balance

    def get_bank_name(self):
        """
        Getter for bank name
        """
        return self._bank_name

    def set_account_number(self, account_number):
        """
        Setter for account number
        :param account_number: the account number
        """
        self._account_number = account_number

    def set_balance(self, balance):
        """
        Setter for balance
        :param balance: the balance
        """
        self._balance = balance

    def add_to_transaction_list(self, transaction):
        """
        Add a new transaction to the transaction list
        :param transaction: the transaction to be added
        """
        self._transaction_list.append(transaction)

    def show_all_approved_transactions(self):
        """
        Print all the approved transaction inside the bank
        """
        for transaction in self._transaction_list:
            print(transaction)

    def view_bank_account_menu(self):
        """
        Summary for the bank.
        Presents all the completed transactions up to date.
        Also, show the closing balance.
        """
        print(
            "========================================================================================================")
        self.show_all_approved_transactions()
        print(
            "========================================================================================================")
        statement = f"{self._time_stamp}: \nThe closing balance is: {self.get_balance()} "
        print(statement)

    def __str__(self):
        """
        String representation of the bank
        :return: the string representation of the bank
        """
        statement = f"Account number: {self.get_account_number()}," \
                    f"\nBalance %.2f{self.get_balance()}"
        return statement

    def set_bank_name(self, bank_name):
        """
        Setter for bank name
        :param bank_name: the bank name
        """
        self._bank_name = bank_name
