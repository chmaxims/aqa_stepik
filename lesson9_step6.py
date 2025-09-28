import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

try:
    browser.find_element(By.CSS_SELECTOR, 'button.trollface').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    y = math.log(abs(12*math.sin(x)))
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
finally:
    time.sleep(5)
    browser.quit()