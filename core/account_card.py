"""this is the class that will deal with all user account cards"""

import random
import datetime


class AccountCard:
    """handles credit/debit cards for users"""

    card_numbers = []

    def __init__(
        self,
        card_holder,
        card_name=None,
        card_type=None,
        card_number=None,
        card_issue_date=None,
        card_expiry_date=None,
        card_cvv=None,
        card_limit=100000,
        card_status="Initiated",
    ):
        """Initializes the card with either provided or generated values"""

        self.card_holder = card_holder
        self.card_type = (
            card_type if card_type is not None else self.generate_card_type()
        )
        self.card_number = (
            card_number if card_number is not None else self.generate_card_number()
        )
        self.card_issue_date = (
            card_issue_date
            if card_issue_date is not None
            else self.generate_card_issue_date()
        )
        self.card_name = (
            card_name if card_name is not None else self.generate_card_name()
        )
        self.card_expiry_date = (
            card_expiry_date
            if card_expiry_date is not None
            else self.generate_card_expiry_date()
        )
        self.card_cvv = card_cvv if card_cvv is not None else self.generate_card_cvv()
        self.card_limit = card_limit
        self.card_status = card_status

        if card_type is None:
            self.save_data_to_file()

    def save_data_to_file(self, update=False):
        """this functions will save/update the cards data on the text file"""
        if update:
            with open("data/user_cards_data.txt", "r", encoding="UTF-8") as fp:
                lines = fp.readlines()
                updated_lines = []
                for line in lines:
                    dp = line.split()
                    card_num = f"{dp[4]} {dp[5]} {dp[6]} {dp[7]}"
                    if self.card_number == card_num:
                        dp[-1] = self.card_status
                        updated_line = " ".join(dp)
                    else:
                        updated_line = line.strip()
                    updated_lines.append(updated_line + "\n")
            with open("data/user_cards_data.txt", "w", encoding="UTF-8") as file:
                file.writelines(updated_lines)
        else:
            with open("data/user_cards_data.txt", encoding="UTF-8", mode="a") as file:
                data = f"{self.card_holder.account_number.get_account_number()} {self.card_name} \
{self.card_type} {self.card_number} {self.card_issue_date} {self.card_expiry_date} \
{self.card_cvv} {self.card_limit} {self.card_status}"
                file.write(data + "\n")

    def generate_card_type(self):
        """generates the card type randomly"""
        if self.card_holder.balance.get_balance() < 10000:
            return random.choice(["Visa", "Mastercard"])
        return random.choice(["AmericanExpress", "UnionPay"])

    def generate_card_name(self):
        """generates card name"""
        return f"{self.card_holder.first_name.title()} {self.card_holder.last_name.title()}"

    @staticmethod
    def generate_card_number():
        """generates the card number"""
        card_num = ""
        count = 0
        while True:
            four_digits = random.randint(1000, 9999)
            card_num = card_num + " " + str(four_digits)
            count += 1
            if count == 4:
                if card_num in AccountCard.card_numbers:
                    count = 0
                    card_num = ""
                    continue
                AccountCard.card_numbers.append(card_num)
                break
        return card_num

    @staticmethod
    def generate_card_issue_date():
        """generates the card issue date"""
        now = datetime.datetime.now()
        month = now.month
        year_last_two_digits = str(now.year)[-2:]
        return f"{month:02d}/{year_last_two_digits}"

    @staticmethod
    def generate_card_expiry_date():
        """generates the card expiry date"""
        now = datetime.datetime.now()
        expiry_year = now.year + 3
        month = now.month
        year_last_two_digits = str(expiry_year)[-2:]
        return f"{month:02d}/{year_last_two_digits}"

    @staticmethod
    def generate_card_cvv():
        """generates the card cvv"""
        return random.randint(100, 999)

    def show_card_details(self):
        """displays card details"""
        data = f"{self.card_name} {self.card_type} {self.card_number} {self.card_issue_date} \
{self.card_expiry_date} {self.card_cvv} {self.card_limit} {self.card_status}"
        print(data)

    def change_card_status(self, new_status):
        """changes the current status of the card"""
        if new_status == "Activate Card":

            if self.card_status in ("Initiated", "Temporary-Blocked"):
                self.card_status = "Activated"
                self.save_data_to_file(update=True)
                return f"Your Account Card ending with {self.card_number[-4:]} has been Activated."
            if self.card_status == "Permanent-Blocked":
                return "This card is Permanently Blocked. It can not be Activated. \
Please contact support."
            return "Your Account Card is already set to Active."

        if new_status == "Temporary Block":

            if self.card_status in ("Initiated", "Activated"):
                self.card_status = "Temporary-Blocked"
                self.save_data_to_file(update=True)
                return f"Your Account Card ending with {self.card_number[-4:]} \
has been set to Temporary Blocked."
            if self.card_status == "Permanent-Blocked":
                return "This card is Permanently Blocked. \
It can not be Temporarily Block. Please contact support."
            return "Your Account Card is already set to Temporary Block."

        if new_status == "Permanent Block":

            if self.card_status in ("Initiated", "Activated", "Temporary-Blocked"):
                self.card_status = "Permanent-Blocked"
                self.save_data_to_file(update=True)
                return f"Your Account Card ending with {self.card_number[-4:]} \
has been set to Permanent-Blocked."
            return "Your Account Card is already set to Permanent Block."
