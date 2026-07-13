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

        # شروع بازار
        scheduler.add_job(
            job,
            trigger="cron",
            day_of_week="sat,sun,mon,tue,wed",
            hour=11,
            minute=45,
            id="market_open_signal",
            replace_existing=True
        )


        # اجرای هر ۵ دقیقه در ساعات بازار
        scheduler.add_job(
            job,
            trigger="cron",
            day_of_week="sat,sun,mon,tue,wed",
            hour="12-16",
            minute="*/5",
            id="market_signal_every_5min",
            replace_existing=True
        )


        # آخرین اجرای ساعت 17:00
        scheduler.add_job(
            job,
            trigger="cron",
            day_of_week="sat,sun,mon,tue,wed",
            hour=17,
            minute=0,
            id="market_close_signal",
            replace_existing=True
        )


        print(
            "Scheduler
