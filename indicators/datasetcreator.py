import pandas as pd
import numpy as np

class DataSetCreator:
    def merge_dfs_on_column(self, dataframes, labels, col):
    #'''Merge a single column of each dataframe into a new combined dataframe'''
        series_dict = {}
        for index in range(len(dataframes)):
            series_dict[labels[index]] = dataframes[index][col]
        return pd.DataFrame(series_dict)
    
    def merge_into_single(self, exchange_data):
        # Merge the BTC price dataseries' into a single dataframe
        btc_datasets = self.merge_dfs_on_column(list(exchange_data.values()), list(exchange_data.keys()), 'Weighted Price')
        # Remove "0" values
        btc_datasets.replace(0, np.nan, inplace=True)
        return btc_datasets
        
    def get_avg_btc_price_usd(self, btc_datasets):
        # Calculate the average BTC price as a new column
        btc_datasets['avg_btc_price'] = btc_datasets.mean(axis=1)
        dataset = btc_datasets['avg_btc_price']
        return dataset