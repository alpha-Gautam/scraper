from bs4 import BeautifulSoup
from .models import News

import requests



def scrape_new_movies():
    url = 'https://www.imdb.com/news/movie'
    headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/91.0.4472.124 Safari/537.36'
                }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    news_items = []
    deta = soup.find_all('div', class_='ipc-list-card--border-line')

    for item in deta:
        title = item.find('a',class_="ipc-link ipc-link--base sc-fbb0baf2-2 jQjxnE")
        description = item.find('div', class_='ipc-html-content-inner-div')
        image_url = item.find('img',class_="ipc-image")
        external_url = title['href']

        news_item = News(
            title=title.text if title else 'no title',
            description=description.text if description else 'no description',
            image_url=image_url['src'] if image_url else 'no image',
            external_url=external_url if external_url else 'no url'
        )
        news_items.append(news_item)


    News.objects.bulk_create(news_items)  # Efficient bulk insert

    # print(news_items[0])  # Debugging line to check the scraped items
    # News.objects.bulk_create(news_items)  # Efficient bulk insert


scrape_new_movies()



# def scrape_movies():
#     url = 'https://www.imdb.com/chart/top'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     movies = []
#     for row in soup.select('table.chart.full-width tr'):
#         title_column = row.select_one('td.titleColumn')
#         if not title_column:
#             continue
        
#         title = title_column.a.text
#         year = int(title_column.span.text.strip('()'))
#         rating = float(row.select_one('td.imdbRating strong').text)
#         genre = row.select_one('td.genre').text.strip()
#         director = row.select_one('td.director').text.strip()
#         actors = ', '.join([a.text for a in row.select('td.actors a')])
#         plot = row.select_one('td.plot').text.strip()
#         poster_url = row.select_one('td.poster img')['src']
        
#         movie = Movies(
#             title=title,
#             year=year,
#             rating=rating,
#             genre=genre,
#             director=director,
#             actors=actors,
#             plot=plot,
#             poster_url=poster_url
#         )
#         movies.append(movie)
    
#     Movies.objects.bulk_create(movies)  # Efficient bulk insert

# def scrape_news():
#     url = 'https://news.ycombinator.com/'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     news_items = []
#     for item in soup.select('tr.athing'):
#         title = item.select_one('a.storylink').text
#         external_url = item.select_one('a.storylink')['href']
#         news_item = News(
#             title=title,
#             external_url=external_url
#         )
#         news_items.append(news_item)

#     News.objects.bulk_create(news_items)  # Efficient bulk insert
