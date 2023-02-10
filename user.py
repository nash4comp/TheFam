from enum import Enum

from bank import Bank
from budget import Budget
from budget import BudgetTypeEnum
from transaction import Transaction


class UserTypes(Enum):
    ANGEL = "Angel"
    TROUBLE_MAKER = "Trouble Maker"
    REBEL = "Rebel"


# TODO Think about putting unique ID variable into each account.
class User:
    """
    This class manages users' information.
    """
    user_type_list = UserTypes

    def __init__(self, user_name="", user_age=0, user_type="", account_number="", balance=0.0, bank_name="",
                 budget=None, login_status=False):
        if budget is None:
            budget = [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]]
        self._users = []  # list of dictionary
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
        self.login_status = login_status

    def setup(self, budget):
        budget.setup()

    def add_transaction_to_budget(self, transaction):
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

    def show_transaction_by_budget(self):
        print("Game and Entertainment: ")
        self._budget.get("GE").show_budget_record()
        print("Clothing and Accessories: ")
        self._budget.get("CA").show_budget_record()
        print("Eat out: ")
        self._budget.get("EO").show_budget_record()
        print("Miscellaneous: ")
        self._budget.get("MIS").show_budget_record()

    def get_user_name(self):
        return self._user_name

    def get_user_age(self):
        return self._user_age

    def get_user_type(self):
        return self._user_type

    def get_user_bank_account_number(self):
        return self._bank.get_account_number()

    def get_user_bank_balance(self):
        return self._bank.get_balance()

    def get_user_budget(self, budget_type):
        return self._budget.get(budget_type)

    def show_specific_budget(self):
        budget = self.get_user_budget()
        budget.show_budget_record()

    def get_bank(self):
        return self._bank

    def get_bank_name(self):
        return self._bank.get_bank_name()

    def get_login_status(self):
        return self.login_status

    def get_user_count(self):
        return self._users.__len__()

    def get_current_user_index(self):
        index = 0
        for i in self._users:
            if self._users[index].login_status:
                return index
            index += 1

    def get_current_user(self, index):
        return self._users[index]

    def get_current_bank(self, index):
        return self._users[index].get_bank()  # indexed user dictionary and function

    # def get_current_user_budget(self, index):
    #     return self._users[index].get_user_budget(budget_type)

    def get_current_user_name(self, index):
        return self._users[index].get_user_name()

    def register_user(self):
        new_user_name = input("Name: ")
        if new_user_name == '':
            print("Please enter a valid name.")
            return
        new_user_age = input("Age: ")
        try:
            new_user_age = int(new_user_age)
        except ValueError:
            print("Please enter a valid number for age.")
            return

        new_user_type = 0
        new_user_warning_limit_factor = 0
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
                new_user_warning_limit_factor = 0.9
            elif new_user_type == 2:
                new_user_warning_limit_factor = 0.75
            elif new_user_type == 3:
                new_user_warning_limit_factor = 0.5
            else:
                print("Please select the type from 1 - 3.")

        type_list = list(UserTypes)
        new_user_type = type_list[int(new_user_type) - 1].value

        new_user_account_number = input("Account number: ")
        if new_user_account_number == '':
            print("Please enter a valid account number.")
            return

        new_user_bank_name = input("Bank name: ")
        if new_user_bank_name == '':
            print("Please enter a bank name.")
            return

        new_user_bank_balance = input("Bank balance: ")
        try:
            new_user_bank_balance = float(new_user_bank_balance)
        except ValueError:
            print("Please enter a valid number for balance.")
            return

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
            return

        new_user_budget_limit_ge = new_user_warning_limit_factor * new_user_budget_ge
        new_user_budget_limit_ca = new_user_warning_limit_factor * new_user_budget_ca
        new_user_budget_limit_eo = new_user_warning_limit_factor * new_user_budget_eo
        new_user_budget_limit_mis = new_user_warning_limit_factor * new_user_budget_mis

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
        self._users.append(User(user_name="Jeff",
                                user_age=37,
                                user_type="Angel",
                                account_number="1234567",
                                balance=1000,
                                budget=[[100, 90], [200, 180], [300, 270], [400, 360]],
                                bank_name="TD"))
        self._users.append(User(user_name="Nash",
                                user_age=43,
                                user_type="Trouble Maker",
                                account_number="9876543",
                                balance=2000,
                                budget=[[200, 150], [300, 225], [400, 300], [500, 375]],
                                bank_name="RBC"))
        self._users.append(User(user_name="Taylor",
                                user_age=27,
                                user_type="Rebel",
                                account_number="1357911",
                                balance=5000,
                                budget=[[500, 250], [600, 300], [700, 350], [800, 400]],
                                bank_name="CIBC"))

    def list_user(self, option):
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
                print(f"{cnt}. {user_data.get_user_name()}")
                cnt += 1

    def set_user_name(self, name):
        self._user_name = name

    def set_user_age(self, age):
        self._user_age = age

    def set_user_type(self, user_type):
        self._user_type = user_type

    def set_user_bank_account_number(self, account_number):
        self._bank.set_account_number(account_number)

    def set_user_bank_balance(self, balance):
        self._bank.set_balance(balance)

    # def set_user_budget(self, budget):
    #     self._budget.set_total_budget(budget)
    #
    # def set_warning_budget_limit(self, budget_limit):
    #     self._budget.set_warning_budget_limit(budget_limit)

    def set_bank_name(self, bank_name):
        return self._bank.set_bank_name(bank_name)

    def set_login_status(self, index, login_status):
        self._users[index - 1].login_status = login_status
        # print(self._users[index - 1].get_user_name())
        # print(self._users[index - 1].get_login_status())


class Angel(User):
    def __init__(self):
        super().__init__()

    pass


class TroubleMaker(User):
    def __init__(self):
        super().__init__()
        self._is_locked_out = False

    def get_user_locked_out_status(self):
        return self._is_locked_out

    def set_user_locked_out_status(self, locked_out_status):
        self._is_locked_out = locked_out_status


class Rebel(User):
    def __init__(self):
        super().__init__()
        self._is_locked_out = False

    def get_user_locked_out_status(self):
        return self._is_locked_out

    def set_user_locked_out_status(self, locked_out_status):
        self._is_locked_out = locked_out_status
