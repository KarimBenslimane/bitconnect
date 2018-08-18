from database.repositoryinterface import RepositoryInterface
from database.connection import Connection
from .arbitrage import Arbitrage


class ArbitrageRepository(RepositoryInterface):
    tablename = 'arbitrages'

    def __init__(self):
        super().__init__(self.tablename)

    def get(self, id):
        """
        Retrieve an arbitrage from database by id
        :param id:
        :return Arbitrage:
        """
        bot_data = self.connection.query(Connection.TYPE_SELECT, {Arbitrage.ARBITRAGE_BOT: id})
        return self.create_model(bot_data)

    def getList(self, search_criteria):
        """
        Retrieve arbitrages from database by searchCriteria
        :param search_criteria:
        :return Arbitrage[]:
        """
        bot_data = self.connection.query_all(Connection.TYPE_SELECT, search_criteria)
        models = []
        if bot_data:
            for bot in bot_data:
                model = self.create_model(bot)
                models.append(model)
        return models

    def create(self, bot_id, exchange1, exchange2):
        """
        Create an arbitrage in database and retrieve the Bot model
        :param bot_id:
        :param exchange2:
        :param exchange1:
        :return Arbitrage:
        """
        self.connection.query(
            Connection.TYPE_INSERT,
            {
                Arbitrage.ARBITRAGE_BOT: bot_id,
                Arbitrage.ARBITRAGE_E1: exchange1,
                Arbitrage.ARBITRAGE_E2: exchange2
            }
        )
        return self.get(bot_id)

    def create_model(self, data):
        """
        Create an Arbitrage model from database data (bot_id, exchange1, exchange2)
        :param data:
        :return Arbitrage:
        """
        model = Arbitrage()
        model.set_bot(data[0])
        model.set_exchange_one(data[1])
        model.set_exchange_two(data[2])
        return model

    def delete(self, bot_id):
        """
        Delete an Arbitrage from the database
        :param bot_id:
        """
        self.connection.query(
            Connection.TYPE_DELETE,
            {
                Arbitrage.ARBITRAGE_BOT: bot_id
            }
        )
