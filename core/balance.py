"""this class will handle the user account balance"""


class Balance:
    """this class will handle the user account balance"""

    def __init__(self, initial_deposit, currency="PKR"):
        self.amount = float(initial_deposit)
        self.currency = currency

    def set_balance(self, amount):
        self.amount = float(amount)

    def get_balance(self):
        return self.amount

    def deposit(self, amount):
        self.amount += float(amount)

    def withdraw(self, amount):
        if self.amount >= float(amount):
            self.amount -= float(amount)
            return True
        return False

    def transfer(self):
        pass
