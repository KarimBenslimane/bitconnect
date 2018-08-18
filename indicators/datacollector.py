import quandl

class DataCollector:
    
    def get_quandl_data(self, quandl_id):
        df = quandl.get(quandl_id, returns="pandas")
        return df
        
    def get_exchanges_data(self, exchanges, currency):
        exchange_data = {}
        for exchange in exchanges:
            exchange_code = 'BCHARTS/{}'+str(currency).format(exchange)
            btc_exchange_df = self.get_quandl_data(exchange_code)
            exchange_data[exchange] = btc_exchange_df
        return exchange_data


import os
import numpy as np
import pandas as pd

import pickle
import quandl

from datetime import datetime

import plotly.offline as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
py.init_notebook_mode(connected=True)

import matplotlib.pyplot as plt

import talib  as ta

##Stap 2. Collecting Data
def get_quandl_data(quandl_id):
    df = quandl.get(quandl_id, returns="pandas")
    return df
    
# Pull Kraken BTC price exchange data
btc_usd_price_kraken = get_quandl_data('BCHARTS/KRAKENUSD')
#btc_usd_price_gemini = get_quandl_data('BCHARTS/GEMINIUSD')

# Chart the BTC pricing data
btc_trace = go.Scatter(x=btc_usd_price_kraken.index, y=btc_usd_price_kraken['Weighted Price'])
py.iplot([btc_trace])

# Pull pricing data for 3 more BTC exchanges
exchanges = ['COINBASE','BITSTAMP','ITBIT','HitBTC']  #GEMINI

exchange_data = {}

exchange_data['KRAKEN'] = btc_usd_price_kraken

for exchange in exchanges:
    exchange_code = 'BCHARTS/{}USD'.format(exchange)
    btc_exchange_df = get_quandl_data(exchange_code)
    exchange_data[exchange] = btc_exchange_df
    
def merge_dfs_on_column(dataframes, labels, col):
    '''Merge a single column of each dataframe into a new combined dataframe'''
    series_dict = {}
    for index in range(len(dataframes)):
        series_dict[labels[index]] = dataframes[index][col]
        
    return pd.DataFrame(series_dict)
    
# Merge the BTC price dataseries' into a single dataframe
btc_usd_datasets = merge_dfs_on_column(list(exchange_data.values()), list(exchange_data.keys()), 'Weighted Price')
# Remove "0" values
btc_usd_datasets.replace(0, np.nan, inplace=True)
# Calculate the average BTC price as a new column
btc_usd_datasets['avg_btc_price_usd'] = btc_usd_datasets.mean(axis=1)
btc_usd_datasets.tail()

dataset = btc_usd_datasets['avg_btc_price_usd']

## Stap 3. Calculating trading indicators
#maak een single array
a = btc_usd_price_kraken['Weighted Price']

#--------------------
#Momentum Indicators Part 1
#MACD MOVING AVERAGE CONVERGENCE DIVERGENCE

macd, macdsignal, macdhist = ta.MACD(a, fastperiod=12, slowperiod=26, signalperiod=9)


trace1 = go.Scatter(
    x= macd.index ,
    y= a ,
    name = '<b>BTC</b>', # Style name/legend entry with html tags
    #connectgaps=True
)
trace2 = go.Scatter(
    x= macd.index ,
    y= macd ,
    name = '<b>MACD</b>',
)
trace3 = go.Scatter(
    x= macd.index ,
    y= macdsignal ,
    name = '<b>MACD-signal</b>',
)
trace4 = go.Scatter(
    x= macd.index ,
    y= macdhist ,
    name = '<b>MACD-hist</b>',
)
data = [trace1, trace2, trace3, trace4]


fig = dict(data=data)
py.iplot( fig)



#--------------------
#Momentum Indicators Part 2
#MACD MOVING AVERAGE CONVERGENCE DIVERGENCE

macd, macdsignal, macdhist = ta.MACD(a, fastperiod=12, slowperiod=26, signalperiod=9)

BTC = go.Scatter(
    x= macd.index ,
    y= a ,
    name = '<b>BTC</b>', # Style name/legend entry with html tags
    #connectgaps=True
)

#trace2 = go.Scatter(
#    x= macd.index ,
#    y= macd ,
#    name = '<b>MACD</b>',
#)
#trace3 = go.Scatter(
#    x= macd.index ,
#    y= macdsignal ,
#    name = '<b>MACD-signal</b>',
#)
MACD_indicator = go.Scatter(
    x= macd.index ,
    y= (macd - macdsignal) ,
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

#fig2 = dict(data=data2)
py.iplot( fig2)

#--------------------
#Momentum Indicators
#Relative Strength Index (RSI)
#https://www.lynx.nl/kennis/artikelen/rsi-indicator-momentum/
real = ta.RSI(a, timeperiod=14)

BTC = go.Scatter(
    x= a.index ,
    y= a ,
    name = '<b>BTC</b>', # Style name/legend entry with html tags
    #connectgaps=True
)

RSI = go.Scatter(
    x= a.index ,
    y= real ,
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

#fig2 = dict(data=data2)
py.iplot( fig2)


#--------------------
#Overlap Studies
#SIMPLE MOVING AVERAGE
sma = ta.SMA(a)



BTC = go.Scatter(
    x= a.index ,
    y= a ,
    name = 'BTC', # Style name/legend entry with html tags
    #connectgaps=True
)
Simple_moving_average = go.Scatter(
    x= a.index ,
    y= sma ,
    name = 'Simple moving average',
)

data = [BTC, Simple_moving_average]


fig = dict(data=data)
py.iplot( fig)



#--------------------
#Overlap Studies
# Calculating bollinger bands, with triple exponential moving average
upper, middle, lower = ta.BBANDS(a, matype=MA_Type.T3)

BTC = go.Scatter(
    x= a.index ,
    y= a ,
    name = 'BTC', # Style name/legend entry with html tags
    #connectgaps=True
)
Upper = go.Scatter(
    x= a.index ,
    y= upper ,
    name = 'Upper',
)
Middle = go.Scatter(
    x= a.index ,
    y= middle ,
    name = 'Middle',
)
Lower = go.Scatter(
    x= a.index ,
    y= lower ,
    name = 'Lower',
)
data = [BTC, Upper, Middle, Lower]


fig = dict(data=data)
py.iplot( fig)






#
#plt.figure(figsize=(20,10))
#plt.plot(a)
#plt.plot(upper)
#plt.plot(middle)
#plt.plot(lower)
#plt.show()




#--------------------
# Pattern Recognition
#CDL TRISTAR
open = btc_usd_price_kraken['Open']
high = btc_usd_price_kraken['High']
low = btc_usd_price_kraken['Low']
close = btc_usd_price_kraken['Close']

Pattern_Recognition = ta.CDLTRISTAR(open, high, low, close)


BTC = go.Scatter(
    x= macd.index ,
    y= a ,
    name = '<b>BTC</b>', # Style name/legend entry with html tags
    #connectgaps=True
)

#trace2 = go.Scatter(
#    x= macd.index ,
#    y= macd ,
#    name = '<b>MACD</b>',
#)
#trace3 = go.Scatter(
#    x= macd.index ,
#    y= macdsignal ,
#    name = '<b>MACD-signal</b>',
#)
Pattern_recognition = go.Scatter(
    x= macd.index ,
    y= Pattern_Recognition ,
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

#fig2 = dict(data=data2)
py.iplot( fig2)

#plt.figure(figsize=(20,10))
#plt.plot(Pattern_Recognition)
#plt.plot(a)
#
#plt.show()

