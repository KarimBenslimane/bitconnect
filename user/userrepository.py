from database.repositoryinterface import RepositoryInterface
from database.connection import Connection
from .user import User


class UserRepository(RepositoryInterface):

    def __init__(self):
        self.connection = Connection('users')
        super().__init__()
        self.table = 'users'

    def get(self, id):
        """
        Retrieve a user from database by id
        :param id:
        :return User:
        """
        query = "SELECT * FROM users WHERE users.user_id = %s;"
        params = str(id)
        users = self.database.executeQuery(query, params)
        user = self.connection.query(TYPE_SELECT, {User.USER_ID: id})

        user = None
        if users:
            data = users[0]
            user = self.create_model(data)
        return user

        return self.database.execute(query)

    def getList(self, search_criteria):
        """
        Retrieve a user from database by searchCriteria
        :param search_criteria:
        :return User[]:
        """
        # TODO IMPLEMENT search_criteria
        query = "SELECT * FROM users"
        params = ()
        data = self.database.executeQuery(query, params)
        models = []
        if data:
            for user_data in data:
                model = self.create_model(user_data)
                models.append(model)
        return models

    def save(self, abstractobject):
        return

    def create(self, username, password):
        """
        Create a user in database and retrieve the User
        :param username:
        :param password:
        :return User:
        """
        query = "INSERT INTO users (name, password) values (%s, %s);"
        params = (str(username), str(password))
        self.database.executeQuery(query, params)
        return self.get(self.database.getLastId())

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
