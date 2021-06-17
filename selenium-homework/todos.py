# 015 Feladat: Selenium adat kinyeréses feladatok

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://localhost:9999/todo.html')

articels = driver.find_elements_by_xpath("//ul//span[@class='done-false']")

row = 0
for articel in articels:
    row += 1
    print(f"{row}. aktív bejegyzés: ", articel.text)


# Ha kikapcsolunk bejegyzéseket:
but_off1 = driver.find_element_by_xpath("/html/body/div/div/div/ul/li[2]/input")
but_off2 = driver.find_element_by_xpath("/html/body/div/div/div/ul/li[4]/input")
but_off1.click()
but_off2.click()

print('*' * 50)
print("Ha érvénytelenítünk két sort:")
articels = driver.find_elements_by_xpath("//ul//span[@class='done-false']")

row = 0
for articel in articels:
    row += 1
    print(f"{row}.  aktív bejegyzés: ", articel.text)