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
            User(user_name="Ken", user_age=23, user_type=user.UserTypes.REBEL.value, account_number="1234", balance=500, budget=300, budget_limit=1000, bank_name="TD"),
            User(user_name="Ryu", user_age=25, user_type=user.UserTypes.ANGEL.value, account_number="5678", balance=800, budget=700, budget_limit=2000, bank_name="CIBC"),
        ]
        user_list[0].set_user_name("Ben")
        user_list[0].set_user_age(22)
        user_list[0].set_user_type(user.UserTypes.TROUBLE_MAKER.value)
        user_list[0].set_user_bank_account_number("0987")
        user_list[0].set_user_budget(300)
        user_list[0].set_warning_budget_limit(100)
        user_list[0].set_user_bank_balance(500)
        user_list[0].set_bank_name("RBC")

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
                  user_data.get_user_bank_balance(),
                  user_data.get_bank_name()
                  )
