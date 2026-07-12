from apscheduler.schedulers.background import BackgroundScheduler
from data_api import get_fund_data

scheduler = BackgroundScheduler(timezone="Asia/Tehran")


def start_scheduler(job):

    scheduler.remove_all_jobs()

    scheduler.add_job(
        job,
        trigger="cron",
        day_of_week="sat,sun,mon,tue,wed",
        hour="11-17",
        minute="*/15",
        id="signal_job",
        replace_existing=True
    )

    if not scheduler.running:
        scheduler.start()
        
