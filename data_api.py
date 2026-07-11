
from price_history import update_price, get_price_history


from funds_config import FUNDS
from market_tsetmc import get_tsetmc_data


def get_tgju_data():
    """
    اطلاعات طلا و دلار
    فعلاً آماده اتصال به TGJU
    """

    return {
        "gold": 0,
        "dollar": 0
    }



def get_fund_market_data(symbol):
    """
    دریافت اطلاعات معاملات صندوق از TSETMC
    """

    return get_tsetmc_data(symbol)



def get_fund_nav(symbol):
    """
    دریافت NAV و حباب صندوق
    فعلاً آماده اتصال به FIPIRAN
    """

    return {
        "nav": 0,
        "bubble": 0
    }



def get_fund_data():

    funds_data = {}

    for name, info in FUNDS.items():

        symbol = info["symbol"]

        market_data = get_fund_market_data(symbol)

        nav_data = get_fund_nav(symbol)

        funds_data[name] = {
            **market_data,
            **nav_data
        }

    return funds_data



def get_market_data():

    return {
        "market": get_tgju_data(),
        "funds": get_fund_data()
    }
