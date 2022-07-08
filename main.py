from getdata.forex import *
from getdata.technical import technical_indicator

# print(fx_intraday("5min", "USD", "EUR"))
# print(fx_daily("USD", "EUR"))
# print(currency_exchange_rate("JPY", "USD"))
print(technical_indicator("60", "5min", "SMA", "MSFT"))
