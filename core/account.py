from datetime import datetime


class Account:
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

    def register_account(self):
        if self.email in Account.user_accounts:
            print(
                "Account already exists with this email. Please login using email & password."
            )

        else:
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
            print("------Account Registration Successful-----------")
            self.login_account(self.email, self.password)

    @staticmethod
    def login_account(email, password):
        if email in Account.user_accounts:
            if password != Account.user_accounts[email]["password"]:
                print("Incorrect password")
            else:
                print("----------Logging In-------------")
                print(Account.user_accounts)
        else:
            print("Account not found with this email. Please register an account")

    @staticmethod
    def is_new_user(email):
        if email in Account.user_accounts:
            return False
        return True
