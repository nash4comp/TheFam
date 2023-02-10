from enum import Enum


class Budget:
    """
    This class manages budget of user.
    """

    def __init__(self, budget_type_name="", total_budget=0, warning_budget_limit=0.0):
        self._budget_type_name = budget_type_name
        self._total_budget = total_budget
        self._warning_budget_limit = warning_budget_limit
        self._spent_amount = 0
        self._lockout_limit = 0
        self._budget_record = []  # list of transaction
        self._is_budget_warning_limit_met = False
        self._is_locked = False
        self._angel_warning_ratio = 0.9
        self._tm_warning_ratio = 0.75
        self._rebel_warning_ratio = 0.5
        self._angel_lockout_ratio = 0
        self._tm_lockout_ratio = 1.2
        self._rebel_lockout_ratio = 1

    def setup(self):
        if self._total_budget / self._warning_budget_limit == self._angel_warning_ratio:
            self.angel_setup()
        elif self._total_budget / self._warning_budget_limit == self._tm_warning_ratio:
            self.tm_setup()
        elif self._total_budget / self._warning_budget_limit == self._rebel_warning_ratio:
            self.rebel_setup()

    def angel_setup(self):
        """
        Angel never gets locked out
        No lockout limit
        """
        self._lockout_limit = None

    def tm_setup(self):
        """
        Angel never gets locked out
        No lockout limit
        """
        self.set_lockout_budget_limit(self._total_budget * self.get_tm_lockout_ratio())

    def rebel_setup(self):
        """
        Angel never gets locked out
        No lockout limit
        """
        self.set_lockout_budget_limit(self._total_budget)

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
            self.set_met_warning_limit()  # true, met the warning limit
        return self.get_is_budget_warning_limit_met()

    def add_transaction(self, transaction):
        """
        add new transaction to this budget
        if the new transaction's cost + spent_amount does not equal or greater than
        budget limit
        if not, print warning message and lock the budget based on user type
        """
        # if it is equal to or greater than budget_warning_limit
        if self.is_met_warning_budget_limit():
            # and if it reaches to the lockout_limit
            if self._spent_amount >= self.get_lockout_budget_limit():
                if self.get_lockout_budget_limit() != 0:  # checking for angel, angel has 0 for
                    # lockout budget limit
                    self.lock_budget()
                    self.prompt_lock_message()
            else:
                self.prompt_gentle_warning_message()
                self._budget_record.append(transaction)
                self.update_spend_amount(transaction.get_dollar_amount())
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

    def get_is_budget_warning_limit_met(self):
        return self._is_budget_warning_limit_met

    def set_met_warning_limit(self):
        self._is_budget_warning_limit_met = True

    def get_warning_budget_limit(self):
        return self._warning_budget_limit

    def set_total_budget(self, budget):
        self._total_budget = budget

    def get_lockout_budget_limit(self):
        return self._lockout_limit

    def set_lockout_budget_limit(self, lockout_limit):
        self._lockout_limit = lockout_limit

    def get_angel_lockout_ratio(self):
        return self._angel_lockout_ratio

    def get_tm_lockout_ratio(self):
        return self._tm_lockout_ratio

    def get_rebel_lockout_ratio(self):
        return self._rebel_lockout_ratio

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
