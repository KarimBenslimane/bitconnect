from console.action.baseaction import BaseAction
from exchanges import exchangeshelper
from bot import bothelper


# Needs no init function due to only needing base arguments
class Add(BaseAction):
    def __init__(self):
        super().__init__()
        self.action = 'add_bot'
        self.func = self.execute

    def execute(self, args):
        # add new bot
        if exchangeshelper.has_exchanges_saved(args.password, args.filename):
            bothelper.add_new_bot()
        else:
            print("[Error] Please insert exchange(s) information first.\n")
        return self
