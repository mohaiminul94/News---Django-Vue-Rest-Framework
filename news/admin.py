from django.contrib import admin
from news.models import Article, Journalist

# Register your models here.
admin.site.register(Journalist)
admin.site.register(Article)