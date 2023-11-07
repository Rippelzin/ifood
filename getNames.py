from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests

navegador = webdriver.Chrome()


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
navegador = webdriver.Chrome(options=options)


navegador.get('https://www.ifood.com.br/restaurantes')
navegador.maximize_window()
time.sleep(3)

elemento = navegador.find_element(By.CLASS_NAME, "btn-address--full-size")
elemento.click()
time.sleep(4)

actions = ActionChains(navegador)

b = range(2)
while True:
     try :
        btnVerMais = navegador.find_element(By.CLASS_NAME, "cardstack-nextcontent")
        actions.move_to_element(btnVerMais).perform()
    
        btnVerMais.click()
        time.sleep(4)
     except:
        break



url = 'https://script.google.com/macros/s/AKfycbyjmurPSSrhRAjBakiJ0Cgv2P17nAquFkQ9uCF1D5gJfzMeGyy3FdTi66AXSZ3Gx6RK/exec'

page_content = navegador.page_source

site = BeautifulSoup(page_content, 'html.parser')

nomes = site.find_all('span', attrs={'class': 'merchant-v2__name'})

for nome in nomes:
    data = {
    'nome': nome
    }
    response = requests.post(url, data=data)
    print(response)