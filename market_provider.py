from providers.tsetmc_provider import get_tsetmc
from providers.fipiran_provider import get_fipiran
from providers.tgju_provider import get_tgju
from providers.rahavard_provider import get_rahavard



def safe_get(provider, *args):

    try:

        result = provider(*args)

        if result is None:
            return {}

        return result


    except Exception as e:

        print(
            f"Provider error: {e}",
            flush=True
        )

        return {}



def get_market_snapshot(symbol):

    print(
        f"START DATA FOR {symbol}",
        flush=True
    )


    tsetmc = safe_get(
        get_tsetmc,
        symbol
    )


    fipiran = safe_get(
        get_fipiran,
        symbol
    )


    tgju = safe_get(
        get_tgju
    )


    rahavard = safe_get(
        get_rahavard,
        symbol
    )


    snapshot = {

        "symbol": symbol,


        "price": tsetmc.get("price"),
        "close": tsetmc.get("close"),

        "volume": tsetmc.get("volume"),
        "value": tsetmc.get("value"),

        "trade_count": tsetmc.get("trade_count"),

        "buy_power": tsetmc.get("buy_power"),
        "sell_power": tsetmc.get("sell_power"),

        "prices": tsetmc.get("prices"),


        "nav": fipiran.get("nav"),
        "bubble": fipiran.get("bubble"),
        "aum": fipiran.get("aum"),


        "gold": tgju.get("gold"),
        "dollar": tgju.get("dollar"),
        "ounce": tgju.get("ounce"),


        "ema20": rahavard.get("ema20"),
        "ema50": rahavard.get("ema50"),
        "ema200": rahavard.get("ema200"),

        "rsi": rahavard.get("rsi"),
        "macd": rahavard.get("macd"),



        "sources": {

            "tsetmc": tsetmc.get(
                "status",
                "unknown"
            ),

            "fipiran": fipiran.get(
                "status",
                "unknown"
            ),

            "tgju": tgju.get(
                "status",
                "unknown"
            ),

            "rahavard": rahavard.get(
                "status",
                "unknown"
            )

        }

    }


    available_sources = sum(
        1
        for source in snapshot["sources"].values()
        if source not in ["error", "unknown", None]
    )


    if available_sources == 4:

        snapshot["status"] = "complete"

    elif available_sources > 0:

        snapshot["status"] = "partial"

    else:

        snapshot["status"] = "failed"



    print(
        f"SNAPSHOT DONE {symbol}",
        flush=True
    )


    return snapshot
