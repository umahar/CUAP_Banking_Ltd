from data import prompts, menu_options as mo
from core.account import Account
from utils.input_handler import UserInputHandler


def get_user_option():
    """Display the main menu and get the user's option."""
    print(prompts.WELCOME_TEXT)
    while True:
        print(prompts.MENU_TEXT)
        for index, item in enumerate(mo.main_menu_options):
            print(f"{index + 1}. {item}")
        opt = input("\nOption #: ")
        if opt.strip().isdigit():
            opt = int(opt)
            if 0 <= opt <= len(mo.main_menu_options):
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
        initial_deposit = UserInputHandler.get_valid_deposit(
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


def login_user():
    """Handle user login."""
    email = UserInputHandler.get_valid_email("Enter your email to register: ")
    password = input("Enter your password: ")
    if Account.login_user(email, password):
        print(prompts.LOGIN_SUCCESS)
    else:
        print(prompts.LOGIN_FAILED)


def display_main_menu():
    """Main function to handle menu options."""
    while True:
        opt = get_user_option()
        if opt == 0:
            print(prompts.EXIT)
            break
        if opt == 1:
            login_user()
        elif opt == 2:
            register_user()
        else:
            print(prompts.INVALID_INPUT_TEXT)


display_main_menu()
