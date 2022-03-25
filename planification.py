from pytz import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from import_donnees import importer_donnees

montreal_timezone = timezone('America/Montreal')

scheduler = BackgroundScheduler(timezone=montreal_timezone)


def job():
    print('job')


scheduler.add_job(func=importer_donnees, trigger='cron', hour='00',
                  minute='00')


# scheduler.add_job(func=job, trigger='cron', second='00')


def demarrer_planification():
    scheduler.start()
