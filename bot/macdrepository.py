from database.repositoryinterface import RepositoryInterface
from database.connection import Connection
from .macd import Macd


class MacdRepository(RepositoryInterface):
    tablename = 'macd'

    def __init__(self):
        super().__init__(self.tablename)

    def get(self, id):
        """
        Retrieve an macd from database by id
        :param id:
        :return Macd:
        """
        bot_data = self.connection.query(Connection.TYPE_SELECT, [Macd.MACD_BOT], [id])
        return self.create_model(bot_data)

    def getList(self, search_criteria):
        """
        Retrieve macds from database by searchCriteria
        :param search_criteria:
        :return Macd[]:
        """
        keys = []
        values = []
        for key, value in search_criteria.items():
            keys.append(key)
            values.append(value)
        bot_data = self.connection.query_all(Connection.TYPE_SELECT, keys, values)
        models = []
        if bot_data:
            for bot in bot_data:
                model = self.create_model(bot)
                models.append(model)
        return models

    def create(self, bot_id, exchange):
        """
        Create an macd in database and retrieve the Bot model
        :param bot_id:
        :param exchange:
        :return Arbitrage:
        """
        self.connection.query(
            Connection.TYPE_INSERT,
            [Macd.MACD_BOT, Macd.MACD_EXCHANGE],
            [bot_id, exchange]
        )
        return self.get(bot_id)

    def create_model(self, data):
        """
        Create an Macd model from database data (bot_id, exchange)
        :param data:
        :return Macd:
        """
        model = Macd()
        model.set_bot(data[0])
        model.set_exchange(data[1])
        return model

    def delete(self, bot_id):
        """
        Delete an Macd from the database
        :param bot_id:
        """
        self.connection.query(
            Connection.TYPE_DELETE,
            [Macd.MACD_BOT],
            [bot_id]
        )
