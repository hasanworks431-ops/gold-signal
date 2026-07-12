from indicators import analyze_trend


def analyze_fund(name, data):

    score = 0
    reasons = []

    prices = data.get("prices", [])

    volume = data.get("volume", 0)
    buy_power = data.get("buy_power", 0)
    sell_power = data.get("sell_power", 0)
    bubble = data.get("bubble", 0)


    # تحلیل روند
    if prices:

        trend = analyze_trend(prices)

        if trend.get("short_trend") == "صعودی":

            score += 1
            reasons.append(
                "روند کوتاه مدت مثبت است"
            )


        if trend.get("medium_trend") == "صعودی":

            score += 1
            reasons.append(
                "روند میان مدت مثبت است"
            )


        if trend.get("main_trend") == "صعودی":

            score += 2
            reasons.append(
                "روند اصلی مثبت است"
            )



    # حجم معاملات

    if volume > 0:

        score += 1

        reasons.append(
            "حجم معاملات فعال است"
        )



    # قدرت خریدار و فروشنده

    if buy_power > sell_power:

        score += 2

        reasons.append(
            "قدرت خریدار بیشتر است"
        )


    elif sell_power > buy_power:

        score -= 1

        reasons.append(
            "فشار فروش بیشتر است"
        )



    # حباب صندوق

    if bubble > 0:


        if bubble < 5:

            score += 1

            reasons.append(
                "حباب مناسب است"
            )


        elif bubble > 10:

            score -= 1

            reasons.append(
                "حباب بالا است"
            )



    # تصمیم نهایی

    if score >= 6:

        signal = "🟢 خرید"


    elif score <= 2:

        signal = "🔴 فروش"


    else:

        signal = "🟡 نگهداری"



    message = f"""
📊 صندوق: {name}

وضعیت: {signal}

امتیاز: {score}/10

دلایل:
"""


    if reasons:

        for reason in reasons:

            message += f"\n✅ {reason}"

    else:

        message += "\n⚪ داده کافی برای تحلیل وجود ندارد"



    return message



def analyze_all_funds(data):

    result = []

    funds = data.get("funds", {})


    for name, fund in funds.items():

        market_data = fund.get(
            "market",
            {}
        )


        result.append(
            analyze_fund(
                name,
                market_data
            )
        )


    return "\n\n----------------\n\n".join(result)
