"""This is the account class that will manage all user accounts"""

from datetime import datetime


class Account:
    """This is the account class that will manage all user accounts"""

    user_accounts = {}

    def __init__(
        self,
        email,
        phone_no,
        first_name,
        last_name,
        gender,
        password,
        initial_deposit,
        account_type,
        date_of_birth,
        country,
        city,
    ):
        self.email = email
        self.phone_no = phone_no
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.password = password
        self.initial_deposit = initial_deposit
        self.account_type = account_type
        self.date_created = datetime.now()
        self.date_of_birth = date_of_birth
        self.country = country
        self.city = city

    def register_user(self):
        if Account.is_old_user(self.email):
            return False
        Account.user_accounts.update(
            {
                self.email: {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "gender": self.gender,
                    "email": self.email,
                    "phone_no": self.phone_no,
                    "password": self.password,
                    "initial_deposit": self.initial_deposit,
                    "account_type": self.account_type,
                    "date_created": self.date_created.strftime("%Y-%m-%d %H:%M:%S"),
                    "date_of_birth": self.date_of_birth,
                    "country": self.country,
                    "city": self.city,
                }
            }
        )
        return True

    @staticmethod
    def is_old_user(email):
        if email in Account.user_accounts:
            return True
        return False

    @staticmethod
    def login_user(email, password):
        if (
            email in Account.user_accounts
            and Account.user_accounts[email]["password"] == password
        ):
            return True
        if email not in Account.user_accounts:
            return False

    def __str__(self):
        return f"Account for {self.first_name} {self.last_name} ({self.email})"

    def __repr__(self):
        return (
            f"Account(email={self.email}, phone_no={self.phone_no}, "
            f"name={self.first_name} {self.last_name}, "
            f"gender={self.gender}, initial_deposit={self.initial_deposit}, "
            f"account_type={self.account_type}, "
            f"date_of_birth={self.date_of_birth}, country={self.country}, "
            f"city={self.city})"
        )
