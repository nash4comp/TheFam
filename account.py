import user
from budget import BudgetTypeEnum


class Account:
    """
    This class displays main menu.
    """

    def __init__(self, user_list):
        self._user_dict = user_list  # dictionary

    def display_login_menu(self, users):
        print("Currently registered users are ")
        users.list_user(1)
        user_cnt = self._user_dict.get_user_count()
        user_number = 0
        for index in range(user_cnt):
            self._user_dict.set_login_status(index, False)
            index += 1
        while (user_number < 1) or (user_number > user_cnt):
            user_number = input("Log in as: ")
            if user_number == '':
                user_number = -1
            try:
                user_number = int(user_number)
            except ValueError:
                user_number = -1

        self._user_dict.set_login_status(user_number, True)

    def display_account_menu(self, transaction, users):
        users.quick_add_user()
        self.display_login_menu(users)
        user_input = None
        current_user_index = users.get_current_user_index()
        while user_input != 0:
            print(f"\nHello, {self._user_dict.get_current_user_name(current_user_index)}!")
            print("Welcome to the FAM system.")
            print("-----------------------")
            print("1. View Budgets")
            print("2. Record a Transaction")
            print("3. View Transactions by Budget")
            print("4. View Bank Account Details")
            print("---<User management>---")
            print("6. Register User")
            print("7. List up Users")
            print("9. Switch User")
            print("0. Quit")
            string_input = input("Please enter your choice (0-9)")

            if string_input == '':
                continue
            user_input = int(string_input)
            current_user = self._user_dict.get_current_user(current_user_index)
            current_user_type = current_user.get_user_type()
            current_user_bank = self._user_dict.get_current_bank(current_user_index)

            if user_input == 1:
                for budget in current_user.get_user_budget_dict().values():
                    print(budget.budget_summary())
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                if current_user_type == user.UserTypes.REBEL.value and \
                        current_user.is_locked_user():
                    print("Your account has been locked.")

                else:
                    new_transaction = transaction.add_transaction()
                    new_transaction_type = new_transaction.get_budget_type_for_key()
                    current_user_budget_type = current_user.get_user_budget(new_transaction_type)
                    # print(current_user_budget_type)
                    print(current_user.get_user_type())
                    current_user_budget_type.setup_user_budget_type(current_user_type)
                    if current_user_bank.is_enough_balance(new_transaction):
                        if not current_user_budget_type.is_locked_budget(
                                new_transaction):  # if the budget is not locked
                            current_user_bank.update_balance(new_transaction)  # before updating bank balance
                            current_user_bank.add_to_transaction_list(new_transaction)
                            current_user.add_transaction_to_budget(new_transaction)
                        else:
                            print("Sorry your budget is locked. You cannot record new transaction")
                            current_user.add_to_locked_budget_list(current_user_budget_type)
                    else:
                        print("Out of balance!")
            elif user_input == 3:  # show transaction by budget
                print("Please select one budget")
                print("-----------------------")
                print("1. Game and Entertainment")
                print("2. Clothing and Accessories")
                print("3. Eating Out")
                print("4. Miscellaneous")
                budget_type_helper = None
                to_show_user_budget_type = int(input("Enter the budget type number: "))
                if to_show_user_budget_type == 1:
                    print("Game and Entertainment")
                    print("==============================================================")
                    budget_type_helper = current_user.get_user_budget(BudgetTypeEnum.GE.name)
                    budget_type_helper.show_budget_record()
                elif to_show_user_budget_type == 2:
                    print("Clothing and Accessories")
                    print("==============================================================")
                    budget_type_helper = current_user.get_user_budget(BudgetTypeEnum.CA.name)
                    budget_type_helper.show_budget_record()
                elif to_show_user_budget_type == 3:
                    print("Eat out Category")
                    print("==============================================================")
                    budget_type_helper = current_user.get_user_budget(BudgetTypeEnum.EO.name)
                    budget_type_helper.show_budget_record()
                elif to_show_user_budget_type == 4:
                    print("Miscellaneous")
                    print("==============================================================")
                    budget_type_helper = current_user.get_user_budget(BudgetTypeEnum.MIS.name)
                    budget_type_helper.show_budget_record()
                user_input = input("Press Enter to continue")
            elif user_input == 4:
                # print all the approved transactions up to now
                # print the closing balance
                # bank method to print out the all the approved transactions
                current_user_bank.view_bank_account_menu()
                user_input = input("Press Enter to continue")
            elif user_input == 6:
                users.register_user()
            elif user_input == 7:
                users.list_user(0)
            elif user_input == 9:
                self.display_login_menu(users)
            elif user_input == 0:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 5.")

        print("Thank you for using the FAM system.")
        pass
