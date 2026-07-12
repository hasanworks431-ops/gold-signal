from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler(timezone="Asia/Tehran")


def start_scheduler(job):

    scheduler.remove_all_jobs()

    scheduler.add_job(
        job,
        trigger="cron",
        day_of_week="sat,sun,mon,tue,wed",
        hour="*",
        minute="*/5",
        id="signal_job",
        replace_existing=True
    )

    print("Scheduler job added")

    if not scheduler.running:

        scheduler.start()

        print("Scheduler started")
