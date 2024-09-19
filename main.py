"""The bank app starts here. This main function will keep it going."""

from data import prompts, menu_options as mo
from core import account
from utils import input_check

Account = account.Account
chk_inp = input_check.CheckInput


def display_main_menu():
    """function that displays menu until the user enters 0. Handles invalid input"""
    print(prompts.WELCOME_TEXT)
    # main loop that keeps showing menu from a list retrieved from data until user enters 0
    while True:
        print(prompts.MENU_TEXT)
        for index, item in enumerate(mo.main_menu_options):
            print(f"{index + 1}. {item}")
        opt = input("\nOption #: ")
        if not opt.strip().isdigit():
            print(prompts.INVALID_INPUT_TEXT)
            continue
        opt = int(opt)
        # exit the program is user enters zero
        if opt == 0:
            print(prompts.EXIT)
            break
        # check if the opt is valid from menu
        if 0 < opt <= len(mo.main_menu_options):
            print("\nSelection --> ", mo.main_menu_options[opt - 1], "\n")
            email = input(f"Enter your email to {mo.main_menu_options[opt-1]}: ")
            while not chk_inp.is_valid_email(email):
                print("Invalid Email")
                email = input(f"Enter your email to {mo.main_menu_options[opt-1]}: ")
            password = input("Enter your password: ")
            while not chk_inp.is_valid_password(password):
                print("Invalid Password")
                password = input("Enter your password: ")
            # if user selects to login, check if the user exists and login the user
            if opt == 1:
                if Account.login_user(email, password):
                    print(prompts.LOGIN_SUCCESS)
                else:
                    print(prompts.LOGIN_FAILED)
            # if user selects register, check if the user exists and register a new user
            elif opt == 2:
                if Account.is_old_user(email):
                    print(prompts.REGISTER_FAILED)
                else:
                    phone_no = input("Enter your phone no: ")
                    first_name = input("Enter your first name: ")
                    last_name = input("Enter your last name: ")
                    gender = input("Enter your gender: ")
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
                    if new_account.register_user():
                        print(prompts.REGISTER_SUCCESS)
                    else:
                        print(prompts.UNKNOWN_ERROR)

        else:
            print(prompts.INVALID_INPUT_TEXT)


display_main_menu()
