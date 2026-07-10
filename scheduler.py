
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz


def start_scheduler(job):

    scheduler = BackgroundScheduler(
        timezone=pytz.timezone("Asia/Tehran")
    )

    # شنبه تا چهارشنبه، هر 30 دقیقه بین 11:45 تا 17:00
    scheduler.add_job(
        job,
        "cron",
        day_of_week="sat-wed",
        hour="11-16",
        minute="0,30"
    )

    # اجرای 17:00
    scheduler.add_job(
        job,
        "cron",
        day_of_week="sat-wed",
        hour="17",
        minute="0"
    )

    scheduler.start()
