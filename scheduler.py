from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import pytz


scheduler = BackgroundScheduler(
    timezone=pytz.timezone("Asia/Tehran")
)


def start_scheduler(job):
    scheduler.add_job(
        job,
        "cron",
        day_of_week="sat, sun, mon, tue, wed",
        hour="11-16",
        minute="45",
    )

    scheduler.start()
