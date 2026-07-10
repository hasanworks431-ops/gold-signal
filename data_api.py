import requests


FUNDS = {
    "عیار": {
        "symbol": "عیار"
    },
    "طلا": {
        "symbol": "طلا"
    },
    "کهربا": {
        "symbol": "کهربا"
    }
}


def get_tgju_data():
    """
    اطلاعات کلی طلا و دلار
    """
    try:
        # در مرحله بعد اتصال دقیق به منبع اضافه می‌شود
        return {
            "gold": 0,
            "dollar": 0
        }

    except Exception:
        return {
            "gold": 0,
            "dollar": 0
        }



def get_tsetmc_data(symbol):
    """
    اطلاعات معاملات صندوق
    """

    try:
        # آماده برای اتصال به داده بازار
        return {
            "price": 0,
            "volume": 0,
            "buy_power": 0,
            "sell_power": 0,
            "buyers": 0,
            "sellers": 0
        }

    except Exception:
        return {
            "price": 0,
            "volume": 0,
            "buy_power": 0,
            "sell_power": 0,
            "buyers": 0,
            "sellers": 0
        }



def get_fipiran_nav(symbol):
    """
    NAV و ارزش دارایی صندوق
    """

    try:
        return {
            "nav": 0,
            "bubble": 0
        }

    except Exception:
        return {
            "nav": 0,
            "bubble": 0
        }



def get_fund_data():

    funds = {}

    for name, info in FUNDS.items():

        market = get_tsetmc_data(info["symbol"])
        nav = get_fipiran_nav(info["symbol"])

        funds[name] = {
            **market,
            **nav
        }

    return funds



def get_market_data():

    market = get_tgju_data()
    funds = get_fund_data()

    return {
        "market": market,
        "funds": funds
    }
