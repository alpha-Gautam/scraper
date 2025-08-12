
from django.urls import path
from .views import scrape_movies_view,home

urlpatterns = [
    path("home/",home, name='home'),
    path('scrape/',scrape_movies_view, name='scrape_movies_view'),
]
