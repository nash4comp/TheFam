import datetime
import time


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
        """
        self._time_stamp = (datetime.datetime.now())
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

    @staticmethod
    def show_transaction_by_budget():
        """
        Shows all the recorded transactions.
        For lab 4, it will print all the transaction stored in class attribute that is transaction list.
        The proper function will be updated later.
        """
        print("\n--- Transaction Record ---")
        for transaction in Transaction.transactions:
            print(transaction)

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

    def set_shop_name(self, user_input_shop_name):
        """
        Setter for shop_name
        :param user_input_shop_name
        """
        self._shop_name = user_input_shop_name



    def set_budget_type(self, user_input_budget_type):
        """
        Setter for shop_name
        :param user_input_shop_name
        """
        self._budget_type = user_input_budget_type

    def __str__(self):
        to_str = f"Date is {self.get_time()} and amount spent is  {self.get_dollar_amount()}, " \
                 f"Store name is {self.get_shop_name()}, budget type is {self.get_budget_type()}"
        return to_str


# test = Transaction(120, "Tim Hortons", "Eat out")
# Transaction.add_transactions_to_list(test)
# Transaction.show_transaction_by_budget()
# time.sleep(60)
# test = Transaction(300, "Mcdonalds", "Eat out")
# Transaction.add_transactions_to_list(test)
# Transaction.show_transaction_by_budget()
