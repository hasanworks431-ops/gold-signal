from flask import Flask
from data_api import get_market_data
from signal_engine import analyze_all_funds
from telegram_bot import send_message
from scheduler import start_scheduler
import asyncio


app = Flask(__name__)


def run_signal():

    print("RUN_SIGNAL STARTED", flush=True)

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


@app.route("/")
def home():

    return "Gold Signal Pro Bot is Running!"


scheduler_started = False


def start_once():

    global scheduler_started

    if scheduler_started:
        return

    start_scheduler(run_signal)

    scheduler_started = True


# شروع Scheduler
start_once()
