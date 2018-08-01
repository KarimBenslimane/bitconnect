from .usermanager import UserManager


class Login:
    user_manager = None

    def __init__(self):
        self.user_manager = UserManager()

    def check_login(self, username, password):
        """
        Check if a user exists with that username and check if the given password is correct
        :param username:
        :param password:
        :return bool:
        """
        users = self.user_manager.get_user_by_username(username)
        if users and users[0].get_password() == password:
            return True
        return False
