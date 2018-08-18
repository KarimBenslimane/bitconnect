from indicators.datacollector import DataCollector
from indicators.datasetcreator import DataSetCreator
from indicators.indicators import Indicators

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
        
        self.indicators = Indicators(btc_datasets, avg_btc_price)
    