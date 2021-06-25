# 009 Feladat: selenium dátum mezők gyakorlása

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

driver.get("http://localhost:9999/forms.html")

nowutc = datetime.now(timezone.utc)
print(nowutc)
nowutc_d = nowutc.date()
print(nowutc_d)

date_d1 = date(2021, 6, 5)
date_d2 = datetime(2012, 5, 5, 5, 5, 5)
date_d3 = datetime(2000, 5, 12)
date_d4 = datetime(1995, 12, 6)
date_d5 = datetime(2015, 12, 28)
date_d6 = datetime(2015, 12, 28, 12, 25, 32)


print('A kötött megjelenés miatt a feladatkiírásban kért formátumok nem kivitelezhetők.')
print('Ezen felül: hibás működésű a dátum kitöltő -> 6 karaktert ír az első mezőbe -> a "00"-val kiütöm az első két karaktert, és utána jó...')
driver.find_element_by_id("example-input-date").send_keys('00' + date_d1.strftime("%Y/%m/%d"))
driver.find_element_by_id("example-input-date-time").send_keys(date_d2.strftime("%Y.%m.%d. %H:%M:%S:555"))
driver.find_element_by_id("example-input-date-time-local").send_keys('00' + date_d3.strftime("%Y/%m/%d") + '1201')
driver.find_element_by_id("example-input-month").send_keys('00' + date_d4.strftime("%Y" + 'd'))
driver.find_element_by_id("example-input-week").send_keys(date_d5.strftime("%W" + '00' + "%Y"))
driver.find_element_by_id("example-input-time").send_keys(date_d6.strftime("%H:%M"))

time.sleep(6)
driver.close()


