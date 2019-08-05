import pandas as pd
import numpy as np
import talib as ta


class MacdIndicator:
    SIGNAL_SELL = 'sell'
    SIGNAL_BUY = 'buy'

    def indicate(self, data):
        series = self.get_series_data(data)
        macd, macdsignal, macdhist = ta.MACD(series, fastperiod=15, slowperiod=196, signalperiod=496)
        last = self.get_last_macdhist(np.array(macdhist))
        before = self.get_second_to_last_macdhist(np.array(macdhist))
        print('last'+'{:.8f}'.format(last))
        print('before'+'{:.8f}'.format(before))
        if last > 0 > before:
            # MACD hist at this moment (t=0) greater than 0 and t-1 lower than 0
            return self.SIGNAL_BUY
        elif last < 0 < before:
            # MACD hist at t=0 lower than 0 and t-1 greater than 0
            return self.SIGNAL_SELL
        else:
            return None

    def get_last_macdhist(self, macdhist):
        if len(macdhist) >= 1:
            return macdhist[-1]

    def get_second_to_last_macdhist(self, macdhist):
        if len(macdhist) > 1:
            return macdhist[-2]

    def get_series_data(self, data):
        for d in data:
            d[0] = pd.to_datetime(d[0]*1000000)
        data_frame = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
        data_frame = data_frame[["timestamp", "close"]].set_index("timestamp").sort_index(ascending=True)
        np_array = np.array(data_frame.close)
        return pd.Series(np_array, index=data_frame.index)
