import ccxt
from pprint import pprint

class CcxtLibrary:
    def get_exchanges(self):
        return ccxt.exchanges

    def print_exchanges(self):
        for exchange in self.get_exchanges():
            print(exchange)

    def load_markets(self, exchange):
        """
        Initiates an exchange by a given name and loads all the markets
        :param exchange:
        :return:
        """
        exchange = self.init_exchange(exchange)
        exchange.loadMarkets()
        return exchange

    def get_pairs(self, exchange):
        exchange = self.load_markets(exchange)
        pairs = []
        for key, value in exchange.markets.items():
            pairs.append(key)
        return pairs

    def init_exchange(self, exchange):
        """
        Creates an exchange class
        :param exchange:
        :return:
        """
        exchange_class = getattr(ccxt, exchange.get_name())
        return exchange_class({
            'apiKey': str(exchange.get_public()),
            'secret': str(exchange.get_private()),
            'timeout': 30000,
            'enableRateLimit': True,
            'uid': str(exchange.get_uid()),
            'password': str(exchange.get_pw())
        })

    def fetch_balance(self, exchange, pair):
        """
        Checks the balance for a given currency on a given exchange
        :param exchange:
        :param pair:
        :return:
        """
        returnbalance = 0
        currency = pair.split("/", 1)[0]
        ccxt_exchange = self.init_exchange(exchange)
        balance = ccxt_exchange.fetch_balance()
        for key, value in balance.items():
            if key == currency:
                returnbalance = value["free"]
        return returnbalance

    def get_exchange_pair(self, exchange, pair):
        """
        Retrieves the current value for a pair in a certain exchange
        :param exchange_name:
        :param pair:
        :return:
        """
        ccxt_exchange = self.load_markets(exchange)
        return ccxt_exchange.markets[pair]

    def get_exchange_trading_fee(self, exchange, pair, fee_type):
        """
        Retrieves the trading fees IN PERCENTAGES for a taker or maker
        A taker fee_type 'takes' liquidity from the exchange and fill someone else's order
        A maker fee_type 'makes' liquidity for the exchange and order
        :param exchange:
        :param pair:
        :param fee_type:
        :return:
        """
        return float(self.get_exchange_pair(exchange, pair)[fee_type])

    def get_market_price(self, exchange, pair, price_type):
        """
        Get market price for buy (bid) or sell (ask) for a certain currency on a certain exchange
        :param exchange:
        :param pair:
        :param price_type:
        :return:
        """
        ccxt_exchange = self.load_markets(exchange)
        orderbook = ccxt_exchange.fetch_order_book(pair)
        bid = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None
        ask = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None
        if price_type == "buy":
            price = bid
        else:
            price = ask
        return float(price)

    def place_order(self, exchange, pair, order_type, amount, price = None):
        """
        Place an order through the ccxt library
        #TODO: might need to test what is best, market or limit orders.
        :param exchange:
        :param pair:
        :param type:
        :param amount:
        :return:
        """
        ccxt_exchange = self.load_markets(exchange)
        if order_type == "buy":
            if price:
                return ccxt_exchange.create_limit_buy_order(pair, amount, price)
            else:
                if exchange.has['createMarketOrder']:
                    return exchange.create_market_buy_order(pair, amount)
                else:
                    raise Exception("This exchange does not accept market orders.")
        else:
            if price:
                return ccxt_exchange.create_limit_sell_order(pair, amount, price)
            else:
                if exchange.has['createMarketOrder']:
                    return exchange.create_market_sell_order(pair, amount)
                else:
                    raise Exception("This exchange does not accept market orders.")

    def cancel_order(self, exchange, id):
        """
        Cancel an existing order on an exchange by id (might need pair too)
        :param exchange:
        :param id:
        :return:
        """
        ccxt_exchange = self.load_markets(exchange)
        ccxt_exchange.cancel_order(id)

    def get_history_data(self, exchange, pair, timedelta):
        """
        Get the history data for a certain exchange for a certain time for a certain pair through the CCXT library
        :param exchange:
        :param pair:
        :param timedelta:
        :return:
        """
        ccxt_exchange = self.load_markets(exchange)
        if ccxt_exchange.has['fetchOHLCV'] == True:
            return ccxt_exchange.fetch_ohlcv(ccxt_exchange.markets[pair]['symbol'], '1h', timedelta)
        else:
            raise Exception("This exchange does not accept OHLCV")
