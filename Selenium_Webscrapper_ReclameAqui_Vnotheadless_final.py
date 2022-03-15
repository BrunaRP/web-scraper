from operator import length_hint
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import unittest
import csv

driver = webdriver.Chrome()
i=1
# Used in google sheets to create list: ="['"&textjoin("','",1,A2:A)&"']" - without header
line = ['gutscheinsammler','gutegutscheine','audilo','bonial','bulonescoiro','cecilhagelstam','maxxilub','the-border','vecchietti','hiperportugal','irr','ipc-concarneau','akateeminen','brookstone','freeshipping','mali-vragci','nakupek','simplyaudiobooks','deadlydragonsound','vapesbyenushi','bionairecanada','badlands','resinpro','slando','europosters','freerideboardshop','spearitco','tradetang','kentmodels','amaten','ourgreenhouse','moinat','pop-addiction','reizentolo','time4wahmoms','antik','mrmuffinstrains','andromedaspop','wilesco-shop','marktplaza','okluma','levergear','mirage','lotteshopping','myhanil']

nome_list = []
nota_list = []
reclamacoes_list = []
respondidas_list = []
visualizacoes_list = []
indicesolucao_list = []
notaconsumidor_list = []

for i in range(length_hint(line)):
    driver.get("http://www.google.com")
    element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.NAME, "q")))

    searchField = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    searchField.send_keys('reclame aqui ' + line[i])
    searchField.submit()
    print (line[i])
    try:
        button = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/a/h3')
    except NoSuchElementException:
        nome = ''
        nota = ''
        reclamacoes = ''
        respondidas = ''
        visualizacoes = ''
        indicesolucao = ''
        notaconsumidor = ''
        nome_list.append(nome)
        nota_list.append(nota)
        reclamacoes_list.append(reclamacoes)
        respondidas_list.append(respondidas)
        visualizacoes_list.append(visualizacoes)
        indicesolucao_list.append(indicesolucao)
        notaconsumidor_list.append(notaconsumidor)
        continue
    button.click()
    # button = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3') \\ na pagina com algo do lado
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3"))).click()

    url = driver.current_url
    driver.get(url)
    try:
        nome = driver.find_element_by_xpath('//*[@id="hero"]/div[2]/div/div[2]/div[1]/h1').text
    except NoSuchElementException:
        nome = '--'
    try:
        nota = driver.find_element_by_xpath('//*[@id="reputation"]/div[1]/div[1]/div[2]/span[2]/b').text
    except NoSuchElementException:
        nota = '--'
    try:
        reclamacoes = driver.find_element_by_xpath('//*[@id="reputation"]/div[1]/div[2]/a[1]/div/div/b').text
    except NoSuchElementException:
        reclamacoes = '--'
    try:
        respondidas = driver.find_element_by_xpath('//*[@id="reputation"]/div[1]/div[2]/a[2]/div/div/b').text
    except NoSuchElementException:
        respondidas = '--'
    try:
        visualizacoes = driver.find_element_by_xpath('//*[@id="hero"]/div[2]/div/div[2]/div[2]/div/div/a').text
    except:
        visualizacoes = '--'
    try:
        indicesolucao = driver.find_element_by_xpath('//*[@id="reputation"]/div[2]/div[1]/div[3]/span').text 
    except NoSuchElementException:
        indicesolucao = '--'
    try:
        notaconsumidor = driver.find_element_by_xpath('//*[@id="reputation"]/div[2]/div[1]/div[4]/span').text 
    except NoSuchElementException:
        notaconsumidor = '--' 

    nome_list.append(nome)
    nota_list.append(nota)
    reclamacoes_list.append(reclamacoes)
    respondidas_list.append(respondidas)
    visualizacoes_list.append(visualizacoes)
    indicesolucao_list.append(indicesolucao)
    notaconsumidor_list.append(notaconsumidor)

    myData = [line,nome_list, nota_list, reclamacoes_list, respondidas_list,visualizacoes_list,indicesolucao_list,notaconsumidor_list]
    myFile = open('lead_list_enriched_ecommerce4.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)

print (nome_list)
print (nota_list)
print (reclamacoes_list)
print (respondidas_list)

# class Test(unittest.TestCase):

#     def test_write_csv_file(self):
#         myData = [line,nome_list, nota_list, reclamacoes_list, respondidas_list,visualizacoes_list,indicesolucao_list,notaconsumidor_list]
#         myFile = open('lead_list_enriched_startups_investors3.csv', 'w')
#         with myFile:
#            writer = csv.writer(myFile)
#            writer.writerows(myData)

# if __name__ == "__main__":
#     unittest.main()