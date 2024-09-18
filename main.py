"""The program starts here. This main function will keep it going."""

from data import prompts, menu_options as mo
from core import account


def display_menu():
    """function that displays menu until the user enters 0. Handles invalid input"""
    print(prompts.WELCOME_TEXT)
    while True:
        print(prompts.MENU_TEXT)
        for index, item in enumerate(mo.main_menu_options):
            print(f"{index + 1}. {item}")
        opt = input("\nOption #: ")
        if not opt.strip().isdigit():
            print(prompts.INVALID_INPUT_TEXT)
            continue
        opt = int(opt)
        if opt == 0:
            print(prompts.EXIT)
            break
        if 0 < opt <= len(mo.main_menu_options):
            print("\nSelection --> ", mo.main_menu_options[opt - 1], "\n")
            handle_input(opt)
        else:
            print(prompts.INVALID_INPUT_TEXT)


def handle_input(opt):
    """This function will take opt which is the option selected
    by user and handle the function required

    Args:
        opt (int): will be an option within main menu
    """
    if opt == 1:
        email = input("Enter your email: ")
        if account.Account.is_new_user(email):
            print("You do not have an account. Please register")
        else:
            password = input("Enter your password: ")
            account.Account.login_account(email, password)
    elif opt == 2:
        email = input("Enter your email: ")
        phone_no = input("Enter your phone no: ")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        gender = input("Enter your gender: ")
        password = input("Enter your password: ")
        initial_deposit = input("Enter your initial deposit: ")
        account_type = input("Enter your account type: ")
        date_of_birth = input("Enter your date of birth: ")
        country = input("Enter your country: ")
        city = input("Enter your city: ")
        new_account = account.Account(
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
        )
        new_account.register_account()


display_menu()
