import datetime


class Transaction:
    """
    Transaction class creates transactions,
    """
    transactions = []

    def __init__(self, dollar_amount, shop_name):
        """
        initialize transaction with dollar amount you spent, and the store name
        :param dollar_amount: positive float
        :param shop_name: string
        """
        self._time_stamp = (datetime.datetime.now())
        self._dollar_amount = dollar_amount
        self._shop_name = shop_name

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
        print(f"\nYou spent {self.get_dollar_amount()} at {self.get_shop_name()}\n")
        transaction_to_add = Transaction(self.get_dollar_amount(), self.get_shop_name())
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

    def show_transaction_by_budget(self):
        """
        Shows all the recorded transactions.
        For lab 4, it will print all the transaction stored in class attribute that is transaction list.
        The proper function will be updated later.
        """
        print("\n--- Transaction Record ---")
        for transaction in Transaction.transactions:
            print(f"You spent {transaction.get_dollar_amount()} at {transaction.get_shop_name()}")

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

    def set_shop_name(self, user_input_shop_name):
        """
        Setter for shop_name
        :param user_input_shop_name
        """
        self._shop_name = user_input_shop_name