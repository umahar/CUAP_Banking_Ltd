"""this class manages auxillary functions to do tasks"""

from core.account import Account
from core.account_number import AccountNumber
from data import prompts
from utils.input_handler import UserInputHandler


class AccountFunctions:
    """this class will handle all functions that a logged in user can perform"""

    @staticmethod
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

    @staticmethod
    def handle_my_details(user):
        """the function handles the user function of My Details"""
        print(prompts.MY_DETAILS)
        AccountFunctions.display_user_details(user)

    @staticmethod
    def handle_edit_details(user):
        """the function handles the user function of Edit Details"""
        AccountFunctions.edit_user_details(user)

    @staticmethod
    def handle_check_balance(user):
        """the function handles the user function of Check Balance"""
        print(prompts.CURRENT_BALANCE.format(user.balance.get_balance()))

    @staticmethod
    def handle_deposit_money(user):
        """the function handles the user function of deposit_money"""
        print(prompts.CURRENT_BALANCE.format(user.balance.get_balance()))
        amount = UserInputHandler.get_valid_initial_deposit(
            "Enter your Deposit Amount: "
        )
        user.balance.deposit(amount)
        print(prompts.CURRENT_BALANCE.format(user.balance.get_balance()))
        print(prompts.DEPOSIT_SUCCESSFUL)

    @staticmethod
    def handle_withdraw_money(user):
        """the function handles the user function of withdraw_money"""
        print(prompts.CURRENT_BALANCE.format(user.balance.get_balance()))
        amount = UserInputHandler.get_valid_initial_deposit(
            "Enter your Withdrawal Amount: "
        )
        if user.balance.withdraw(amount):
            print(prompts.CURRENT_BALANCE.format(user.balance.get_balance()))
            print(prompts.WITHDRAW_SUCCESSFUL)
        else:
            print(prompts.INSUFFICIENT_BALANCE)

    @staticmethod
    def handle_change_pin(user):
        """the function handles the user function of change_pin"""

    @staticmethod
    def handle_my_cards(user):
        """the function handles the user function of my_cards"""

    @staticmethod
    def handle_transfer_money(user):
        """the function handles the user function of transfer_money"""
        sender = user
        sender_acc_num = sender.account_number.get_account_number()
        sender_balance = sender.balance.get_balance()
        print(prompts.CURRENT_BALANCE.format(sender_balance))
        amount_to_send = UserInputHandler.get_valid_transfer_amount(
            "Enter the amount to Transfer: ", sender_balance
        )
        rec_acc_num = UserInputHandler.get_valid_account_number(
            "Enter the Account Number of the recipient: "
        )
        if sender_acc_num == rec_acc_num:
            print(prompts.INV_ACCOUNT_NUMBER)
        elif sender_acc_num != rec_acc_num:
            if AccountNumber.is_account_number(rec_acc_num):
                # get the receiver user
                receiver = Account.get_account_by_acc_num(rec_acc_num)
                if receiver:
                    print(
                        f"\nRecipient Account Title: {receiver.first_name.title()} {receiver.last_name.title()}"
                    )
                    options = ["YES", "NO"]
                    opt = AccountFunctions.get_user_option(
                        "Do you wish to Proceed with the Transfer? ", options
                    )
                    if opt == 1:
                        print(prompts.CONFIRM_TRANSFER)
                        sender.balance.withdraw(amount_to_send)
                        receiver.balance.deposit(amount_to_send)
                        print(prompts.TRANSFER_COMPLETE)
                        print(
                            prompts.CURRENT_BALANCE.format(sender.balance.get_balance())
                        )
                    if opt == 2:
                        print(prompts.TRANSFER_INCOMPLETE)
                else:
                    print(prompts.NO_ACCOUNT_FOUND)
        else:
            print(prompts.NO_ACCOUNT_FOUND)

    @staticmethod
    def handle_notifications(user):
        """the function handles the user function of notifications"""

    @staticmethod
    def handle_account_statement(user):
        """the function handles the user function of account_statement"""

    @staticmethod
    def handle_account_investments(user):
        """the function handles the user function of account_investments"""

    @staticmethod
    def display_user_details(user):
        """get the user details based on an email and prints them one by one"""
        print(
            f"Email: {user.email}\nFirst Name: {user.first_name}"
            f"\nLast Name: {user.last_name}\nBalance: {user.balance.get_balance()}"
            f"\nAccount Number: {user.account_number.get_account_number()} \nGender: {user.gender}"
            f"\nPhone No: {user.phone_no}\nPassword: {user.password}"
            f"\nInitial Deposit: {user.initial_deposit}\nAccount Type: {user.account_type}"
            f"\nDate Created: {user.date_created}\nDate of Birth: {user.date_of_birth}"
            f"\nCountry: {user.country}\nCity: {user.city}"
        )

    @staticmethod
    def edit_user_details(user):
        """Function to edit the current user details."""

        # List of user attributes and their corresponding prompts
        editable_fields = [
            ("first_name", "Enter your new First Name: "),
            ("last_name", "Enter your new Last Name: "),
            ("gender", "Enter your new Gender: "),
            ("email", "Enter your new Email: "),
            ("phone_no", "Enter your new Phone No: "),
            ("password", "Enter your new Password: "),
            ("account_type", "Enter your new Account Type: "),
            ("date_of_birth", "Enter your new Date of Birth: "),
            ("country", "Enter your new Country: "),
            ("city", "Enter your new City: "),
        ]

        # Create the menu items dynamically
        menu_items = [
            f"{field_name.replace('_', ' ').title()}: {getattr(user, field_name)}"
            for field_name, _ in editable_fields
        ]

        opt = AccountFunctions.get_user_option(prompts.EDIT_DETAILS, menu_items)

        if 0 < opt <= len(editable_fields):
            field_name, prompt = editable_fields[opt - 1]
            Account.handle_edit(user, field_name, prompt)
        elif opt == 0:
            pass
        else:
            print(prompts.INVALID_INPUT_TEXT)
