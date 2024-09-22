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
    email = UserInputHandler.get_valid_email("Enter your Email to register: ")
    if Account.is_old_user(email):
        print(prompts.REGISTER_FAILED)
    else:
        password = UserInputHandler.get_valid_password("Enter your Password: ")
        phone_no = UserInputHandler.get_valid_phone_no("Enter your Phone No: ")
        first_name = UserInputHandler.get_valid_first_name("Enter your First Name: ")
        last_name = UserInputHandler.get_valid_last_name("Enter your Last Name: ")
        gender = UserInputHandler.get_valid_gender(
            "Enter your gender (Male/Female/Other): "
        )
        account_balance = UserInputHandler.get_valid_account_balance("Enter your initial Deposit: ")
        account_type = UserInputHandler.get_valid_account_type(
            """Enter your Account type("Current", "Saving", "Other"): """
        )
        date_of_birth = UserInputHandler.get_valid_date_of_birth(
            "Enter your Date of Birth (YYYY-MM-DD): "
        )
        country = UserInputHandler.get_valid_country("Enter name of your Country: ")
        city = UserInputHandler.get_valid_city("Enter name of your City: ")
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
            email = UserInputHandler.get_valid_email("Enter your account Email to login: ")
            password = input("Enter your account Password: ")
            login_user(email, password)
        elif opt == 2:
            register_user()
        else:
            print(prompts.INVALID_INPUT_TEXT)


def handle_edit(email, item_to_edit, prompt):
    """the function to take the new data and call the update functions"""
    if item_to_edit in ('account_balance','date_created'):
        print(prompts.EDIT_NOT_ALLOWED)
    else:
        current_data = Account.user_accounts[email][item_to_edit]
        print(f"Current {item_to_edit.title().replace("_"," ")}: ",current_data)
        get_function_name = f"get_valid_{item_to_edit}"
        get_function = getattr(UserInputHandler, get_function_name)
        new_data = get_function(prompt)
        if item_to_edit=='email':
            while Account.is_old_user(new_data):
                print(prompts.REGISTER_FAILED)
                new_data = get_function(prompt)
        Account.update_new_value(email, item_to_edit, new_data)
        print(
            f"{prompts.DASHES}Changing {item_to_edit.title().replace("_"," ")}:"
            f" '{current_data}' to '{new_data}'{prompts.DASHES}"
        )
        print(prompts.UPDATE_SUCCESSFUL)


def edit_user_details(email):
    """function to edit the current user details"""
    raw_menu_items = Account.user_accounts.get(email)
    menu_items = []
    for item in raw_menu_items:
        menu_items.append(item.replace("_", " ").title())
    opt = get_user_option(prompts.EDIT_DETAILS, menu_items)
    func_map = {
        1: lambda: handle_edit(email, "first_name", "Enter your new First Name: "),
        2: lambda: handle_edit(email, "last_name", "Enter your new Last Name: "),
        3: lambda: handle_edit(email, "gender", "Enter your new Gender: "),
        4: lambda: handle_edit(email, "email", "Enter your new Email: "),
        5: lambda: handle_edit(email, "phone_no", "Enter your new Phone No: "),
        6: lambda: handle_edit(email, "password", "Enter your new Password: "),
        7: lambda: handle_edit(email, "account_balance", "Enter your new Acount Balance: "),
        8: lambda: handle_edit(email, "account_type", "Enter your new Account Type: "),
        9: lambda: handle_edit(email, "date_created", "Enter your new Date of Acc Creation: "),
        10: lambda: handle_edit(email, "date_of_birth", "Enter your new Date of Birth: "),
        11: lambda: handle_edit(email, "country", "Enter your new Country: "),
        12: lambda: handle_edit(email, "city", "Enter your new City: "),
    }
    if opt == 0:
        pass
    if opt in func_map:
        func_map[opt]()
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
            edit_user_details(email)
        else:
            print(prompts.INVALID_INPUT_TEXT)


def main():
    """Main function to start the program"""
    Account.load_data()
    display_main_menu()


main()
