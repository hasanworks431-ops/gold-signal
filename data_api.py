from funds_config import FUNDS
from market_tsetmc import get_market_data


def get_tgju_data():
    return {
        "gold": 0,
        "dollar": 0
    }


def get_fund_nav(symbol):
    return {
        "nav": 0,
        "bubble": 0
    }


def get_market_all_data():

    funds_data = {}

    for name, info in FUNDS.items():

        symbol = info["symbol"]

        market = get_market_data(symbol)

        nav = get_fund_nav(symbol)

        funds_data[name] = {
            "symbol": symbol,
            "market": market,
            "nav": nav
        }

    return funds_data


# سازگار با main.py فعلی
def get_market_data_all():

    return get_market_all_data()
        
