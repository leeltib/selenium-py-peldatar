from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://fonts.google.com/')

q = driver.find_element_by_id('mat-input-0')
q.send_keys('Anton')

submit = driver.find_element_by_xpath("//h1[contains(@class,'mat-text--title gmat-headline-6')]")
submit.click()

driver.close()


# fontkereső függvény
font = input("Melyik fontot szeretnéd megnézni? (pl. Asul) ")

driver = webdriver.Chrome()
driver.get('https://fonts.google.com/')

q = driver.find_element_by_id('mat-input-0')
q.send_keys(font)

submit = driver.find_element_by_xpath(f"//h1[contains(text(),'{font}')]")
submit.click()

# driver.close()


# megnyitás Firefox-ban

driver = webdriver.Firefox()
driver.get('https://fonts.google.com/')

q = driver.find_element_by_id('mat-input-0')
q.send_keys('Allan')

submit = driver.find_element_by_xpath("//h1[contains(text(),'Allan')]")
submit.click()

driver.close()
