from indicators import analyze_trend

from liquidity_engine import calculate_liquidity
from valuation_engine import calculate_valuation
from risk_engine import calculate_risk_reward



def analyze_fund(name, data):

    score = 0
    reasons = []


    # -----------------
    # تحلیل تکنیکال
    # -----------------

    prices = data.get(
        "prices",
        []
    )


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



    # -----------------
    # نقدشوندگی
    # -----------------

    liquidity = calculate_liquidity(data)


    liquidity_score = liquidity.get(
        "liquidity_score",
        0
    )


    if liquidity_score >= 60:

        score += 2

        reasons.extend(
            liquidity.get(
                "liquidity_reasons",
                []
            )
        )



    # -----------------
    # ارزش صندوق
    # -----------------

    valuation = calculate_valuation(data)


    valuation_score = valuation.get(
        "valuation_score",
        0
    )


    if valuation_score >= 70:

        score += 2

        reasons.extend(
            valuation.get(
                "valuation_reasons",
                []
            )
        )



    # -----------------
    # ریسک به ریوارد
    # -----------------

    risk = calculate_risk_reward(data)


    risk_reward = risk.get(
        "risk_reward",
        0
    )


    if risk_reward >= 2:

        score += 2

        reasons.append(
            "نسبت سود به ضرر مناسب است"
        )



    # -----------------
    # تصمیم نهایی
    # -----------------

    if score >= 7:

        signal = "🟢 خرید"


    elif score <= 3:

        signal = "🔴 فروش"


    else:

        signal = "🟡 نگهداری"



    message = f"""
📊 صندوق: {name}

وضعیت: {signal}

امتیاز: {score}/10

نقدشوندگی: {liquidity_score}/100

ارزش صندوق: {valuation_score}/100

ریسک/بازده: {risk_reward}

"""


    if risk.get("entry",0):

        message += f"""
ورود: {risk.get('entry')}
حد ضرر: {risk.get('stop_loss')}
هدف: {risk.get('target')}
"""



    message += "\nدلایل:"


    for reason in reasons:

        message += f"\n✅ {reason}"



    return message




def analyze_all_funds(data):

    result = []


    funds = data.get(
        "funds",
        {}
    )


    for name, fund in funds.items():


        result.append(
            analyze_fund(
                name,
                fund.get(
                    "market",
                    {}
                )
            )
        )


    return "\n\n----------------\n\n".join(result)
