# 017 Feladat: Navigációs feladatok

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://localhost:9999/general.html')

links = driver.find_elements_by_xpath('//body//a')
link_num1 = len(links)
print("-" * 80)
print(f"Ezen az oldalon összesen {link_num1} link található.")
print("-" * 80)

row = 0
for link in links:
    row += 1
    href_text = link.get_attribute('href')
    print(f"{row}. link:", href_text, ", a link szövege:", link.text)

print("*" * 80)
print("         A LINKEK VIZSGÁLATA")
print("-" * 80)

row = 0
for link in links:
    row += 1
    href_text = link.get_attribute('href')
    target_text = link.get_attribute('target')
#    print(target_text)
    print(f"{row}. link:", href_text, ", a link szövege:", link.text)
    if href_text == 'http://www.w3schools.com/tags/' or href_text == 'http://example.com/' or href_text == 'https://www.fillmurray.com/' or href_text == 'https://creativecommons.org/licenses/by-sa/3.0' or href_text == 'https://commons.wikimedia.org/wiki/File:What_hath_God_wrought.ogg':
        print(' "CSALTAM"!!!   Itt még VALAMI GOND VAN..., kezelni kell :)')
        print("-" * 80)
        continue
    elif target_text == "_blank":
        link.click()
        print("         Ez a link új böngészőablakot nyit, abban kell vizsgálni.")
        brow_text = driver.current_url
        if href_text == brow_text:
            print("         A link megfelelően működik.")
            print("-" * 80)
        else:
            print("         A link NEM megfelelően műkodik.")
            print("-" * 80)
        time.sleep(1.0)
        driver = webdriver.Chrome()
        driver.get('http://localhost:9999/general.html')
    else:
        link.click()
        brow_text = driver.current_url
        if href_text == brow_text:
            print("         Ez a link megfelelően működik.")
            print("-" * 80)
        else:
            print("         Ez a link NEM megfelelően műkodik.")
            print("-" * 80)
        time.sleep(0.5)
        driver.back()

driver.close()


