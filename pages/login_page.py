from .base_page import BasePage
from .locators import *


class LoginPage(BasePage):
    """Страница логина"""

    def should_be_login_page(self):
        """Проверяет, что текущая страница - страница логина и регистрации"""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверяет, что в строке текущего url есть 'login'"""
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        """Проверяет, что на текущей странице есть поля для авторизации пользователя"""
        assert self.is_element_present(*LoginPageLocators.login_email) and \
            self.is_element_present(*LoginPageLocators.login_password) and \
            self.is_element_present(*LoginPageLocators.login_button), "Не найдена форма логина!"

    def should_be_register_form(self):
        """Проверяет, что на текущей страницы есть поля для регистрации пользователя"""
        assert self.is_element_present(*LoginPageLocators.registration_email) and \
            self.is_element_present(*LoginPageLocators.registration_password_1) and \
            self.is_element_present(*LoginPageLocators.registration_password_2) and \
            self.is_element_present(*LoginPageLocators.registration_button), "Не найдена форма регистрации!"

    def click_login_link(self):
        """Для нажатия на кнопку входа после ввода логина/пароля"""
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()

    def log_in(self, email, password):
        """Ввод пользовательских данных для авторизации"""
        self.click_login_link()
        self.browser.find_element(*LoginPageLocators.login_email).send_keys(email)
        self.browser.find_element(*LoginPageLocators.login_password).send_keys(password)
        self.browser.find_element(*LoginPageLocators.login_button).click()

    def register_new_user(self, email, password):
        """Регистрация нового пользователя"""
        self.browser.find_element(*LoginPageLocators.registration_email).send_keys(email)
        self.browser.find_element(*LoginPageLocators.registration_password_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.registration_password_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.registration_button).click()
