import requests
from time import sleep
import datetime
from datetime import datetime

from urllib.parse import urlparse


# Fin imports

def status(url):
    url_request = requests.get(url)
    dominio = urlparse(url).netloc
    output = dominio + ': ' + str(url_request.status_code)
    return output


# Fin definicion de funciones


# Inicio Prints de inicio

ip = requests.get('https://api.ipify.org').text
print(f'La ip externa actual es: {ip}')

# Fin prints inicio

# Inicio urls para requests

list_urls = open(r"urls.txt", 'r')
urls_n = list(list_urls)
urls = [url.rstrip('\n') for url in urls_n]
for url in urls:
    print(status(url))