from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


url = 'https://stepik.org/lesson/236895/step/1'


def test_sign_in(browser, load_config):
    browser.get(url)
    login = load_config['login']
    password = load_config['password']

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth"))).click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='login']"))).send_keys(login)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[name='password']"))).send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

    WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "[data-tab-name='registration'")))


#prompt = browser.switch_to.alert
#prompt.send_keys("My answer")
#prompt.accept()