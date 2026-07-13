from flask import Flask

import asyncio


app = Flask(__name__)



def run_signal():

    print(
        "RUN_SIGNAL STARTED",
        flush=True
    )

    try:

        from data_api import get_market_data
        from signal_engine import analyze_all_funds
        from telegram_bot import send_message


        data = get_market_data()


        print(
            "MARKET DATA RECEIVED",
            flush=True
        )


        message = analyze_all_funds(data)


        print(
            "ANALYSIS COMPLETED",
            flush=True
        )


        asyncio.run(
            send_message(message)
        )


        print(
            "Signal sent successfully",
            flush=True
        )


    except Exception as e:

        print(
            f"Signal error: {e}",
            flush=True
        )



# تلاش برای فعال کردن Scheduler

try:

    from scheduler import start_scheduler


    start_scheduler(
        run_signal
    )


except Exception as e:

    print(
        f"Scheduler error: {e}",
        flush=True
    )



@app.route("/")
def home():

    return "Gold Signal Pro API Running!"



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
