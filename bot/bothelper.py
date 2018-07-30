from .arbitrage import Arbitrage
from file import helper


def validate_bot(bot):
    # print all values and ask for yes/no
    print("Are the following values for the bot correct?\n")
    bot.print_values()
    validation_input = str(raw_input("(y)es or (n)o?")).lower()
    return validation_input == "y"


def create_bot():
    print("Choose one of the following bots:\n")
    type_input = str(raw_input("(A)rbitrage.")).lower()
    return create_bot_from_type(type_input)


def start_bot(filename, bot):
    helper.add_bot_to_file(filename, format_bot_values(bot.get_values()))


def create_bot_from_type(bot_type):
    bot = 0
    if bot_type == "a":
        bot = Arbitrage()
    return bot


def init_bot(bot, exchanges):
    bot.init(exchanges)


def format_bot_values(values):
    string = "exchanges: "
    for value in values:
        string += value + ","
    string += "\n"
    return string


def add_new_bot(password_input, filename_lower):
    # continue creating
    # select what kind of bot
    bot = create_bot()
    exchanges = get_bot_trade_exchanges(password_input, filename_lower)
    init_bot(bot, exchanges)
    if validate_bot(bot):
        start_bot(filename_lower, bot)
    else:
        print("[Error] Bot cannot be validated.\n")
