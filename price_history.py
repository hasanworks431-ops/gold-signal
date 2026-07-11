import json
import os


FILE_NAME = "prices.json"



def load_prices():

    if not os.path.exists(FILE_NAME):
        return {}

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)



def save_prices(data):

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def update_price(symbol, price):

    data = load_prices()


    if symbol not in data:
        data[symbol] = []


    data[symbol].append(price)


    # نگهداری آخرین 300 روز
    data[symbol] = data[symbol][-300:]


    save_prices(data)



def get_price_history(symbol):

    data = load_prices()

    return data.get(symbol, [])
