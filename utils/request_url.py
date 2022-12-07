import requests
import os

path = os.getcwd()

def download_url(url):
    file = 'card.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(file, 'wb') as image:
            for chunk in request:
                image.write(chunk)
    return f'{path}/{file}'
    