"""This is the main.py The program starts from this file"""

from data import prompts
from data.menu_options import main_menu_options
from data.menu_options import login_menu_options
from core.account import Account
from core.account_functions import AccountFunctions
from core.notification import Notification
from utils.input_handler import UserInputHandler


def exit_program():
    """kills the program"""
    print(prompts.EXIT)
    return True


def handle_login():
    """handles login for user"""
    email = UserInputHandler.get_valid_email("Enter your account Email to Login: ")
    password = input("Enter your Account Password: ")
    user = Account.login_user(email, password)
    if user:
        print(prompts.LOGIN_SUCCESS)
        new_notification = Notification(
            notification_type="Logged_In",
            acc_num=f"{user.account_number.get_account_number()}",
            acc_name=f"{user.first_name.title()} {user.last_name.title()}",
        )
        user.notifications.append(new_notification)
        unread_notifications = []
        for notification in user.notifications:
            if notification.status == "Unread":
                unread_notifications.append(notification)
        print(prompts.UNREAD_NOTIFICATIONS.format(len(unread_notifications)))
        display_login_menu(user)
    else:
        print(prompts.LOGIN_FAILED)


def handle_register():
    """handles register for new user"""
    user = Account.register_user()
    if user:
        print(prompts.REGISTER_SUCCESS)
        new_notification = Notification(
            notification_type="Registered",
            acc_num=f"{user.account_number.get_account_number()}",
            acc_name=f"{user.first_name.title()} {user.last_name.title()}",
        )
        user.notifications.append(new_notification)
        display_login_menu(user)
    else:
        print(prompts.REGISTER_FAILED)


def handle_bill_payment():
    """function to allow user to pay bills without login"""
    bill_id = input("Enter your Bill ID: ")
    if bill_id in Account.bill_ids:
        AccountFunctions.handle_bill_payment(bill_id)
    else:
        print(prompts.INVALID_BILL_ID)


def display_main_menu():
    """Main function to handle menu options."""
    while True:
        opt = AccountFunctions.get_user_option(prompts.WELCOME_TEXT, main_menu_options)
        func_map = {
            0: exit_program,
            1: handle_login,
            2: handle_register,
            3: handle_bill_payment,
        }
        if opt in func_map:
            if func_map[opt]():
                break
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
        func_map = {
            1: AccountFunctions.handle_my_details,
            2: AccountFunctions.handle_edit_details,
            3: AccountFunctions.handle_check_balance,
            4: AccountFunctions.handle_deposit_money,
            5: AccountFunctions.handle_withdraw_money,
            6: AccountFunctions.handle_change_pin,
            7: AccountFunctions.handle_my_cards,
            8: AccountFunctions.handle_transfer_money,
            9: AccountFunctions.handle_notifications,
            10: AccountFunctions.handle_account_statement,
            11: AccountFunctions.handle_account_investments,
        }
        if opt in (0, 12):
            new_notification = Notification(
                notification_type="Logged_Out",
                acc_num=f"{user.account_number.get_account_number()}",
                acc_name=f"{user.first_name.title()} {user.last_name.title()}",
            )
            user.notifications.append(new_notification)
            break
        if opt in func_map:
            if func_map[opt](user):
                break
        else:
            print(prompts.INVALID_INPUT_TEXT)


def main():
    """Main function to start the program"""
    AccountFunctions.load_data()
    display_main_menu()


main()
