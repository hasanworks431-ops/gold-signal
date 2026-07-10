
def analyze_fund(name, data):

    score = 0
    reasons = []

    price = data.get("price", 0)
    volume = data.get("volume", 0)

    buy_power = data.get("buy_power", 0)
    sell_power = data.get("sell_power", 0)

    nav = data.get("nav", 0)
    bubble = data.get("bubble", 0)


    # حجم معاملات
    if volume > 0:
        score += 1
        reasons.append("حجم معاملات فعال است")


    # قدرت خریدار
    if buy_power > sell_power:
        score += 1
        reasons.append("قدرت خریدار بیشتر از فروشنده است")

    elif sell_power > buy_power:
        score -= 1
        reasons.append("فشار فروش بیشتر است")


    # بررسی NAV و حباب
    if nav > 0:

        if bubble < 3:
            score += 1
            reasons.append("حباب مناسب است")

        elif bubble > 10:
            score -= 1
            reasons.append("حباب بالا است")


    # نتیجه نهایی

    if score >= 3:
        signal = "🟢 خرید"

    elif score <= -1:
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

    for name, fund_data in funds.items():

        result.append(
            analyze_fund(name, fund_data)
        )


    return "\n\n----------------\n\n".join(result)
