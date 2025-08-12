from django.shortcuts import render
from django.http import JsonResponse
from .script import scrape_new_movies
from .models import News
from django.core.paginator import Paginator

from home.tasks import add

# Create your views here.
def scrape_movies_view(request):
    scrape_new_movies()
    count = 10
    return JsonResponse({'status': 'success',
                         'message': f'Movies scraped successfully. {count} images downloaded.'}, status=200)

def home(request):
    result= add.delay(10,4)
    print("result of add:",result)
    movie_detail = News.objects.all()  # Fetch the latest 10 news items
    movie_details = Paginator(movie_detail, 12)  # Paginate the results, 10 items per page
    page_number = request.GET.get('page')
    page_obj = movie_details.get_page(page_number)
    return render(request, 'home.html',context={'news_data': page_obj})
