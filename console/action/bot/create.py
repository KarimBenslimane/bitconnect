from console.action.baseaction import BaseAction
from bot.botmanager import BotManager
from bot.bot import Bot


class Create(BaseAction):
    bot_manager = None

    def __init__(self):
        super().__init__()
        self.action = 'bot_create'
        self.func = self.execute
        self.bot_manager = BotManager()
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
                raise Exception("Exchange 1 and exchange 2 arguments must be given.")
            else:
                self.bot_manager.create_bot(args.bottype, args.threshold, args.winlimit, args.losslimit, args.amount)
                # TODO create arbitrage
        print("Successfully created the bot")
