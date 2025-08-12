from celery import shared_task
import time
import os 
import requests

@shared_task
def add(x, y):
    time.sleep(5)

    return x + y



@shared_task
def download_image(image_url, save_dir, image_name):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    downloaded=0
    image_path = os.path.join(save_dir, image_name)
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(f"{save_dir}/{image_name}", "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
            downloaded=1
    return image_url, downloaded