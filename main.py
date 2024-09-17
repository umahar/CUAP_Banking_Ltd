"""The program starts here. This main function will keep it going."""

from data import prompts, menu_options as mo
from core import register as rg, login as lg, balance_check as bc


def display_menu():
    """function that displays menu until the user enters 0. Handles invalid input"""
    print(prompts.WELCOME_TEXT)
    while True:
        print(prompts.MENU_TEXT)
        for index, item in enumerate(mo.main_menu_options):
            print(f"{index + 1}. {item}")
        opt = input("\nOption #: ")
        if not opt.strip().isdigit():
            print(prompts.INVALID_INPUT_TEXT)
            continue
        opt = int(opt)
        if opt == 0:
            print(prompts.EXIT)
            break
        if 0 < opt <= len(mo.main_menu_options):
            print("\nSelection --> ", mo.main_menu_options[opt - 1], "\n")
            handle_input(opt)
        else:
            print(prompts.INVALID_INPUT_TEXT)


def handle_input(opt):
    """This function will take opt which is the option selected
    by user and handle the function required

    Args:
        opt (int): will be an option within main menu
    """
    if opt == 1:
        lg.login()
    elif opt == 2:
        rg.register()
    elif opt == 3:
        bc.balance_check()


display_menu()
