# 015 Feladat: felugró ablakok és tabok kezelése


from selenium import webdriver
from selenium.webdriver import ActionChains          # a dupla click-hez kell...
import time

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

#driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)       # Headless mód
driver = webdriver.Chrome(ChromeDriverManager().install())                              # normál mód

driver.get("http://localhost:9999/alert_playground.html")

# -----------------------------------------
# 1. Alert funkció:

try:
    driver.find_element_by_name('alert').click()
    ref_text = "I am alert"
    alert = driver.switch_to.alert
    assert(alert.text == ref_text)
    print(alert.text)
    time.sleep(1)
    alert.accept()
    time.sleep(1)
    print("Alert funkció OK.")
except:
    print("Nem egyezik a referencia szöveg.")
finally:
    pass

# -----------------------------------------
# 2. Confirmation box:

driver.refresh()
try:
    # 2/1. Az OK gombot választjuk.
    driver.find_element_by_name('confirmation').click()
    ref2_text = "I am confirm"
    conf = driver.switch_to.alert
    assert(conf.text == ref2_text)
    print(conf.text)
    time.sleep(1)
    conf.accept()
    time.sleep(1)
    print("Confirmation OK funkciója rendben.")
except:
    print("Az OK funkció nem működik megfelelően.")
finally:
    pass

driver.refresh()
try:
    # 2/2. A "Mégse" gombot választjuk.
    driver.find_element_by_name('confirmation').click()
    ref2_text = "I am confirm"
    conf = driver.switch_to.alert
    assert(conf.text == ref2_text)
    print(conf.text)
    time.sleep(1)
    conf.dismiss()           # ez az elutasítás kiválasztása
    time.sleep(1)
    print('Confirmation "Mégse" funkciója rendben.')
except:
    print('A "Mégse" funkció nem működik megfelelően.')
finally:
    pass
#    driver.close()


# -----------------------------------------
# 3. Prompt funkció:

def prompt_test_text(tx):
    try:
        ref3_text = "I am prompt"
        prom = driver.switch_to.alert
        assert(prom.text == ref3_text)
        print(prom.text)
        time.sleep(1)
        text = tx
        prom.send_keys(text)
        prom.accept()
        time.sleep(1)
        par_text = driver.find_element_by_id('demo').text
        print(par_text)
        if text == "":
            assert (par_text == "You entered:")
            print("Ha nincs szöveg bevitel, csak OK, a prompt OK funkció rendben, a p tag szöveg nélkül jelenik meg.")
        else:
            assert(par_text == f"You entered: {text}")
            print("A prompt OK funkció rendben, a p tag megjelenik, a szöveg egyezik.")
    except:
        print("A prompt OK funkció nem működik megfelelően.")
    finally:
        pass

# 3/1. Az "OK" gombot választjuk, szöveggel, vagy szöveg nélkül.
driver.refresh()
driver.find_element_by_name('prompt').click()
prompt_test_text("Hello prompt!")
driver.refresh()
driver.find_element_by_name('prompt').click()
prompt_test_text("")

def prompt_test_cans(tx2):
    try:
        ref3_text = "I am prompt"
        prom = driver.switch_to.alert
        assert(prom.text == ref3_text)
        print(prom.text)
        time.sleep(1)
        text = tx2
        prom.send_keys(text)
        prom.dismiss()
        time.sleep(1)
        par_text = driver.find_element_by_id('demo').text
        assert (par_text == "")
        print('A prompt "Mégse" funkció rendben, a p tag nem jelenik meg.')
    except:
        print("A prompt OK funkció nem működik megfelelően.")
    finally:
        pass

# 3/2. A "Mégse" gombot választjuk, szöveggel, vagy szöveg nélkül.

driver.refresh()
driver.find_element_by_name('prompt').click()
prompt_test_cans("Hello prompt!")
driver.refresh()
driver.find_element_by_name('prompt').click()
prompt_test_cans("")


# -----------------------------------------
# 4. Dupla click funkció:

driver.refresh()
try:
    dc_button = driver.find_element_by_id('double-click')
    action = ActionChains(driver)
    action.double_click(dc_button).perform()
    ref_text = "You double clicked me!!!, You got to be kidding me"
    alert = driver.switch_to.alert
    assert(alert.text == ref_text)
    print(alert.text)
    time.sleep(1)
    alert.accept()
    time.sleep(1)
    print("Double click funkció OK.")
except:
    print("A Double click funkció nem működik.")
finally:
    pass

time.sleep(1)
driver.close()

