from funds_config import FUNDS
from market_tsetmc import 
get_market_data

def get_tgju_data():
    return {
        "gold": 0,
        "dollar": 0
    }



def get_fund_nav(symbol):
    """
    دریافت NAV و حباب صندوق
    بعداً به فیپیران متصل می‌شود
    """

    return {
        "nav": 0,
        "bubble": 0
    }



def get_fund_data():

    funds_data = {}

    for name, info in FUNDS.items():

        symbol = info["symbol"]

        market = get_tsetmc_data(symbol)

        nav = get_fund_nav(symbol)

        funds_data[name] = {
            **market,
            **nav
        }

    return funds_data



def get_market_data():

    return {
        "market": get_tgju_data(),
        "funds": get_fund_data()
    }
def get_fund_data(symbol):

    data = get_market_data(symbol)

    return {
        "symbol": symbol,
        "price": data.get("price"),
        "volume": data.get("volume"),
        "status": data.get("status")
    }
