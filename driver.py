""" TODO
Explanation

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji TODO: add email in here
# Student number1: A01304056

UML diagram: https://app.diagrams.net/#G1DUxHF4SH4QveN8GbqGaHewuu07bC5lDG
"""
import user
from account import Account
from bank import Bank
from budget import Budget

from transaction import Transaction
from user import User


class FAM:
    """
    This class is driver class for this program
    """

    def __init__(self):
        self._account = Account("")
        # self._test = Test()


def main():
    u1 = User(user_name="Tim",
              user_age=12,
              user_type="Angel",
              account_number="1234567",
              balance=1000,
              budget=[[100, 90], [200, 180], [300, 270], [400, 360]],
              bank_name="TD")

    users = u1
    transaction_driver = Transaction(0.0, "test", "GE")

    my_account = Account(users)
    my_account.display_account_menu(transaction_driver, users)



if __name__ == '__main__':
    main()
