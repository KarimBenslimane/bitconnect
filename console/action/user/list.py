from console.action.baseaction import BaseAction
from user.usermanager import UserManager


class List(BaseAction):
    user_manager = None

    def __init__(self):
        super().__init__()
        self.action = 'user_list'
        self.func = self.execute
        self.user_manager = UserManager()
        self.init_args()

    def init_args(self):
        self.flags.append(['-id', '--userid'])
        self.arguments.append({'dest': 'id'})

    def execute(self, args):
        self.user_manager.list_user(args)
        return self
