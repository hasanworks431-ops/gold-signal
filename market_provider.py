from providers.tsetmc_provider import get_tsetmc
from providers.fipiran_provider import get_fipiran
from providers.tgju_provider import get_tgju
from providers.rahavard_provider import get_rahavard


def get_market_snapshot(symbol):

    tsetmc = get_tsetmc(symbol)

    fipiran = get_fipiran(symbol)

    tgju = get_tgju()

    rahavard = get_rahavard(symbol)


    snapshot = {

        "symbol": symbol,


        # TSETMC
        "price": tsetmc.get("price", 0),
        "close": tsetmc.get("close", 0),

        "volume": tsetmc.get("volume", 0),
        "value": tsetmc.get("value", 0),
        "trade_count": tsetmc.get("trade_count", 0),

        "buy_power": tsetmc.get("buy_power", 0),
        "sell_power": tsetmc.get("sell_power", 0),

        "prices": tsetmc.get("prices", []),


        # FIPIRAN
        "nav": fipiran.get("nav", 0),
        "bubble": fipiran.get("bubble", 0),
        "aum": fipiran.get("aum", 0),


        # TGJU
        "gold": tgju.get("gold", 0),
        "dollar": tgju.get("dollar", 0),


        # Rahavard
        "ema20": rahavard.get("ema20", 0),
        "ema50": rahavard.get("ema50", 0),
        "ema200": rahavard.get("ema200", 0),

        "rsi": rahavard.get("rsi", 0),
        "macd": rahavard.get("macd", 0),


        # تحلیل بعداً این را پر می‌کند
        "liquidity_score": 0,


        "status": "ok"

    }


    return snapshot
