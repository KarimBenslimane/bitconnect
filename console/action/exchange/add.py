from console.action.baseaction import BaseAction
from exchanges.exchangemanager import ExchangeManager
from user.usermanager import UserManager


class Add(BaseAction):
    exchange_manager = None
    user_manager = None

    def __init__(self):
        super().__init__()
        self.action = 'exchange_add'
        self.func = self.execute
        self.exchange_manager = ExchangeManager()
        self.user_manager = UserManager()

        self.flags.append(['-n', '--name'])
        self.flags.append(['-pu', '--public'])
        self.flags.append(['-pr', '--private'])
        self.flags.append(['-uid', '--userid'])

        self.arguments.append({'dest': 'name', 'required': True})
        self.arguments.append({'dest': 'public', 'required': True})
        self.arguments.append({'dest': 'private', 'required': True})
        self.arguments.append({'dest': 'userid'})

    def execute(self, args):
        if args.userid:
            self.exchange_manager.create_exchange(args.name, args.public, args.private, args.userid)
        else:
            userid = self.user_manager.get_user_by_username(args.username)[0].get_id()
            self.exchange_manager.create_exchange(args.name, args.public, args.private, userid)
        return self
