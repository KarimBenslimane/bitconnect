from console.action.baseaction import BaseAction
from user.usermanager import UserManager


class Delete(BaseAction):
    user_manager = None

    def __init__(self):
        super().__init__()
        self.action = 'user_delete'
        self.func = self.execute
        self.user_manager = UserManager()
        self.flags.append(['-id', '--userid'])
        self.arguments.append({'dest': 'id', 'required': True})

    def execute(self, args):
        if self.ask_confirmation():
            self.user_manager.delete_user(args.id)
            print("Successfully deleted user with id '" + args.id + "'.")
        return self
