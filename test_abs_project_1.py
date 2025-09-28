import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Tests(unittest.TestCase):
    def test_first_url(self):
        try:
            link = "https://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            first = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
            first.send_keys('Max')

            second = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
            second.send_keys('Maksovich')

            mail = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
            mail.send_keys('test@gmail.com')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual('Congratulations! You have successfully registered!', welcome_text, "Приветственный текст не соответствует ожидаемому в 1ом url")

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_second_url(self):
            try:
                link = "https://suninjuly.github.io/registration2.html"
                browser = webdriver.Chrome()
                browser.get(link)

                # Ваш код, который заполняет обязательные поля
                first = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
                first.send_keys('Max')

                second = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
                second.send_keys('Maksovich')

                mail = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
                mail.send_keys('test@gmail.com')

                # Отправляем заполненную форму
                button = browser.find_element(By.CSS_SELECTOR, "button.btn")
                button.click()

                # Проверяем, что смогли зарегистрироваться
                # ждем загрузки страницы
                time.sleep(1)

                # находим элемент, содержащий текст
                welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
                # записываем в переменную welcome_text текст из элемента welcome_text_elt
                welcome_text = welcome_text_elt.text

                # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
                self.assertEqual('Congratulations! You have successfully registered!', welcome_text,
                                 "Приветственный текст не соответствует ожидаемому во 2ом url")

            finally:
                # ожидание чтобы визуально оценить результаты прохождения скрипта
                time.sleep(3)
                # закрываем браузер после всех манипуляций
                browser.quit()

if __name__ == '__main__':
    unittest.main()