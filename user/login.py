from getpass import getpass
from file import helper
import os.path


def get_password():
    password_first = str(
        getpass("Please insert your password. If this is your first time, please remember it for the next one."))
    password_second = str(
        getpass("Please confirm your password.")
    )
    if password_first == password_second:
        return password_first
    else:
        print("[Error] Passwords did not match up. Please try again.\n")
        return get_password()


def check_name(filename):
    if os.path.isfile(helper.get_user_file_name(filename)):
        return True
    else:
        return False
