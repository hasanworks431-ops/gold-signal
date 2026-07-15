from apscheduler.schedulers.background import BackgroundScheduler


print(
    "SCHEDULER MODULE LOADED",
    flush=True
)


scheduler = BackgroundScheduler(
    timezone="Asia/Tehran"
)


def start_scheduler(job):

    print(
        "STARTING SCHEDULER",
        flush=True
    )


    scheduler.add_job(
        job,
        trigger="cron",
        day_of_week="sat,sun,mon,tue,wed",
        hour="11-16",
        minute="*/5",
        id="signal_job",
        replace_existing=True
    )


    # اجرای ساعت 17:00 آخر بازار
    scheduler.add_job(
        job,
        trigger="cron",
        day_of_week="sat,sun,mon,tue,wed",
        hour="17",
        minute="0",
        id="signal_job_final",
        replace_existing=True
    )


    scheduler.start()


    print(
        "SCHEDULER STARTED",
        flush=True
    )
