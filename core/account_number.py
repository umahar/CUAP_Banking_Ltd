"""this class will create and manage unique account numbers for each account"""

import random


class AccountNumber:
    """main class to handle acc numbers"""

    user_account_numbers = set()

    def __init__(self):
        self.account_number = AccountNumber.generate_account_number()

    def get_account_number(self):
        """returns the acc num of a user"""
        return self.account_number

    def set_account_number(self, acc_num):
        """manually sets an acc num for a user"""
        AccountNumber.user_account_numbers.discard(self.account_number)
        self.account_number = acc_num
        AccountNumber.user_account_numbers.add(acc_num)

    @staticmethod
    def generate_account_number():
        """generates a unique random acc num for the user"""
        while True:
            acc_num = random.randint(100000, 999999)
            if acc_num not in AccountNumber.user_account_numbers:
                AccountNumber.user_account_numbers.add(acc_num)
                return acc_num
