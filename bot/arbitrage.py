from botinterface import BotInterface


class Arbitrage(BotInterface):
    exchanges = []

    def init(self, exchanges):
        if not exchanges or len(exchanges) < 1:
            return False
        else:
            self.exchanges = exchanges
            # TODO: get some information (prices, order values, etc)
            return True

    def start(self):
        # TODO: Save bot in database for main bot to pick up (botManager)?
        return

    def get_values(self):
        return self.exchanges

    def get_exchanges(self):
        return self.exchanges
