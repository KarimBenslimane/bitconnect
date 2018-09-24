class Arbitrage:
    ARBITRAGE_BOT = 'bot_id'
    ARBITRAGE_E1 = 'exchange_one'
    ARBITRAGE_E2 = 'exchange_two'

    bot_id = ''
    exchange_one = ''
    exchange_two = ''

    def set_bot(self, bot_id):
        self.bot_id = bot_id
        return self

    def set_exchange_one(self, exchange):
        self.exchange_one = exchange
        return self

    def set_exchange_two(self, exchange):
        self.exchange_two = exchange
        return self

    def get_exchange_one(self):
        return self.exchange_one

    def get_exchange_two(self):
        return self.exchange_two