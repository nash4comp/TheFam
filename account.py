from user import User


class Account:
    """
    This class displays main menu.
    """

    def __init__(self, user_list):
        self._user_list = user_list
        self._user = User
        # self._test = Test()

    def display_account_menu(self, transaction, users, bank):

        users.quick_add_user()
        user_input = None
        while user_input != 0:
            print("\nWelcome to the FAM system!!!")
            print("-----------------------")
            print("1. View Budgets")
            print("2. Record a Transaction")
            print("3. View Transactions by Budget")
            print("4. View Bank Account Details")
            print("---<User management>---")
            print("6. Register User")
            print("7. List up Users")
            print("8. Remove User")
            print("0. Quit")
            string_input = input("Please enter your choice (0-9)")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                new_transaction = transaction.add_transaction()
                if bank.is_enough_balance(new_transaction):
                    bank.update_balance(new_transaction)
                    self._user_list.add_transaction_to_budget(new_transaction)  # test user Ken
                else:
                    print("User type error message")
            elif user_input == 3:  # show transaction by budget
                self._user_list.show_transaction_by_budget()
                user_input = input("Press Enter to continue")
            elif user_input == 4:
                print(bank)
                user_input = input("Press Enter to continue")
            elif user_input == 6:
                users.register_user()
            elif user_input == 7:
                users.list_user()
            elif user_input == 0:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 5.")

        print("Thank you for using the FAM system.")
        pass
