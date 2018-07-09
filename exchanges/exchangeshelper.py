from file import helper
from exchanges import exchangemanager

# @todo rename naar Helper voor Exchanges/Helper en omzetten naar een class?
# @todo Misschien beter niet voor de proof of concept? (Die was alleen technieken uitproberen, nog niet extra functionaliteit)
# @todo ^ hiervoor losse actions als classes in console/actions? Die dan deze helper/manager aanroepen?

def list_user_exchanges(password, filename):
    values = helper.read_user_file(password, filename)
    if len(values) > 0:
        for key, value in values.iteritems():
            print(key)
    print("\n")


def has_exchanges_saved(password, filename):
    values_exchanges = helper.read_user_file(password, filename)
    if len(values_exchanges) > 0:
        return True
    return False


def add_exchange_to_user(password, filename):
    print("Choose one of the following exchanges:\n")
    exchangemanager.print_exchanges()
    exchange = str(
        raw_input("Please insert the name of the exchange you want to add.")).lower()
    if is_exchange_valid(exchange):
        public_key = str(raw_input(
            "Please insert the public key address of " + exchange + ". Don't worry your keys will be stored encrypted."))
        private_key = str(raw_input("Please insert the private key address of " + exchange + "."))
        helper.add_exchange_to_user_file(password, filename, public_key, private_key, exchange)
    else:
        print("[Error] " + exchange + " Is not a valid exchange.")


def remove_exchange_from_user(exchange, filename):
    return helper.remove_exchange_from_user_file(exchange, filename)


def get_bot_trade_exchanges(password, filename):
    exchanges = []
    print("Choose one (or more) of the following exchanges:\n")
    list_user_exchanges(password, filename)
    exchange_input = ''
    while exchange_input != "q":
        exchange_input = str(
            raw_input("Please insert the name of the exchange you want to add, if you want to quit press (q).")).lower()
        if exchange_input == "q":
            continue
        if is_user_exchange(exchange_input, password, filename) and exchange_input not in exchanges:
            exchanges.append(exchange_input)
        else:
            print("[Error] " + exchange_input + " is not a valid exchange or has already been added.")
    return exchanges


def is_exchange_valid(exchange):
    return exchange in exchangemanager.get_exchanges()


def is_user_exchange(exchange, password, filename):
    return exchange in helper.read_user_file(password, filename)
