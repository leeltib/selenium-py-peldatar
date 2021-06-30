# 011 Feladat: selenium táblázatok gyakorlása
# Az újonnan bevitt adatok mellett a DOM struktúra is át lett írva...


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

# *******************************************************************************************************
# FELADAT-1 : Addj hozzá még két teljsen kitöltött sort. Ellenőrizd, hogy tényleg hozzáadódtak-e a sorok.

# függvény a táblázat teljes tartalmának kiolvasására:
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
row_num = len(extracted_data)
print('-' * 10, " ÚJ SOROK FELVÉTELE ", '-' * 18)
print('-' * 50)
print(f"Az eredeti táblázat {row_num} sort tartalmaz.")
print('-' * 50)

# függvény bármelyik, tetszőleges mező értékének lekérdezéséhez:
def data_table(row, cell):
    table = driver.find_element_by_xpath("//table[@class='table table-bordered']//tbody")
    rows = table.find_elements_by_tag_name('tr')
    cells = rows[row-1].find_elements_by_tag_name('td')
    element = cells[cell-1].find_element_by_tag_name('input')
    value_table = element.get_attribute('value')
    print(value_table)

# függvény bármelyik, tetszőleges mező értékének módosításához -> a DOM struktúra módosításával együtt:
def edit_data(row, cell, val):
    table = driver.find_element_by_xpath("//table[@class='table table-bordered']//tbody")
    rows = table.find_elements_by_tag_name('tr')
    cells = rows[row - 1].find_elements_by_tag_name('td')
    el_edit = cells[cell-1].find_element_by_tag_name('input')
    el_edit.clear()
    el_edit.send_keys(val)                                                           # Ez írja ki a táblázatba...
    driver.execute_script(f"arguments[0].setAttribute('value', '{val}')", el_edit)   # Ez a sor módosítja a DOM-ban megadott értéket!!!

# felveszünk két új sort, és kitöltjük őket
add_button = driver.find_element_by_xpath('//div[@id="container"]/div/div[2]/button')
add_button.click()

edit_data(7, 1, "samsungA10")
edit_data(7, 2, "90.50")
edit_data(7, 3, "5")
edit_data(7, 4, "Electronics")

add_button.click()

edit_data(8, 1, 'LG Smart TV')
edit_data(8, 2, '105.90')
edit_data(8, 3, '2')
edit_data(8, 4, 'Electronics')

extracted_data2 = []
cont_table(extracted_data2)
#pprint.pprint(extracted_data2)
row_num2 = len(extracted_data2)

print(f"A bővített táblázat {row_num2} sort tartalmaz.")
print('-' * 50)

# tartalom ellenörzése:
try:
    assert((extracted_data2[6]['name']) == 'samsungA10')
    assert((extracted_data2[6]['price']) == '90.50')
    assert((extracted_data2[6]['quantity']) == '5')
    assert((extracted_data2[6]['category']) == 'Electronics')
    assert((extracted_data2[7]['name']) == 'LG Smart TV')
    assert((extracted_data2[7]['price']) == '105.90')
    assert((extracted_data2[7]['quantity']) == '2')
    assert((extracted_data2[7]['category']) == 'Electronics')
    print("Az új adatok felvétele OK!")
except:
    print("Az új adatok felvétele nincs rendben, az adatok nem megfelelően jelentek meg a táblázatban!")

print('-' * 50)
time.sleep(3)

# *******************************************************************************************************
# FELADAT-3 :  Írd át a táblázat egyes celláit és ellenőrizd, hogy megfelelően frissült-e a DOM struktúra.

print('-' * 10, " MEGLÉVŐ ADATOK MÓDOSÍTÁSA ", '-' * 21)
print('-' * 60)
print("Eredeti adatok:")
data_table(5, 1)
data_table(5, 3)

edit_data(5, 1, "iPhone 6")
edit_data(5, 3, "7")

print('-' * 60)
print("Módosítás utáni adatok:")
data_table(5, 1)
data_table(5, 3)

extracted_data4 = []
cont_table(extracted_data4)

# a táblázat tartalmának ellenörzése:
print('-' * 60)
try:
    assert((extracted_data4[4]['name']) == 'iPhone 6')
    assert((extracted_data4[4]['quantity']) == '7')
    print("Módosítás OK!")
except:
    print("Hiba! Az eredeti adat nem módosult!")

print('-' * 60)
time.sleep(4)

# *******************************************************************************************************
# FELADAT-2 : Ellenőrizd a kereső funkciót.

driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/input').send_keys('baseball')

extracted_data3 = []
cont_table(extracted_data3)
row_num3 = len(extracted_data3)
print('-' * 10, " KERESŐ FUNKCIÓ ELLENŐRZÉSE ", '-' * 12)
print('-' * 52)
print(f"Keresés után a táblázat {row_num3} sort tartalmaz.")
print('-' * 52)

# tartalom ellenörzése:
try:
    assert((extracted_data3[0]['name']) == 'baseball')
    assert((extracted_data3[0]['price']) == '9.99')
    assert((extracted_data3[0]['quantity']) == '15')
    assert((extracted_data3[0]['category']) == 'Sporting Goods')
    print("A keresés után a megfelelő tartalom jelenik meg.")
except:
    print("A kereső funkció hibásan működik!")

time.sleep(4)
driver.close()
