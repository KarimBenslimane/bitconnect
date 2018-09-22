from database.repositoryinterface import RepositoryInterface
from database.connection import Connection
from .bot import Bot


class BotRepository(RepositoryInterface):
    tablename = 'bots'

    def __init__(self):
        super().__init__(self.tablename)

    def get(self, id):
        """
        Retrieve a bot from database by id
        :param id:
        :return Bot:
        """
        bot_data = self.connection.query(Connection.TYPE_SELECT, {Bot.BOT_ID: id})
        return self.create_model(bot_data)

    def getList(self, search_criteria):
        """
        Retrieve bots from database by searchCriteria
        :param search_criteria:
        :return Bot[]:
        """
        bot_data = self.connection.query_all(Connection.TYPE_SELECT, search_criteria)
        models = []
        if bot_data:
            for bot in bot_data:
                model = self.create_model(bot)
                models.append(model)
        return models

    def create(self, bot_type, threshold, win_limit, loss_limit, amount, status):
        """
        Create a bot in database and retrieve the Bot model
        :param status:
        :param amount:
        :param loss_limit:
        :param win_limit:
        :param threshold:
        :param bot_type:
        :return Bot:
        """
        self.connection.query(
            Connection.TYPE_INSERT,
            {
                Bot.BOT_TYPE: bot_type,
                Bot.BOT_THRESHOLD: threshold,
                Bot.BOT_WIN_LIMIT: win_limit,
                Bot.BOT_LOSS_LIMIT: loss_limit,
                Bot.BOT_AMOUNT: amount,
                Bot.BOT_STATUS: status
            }
        )
        # TODO: maybe replace last_insert_id with something specific
        # TODO: when many people will use the system to avoid wrong ids return
        return self.get(self.connection.query_last_insert_id())

    def create_model(self, data):
        """
        Create an Bot model from database data (bot_id, bot_type, threshold, win_limt, loss_limit, amount)
        :param data:
        :return Bot:
        """
        model = Bot()
        model.set_id(data[0])
        model.set_type(data[1])
        model.set_threshold(data[2])
        model.set_win_limit(data[3])
        model.set_loss_limit(data[4])
        model.set_amount(data[5])
        model.set_created_at(data[6])
        model.set_status(data[7])
        return model

    def delete(self, bot_id):
        """
        Delete a bot from the database
        :param bot_id:
        """
        self.connection.query(
            Connection.TYPE_DELETE,
            {
                Bot.BOT_ID: bot_id
            }
        )
