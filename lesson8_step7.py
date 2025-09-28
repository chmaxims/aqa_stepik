import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

broswer = webdriver.Chrome()
broswer.get('http://suninjuly.github.io/file_input.html')
time.sleep(1)
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
print(file_path)

try:
    broswer.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Max')
    #time.sleep(0.2)
    broswer.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Popov')
    #time.sleep(0.2)
    broswer.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('maw@mail.ru')
    #time.sleep(0.2)
    broswer.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(file_path)
    #time.sleep(0.2)
    broswer.find_element(By.CSS_SELECTOR, 'button.btn-primary').click()
    #time.sleep(0.2)

finally:
    time.sleep(5)
    broswer.quit()