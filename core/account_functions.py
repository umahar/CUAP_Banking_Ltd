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
    def display_user_details(user):
        """get the user details based on an email and prints them one by one"""
        print(
            f"1. Email: {user.email}\n2. First Name: {user.first_name}\n3. Last Name: {user.last_name}"
            f"\n4. Gender: {user.gender}\n5. Phone No: {user.phone_no}\n6. Password: {user.password}\n7. Account Balance: {user.account_balance}"
            f"\n8. Account Type: {user.account_type}\n9. Date Created: {user.date_created}\n10. Date of Birth: {user.date_of_birth}\n11. Country: {user.country}\n12. City: {user.city}"
        )

    @staticmethod
    def edit_user_details(user):
        """function to edit the current user details"""
        menu_items = [
            f"First Name: {user.first_name}",
            f"Last Name: {user.last_name}",
            f"Gender: {user.gender}",
            f"Email: {user.email}",
            f"Phone No: {user.phone_no}",
            f"Password: {user.password}",
            f"Account Balance: {user.account_balance}",
            f"Account Type: {user.account_type}",
            f"Date Created: {user.date_created}",
            f"Date of Birth: {user.date_of_birth}",
            f"Country: {user.country}",
            f"City: {user.city}",
        ]
        opt = AccountFunctions.get_user_option(prompts.EDIT_DETAILS, menu_items)
        func_map = {
            1: lambda: Account.handle_edit(
                user, "first_name", "Enter your new First Name: "
            ),
            2: lambda: Account.handle_edit(
                user, "last_name", "Enter your new Last Name: "
            ),
            3: lambda: Account.handle_edit(user, "gender", "Enter your new Gender: "),
            4: lambda: Account.handle_edit(user, "email", "Enter your new Email: "),
            5: lambda: Account.handle_edit(
                user, "phone_no", "Enter your new Phone No: "
            ),
            6: lambda: Account.handle_edit(
                user, "password", "Enter your new Password: "
            ),
            7: lambda: Account.handle_edit(
                user, "account_balance", "Enter your new Acount Balance: "
            ),
            8: lambda: Account.handle_edit(
                user, "account_type", "Enter your new Account Type: "
            ),
            9: lambda: Account.handle_edit(
                user, "date_created", "Enter your new Date of Acc Creation: "
            ),
            10: lambda: Account.handle_edit(
                user, "date_of_birth", "Enter your new Date of Birth: "
            ),
            11: lambda: Account.handle_edit(
                user, "country", "Enter your new Country: "
            ),
            12: lambda: Account.handle_edit(user, "city", "Enter your new City: "),
        }
        if opt == 0:
            pass
        if opt in func_map:
            func_map[opt]()
        else:
            print(prompts.INVALID_INPUT_TEXT)
