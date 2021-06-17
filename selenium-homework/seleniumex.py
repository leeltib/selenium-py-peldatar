from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://fonts.google.com/')

def search(font_type):
    try:
        q = driver.find_element_by_id(font_type)
    except:
        print("Nincs az oldalon ilyen elem.")

keres = 'nemletezik'
search(keres)

driver.close()


# font keresés hibakezeléssel kiegészítve

def search2(font_type):
    try:
        q = driver.find_element_by_id('mat-input-0')
        q.send_keys(font_type)
        submit = driver.find_element_by_xpath(f"//h1[contains(text(),'{font_type}')]")
        submit.click()
        print("A keresés sikeres, az oldal megnyitva!")
    except:
        print("Nincs az oldalon ilyen elem.")

font = input("Milyen nevű fontot keresel? (pl. Asul?) ")

driver = webdriver.Chrome()
driver.get('https://fonts.google.com/')

search2(font)