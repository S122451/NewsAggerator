from django.core.management.base import BaseCommand
import requests 
from bs4 import BeautifulSoup as BSoup
import logging

# Django
from django.conf import settings

# Third Party
import feedparser
from dateutil import parser
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from news.models import Article, nieuwsweb
from news.models import nieuwsweb

logger = logging.getLogger(__name__)

def save_new_article():
   nieuwsweb_list = nieuwsweb.objects.all()
   for web in nieuwsweb_list:
    soup = BSoup(requests.get(web.url).text, "html.parser")
    Articlelist = soup.find_all(web.listarticleobject,{web.listarticleelement:web.listarticlename})
    for article in Articlelist:
        if(web.descarticleobject != None):
            destag = article.find(web.descarticleobject,{web.descarticleelement:web.descearticlename})
            if(destag != None):
              desctekst = destag.text

        artikel = Article(
        image = article.find("img")["src"],
        link = article.find(web.linkarticleobject)[web.linkarticleelement],
        title = article.find(web.titlearticleobject,{web.titlearticleelement:True}).text,
        desc = desctekst
        ) 
        artikel.save()   


class Command(BaseCommand):
    
    help = "Runs apscheduler."
    def handle(self, *args, **options):   
       
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            save_new_article,
            trigger="interval",
            minutes=1,
            id="Zoek nieuw artikels",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job: nieuwe artikels")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")