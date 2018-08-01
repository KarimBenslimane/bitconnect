class Exchange:
    EXCHANGE_ID = 'exchange_id'
    EXCHANGE_NAME = 'name'
    EXCHANGE_PUBLIC = 'public'
    EXCHANGE_PRIVATE = 'private'
    EXCHANGE_USER = 'user_id'

    id = ''
    name = ''
    public = ''
    private = ''
    user_id = ''

    def set_id(self, id):
        self.id = str(id)
        return self

    def set_name(self, name):
        self.name = name
        return self

    def set_public(self, public):
        self.public = public
        return self

    def set_private(self, private):
        self.private = private
        return self

    def set_user_id(self, user_id):
        self.user_id = str(user_id)
        return self

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_public(self):
        return self.public

    def get_private(self):
        return self.private

    def get_user_id(self):
        return self.user_id
