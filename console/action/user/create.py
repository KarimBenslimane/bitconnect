from console.action.baseaction import BaseAction
from user.usermanager import UserManager


# Needs no init function due to only needing base arguments
class Create(BaseAction):
    user_manager = None

    def __init__(self):
        super().__init__()
        self.action = 'user_create'
        self.func = self.execute
        self.user_manager = UserManager()

    def execute(self, args):
        self.user_manager.create_user(args.username, args.password)
        return self
