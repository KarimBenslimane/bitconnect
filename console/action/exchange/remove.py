from console.action.baseaction import BaseAction
from exchanges import exchangeshelper


# Needs no init function due to only needing base arguments
class Remove(BaseAction):
    def __init__(self):
        super().__init__()
        self.action = 'exchange_remove'
        self.func = self.execute

    def execute(self, args):
        exchangeshelper.remove_exchange(args.filename)
        return self
