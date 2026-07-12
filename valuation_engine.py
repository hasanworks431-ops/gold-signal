def calculate_valuation(data):

    score = 50
    reasons = []


    nav = data.get("nav", 0)

    bubble = data.get("bubble", 0)

    aum = data.get("aum", 0)



    # بررسی NAV

    if nav > 0:

        score += 20

        reasons.append(
            "NAV صندوق دریافت شده است"
        )



    # بررسی حباب

    if bubble > 0:


        if bubble < 5:

            score += 20

            reasons.append(
                "حباب در محدوده مناسب است"
            )


        elif bubble > 10:

            score -= 20

            reasons.append(
                "حباب صندوق بالا است"
            )



    # ارزش دارایی صندوق

    if aum > 0:

        score += 10

        reasons.append(
            "ارزش دارایی صندوق مناسب است"
        )



    # محدود کردن امتیاز

    if score > 100:

        score = 100


    if score < 0:

        score = 0



    return {

        "valuation_score": score,

        "valuation_reasons": reasons

    }
