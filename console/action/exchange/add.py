from console.action.baseaction import BaseAction
from exchanges import exchangeshelper


# Needs no init function due to only needing base arguments
class Add(BaseAction):
    def __init__(self):
        super().__init__()
        self.action = 'exchange_add'
        self.func = self.execute
        # TODO add init_args function that adds exchange option

    def execute(self, args):
        #TODO refactor exchangehelper to manager and repo with MySQL
        #exchangeshelper.add_exchange(args.password, args.filename)
        return self
