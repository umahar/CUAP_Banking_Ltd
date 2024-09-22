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
        account_balance,
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
        self.account_balance = account_balance
        self.account_type = account_type
        self.date_created = datetime.now()
        self.date_of_birth = date_of_birth
        self.country = country
        self.city = city

    def register_user(self):
        """the main function to store details of a user in a file and dict"""
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
                    "account_balance": self.account_balance,
                    "account_type": self.account_type,
                    "date_created": self.date_created.strftime("%Y-%m-%d"),
                    "date_of_birth": self.date_of_birth,
                    "country": self.country,
                    "city": self.city,
                }
            }
        )
        file = open("data/user_accounts.txt", "a", encoding="UTF-8")
        file.write(f"{self.email} {self.first_name} {self.last_name} {self.gender} {self.email} {self.phone_no} {self.password} {self.account_balance} {self.account_type} {self.date_created.strftime("%Y-%m-%d")} {self.date_of_birth} {self.country} {self.city}" + "\n")
        file.close()
        return True

    @staticmethod
    def is_old_user(email):
        """This functions checks if the user already has an account"""
        if email in Account.user_accounts:
            return True
        return False

    @staticmethod
    def login_user(email, password):
        """this functions checks for a duplicate email and authenticates the user and logins user"""
        if (
            email in Account.user_accounts
            and Account.user_accounts[email]["password"] == password
        ):
            return True
        return False
    
    @staticmethod
    def load_data():
        """this functions is called on the start of program and it loads
        all data saved in the file to a dict"""
        with open('data/user_accounts.txt',"r", encoding="UTF-8") as fp:  
            lines = fp.readlines()
            # Iterate the file till it reached the EOF
            for line in lines:
                print(lines.index(line)+1,":",line, end='')
                dp = line.split()
                Account.user_accounts.update(
            {
                dp[0]: {
                    "first_name": dp[1],
                    "last_name": dp[2],
                    "gender": dp[3],
                    "email": dp[4],
                    "phone_no": dp[5],
                    "password": dp[6],
                    "account_balance": dp[7],
                    "account_type": dp[8],
                    "date_created": dp[9],
                    "date_of_birth": dp[10],
                    "country": dp[11],
                    "city": dp[12],
                }
            }
        )    
    
    def __str__(self):
        return f"Account for {self.first_name} {self.last_name} ({self.email})"

    def __repr__(self):
        return (
            f"Account(email={self.email}, phone_no={self.phone_no}, "
            f"name={self.first_name} {self.last_name}, "
            f"gender={self.gender}, initial_deposit={self.account_balance}, "
            f"account_type={self.account_type}, "
            f"date_of_birth={self.date_of_birth}, country={self.country}, "
            f"city={self.city})"
        )

    @staticmethod
    def display_user_details(email):
        """get the user details based on an email and prints them one by one"""
        user_details = Account.user_accounts.get(email)
        count = 1
        for key,value in user_details.items():
            print(f"{count}. {key.replace("_"," ").title()}:  {value}")
            count+=1

    @staticmethod
    def replace_line_in_file(file_path, line_number, new_data):
        """this function makes the change in the file"""
        with open(file_path, 'r',encoding="UTF-8") as file:
            lines = file.readlines()

        if 0 <= line_number < len(lines):  # Ensure the line number is valid
            lines[line_number] = new_data + '\n'  # Replace the content of the specific line

        with open(file_path, 'w',encoding="UTF-8") as file:
            file.writelines(lines)


    @staticmethod
    def update_new_value(email,item_to_edit,updated_value):
        """this function takes the updated value and stores it in dict and and calls for file update"""
        Account.user_accounts[email][item_to_edit]=updated_value
        user_details = Account.user_accounts.get(email)
        list_of_acc = list(Account.user_accounts.keys())
        line_no = list_of_acc.index(email)
        data = email+" "
        for _key,value in user_details.items():
            data = data + str(value) + " "
        Account.replace_line_in_file("data/user_accounts.txt",line_no,data)
