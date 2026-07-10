import requests


def get_tsetmc_data(symbol):

    try:
        # این بخش بعد از تعیین شناسه دقیق نماد تکمیل می‌شود
        return {
            "symbol": symbol,
            "price": 0,
            "volume": 0,
            "value": 0,
            "buyers": 0,
            "sellers": 0,
            "buy_power": 0,
            "sell_power": 0
        }

    except Exception:
        return {
            "symbol": symbol,
            "price": 0,
            "volume": 0,
            "value": 0,
            "buyers": 0,
            "sellers": 0,
            "buy_power": 0,
            "sell_power": 0
        }
