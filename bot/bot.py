class Bot:
    BOT_ID = 'bot_id'
    BOT_TYPE = 'type'
    BOT_THRESHOLD = 'threshold'
    BOT_WIN_LIMIT = 'win_limit'
    BOT_LOSS_LIMIT = 'loss_limit'
    BOT_AMOUNT = 'amount'

    TYPE_ARBITRAGE = 'arbitrage'

    id = ''
    bot_type = ''
    threshold = ''
    win_limit = ''
    loss_limit = ''
    amount = ''

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

