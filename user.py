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

    def get_user_age(self):
        pass

    def get_user_type(self):
        pass

    def get_user_bank_account_number(self):
        pass

    def get_user_bank_balance(self):
        pass

    def get_user_budget(self):
        """
        Returns budget
        :return: user's budget
        """
        return self._budget

    def add_new_user(self):
        pass

    def delete_user(self):
        pass

    def set_user_name(self):
        """
        Returns user name
        :return: user name
        """
        return self._user_name

    def set_user_age(self):
        pass

    def set_user_type(self):
        pass

    def set_user_bank_account_number(self):
        pass

    def set_user_bank_balance(self):
        pass

    def set_user_budget(self):
        pass
