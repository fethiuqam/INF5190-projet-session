from pytz import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from import_donnees import importer_donnees

montreal_timezone = timezone('America/Montreal')
scheduler = BackgroundScheduler(timezone=montreal_timezone)
scheduler.add_job(func=importer_donnees, trigger='cron', hour='00',
                  minute='00')


def demarrer_planification():
    scheduler.start()

