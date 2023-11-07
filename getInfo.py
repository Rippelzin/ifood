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

for copy in copys:
    print(copy)

