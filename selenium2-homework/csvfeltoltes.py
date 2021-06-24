# 006 Feladat: Űrlap automatizálás fájlból

import csv
from selenium import webdriver
from datetime import datetime, timezone, date
import time


from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
driver = webdriver.Chrome(ChromeDriverManager().install())                              # normál mód

driver.get("http://localhost:9999/another_form.html")


def find_and_clear_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element

add_button = driver.find_element_by_id("submit")

filename = "table2_in.csv"
with open(filename, "r", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
#        print(row)
        find_and_clear_by_id("fullname").send_keys(row[0])
        find_and_clear_by_id("email").send_keys(row[1])
        dob = find_and_clear_by_id("dob")
        date_str = row[2]
        date_form = date_str.replace("-", "").replace("-", "")
        dob.send_keys(date_form)
        find_and_clear_by_id("phone").send_keys(row[3])

        add_button.click()

time.sleep(2)
add_button_exp = driver.find_element_by_xpath("/html/body/main/div/button")
add_button_exp.click()
time.sleep(5)

filename2 = "table2_in.csv"
with open(filename2, "r", encoding='utf-8') as csvfile2:
    reader2 = csv.reader(csvfile2, delimiter=',')
    next(reader2)
    reader2_data = list(reader2)
    print(reader2_data)

filename3 = "C:\\Users\\Tibor\\Downloads\\table.csv"
with open(filename3, "r", encoding='utf-8') as csvfile3:
    reader3 = csv.reader(csvfile3, delimiter=',')
    next(reader3)
    reader3_data = list(reader3)
    print(reader3_data)

if reader2_data == reader3_data:
    print("A művelet sikeres, az adatok egyeznek.")
else:
    print("Eltérés van az eredeti és a visszajövő adatok között!")

driver.close()

