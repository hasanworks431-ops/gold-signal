from flask import Flask
import asyncio

from scheduler import start_scheduler
from signal_engine import analyze_signal
from data_api import get_market_data
from telegram_bot import send_message


app = Flask(__name__)


def run_signal():

    data = get_market_data()

    message = analyze_signal(data)

    asyncio.run(
        send_message(message)
    )


start_scheduler(run_signal)


@app.route("/")
def home():
    return "Gold Signal Pro Bot is Running!"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )
