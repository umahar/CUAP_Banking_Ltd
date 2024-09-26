"""this file will call the relevant input validation function and return prompts"""

from utils.input_check import CheckInput
from data import prompts


class UserInputHandler:
    """this file will call the relevant input validation function and return prompts"""

    @staticmethod
    def get_valid_email(prompt):
        """this function will prompt the user to keep entering email
        and validating it until its correct"""
        email = input(prompt)
        while not CheckInput.is_valid_email(email):
            print(prompts.INV_EMAIL)
            email = input(prompt)
        return email

    @staticmethod
    def get_valid_password(prompt):
        """this function will prompt the user to keep entering password
        and validating it until its correct"""
        password = input(prompt)
        while not CheckInput.is_valid_password(password):
            print(prompts.INV_PASSWORD)
            password = input(prompt)
        return password

    @staticmethod
    def get_valid_phone_no(prompt):
        """this function will prompt the user to keep entering phone no
        and validating it until its correct"""
        phone_no = input(prompt)
        while not CheckInput.is_valid_phone_no(phone_no):
            print(prompts.INV_PHONE)
            phone_no = input(prompt)
        return phone_no

    @staticmethod
    def get_valid_first_name(prompt):
        """this function will prompt the user to keep entering name
        and validating it until its correct"""
        name = input(prompt)
        while not CheckInput.is_valid_name(name):
            print(
                f"{prompts.DASHES}ERROR: Invalid Name. Please enter again{prompts.DASHES}"
            )
            name = input(prompt)
        return name

    @staticmethod
    def get_valid_last_name(prompt):
        """this function will prompt the user to keep entering name
        and validating it until its correct"""
        name = input(prompt)
        while not CheckInput.is_valid_name(name):
            print(
                f"{prompts.DASHES}ERROR: Invalid Name. Please enter again{prompts.DASHES}"
            )
            name = input(prompt)
        return name

    @staticmethod
    def get_valid_date_of_birth(prompt):
        """this function will prompt the user to keep entering date of birth
        and validating it until its correct"""
        dob = input(prompt)
        while not CheckInput.is_valid_dob(dob):
            print(prompts.INV_DOB)
            dob = input(prompt)
        return dob

    @staticmethod
    def get_valid_initial_deposit(prompt):
        """this function will prompt the user to keep entering deposit
        and validating it until its correct"""
        deposit = input(prompt)
        while not CheckInput.is_valid_deposit(deposit):
            print(prompts.INV_DEPOSIT)
            deposit = input(prompt)
        return deposit

    @staticmethod
    def get_valid_transfer_amount(prompt, current_balance):
        """gets valid amount to transfer to someone"""
        while True:
            amount = input(prompt)
            if not CheckInput.is_valid_deposit(amount):
                print(prompts.INV_TRANSFER_AMOUNT)
                continue
            if not CheckInput.is_valid_transfer_amount(float(amount), current_balance):
                print(prompts.INSUFFICIENT_BALANCE)
                continue
            return amount

    @staticmethod
    def get_valid_gender(prompt):
        """this function will prompt the user to keep entering gender
        and validating it until its correct"""
        gender = input(prompt)
        while gender not in ["Male", "Female", "Other"]:
            print(prompts.INV_GENDER)
            gender = input(prompt)
        return gender

    @staticmethod
    def get_valid_account_type(prompt):
        """this function will prompt the user to keep entering account type
        and validating it until its correct"""
        acc_type = input(prompt)
        while acc_type not in ["Current", "Saving", "Other"]:
            print(prompts.INV_ACC_TYPE)
            acc_type = input(prompt)
        return acc_type

    @staticmethod
    def get_valid_date_created(prompt):
        """this function will prompt the user to keep entering date
        and validating it until its correct"""

    @staticmethod
    def get_valid_country(prompt):
        """this function will prompt the user to keep entering name
        and validating it until its correct"""
        name = input(prompt)
        while not CheckInput.is_valid_name(name):
            print(
                f"{prompts.DASHES}ERROR: Invalid Country Name. Please enter again{prompts.DASHES}"
            )
            name = input(prompt)
        return name

    @staticmethod
    def get_valid_city(prompt):
        """this function will prompt the user to keep entering name
        and validating it until its correct"""
        name = input(prompt)
        while not CheckInput.is_valid_name(name):
            print(
                f"{prompts.DASHES}ERROR: Invalid City Name. Please enter again{prompts.DASHES}"
            )
            name = input(prompt)
        return name

    @staticmethod
    def get_valid_account_number(prompt):
        pass
