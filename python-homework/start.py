from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://fonts.google.com/')

keres = driver.find_element_by_id('mat-input-0')
keres.send_keys('Anton')

submit = driver.find_element_by_xpath("//h1[contains(@class,'mat-text--title gmat-headline-6')]")
submit.click()

# driver.close()
