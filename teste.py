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

cnpjList = []
nomeList = []
dataList = []


navegador.get('https://www.ifood.com.br/restaurantes')
navegador.maximize_window()
time.sleep(3)

elemento = navegador.find_element(By.CLASS_NAME, "btn-address--full-size")
elemento.click()
time.sleep(4)
#navegador.execute_script("document.body.style.zoom='zoom 25%'")

#find_element = retorna um item
#find_elements = retorna todos que tem o parametro passado, como class name = 'abc'
#driver.find_element() = driver.find_elements()[0] - > tbm da pra fazer isso kkk



def openCard():
    x = range(20) #999
    for y in x:
        restaurante = navegador.find_elements(By.CLASS_NAME, 'merchant-list-v2__item-wrapper')
        if restaurante:
            time.sleep(8)
            restaurante[y].click()
            time.sleep(8)
            navegador.back()
#a = range(2)
#for b in a:
#    x = range(20)
#    for y in x:
#        restaurantes = navegador.find_elements(By.CLASS_NAME, 'merchant-list-v2__item-wrapper')
#        if restaurantes:
#            time.sleep(8)
#            restaurantes[y].click()
#            time.sleep(8)
#            navegador.back()
#    btnVerMais = navegador.find_element(By.CLASS_NAME, "cardstack-nextcontent")
#    btnVerMais.click()
#    time.sleep(8)

 #   time.sleep(3)


"""
a = range()
for b in a:
    btnVerMais = navegador.find_element(By.CLASS_NAME, "cardstack-nextcontent")
    btnVerMais.click()
    time.sleep(8)
"""
actions = ActionChains(navegador)

b = range(10)
while True:
     try :
        btnVerMais = navegador.find_element(By.CLASS_NAME, "cardstack-nextcontent")
        actions.move_to_element(btnVerMais).perform()
    
        btnVerMais.click()
        time.sleep(8)
     except:
        break



url = 'https://script.google.com/macros/s/AKfycbwnxwJNc9Qunl0ghreKJae8vv_hMmfrwb7_ZaivbY3vVFfy-MX_0J9qVZ2bthd0xsoK/exec'
x = range(9999) #999
for y in x:
    try: 
        restaurantes = navegador.find_elements(By.CLASS_NAME, 'merchant-list-v2__item-wrapper')
        if restaurantes:
            #vai ate o card do restaurante
            actions.move_to_element(restaurantes[y]).perform()
            #espera 8 segundos
            time.sleep(8)
            #clica no card do botao
            restaurantes[y].click()
            time.sleep(8)
        
            #cicla no botao ver mais dentro da pagina do restaurante
            btnCnpj = navegador.find_element(By.CLASS_NAME, 'merchant-details__button')
            btnCnpj.click()
            time.sleep(2)


            page_content = navegador.page_source
            site = BeautifulSoup(page_content, 'html.parser')

            nome = site.find('h1', attrs={'class': 'merchant-info__title'}).text

            #pega uma lista de p com a mesma classe, o campo cnpj se encontra no index 3 dessa lista, na 4 posicao
            dados = site.find_all('p' , attrs={'class': 'merchant-details-about__info-data'})
            
            
            #cria o dado cnpj, que e o index 3 de uma lista dados
            cnpj = dados[3].text

            #add to dataList uma lista com dois dados, nome e cnpj
            #dataList.append([nome, cnpj])

            cnpj = cnpj[6:]
            data = {
            'nome': nome,
            'cnpj': cnpj,
            'url': 'https://cnpj.biz/'
            }
            response = requests.post(url, data=data)


            time.sleep(4)

            navegador.back()
    except :
        break
        
""""
print(dataList)
#atribui meu endpoint do appscript para uma variavel
url = 'https://script.google.com/macros/s/AKfycbwnxwJNc9Qunl0ghreKJae8vv_hMmfrwb7_ZaivbY3vVFfy-MX_0J9qVZ2bthd0xsoK/exec'


#para cada item na minha lista 
for item in dataList:
    #tira o parte : cnpj: antes do cnpj/numero 
    item[1]= item[1][6:]
    #cria um dictionary python com os dados
    data = {
    'nome': item[0],
    'cnpj': item[1],
    'url': 'https://cnpj.biz/'
}
    response = requests.post(url, data=data)
    

"""
