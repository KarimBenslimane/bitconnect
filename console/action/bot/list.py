from console.action.baseaction import BaseAction
from bot.botmanager import BotManager
from bot.bot import Bot


class List(BaseAction):
    bot_manager = None

    def __init__(self):
        super().__init__()
        self.action = 'bot_list'
        self.func = self.execute
        self.bot_manager = BotManager()
        # TODO DEFAULT NONE
        self.flags.append(['-id', '--botid'])
        self.arguments.append({'dest': 'id'})

    def execute(self, args):
        if args.id:
            self.bot_manager.list_bots({Bot.BOT_ID: args.id})
        else:
            self.bot_manager.list_bots([])
        return self
