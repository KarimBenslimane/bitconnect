from console.action.baseaction import BaseAction
from bot.botmanager import BotManager


class Delete(BaseAction):
    bot_manager = None

    def __init__(self):
        super().__init__()
        self.action = 'bot_delete'
        self.func = self.execute
        self.bot_manager = BotManager()
        self.flags.append(['-id', '--botid'])
        self.arguments.append({'dest': 'id', 'required': True})

    def execute(self, args):
        if self.ask_confirmation():
            self.bot_manager.delete_bot(args.id)
            print("Successfully deleted bot with id '" + args.id + "'.")
        return self
