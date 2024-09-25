"""this class will handle the user account balance"""

from core import account


class Balance:
    """this class will handle the user account balance"""

    def __init__(self, initial_deposit, currency="PKR"):
        self.amount = float(initial_deposit)
        self.currency = currency

    def set_balance(self, amount):
        """this is called for purposes of directly setting the acc balance on load"""
        self.amount = float(amount)

    def get_balance(self):
        """returns the current acc balance"""
        return self.amount

    def deposit(self, amount):
        """deposits money into account"""
        self.amount += float(amount)
        account.Account.update_new_value()

    def withdraw(self, amount):
        """withdraws money from account"""
        if self.amount >= float(amount):
            self.amount -= float(amount)
            account.Account.update_new_value()
            return True
        return False

    def transfer(self):
        """transfers money from self acc to another"""
