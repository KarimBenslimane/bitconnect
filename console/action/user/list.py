from console.action.baseaction import BaseAction
from user.user import User
from user.usermanager import UserManager


class List(BaseAction):
    user_manager = None

    def __init__(self):
        super().__init__()
        self.action = 'user_list'
        self.func = self.execute
        self.user_manager = UserManager()
        # TODO DEFAULT NONE
        self.flags.append(['-id', '--userid'])
        self.arguments.append({'dest': 'id'})

    def execute(self, args):
        if args.id:
            self.user_manager.list_user({User.USER_ID: args.id})
        else:
            self.user_manager.list_user([])
        return self
