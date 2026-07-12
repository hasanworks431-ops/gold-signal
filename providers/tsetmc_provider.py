from market_tsetmc import get_market_data


def get_tsetmc(symbol):

    try:

        data = get_market_data(symbol)

        return {
            "symbol": symbol,

            "price": data.get("last_price", 0),
            "close": data.get("close_price", 0),

            "volume": data.get("volume", 0),
            "value": data.get("value", 0),
            "trade_count": data.get("trade_count", 0),

            "buy_power": data.get("buy_power", 0),
            "sell_power": data.get("sell_power", 0),

            "prices": data.get("prices", []),

            "source": "tsetmc",
            "status": "ok"
        }


    except Exception as e:

        print(
            f"TSETMC provider error for {symbol}: {e}",
            flush=True
        )

        return {
            "symbol": symbol,

            "price": 0,
            "close": 0,

            "volume": 0,
            "value": 0,
            "trade_count": 0,

            "buy_power": 0,
            "sell_power": 0,

            "prices": [],

            "source": "tsetmc",
            "status": "error"
        }
