from abc import ABCMeta, abstractmethod


class BotInterface:
    __metaclass__ = ABCMeta
    exchanges = []

    @abstractmethod
    def init(self, exchanges):
        # initialize the bot and setup
        return

    @abstractmethod
    def get_exchanges(self):
        # get exchanges
        return

    @abstractmethod
    def get_values(self):
        # get values
        return

    @abstractmethod
    def print_values(self):
        # print values
        return
