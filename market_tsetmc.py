import requests


TSETMC_SEARCH_URL = "https://old.tsetmc.com/tsev2/data/search.aspx"


def search_symbol(symbol):

    try:

        response = requests.get(
            TSETMC_SEARCH_URL,
            params={"name": symbol},
            timeout=5
        )


        if response.status_code == 200:

            return response.text


    except requests.exceptions.RequestException as e:

        print(
            f"TSETMC connection error for {symbol}: {e}",
            flush=True
        )


    return None



def get_market_data(symbol):

    raw = search_symbol(symbol)


    if not raw:

        return {

            "symbol": symbol,

            "status": "unavailable",

            "prices": [],

            "volume": 0,

            "buy_power": 0,

            "sell_power": 0,

            "bubble": 0

        }



    return {

        "symbol": symbol,

        "status": "found",

        "prices": [],

        "volume": 0,

        "buy_power": 0,

        "sell_power": 0,

        "bubble": 0,

        "raw": raw[:200]

    }
