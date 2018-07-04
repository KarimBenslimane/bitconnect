from abc import ABCMeta, abstractmethod


class BotInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def init(self, exchanges):
        # initialize the bot and setup
        return

    @abstractmethod
    def start(self):
        # start the bot
        return

    @abstractmethod
    def get_exchanges(self):
        # get exchanges
        return

    def get_values(self):
        # get values
        return
