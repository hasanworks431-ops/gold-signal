import requests
import re


def get_tsetmc_data(symbol):

    try:
        url = f"https://www.tsetmc.com/Loader.aspx?ParTree=151311&i={symbol}"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        text = response.text


        # فعلاً استخراج اولیه
        numbers = re.findall(r'\d+', text)


        return {
            "symbol": symbol,
            "price": 0,
            "close_price": 0,
            "volume": 0,
            "value": 0,
            "buyers": 0,
            "sellers": 0,
            "buy_power": 0,
            "sell_power": 0,
            "raw": numbers[:10]
        }


    except Exception as e:

        return {
            "symbol": symbol,
            "price": 0,
            "close_price": 0,
            "volume": 0,
            "value": 0,
            "buyers": 0,
            "sellers": 0,
            "buy_power": 0,
            "sell_power": 0,
            "error": str(e)
        }
        if __name__ == "__main__":

    for symbol in ["عیار", "طلا", "کهربا"]:
        data = get_tsetmc_data(symbol)
        print(symbol, data)
