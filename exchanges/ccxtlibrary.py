import ccxt


class CcxtLibrary:
    def get_exchanges(self):
        return ccxt.exchanges

    def print_exchanges(self):
        for exchange in self.get_exchanges():
            print(exchange)

    def get_pairs(self, market):
        markets = getattr(ccxt, market)().load_markets()
        pairs = []
        for key, value in markets.items():
            pairs.append(key)
        return pairs