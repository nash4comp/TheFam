class Account:
    """
    This class displays main menu.
    """

    def __init__(self, user_list):
        self._user_list = user_list
        # self._test = Test()

    def display_account_menu(self, transaction):

        user_input = None
        while user_input != 5:
            print("\nWelcome to the FAM system!!!")
            print("-----------------------")
            print("1. View Budgets")
            print("2. Record a Transaction")
            print("3. View Transactions by Budget")
            print("4. View Bank Account Details")
            print("5. Quit")
            string_input = input("Please enter your choice (1-5)")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                transaction.add_transaction()
                transaction.show_transaction_by_budget()
            elif user_input == 3:
                user_input = input("Press Enter to continue")
            elif user_input == 4:
                user_input = input("Press Enter to continue")
            elif user_input == 5:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 5.")

        print("Thank you for using the FAM system.")
        pass