# 010 Feladat: Selenium findby elágazásokkal

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://localhost:9999/trickyelements.html')

elements = []
element1 = driver.find_element_by_id('element1')
elements.append(element1)
element2 = driver.find_element_by_id('element2')
elements.append(element2)
element3 = driver.find_element_by_id('element3')
elements.append(element3)
element4 = driver.find_element_by_id('element4')
elements.append(element4)
element5 = driver.find_element_by_id('element5')
elements.append(element5)

# print(elements)
sorszam = 0
for elem in elements:
    sorszam += 1
    elem.click()
    result = driver.find_element_by_xpath('//label[@id="result"]')
    if result.text == f"{elem.text} was clicked":
        print(f"Az első button típusú elemünk: {elem.text}.")
        print("Az elemek listája alatti szöveg helyes.")
        break
    elif result.text == "[Click any button]":
        print(f"A {sorszam}. elem nem gomb.")
    else:
        print(f"Az első button típusú elemünk: {elem.text}.")
        print("Az elemek listája alatti szöveg viszont helytelen.")
        break

