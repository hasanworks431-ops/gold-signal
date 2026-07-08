import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask
import threading

TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)

@app.route("/")
def home():
    return "Gold Signal Bot is Running"


async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """
📊 تحلیل صندوق طلای مفید

🟡 وضعیت فعلی:
- اونس جهانی: در حال بررسی
- دلار آزاد: در حال بررسی
- NAV صندوق: در حال بررسی
- حجم خریدار: در حال بررسی
- قدرت خریدار/فروشنده: در حال بررسی

📈 تحلیل تکنیکال:
- روند بازار
- حجم معاملات
- قدرت خریدار

⏳ سیگنال نهایی:
🟡 نگهداری

(اتصال داده‌های واقعی در مرحله بعد اضافه می‌شود)
"""
    await update.message.reply_text(message)


def run_flask():
    app.run(host="0.0.0.0", port=8080)


def main():
    bot = Application.builder().token(TOKEN).build()

    bot.add_handler(CommandHandler("signal", signal))

    threading.Thread(target=run_flask).start()

    bot.run_polling()


if __name__ == "__main__":
    main()
