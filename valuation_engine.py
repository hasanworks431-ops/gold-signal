def calculate_valuation(data):
    """
    محاسبه امتیاز ارزش‌گذاری صندوق
    بر اساس:
    - NAV
    - Bubble
    - AUM
    """

    score = 50
    reasons = []

    nav = data.get("nav")
    bubble = data.get("bubble")
    aum = data.get("aum")

    # -----------------
    # NAV
    # -----------------

    if nav is not None:

        if nav > 0:
            score += 20
            reasons.append("NAV صندوق دریافت شده است")

    else:

        reasons.append("NAV در دسترس نیست")

    # -----------------
    # Bubble
    # -----------------

    if bubble is not None:

        if bubble < 5:

            score += 20
            reasons.append("حباب صندوق پایین و مناسب است")

        elif bubble <= 10:

            reasons.append("حباب صندوق در محدوده عادی است")

        else:

            score -= 20
            reasons.append("حباب صندوق بالا است")

    else:

        reasons.append("اطلاعات حباب موجود نیست")

    # -----------------
    # AUM
    # -----------------

    if aum is not None:

        if aum > 0:

            score += 10
            reasons.append("ارزش دارایی صندوق مناسب است")

    else:

        reasons.append("اطلاعات AUM موجود نیست")

    # -----------------
    # محدودسازی امتیاز
    # -----------------

    score = max(0, min(score, 100))

    return {

        "valuation_score": score,

        "valuation_reasons": reasons

    }
