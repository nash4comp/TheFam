"""
This is the driver class for this program.

The program is a prototype of a parental control for a bank account which is called
F.A.M. (Family Appointed Moderator). It acts as a parental control for a bank account.
It allows parents to set a budget for their children and monitor their spending.

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji (taylor.ji719@gmail.com)
# Student number2: A01304056

UML diagram: https://app.diagrams.net/#G1DUxHF4SH4QveN8GbqGaHewuu07bC5lDG
"""
from account import Account
from bank import Bank

from test import Test
from transaction import Transaction
from user import User


class FAM:
    """
    This class is driver class for this program
    """

    def __init__(self):
        self._account = Account("")
        self._test = Test()


def main():
    test = Test()
    bank = Bank("a1302", 120.85, "td")
    users = User("Test", 13, "Angel", "a1302", "td", 120.85, [[100, 60], [200, 120],
                                                              [400, 50], [120, 60]])
    transaction = Transaction(0.0, "test", "GE")
    my_account = Account(users)
    my_account.display_account_menu(transaction, users, bank)
    # transaction = Transaction(19.32, "Burger king")

    # test_user = User("Ryu", 25, user.UserTypes.ANGEL.value, "5678", [[200, 200], [200, 200], [200, 200], [200, 200]], 700)
    #
    # my_account = Account(test_user)
    # test_bank = Bank("A0000", 200)
    # test_transaction = Transaction(100, "test", "Eat out")
    # my_account.display_account_menu(test_transaction, test_bank)  # test user Ken


if __name__ == '__main__':
    main()
