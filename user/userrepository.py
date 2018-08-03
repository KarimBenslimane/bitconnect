from database.repositoryinterface import RepositoryInterface
from database.connection import Connection
from .user import User


class UserRepository(RepositoryInterface):
    tablename = 'users'

    def __init__(self):
        super().__init__(self.tablename)

    def get(self, id):
        """
        Retrieve a user from database by id
        :param id:
        :return User:
        """
        user_data = self.connection.query(Connection.TYPE_SELECT, {User.USER_ID: id})
        return self.create_model(user_data)

    def getList(self, search_criteria):
        """
        Retrieve a user from database by searchCriteria
        :param search_criteria:
        :return User[]:
        """
        user_data = self.connection.query_all(Connection.TYPE_SELECT, search_criteria)
        models = []
        if user_data:
            for user in user_data:
                model = self.create_model(user)
                models.append(model)
        return models

    def create(self, username, password):
        """
        Create a user in database and retrieve the User
        :param username:
        :param password:
        :return User:
        """
        self.connection.query(
            Connection.TYPE_INSERT,
            {User.USER_NAME: username, User.USER_PASSWORD: password}
        )
        # TODO: maybe replace last_insert_id with something specific
        # TODO: when many people will use the system to avoid wrong ids return
        return self.get(self.connection.query_last_insert_id())

    def create_model(self, data):
        """
        Create a User model from database data (id, username, password)
        :param data:
        :return User:
        """
        model = User()
        model.set_id(data[0])
        model.set_name(data[1])
        model.set_password(data[2])
        return model

    def delete(self, user_id):
        """
        Delete an user from the database
        :param user_id:
        """
        self.connection.query(
            Connection.TYPE_DELETE,
            {
                User.USER_ID: user_id
            }
        )
