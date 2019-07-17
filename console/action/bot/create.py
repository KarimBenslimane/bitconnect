from console.action.baseaction import BaseAction
from bot.botmanager import BotManager
from bot.arbitragemanager import ArbitrageManager
from bot.bot import Bot
from exchanges.exchange import Exchange
from user.usermanager import UserManager
from exchanges.exchangemanager import ExchangeManager
from bot.macdmanager import MacdManager


class Create(BaseAction):
    bot_manager = None
    arbi_manager = None
    user_manager = None
    exchange_manager = None
    macd_manager = None

    def __init__(self):
        super().__init__()
        self.action = 'bot_create'
        self.func = self.execute
        self.bot_manager = BotManager()
        self.arbi_manager = ArbitrageManager()
        self.user_manager = UserManager()
        self.exchange_manager = ExchangeManager()
        self.macd_manager = MacdManager()
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
        users = self.user_manager.get_user_by_username(args.username)
        if not users or not users[0].get_id():
            raise Exception("User cannot be found.")
        user_id = users[0].get_id()
        if args.bottype == Bot.TYPE_ARBITRAGE:
            if not args.exchange1 or not args.exchange2:
                raise Exception("Exchange 1 and exchange 2 arguments must be given for ARBITRAGE.")
            if not self.valid_pairs(str(args.pair), [args.exchange1, args.exchange2], user_id):
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
        elif args.bottype == Bot.TYPE_MACD:
            if not args.exchange1:
                raise Exception("Exchange 1 must be given for MACD")
            if not self.valid_pairs(str(args.pair), [args.exchange1], user_id):
                raise Exception("Crypto pair not valid for exchange. (example: BTC/ETH)")
            else:
                self.create_macd(
                    args.pair,
                    args.bottype,
                    args.threshold,
                    args.winlimit,
                    args.losslimit,
                    args.amount,
                    args.exchange1,
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

    def create_macd(self, pair, bottype, threshold, winlimit, losslimit, amount, exchange, user_id):
        """
        Creates a Bot and the MACD
        :param bottype:
        :param threshold:
        :param winlimit:
        :param losslimit:
        :param amount:
        :param exchange:
        :param user_id:
        :return:
        """
        bot = self.create_bot(pair, bottype, threshold, winlimit, losslimit, amount, user_id)
        self.macd_manager.create_macd(bot.get_id(), exchange)

    def valid_pairs(self, pair, exchanges_names, user_id):
        """
        Check for (all) exchanges if the pairs exist
        :param pair:
        :param e_one:
        :param e_two:
        :return bool:
        """
        exchanges = []
        if "all" in exchanges_names:
            exchanges = self.exchange_manager.get_exchanges({Exchange.EXCHANGE_USER: user_id})
        else:
            for exchangename in exchanges_names:
                exchanges = exchanges + self.exchange_manager.get_exchanges({Exchange.EXCHANGE_USER: user_id, Exchange.EXCHANGE_NAME: exchangename})
        for exchange in exchanges:
            if not self.exchange_manager.is_valid_pair(pair, exchange):
                return False
        return True
