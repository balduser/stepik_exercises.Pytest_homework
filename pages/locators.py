from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    registration_url = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    login_email = (By.CSS_SELECTOR, '#id_login-username')
    login_password = (By.CSS_SELECTOR, "#id_login-password")
    login_button = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    registration_email = (By.CSS_SELECTOR, '#id_registration-email')
    registration_password_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    registration_password_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    registration_button = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
