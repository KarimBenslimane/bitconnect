from bot.macdrepository import MacdRepository


class MacdManager():
    macd_repo = None

    def __init__(self):
        self.macd_repo = MacdRepository()

    def get_macd(self, bot_id):
        """
        Retrieve an macd from database by id
        :param bot_id:
        :return Macd:
        """
        return self.macd_repo.get(bot_id)

    def get_macds(self, search_criteria):
        """
        Retrieve macds from database
        :return Macd[]:
        """
        return self.macd_repo.getList(search_criteria=search_criteria)

    def print_macd(self, macd):
        """
        Print Macd info
        :param macd:
        """
        print(macd.get_id())
        print(macd.get_exchange())

    def create_macd(self, bot_id, exchange):
        """
        Create an macd in the database
        :param bot_id:
        :param exchange:
        :return Arbitrage:
        """
        if not bot_id or not exchange:
            raise Exception("All data must be given")
        else:
            return self.macd_repo.create(bot_id, exchange)

    def delete_macd(self, bot_id):
        """
        Delete an existing macd from the database
        :param bot_id:
        :return:
        """
        if bot_id:
            self.macd_repo.delete(bot_id)
        else:
            raise Exception("No bot_id found for deleting macd.")

    def get_bot_dict(self, bot):
        """
        Get all the info of an macd bot
        :param bot:
        :return {}:
        """
        arbitrage = self.get_macd(bot.get_id())
        if not arbitrage:
            raise Exception("No macd bot found")
        else:
            bot_dict = {
                "id": str(bot.get_id()),
                "threshold": str(bot.get_threshold()),
                "win_limit": str(bot.get_win_limit()),
                "loss_limit": str(bot.get_loss_limit()),
                "type": str(bot.get_type()),
                "amount": str(bot.get_amount()),
                "created_at": str(bot.get_created_at()),
                "status": str(bot.get_status()),
                "user_id": str(bot.get_userid()),
                "exchange": str(arbitrage.get_exchange()),
                "pair": str(bot.get_pair())
            }
            return bot_dict
