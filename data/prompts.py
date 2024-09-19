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
