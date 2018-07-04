from user import login
from console import actions
from exchanges import exchangeshelper

name_input = str(raw_input("What is your name, trader?\n"))
password_input = login.get_password()
filename_lower = name_input.lower()

if login.check_name(filename_lower):
    # open the file and read the file
    print("Welcome back " + name_input + ".\n")
else:
    # create the file and put in values
    print("Welcome newcomer " + name_input + ".\n")

dead = False
while not dead:
    action = str(actions.get_action())
    if action == "E":
        # add exchange
        if exchangeshelper.add_exchange(password_input, filename_lower):
            print("Successfully added a new exchange.\n")
    elif action == "D":
        # remove exchange
        exchange_input = str(raw_input("Please enter the exchange to be deleted.")).lower()
        deleted_outcome = exchangeshelper.remove_exchange(exchange_input, filename_lower)
        if deleted_outcome:
            print("Successfully removed " + exchange_input + " from your database.\n")
        else:
            print("Could not find " + exchange_input + " in your database.\n")
    elif action == "B":
        # add new bot
        if exchangeshelper.has_exchanges_saved(password_input, filename_lower):
            # continue creating
            print("Yo")
        else:
            print("Please insert exchange(s) information first.\n")
    elif action == "L":
        exchangeshelper.list_exchanges(password_input, filename_lower)
    elif action == "Q":
        print("Goodbye...\n")
        dead = True

print("Exiting application...")
