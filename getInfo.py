import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time



url = 'https://script.google.com/macros/s/AKfycbyinhEEiW_ZkxjT5SRRsMsfRoCmWJMXQxI6gjBnejwwus7mgfLFEfk7HBcr6rX1Bg2Zvg/exec'

response = requests.get(url)
cnpj = response.json()


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

#contato, socios, capital social, cnae, data de abertura, razao social e localizacao

browser.get('https://cnpj.biz/'+cnpj)

page_content = browser.page_source

site = BeautifulSoup(page_content, 'html.parser')


copys = site.find_all('b', attrs={'class': 'copy'})
p = site.find_all('p')

#for copy in copys:
#    print(copy.text)

cep = ''
razao = ''
data = ''
capitalSocial = ''
contato = ''
email=''
socio = []

for x in p:
    y = x.text
    if 'CEP' in y :
        cep = y[4:14]
    if 'Razão Social' in y :
        razao = y[13:-19]
    if 'Data da Abertura' in y :
        data = y[17:28]
    if 'Capital Social' in y :
        capitalSocial = y[16:-21]
    if 'E-mail' in y:
        email = y[8:-36]
    if 'Telefone' in y :
        contato = y[14:29]
    if 'Sócio' in y:
        socio.append(y)

divs = site.find_all('div', attrs={'class': 'col c12'})
cnae = []
for div in divs:
    print(div.text)
    if 'Principal' in div:
        cnae.append(div.text)


    
    
print(cep)  
print(razao)
print(data)
print(capitalSocial)
print(contato)
print(email)
print(socio[0])
print(cnae)



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