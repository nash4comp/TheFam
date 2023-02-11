"""
This file manages users' information. And it also supports user management.

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji (taylor.ji719@gmail.com)
# Student number2: A01304056

UML diagram: https://app.diagrams.net/#G1DUxHF4SH4QveN8GbqGaHewuu07bC5lDG
"""
from enum import Enum
from bank import Bank
from budget import Budget
from budget import BudgetTypeEnum

ANGEL_LIMIT_FACTOR = 0.9
TROUBLEMAKER_LIMIT_FACTOR = 0.75
REBEL_LIMIT_FACTOR = 0.5


class UserTypes(Enum):
    """
    This class defines three different user types.
    """
    ANGEL = "Angel"
    TROUBLE_MAKER = "Trouble Maker"
    REBEL = "Rebel"


class User:
    """
    This class manages users' information.
    """
    user_type_list = UserTypes

    def __init__(self, user_name="", user_age=0, user_type="", account_number="", balance=0.0, bank_name="",
                 budget=None, login_status=False, is_locked_out=False):
        """
        This method initializes the user object.
        :param user_name: user name
        :param user_age: user age
        :param user_type: user type
        :param account_number: user's bank account number
        :param balance: user's bank account balance
        :param bank_name: user's bank name
        :param budget: user's budget
        :param login_status: user's login status
        :param is_locked_out: user's lock status
        """
        if budget is None:
            budget = [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]]
        self._users = []
        self._user_name = user_name
        self._user_age = user_age
        self._user_type = user_type
        self._transaction = []
        self._bank = Bank(account_number, balance, bank_name)
        self._budget = {"GE": Budget("Game and Entertainment", budget[0][0], budget[0][1]),
                        "CA": Budget("Clothing and Accessories", budget[1][0], budget[1][1]),
                        "EO": Budget("Eating Out", budget[2][0], budget[2][1]),
                        "MIS": Budget("Miscellaneous", budget[3][0], budget[3][1])
                        }
        self._locked_budget_list = []
        self.login_status = login_status
        self._is_locked_out = is_locked_out

    def add_transaction_to_budget(self, transaction):
        """
        This method adds a transaction to the budget.
        :param transaction: transaction object
        """
        budget_type_of_transaction = transaction.get_budget_type()
        if budget_type_of_transaction == BudgetTypeEnum.GE.value:
            game_entertainment = self._budget.get("GE")  # GE budget
            game_entertainment.add_transaction(transaction)
            print(transaction)
        elif budget_type_of_transaction == BudgetTypeEnum.CA.value:
            clothing_accessories = self._budget.get("CA")
            clothing_accessories.add_transaction(transaction)
            print(transaction)
            # print(clothing_accessories.show_budget_record())
        elif budget_type_of_transaction == BudgetTypeEnum.EO.value:
            eo = self._budget.get("EO")  # GE budget
            eo.add_transaction(transaction)
            print(transaction)
            # print(eo.show_budget_record())
        elif budget_type_of_transaction == BudgetTypeEnum.MIS.value:
            mis = self._budget.get("MIS")  # GE budget
            mis.add_transaction(transaction)
            print(transaction)
            # print(mis.show_budget_record())
        else:
            print("Please check your budget type")

    def add_to_locked_budget_list(self, budget):
        """
        This method adds a budget to the locked budget list.
        :param budget: budget object
        """
        if budget not in self._locked_budget_list:
            self._locked_budget_list.append(budget)

    def get_locked_budget_count(self):
        """
        This method returns the number of locked budgets.
        :return: length of the locked budget list
        """
        return len(self._locked_budget_list)

    def is_locked_user(self):
        """
        This method checks if the user is locked.
        """
        if self.get_locked_budget_count() >= 2:
            self.lock_user()

    def lock_user(self):
        """
        This method locks the user.
        """
        self._is_locked_out = True

    def get_user_name(self):
        """
        This method returns the user's name.
        :return: the username
        """
        return self._user_name

    def get_user_age(self):
        """
        This method returns the user's age.
        :return: the user's age
        """
        return self._user_age

    def get_user_type(self):
        """
        This method returns the user's type
        :return: the user's type
        """
        return self._user_type

    def get_user_locked_status(self):
        """
        This method returns the user's type
        :return: the user's type
        """
        return self._is_locked_out

    def get_user_bank_account_number(self):
        """
        This method returns the user's bank account number.
        :return: the user's bank account number
        """
        return self._bank.get_account_number()

    def get_user_bank_balance(self):
        """
        This method returns the user's bank balance.
        :return: the user's bank balance
        """
        return self._bank.get_balance()

    def get_user_budget(self, budget_type):
        """
        This method returns the user's budget.
        :param budget_type: the budget type to get
        :return: the user's budget
        """
        return self._budget.get(budget_type)

    def get_user_budgets_as_whole(self):
        """
        This method returns the user's budget.
        :return: dictionary of the user's budget
        """
        return self._budget

    def get_bank(self):
        """
        This method returns the user's bank.
        :return: bank object
        """
        return self._bank

    def get_bank_name(self):
        """
        This method returns the user's bank name.
        :return: the user's bank name
        """
        return self._bank.get_bank_name()

    def get_login_status(self):
        """
        This method returns the user's login status.
        :return: the user's login status
        """
        return self.login_status

    def get_user_count(self):
        """
        This method returns the number of users.
        :return: the number of users
        """
        return self._users.__len__()

    def get_current_user_index(self):
        """
        This method returns the index of the current(login) user.
        :return: the index of the current user
        """
        index = 0
        for i in self._users:
            if self._users[index].login_status:
                return index
            index += 1

    def get_current_user(self, index):
        """
        This method returns the current(login) user.
        :param index: index of the current user
        :return: user object
        """
        return self._users[index]

    def get_current_bank(self, index):
        """
        This method returns the current(login) user's bank.
        :param index: index of the current user
        :return: bank object
        """
        return self._users[index].get_bank()

    def get_current_user_name(self, index):
        """
        This method returns the name of the current(login) user.
        :param index: the index of the current user
        :return: the name of the current user
        """
        return self._users[index].get_user_name()

    def get_current_user_type(self, index):
        """
        This method returns the type of the current(login) user.
        :param index: the index of the current user
        :return: the type of the current user
        """
        return self._users[index].get_user_type()

    def get_current_user_lock_status(self, index):
        """
        This method returns the user's lock status.
        :return: the user's lock status
        """
        return self._users[index].get_user_locked_status()

    def register_user(self):
        """
        This method is for registering a new user.
        """
        new_user_name = input("Name: ")
        if new_user_name == '':
            print("Please enter a valid name.")
            return -1
        new_user_age = input("Age: ")
        try:
            new_user_age = int(new_user_age)
        except ValueError:
            print("Please enter a valid number for age.")
            return -1

        new_user_type = 0
        new_user_limit_factor = 0
        while (new_user_type < 1) or (new_user_type > 3):
            print("1. Angel")
            print("2. Trouble Maker")
            print("3. Rebel")
            new_user_type = input("Select the user's type: ")
            if new_user_type == '':
                new_user_type = -1
            try:
                new_user_type = int(new_user_type)
            except ValueError:
                print("Please enter a valid number.")
                continue
            if new_user_type == 1:
                new_user_limit_factor = ANGEL_LIMIT_FACTOR
            elif new_user_type == 2:
                new_user_limit_factor = TROUBLEMAKER_LIMIT_FACTOR
            elif new_user_type == 3:
                new_user_limit_factor = REBEL_LIMIT_FACTOR
            else:
                print("Please select the type from 1 - 3.")

        type_list = list(UserTypes)
        new_user_type = type_list[int(new_user_type) - 1].value

        new_user_account_number = input("Account number: ")
        if new_user_account_number == '':
            print("Please enter a valid account number.")
            return -1

        new_user_bank_name = input("Bank name: ")
        if new_user_bank_name == '':
            print("Please enter a bank name.")
            return -1

        new_user_bank_balance = input("Bank balance: ")
        try:
            new_user_bank_balance = float(new_user_bank_balance)
        except ValueError:
            print("Please enter a valid number for balance.")
            return -1

        new_user_budget_ge = input("Game and Entertainment Budget: ")
        new_user_budget_ca = input("Clothing and Accessories Budget: ")
        new_user_budget_eo = input("Eating Out Budget: ")
        new_user_budget_mis = input("Miscellaneous Budget: ")

        try:
            new_user_budget_ge = float(new_user_budget_ge)
            new_user_budget_ca = float(new_user_budget_ca)
            new_user_budget_eo = float(new_user_budget_eo)
            new_user_budget_mis = float(new_user_budget_mis)
        except ValueError:
            print("Please enter a valid number for budget.")
            return -1

        new_user_budget_limit_ge = new_user_limit_factor * new_user_budget_ge
        new_user_budget_limit_ca = new_user_limit_factor * new_user_budget_ca
        new_user_budget_limit_eo = new_user_limit_factor * new_user_budget_eo
        new_user_budget_limit_mis = new_user_limit_factor * new_user_budget_mis

        self._users.append(
            User(user_name=new_user_name,
                 user_age=new_user_age,
                 user_type=new_user_type,
                 account_number=new_user_account_number,
                 balance=new_user_bank_balance,
                 budget=[[new_user_budget_ge, new_user_budget_limit_ge],
                         [new_user_budget_ca, new_user_budget_limit_ca],
                         [new_user_budget_eo, new_user_budget_limit_eo],
                         [new_user_budget_mis, new_user_budget_limit_mis]],
                 bank_name=new_user_bank_name))

    def quick_add_user(self):
        """
        This method is for adding a new user for initial setting for login.
        """
        self._users.append(User(user_name="Jeff",
                                user_age=37,
                                user_type="Angel",
                                account_number="1234567",
                                balance=1000,
                                budget=[[100, 90], [200, 180], [300, 270], [400, 360]],
                                bank_name="TD",
                                is_locked_out=False))
        self._users.append(User(user_name="Mike",
                                user_age=37,
                                user_type="Angel",
                                account_number="9785567",
                                balance=1000,
                                budget=[[100, 90], [200, 180], [300, 270], [400, 360]],
                                bank_name="TD",
                                is_locked_out=False))
        self._users.append(User(user_name="Nash",
                                user_age=43,
                                user_type="Trouble Maker",
                                account_number="9876543",
                                balance=2000,
                                budget=[[200, 150], [300, 225], [400, 300], [500, 375]],
                                bank_name="RBC",
                                is_locked_out=True))
        self._users.append(User(user_name="Taylor",
                                user_age=27,
                                user_type="Rebel",
                                account_number="1357911",
                                balance=5000,
                                budget=[[500, 250], [600, 300], [700, 350], [800, 400]],
                                bank_name="CIBC",
                                is_locked_out=True))
        self._users.append(User(user_name="Jackie",
                                user_age=27,
                                user_type="Rebel",
                                account_number="1357911",
                                balance=5000,
                                budget=[[500, 250], [600, 300], [700, 350], [800, 400]],
                                bank_name="CIBC",
                                is_locked_out=False))
        self._users.append(User(user_name="Alex",
                                user_age=27,
                                user_type="Trouble Maker",
                                account_number="1357911",
                                balance=5000,
                                budget=[[500, 250], [600, 300], [700, 350], [800, 400]],
                                bank_name="CIBC",
                                is_locked_out=False))

    def list_user(self, option):
        """
        This method is for listing all users.
        :param option: 0 list all users, 1 list only username.
        """
        cnt = 1
        for user_data in self._users:
            if option == 0:
                print("\n------< User No. " + str(cnt) + " >------")
                print("Basic Information")
                print(" - Name: " + user_data.get_user_name(),
                      "\n - Age: " + str(user_data.get_user_age()),
                      "\n - Type: " + user_data.get_user_type(),
                      "\n - Bank Name: " + user_data.get_bank_name(),
                      "\n - Account Number: " + str(user_data.get_user_bank_account_number()),
                      "\n - Balance: " + str(user_data.get_user_bank_balance()),
                      "\nBudget Categories (Budget / Limit)",
                      user_data.get_user_budget("GE"),
                      user_data.get_user_budget("CA"),
                      user_data.get_user_budget("EO"),
                      user_data.get_user_budget("MIS")
                      )
                cnt += 1
            elif option == 1:
                if self.get_current_user_lock_status(cnt - 1):
                    print(f"{cnt}. {user_data.get_user_name()} ({user_data.get_user_type()}) - LOCKED")
                else:
                    print(f"{cnt}. {user_data.get_user_name()} ({user_data.get_user_type()})")
                cnt += 1

    def get_user_locked_out_status(self):
        """
        This method is for getting user locked out status.
        :return: locked out status
        """
        return self._is_locked_out

    def set_user_name(self, name):
        """
        This method is for setting username.
        :param name: username
        """
        self._user_name = name

    def set_user_age(self, age):
        """
        This method is for setting user age.
        :param age: user age
        """
        self._user_age = age

    def set_user_type(self, user_type):
        """
        This method is for setting user type.
        :param user_type: ANGEL, REBEL or TROUBLE MAKER
        """
        self._user_type = user_type

    def set_user_bank_account_number(self, account_number):
        """
        This method is for setting user bank account number.
        :param account_number: user's bank account number
        """
        self._bank.set_account_number(account_number)

    def set_user_bank_balance(self, balance):
        """
        This method is for setting user bank balance.
        :param balance: user's bank balance
        """
        self._bank.set_balance(balance)

    def set_bank_name(self, bank_name):
        """
        This method is for setting user bank name.
        :param bank_name: user's bank name
        """
        return self._bank.set_bank_name(bank_name)

    def set_login_status(self, index, login_status):
        """
        This method is for setting user login status.
        :param index: the index of the current user in the list
        :param login_status: True if this user is current user else False
        """
        self._users[index - 1].login_status = login_status
