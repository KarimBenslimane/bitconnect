class Exchange:
    EXCHANGE_ID = 'exchange_id'
    EXCHANGE_NAME = 'name'
    EXCHANGE_PUBLIC = 'public'
    EXCHANGE_PRIVATE = 'private'
    EXCHANGE_USER = 'user_id'
    EXCHANGE_UID = 'exchange_uid'
    EXCHANGE_PW = 'exchange_pw'

    id = ''
    name = ''
    public = ''
    private = ''
    user_id = ''
    exchange_uid = ''
    exchange_pw = ''

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

    def set_uid(self, uid):
        self.exchange_uid = str(uid)
        return self

    def set_pw(self, pw):
        self.exchange_pw = str(pw)
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

    def get_uid(self):
        return self.exchange_uid

    def get_pw(self):
        return self.exchange_pw
