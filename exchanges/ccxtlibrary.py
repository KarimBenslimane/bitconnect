import ccxt


class CcxtLibrary:
    def get_exchanges(self):
        return ccxt.exchanges

    def print_exchanges(self):
        for exchange in self.get_exchanges():
            print(exchange)

    def get_pairs(self, exchange):
        markets = getattr(ccxt, exchange)().load_markets()
        pairs = []
        for key, value in markets.items():
            pairs.append(key)
        return pairs

    def init_exchange(self, exchange, api, secret, uid, pw):
        """
        Creates an exchange class
        :param exchange:
        :param api:
        :param secret:
        :return:
        """
        exchange_class = getattr(ccxt, exchange)
        return exchange_class({
            'apiKey': str(api),
            'secret': str(secret),
            'timeout': 30000,
            'enableRateLimit': True,
            'uid': str(uid),
            'password': str(pw)
        })

    def fetch_balance(self, exchange, pair):
        """
        Checks the balance for a given currency on a given exchange
        :param exchange:
        :param api:
        :param secret:
        :param pair:
        :return:
        """
        returnbalance = 0
        currency = pair.split("/", 1)[0]
        exchange = self.init_exchange(exchange.get_name(), exchange.get_public(), exchange.get_private(),
                                      exchange.get_uid(), exchange.get_pw())
        balance = exchange.fetch_balance()
        for key, value in balance.items():
            if key == currency:
                returnbalance = value["free"]
        return returnbalance
