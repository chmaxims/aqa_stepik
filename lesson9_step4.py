import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/alert_accept.html')
time.sleep(2)

try:
    browser.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
    browser.switch_to.alert.accept()
    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    y = math.log(abs(12*math.sin(x)))
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
finally:
    time.sleep(5)
    browser.quit()
