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
            user = Account.login_user(email, password)
            if user:
                print(prompts.LOGIN_SUCCESS)
                display_login_menu(user)
            else:
                print(prompts.LOGIN_FAILED)
        elif opt == 2:
            user = Account.register_user()
            if user:
                print(prompts.REGISTER_SUCCESS)
                display_login_menu(user)
            else:
                print(prompts.REGISTER_FAILED)
        else:
            print(prompts.INVALID_INPUT_TEXT)


def display_login_menu(user):
    """sub function to handle login menu options."""
    while True:
        opt = AccountFunctions.get_user_option(
            prompts.WELCOME_LOGIN_TEXT.format(
                prompts.DASHES,
                user.first_name,
                user.last_name,
                prompts.DASHES,
            ),
            login_menu_options,
        )
        if opt in (0, 9):
            print(prompts.LOGOUT)
            break
        if opt == 1:
            print(prompts.MY_DETAILS)
            AccountFunctions.display_user_details(user)
        elif opt == 2:
            AccountFunctions.edit_user_details(user)
        elif opt == 3:
            print(prompts.CURRENT_BALANCE.format(user.balance.get_balance()))
        elif opt == 4:
            print(prompts.CURRENT_BALANCE.format(user.balance.get_balance()))
            amount = UserInputHandler.get_valid_initial_deposit(
                "Enter your Deposit Amount: "
            )
            user.balance.deposit(amount)
            print(prompts.CURRENT_BALANCE.format(user.balance.get_balance()))
            print(prompts.DEPOSIT_SUCCESSFUL)
        elif opt == 5:
            print(prompts.CURRENT_BALANCE.format(user.balance.get_balance()))
            amount = UserInputHandler.get_valid_initial_deposit(
                "Enter your WithDrawl Amount: "
            )
            if user.balance.withdraw(amount):
                print(prompts.CURRENT_BALANCE.format(user.balance.get_balance()))
                print(prompts.WITHDRAW_SUCCESSFUL)
            else:
                print(prompts.INSUFFICIENT_BALANCE)
        else:
            print(prompts.INVALID_INPUT_TEXT)


def main():
    """Main function to start the program"""
    Account.load_data()
    display_main_menu()


main()
