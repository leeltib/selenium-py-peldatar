# 011 Feladat: selenium táblázatok gyakorlása
# hasznos oldal: https://www.geeksforgeeks.org/rect-element-method-selenium-python/?ref=rp

from selenium import webdriver
import pprint
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager               # webdriver-manager / Chrome

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
driver = webdriver.Chrome(ChromeDriverManager().install())                              # normál mód

driver.get("http://localhost:9999/editable-table.html")

# készítünk egy függvényt a táblázat tartalmának kiolvasására
def cont_table(ed):
    table = driver.find_element_by_xpath("//table[@class='table table-bordered']//tbody")
    rows = table.find_elements_by_tag_name('tr')
    for row in rows:                                    # kulcs-érték párokban kiírjuk a látható táblázat tartalmát
        data_row = {}
        cells = row.find_elements_by_tag_name('td')
        cells0 = cells[0].find_element_by_tag_name('input')
        data_row["name"] = cells0.get_attribute('value')
        cells1 = cells[1].find_element_by_tag_name('input')
        data_row["price"] = cells1.get_attribute('value')
        cells2 = cells[2].find_element_by_tag_name('input')
        data_row["quantity"] = cells2.get_attribute('value')
        cells3 = cells[3].find_element_by_tag_name('input')
        data_row["category"] = cells3.get_attribute('value')
        ed.append(data_row)

extracted_data = []
cont_table(extracted_data)
#pprint.pprint(extracted_data)
#pprint.pprint(extracted_data[5])
row_num = len(extracted_data)
print('-' * 50)
print(f"Az eredeti táblázat {row_num} sort tartalmaz.")
print('-' * 50)

# felveszünk két új sort
add_button = driver.find_element_by_xpath('//div[@id="container"]/div/div[2]/button')
add_button.click()


#js = "var tr7 = document.getElementsByClassName('eachRow')[5]; var td1 = tr7.getElementsByTagName('td')[2]; var name = td1.querySelector('input'); name.value = 'bármi';"
#js = "document.evaluate('/html/body/div/div/div[1]/table/tbody/tr[4]/td[0]/input', document).value = 'bármi';"
js = "var tr7 = document.getElementsByClassName('eachRow')[5]; var td1 = tr7.getElementsByTagName('td')[2].firstElementChild.value = 'bármi';"


driver.execute_script(js)
add_button.click()


extracted_data2 = []
cont_table(extracted_data2)
#pprint.pprint(extracted_data2)
pprint.pprint(extracted_data2[6:])
row_num2 = len(extracted_data2)
print('-' * 50)
print(f"A bővített táblázat {row_num2} sort tartalmaz.")
print('-' * 50)



