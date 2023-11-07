import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup



#asdads

browser = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
navegador = webdriver.Chrome(options=options)

navegador.get('https://www.ifood.com.br/restaurantes')
navegador.maximize_window()
time.sleep(3)

elemento = navegador.find_element(By.CLASS_NAME, "btn-address--full-size")
elemento.click()
time.sleep(4)


url = 'https://script.google.com/macros/s/AKfycby160ONenrX5ZcvYsLh2vMfevX4Ob4nW3FduHNVWdezrJULKRVyfmkSsx_pY71WnGv4/exec'


a = range(3800)
for b in a:
    

    

    response = requests.get(url)
    print(response)
    restaurantName = response.json()

    searchBar = navegador.find_element(By.CLASS_NAME, 'search-input__field')
    searchBar.send_keys(restaurantName)
    searchBar.submit()


    time.sleep(3)
    restaurantes = navegador.find_elements(By.CLASS_NAME, 'merchant-list-v2__item-wrapper')

    if restaurantes:
            
        restaurantes[0].click()
        time.sleep(4)

        btnCnpj = navegador.find_element(By.CLASS_NAME, 'merchant-details__button')
        btnCnpj.click()
        time.sleep(2)


        page_content = navegador.page_source
        site = BeautifulSoup(page_content, 'html.parser')

        #pega uma lista de p com a mesma classe, o campo cnpj se encontra no index 3 dessa lista, na 4 posicao
        dados = site.find_all('p' , attrs={'class': 'merchant-details-about__info-data'})


        #cria o dado cnpj, que e o index 3 de uma lista dados
        cnpj = dados[3].text

        cnpj = cnpj[6:]

        print(restaurantName , cnpj)

        navegador.back()
        navegador.back()

        urlPost = 'https://script.google.com/macros/s/AKfycbxO7PyIKc2AZTgi4pxg-uSCYZrW6nbQkmzwPn1XUgc9uk4VkKtIhfsLWTB_Q3iZvXXWfg/exec'

        data = {
            'cnpj': cnpj
        }
        
            

        response = requests.post(urlPost, data=data)
        
    else:
        urlPost = 'https://script.google.com/macros/s/AKfycbxO7PyIKc2AZTgi4pxg-uSCYZrW6nbQkmzwPn1XUgc9uk4VkKtIhfsLWTB_Q3iZvXXWfg/exec'

        data = {
            'cnpj': '------'
        }
        response = requests.post(urlPost, data=data)
        navegador.back()
        
