"""This is the account class that will manage all user accounts"""

from datetime import datetime
from core.account_balance import Balance
from core.account_card import AccountCard
from core.account_number import AccountNumber
from data import prompts
from utils.input_handler import UserInputHandler

class Account:
    """This is the account class that will manage all user accounts"""

    accounts_data = {}
    bill_ids =[]

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
        pin,
        create_card=True
    ):
        self.email = email
        self.phone_no = phone_no
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.password = password
        self.initial_deposit = initial_deposit
        self.account_type = account_type
        self.date_created = datetime.now().date()
        self.date_of_birth = date_of_birth
        self.country = country
        self.city = city
        self.pin = pin
        self.balance = Balance(initial_deposit)
        self.account_number = AccountNumber()
        self.cards = []
        self.transactions = []
        self.notifications = []
        if create_card:
            self.add_card()
        Account.accounts_data[self.email]=self

    @staticmethod
    def get_account_by_email(email):
        """this is the function that will return a user object based on email"""
        return Account.accounts_data.get(email)

    @staticmethod
    def get_account_by_acc_num(rec_acc_num):
        '''finds an account user based on account number'''
        for email in Account.accounts_data:
            user = Account.get_account_by_email(email)
            user_acc_num = int(user.account_number.get_account_number())
            if rec_acc_num == user_acc_num:
                return user
        return False

    @staticmethod
    def register_user():
        """Handle user registration."""
        email = UserInputHandler.get_valid_email("Enter your Email to register: ")
        if Account.is_old_user(email):
            return False
        password = UserInputHandler.get_valid_password("Enter your Password: ")
        pin = UserInputHandler.get_valid_pin("Enter your Pin Code: ")
        phone_no = UserInputHandler.get_valid_phone_no("Enter your Phone No: ")
        first_name = UserInputHandler.get_valid_first_name("Enter your First Name: ")
        last_name = UserInputHandler.get_valid_last_name("Enter your Last Name: ")
        gender = UserInputHandler.get_valid_gender(
            "Enter your Gender (Male/Female/Other): "
        )
        initial_deposit = UserInputHandler.get_valid_initial_deposit(
            "Enter your Initial Deposit: "
        )
        account_type = UserInputHandler.get_valid_account_type(
            """Enter your Account type("Current", "Saving", "Other"): """
        )
        date_of_birth = UserInputHandler.get_valid_date_of_birth(
            "Enter your Date of Birth (YYYY-MM-DD): "
        )
        country = UserInputHandler.get_valid_country("Enter the name of your Country: ")
        city = UserInputHandler.get_valid_city("Enter the name of your City: ")
        new_account = Account(
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
            pin
        )
        Account.write_data("data/user_accounts_data.txt",'a',new_account)
        return new_account

    @staticmethod
    def write_data(path,mode,new_account):
        '''func to write all data of a user into file'''
        with open(path, mode, encoding="UTF-8") as file:
            file.write(
                    f"{new_account.email} {new_account.first_name} {new_account.last_name}"
                    f" {new_account.gender} {new_account.email} {new_account.phone_no}"
                    f" {new_account.password} {new_account.initial_deposit}"
                    f" {new_account.account_type}"
                    f" {new_account.date_created} {new_account.date_of_birth}"
                    f" {new_account.country} {new_account.city}"
                    f" {new_account.balance.get_balance()}"
                    f" {new_account.account_number.get_account_number()} {new_account.pin}\n"
                       )

    @staticmethod
    def is_old_user(email):
        """This functions checks if the user already has an account"""
        if email in Account.accounts_data:
            return True
        return False

    @staticmethod
    def validate_pin(email, pin):
        """this functions checks for a duplicate email and authenticates the user and logins user"""
        user = Account.get_account_by_email(email)
        if user:
            if int(user.pin) == pin:
                print(prompts.VALIDATION_SUCCESS)
                return True
        return False

    @staticmethod
    def login_user(email, password):
        """this functions checks for a duplicate email and authenticates the user and logins user"""
        user = Account.get_account_by_email(email)
        if user:
            if user.password == password:
                return user
        return False

    @staticmethod
    def update_new_value(user='null',item_to_edit='balance',updated_value='null'):
        """this function takes the updated value and stores
        it in dict and and calls for file update"""
        #making a copy of data
        # open both files
        with open('data/user_accounts_data.txt','r', encoding="UTF-8") as accounts_data,\
            open('data/user_cards_data.txt','r', encoding="UTF-8") as cards_data,\
            open('data/temp_data.txt','a', encoding="UTF-8") as second_file:
            second_file.write("\n")
            for line in accounts_data:
                second_file.write(line)
            second_file.write("\n")
            for line in cards_data:
                second_file.write(line)
        if item_to_edit != 'balance':
            setattr(user,item_to_edit,updated_value)
        with open("data/user_accounts_data.txt", "w", encoding="UTF-8") as file:
            for email in Account.accounts_data:
                new_account=Account.accounts_data.get(email)
                file.write(
                    f"{new_account.email} {new_account.first_name} {new_account.last_name}"
                    f" {new_account.gender} {new_account.email} {new_account.phone_no}"
                    f" {new_account.password} {new_account.initial_deposit}"
                    f" {new_account.account_type}"
                    f" {new_account.date_created} {new_account.date_of_birth}"
                    f" {new_account.country} {new_account.city}"
                    f" {new_account.balance.get_balance()} \
{new_account.account_number.get_account_number()}"
                    f" {new_account.pin}\n"
                    )

    @staticmethod
    def handle_edit(user, item_to_edit, prompt):
        """the function to take the new data and call the update functions"""
        if item_to_edit in ("initial_deposit","date_created"):
            print(prompts.EDIT_NOT_ALLOWED)
        else:
            old_data = getattr(user,item_to_edit)
            get_function_name = f"get_valid_{item_to_edit}"
            get_function = getattr(UserInputHandler, get_function_name)
            new_data = get_function(prompt)
            if item_to_edit=='email':
                while Account.is_old_user(new_data):
                    print(prompts.REGISTER_FAILED)
                    new_data = get_function(prompt)
            Account.update_new_value(user, item_to_edit, new_data)
            print(
                f"{prompts.DASHES}Changing {item_to_edit.title().replace("_"," ")}:"
                f" '{old_data}' to '{new_data}'{prompts.DASHES}"
            )
            print(prompts.UPDATE_SUCCESSFUL)

    def add_card(self,name=None):
        '''func to add a new card'''
        card_holder = self
        if name is not None:
            card = AccountCard(card_holder,name)
        else:
            card = AccountCard(card_holder)
        self.cards.append(card)

    
