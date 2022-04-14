from pytz import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from import_data import import_data

montreal_timezone = timezone('America/Montreal')
scheduler = BackgroundScheduler(timezone=montreal_timezone)
scheduler.add_job(func=import_data, trigger='cron', hour='00',
                  minute='00')


def start_planification():
    scheduler.start()

