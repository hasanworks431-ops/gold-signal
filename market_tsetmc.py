import requests
import time


TSETMC_SEARCH_URL = "https://old.tsetmc.com/tsev2/data/search.aspx"


def search_symbol(symbol, retries=3):

    for attempt in range(retries):

        try:

            params = {
                "name": symbol
            }

            response = requests.get(
                TSETMC_SEARCH_URL,
                params=params,
                timeout=20
            )

            if response.status_code == 200:

                return response.text


        except requests.exceptions.Timeout:

            print(
                f"TSETMC timeout for {symbol} - attempt {attempt + 1}"
            )


        except requests.exceptions.RequestException as e:

            print(
                f"TSETMC connection error for {symbol}: {e}"
            )


        time.sleep(2)


    return None



def get_market_data(symbol):

    raw = search_symbol(symbol)


    if not raw:

        return {
            "symbol": symbol,
            "status": "unavailable",
            "last_price": None,
            "close_price": None,
            "volume": None
        }


    return {
        "symbol": symbol,
        "status": "found",
        "last_price": None,
        "close_price": None,
        "volume": None,
        "raw": raw[:200]
    }
