from console.action.baseaction import BaseAction
from exchanges import exchangeshelper


# Needs no init function due to only needing base arguments
class Add(BaseAction):
    def __init__(self):
        super().__init__()
        self.action = 'exchange_add'
        self.func = self.execute

    def execute(self, args):
        exchangeshelper.add_exchange(args.password, args.filename)
        return self
