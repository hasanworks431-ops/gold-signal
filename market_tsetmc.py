
  import requests


TSETMC_SEARCH_URL = "https://old.tsetmc.com/tsev2/data/search.aspx"


def search_symbol(symbol):
    try:
        params = {
            "name": symbol
        }

        response = requests.get(
            TSETMC_SEARCH_URL,
            params=params,
            timeout=10
        )

        if response.status_code == 200:
            return response.text

        return None

    except Exception as e:
        print("TSETMC search error:", e)
        return None



def get_market_data(symbol):

    raw = search_symbol(symbol)

    if not raw:
        return {
            "symbol": symbol,
            "status": "not_found",
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
print(get_market_data("عیار"))
