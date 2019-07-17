from bot.botmanager import BotManager
from bot.bot import Bot
from bot.macdmanager import MacdManager
from helpers.logger import Logger
from exchanges.exchangemanager import ExchangeManager
from exchanges.exchange import Exchange
from indicators.macdindicator import MacdIndicator
import datetime
from time import strftime
import traceback


class MACDProcess:

    macdindicator = None
    exchange_manager = None
    bot_manager = None
    bot = None
    macdmanager = None
    macd = None
    open_order = None
    exchange = None

    # TODO: maybe change to some config file
    BALANCE_LIMIT = 0.002  # minimum balance needed on the exchange

    def __init__(self, botId):
        self.logger = Logger("macd")
        self.logger.info("#" + str(botId) + ": Initializing.")
        self.bot_manager = BotManager()
        self.exchange_manager = ExchangeManager()
        self.macd_manager = MacdManager()
        self.macdindicator = MacdIndicator()
        self.bot = self.bot_manager.get_bot(botId)
        self.macd = self.macd_manager.get_macd(botId)

    def start_process(self):
        """
        Start the macd process by checking the balances on the exchanges first,
        then making a verdict on the prices and if viable place an order, repeat.
        """
        print(strftime('%Y%m%d%H%M%S') + ' starting MACD process for bot#' + str(self.bot.get_id()))
        self.logger.info("#" + str(self.bot.get_id()) + ": Starting.")
        while not self.open_order:
            try:
                if not self.exchange:
                    self.init_exchange()
                # if self.check_balance():
                print(strftime('%Y%m%d%H%M%S') + ' do magic #' + str(self.bot.get_id()))
                verdict = self.do_magic()
                if verdict:
                    self.place_orders(verdict)
                    self.finish_bot()
            except Exception as e:
                print(strftime('%Y%m%d%H%M%S') + ' ' + str(e))
                self.logger.info(str(e))
                self.logger.info(traceback.format_exc())
                # TODO: uncomment this line
                # self.bot_manager.update_bot(self.bot.get_id, {Bot.BOT_STATUS: Bot.STATUS_ERROR})
                break
        print(strftime('%Y%m%d%H%M%S') + ' finished MACD process for bot#' + str(self.bot.get_id()))
        self.logger.info("#" + str(self.bot.get_id()) + ": Finished.")
        # TODO: uncomment this line
        # self.bot_manager.update_bot(self.bot.get_id, {Bot.BOT_STATUS: Bot.STATUS_FINISHED})

    def init_exchange(self):
        """
        Find the exchange that are needed for the MACD
        """
        exchange = self.fetch_exchange(self.macd.get_exchange())
        if exchange:
            self.exchange = exchange
        else:
            raise Exception("Exchange not found.")

    def fetch_exchange(self, exchange):
        """
        Fetch exchange
        :param exchange:
        :return:
        """
        exchanges = self.exchange_manager.get_exchanges(
            {Exchange.EXCHANGE_USER: self.bot.get_userid(),
             Exchange.EXCHANGE_NAME: exchange}
        )
        if exchanges:
            return exchanges[0]
        else:
            return None

    def check_balance(self):
        # TODO: might place this somewehere else for more process to acces? maybe an abstract class that each process can inherent
        """
        Check balances on the exchange
        :return bool:
        """
        balance = self.exchange_manager.fetch_balance(
            self.exchange,
            self.bot.get_pair()
        )
        if not balance or float(balance) < float(self.BALANCE_LIMIT):
            raise Exception(
                "Not enough balance on exchange '" + self.exchange.get_name() + "' / '" + balance + "'."
            )
        return True

    def do_magic(self):
        """
        Take the exchange data for the given pair for the last 700 hours,
        put this data in the MACD function,
        compare t with t-1,
        this will gives us a verdict
        """
        hoursago = datetime.datetime.now() - datetime.timedelta(hours=720)
        data = self.exchange_manager.get_history_data(self.exchange, self.bot.get_pair(), hoursago.timestamp())
        return self.macdindicator.indicate(data)

    def place_orders(self, verdict):
        """
        Place an order depending on the verdict.
        :param verdict:
        :return:
        """
        print("placing order with verdict: '" + verdict + "'")
        order_result = self.exchange_manager.place_order(
            self.exchange,
            self.bot.get_pair(),
            verdict,
            self.bot.get_amount()
        )
        if not order_result["id"]:
            raise Exception("Could not place " + verdict + "order. " + order_result["info"])
        self.open_order = True

    def finish_bot(self):
        """
        Set local open order variable to true so no new order will be placed for this bot
        :return:
        """
        #TODO: fetch the order data wait untill closed and save them in order DB?
        self.bot.set_status(Bot.STATUS_FINISHED)
