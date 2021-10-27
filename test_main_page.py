import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        """Проверяет, что гость может перейти на страницу логина"""
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        """Проверяет, что гостю доступна ссылка на форму логина"""
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_login_form_should_be_present(self, browser):
        """Проверяет, что на странице должны быть форма логина"""
        page = LoginPage(browser, link)
        page.open()
        page.click_login_link()
        page.should_be_login_page()

@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """Проверяет, что корзина гостя пуста"""
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.basket_has_no_items()
    page.basket_is_empty_by_text()
