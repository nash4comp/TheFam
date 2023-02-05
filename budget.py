from enum import Enum


class Budget:
    """
    This class manages budget of user.
    """

    def __init__(self, budget_type_name, total_budget, budget_limit):
        self._budget_type_name = budget_type_name
        self._total_budget = total_budget
        self._warning_budget_limit = budget_limit
        self._spent_amount = 0
        self._budget_record = []  # list of transaction
        self._is_budget_limit_met = False
        self._is_out_of_balance = False

    def get_total_budget(self):
        return self._total_budget

    def check_budget_limit(self):
        pass

    def lock_out(self):
        # condition for lock out varies based on user type
        # if the condition is met then the user cannot record transaction
        pass

    def get_warning_budget_limit(self):
        return self._warning_budget_limit

    def set_total_budget(self, budget):
        self._total_budget = budget

    def set_warning_budget_limit(self, budget_limit):
        self._warning_budget_limit = budget_limit


class BudgetTypeEnum(Enum):
    GE = "Game and Entertainment"
    CA = "Clothing and Accessories"
    EO = "Eat out"
    MIS = "Miscellaneous"
