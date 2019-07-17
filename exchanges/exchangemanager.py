from .exchangerepository import ExchangeRepository
from .exchange import Exchange
from exchanges.ccxtlibrary import CcxtLibrary

class ExchangeManager:
    exch_repo = None
    ccxt = None

    def __init__(self):
        self.exch_repo = ExchangeRepository()
        self.ccxt = CcxtLibrary()

    def get_exchange(self, id):
        """
        Retrieve an exchange from database by id
        :param id:
        :return Exchange:
        """
        return self.exch_repo.get(id)

    def get_exchanges(self, search_criteria):
        """
        Retrieve exchanges from database
        :return Exchange[]:
        """
        return self.exch_repo.getList(search_criteria=search_criteria)

    def print_exchange(self, exchange):
        """
        Print Exchange info
        :param exchange:
        """
        print("Id: " + exchange.get_id())
        print("Name: " + exchange.get_name())
        print("Public key: " + exchange.get_public())
        print("User id: " + exchange.get_user_id())
        print("\n")

    def list_exchanges(self, search_criteria=None):
        """
        List all exchanges or one exchange if -id option is given
        """
        if search_criteria is None:
            search_criteria = {}
        exchanges = self.get_exchanges(search_criteria)
        for exchange in exchanges:
            self.print_exchange(exchange)

    def create_exchange(self, exchangename, public_key, private_key, user_id, uid = None, pw = None):
        """
        Create a new exchange in the database
        :param exchangename:
        :param public_key:
        :param private_key:
        :param user_id:
        :return Exchange:
        """
        if not exchangename or not public_key or not private_key:
            raise Exception("Exchangename, public key and private key must be given")
        else:
            return self.exch_repo.create(exchangename, public_key, private_key, user_id, uid, pw)

    def delete_exchange(self, exchange_id):
        """
        Delete an existing exchange from the database
        :param exchange_id:
        :return:
        """
        if exchange_id:
            self.exch_repo.delete(exchange_id=exchange_id)
        else:
            raise Exception("No exchange_id found for deleting exchange.")

    def is_valid_pair(self, pair, exchange):
        """
        Checks if an input pair is a valid one for given exchange
        :param exchange:
        :param pair:
        :return bool:
        """
        pairs = self.ccxt.get_pairs(exchange)
        print(pairs)
        return pair in pairs

    def fetch_balance(self, exchange, pair):
        """
        Fetches balance for a pair on an exchange through CCXT
        :param exchange:
        :param pair:
        :return:
        """
        return self.ccxt.fetch_balance(exchange, pair)

    def get_exchange_trading_fee(self, exchange, pair, type):
        """
        Retrieves the trading fee for a certain pair on a certain exchange
        :param exchange:
        :param pair:
        :param type:
        :return:
        """
        return self.ccxt.get_exchange_trading_fee(exchange, pair, type)

    def get_market_price(self, exchange, pair, type):
        """
        Retrieves the market price for a certain pair on a certain exchange for a certain type(maker or taker)
        :param exchange:
        :param pair:
        :param type:
        :return:
        """
        return self.ccxt.get_market_price(exchange, pair, type)

    def place_order(self, exchange, pair, type, amount, price = None):
        """
        Place an order through the ccxt library for a certain exchange,
        for a certain pair (BTC/USD), type as buy/sell, and amount in currency (if BTC/USD will be BTC)
        :param price:
        :param exchange:
        :param pair:
        :param type:
        :param amount:
        :return:
        """
        return self.ccxt.place_order(exchange, pair, type, amount, price)

    def cancel_order(self, exchange, order_id):
        """
        Cancel the order through ccxt library for a certain exchange
        :param exchange:
        :param order_id:
        :return:
        """
        return self.ccxt.cancel_order(exchange, order_id)

    def get_history_data(self, exchange, pair, timedelta):
        """
        Get the the data for a certain exchange for a given pair for the last 700 hours
        :param exchange:
        :param pair:
        :param timedelta:
        :return array:
        """
        return self.ccxt.get_history_data(exchange, pair, timedelta)
