class User:
    USER_ID = 'user_id'
    USER_NAME = 'name'
    USER_PASSWORD = 'password'

    id = ''
    name = ''
    password = ''

    def set_id(self, user_id):
        self.id = str(user_id)
        return self

    def set_name(self, name):
        self.name = name
        return self

    def set_password(self, password):
        self.password = password
        return self

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_password(self):
        return self.password
