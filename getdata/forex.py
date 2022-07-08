import requests


def fx_intraday(interval, to_symbol, from_symbol):

    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {
        "function": "FX_INTRADAY", "interval": f"{interval}", "to_symbol": f"{to_symbol}",
        "from_symbol": f"{from_symbol}", "datatype": "json", "outputsize": "compact"
    }

    headers = {
        "X-RapidAPI-Key": "147f31d0d7mshfeff868a0b4d1dap1fc5b2jsn307a403f36ec",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text


def fx_daily(to_symbol, from_symbol):

    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"from_symbol": f"{from_symbol}", "function": "FX_DAILY", "to_symbol": f"{to_symbol}", "outputsize": "compact",
                   "datatype": "json"}

    headers = {
        "X-RapidAPI-Key": "147f31d0d7mshfeff868a0b4d1dap1fc5b2jsn307a403f36ec",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text


def fx_weekly(to_symbol, from_symbol):

    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"function": "FX_WEEKLY", "from_symbol": f"{from_symbol}", "to_symbol": f"{to_symbol}", "datatype": "json"}

    headers = {
        "X-RapidAPI-Key": "147f31d0d7mshfeff868a0b4d1dap1fc5b2jsn307a403f36ec",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text





