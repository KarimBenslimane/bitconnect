from console.action.baseaction import BaseAction
from bot.botmanager import BotManager
from bot.arbitragemanager import ArbitrageManager
from bot.bot import Bot
from user.usermanager import UserManager


class Create(BaseAction):
    bot_manager = None
    arbi_manager = None
    user_manager = None

    def __init__(self):
        super().__init__()
        self.action = 'bot_create'
        self.func = self.execute
        self.bot_manager = BotManager()
        self.arbi_manager = ArbitrageManager()
        self.user_manager = UserManager()
        self.flags.append(['-pa', '--pair'])
        self.flags.append(['-t', '--type'])
        self.flags.append(['-th', '--threshold'])
        self.flags.append(['-w', '--winlimit'])
        self.flags.append(['-l', '--losslimit'])
        self.flags.append(['-a', '--amount'])
        self.flags.append(['-e1', '--exchange1'])
        self.flags.append(['-e2', '--exchange2'])

        self.arguments.append({'dest': 'pair', 'required': True})
        self.arguments.append({'dest': 'bottype', 'required': True})
        self.arguments.append({'dest': 'threshold', 'required': True})
        self.arguments.append({'dest': 'winlimit', 'required': True})
        self.arguments.append({'dest': 'losslimit', 'required': True})
        self.arguments.append({'dest': 'amount', 'required': True})
        self.arguments.append({'dest': 'exchange1'}) #arbitrage
        self.arguments.append({'dest': 'exchange2'}) #arbitrage

    def execute(self, args):
        user_id = self.user_manager.get_user_by_username(args.username)
        if args.bottype == Bot.TYPE_ARBITRAGE:
            if not args.exchange1 or not args.exchange2:
                raise Exception("Exchange 1 and exchange 2 arguments must be given for ARBITRAGE.")
            if not self.valid_pairs(str(args.pair), args.exchange1, args.exchange2):
                raise Exception("Crypto pair not valid. (example: BTC/ETH)")
            else:
                self.create_arbitrage(
                    args.pair,
                    args.bottype,
                    args.threshold,
                    args.winlimit,
                    args.losslimit,
                    args.amount,
                    args.exchange1,
                    args.exchange2,
                    user_id
                )
        print("Successfully created the bot")

    def create_bot(self, pair, bottype, threshold, winlimit, losslimit, amount, user_id):
        """
        Creates a Bot through BotManager
        :param bottype:
        :param threshold:
        :param winlimit:
        :param losslimit:
        :param amount:
        :return Bot:
        """
        return self.bot_manager.create_bot(
            pair,
            bottype,
            threshold,
            winlimit,
            losslimit,
            amount,
            Bot.STATUS_OFF,
            user_id
        )

    def create_arbitrage(self, pair, bottype, threshold, winlimit, losslimit, amount, exchange1, exchange2, user_id):
        """
        Creates a Bot and the Arbitrage
        :param bottype:
        :param threshold:
        :param winlimit:
        :param losslimit:
        :param amount:
        :param exchange1:
        :param exchange2:
        :return:
        """
        bot = self.create_bot(pair, bottype, threshold, winlimit, losslimit, amount, user_id)
        self.arbi_manager.create_arbitrage(bot.get_id(), exchange1, exchange2)

    def valid_pairs(self, pair, e_one, e_two):
        """
        Check for both exchanges if the pair exists, otherwise we cannot make the bot
        :param pair:
        :param e_one:
        :param e_two:
        :return bool:
        """
        return self.bot_manager.is_valid_pair(pair, e_one) and self.bot_manager.is_valid_pair(pair, e_two)