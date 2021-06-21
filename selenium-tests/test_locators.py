# 013 Feladat: Lokátorok gyakorlása

from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
#driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://localhost:9999/kitchensink.html')

# keresés ID alapján -------------------------------
test_chbox_exam_bmw = driver.find_element_by_id('bmwcheck')
test_chbox_exam_benz = driver.find_element_by_id('benzcheck')
test_chbox_exam_honda = driver.find_element_by_id('hondacheck')
# ellenőrzés
test_chbox_exam_bmw.click()
test_chbox_exam_benz.click()
test_chbox_exam_honda.click()
print("Keresés ID alapján. Elvárt eredmény:")
print("A Checkbox Example oszlopban mindhárom autónév mellett pipa van.")


# keresés NAME alapján -------------------------------
test_search_name = driver.find_elements_by_name('cars')

# ellenőrzés
for elem in test_search_name[1:3]:
    elem.click()
print('*' * 50)
print("Keresés NAME alapján. Elvárt eredmény:")
print("A Radio Button Example oszlopban a Honda autónév mellett pipa van.")
print('*' * 50)

# keresés XPath kifejezéssel  -------------------------------

test_back_link = driver.find_element_by_xpath("/html/body/div[1]/a")
print("Keresés XPath kifejezéssel-1")
print(test_back_link.text)
print('*' * 50)
# ellenőrzés
test_back_link.click()
time.sleep(1.0)
driver.back()


test_mouse_hov = driver.find_element_by_xpath('//button[@id="mousehover"]')
print("Keresés XPath kifejezéssel-2")
print(test_mouse_hov.text)
print('*' * 50)
# ellenőrzés
test_mouse_hov.click()


test_action_del = driver.find_element_by_xpath('//table[@id="product"]/tbody/tr[3]/td[4]/button')
print("Keresés XPath kifejezéssel-3")
print(test_action_del.text)
print('*' * 50)
# ellenőrzés
test_action_del.click()

driver.close()

