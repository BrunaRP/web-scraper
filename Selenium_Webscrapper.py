from operator import length_hint
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest
import csv

driver = webdriver.Chrome()
i=1
# Used in google sheets to create list: ="['"&textjoin("','",1,A2:A)&"']" - without header
line = ['lacadordeofertas','abracadabra','infostore','carvalhoshop']
# with open("leadlist2.csv") as fp:
#     line = fp.readlines()

nome_list = []
nota_list = []

for i in range(length_hint(line)):
    driver.get("http://www.google.com")
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "q")))

    searchField = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    searchField.send_keys('reclame aqui ' + line[i])
    searchField.submit()
    
    try:
        button = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/a/h3')
    except NoSuchElementException:
        nome = ''
        nota = ''
        nome_list.append(nome)
        nota_list.append(nota)
        
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

   

    nome_list.append(nome)
    nota_list.append(nota)
    
print (nome_list)
print (nota_list)

class Test(unittest.TestCase):

    def test_write_csv_file(self):
        myData = [line,nome_list, nota_list]
        myFile = open('lead_list_enriched.csv', 'w')
        with myFile:
           writer = csv.writer(myFile)
           writer.writerows(myData)

if __name__ == "__main__":
    unittest.main()