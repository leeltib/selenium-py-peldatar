# 015 Feladat: Selenium adat kinyeréses feladatok

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
#driver = webdriver.Chrome(ChromeDriverManager().install())                              # normál mód

driver.get('http://localhost:9999/todo.html')

articels1 = driver.find_elements_by_xpath("//ul//span[@class='done-false']")

def test_func_todos():
    row = 0
    for artic in articels1:
        row += 1
        szoveg = artic.text
        print(f"{row}. aktív bejegyzés: {szoveg}")

# Ha kikapcsolunk bejegyzéseket:
but_off1 = driver.find_element_by_xpath("/html/body/div/div/div/ul/li[2]/input")
but_off2 = driver.find_element_by_xpath("/html/body/div/div/div/ul/li[4]/input")
but_off1.click()
but_off2.click()

articels2 = driver.find_elements_by_xpath("//ul//span[@class='done-false']")

def test_func_todos2():
    row = 0
    for artic2 in articels2:
        row += 1
        szoveg2 = artic2.text
        print(f"{row}. aktív bejegyzés: {szoveg2}")

test_func_todos()
print('*' * 50)
print("Ha érvénytelenítünk két sort:")
test_func_todos2()

driver.close()


