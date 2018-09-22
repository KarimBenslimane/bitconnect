import talib  as ta
import plotly.offline as py
import plotly.graph_objs as go

class Indicators:
    dataset = None
    dataset_prices = None
    
    def __init__(self, dataset, prices):
        self.dataset = dataset
        self.dataset_prices = prices
        
    def macd(self):
        """
        Momentum Indicators Part 2
        MACD MOVING AVERAGE CONVERGENCE DIVERGENCE
        :return [List, List, List]:
        """
        return ta.MACD(self.dataset, fastperiod=12, slowperiod=26, signalperiod=9)
        
    def plot_macd(self):
        macd, macdsignal, macdhist = self.macd()
        BTC = go.Scatter(
            x= macd.index ,
            y= self.dataset ,
            name = '<b>BTC</b>', # Style name/legend entry with html tags
        )
        MACD_indicator = go.Scatter(
            x= macd.index ,
            y= (macdhist) ,
            name = '<b>MACD_indicator</b>',
            yaxis='y2'
        )
        
        data2 = [ BTC,  MACD_indicator]
        layout = go.Layout(
            title='BTC vs MACD_indicator',
            yaxis=dict(
                title='BTC price'
            ),
            yaxis2=dict(
                title='MACD value',
                titlefont=dict(
                    color='rgb(148, 103, 189)'
                ),
                tickfont=dict(
                    color='rgb(148, 103, 189)'
                ),
                overlaying='y',
                side='right'
            )
        )
        fig2 = go.Figure(data=data2, layout=layout)
        py.iplot( fig2)
        
    def rsi(self):
        """
        Momentum Indicators
        Relative Strength Index (RSI)
        https://www.lynx.nl/kennis/artikelen/rsi-indicator-momentum/
        
        :return List:
        """
        return ta.RSI(self.dataset, timeperiod=14)
        
    def plot_rsi(self):
        rsi = self.rsi()
        BTC = go.Scatter(
            x= self.dataset.index ,
            y= self.dataset ,
            name = '<b>BTC</b>',
        )
        
        RSI = go.Scatter(
            x= self.dataset.index ,
            y= rsi ,
            name = '<b>Relative Strength Index (RSI)</b>',
            yaxis='y2'
        )
        
        data2 = [ BTC,  RSI]
        layout = go.Layout(
            title='BTC vs RSI_indicator',
            yaxis=dict(
                title='BTC price'
            ),
            yaxis2=dict(
                title='RSI value',
                titlefont=dict(
                    color='rgb(148, 103, 189)'
                ),
                tickfont=dict(
                    color='rgb(148, 103, 189)'
                ),
                overlaying='y',
                side='right'
            )
        )
        fig2 = go.Figure(data=data2, layout=layout)
        py.iplot(fig2)
        
    def sma(self):
        """
        Overlap Studies
        SIMPLE MOVING AVERAGE
        
        :return List:
        """
        return ta.SMA(self.dataset)
        
    def plot_sma(self):
        sma = self.sma()
        BTC = go.Scatter(
            x= self.dataset.index ,
            y= self.dataset,
            name = 'BTC',
        )
        Simple_moving_average = go.Scatter(
            x= self.dataset.index ,
            y= sma ,
            name = 'Simple moving average',
        )
        data = [BTC, Simple_moving_average]
        fig = dict(data=data)
        py.iplot( fig)
        
    def bollinger_bands(self):
        """
        #Overlap Studies
        # Calculating bollinger bands, with triple exponential moving average
        
        Return [List, List, List]
        """
        return ta.BBANDS(self.dataset, matype=MA_Type.T3)
        
    def plot_bollinger_bands(self):
        upper, middle, lower = self.bollinger_bands()
        BTC = go.Scatter(
            x= self.dataset.index ,
            y= self.dataset,
            name = 'BTC',
        )
        Upper = go.Scatter(
            x= self.dataset.index ,
            y= upper ,
            name = 'Upper',
        )
        Middle = go.Scatter(
            x= self.dataset.index ,
            y= middle ,
            name = 'Middle',
        )
        Lower = go.Scatter(
            x= self.dataset.index ,
            y= lower ,
            name = 'Lower',
        )
        data = [BTC, Upper, Middle, Lower]
        fig = dict(data=data)
        py.iplot( fig)
        
    def tristar(self):
        """
        Pattern Recognition
        CDL TRISTAR
        """
        open_price = self.dataset_prices['Open']
        high_price = self.dataset_prices['High']
        low_price = self.dataset_prices['Low']
        close_price = self.dataset_prices['Close']
        return ta.CDLTRISTAR(open_price, high_price, low_price, close_price)
        
    def plot_tristar(self):
        macd = self.macd()
        tristar = self.tristar()
        BTC = go.Scatter(
            x= macd.index ,
            y= self.dataset,
            name = '<b>BTC</b>',
        )
        Pattern_recognition = go.Scatter(
            x= macd.index ,
            y= tristar,
            name = '<b>Pattern_recognition</b>',
            yaxis='y2'
        )
        
        data2 = [ BTC,  Pattern_recognition]
        layout = go.Layout(
            title='BTC & CDL Tristar',
            yaxis=dict(
                title='BTC price'
            ),
            yaxis2=dict(
                title='Pattern',
                titlefont=dict(
                    color='rgb(148, 103, 189)'
                ),
                tickfont=dict(
                    color='rgb(148, 103, 189)'
                ),
                overlaying='y',
                side='right'
            )
        )
        fig2 = go.Figure(data=data2, layout=layout)
        py.iplot( fig2)