"""
TODO Taylor: Write a description here

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji (taylor.ji719@gmail.com)
# Student number2: A01304056

UML diagram: https://app.diagrams.net/#G1DUxHF4SH4QveN8GbqGaHewuu07bC5lDG
"""

from enum import Enum


class Budget:
    """
    This class manages budgets of user.
    The budget will have different characteristics based on user type.
    Angel never gets locked out while Trouble make, and Rebel get locked out
    """

    def __init__(self, budget_type_name="", total_budget=0, warning_budget_limit=0.0):
        """
        Initializer for budget.
        Lockout limit is used to check if the spent amount equal to or greater than the lockout limit.
        Warning budget limit is used to notify the user.
        """
        self._budget_type_name = budget_type_name
        self._total_budget = total_budget
        self._warning_budget_limit = warning_budget_limit
        self._user_budget_type = None
        self._spent_amount = 0
        self._lockout_limit = 0
        self._remaining_budget = 0
        self._budget_record = []  # list of transaction
        self._is_budget_warning_limit_met = False
        self._is_locked = False
        self._angel_lockout_ratio = 0
        self._tm_lockout_ratio = 1.2
        self._rebel_lockout_ratio = 1

    def angel_setup(self):
        """
        Angel never gets locked out
        No lockout limit
        """
        self.set_user_budget_type("Angel")
        self._lockout_limit = float("inf")

    def tm_setup(self):
        """
        Angel never gets locked out
        No lockout limit
        """
        self.set_user_budget_type("Trouble Maker")
        self.set_lockout_budget_limit(self._total_budget * self.get_tm_lockout_ratio())

    def rebel_setup(self):
        """
        Angel never gets locked out
        No lockout limit
        """
        self.set_user_budget_type("Rebel")
        self.set_lockout_budget_limit(self._total_budget * self._rebel_lockout_ratio)

    def setup_user_budget_type(self, user_type):
        """
        Setup budgets based on the user type
        """
        if user_type == "Angel":
            self.angel_setup()
        elif user_type == "Trouble Maker":
            self.tm_setup()
            print(self.get_lockout_budget_limit())
        else:
            self.rebel_setup()
            print(self.get_lockout_budget_limit())

    def get_total_budget(self):
        """
        Getter for total_budget
        """
        return self._total_budget

    def update_spend_amount(self, amount):
        """
        Update the spent amount.
        """
        self._spent_amount += amount

    def get_remaining_budget(self):
        """
        Calculate the remaining budget.
        return float
        """
        self._remaining_budget = self.get_total_budget() - self._spent_amount
        return self._remaining_budget

    def is_met_warning_budget_limit(self, transaction):
        """
        Check whether the total spent amount of the budget meets the budget limit
        return Boolean
        """
        if self._spent_amount + transaction.get_dollar_amount() >= self._warning_budget_limit:
            self.set_met_warning_limit()  # true, met the warning limit
        return self.get_is_budget_warning_limit_met()

    def is_locked_budget(self, transaction):
        """
        Check whether the total spent amount of the budget meets the budget limit
        return Boolean
        """
        if self.get_user_budget_type() == "Angel":  # angel case, never lock the account
            return self.get_is_locked_status()
        else:
            if self._spent_amount + transaction.get_dollar_amount() > self.get_lockout_budget_limit():
                self.lock_budget()  # true, met the warning limit
        return self.get_is_locked_status()

    def add_transaction(self, transaction):
        # do not have to worry about lock because I checked it at account
        """
        Add new transaction to this budget
        If the new transaction's cost + spent_amount does not equal or greater than budget limit
        If not, print warning message and lock the budget based on user type
        Angel user is handled differently because it does not have lockout limit
        """

        if self.get_user_budget_type() == "Angel":
            if self._spent_amount + transaction.get_dollar_amount() > self.get_total_budget():
                self.prompt_angel_exceeding_message()
            else:
                if self.is_met_warning_budget_limit(transaction):
                    self.prompt_gentle_warning_message()
            self._budget_record.append(transaction)
            self.update_spend_amount(transaction.get_dollar_amount())
        elif self.get_user_budget_type() == "Trouble Maker":
            if self._spent_amount + transaction.get_dollar_amount() > self.get_lockout_budget_limit():
                self.prompt_gentle_exceeding_message()
                self.lock_budget()
                return
            else:
                if self.is_met_warning_budget_limit(transaction):
                    self.prompt_gentle_warning_message()
                self._budget_record.append(transaction)
                self.update_spend_amount(transaction.get_dollar_amount())
        else:
            if self._spent_amount + transaction.get_dollar_amount() > self.get_lockout_budget_limit():
                self.prompt_strong_exceeding_message()
                self.lock_budget()
                return
            else:
                if self.is_met_warning_budget_limit(transaction):
                    self.prompt_strong_warning_message()
                self._budget_record.append(transaction)
                self.update_spend_amount(transaction.get_dollar_amount())

            # if self.is_met_warning_budget_limit(transaction):
            #     if self.get_user_budget_type() == "Trouble Maker":
            #         self.prompt_gentle_exceeding_message()
            #     else:
            #         self.prompt_strong_warning_message()
            #         if self.get_user_budget_type() == "Rebel":
            #             self.prompt_strong_exceeding_message()
            #     self._budget_record.append(transaction)
            #     self.update_spend_amount(transaction.get_dollar_amount())
            # else:
            #     self._budget_record.append(transaction)
            #     self.update_spend_amount(transaction.get_dollar_amount())

    def prompt_gentle_warning_message(self):
        """
        Gentle warning message
        """
        message = f"You are getting close to meet the budget limit: {self.get_warning_budget_limit()}"
        print(message)

    def prompt_gentle_exceeding_message(self):
        """
        Gentle exceeding message
        """
        message = f"You exceed the budget limit. Transaction failed."
        print(message)

    def prompt_angel_exceeding_message(self):
        """
        Gentle exceeding message
        """
        message = f"You exceed the budget limit."
        print(message)

    def prompt_strong_warning_message(self):
        """
        Special warning message for Rebel
        """
        message = f"Do not waste your money!!!"
        print(message)

    def prompt_strong_exceeding_message(self):
        """
        Special exceeding message for Rebel
        """
        message = f"Transaction is Denied. Your budget is frozen!!! You are banned!!!"
        print(message)

    def prompt_lock_message(self):
        """
        Message to notify user that the budget has been locked
        """
        message = f"{self._budget_type_name} has been locked!"
        print(message)

    def show_budget_record(self):
        """
        Print all the transaction belong this budget
        """
        for transaction in self._budget_record:
            print(transaction)

    def get_is_budget_warning_limit_met(self):
        """
        Getter for budget warning limit
        """
        return self._is_budget_warning_limit_met

    def set_met_warning_limit(self):
        """
        Change is budget warning limit met, which was False to True
        """
        self._is_budget_warning_limit_met = True

    def get_warning_budget_limit(self):
        """
        Getter for warning budget limit
        return float
        """
        return self._warning_budget_limit

    def set_total_budget(self, budget):
        """
        Setter for total budget
        """
        self._total_budget = budget

    def get_lockout_budget_limit(self):
        """
        Get lockout limit
        """
        return self._lockout_limit

    def set_lockout_budget_limit(self, lockout_limit):
        """
        Set the lockout limit to be lockout_limit
        """
        self._lockout_limit = lockout_limit

    def get_tm_lockout_ratio(self):
        """
        Get trouble maker's lock out ratio which is 1.2
        return float
        """
        return self._tm_lockout_ratio

    def get_rebel_lockout_ratio(self):
        """
        Get Rebel's lock out ratio which is 1.0
        return float
        """
        return self._rebel_lockout_ratio

    def get_is_locked_status(self):
        """
        Get the budget lock status
        return Boolean
        """
        return self._is_locked

    def get_user_budget_type(self):
        """
        Getter for user budget type
        Return String
        """
        return self._user_budget_type

    def set_user_budget_type(self, user_type):
        """
        Setter for user budget type
        """
        self._user_budget_type = user_type

    def lock_budget(self):
        """
        Lock the budget by changing the lock status from false to true
        """
        self._is_locked = True

    def set_warning_budget_limit(self, budget_limit):
        """
        Setter for warning budget limit
        """
        self._warning_budget_limit = budget_limit

    def set_lockout_limit(self, lockout_limit):
        """
        Setter for lock out limit
        """
        self._lockout_limit = lockout_limit

    def budget_summary(self):
        """
        Summary for User Menu 1.
        This describes the current lock status, total spent amount,
        remaining amount, and total budget that was assigned when the budget was created.
        Return String
        """
        summary = f"==============================================================" \
                  f"\n{self._budget_type_name}: " \
                  f"\n Locked status: {self.get_is_locked_status()}" \
                  f"\n Total spent amount: ${self._spent_amount}" \
                  f"\n Remaining budget: ${self.get_remaining_budget()}" \
                  f"\n Total allowed budget: ${self.get_total_budget()}"
        return summary

    def __str__(self):
        return "\n - " + self._budget_type_name + ": " + str(self._total_budget) + " / " + str(
            self._warning_budget_limit)


class BudgetTypeEnum(Enum):
    GE = "Game and Entertainment"
    CA = "Clothing and Accessories"
    EO = "Eat out"
    MIS = "Miscellaneous"
