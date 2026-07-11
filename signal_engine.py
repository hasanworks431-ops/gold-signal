
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

        if trend["short_trend"] == "صعودی":
            score += 1
            reasons.append("روند کوتاه مدت EMA20 مثبت است")

        if trend["medium_trend"] == "صعودی":
            score += 1
            reasons.append("روند میان مدت MA50 مثبت است")

        if trend["main_trend"] == "صعودی":
            score += 2
            reasons.append("روند اصلی مثبت است")



    # حجم معاملات
    if volume > 0:
        score += 1
        reasons.append("حجم معاملات فعال است")



    # قدرت خریدار و فروشنده
    if buy_power > sell_power:
        score += 2
        reasons.append("قدرت خریدار بیشتر است")

    elif sell_power > buy_power:
        score -= 1
        reasons.append("فشار فروش بیشتر است")



    # حباب
    if bubble > 0:

        if bubble < 5:
            score += 1
            reasons.append("حباب در محدوده مناسب است")

        elif bubble > 10:
            score -= 1
            reasons.append("حباب بالا است")



    # نتیجه نهایی

    if score >= 6:
        signal = "🟢 خرید"

    elif score <= 2:
        signal = "🔴 فروش"

    else:
        signal = "🟡 دست نگهدار"



    message = f"""
📊 صندوق: {name}

سیگنال: {signal}

امتیاز: {score}

دلایل:
"""


    for r in reasons:
        message += f"\n✅ {r}"


    return message



def analyze_all_funds(data):

    result = []

    funds = data.get("funds", {})

    for name, fund in funds.items():

        result.append(
            analyze_fund(name, fund)
        )


    return "\n\n----------------\n\n".join(result)
