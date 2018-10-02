class Bot:
    BOT_ID = 'bot_id'
    BOT_TYPE = 'type'
    BOT_THRESHOLD = 'threshold'
    BOT_WIN_LIMIT = 'win_limit'
    BOT_LOSS_LIMIT = 'loss_limit'
    BOT_AMOUNT = 'amount'
    BOT_CREATED_AT = 'created_at'
    BOT_STATUS = 'status'
    BOT_PAIR = 'pair'
    BOT_USERID = 'user_id'

    TYPE_ARBITRAGE = 'arbitrage'

    STATUS_ON = 'on'
    STATUS_OFF = 'off'
    STATUS_ERROR = 'error'
    STATUS_CANCELED = 'canceled'
    STATUS_FINISHED = 'finished'

    id = ''
    bot_type = ''
    threshold = ''
    win_limit = ''
    loss_limit = ''
    amount = ''
    created_at = ''
    status = ''
    pair = ''
    userid = ''

    def set_id(self, id):
        self.id = id
        return self

    def set_type(self, bot_type):
        self.bot_type = bot_type
        return self

    def set_threshold(self, threshold):
        self.threshold = threshold
        return self

    def set_win_limit(self, win_limit):
        self.win_limit = win_limit
        return self

    def set_loss_limit(self, loss_limit):
        self.loss_limit = loss_limit
        return self

    def set_amount(self, amount):
        self.amount = amount

    def set_created_at(self, created_at):
        self.created_at = created_at

    def set_status(self, status):
        self.status = status

    def set_pair(self, pair):
        self.pair = pair

    def set_userid(self, userid):
        self.userid = userid

    def get_id(self):
        return self.id

    def get_type(self):
        return self.bot_type

    def get_threshold(self):
        return self.threshold

    def get_win_limit(self):
        return self.win_limit

    def get_loss_limit(self):
        return self.loss_limit

    def get_amount(self):
        return self.amount

    def get_created_at(self):
        return self.created_at

    def get_status(self):
        return self.status

    def get_pair(self):
        return self.pair

    def get_userid(self):
        return self.userid
