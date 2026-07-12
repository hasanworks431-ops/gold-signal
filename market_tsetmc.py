
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

    result = search_symbol(symbol)

    if result:
        return {
            "symbol": symbol,
            "status": "found",
            "raw": result[:200]
        }

    return {
        "symbol": symbol,
        "status": "not_found",
        "raw": None
    }



if __name__ == "__main__":

    for symbol in ["عیار", "طلا", "کهربا"]:
        print(get_market_data(symbol))
