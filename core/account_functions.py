from core.account import Account
from data import prompts


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
    def display_user_details(email):
        """get the user details based on an email and prints them one by one"""
        user_details = Account.user_accounts.get(email)
        count = 1
        for key,value in user_details.items():
            print(f"{count}. {key.replace("_"," ").title()}:  {value}")
            count+=1
    
    @staticmethod
    def edit_user_details(email):
        """function to edit the current user details"""
        raw_menu_items = Account.user_accounts.get(email)
        menu_items = []
        for item in raw_menu_items:
            menu_items.append(item.replace("_", " ").title())
        opt = AccountFunctions.get_user_option(prompts.EDIT_DETAILS, menu_items)
        func_map = {
            1: lambda: Account.handle_edit(
                email, "first_name", "Enter your new First Name: "
            ),
            2: lambda: Account.handle_edit(
                email, "last_name", "Enter your new Last Name: "
            ),
            3: lambda: Account.handle_edit(email, "gender", "Enter your new Gender: "),
            4: lambda: Account.handle_edit(email, "email", "Enter your new Email: "),
            5: lambda: Account.handle_edit(
                email, "phone_no", "Enter your new Phone No: "
            ),
            6: lambda: Account.handle_edit(
                email, "password", "Enter your new Password: "
            ),
            7: lambda: Account.handle_edit(
                email, "account_balance", "Enter your new Acount Balance: "
            ),
            8: lambda: Account.handle_edit(
                email, "account_type", "Enter your new Account Type: "
            ),
            9: lambda: Account.handle_edit(
                email, "date_created", "Enter your new Date of Acc Creation: "
            ),
            10: lambda: Account.handle_edit(
                email, "date_of_birth", "Enter your new Date of Birth: "
            ),
            11: lambda: Account.handle_edit(
                email, "country", "Enter your new Country: "
            ),
            12: lambda: Account.handle_edit(email, "city", "Enter your new City: "),
        }
        if opt == 0:
            pass
        if opt in func_map:
            func_map[opt]()
        else:
            print(prompts.INVALID_INPUT_TEXT)
