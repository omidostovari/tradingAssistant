from getdata.forex import *
from getdata.technical import technical_indicator
import json
from getdata.yfinance import data
# print(fx_intraday("5min", "USD", "EUR"))
# print(fx_daily("USD", "EUR"))
# print(currency_exchange_rate("JPY", "USD"))
# macd_json = technical_indicator("60", "5min", "MACD", "MSFT")
# macd_dumps = json.load(macd_json)
# print(json.loads(macd_json)['Technical Analysis: MACD']['2022-07-07 20:00'])
print(data(tickers='MSFT', start='2020-10-10', end='2020-10-20', interval='1d'))
# print(data)