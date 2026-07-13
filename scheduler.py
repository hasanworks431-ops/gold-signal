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


    scheduler.add_job(
        job,
        trigger="cron",
        day_of_week="sat,sun,mon,tue,wed",
        hour="11-16",
        minute="*/5",
        id="signal_job",
        replace_existing=True
    )


    scheduler.add_job(
        job,
        trigger="cron",
        day_of_week="sat,sun,mon,tue,wed",
        hour=17,
        minute=0,
        id="final_signal",
        replace_existing=True
    )


    print(
        "Scheduler jobs added",
        flush=True
    )


    scheduler.start()


    print(
        "Scheduler started",
        flush=True
    )
