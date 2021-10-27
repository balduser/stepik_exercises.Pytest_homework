from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .locators import BasePageLocators


class BasePage:
    """Базовая страница Page Object Model"""

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        """Проверяет, что ссылка на страницу логина присутствует"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        """Переход к странице логина и регистрации"""
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def go_to_basket_page(self):
        """Переход в корзину"""
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()

    def should_be_authorized_user(self):
        """Проверяет, авторизован ли пользователь, по наличию иконки пользователя"""
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented, probably unauthorised user"

    def is_element_present_implicitly(self, how, what):
        """Проверяет присутствие элемента. Рекомендуется использовать с неявным ожиданием
        (implicitly_wait())."""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_present(self, how, what, timeout=4):
        """Проверяет присутствие элемента в течение интервала timeout.
        Неявное ожидание нужно отключить."""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Проверяет, что элемента на странице нет в течение интервала timeout.
        Неявное ожидание нужно отключить."""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """Проверяет, что элемент исчезает в течение интервала timeout.
        Неявное ожидание нужно отключить."""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
