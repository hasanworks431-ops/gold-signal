from data_api import get_market_data
from signal_engine import analyze_all_funds
from telegram_bot import send_message
from scheduler import start_scheduler
import asyncio



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
            f"Worker error: {e}",
            flush=True
        )




def main():

    print(
        "WORKER STARTED",
        flush=True
    )


    start_scheduler(
        run_signal
    )


    # جلوگیری از بسته شدن Worker

    while True:

        import time

        time.sleep(60)




if __name__ == "__main__":

    main()
