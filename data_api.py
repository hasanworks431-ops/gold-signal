import requests
from config import GOLD_API_KEY, CURRENCY_API_KEY


def get_gold_price():
    try:
        url = "https://www.goldapi.io/api/XAU/USD"
        headers = {
            "x-access-token": GOLD_API_KEY,
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

        return {
            "gold": data.get("price", 0)
        }

    except Exception:
        return {
            "gold": 0
        }


def get_currency_price():
    try:
        url = "https://api.exchangerate.host/latest?base=USD&symbols=IRR"

        response = requests.get(url, timeout=10)
        data = response.json()

        return {
            "dollar": data.get("rates", {}).get("IRR", 0)
        }

    except Exception:
        return {
            "dollar": 0
        }


def get_ayar_data():
    # در مرحله بعد به API بورس ایران متصل می‌شود
    return {
        "price": 0,
        "nav": 0,
        "bubble": 0,
        "volume": 0
    }


def get_market_data():

    gold = get_gold_price()
    dollar = get_currency_price()
    ayar = get_ayar_data()

    return {
        **gold,
        **dollar,
        **ayar
    }
