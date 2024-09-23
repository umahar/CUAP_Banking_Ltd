"""This is the main.py The program starts from this file"""

from data import prompts
from data.menu_options import main_menu_options
from data.menu_options import login_menu_options
from core.account import Account
from core.account_functions import AccountFunctions
from utils.input_handler import UserInputHandler


def display_main_menu():
    """Main function to handle menu options."""
    while True:
        opt = AccountFunctions.get_user_option(prompts.WELCOME_TEXT, main_menu_options)
        if opt == 0:
            print(prompts.EXIT)
            break
        if opt == 1:
            email = UserInputHandler.get_valid_email(
                "Enter your account Email to login: "
            )
            password = input("Enter your account Password: ")
            user_details = Account.handle_login_user(email, password)
            if user_details:
                display_login_menu(email, user_details)
        elif opt == 2:
            Account.handle_register_user()
        else:
            print(prompts.INVALID_INPUT_TEXT)


def display_login_menu(email, user_details):
    """sub function to handle login menu options."""
    while True:
        opt = AccountFunctions.get_user_option(
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
            AccountFunctions.display_user_details(email)
        elif opt == 2:
            AccountFunctions.edit_user_details(email)
        else:
            print(prompts.INVALID_INPUT_TEXT)


def main():
    """Main function to start the program"""
    Account.load_data()
    display_main_menu()


main()
