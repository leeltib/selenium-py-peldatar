# 017 Feladat: komplett űrlap tesztelés

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains          # a dupla click-hez kell...
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
driver = webdriver.Chrome(ChromeDriverManager().install())                              # normál mód

driver.get("http://localhost:9999/simplevalidation.html")

# input mezők kijelölése, listába írása függvény:
def find_el():
    inp_1 = driver.find_element_by_id("test-email")                     # mail cím
    inp_list.append(inp_1)
    inp_2 = driver.find_element_by_id("test-password")                  # jelszó
    inp_list.append(inp_2)
    inp_3 = driver.find_element_by_id("test-confirm-password")          # jelszó újra
    inp_list.append(inp_3)
    inp_4 = driver.find_element_by_id("test-customer-number")           # ügyfélszám
    inp_list.append(inp_4)
    inp_5 = driver.find_element_by_id("test-dealer-number")             # eladó száma
    inp_list.append(inp_5)
    inp_6 = driver.find_element_by_id("test-random-field")              # opcionális : "twelve" vagy semmi..
    inp_list.append(inp_6)
    inp_7 = driver.find_element_by_id("test-date-field")                # dátum
    inp_list.append(inp_7)
    inp_8 = driver.find_element_by_id("test-url-field")                 # URL
    inp_list.append(inp_8)
    inp_9 = driver.find_element_by_id("test-random-textarea")           # tetszőleges szöveg...
    inp_list.append(inp_9)
    inp_10 = driver.find_element_by_id("test-card-number")              # kártya szám
    inp_list.append(inp_10)
    inp_11 = driver.find_element_by_id("test-card-cvv")                 # cvv szám
    inp_list.append(inp_11)


# függvény az input mezők feltöltéséhez
def data_upl(tc, inp):
    if len(tc) == len(inp):
        r_num = len(tc)
        for i in range(r_num):
            elem = inp[i]
            act_data = tc[i]
            elem.clear()
            elem.send_keys(act_data)
    else:
        print("Hiba! A megadott két lista elemszáma nem azonos!")


# függvény checkbox kapcsolókhoz:
def chbox_full(a, b, c, d):
    if a == 1:              # a=1 -> chbox_1 bekapcs
        chbox_1.click()
    if b == 1:              # b=1 -> yes bekapcs
        chbox_2.click()
    if b == 2:              # b=2 -> no bekapcs
        chbox_3.click()
    if c == 1:              # c=1 -> chbox_4 bekapcs
        chbox_4.click()
    if d == 1:              # d=1 -> chbox_5 bekapcs
        chbox_5.click()
    else:
        pass

# függvény a selectiv mezők kiválasztásához
def sel_inp(a, av, b, bv, c, cv):
    if a == sel_1 and 2 <= av <= 5:    # sel_1 lehetséges értéke: (av) 2-5
        driver.find_element_by_xpath(f'//*[@id="test-card-type"]/option[{av}]').click()
    if b == sel_2 and 2 <= bv <= 13:   # sel_2 lehetséges értéke: (bv) 2-13
        driver.find_element_by_xpath(f'//*[@id="test-card-month"]/option[{bv}]').click()
    if c == sel_3 and 2 <= cv <= 11:   # sel_3 lehetséges értéke: (cv) 2-11
        driver.find_element_by_xpath(f'//*[@id="test-card-year"]/option[{cv}]').click()
    else:
        print("Rossz adatokat adtál meg, nincs ilyen kiválasztható elem.")


# input mezők hibaüzenet szövegei helyének kijelölése, listába írása (függvénnyel):
val_list = []
def valid_list():
    val_1 = driver.find_element_by_xpath("/html/body/div/form/div[2]/div[2]")
    val_list.append(val_1)
    val_2 = driver.find_element_by_xpath("/html/body/div/form/div[3]/div[2]")
    val_list.append(val_2)
    val_3 = driver.find_element_by_xpath("/html/body/div/form/div[4]/div[2]")
    val_list.append(val_3)
    val_4 = driver.find_element_by_xpath("/html/body/div/form/div[5]/div[2]")
    val_list.append(val_4)
    val_5 = driver.find_element_by_xpath("/html/body/div/form/div[6]/div[2]")
    val_list.append(val_5)
    val_6 = driver.find_element_by_xpath("/html/body/div/form/div[7]/div[2]")
    val_list.append(val_6)
    val_7 = driver.find_element_by_xpath("/html/body/div/form/div[8]/div[2]")
    val_list.append(val_7)
    val_8 = driver.find_element_by_xpath("/html/body/div/form/div[9]/div[2]")
    val_list.append(val_8)
    val_9 = driver.find_element_by_xpath("/html/body/div/form/div[10]/div[2]")
    val_list.append(val_9)
    val_10 = driver.find_element_by_xpath("/html/body/div/form/div[12]/div[2]")
    val_list.append(val_10)
    val_11 = driver.find_element_by_xpath("/html/body/div/form/div[13]/div[2]")
    val_list.append(val_11)

# elvárt hibaüzenetek alap listája - input mezők:
v_text_list = []
def text_list_gen_inp():
    v_text_inp1 = ['E-Mail Address', "Please enter an e-mail"]
    v_text_list.append(v_text_inp1)
    v_text_inp2 = ['Desired Password', "This field can't be empty"]
    v_text_list.append(v_text_inp2)
    v_text_inp3 = ['Confirm Password', "Please complete Desired Password"]
    v_text_list.append(v_text_inp3)
    v_text_inp4 = ['Customer Number', "This field can't be empty"]
    v_text_list.append(v_text_inp4)
    v_text_inp5 = ['Dealer Number', "This field can't be empty"]
    v_text_list.append(v_text_inp5)
    v_text_inp6 = ['Random Field', 'Should contain "twelve"']
    v_text_list.append(v_text_inp6)
    v_text_inp7 = ['Date Field', "This field can't be empty"]
    v_text_list.append(v_text_inp7)
    v_text_inp8 = ['URL Field', 'Please enter a valid URL (starts with "http" or "https")']
    v_text_list.append(v_text_inp8)
    v_text_inp9 = ['Random Textarea', "This field can't be empty"]
    v_text_list.append(v_text_inp9)
    v_text_inp10 = ['Card Number', "Please enter a credit card number (no spaces)"]
    v_text_list.append(v_text_inp10)
    v_text_inp11 = ['Card CVV (on back or card)', "This field can't be empty"]
    v_text_list.append(v_text_inp11)

# elvárt hibaüzenetek alap listája - select kiválasztók:
v_text_list_sel = []
v_text_sel_1 = ['Card Type', "Please select a card type"]
v_text_list_sel.append(v_text_sel_1)
v_text_sel_2 = ['Expiration Month', "Select a month"]
v_text_list_sel.append(v_text_sel_2)
v_text_sel_3 = ['Expiration Year', "Select a year"]
v_text_list_sel.append(v_text_sel_3)

# elvárt hibaüzenetek alap listája - checkbox-ok:
v_text_list_box = []
v_text_chbox_1 = ['Just a regular single checkbox', "This field can't be empty"]
v_text_list_box.append(v_text_chbox_1)
v_text_chbox_23 = ['Receive E-Mail Updates?', "v"]
v_text_list_box.append(v_text_chbox_23)
v_text_chbox_45 = ['Agree to...', "Please agree to both to continue"]
v_text_list_box.append(v_text_chbox_45)


# kiértékelő függvény - input mezők
def valid(va, vt):
    r_num = int(len(va))
#    print(r_num)
    try:
        for i in range(r_num):
            elem = va[i]
            el_name = vt[i][0]
            tex = vt[i][1]
            if elem.text == tex:
                print(f"{el_name}: validálás OK")
            else:
                print(f"{el_name}: nincs megfelelő validálás.")
    except:
        print("Nem definiált hiba.")
    finally:
        pass

# tesztadatok beolvasása, listába rendezése különálló txt fájlból
with open('data017.txt', 'r', encoding='utf-8') as file:
    tc_full = file.readlines()

tc_list_full = []
for el in tc_full[1::2]:
    tc_list_full.append(el.strip().split(","))

#print(tc_list_full)
#print(len(tc_list_full))

# adatfeltőltés-1  ->  alapeset, minden adat megfelelő
inp_list = []
find_el()
sel_1 = driver.find_element_by_id("test-card-type")                 # kártya típus (select)
sel_2 = driver.find_element_by_id("test-card-month")                # nónap (select)
sel_3 = driver.find_element_by_id("test-card-year")                 # év (select)
chbox_1 = driver.find_element_by_id("test-single-checkbox")         # checkbox
chbox_2 = driver.find_element_by_id("test-save-email-yes")          # checkbox
chbox_3 = driver.find_element_by_id("test-save-email-no")           # checkbox
chbox_4 = driver.find_element_by_id("test-terms-service")           # checkbox
chbox_5 = driver.find_element_by_id("test-terms-service-more")      # checkbox
su_button = driver.find_element_by_id("test-button")

tc_list = tc_list_full[0]
print(tc_list)

data_upl(tc_list, inp_list)
sel_inp(sel_1, 3, sel_2, 6, sel_3, 6)
chbox_full(1, 2, 1, 1)

try:
    su_button.click()
    msg = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@id='test-button' and @class='btn btn-primary btn-block']"))).get_attribute("data-jsv-form-tooltip")
    assert msg is not None
    assert msg == "Please complete all fields"
    time.sleep(1)
    print("Hiba az alapadatokban, nem sikerült a hibátlan kitöltés.")
except:
    print("Alapadatok OK, sikerült a hibátlan kitöltés.")
finally:
    pass
#    driver.close()


# ***********************************************************************
# *** TESZTESETEK *******************************************************

# TC-001
print("\nTC-001 teszteset:")
print("Annak vizsgálata, hogy minden input mezőhöz tartozik-e validálás,")
print("azaz hibás adatbevitelnél jelenik-e meg hibaüzenet:")

driver.refresh()
# beviteli mező lista létrehozása
inp_list = []
find_el()
sel_1 = driver.find_element_by_id("test-card-type")                 # kártya típus (select)
sel_2 = driver.find_element_by_id("test-card-month")                # hónap (select)
sel_3 = driver.find_element_by_id("test-card-year")                 # év (select)
chbox_1 = driver.find_element_by_id("test-single-checkbox")         # checkbox
chbox_2 = driver.find_element_by_id("test-save-email-yes")          # checkbox
chbox_3 = driver.find_element_by_id("test-save-email-no")           # checkbox
chbox_4 = driver.find_element_by_id("test-terms-service")           # checkbox
chbox_5 = driver.find_element_by_id("test-terms-service-more")      # checkbox

# aktuális tesztadat lista létrehozása
tc_list = tc_list_full[1]
print(tc_list)

# űrlap kitöltése
data_upl(tc_list, inp_list)
sel_inp(sel_1, 3, sel_2, 4, sel_3, 6)
chbox_full(1, 2, 1, 1)

# hibaüzenet helyek listája
val_list = []
valid_list()
# hibaüzenet szövegek listája
v_text_list = []
text_list_gen_inp()

# teszt futtatás
va = val_list
vt = v_text_list
valid(va, vt)


# -----------------------------------------------------------------------
# TC-002
print("\nTC-002 teszteset: első 3 input mező tesztelése")
print("1. e-mail cím @ karakter nélkül")
print("2. Rövid, 5 karakter hosszú password")
print("3. Az előzőtől eltérő (de egyébként megfelelő) password")

driver.refresh()
# beviteli mező lista létrehozása
inp_list = []
find_el()
sel_1 = driver.find_element_by_id("test-card-type")                 # kártya típus (select)
sel_2 = driver.find_element_by_id("test-card-month")                # hónap (select)
sel_3 = driver.find_element_by_id("test-card-year")                 # év (select)
chbox_1 = driver.find_element_by_id("test-single-checkbox")         # checkbox
chbox_2 = driver.find_element_by_id("test-save-email-yes")          # checkbox
chbox_3 = driver.find_element_by_id("test-save-email-no")           # checkbox
chbox_4 = driver.find_element_by_id("test-terms-service")           # checkbox
chbox_5 = driver.find_element_by_id("test-terms-service-more")      # checkbox

# aktuális tesztadat lista létrehozása
tc_list = tc_list_full[2]
print(tc_list)

# űrlap kitöltése
data_upl(tc_list, inp_list)
sel_inp(sel_1, 3, sel_2, 4, sel_3, 6)
chbox_full(1, 2, 1, 1)

# hibaüzenet helyek listája
val_list = []
valid_list()
# hibaüzenet szövegek listája
v_text_list = []
text_list_gen_inp()

# aktuálisan elvárt hibaüzenetek:
v_text_list[0][1] = 'Please check your E-Mail format'
v_text_list[1][1] = 'Should be between 6 and 20 characters'
v_text_list[2][1] = 'Please complete Desired Password'

# teszt futtatás
va = val_list[:3]
vt = v_text_list[:3]
valid(va, vt)


# -----------------------------------------------------------------------
# TC-003
print("\nTC-003 teszteset: első 3 input mező tesztelése")
print("1. e-mail cím . karakter nélkül")
print("2. Hosszú, 21 karakter hosszú password")
print("3. Az előzőtől eltérő (de egyébként megfelelő) password")

driver.refresh()
# beviteli mező lista létrehozása
inp_list = []
find_el()
sel_1 = driver.find_element_by_id("test-card-type")                 # kártya típus (select)
sel_2 = driver.find_element_by_id("test-card-month")                # hónap (select)
sel_3 = driver.find_element_by_id("test-card-year")                 # év (select)
chbox_1 = driver.find_element_by_id("test-single-checkbox")         # checkbox
chbox_2 = driver.find_element_by_id("test-save-email-yes")          # checkbox
chbox_3 = driver.find_element_by_id("test-save-email-no")           # checkbox
chbox_4 = driver.find_element_by_id("test-terms-service")           # checkbox
chbox_5 = driver.find_element_by_id("test-terms-service-more")      # checkbox

# aktuális tesztadat lista létrehozása
tc_list = tc_list_full[3]
print(tc_list)

# űrlap kitöltése
data_upl(tc_list, inp_list)
sel_inp(sel_1, 3, sel_2, 4, sel_3, 6)
chbox_full(1, 2, 1, 1)

# hibaüzenet helyek listája
val_list = []
valid_list()
# hibaüzenet szövegek listája
v_text_list = []
text_list_gen_inp()

# aktuálisan elvárt hibaüzenetek:
v_text_list[0][1] = 'Please check your E-Mail format'
v_text_list[1][1] = 'Should be between 6 and 20 characters'
v_text_list[2][1] = 'Please complete Desired Password'

# teszt futtatás
va = val_list[:3]
vt = v_text_list[:3]
valid(va, vt)


