def calculate_liquidity(data):

    score = 0
    reasons = []


    volume = data.get("volume", 0)

    value = data.get("value", 0)

    trade_count = data.get("trade_count", 0)

    buy_power = data.get("buy_power", 0)

    sell_power = data.get("sell_power", 0)



    # حجم معاملات

    if volume > 0:

        score += 25

        reasons.append(
            "حجم معاملات فعال است"
        )



    # ارزش معاملات

    if value > 0:

        score += 25

        reasons.append(
            "ارزش معاملات مناسب است"
        )



    # تعداد معاملات

    if trade_count > 0:

        score += 20

        reasons.append(
            "تعداد معاملات قابل قبول است"
        )



    # قدرت خرید و فروش

    if buy_power > sell_power:

        score += 30

        reasons.append(
            "قدرت خریدار بیشتر است"
        )


    elif sell_power > buy_power:

        score += 10

        reasons.append(
            "فشار فروش وجود دارد"
        )



    return {

        "liquidity_score": score,

        "liquidity_reasons": reasons

    }
