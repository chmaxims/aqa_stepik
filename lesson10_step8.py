import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

try:
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
    browser.find_element(By.CSS_SELECTOR, "#book").click()
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    y = math.log(abs(12*math.sin(x)))
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "#solve").click()
finally:
    time.sleep(2)
    browser.quit()