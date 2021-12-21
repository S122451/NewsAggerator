from django.core.management.base import BaseCommand
from news.nieuwsweb import Newweb

class Command(BaseCommand):

    help = "Runs apscheduler."
    def handle(self, *args, **options):
   
            print("Welkom tot het toevoegen van een nieuw website.  Hiervoor heb je wel de inspect element voor nodig.\n")
            newurl = input("Voer het volledige url in.\n")
            newweb = Newweb(newurl)
            newweb.list_info()
            newweb.link_info()
            newweb.title_info()
            existdesc = input("Is er een omschrijving bij elk artikel? voer j of n in? \n")
            if(existdesc == 'j'):
                newweb.description_info()
            newweb.info_save()
            print('Nieuwe nieuws website succesvol opgeslagen')