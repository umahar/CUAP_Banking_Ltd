"""This file contains all constant user prompts used throughout the program"""

DASHES = " --------------- "
WELCOME_TEXT = f"\n{DASHES}Welcome to CUAP Banking LTD{DASHES}\n"
MENU_TEXT = "\nPlease choose an option from the Menu. Enter '0' to exit the app.\n"
INVALID_INPUT_TEXT = (
    f"\n{DASHES}ERROR: Invalid Option Selected. Please enter a valid option.{DASHES}\n"
)

EXIT = f"\n{DASHES}Thanks for using CUAP Banking LTD services. Exiting{DASHES}\n"
LOGIN_SUCCESS = f"\n{DASHES}LOGIN SUCCESSFUL{DASHES}"
LOGIN_FAILED = f"\n{DASHES}ERROR: Unknown email/password. Please recheck your email and password{DASHES}"
REGISTER_FAILED = (
    f"\n{DASHES}ERROR: An account already exists with that email. Please login{DASHES}"
)
REGISTER_SUCCESS = f"\n{DASHES}REGISTRATION SUCCESSFUL{DASHES}"
UNKNOWN_ERROR = (
    f"\n{DASHES}ERROR: An unknown error has occurred. Please contact support.{DASHES}"
)

INV_EMAIL = f"\n{DASHES}ERROR:Invalid Email. Please enter again{DASHES}"
INV_PASSWORD = f"\n{DASHES}ERROR:Invalid Password. Please enter again{DASHES}"
INV_PHONE = f"\n{DASHES}ERROR:Invalid Phone Number. Please enter again{DASHES}"
INV_DOB = f"\n{DASHES}ERROR:Invalid Date of Birth. Please enter again{DASHES}"
INV_DEPOSIT = f"\n{DASHES}ERROR:Invalid Deposit Amount. Please enter again{DASHES}"
INV_GENDER = f"\n{DASHES}ERROR:Invalid Gender. Must be 'Male', 'Female', or 'Other'. Please enter again{DASHES}"
INV_ACC_TYPE = f"\n{DASHES}ERROR:Invalid Account Type. Must be 'Current', 'Saving', or 'Other'.Please enter again{DASHES}"
