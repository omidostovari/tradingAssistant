import requests


def technical_indicator(time_period, interval, function, symbol):
    """
    :param time_period: Number of data points used to calculate each moving average value. Positive integers are accepted (e.g., timeperiod=60, timeperiod=200)
    :param interval: Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    :param function: The technical indicator of your choice. In this case, function=SMA
    :param symbol: The name of the security of your choice. For example: symbol=MSFT
    :return: JSON data
    """

    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"time_period": f"{time_period}", "interval": f"{interval}", "series_type": "close", "function": f"{function}", "symbol": f"{symbol}",
                   "datatype": "json"}

    headers = {
        "X-RapidAPI-Key": "147f31d0d7mshfeff868a0b4d1dap1fc5b2jsn307a403f36ec",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text