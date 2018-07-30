import ccxt


class CcxtLibrary:
    def get_exchanges(self):
        return ccxt.exchanges

    def print_exchanges(self):
        for exchange in self.get_exchanges():
            print(exchange)
