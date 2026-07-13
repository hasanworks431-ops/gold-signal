def get_rahavard(symbol):

    """
    فعلاً نسخه اولیه.
    بعداً به API یا Web Scraper راه‌آورد وصل می‌شود.
    """

    return {

        "symbol": symbol,

        "ema20": 0,
        "ema50": 0,
        "ema200": 0,

        "rsi": 0,
        "macd": 0,

        "status": "placeholder"

    }
