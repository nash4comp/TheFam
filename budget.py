class Budget:
    """
    This class manages budget of user.
    """

    def __init__(self, budget_type_name, total_budget, budget_limit):
        self._budget_type_name = budget_type_name
        self._total_budget = total_budget
        self._warning_budget_limit = budget_limit

    def get_total_budget(self):
        return self._total_budget

    def get_warning_budget_limit(self):
        return self._warning_budget_limit

    def set_total_budget(self, budget):
        self._total_budget = budget

    def set_warning_budget_limit(self, budget_limit):
        self._warning_budget_limit = budget_limit
