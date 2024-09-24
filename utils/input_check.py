"""this file will actually check and validate the inputs provided for each fields"""

import re


class CheckInput:
    """this class will actually check and validate the inputs provided for each fields"""

    @staticmethod
    def is_valid_email(email):
        """function to check if email is valid"""
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, email) is not None

    @staticmethod
    def is_valid_password(password):
        """function to check if password is valid"""
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[0-9]", password):
            return False
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False
        return True

    @staticmethod
    def is_valid_phone_no(phone_no):
        """function to check if phone no is valid"""
        phone_regex = r"^\+?[0-9]{10,15}$"
        return re.match(phone_regex, phone_no) is not None

    @staticmethod
    def is_valid_name(name):
        """function to check if name is valid"""
        name_regex = r"^[A-Za-z\s-]{2,50}$"
        return re.match(name_regex, name) is not None

    @staticmethod
    def is_valid_deposit(initial_deposit):
        """function to check if account balance is valid"""
        try:
            amount = float(initial_deposit)
            return amount > 0
        except ValueError:
            return False

    @staticmethod
    def is_valid_dob(dob):
        """function to check if date of birth is valid"""
        try:
            year, month, day = map(int, dob.split("-"))
            if year < 1900 or year > 2023:
                return False
            if month < 1 or month > 12:
                return False
            if day < 1 or day > 31:
                return False
            if month in [4, 6, 9, 11] and day > 30:
                return False
            if month == 2 and day > 29:
                return False
            if (
                month == 2
                and day == 29
                and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
            ):
                return False
            return True
        except ValueError:
            return False
