"""This is the main.py The program starts from this file"""

from data import prompts
from data.menu_options import main_menu_options
from data.menu_options import login_menu_options
from core.account import Account
from utils.input_handler import UserInputHandler


def get_user_option(heading, options):
    """Display the main menu and get the user's option."""
    while True:
        print(heading)
        print(prompts.MENU_TEXT)
        for index, item in enumerate(options):
            print(f"{index + 1}. {item}")
        opt = input("\nOption #: ")
        print("")
        if opt.strip().isdigit():
            opt = int(opt)
            if 0 <= opt <= len(options):
                return opt
        print(prompts.INVALID_INPUT_TEXT)


def register_user():
    """Handle user registration."""
    email = UserInputHandler.get_valid_email("Enter your email to register: ")
    if Account.is_old_user(email):
        print(prompts.REGISTER_FAILED)
    else:
        password = UserInputHandler.get_valid_password("Enter your password: ")
        phone_no = UserInputHandler.get_valid_phone_no("Enter your phone no: ")
        first_name = UserInputHandler.get_valid_name(
            "Enter your first name: ", "First Name"
        )
        last_name = UserInputHandler.get_valid_name(
            "Enter your last name: ", "Last Name"
        )
        gender = UserInputHandler.get_valid_gender(
            "Enter your gender (Male/Female/Other): "
        )
        account_balance = UserInputHandler.get_valid_deposit(
            "Enter your initial deposit: "
        )
        account_type = UserInputHandler.get_valid_acc_type(
            """Enter your account type("Current", "Saving", "Other"): """
        )
        date_of_birth = UserInputHandler.get_valid_date(
            "Enter your date of birth (YYYY-MM-DD): "
        )
        country = input("Enter your country: ")
        city = input("Enter your city: ")

        new_account = Account(
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
        )
        if new_account.register_user():
            print(prompts.REGISTER_SUCCESS)
            login_user(email, password)
        else:
            print(prompts.UNKNOWN_ERROR)


def login_user(email, password):
    """Handle user login."""

    if Account.login_user(email, password):
        user_details = Account.user_accounts.get(email)
        print(prompts.LOGIN_SUCCESS)
        display_login_menu(email, user_details)
    else:
        print(prompts.LOGIN_FAILED)


def display_main_menu():
    """Main function to handle menu options."""
    while True:
        opt = get_user_option(prompts.WELCOME_TEXT, main_menu_options)
        if opt == 0:
            print(prompts.EXIT)
            break
        if opt == 1:
            email = UserInputHandler.get_valid_email("Enter your email to login: ")
            password = input("Enter your password: ")
            login_user(email, password)
        elif opt == 2:
            register_user()
        else:
            print(prompts.INVALID_INPUT_TEXT)


def display_login_menu(email, user_details):
    """sub function to handle login menu options."""
    while True:
        opt = get_user_option(
            prompts.WELCOME_LOGIN_TEXT.format(
                prompts.DASHES,
                user_details["first_name"],
                user_details["last_name"],
                user_details["account_balance"],
                prompts.DASHES,
            ),
            login_menu_options,
        )
        if opt in (0, 9):
            print(prompts.LOGOUT)
            break
        if opt == 1:
            print(prompts.MY_DETAILS)
            Account.display_user_details(email)
        elif opt == 2:
            pass
        else:
            print(prompts.INVALID_INPUT_TEXT)


def main():
    """Main function to start the program"""
    Account.load_data()
    display_main_menu()


main()
