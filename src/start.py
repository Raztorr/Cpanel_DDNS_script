import requests
import datetime
from datetime import datetime

from urllib.parse import urlparse


# Fin imports

e = datetime.now()
print()
print ('Starting DDNS Webcalls')
print ("Current date and time = %s" % e)
print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))

print()


def status(url, nombre):
    url_request = requests.get(url)
    dominio = urlparse(url).netloc
    output = nombre + ': ' + dominio + ': ' + str(url_request.status_code)
    return output


# Fin definicion de funciones


# Inicio Prints de inicio

ip = requests.get('https://api.ipify.org').text
print(f'La ip externa actual es: {ip}')
print()

# Fin prints inicio

# Inicio urls para requests

list_urls = open(r"urls.txt", 'r')
urls_n = list(list_urls)
urls = [url.rstrip('\n') for url in urls_n]
for url in urls:
    url = url.rstrip('\n')
    nombre, url = url.split()

    print(status(url, nombre))