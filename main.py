


import asyncio
from datetime import datetime, time

from telegram import Bot

from config import TELEGRAM_TOKEN, CHAT_ID
from data_api import get_market_data
from signal_engine import analyze_signal


bot = Bot(token=TELEGRAM_TOKEN)


def is_work_time():

    now = datetime.now()

    # شنبه تا چهارشنبه
    if now.weekday() <= 3:

        start = time(11, 45)
        end = time(17, 0)

        if start <= now.time() <= end:
            return True

    return False


async def send_signal():

    data = get_market_data()

    message = analyze_signal(data)

    await bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )


async def main():

    while True:

        if is_work_time():

            try:
                await send_signal()

            except Exception as e:
                print(e)

            # بررسی هر ۳۰ دقیقه
            await asyncio.sleep(1800)

        else:

            # خارج از ساعت کاری
            await asyncio.sleep(300)


if __name__ == "__main__":
    asyncio.run(main())
