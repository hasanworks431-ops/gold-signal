from funds_config import FUNDS
from market_provider import get_market_snapshot


def get_market_all_data():

    funds_data = {}

    for name, info in FUNDS.items():

        symbol = info["symbol"]

        market = get_market_snapshot(symbol)


        funds_data[name] = {

            "symbol": symbol,

            "market": market

        }


    return {

        "funds": funds_data

    }



def get_market_data():

    return get_market_all_data()
