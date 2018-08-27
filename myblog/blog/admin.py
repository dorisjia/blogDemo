from django.contrib import admin

from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'publish_time')
    list_filter = ('publish_time',)

admin.site.register(Article, ArticleAdmin)