from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    pubdate = models.DateTimeField(auto_now_add=True, blank=True)
    desc = models.CharField(max_length=200, default="", blank=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

    
    def __str__(self) -> str:
        return f"{self.title}"

class nieuwsweb(models.Model):
    url = models.URLField()
    listarticleobject = models.CharField(max_length=200)
    listarticleelement = models.CharField(max_length=200)
    listarticlename = models.CharField(max_length=200)
    linkarticleobject =  models.CharField(max_length=200)
    linkarticleelement = models.CharField(max_length=200)
    linkarticlename = models.CharField(max_length=200)
    titlearticleobject = models.CharField(max_length=200)
    titlearticleelement = models.CharField(max_length=200)
    titlearticlename = models.CharField(max_length=200)
    descarticleobject = models.CharField(max_length=200, blank=True)
    descarticleelement = models.CharField(max_length=200, blank=True)
    descearticlename = models.CharField(max_length=200, blank=True)
