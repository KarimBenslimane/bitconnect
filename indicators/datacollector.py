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

