import warnings

warnings.filterwarnings("ignore")
import ccxt


def get_exchanges():
    return ccxt.exchanges


def print_exchanges():
    for exchange in get_exchanges():
        print(exchange)
