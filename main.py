import argparse
from bot import bothelper
from exchanges import exchangeshelper
from user.usermanager import UserManager

user_manager = UserManager()

parser = argparse.ArgumentParser(prog='bitconnect')
subparsers = parser.add_subparsers(title='action', dest='action', help='Choose one of the actions')
subparsers.required = True

# create the parser for the "list" command
parser_a = subparsers.add_parser('list', help='List all your exchanges')
parser_a.set_defaults(func=exchangeshelper.list_exchanges)
parser_a.add_argument('username', type=str, help='Your username')
parser_a.add_argument('password', type=str, help='Your password')

# create the parser for the "b" command
parser_b = subparsers.add_parser('add', help='Add a new exchange')
parser_b.set_defaults(func=exchangeshelper.add_exchange)
parser_b.add_argument('username', type=str, help='Your username')
parser_b.add_argument('password', type=str, help='Your password')
parser_b.add_argument('exchange', type=str, help='The exchange you want to add')
parser_b.add_argument('public', type=str, help='The public key of the exchange you want to add')
parser_b.add_argument('private', type=str, help='The private key of the exchange you want to add')

parser_c = subparsers.add_parser('users', help='List all users or one user if -id is included')
parser_c.add_argument('-id', type=str, help='The id of the user you are trying to find')
parser_c.set_defaults(func=user_manager.list_user)

parser_d = subparsers.add_parser('create', help='Create a new user')
parser_d.add_argument('username', type=str, help='The username')
parser_d.add_argument('password', type=str, help='The password')
parser_d.set_defaults(func=user_manager.create_user)

try:
    args = parser.parse_args()
    args.func(args)
except Exception as e:
    print(e)


# if action == "E":
#     # add exchange
#     exchangeshelper.add_exchange(password, filename)
# elif action == "D":
#     # remove exchange
#     exchangeshelper.remove_exchange(filename)
# elif action == "B":
#     # add new bot
#     if exchangeshelper.has_exchanges_saved(password, filename):
#         bothelper.add_new_bot(password, filename)
#     else:
#         print("[Error] Please insert exchange(s) information first.\n")
# elif action == "L":
#     exchangeshelper.list_exchanges(password, filename)
# elif action == "Q":
#     print("Goodbye...\n")
#     dead = True

#
# name_input = str(input("What is your name, trader?\n"))
# password_input = login.get_password()
# filename_lower = name_input.lower()
#
# if login.check_name(filename_lower):
#     # open the file and read the file
#     print("Welcome back " + name_input + ".\n")
# else:
#     # create the file and put in values
#     print("Welcome newcomer " + name_input + ".\n")
#
# dead = False
# actions = Actions()
#
# while not dead:
#     action = str(actions.get_action())
#     actions.process_action(action, filename_lower, password_input)
#
# print("Exiting application...")
