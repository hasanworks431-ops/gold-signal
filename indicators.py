def calculate_sma(prices, period):
    if len(prices) < period:
        return 0

    return sum(prices[-period:]) / period



def calculate_ema(prices, period):

    if len(prices) < period:
        return 0

    multiplier = 2 / (period + 1)

    ema = sum(prices[:period]) / period

    for price in prices[period:]:
        ema = (price - ema) * multiplier + ema

    return ema



def analyze_trend(prices):

    if len(prices) < 50:
        return {
            "short_trend": "نامشخص",
            "medium_trend": "نامشخص",
            "main_trend": "نامشخص"
        }


    ema20 = calculate_ema(prices, 20)
    ma50 = calculate_sma(prices, 50)
    ma200 = calculate_sma(prices, 200)

    current_price = prices[-1]


    if current_price > ema20:
        short = "صعودی"
    else:
        short = "نزولی"


    if current_price > ma50:
        medium = "صعودی"
    else:
        medium = "نزولی"


    if ma200 != 0 and current_price > ma200:
        main = "صعودی"
    else:
        main = "نزولی"



    return {
        "EMA20": ema20,
        "MA50": ma50,
        "MA200": ma200,
        "short_trend": short,
        "medium_trend": medium,
        "main_trend": main
    }
