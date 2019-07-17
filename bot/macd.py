class Macd():
    MACD_BOT = 'bot_id'
    MACD_EXCHANGE = 'exchange'

    bot_id = ''
    exchange = ''

    def set_bot(self, bot_id):
        self.bot_id = bot_id
        return self

    def set_exchange(self, exchange):
        self.exchange = exchange
        return self

    def get_exchange(self):
        return self.exchange
