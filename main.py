from flask import Flask

from scheduler import start_scheduler
from data_api import get_market_data
from signal_engine import analyze_all_funds
from telegram_bot import send_message

import asyncio


app = Flask(__name__)



def run_signal():

    print(
        "RUN_SIGNAL STARTED",
        flush=True
    )

    try:

        data = get_market_data()

        message = analyze_all_funds(data)

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



# شروع Scheduler هنگام بالا آمدن Flask

start_scheduler(
    run_signal
)



@app.route("/")
def home():

    return "Gold Signal Pro API Running!"



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
