from console.action.baseaction import BaseAction
from bot.botmanager import BotManager
from bot.arbitragemanager import ArbitrageManager
from bot.bot import Bot


class Create(BaseAction):
    bot_manager = None
    arbi_manager = None

    def __init__(self):
        super().__init__()
        self.action = 'bot_create'
        self.func = self.execute
        self.bot_manager = BotManager()
        self.arbi_manager = ArbitrageManager()
        self.flags.append(['-t', '--type'])
        self.flags.append(['-th', '--threshold'])
        self.flags.append(['-w', '--winlimit'])
        self.flags.append(['-l', '--losslimit'])
        self.flags.append(['-a', '--amount'])
        self.flags.append(['-e1', '--exchange1'])
        self.flags.append(['-e2', '--exchange2'])

        self.arguments.append({'dest': 'bottype', 'required': True})
        self.arguments.append({'dest': 'threshold', 'required': True})
        self.arguments.append({'dest': 'winlimit', 'required': True})
        self.arguments.append({'dest': 'losslimit', 'required': True})
        self.arguments.append({'dest': 'amount', 'required': True})
        self.arguments.append({'dest': 'exchange1'})
        self.arguments.append({'dest': 'exchange2'})

    def execute(self, args):
        if args.bottype == Bot.TYPE_ARBITRAGE:
            if not args.exchange1 or not args.exchange2:
                raise Exception("Exchange 1 and exchange 2 arguments must be given for ARBITRAGE.")
            else:
                self.create_arbitrage(
                    args.bottype,
                    args.threshold,
                    args.winlimit,
                    args.losslimit,
                    args.amount,
                    args.exchange1,
                    args.exchange2
                )
        print("Successfully created the bot")

    def create_bot(self, bottype, threshold, winlimit, losslimit, amount):
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
            bottype,
            threshold,
            winlimit,
            losslimit,
            amount,
            Bot.STATUS_OFF
        )

    def create_arbitrage(self, bottype, threshold, winlimit, losslimit, amount, exchange1, exchange2):
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
        bot = self.create_bot(bottype, threshold, winlimit, losslimit, amount)
        self.arbi_manager.create_arbitrage(bot.get_id(), exchange1, exchange2)
