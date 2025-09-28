import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/execute_script.html')
time.sleep(1)

try:
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    #time.sleep(0.1)
    func1 = str(math.log(abs(12*math.sin(int(x)))))
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(func1)
    #time.sleep(0.1)
    browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()
    #time.sleep(0.1)
    browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()
    #time.sleep(0.1)
    browser.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()

finally:
    time.sleep(5)
    browser.quit()

