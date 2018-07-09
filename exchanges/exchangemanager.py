import warnings

warnings.filterwarnings("ignore")
import ccxt


# @todo rename naar Manager voor Exchanges/Manager en omzetten naar een class?

def get_exchanges():
    return ccxt.exchanges


def print_exchanges():
    for exchange in get_exchanges():
        print(exchange)
