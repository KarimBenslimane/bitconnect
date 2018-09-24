from helpers.logger import Logger
import traceback


class ArbitrageProcess():
    botParams = None
    logger = None

    VERDICT_ONE_TO_TWO = 0
    VERDICT_TWO_TO_ONE = 1

    def __init__(self, botParams):
        self.logger = Logger("arbitrage")
        self.botParams = botParams
        self.logger.info("#" + botParams["id"] + ": Initializing.")

    def start_process(self):
        """
        Start the arbitrage process by checking the balances on the exchanges first,
        then making a verdict on the prices and if viable place an order, repeat.
        :return:
        """
        self.logger.info("#" + self.botParams["id"] + ": Starting.")
        active = True
        while active:
            try:
                if self.check_balance():
                    verdict = self.do_magic()
                    if verdict:
                        self.place_order(verdict)
                else:
                    self.logger.info("#" + self.botParams["id"]+": Not enough balance on exchanges.")
            except Exception as e:
                self.logger.info(str(e))
                self.logger.info(traceback.format_exc())

    def check_balance(self):
        """
        Check balances on both exchanges
        :return:
        """
        #TODO: actual balance checks
        return True

    def do_magic(self):
        """
        Get the orderbooks of both exchanges and check prices,
        if prices ar within limits make a verdict.
        """
        #TODO: actual profit calculations
        if self.botParams['exchange_one'] > self.botParams['exchange_two']:
            return self.VERDICT_ONE_TO_TWO
        elif self.botParams['exchange_one'] < self.botParams['exchange_two']:
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
        #TODO: actual order placements
        if verdict == self.VERDICT_ONE_TO_TWO:
            #buy from A sell to B
            print('placing order')
        else:
            #buy from B sell to A
            print('placing order')