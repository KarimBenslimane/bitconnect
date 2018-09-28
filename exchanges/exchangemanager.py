from .exchangerepository import ExchangeRepository
from .exchange import Exchange

class ExchangeManager:
    exch_repo = None

    def __init__(self):
        self.exch_repo = ExchangeRepository()

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

    def list_exchanges(self, search_criteria):
        """
        List all exchanges or one exchange if -id option is given
        """
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