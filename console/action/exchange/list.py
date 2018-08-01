from console.action.baseaction import BaseAction
from exchanges.exchangemanager import ExchangeManager
from exchanges.exchange import Exchange


class List(BaseAction):
    exchange_manager = None

    def __init__(self):
        super().__init__()
        self.action = 'exchange_list'
        self.func = self.execute
        self.exchange_manager = ExchangeManager()
        # TODO DEFAULT NONE
        self.flags.append(['-id', '--exchangeid'])
        self.arguments.append({'dest': 'id'})

    def execute(self, args):
        if args.id:
            self.exchange_manager.list_exchanges({Exchange.EXCHANGE_ID: args.id})
        else:
            self.exchange_manager.list_exchanges([])
        return self
