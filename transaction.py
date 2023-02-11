"""
TODO Taylor: Write a description here

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji (taylor.ji719@gmail.com)
# Student number2: A01304056

UML diagram: https://app.diagrams.net/#G1DUxHF4SH4QveN8GbqGaHewuu07bC5lDG
"""

import datetime
from budget import BudgetTypeEnum


class Transaction:
    """
    Transaction class creates transactions,
    """
    transactions = []

    def __init__(self, dollar_amount, shop_name, budget_type):
        """
        initialize transaction with dollar amount you spent, and the store name
        :param dollar_amount: positive float
        :param shop_name: string
        :param budget_type: string
        """
        self._raw_temp_time = (datetime.datetime.now())
        self._time_stamp = self._raw_temp_time.strftime("%c")
        self._dollar_amount = dollar_amount
        self._shop_name = shop_name
        self._budget_type = budget_type

    def add_transaction(self):
        """
        This method returns a transaction that will be saved under user class.
        For lab 4, I create a transaction list that stores transactions.
        :return: Transaction
        """
        user_input_store_name = input("Enter the place you went: ")
        self.set_shop_name(user_input_store_name)
        user_input_dollar_amount = float(input("Enter the amount you spent: "))
        self.set_dollar_amount(user_input_dollar_amount)
        print("Please select one budget type")
        print("1. Game and Entertainment")
        print("2. Clothing and Accessories")
        print("3. Eating Out")
        print("4. Miscellaneous")
        user_budget_type = int(input("Enter the budget type number: "))
        if user_budget_type == 1:
            self.set_budget_type("Game and Entertainment")
        elif user_budget_type == 2:
            self.set_budget_type("Clothing and Accessories")
        elif user_budget_type == 3:
            self.set_budget_type("Eat out")
        elif user_budget_type == 4:
            self.set_budget_type("Miscellaneous")
        transaction_to_add = Transaction(self.get_dollar_amount(), self.get_shop_name(), self.get_budget_type())
        Transaction.add_transactions_to_list(transaction_to_add)
        return transaction_to_add

    @classmethod
    def add_transactions_to_list(cls, transaction):
        """
        Save transactions to the transaction list.
        Used for lab4, transactions will be stored into user's transaction list.
        :param transaction
        """
        cls.transactions.append(transaction)

    def get_time(self):
        """
        Getter for dollar amount.
        :return: self._dollar_amount
        """
        return self._time_stamp

    def get_dollar_amount(self):
        """
        Getter for dollar amount.
        :return: self._dollar_amount
        """
        return self._dollar_amount

    def set_dollar_amount(self, user_input_dollar_amount):
        """
        Setter for dollar_amount.
        :param user_input_dollar_amount
        """
        self._dollar_amount = user_input_dollar_amount

    def get_shop_name(self):
        """
        Getter for shop_name.
        :return: self._shop_name
        """
        return self._shop_name

    def get_budget_type(self):
        """
        Getter for dollar amount.
        :return: self._dollar_amount
        """
        return self._budget_type

    def get_budget_type_for_key(self):
        """
        Convert budget type string value to Enum class name
        Return String
        """
        type_to_change = self.get_budget_type()
        key = None
        if type_to_change == BudgetTypeEnum.GE.value:
            key = BudgetTypeEnum.GE.name
        elif type_to_change == BudgetTypeEnum.CA.value:
            key = BudgetTypeEnum.CA.name
        elif type_to_change == BudgetTypeEnum.EO.value:
            key = BudgetTypeEnum.EO.name
        elif type_to_change == BudgetTypeEnum.MIS.value:
            key = BudgetTypeEnum.MIS.name
        return key

    def set_shop_name(self, user_input_shop_name):
        """
        Setter for shop_name
        :param user_input_shop_name
        """
        self._shop_name = user_input_shop_name

    def set_budget_type(self, user_input_budget_type):
        """
        Setter for shop_name
        :param user_input_budget_type
        """
        self._budget_type = user_input_budget_type

    def __str__(self):
        """
        String representation of Transaction class
        :return: string to print
        """
        to_str = f"Budget type is {self.get_budget_type()}, Date is {self.get_time()}, " \
                 f"Amount spent is ${self.get_dollar_amount()}, " \
                 f"Store name is {self.get_shop_name()}"
        return to_str
