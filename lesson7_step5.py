import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'https://suninjuly.github.io/math.html'
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    time.sleep(1)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)
    time.sleep(1)
    input2 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    input2.click()
    time.sleep(1)
    input3 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    input3.click()
    time.sleep(1)
    input4 = browser.find_element(By.CSS_SELECTOR, 'button.btn-default')
    input4.click()
    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()