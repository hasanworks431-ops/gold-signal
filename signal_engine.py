def analyze_signal(data):

    score = 0
    reasons = []

    gold = data.get("gold", 0)
    dollar = data.get("dollar", 0)
    bubble = data.get("bubble", 0)
    volume = data.get("volume", 0)

    # تحلیل انس جهانی
    if gold > 0:
        score += 1
        reasons.append("انس جهانی دارای داده مثبت است")

    # تحلیل دلار
    if dollar > 0:
        score += 1
        reasons.append("دلار دارای داده قابل بررسی است")

    # حجم معاملات
    if volume > 0:
        score += 1
        reasons.append("حجم معاملات فعال است")

    # حباب
    if bubble < 5 and bubble > 0:
        score += 1
        reasons.append("حباب در محدوده مناسب است")


    if score >= 3:
        signal = "🟢 خرید"

    elif score <= 1:
        signal = "🔴 فروش"

    else:
        signal = "🟡 دست نگهدار"


    message = f"""
Gold Signal

سیگنال: {signal}

امتیاز تحلیل: {score}

دلایل:
"""

    for r in reasons:
        message += f"\n✅ {r}"

    return message
