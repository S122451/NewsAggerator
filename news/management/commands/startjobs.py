from django.core.management.base import BaseCommand
import requests 
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Article

class Command(BaseCommand):
    def handle(self, *args, **options):
        
        soup = BSoup(requests.get("https://www.nu.nl/net-binnen").text, "html.parser")
        Articlelist = soup.find_all("li",{"class":"list__item"})
        for artcile in Articlelist:  
            main = artcile
            link = main['href']
            image_src = str(main.find('img')['src']).split(" ")[-4]
            title = main.find('span')['title']  
            print(title)
            episode = Article(
                title = title,
                url = link,
                image = image_src)
            episode.save()          

