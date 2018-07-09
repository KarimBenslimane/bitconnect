from user import login
from console import actions
from exchanges import exchangeshelper
from bot import bothelper

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
    # @todo convert to foreach operation = exchangeshelper.getOperations && operation.getKey = action?
    # @todo ^ Verbeterd leesbaarheid zodra veel operations geimplement worden + dan alleen in exchangeshelper die zooi definieren
    # @todo uitvogelen hoe verschillende exchanges hierin verwerkt kunnen worden.
    # @todo hierin dan ook console/actions verwerken? Beetje gek dat dat nu aparte file waarin het NOG een keer staat
    if action == "E":
        # add exchange
        exchangeshelper.add_exchange_to_user(password_input, filename_lower)
        print("Successfully added a new exchange.\n")
    elif action == "D":
        # remove exchange
        exchange_input = str(raw_input("Please enter the exchange to be deleted.")).lower()
        deleted_outcome = exchangeshelper.remove_exchange_from_user(exchange_input, filename_lower)
        if deleted_outcome:
            print("Successfully removed " + exchange_input + " from your database.\n")
        else:
            print("Could not find " + exchange_input + " in your database.\n")
    elif action == "B":
        # add new bot
        if exchangeshelper.has_exchanges_saved(password_input, filename_lower):
            # continue creating
            # select what kind of bot
            bot = bothelper.create_bot()
            exchanges = exchangeshelper.get_bot_trade_exchanges(password_input, filename_lower)
            bothelper.init_bot(bot, exchanges)
            if bothelper.validate_bot(bot):
                bothelper.start_bot(filename_lower, bot)
            else:
                print("[Error] Bot cannot be validated.\n")
        else:
            print("[Error] Please insert exchange(s) information first.\n")
    elif action == "L":
        print("Your saved exchanges are:")
        exchangeshelper.list_user_exchanges(password_input, filename_lower)
    elif action == "Q":
        print("Goodbye...\n")
        dead = True

print("Exiting application...")
