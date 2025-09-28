import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('https://suninjuly.github.io/selects1.html')
time.sleep(1)

select = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))

try:
    num1 = browser.find_element(By.CSS_SELECTOR, '#num1')
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2')
    sum1 = int(num1.text) + int(num2.text)
    select.select_by_value(str(sum1))
    time.sleep(0.5)
    browser.find_element(By.CSS_SELECTOR, 'button.btn-default').click()
finally:
    time.sleep(5)
    browser.quit()


