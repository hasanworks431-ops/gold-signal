from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler(
    timezone="Asia/Tehran"
)


def start_scheduler(job):

    if scheduler.running:

        print(
            "Scheduler already running",
            flush=True
        )

        return


    existing_jobs = scheduler.get_jobs()


    if not existing_jobs:

        scheduler.add_job(
            job,
            trigger="cron",
            day_of_week="sat,sun,mon,tue,wed",
            hour="*",
            minute="*/5",
            id="signal_job",
            replace_existing=True
        )

        print(
            "Scheduler job added",
            flush=True
        )


    scheduler.start()


    print(
        "Scheduler started",
        flush=True
    )
