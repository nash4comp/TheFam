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
            User("Jeff", 500),
            User("Nash", 1000),
            User("Taylor", 1500)
        ]
        return user_list

    def load_test_user(self):
        """
        Prints user lists.

        :return:
        """
        temp = self.generate_user_lists()
        print("Hardcoded user list loaded.")
        for user in temp:
            print(user.get_user_name(), user.get_budget())