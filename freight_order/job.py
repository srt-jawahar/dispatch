from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from freight_order.task import reset_no_of_trucks


def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(reset_no_of_trucks, 'interval', seconds=5)
    # run the scheduler at every day 6:01 AM
    scheduler.add_job(reset_no_of_trucks, 'cron', hour=6, minute=1)
    scheduler.start()
