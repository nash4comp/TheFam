import datetime
class Bank:

    def __init__(self, account_number="", balance=0.0, bank_name=""):
        self._account_number = account_number
        self._balance = balance
        self._bank_name = bank_name
        self._transaction_list = []
        self._raw_temp_time = (datetime.datetime.now())
        self._time_stamp = self._raw_temp_time.strftime("%c")

    def is_enough_balance(self, transaction):
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

    def add_to_transaction_list(self, transaction):
        self._transaction_list.append(transaction)

    def show_all_approved_transactions(self):
        """
        Print all the approved transaction inside the bank
        """
        for transaction in self._transaction_list:
            print(transaction)

    def view_bank_account_menu(self):
        print("========================================================================================================")
        self.show_all_approved_transactions()
        print("========================================================================================================")
        statement = f"{self._time_stamp}: \nThe closing balance is: {self.get_balance()} "
        print(statement)



    def __str__(self):
        statement = f"Account number: {self.get_account_number()}," \
                    f"\nBalance {self.get_balance()}"
        return statement

    def set_bank_name(self, bank_name):
        self._bank_name = bank_name
