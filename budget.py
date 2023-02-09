from enum import Enum


class Budget:
    """
    This class manages budget of user.
    """

    def __init__(self, budget_type_name="", total_budget=0):
        self._budget_type_name = budget_type_name
        self._total_budget = total_budget
        # self._budget_limit_ratio = budget_ratio
        self._warning_budget_limit = 0
        self._spent_amount = 0
        self._lockout_limit = 0
        self._budget_record = []  # list of transaction
        self._is_budget_limit_met = False
        self._is_locked = False
        self._angel_ratio = 0.9
        self._tm_ratio = 0.75
        self._rebel_ratio = 0.5

    def calculate_budget_limit_and_lockout_limit(self, user_type):
        if user_type == "Angel":
            self.set_warning_budget_limit(self._total_budget * self._angel_ratio)
            self.angel_setup()
            # Trouble Maker
        elif user_type == "Trouble Maker":
            self.set_warning_budget_limit(self._total_budget * self._tm_ratio)
            # Rebel
        elif user_type == "Rebel":
            self.set_warning_budget_limit(self._total_budget * self._rebel_ratio)
        else:
            print("Please check user type")

        # # Angel
        # if self._budget_limit_ratio == 0.9:
        #     self.set_warning_budget_limit(self._total_budget * self._budget_limit_ratio)
        #     self.angel_setup()
        # # Trouble Maker
        # elif self._budget_limit_ratio == 0.75:
        #     self.set_warning_budget_limit(self._total_budget * 0.75)
        # # Rebel
        # elif self._budget_limit_ratio == 0.5:
        #     self.set_warning_budget_limit(self._total_budget * 0.5)
        # else:
        #     print("Please check user type")

    # def userType_checker(self):
    #     if self._budget_limit_ratio == 0.9:
    #         return "Angel"
    #     # Trouble Maker
    #     elif self._budget_limit_ratio == 0.75:
    #         return "TM"
    #     # Rebel
    #     elif self._budget_limit_ratio == 0.5:
    #         return "Rebel"
    #     else:
    #         return None
    def angel_setup(self):
        """
        Angel never gets locked out
        No lockout limit
        """
        self._lockout_limit = None
        self._is_locked = True

    def get_total_budget(self):
        return self._budget_type_name + ": " + str(self._total_budget)

    def update_spend_amount(self, amount):
        self._spent_amount += amount

    def is_met_warning_budget_limit(self):
        """
        Check whether the total spent amount of the budget meets the budget limit
        return Boolean
        """
        if self._spent_amount >= self._warning_budget_limit:
            self._is_budget_limit_met = True
            return self._is_budget_limit_met
        else:
            return self._is_budget_limit_met

    def add_transaction(self, transaction, user_type):
        """
        add new transaction to this budget
        if the new transaction's cost + spent_amount does not equal or greater than
        budget limit
        if not, print warning message and lock the budget based on user type
        """
        self.is_met_warning_budget_limit()
        # if it is equal to or greater than budget_warning_limit
        if self._is_budget_limit_met:
            # and if it reaches to the lockout_limit
            if self._spent_amount >= self._lockout_limit:
                if user_type == "Trouble Maker":
                    self.lock_budget()
                    self.prompt_lock_message()
                # Rebel
                elif user_type == "Rebel":
                    self.lock_budget()
                    self.prompt_lock_message()
                else:  # angel
                    self._budget_record.append(transaction)
                    self.update_spend_amount(transaction.get_dollar_amount())
                    self.prompt_gentle_warning_message()
        else:
            self._budget_record.append(transaction)
            self.update_spend_amount(transaction.get_dollar_amount())

    def prompt_gentle_warning_message(self):
        message = f"You are getting close to meet the budget limit: {self.get_warning_budget_limit()}"
        print(message)

    def prompt_strong_warning_message(self):
        message = f"You are getting close to meet the budget limit: {self.get_warning_budget_limit()}"
        print(message)

    def prompt_lock_message(self):
        message = f"{self._budget_type_name} has been locked!"
        print(message)

    def show_budget_record(self):
        for transaction in self._budget_record:
            print(transaction)

    def lock_out(self, user_type):
        # TM
        if user_type == "Trouble Maker" and \
                self._spent_amount >= self._warning_budget_limit:
            self.lock_budget()
        # Rebel
        elif user_type == "Rebel" and \
                self._spent_amount >= self._warning_budget_limit:
            self.lock_budget()
        else:
            pass

        # condition for lock out varies based on user type
        # if the condition is met then the user cannot record transaction
        pass

    def get_warning_budget_limit(self):
        return self._warning_budget_limit

    def set_total_budget(self, budget):
        self._total_budget = budget

    def get_is_locked_status(self):
        return self._is_locked

    def lock_budget(self):
        self._is_locked = True

    def set_warning_budget_limit(self, budget_limit):
        self._warning_budget_limit = budget_limit

    def set_lockout_limit(self, lockout_limit):
        self._lockout_limit = lockout_limit

    def __str__(self):
        return "\n - " + self._budget_type_name + ": " + str(self._total_budget) + " / " + str(
            self._warning_budget_limit)


class BudgetTypeEnum(Enum):
    GE = "Game and Entertainment"
    CA = "Clothing and Accessories"
    EO = "Eat out"
    MIS = "Miscellaneous"
