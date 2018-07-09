from botinterface import BotInterface


class Arbitrage(BotInterface):

    def init(self, exchanges):
        self.exchanges = exchanges
        return

    def get_values(self):
        # TODO: exchanges is same to values now
        return self.exchanges

    def get_exchanges(self):
        return self.exchanges

    def print_values(self):
        print("Exchanges:")
        for exchange in self.get_exchanges():
            print(exchange)
        print("Values:")
        for value in self.get_values():
            print(value)
