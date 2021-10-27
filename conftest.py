import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose your language: ru, en, it, fr or another")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # To exclude redundant info
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nclosing browser...")
    time.sleep(3)
    browser.quit()
