from console.action.baseaction import BaseAction
from exchanges.exchangemanager import ExchangeManager


class Delete(BaseAction):
    exchange_manager = None

    def __init__(self):
        super().__init__()
        self.action = 'exchange_delete'
        self.func = self.execute
        self.exchange_manager = ExchangeManager()
        self.flags.append(['-id', '--exchangeid'])
        self.arguments.append({'dest': 'id', 'required': True})

    def execute(self, args):
        if self.ask_confirmation():
            self.exchange_manager.delete_exchange(args.id)
            print("Successfully deleted exchange with id '" + args.id + "'.")
        return self
