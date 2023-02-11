"""
This file is for user account management.

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji (taylor.ji719@gmail.com)
# Student number2: A01304056

UML diagram: https://app.diagrams.net/#G1DUxHF4SH4QveN8GbqGaHewuu07bC5lDG
"""
import user
from budget import BudgetTypeEnum


class Account:
    """
    This class displays main menu.
    """

    def __init__(self, user_list):
        self._user_list = user_list

    def display_login_menu(self, users):
        """
        This method displays the login menu.
        :param users: the user object
        """
        print("\nWelcome to the FAM system.")
        print("Currently registered users are ")
        users.list_user(1)
        user_cnt = self._user_list.get_user_count()
        user_number = -1
        for index in range(user_cnt):
            self._user_list.set_login_status(index, False)
            index += 1
        while (user_number < 0) or (user_number > user_cnt):
            user_cnt = self._user_list.get_user_count()
            user_number = input("Log in as (If you are not registered, please enter 0.): ")
            if user_number == '':
                user_number = -1
            try:
                user_number = int(user_number)
            except ValueError:
                user_number = -1
            if int(user_number) == 0:
                if users.register_user() != -1:
                    for index in range(user_cnt):
                        self._user_list.set_login_status(index, False)
                        index += 1
                    user_number = -1
                    users.list_user(1)
                    continue
                else:
                    user_number = -1
            if (user_number < 1) or (user_number > user_cnt):
                user_number = -1
                continue
            if self._user_list.get_current_user_lock_status(user_number - 1):
                print("This user is locked out.")
                user_number = -1

        self._user_list.set_login_status(user_number, True)

    def display_account_menu(self, transaction, users):
        """
        This method displays the main menu.
        :param transaction: the transaction object
        :param users: the user object
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
            string_input = input("Please enter your choice (1-8)")

            if string_input == '':
                continue
            try:
                user_input = int(string_input)
            except ValueError:
                user_input = 0
            current_user = self._user_list.get_current_user(user_index)
            current_user_type = current_user.get_user_type()
            current_user_bank = self._user_list.get_current_bank(user_index)

            if user_input == 1:
                for budget in current_user. get_user_budgets_as_whole().values():
                    print(budget.budget_summary())
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                if current_user_type == user.UserTypes.REBEL.value and \
                        current_user.get_user_locked_out_status():
                    print("Your account has been locked. You rebel!!")
                else:
                    new_transaction = transaction.add_transaction()
                    new_transaction_type = new_transaction.get_budget_type_for_key()
                    current_user_budget_type = current_user.get_user_budget(new_transaction_type)
                    current_user_budget_type.setup_user_budget_type(current_user_type)
                    if current_user_bank.is_enough_balance(new_transaction):
                        if not current_user_budget_type.is_locked_budget(
                                new_transaction):  # if the budget is not locked
                            current_user.add_transaction_to_budget(new_transaction)
                            current_user_bank.update_balance(new_transaction)  # before updating bank balance
                            current_user_bank.add_to_transaction_list(new_transaction)
                        else:
                            if current_user_type == user.UserTypes.REBEL.value:
                                current_user_budget_type.prompt_strong_exceeding_message()
                                current_user.add_to_locked_budget_list(current_user_budget_type)
                                current_user.is_locked_user()
                            elif current_user_type == user.UserTypes.TROUBLE_MAKER.value:
                                current_user_budget_type.prompt_gentle_exceeding_message()
                                current_user.add_to_locked_budget_list(current_user_budget_type)
                            elif current_user_type == user.UserTypes.ANGEL.value:
                                print("Angel in us")
                                current_user_budget_type.prompt_angel_exceeding_message()
                            else:
                                print("Please check your user type")
                    else:
                        print("Out of balance!")
            elif user_input == 3:
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
                current_user_bank.view_bank_account_menu()
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
                      " number from 1 - 8.")
        print("Thank you for using the FAM system.")
        pass
