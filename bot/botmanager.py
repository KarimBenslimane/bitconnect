from .botrepository import BotRepository
from .bot import Bot


class BotManager:
    bot_repo = None

    def __init__(self):
        self.bot_repo = BotRepository()

    def get_bot(self, bot_id):
        """
        Retrieve a bot from database by id
        :param bot_id:
        :return Bot:
        """
        return self.bot_repo.get(bot_id)

    def get_bots(self, search_criteria):
        """
        Retrieve bots from database
        :return Bot[]:
        """
        return self.bot_repo.getList(search_criteria=search_criteria)

    def print_bot(self, bot):
        """
        Print Bot info
        :param bot:
        """
        print(bot.get_id())

    def list_bots(self, search_criteria):
        """
        List all bots or one bot if -id option is given
        """
        bots = self.get_bots(search_criteria)
        for bot in bots:
            self.print_bot(bot)

    def create_bot(self, bot_type, threshold, win_limit, loss_limit, amount, status):
        """
        Create a new bot in the database
        :param status:
        :param amount:
        :param loss_limit:
        :param win_limit:
        :param threshold:
        :param bot_type:
        :return Bot:
        """
        if not bot_type or not threshold or not win_limit or not loss_limit or not amount:
            raise Exception("All data must be given")
        else:
            return self.bot_repo.create(bot_type, threshold, win_limit, loss_limit, amount, status)

    def delete_bot(self, bot_id):
        """
        Delete an existing bot from the database
        :param bot_id:
        :return:
        """
        if bot_id:
            self.bot_repo.delete(bot_id)
        else:
            raise Exception("No bot_id found for deleting bot.")

    def get_new_bot(self):
        """
        Check if new bot has entered the database with status OFF
        :return Bot[] | null:
        """
        return self.get_bots({Bot.BOT_STATUS: Bot.STATUS_OFF})
