"""This file contains all constant user prompts used throughout the program"""

DASHES = " --------------- "
WELCOME_TEXT = f"\n{DASHES}Welcome to CUAP Banking LTD{DASHES}\n"
MENU_TEXT = "\nPlease choose an option from the Menu. Enter '0' to exit.\n"
INVALID_INPUT_TEXT = (
    f"\n{DASHES}ERROR: Invalid Option Selected. Please enter a valid option.{DASHES}\n"
)
EXIT = f"\n{DASHES}Thanks for using CUAP Banking LTD services. Exiting{DASHES}\n"
LOGIN_SUCCESS = f"\n{DASHES}LOGIN SUCCESSFUL{DASHES}\n"
LOGIN_FAILED = (
    f"\n{DASHES}ERROR: Unknown email/password. "
    f"Please recheck your email and password{DASHES}\n"
)
REGISTER_FAILED = (
    f"\n{DASHES}ERROR: An account already exists"
    f" with that email. Please login{DASHES}\n"
)
REGISTER_SUCCESS = f"\n{DASHES}REGISTRATION SUCCESSFUL{DASHES}\n"
UNKNOWN_ERROR = (
    f"\n{DASHES}ERROR: An unknown error has occurred. Please contact support.{DASHES}\n"
)
LOGOUT = f"\n{DASHES}SUCCESSFULLY LOGGED OUT{DASHES}\n"
INV_EMAIL = f"\n{DASHES}ERROR:Invalid Email. Please enter again{DASHES}\n"
INV_PASSWORD = f"\n{DASHES}ERROR:Invalid Password. Please enter again{DASHES}\n"
INV_PHONE = f"\n{DASHES}ERROR:Invalid Phone Number. Please enter again{DASHES}\n"
INV_DOB = f"\n{DASHES}ERROR:Invalid Date of Birth. Please enter again{DASHES}\n"
INV_DEPOSIT = f"\n{DASHES}ERROR:Invalid Deposit Amount. Please enter again{DASHES}\n"
INV_GENDER = (
    f"\n{DASHES}ERROR:Invalid Gender. Must be 'Male',"
    f"'Female', or 'Other'. Please enter again{DASHES}\n"
)
INV_ACC_TYPE = (
    f"\n{DASHES}ERROR:Invalid Account Type. Must be 'Current',"
    f"'Saving', or 'Other'.Please enter again{DASHES}\n"
)
WELCOME_LOGIN_TEXT = "\n{}Welcome {} {}{}\n"
MY_DETAILS = f"\n{DASHES}LOADING DETAILS{DASHES}\n"
EDIT_DETAILS = f"\n{DASHES}EDIT DETAILS{DASHES}\n"
UPDATE_SUCCESSFUL = f"\n{DASHES}DATA UPDATE SUCCESSFUL{DASHES}\n"
EDIT_NOT_ALLOWED = (
    f"\n{DASHES}ERROR:You can not edit this detail."
    f" Please contact bank support.{DASHES}\n"
)
CURRENT_BALANCE = "\nAccount Balance: {}"
DEPOSIT_SUCCESSFUL = f"\n{DASHES}AMOUNT DEPOSITED{DASHES}\n"
WITHDRAW_SUCCESSFUL = f"\n{DASHES}AMOUNT WITHDRAWN{DASHES}\n"
INSUFFICIENT_BALANCE = f"\n{DASHES}ERROR:Insufficient Balance.{DASHES}\n"
INV_TRANSFER_AMOUNT = (
    f"\n{DASHES}ERROR:Invalid Transfer Amount. Please enter again{DASHES}\n"
)
INV_ACCOUNT_NUMBER = f"\n{DASHES}ERROR:Invalid Account Number. \
Please enter a valid 6-digit account number.{DASHES}\n"
NO_ACCOUNT_FOUND = f"\n{DASHES}ERROR:Account Not Found.{DASHES}\n"
TRANSFER_COMPLETE = f"\n{DASHES}MONEY TRANSFERRED SUCCESSFULLY{DASHES}\n"
CONFIRM_TRANSFER = f"\n{DASHES}INITIATING TRANSFER{DASHES}\n"
TRANSFER_INCOMPLETE = f"\n{DASHES}ERROR:Transfer Cancelled by user{DASHES}\n"
INVALID_PIN = f"\n{DASHES}ERROR:Invalid PIN. Please enter a 4-digit number.{DASHES}\n"
WRONG_PIN = f"\n{DASHES}ERROR:PIN CODE validation failed. Please try again.{DASHES}\n"
VALIDATION_SUCCESS = f"\n{DASHES}PIN VALIDATED{DASHES}\n"
MANAGE_CARDS = f"\n{DASHES}MANAGE YOUR ACCOUNT CARDS{DASHES}\n"
NEW_CARD_LIMIT = f"\n{DASHES}ERROR:Your account has reached the maximum\
 limit for new cards. Please contact support.{DASHES}\n"
CARD_CREATED = f"\n{DASHES}NEW CARD CREATION SUCCESSFUL{DASHES}\n"
INVALID_BILL_ID = f"\n{DASHES}ERROR:Invalid Bill ID.{DASHES}\n"
BILL_PAID = f"\n{DASHES}BILL PAID{DASHES}\n"
IN_CARD_DETAILS = (
    f"\n{DASHES}ERROR:Bill Payment Failed. Please check your card information{DASHES}\n"
)
