import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

from collections import defaultdict

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)



b = range(6666)
for a in b:
    url = 'https://script.google.com/macros/s/AKfycbzR2TqHJMaD61h8_16VZxIqQYsrdKfcWXWLn_tqm7dBUvSbLNvRWoSYITkNFfYlvC3sHA/exec'

    response = requests.get(url)
    cnpj = response.json()

    browser = webdriver.Chrome(options=options)

    browser.get('https://cnpj.biz/'+cnpj)

    page_content = browser.page_source

    site = BeautifulSoup(page_content, 'html.parser')


    copys = site.find_all('b', attrs={'class': 'copy'})
    p = site.find_all('p')

    #for copy in copys:
    #    print(copy.text)

   

    objeto = {
        'cnpj': '',
        'cep' : '',
        'razao' : '',
        'data': '',
        'capitalSocial': '',
        'contato' :'',
        'email': '',
        'socio': [],
        'cnae': [],
        }

    objeto = defaultdict(list)

    for x in p:
        y = x.text
        if 'CEP' in y :
            objeto['cep'] = y[4:14]
        if 'Razão Social' in y :
            objeto['razao'] = y[13:-19]
        if 'Data da Abertura' in y :
            objeto['data'] = y[17:28]
        if 'Capital Social' in y :
            objeto['capitalSocial'] = y[16:-21]
        if 'E-mail' in y:
            objeto['email'] = y[8:-36]
        if 'Telefone' in y :
            objeto['contato'] = y[14:29]
        if 'Sócio' in y:
            objeto['socio'].append(y)
  
    
    u = site.find_all('u')
    for l in u:
        print(l.text)
        objeto['cnae'].append(l.text)

    objeto['cnpj'] = cnpj
    print(objeto)

    urlPost = 'https://script.google.com/macros/s/AKfycbxyBD73GSgnqkrvFlClSDrSiTA_lmyaEsEEPpmzNdg88k2uUQWX5Z3GY9IJ4FCIkPcaCQ/exec'
    response = requests.post(urlPost, data=objeto)
    
    browser.close()
"""
print(cep)  
print(razao)
print(data)
print(capitalSocial)
print(contato)
print(email)
print(socio[0])
print(cnae)

"""

"""
data = {
    "cnpj": copys[0].text,
    "razao": copys[3].text,
    "data": copys[4].text,
    "capital": copys[7].text,
    "contato": copys[11].text,
    "cep": copys[14].text,

    
}
print(data)

    #cnpj 0
    #razao socila 3
    #data de abertura 4
    #capital social 7
    #contanto 11
    #cep 14

urlPost = 'https://script.google.com/macros/s/AKfycbyijBqtrgEMzSbjuTdV15I4ZpNdwa8CJrGD3qCoRq5ivpQQGh-YNpYlCQP5VoGEG5muuA/exec'
response = requests.post(urlPost, data=data)


"""