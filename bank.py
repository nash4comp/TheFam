class Bank:

    def __init__(self, account_number, balance, bank_name):
        self._account_number = account_number
        self._balance = balance
        self._bank_name = bank_name

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

    def set_bank_name(self, bank_name):
        self._bank_name = bank_name
