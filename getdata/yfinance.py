# Import Librarys
import pandas as pd
import yfinance as yf


# Get DataFrame
def data(tickers, start=None, end=None, period="max", interval="1d", **kwargs):
    """
    :param tickers: List of tickers to download EX: "EURUSD=X"
    :param start: Download start date string (YYYY-MM-DD) or _datetime.
                  Default is 1900-01-01
    :param end: Download start date string (YYYY-MM-DD) or _datetime.
                Default is 1900-01-01
    :param period: Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
                   Either Use period parameter or use start and end
    :param interval:Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
                    Intraday data cannot extend last 60 days
    :return: Get Data from Yahoo Finance EX: data("EURUSD=X", "1mo", "5m")
    """
    df = yf.download(tickers=tickers, start=start, end=end, period=period, interval=interval)

    return df

