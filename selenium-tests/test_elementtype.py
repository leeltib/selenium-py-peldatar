# 010 Feladat: Selenium findby elágazásokkal

from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
#driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://localhost:9999/trickyelements.html')

test_elements = []
for i in range(5):
    k = str(i + 1)
    element = driver.find_element_by_id("element" + k)
    test_elements.append(element)

# print(elements)
test_sorszam = 0
for test_elem in test_elements:
    test_sorszam += 1
    test_elem.click()
    test_result = driver.find_element_by_xpath('//label[@id="result"]')
    if test_result.text == f"{test_elem.text} was clicked":
        print(f"Az első button típusú elemünk: {test_elem.text}.")
        print("Az elemek listája alatti szöveg helyes.")
        break
    elif test_result.text == "[Click any button]":
        print(f"A(z) {test_sorszam}. elem nem gomb.")
    else:
        print(f"Az első button típusú elemünk: {test_elem.text}.")
        print("Az elemek listája alatti szöveg viszont helytelen.")
        break


