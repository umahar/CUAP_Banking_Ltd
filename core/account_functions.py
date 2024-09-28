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
        pin = UserInputHandler.get_valid_pin("Enter your PIN Code: ")
        if Account.validate_pin(user.email, pin):
            AccountFunctions.edit_user_details(user)
        else:
            print(prompts.WRONG_PIN)

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
        pin = UserInputHandler.get_valid_pin("Enter your PIN Code: ")
        if Account.validate_pin(user.email, pin):
            user.balance.deposit(amount)
            print(prompts.CURRENT_BALANCE.format(user.balance.get_balance()))
            print(prompts.DEPOSIT_SUCCESSFUL)
        else:
            print(prompts.WRONG_PIN)

    @staticmethod
    def handle_withdraw_money(user):
        """the function handles the user function of withdraw_money"""
        print(prompts.CURRENT_BALANCE.format(user.balance.get_balance()))
        amount = UserInputHandler.get_valid_initial_deposit(
            "Enter your Withdrawal Amount: "
        )
        pin = UserInputHandler.get_valid_pin("Enter your PIN Code: ")
        if Account.validate_pin(user.email, pin):
            if user.balance.withdraw(amount):
                print(prompts.CURRENT_BALANCE.format(user.balance.get_balance()))
                print(prompts.WITHDRAW_SUCCESSFUL)
            else:
                print(prompts.INSUFFICIENT_BALANCE)
        else:
            print(prompts.WRONG_PIN)

    @staticmethod
    def handle_change_pin(user):
        """the function handles the user function of change_pin"""
        pin = UserInputHandler.get_valid_pin("Enter your current PIN Code: ")
        if Account.validate_pin(user.email, pin):
            Account.handle_edit(user, "pin", "Enter your new PIN Code: ")
        else:
            print(prompts.WRONG_PIN)

    @staticmethod
    def handle_my_cards(user):
        """the function handles the user function of my_cards"""
        print(prompts.MANAGE_CARDS)
        heading = f"Total Cards: {len(user.cards)}"
        cards_menu = ["Order a New Card"]
        for card in user.cards:
            data = f"{card.card_name} {card.card_type} {card.card_number} {card.card_issue_date} {card.card_expiry_date} {card.card_cvv} {card.card_limit} {card.card_status}"
            cards_menu.append(data)
        opt = AccountFunctions.get_user_option(heading, cards_menu)
        if opt == 0:
            print(prompts.EXIT)
        if opt == 1:
            if len(user.cards) == 3:
                print(prompts.NEW_CARD_LIMIT)
            else:
                heading = f"\nDo you wish to get {user.first_name.title()} {user.last_name.title()} as your full name on the card?"
                opt = AccountFunctions.get_user_option(heading, ["Yes", "No"])
                if opt == 1:
                    user.add_card()
                if opt == 2:
                    f_name = UserInputHandler.get_valid_first_name(
                        "Enter your First Name: "
                    )
                    l_name = UserInputHandler.get_valid_first_name(
                        "Enter your Last Name: "
                    )
                    full_name = f"{f_name} {l_name}"
                    user.add_card(name=full_name)
                    print(prompts.CARD_CREATED)
        elif opt > 1:
            index = opt - 2
            card = user.cards[index]
            print(f"Selection: {cards_menu[opt-1]}")
            print(f"Card Current Status: {card.card_status}\n")
            heading = "What would you like to do to this card?"
            options = [
                "Activate Card",
                "Temporary Block",
                "Permanent Block",
                "Change Limit",
            ]
            opt = AccountFunctions.get_user_option(heading, options)
            if opt == 0:
                print(prompts.EXIT)
            if opt in (1, 2, 3):
                pin = UserInputHandler.get_valid_pin("Enter your PIN Code: ")
                if Account.validate_pin(user.email, pin):
                    index = opt - 1
                    new_status = options[index]
                    response = card.change_card_status(new_status)
                    print(f"{prompts.DASHES}{response}{prompts.DASHES}")
                else:
                    print(prompts.WRONG_PIN)
            if opt == 4:
                print(f"\nCurrent Card Limit: {card.card_limit}")
                print("Contact Support to change this limit")
                # will finish later on

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
                        pin = UserInputHandler.get_valid_pin("Enter your PIN Code: ")
                        if Account.validate_pin(user.email, pin):
                            print(prompts.CONFIRM_TRANSFER)
                            sender.balance.withdraw(amount_to_send)
                            receiver.balance.deposit(amount_to_send)
                            print(prompts.TRANSFER_COMPLETE)
                            print(
                                prompts.CURRENT_BALANCE.format(
                                    sender.balance.get_balance()
                                )
                            )
                        else:
                            print(prompts.WRONG_PIN)
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
            f"\nPhone No: {user.phone_no}\nPassword: {user.password}\nPIN: {user.pin}"
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

    @staticmethod
    def handle_bill_payment():
        """handles bill payment for user"""
        given_card_no = input("Enter your Card Number: ")
        given_card_name = input("Enter your Card Full Name: ")
        given_card_expiry = input("Enter your Card Expiry Data: ")
        given_card_cvv = input("Enter your Card CVV: ")

        user_email = None
        for email in Account.accounts_data:
            c_user = Account.get_account_by_email(email)
            for curr_card in c_user.cards:
                if AccountFunctions.is_card_matched(
                    curr_card,
                    given_card_no,
                    given_card_name,
                    given_card_expiry,
                    given_card_cvv,
                ):
                    user_email = email
                    break
        if user_email:
            user = Account.get_account_by_email(user_email)
            if user.balance.get_balance() < 5000:
                print(prompts.INSUFFICIENT_BALANCE)
            else:
                print(prompts.CONFIRM_TRANSFER)
                pin = UserInputHandler.get_valid_pin("Enter your PIN Code: ")
                if Account.validate_pin(user.email, pin):
                    if user.balance.withdraw(5000):
                        print(prompts.BILL_PAID)
                else:
                    print(prompts.WRONG_PIN)
        else:
            print(prompts.IN_CARD_DETAILS)

    @staticmethod
    def is_card_matched(
        card, given_card_no, given_card_name, given_card_expiry, given_card_cvv
    ):
        """matches user entered card details with actual details"""
        if (
            card.card_number == given_card_no
            and card.card_name == given_card_name
            and card.card_expiry_date == given_card_expiry
            and str(card.card_cvv) == given_card_cvv
            and card.card_status == "Activated"
        ):
            return True
        return False
