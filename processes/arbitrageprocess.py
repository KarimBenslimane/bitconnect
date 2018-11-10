from bot.arbitrage import Arbitrage
from bot.arbitragemanager import ArbitrageManager
from bot.bot import Bot
from bot.botmanager import BotManager
from exchanges.exchangemanager import ExchangeManager
from exchanges.exchange import Exchange
from helpers.logger import Logger
from time import strftime
import traceback


class ArbitrageProcess():
    logger = None
    open_order = False
    exchanges_one = []
    exchanges_two = []
    exchange_manager = None
    arbitrage_manager = None
    bot_manager = None
    arbitrage = None
    bot = None

    # TODO: maybe change to some config file
    BALANCE_LIMIT = 0.002  # minimum balance needed on the exchange

    def __init__(self, botId):
        self.logger = Logger("arbitrage")
        self.logger.info("#" + str(botId) + ": Initializing.")
        self.bot_manager = BotManager()
        self.exchange_manager = ExchangeManager()
        self.arbitrage_manager = ArbitrageManager()
        self.bot = self.bot_manager.get_bot(botId)
        self.arbitrage = self.arbitrage_manager.get_arbitrage(botId)

    def start_process(self):
        """
        Start the arbitrage process by checking the balances on the exchanges first,
        then making a verdict on the prices and if viable place an order, repeat.
        """
        # TODO: uncomment this line
        # self.turn_on_bot()
        print(strftime('%Y%m%d%H%M%S') + ' starting arbitrage process for bot#' + str(self.bot.get_id()))
        self.logger.info("#" + str(self.bot.get_id()) + ": Starting.")
        while not self.open_order:
            try:
                if not self.exchanges_one or not self.exchanges_two:
                    self.init_exchanges()
                if self.check_balance():
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
        print(strftime('%Y%m%d%H%M%S') + ' finished arbitrage process for bot#' + str(self.bot.get_id()))
        self.logger.info("#" + str(self.bot.get_id()) + ": Finished.")
        # TODO: uncomment this line
        # self.bot_manager.update_bot(self.bot.get_id, {Bot.BOT_STATUS: Bot.STATUS_FINISHED})

    def init_exchanges(self):
        """
        Find the exchanges that are needed for the arbitrage
        """
        exchange_one = self.fetch_exchanges(self.arbitrage.get_exchange_one())
        exchange_two = self.fetch_exchanges(self.arbitrage.get_exchange_two())
        if exchange_one and exchange_two:
            self.exchanges_one = exchange_one
            self.exchanges_two = exchange_two
        else:
            raise Exception("Exchanges not found.")

    def fetch_exchanges(self, exchange):
        """
        Fetch exchanges
        :param exchange:
        :return:
        """
        if exchange == "all":
            return self.exchange_manager.get_exchanges({Exchange.EXCHANGE_USER: self.bot.get_userid()})
        else:
            return self.exchange_manager.get_exchanges(
                {Exchange.EXCHANGE_USER: self.bot.get_userid(),
                 Exchange.EXCHANGE_NAME: exchange}
            )

    def check_balance(self):
        # TODO: might place this somewehere else for more process to acces? maybe an abstract class that each process can inherent
        """
        Check balances on all exchanges
        :return bool:
        """
        exchanges = self.exchanges_one.copy()
        exchanges.extend(self.exchanges_two)
        for exchange in exchanges:
            balance = self.exchange_manager.fetch_balance(
                exchange,
                self.bot.get_pair()
            )
            if not balance or float(balance) < float(self.BALANCE_LIMIT):
                raise Exception(
                    "Not enough balance on exchange '" + exchange.get_name() + "' / '" + balance + "'."
                )
        return True

    def do_magic(self):
        """
        Take exchange as base exchange (A) value,
        loop through the other exchange (B) and compare value with base exchange,
        if base exchange is value A significantly lower than B,
        put base exchange A as BUY and exchange B as SELL.
        """
        # TODO: check on fees, make a real arbitrage transaction and see what fees are applied
        print("magic starts")
        amount = float(self.bot.get_amount())
        win_limit = float(self.bot.get_win_limit())
        pair = self.bot.get_pair()
        buy_and_sell = {}
        for a_exchange in self.exchanges_one:
            a_fee_percentage = self.exchange_manager.get_exchange_trading_fee(
                a_exchange,
                pair,
                "maker"
            )  # maker costs in %
            a_price = self.exchange_manager.get_market_price(a_exchange, pair, "buy")  # get price from base exchange
            fee_maker = (a_price * amount) * a_fee_percentage  # calculate the maker fee in 'base currency BTC/USD (BTC)?'
            for b_exchange in self.exchanges_two:  # now loop through the remainder of the exchanges
                if b_exchange != a_exchange:
                    # TODO: INTERCHANGE THESE 2 IF's
                    # if b_exchange.get_id() != a_exchange.get_id():
                    b_fee_percentage = self.exchange_manager.get_exchange_trading_fee(
                        b_exchange,
                        pair,
                        "taker"
                    )  # taker costs in %t
                    b_price = self.exchange_manager.get_market_price(
                        b_exchange,
                        pair,
                        "sell"
                    )  # get price from comparison exchange
                    fee_taker = (b_price * amount) * b_fee_percentage  # calculate the taker fee in #?
                    turnover = (b_price - a_price) * amount  # calculate the turnover
                    total_fees = fee_maker + fee_taker  # calculate the total fees
                    min_profit = (a_price * amount) * (win_limit / float(100))  # calculate the required profit
                    if (turnover - total_fees) > min_profit:
                        # if these exchanges make the required profit, set the list up to place the orders
                        buy_and_sell["buy"] = {"exchange": a_exchange, "price": a_price}
                        buy_and_sell["sell"] = {"exchange": b_exchange, "price": b_price}
        return buy_and_sell

    def place_orders(self, verdict):
        """
        Place an order depending on the verdict.
        Buy from exchange1 and sell to exchange 2 and vice versa.
        :param verdict:
        :return:
        """
        print(verdict)
        print("placing order")
        # first do the buy order
        buy_order = verdict["buy"]
        buy_result = self.exchange_manager.place_order(
            buy_order["exchange"],
            self.bot.get_pair(),
            "buy",
            self.bot.get_amount()
        )
        #TODO: CREATE ORDER MODEL WITH BUY TYPE
        if not buy_result["id"]:
            raise Exception("Could not place BUY order. " + buy_result["info"])
        # then if it went sucessfully place the sell order
        sell_order = verdict["sell"]
        sell_result = self.exchange_manager.place_order(
            sell_order["exchange"],
            self.bot.get_pair(),
            "sell",
            self.bot.get_amount()
        )
        #TODO: CREATE ORDER MODEL WITH SELL TYPE
        if not sell_result["id"]:
            raise Exception("Could not place SELL order. " + sell_result["info"])
        self.open_order = True

    def finish_bot(self):
        """
        Set local open order variable to true so no new order will be placed for this bot
        :return:
        """
        #TODO: fetch the order data wait untill closed and save them in order DB?
        self.bot.set_status(Bot.STATUS_FINISHED)

    def turn_on_bot(self):
        """
        Sets the status of the bot to on and updates the database for future processes
        :return:
        """
        self.bot.set_status(Bot.STATUS_ON)
        self.bot = self.bot_manager.update_bot(self.bot)
