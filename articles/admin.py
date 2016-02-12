from django.contrib import admin

# Register your models here.
from .models import Article,ArticleCategory

admin.site.register(Article)
admin.site.register(ArticleCategory)
