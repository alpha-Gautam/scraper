from bs4 import BeautifulSoup
from .models import News

import requests
import os
import uuid
from .tasks import download_image







# def download_image(image_url, save_dir, image_name):
#     if not os.path.exists(save_dir):
#         os.makedirs(save_dir)
    
#     downloaded=0
#     image_path = os.path.join(save_dir, image_name)
#     response = requests.get(image_url)
#     if response.status_code == 200:
#         with open(f"{save_dir}/{image_name}", "wb") as f:
#             for chunk in response.iter_content(1024):
#                 f.write(chunk)
#             downloaded=1
#     return image_url, downloaded

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
        
        img_src = 'no image'
        if image_url:
            image_name=f"{str(uuid.uuid4())}.jpg" if title else "no_image.jpg"
            # Fix image URL schema if it starts with //
            img_src = str(image_url['src'])
            if img_src.startswith('//'):
                img_src = 'https:' + img_src
            download_image.delay(img_src, 'downloaded_images', image_name)


        news_item = News(
            title=title.text if title else 'no title',
            description=description.text if description else 'no description',
            image_url=img_src,
            external_url=external_url if external_url else 'no url'
        )
      
        news_items.append(news_item)
    
    # News.objects.bulk_create(news_items)  # Efficient bulk insert


# scrape_new_movies()
 