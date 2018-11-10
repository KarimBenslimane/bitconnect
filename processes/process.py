from bot.bot import Bot
from processes.arbitrageprocess import ArbitrageProcess
import sys
import json


class Process:
    test = None
    process = None
    botParams = None

    def __init__(self, botParams, test=True):
        self.test = test
        self.botParams = botParams
        self.process = self.get_process()

    def get_process(self):
        """
        Initiate the correct process class
        :return:
        """
        if self.botParams[Bot.BOT_TYPE] == Bot.TYPE_ARBITRAGE:
            return ArbitrageProcess(self.botParams[Bot.BOT_ID])

    def start_process(self):
        """
        Start the process
        :return:
        """
        self.process.start_process()


# bot_values = json.loads(sys.argv[1])
# process = Process(bot_values)
# process.start_process()
