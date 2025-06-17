from django.contrib import admin
from .models import Movies, News
# Register your models here.


@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'rating', 'genre', 'director')
    search_fields = ('title', 'director', 'actors')
    list_filter = ('year', 'genre')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_url', 'external_url')
    search_fields = ('title',)