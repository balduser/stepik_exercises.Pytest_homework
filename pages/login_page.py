from .base_page import BasePage
from .locators import *


class LoginPage(BasePage):
    """Страница логина"""

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.login_email) and \
            self.is_element_present(*LoginPageLocators.login_password) and \
            self.is_element_present(*LoginPageLocators.login_button), "Не найдена форма логина!"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.registration_email) and \
            self.is_element_present(*LoginPageLocators.registration_password_1) and \
            self.is_element_present(*LoginPageLocators.registration_password_2) and \
            self.is_element_present(*LoginPageLocators.registration_button), "Не найдена форма регистрации!"

    def click_login_link(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()

    def log_in(self, email, password):
        self.click_login_link()
        self.browser.find_element(*LoginPageLocators.login_email).send_keys(email)
        self.browser.find_element(*LoginPageLocators.login_password).send_keys(password)
        self.browser.find_element(*LoginPageLocators.login_button).click()

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.registration_email).send_keys(email)
        self.browser.find_element(*LoginPageLocators.registration_password_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.registration_password_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.registration_button).click()
