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
        """
        self._account_number = account_number

    def set_balance(self, balance):
        """
        Setter for balance
        """
        self._balance = balance

    def add_to_transaction_list(self, transaction):
        """
        Add a new transaction to the transaction list
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
        statement = f"Account number: {self.get_account_number()}," \
                    f"\nBalance %.2f{self.get_balance()}"  # format to have 2 decimal numbers
        return statement

    def set_bank_name(self, bank_name):
        """
        Setter for bank name
        """
        self._bank_name = bank_name
