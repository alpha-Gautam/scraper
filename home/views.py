from django.shortcuts import render
from django.http import JsonResponse
from .script import scrape_new_movies
from .models import News

# Create your views here.
def scrape_movies_view(request):
    scrape_new_movies()
    return JsonResponse({'status': 'success',
                         'message': 'Movies scraped successfully.'}, status=200)

def home(request):
    
    
    movie_details = News.objects.all()  # Fetch the latest 10 news items
    return render(request, 'home.html',context={'news_data': movie_details})
