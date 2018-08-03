from .userrepository import UserRepository
from .user import User


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

    def get_user_by_username(self, username):
        """
        Retrieve a user from database by username
        :param username:
        :return User[] | []:
        """
        return self.user_repo.getList(search_criteria={User.USER_NAME: username})

    def get_users(self, search_criteria):
        """
        Retrieve user from database
        :return User[]:
        """
        return self.user_repo.getList(search_criteria=search_criteria)

    def print_user(self, user):
        """
        Print User info
        :param user:
        """
        print("Id: " + user.get_id())
        print("Name: " + user.get_name())
        print("\n")

    def list_user(self, search_criteria):
        """
        List all users or one user if -id option is given
        """
        users = self.get_users(search_criteria)
        for user in users:
            self.print_user(user)

    def create_user(self, username, password):
        """
        Create a new user in the database
        :param username:
        :param password:
        :return User:
        """
        if not username or not password:
            raise Exception("Username and password must be given")
        else:
            return self.user_repo.create(username=username, password=password)

    def delete_user(self, user_id):
        """
        Delete an existing user from the database
        :param user_id:
        :return:
        """
        if user_id:
            self.user_repo.delete(user_id=user_id)
        else:
            raise Exception("No user_id found for deleting user.")
