import requests
import json
url = 'https://script.google.com/macros/s/AKfycbwnxwJNc9Qunl0ghreKJae8vv_hMmfrwb7_ZaivbY3vVFfy-MX_0J9qVZ2bthd0xsoK/exec'
data = {
    'nome': 'nome do restaurante',
    'cnpj': 34566543,
    'url': ''
}

print(data)
response = requests.post(url, data=data)
print(response)