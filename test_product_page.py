import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

link_1 = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
links = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{n}" for n in range(10)]

@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # To exclude redundant info
        self.browser = webdriver.Chrome(options=options)
        self.page = LoginPage(self.browser, link)
        self.page.open()
        self.page.click_login_link()
        email = str(time.time()) + "@fakemail.org"
        self.page.register_new_user(email, "biba+boba=He110nE@rth")
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        """Проверяет, что при открытии юзером страницы продукта сообщение об
        успешном добавлении не появляется"""
        self.page = ProductPage(self.browser, link)
        self.page.open()
        self.page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        """Проверяет, что название книги в каталоге соответствует названию в корзине"""
        self.page = ProductPage(self.browser, link)
        self.page.open()
        self.page.add_to_basket_and_check_name()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Проверяет, что со страницы продукта гость может перейти на страницу логина"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Проверяет, что при переходе гостя со страницы товара в корзину, корзина пуста."""
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_has_no_items()
    page.basket_is_empty_by_text()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    """Проверяет, что название книги в каталоге соответствует названию в корзине"""
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket_and_check_name()

@pytest.mark.basket
@pytest.mark.xfail(reason="Success message should certainly be present", strict=True)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Негативный тест. Проверяет, что после добавления гостем товара в корзину
    сообщение об успешном добавлении не появляется."""
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.basket
@pytest.mark.xfail(reason="Correct behavior", strict=True)
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Негативный тест. Проверяет, что после добавления гостем товара в корзину
    сообщение об успешном добавлении исчезает"""
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    """Проверяет, что на странице продукта гостю доступна ссылка на форму логина"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_success_message(browser):
    """Проверяет, что при открытии юзером страницы продукта сообщение об
    успешном добавлении не появляется"""
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_user_can_log_in(browser):
    page = LoginPage(browser, link)
    page.open()
    page.click_login_link()
    page.log_in("biba@boba.ru", "biba+boba=2")
    page.should_be_authorized_user()

def test_register_new_user(browser):
    page = LoginPage(browser, link)
    page.open()
    page.click_login_link()
    email = str(time.time()) + "@fakemail.org"
    page.register_new_user(email, "biba+boba=He110nE@rth")
    page.should_be_authorized_user()
