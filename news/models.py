from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    image = models.URLField()

    def __str__(self) -> str:
        return f"{self.title}"