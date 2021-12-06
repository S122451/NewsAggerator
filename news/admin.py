from django.contrib import admin

from .models import Article

@admin.register(Article)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("title","image")