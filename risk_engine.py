def calculate_risk_reward(data):

    prices = data.get("prices", [])

    current_price = data.get("price", 0)


    if not prices or current_price <= 0:

        return {

            "risk_reward": 0,

            "entry": current_price,

            "stop_loss": 0,

            "target": 0,

            "risk_level": "نامشخص"

        }


    recent_prices = prices[-20:]


    low_price = min(recent_prices)

    high_price = max(recent_prices)



    stop_loss = low_price

    target = high_price



    risk = current_price - stop_loss

    reward = target - current_price



    if risk > 0:

        ratio = round(
            reward / risk,
            2
        )

    else:

        ratio = 0



    if ratio >= 2:

        risk_level = "مناسب"


    elif ratio >= 1:

        risk_level = "متوسط"


    else:

        risk_level = "ضعیف"



    return {

        "risk_reward": ratio,

        "entry": current_price,

        "stop_loss": stop_loss,

        "target": target,

        "risk_level": risk_level

    }
