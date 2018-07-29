from console.action.baseaction import BaseAction
from exchanges import exchangeshelper


# Needs no init function due to only needing base arguments
class List(BaseAction):
    def __init__(self):
        super().__init__()
        self.action = 'exchange_list'
        self.func = self.execute

    def execute(self, args):
        exchangeshelper.list_exchanges(args.password, args.filename)
        return self
