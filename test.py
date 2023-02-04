import user
from user import User


class Test:
    def __init__(self):
        pass

    def generate_user_lists(self):
        """
        This method generates hardcoded data such as name and budget.

        :return: generated user list
        """
        user_list = [
            User("Ken", 23, user.UserTypes.REBEL.value, 1234, 500, 300, 1000),
            User("Ryu", 25, user.UserTypes.ANGEL.value, 5678, 800, 700, 2000)
        ]
        user_list[0].set_user_name("Ben")

        return user_list

    def load_test_user(self):
        """
        Prints user lists.

        :return:
        """
        temp = self.generate_user_lists()
        print("Hardcoded user list loaded.")
        for user_data in temp:
            print(user_data.get_user_name(),
                  user_data.get_user_age(),
                  user_data.get_user_type(),
                  user_data.get_user_bank_account_number(),
                  user_data.get_user_budget(),
                  user_data.get_warning_budget_limit(),
                  user_data.get_user_bank_balance()
                  )
