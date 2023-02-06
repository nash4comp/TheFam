class Bank:

    def __init__(self, account_number, balance, bank_name):
        self._account_number = account_number
        self._balance = balance
        self._bank_name = bank_name

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

    def __str__(self):
        statement = f"Account number: {self.get_account_number()}," \
                    f"Balance {self.get_balance()}"
        return statement

    def set_bank_name(self, bank_name):
        self._bank_name = bank_name
