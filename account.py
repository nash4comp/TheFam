"""
This file is for user account management.

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji (taylor.ji719@gmail.com)
# Student number2: A01304056

UML diagram: https://app.diagrams.net/#G1DUxHF4SH4QveN8GbqGaHewuu07bC5lDG
"""


class Account:
    """
    This class displays main menu.
    """

    def __init__(self, user_list):
        self._user_list = user_list

    def display_login_menu(self, users):
        """
        TODO Clean up this menu items
        This method displays the login menu.
        :param users: the user object
        """
        print("\nWelcome to the FAM system.")
        print("Currently registered users are ")
        users.list_user(1)
        user_cnt = self._user_list.get_user_count()
        user_number = 0
        for index in range(user_cnt):
            self._user_list.set_login_status(index, False)
            index += 1
        while (user_number < 1) or (user_number > user_cnt):
            user_number = input("Log in as: ")
            if user_number == '':
                user_number = -1
            try:
                user_number = int(user_number)
            except ValueError:
                user_number = -1
            if self._user_list.get_current_user_lock_status(user_number - 1):
                print("This user is locked out.")
                user_number = -1

        self._user_list.set_login_status(user_number, True)

    def display_account_menu(self, transaction, users, bank):
        """
        This method displays the main menu.
        :param transaction: the transaction object
        :param users: the user object
        :param bank: the bank object
        """
        users.quick_add_user()
        self.display_login_menu(users)
        user_input = None
        while user_input != 8:
            user_index = users.get_current_user_index()
            print(
                f"\nHello, {self._user_list.get_current_user_name(user_index)} "
                f"({self._user_list.get_current_user_type(user_index)})!")
            print("-----------------------")
            print("1. View Budgets")
            print("2. Record a Transaction")
            print("3. View Transactions by Budget")
            print("4. View Bank Account Details")
            print("5. Register User")
            print("6. List up Users")
            print("7. Switch User")
            print("8. Quit")
            string_input = input("Please enter your choice (0-8)")

            if string_input == '':
                continue
            user_input = int(string_input)

            if user_input == 1:
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                new_transaction = transaction.add_transaction()
                if bank.is_enough_balance(new_transaction):
                    bank.update_balance(new_transaction)
                    users.add_transaction_to_budget(new_transaction)  # test user Ken
                else:
                    print("User type error message")
            elif user_input == 3:  # show transaction by budget
                users.show_transaction_by_budget()
                user_input = input("Press Enter to continue")
            elif user_input == 4:
                print(bank)
                user_input = input("Press Enter to continue")
            elif user_input == 5:
                users.register_user()
            elif user_input == 6:
                users.list_user(0)
            elif user_input == 7:
                self.display_login_menu(users)
            elif user_input == 8:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 5.")
        print("Thank you for using the FAM system.")
        pass
