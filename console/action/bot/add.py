from console.action.baseaction import BaseAction

# Needs no init function due to only needing base arguments
class Add(BaseAction):
    def __init__(self):
        super().__init__()
        self.action = 'add_bot'
        self.func = self.execute

    def execute(self, args):
        #TODO refactor bothelper to manager and repo with MySQL
        # add new bot
        #if exchangeshelper.has_exchanges_saved(args.password, args.filename):
        #    bothelper.add_new_bot()
        #else:
        #    print("[Error] Please insert exchange(s) information first.\n")
        return self
