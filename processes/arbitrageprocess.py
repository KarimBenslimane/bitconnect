from exchanges.exchange import Exchange
from helpers.logger import Logger
import traceback
from time import strftime
from exchanges.exchangemanager import ExchangeManager
from exchanges.ccxtlibrary import CcxtLibrary


class ArbitrageProcess():
    botParams = None
    logger = None
    open_order = False
    ccxt = None
    exchange_one = None
    exchange_two = None

    exchange_manager = None

    VERDICT_ONE_TO_TWO = 0
    VERDICT_TWO_TO_ONE = 1

    # TODO: maybe change to some config file
    BALANCE_LIMIT = 0.002

    def __init__(self, botParams):
        self.logger = Logger("arbitrage")
        self.botParams = botParams
        self.logger.info("#" + botParams["id"] + ": Initializing.")
        self.exchange_manager = ExchangeManager()
        self.ccxt = CcxtLibrary()

    def start_process(self):
        """
        Start the arbitrage process by checking the balances on the exchanges first,
        then making a verdict on the prices and if viable place an order, repeat.
        """
        print(strftime('%Y%m%d%H%M%S') + ' starting arbitrage process for bot#' + self.botParams["id"])
        self.logger.info("#" + self.botParams["id"] + ": Starting.")
        while not self.open_order:
            try:
                if not self.exchange_one or not self.exchange_two:
                    self.init_exchanges()
                if self.check_balance():
                    verdict = self.do_magic()
                    if verdict:
                        self.place_order(verdict)
            except Exception as e:
                print(strftime('%Y%m%d%H%M%S') + ' ' + str(e))
                self.logger.info(str(e))
                self.logger.info(traceback.format_exc())
                break
        print(strftime('%Y%m%d%H%M%S') + ' finished arbitrage process for bot#' + self.botParams["id"])
        self.logger.info("#" + self.botParams["id"] + ": Finished.")

    def init_exchanges(self):
        """
        Find the exchanges that are needed for the arbitrage and put them in local variables
        """
        exchange_one = self.exchange_manager.get_exchanges(
            {Exchange.EXCHANGE_USER: self.botParams["user_id"], Exchange.EXCHANGE_NAME: self.botParams["exchange_one"]}
        )
        exchange_two = self.exchange_manager.get_exchanges(
            {Exchange.EXCHANGE_USER: self.botParams["user_id"], Exchange.EXCHANGE_NAME: self.botParams["exchange_two"]}
        )
        if exchange_one and exchange_two:
            self.exchange_one = exchange_one[0]
            self.exchange_two = exchange_two[0]
        else:
            raise Exception("Exchanges one and/or two not found.")

    def check_balance(self):
        """
        Check balances on both exchanges
        :return bool:
        """
        balance_one = self.ccxt.fetch_balance(
            self.exchange_one,
            self.botParams["pair"]
        )
        balance_two = self.ccxt.fetch_balance(
            self.exchange_two,
            self.botParams["pair"]
        )
        if float(balance_one) >= float(self.BALANCE_LIMIT) and float(balance_two) >= float(self.BALANCE_LIMIT):
            return True
        else:
            raise Exception(
                "Not enough balance on exchanges, balance one: " + str(balance_one) + ", balance two: " + str(
                    balance_two))

    def do_magic(self):
        """
        Get the orderbooks of both exchanges and check prices,
        if prices ar within limits make a verdict.
        """
        # TODO: actual profit calculations
        if self.botParams["exchange_one"] > self.botParams["exchange_two"]:
            return self.VERDICT_ONE_TO_TWO
        elif self.botParams["exchange_one"] < self.botParams["exchange_two"]:
            return self.VERDICT_TWO_TO_ONE
        else:
            return False

    def place_order(self, verdict):
        """
        Place an order depending on the verdict.
        Buy from exchange1 and sell to exchange 2 and vice versa.
        :param verdict:
        :return:
        """
        # TODO: actual order placements
        if verdict == self.VERDICT_ONE_TO_TWO:
            # buy from A sell to B
            print('placing order')
        else:
            # buy from B sell to A
            print('placing order')
        self.open_order = True
