from indicators.old_stuff.datacollector import DataCollector
from indicators.old_stuff.datasetcreator import DataSetCreator
from indicators.old_stuff.indicators import Indicators

class IndicatorManager:
    data_collector = None
    dataset_creator = None
    indicators = None    
    
    def __init__(self):
        self.data_collector = DataCollector()
        self.dataset_creator = DataSetCreator()
        
    def execute(self):
        exchanges = ['KRAKEN']
        currency = 'USD'
        exchange_data = self.data_collector.get_exchanges_data(exchanges, currency)
        btc_datasets = self.dataset_creator.merge_into_single(exchange_data)
        avg_btc_price = self.dataset_creator.get_avg_btc_price_usd(btc_datasets)
        
        self.indicators = Indicators(avg_btc_price, btc_datasets)
        self.indicators.plot_macd()
