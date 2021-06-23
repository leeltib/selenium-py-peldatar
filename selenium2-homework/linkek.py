# 001 Feladat: Python filekezelés feladatok

import csv
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
driver = webdriver.Chrome(ChromeDriverManager().install())                              # normál mód

driver.get("http://localhost:9999")

links = driver.find_elements_by_xpath("//body//a")
link_num = len(links)
print("-" * 80)
print(f"Ezen az oldalon összesen {link_num} link található.")
print("-" * 80)

with open("link_list.txt", "w", encoding='utf-8') as f:
    row = 0
    for link in links:
        row += 1
        href_text = link.get_attribute('href')
        f.write(f'{row}. link: "{href_text}", a link szövege: "{link.text}" \n')

