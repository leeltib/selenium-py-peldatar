# 017 Feladat: Navigációs feladatok - 2. megoldás

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
driver = webdriver.Chrome(ChromeDriverManager().install())                                # normál mód

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
    print(f"{row}. link:", href_text, f', a link szövege: "{link.text}"')

print("*" * 85)
print("    A LINKEK VIZSGÁLATA. A # linkeket nem vizsgáljuk. Marad 20 db vizsgálandó link.")
print("-" * 85)

# összehasonlító függvény
def exam(href_text):
    brow_text = driver.current_url
    if href_text[-1] == "/" and brow_text[-1] != "/":
        brow_text += "/"
    if href_text[-1] != "/" and brow_text[-1] == "/":
        href_text += "/"
    if href_text[-7:] == brow_text[-7:]:
        print("    URL:", brow_text)
        print("         A link megfelelően működik.")
        print("-" * 80)
    else:
        print("    URL:", brow_text)
        print("         A link NEM megfelelően műkodik.")
        print("-" * 80)
    time.sleep(1.0)

row = 0
for i in range(len(links)):
    link = driver.find_elements_by_xpath("//a")[i]
    if link.text == '#':
        continue
    row += 1
    href_text = link.get_attribute('href')
    target_text = link.get_attribute('target')
    print(f'{row}. link: "{link.text}"')
    print("   link:", href_text)
    if target_text == "_blank":                                                     # nyitás új ablakban (program szerint)
        main_window = driver.window_handles[0]
        link.click()
        time.sleep(1)
        other_window = driver.window_handles[1]
        driver.switch_to.window(other_window)
        print("         Ez a link új fülön nyilik meg, abban kell vizsgálni.")
        exam(href_text)
        driver.close()
        driver.switch_to.window(main_window)
    else:                                                                          # saját oldalon belüli navigáció vagy az alap oldal helyére nyíló linkek
        link.click()
        exam(href_text)
        driver.back()

driver.close()
