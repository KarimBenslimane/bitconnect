from .userrepository import UserRepository


class UserManager:
    user_repo = None

    def __init__(self):
        self.user_repo = UserRepository()

    def get_user(self, id):
        """
        Retrieve a user from database by id
        :param id:
        :return User:
        """
        return self.user_repo.get(id)

    def get_users(self):
        """
        Retrieve user from database
        :return User[]:
        """
        return self.user_repo.getList([])

    def print_user(self, user):
        """
        Print User info
        :param user:
        """
        print("Name: " + user.get_name())
        print("Id: " + user.get_id())
        print("\n")

    def list_user(self, args):
        """
        List all users or one user if -id option is given
        """
        if args.id:
            user = self.get_user(args.id)
            self.print_user(user)
        else:
            users = self.get_users()
            for user in users:
                self.print_user(user)

    def create_user(self, args):
        """
        Create a new user in the database
        :param args:
        :return User:
        """
        if not args.username or not args.password:
            raise Exception("Username and password must be given")
        else:
            user = self.user_repo.create(username=args.username, password=args.password)
            print("Successfully created a new User. \n")
            self.print_user(user)
