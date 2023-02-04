class User:
    """
    This class manages users' information.
    """
    def __init__(self, user_name, budget):
        self._user_name = user_name
        self._budget = budget

    def get_user_name(self):
        """
        Returns user name
        :return: user name
        """
        return self._user_name

    def get_budget(self):
        """
        Returns budget
        :return: user's budget
        """
        return self._budget
