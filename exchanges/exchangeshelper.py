from file import helper
from exchanges import exchangemanager


def list_exchanges(password, filename):
    values = helper.read_user_file(password, filename)
    print("Your saved exchanges are:")
    if len(values) > 0:
        for key, value in values.iteritems():
            print(key)
    print("\n")


def has_exchanges_saved(password, filename):
    values_exchanges = helper.read_user_file(password, filename)
    if len(values_exchanges) > 0:
        return True
    return False


def add_exchange(password, filename):
    print("Choose one of the following exchanges:\n")
    exchangemanager.print_exchanges()
    exchange = str(
        raw_input("Please insert the name of the exchange you want to add, if you want to quit press (q).")).lower()
    if exchange == "q":
        return False
    else:
        public_key = str(raw_input(
            "Please insert the public key address of " + exchange + ". Don't worry your keys will be stored encrypted."))
        private_key = str(raw_input("Please insert the private key address of " + exchange + "."))
        helper.add_exchange_to_user_file(password, filename, public_key, private_key, exchange)
        return True


def remove_exchange(exchange, filename):
    return helper.remove_exchange_from_user_file(exchange, filename)
