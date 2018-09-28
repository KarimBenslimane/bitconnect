from console.action.baseaction import BaseAction
from exchanges.exchangemanager import ExchangeManager
from user.usermanager import UserManager


class Create(BaseAction):
    exchange_manager = None
    user_manager = None

    def __init__(self):
        super().__init__()
        self.action = 'exchange_create'
        self.func = self.execute
        self.exchange_manager = ExchangeManager()
        self.user_manager = UserManager()

        self.flags.append(['-n', '--name'])
        self.flags.append(['-pu', '--public'])
        self.flags.append(['-pr', '--private'])
        self.flags.append(['-uid', '--userid'])
        self.flags.append(['-euid', '--exchangeuid'])
        self.flags.append(['-epw', '--exchangepw'])

        self.arguments.append({'dest': 'name', 'required': True})
        self.arguments.append({'dest': 'public', 'required': True})
        self.arguments.append({'dest': 'private', 'required': True})
        self.arguments.append({'dest': 'userid'})
        self.arguments.append({'dest': 'exchangeuid'})
        self.arguments.append({'dest': 'exchangepw'})

    def execute(self, args):
        """
        Create an exchange for an user. If not user_id is given it defaults to the current logged in user.
        :param args:
        """
        userid = args.userid
        exchangeuid = args.exchangeuid
        exchangepw = args.exchangepw
        if not userid:
            userid = self.user_manager.get_user_by_username(args.username)[0].get_id()
        exchange = self.exchange_manager.create_exchange(args.name, args.public, args.private, userid, exchangeuid,
                                                         exchangepw)
        print("Successfully created a new Exchange.")
        self.exchange_manager.print_exchange(exchange)
