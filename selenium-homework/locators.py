# 013 Feladat: Lokátorok gyakorlása

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://localhost:9999/kitchensink.html')

# keresés ID alapján -------------------------------
chbox_exam_bmw = driver.find_element_by_id('bmwcheck')
chbox_exam_benz = driver.find_element_by_id('benzcheck')
chbox_exam_honda = driver.find_element_by_id('hondacheck')
# ellenőrzés
chbox_exam_bmw.click()
chbox_exam_benz.click()
chbox_exam_honda.click()
print("Keresés ID alapján. Elvárt eredmény:")
print("A Checkbox Example oszlopban mindhárom autónév mellett pipa van.")


# keresés NAME alapján -------------------------------
search_name = driver.find_elements_by_name('cars')

# ellenőrzés
for elem in search_name[1:3]:
    elem.click()
print('*' * 50)
print("Keresés NAME alapján. Elvárt eredmény:")
print("A Radio Button Example oszlopban a Honda autónév mellett pipa van.")
print('*' * 50)

# keresés XPath kifejezéssel  -------------------------------

back_link = driver.find_element_by_xpath("/html/body/div[1]/a")
print("Keresés XPath kifejezéssel-1")
print(back_link.text)
print('*' * 50)
# ellenőrzés
back_link.click()
time.sleep(1.0)
driver.back()


mouse_hov = driver.find_element_by_xpath('//button[@id="mousehover"]')
print("Keresés XPath kifejezéssel-2")
print(mouse_hov.text)
print('*' * 50)
# ellenőrzés
mouse_hov.click()


action_del = driver.find_element_by_xpath('//table[@id="product"]/tbody/tr[3]/td[4]/button')
print("Keresés XPath kifejezéssel-3")
print(action_del.text)
print('*' * 50)
# ellenőrzés
action_del.click()
