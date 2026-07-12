from market_tsetmc import get_market_data as get_tsetmc_data


def get_market_snapshot(symbol):

    market = get_tsetmc_data(symbol)

    snapshot = {

        "symbol": symbol,

        # قیمت
        "price": market.get("last_price"),
        "close": market.get("close_price"),

        # معاملات
        "volume": market.get("volume", 0),
        "value": 0,
        "trade_count": 0,

        # قدرت بازار
        "buy_power": market.get("buy_power", 0),
        "sell_power": market.get("sell_power", 0),

        # صندوق
        "nav": 0,
        "bubble": 0,
        "aum": 0,

        # نقدشوندگی
        "liquidity_score": 0,

        # بازار جهانی
        "gold": 0,
        "dollar": 0,

        # تکنیکال
        "prices": market.get("prices", []),
        "ema20": 0,
        "ema50": 0,
        "ema200": 0,
        "rsi": 0,
        "macd": 0,

        # وضعیت دریافت داده
        "status": market.get("status", "unknown")

    }

    return snapshot
