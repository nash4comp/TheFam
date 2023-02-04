""" TODO
Explanation

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji TODO: add email in here
# Student number1: A01304056

UML diagram: https://app.diagrams.net/#G1DUxHF4SH4QveN8GbqGaHewuu07bC5lDG
"""


from account import Account
# from test import Test
# from transaction import Transaction


class FAM:
    """
    This class is driver class for this program
    """

    def __init__(self):
        self._account = Account("")
        # self._test = Test()


def main():
    # test = Test()
    transaction = None
    user_list = None
    # transaction = Transaction(19.32, "Burger king")
    # user_list = test.load_test_user()
    my_account = Account(user_list)
    my_account.display_account_menu(transaction)


if __name__ == '__main__':
    main()
