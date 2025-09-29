import pytest
from selenium import webdriver
import json


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="session")
def load_config():
    with open("log.json", "r") as f:
        config = json.load(f)
        return config