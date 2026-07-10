from funds_config import FUNDS


def get_tgju_data():
    return {
        "gold": 0,
        "dollar": 0
    }



def get_fund_market_data(symbol):

    # فعلاً آماده اتصال به داده بازار
    return {
        "price": 0,
        "volume": 0,
        "buy_power": 0,
        "sell_power": 0,
        "buyers": 0,
        "sellers": 0
    }



def get_fund_nav(symbol):

    # فعلاً آماده اتصال به NAV
    return {
        "nav": 0,
        "bubble": 0
    }



def get_fund_data():

    result = {}

    for name, info in FUNDS.items():

        market = get_fund_market_data(
            info["symbol"]
        )

        nav = get_fund_nav(
            info["symbol"]
        )

        result[name] = {
            **market,
            **nav
        }

    return result



def get_market_data():

    return {
        "market": get_tgju_data(),
        "funds": get_fund_data()
    }
