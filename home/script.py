from bs4 import BeautifulSoup
from .models import News

import requests
import os



def download_image(image_url, save_dir, image_name):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    
    image_path = os.path.join(save_dir, image_name)
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(f"{save_dir}/{image_name}", "wb") as f:
            f.write(response.content)

def scrape_new_movies():
    url = 'https://www.imdb.com/news/movie'
    headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/91.0.4472.124 Safari/537.36'
                }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    news_items = []
    deta = soup.select('div', class_='ipc-list-card--border-line')

    for item in deta:
        title = item.select_one('a',class_="ipc-link ipc-link--base sc-fbb0baf2-2 jQjxnE")
        description = item.select_one('div', class_='ipc-html-content-inner-div')
        image_url = item.select_one('img',class_="ipc-image")
        external_url = title['href'] if title else None
    
        news_item = News(
            title=title.text if title else 'no title',
            description=description.text if description else 'no description',
            image_url=image_url['src'] if image_url else 'no image',
            external_url=external_url if external_url else 'no url'
        )
        news_items.append(news_item)
        img_url = news_item.image_url
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        download_image(img_url, 'downloaded_images', img_url.split('/')[-1])


    News.objects.bulk_create(news_items)  # Efficient bulk insert

 