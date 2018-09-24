from .arbitragerepository import ArbitrageRepository
from .arbitrage import Arbitrage

class ArbitrageManager:
    arbi_repo = None

    def __init__(self):
        self.arbi_repo = ArbitrageRepository()

    def get_arbitrage(self, bot_id):
        """
        Retrieve an arbitrage from database by id
        :param bot_id:
        :return Arbitrage:
        """
        return self.arbi_repo.get(bot_id)

    def get_arbitrages(self, search_criteria):
        """
        Retrieve arbitrages from database
        :return Arbitrage[]:
        """
        return self.arbi_repo.getList(search_criteria=search_criteria)

    def print_arbitrage(self, arbitrage):
        """
        Print Arbitrage info
        :param Arbitrage:
        """
        print(arbitrage.get_id())
        print(arbitrage.get_exchange_one())
        print(arbitrage.get_exchange_two())

    def create_arbitrage(self, bot_id, exchange1, exchange2):
        """
        Create an arbitrage in the database
        :param bot_id:
        :param exchange1:
        :param exchange2:
        :return Arbitrage:
        """
        if not bot_id or not exchange1 or not exchange2:
            raise Exception("All data must be given")
        else:
            return self.arbi_repo.create(bot_id, exchange1, exchange2)

    def delete_arbitrage(self, bot_id):
        """
        Delete an existing arbitrage from the database
        :param bot_id:
        :return:
        """
        if bot_id:
            self.arbi_repo.delete(bot_id)
        else:
            raise Exception("No bot_id found for deleting arbitrage.")

    def get_bot_dict(self, bot):
        """
        Get all the info of an arbitrage bot
        :param bot:
        :return {}:
        """
        arbitrage = self.get_arbitrage(bot.get_id())
        if not arbitrage:
            raise Exception("No arbitrage bot found")
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
                "exchange_one": str(arbitrage.get_exchange_one()),
                "exchange_two": str(arbitrage.get_exchange_two())
            }
            return bot_dict
