from botinterface import BotInterface
from arbitrage import Arbitrage
from file import helper


def validate_bot(bot):
    return True


def create_bot(filename):
    print("Choose one of the following bots:\n")
    type = str(raw_input("(A)bitrage")).lower()
    bot = create_bot_from_type(type)
    helper.add_bot_to_file(filename, bot.get_values())


def start_bot(bot):
    bot.start()


def create_bot_from_type(type):
    bot = 0
    if type == "A":
        bot = Arbitrage()
    exchanges = []
    bot.init(exchanges)
    return bot
